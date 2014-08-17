import sys
import os.path
import datetime
import re
from collections import defaultdict

from whoosh import analysis, fields, index
from whoosh.lang.stopwords import stoplists
from whoosh.util import now

sourcedir = os.path.abspath(sys.argv[1])
indexdir = os.path.abspath(sys.argv[2])

title_re = re.compile("^\s*((\w|[:]).*?)\n[-*=#+%]{3,}$", re.MULTILINE) #^\s elke spatie aan het begin van de line. 

ana = analysis.StemmingAnalyzer(stoplist=stoplists["en"], maxsize=40)

class PydocSchema(fields.SchemaClass):
    path = fields.STORED

    title = fields.TEXT(stored=True, sortable=True, spelling=True, analyzer=ana)
    tgrams = fields.NGRAMWORDS

    content = fields.TEXT(spelling=True, analyzer=ana)

    chapter = fields.ID(sortable=True)

    size = fields.NUMERIC(sortable=True)


ix = index.create_in(indexdir, PydocSchema)
with ix.writer(limitmb=2048) as w:
    t = now()
    for dirpath, dirnames, filenames in os.walk(sourcedir):
        chapter = unicode(os.path.basename(dirpath))
        for filename in filenames:
            if not filename.endswith(".rst"):
                continue

            filepath = os.path.join(dirpath, filename)
            size = os.path.getsize(filepath)

            print filepath
            with open(filepath, "rb") as f:
                data = f.read().decode("utf-8")

                revdate = revnum = None

                path = filepath[len(sourcedir):]
                
                title_match = title_re.search(data)
                if title_match:
                    title = title_match.group(1)

                w.add_document(path=path,
                               title=title, tgrams=title,
                               content=data,
                               chapter=chapter,
                               size=size)

    print "-", now() - t

print now() - t
