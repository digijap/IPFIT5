import os
import time

from whoosh import analysis, fields, index
from whoosh.lang.stopwords import stoplists
from whoosh.util import now

sourcedir = raw_input("Wat moet er geindexd worden?\n")
indexdir = '/home/jasper/SuperAwesomeSearch/index'

ana = analysis.StemmingAnalyzer(stoplist=stoplists["en"], maxsize=40)




class PydocSchema(fields.SchemaClass):

    path = fields.STORED

    title = fields.TEXT(stored=True, sortable=True, spelling=True, analyzer=ana)
    tgrams = fields.NGRAMWORDS

    ext = fields.TEXT(stored=True, sortable=True)

    content = fields.TEXT(spelling=True, analyzer=ana)

    chapter = fields.ID(sortable=True)

    size = fields.NUMERIC(sortable=True)

    lastopened = fields.TEXT(sortable=True)

    lastchanged = fields.TEXT(sortable=True)

    created = fields.TEXT(sortable=True)


ix = index.create_in(indexdir, PydocSchema)
with ix.writer(limitmb=2048) as w:
    t = now()
    for dirpath, dirnames, filenames in os.walk(sourcedir):
        chapter = unicode(os.path.basename(dirpath))
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            size = os.path.getsize(filepath)

            path = dirpath

            fileName, fileExt = os.path.splitext(filename)
            fileName = unicode(fileName, errors='ignore')
            fileExt = unicode(fileExt, errors='ignore')
            data = None

            lasto = time.ctime(os.stat(filepath).st_atime)
            lasto = unicode(lasto[4:])

            lasta = time.ctime(os.stat(filepath).st_mtime)
            lasta = unicode(lasta[4:])

            created = time.ctime(os.stat(filepath).st_ctime)
            created = unicode(created[4:])


            w.add_document(path=path,
                            title=fileName, tgrams=fileName,
                            ext=fileExt,
                            content=data,
                            chapter=chapter,
                            size=size,
                            lastopened=lasto,
                            lastchanged=lasta,
                            created=created)

    print "-", now() - t

print now() - t

os.system("python ~/SuperAwesomeSearch/present.py")
