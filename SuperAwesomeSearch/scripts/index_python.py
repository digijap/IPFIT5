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

revfile = None
if len(sys.argv) > 3:
    revfile = sys.argv[3]

title_re = re.compile("^\s*((\w|[:]).*?)\n[-*=#+%]{3,}$", re.MULTILINE)
charclass_re = re.compile(":(?P<cls>[^:]+):`~?(?P<ref>[^`\n]+)`", re.MULTILINE)
def_re = re.compile("^[.][.] ?([^:]+):: (.*?)$", re.MULTILINE)

deffields = {"class": "cls", "module": "mod"}
reffields = {"mod": "modref", "class": "clsref", "func": "funcref", "pep": "pep"}

ana = analysis.StemmingAnalyzer(stoplist=stoplists["en"], maxsize=40)

cls_ana = (analysis.SpaceSeparatedTokenizer()
           | analysis.IntraWordFilter(mergewords=True)
           | analysis.LowercaseFilter())

tech_ana = (analysis.RegexTokenizer("\w+")
            | analysis.LowercaseFilter())


class PydocSchema(fields.SchemaClass):
    path = fields.STORED

    title = fields.TEXT(stored=True, sortable=True, spelling=True, analyzer=ana)
    tgrams = fields.NGRAMWORDS

    content = fields.TEXT(spelling=True, analyzer=ana)

    chapter = fields.ID(sortable=True)

    size = fields.NUMERIC(sortable=True)
    rev = fields.NUMERIC(sortable=True)
    revised = fields.DATETIME(sortable=True)

    modref = fields.TEXT(analyzer=tech_ana, phrase=False)
    clsref = fields.TEXT(analyzer=tech_ana, phrase=False)
    funcref = fields.TEXT(analyzer=tech_ana, phrase=False)
    pep = fields.TEXT(analyzer=tech_ana, phrase=False)

    cls = fields.TEXT(analyzer=cls_ana)
    mod = fields.TEXT(analyzer=tech_ana, phrase=False)


rev_data = {}
if revfile:
    t = now()
    with open(revfile, "rb") as f:
        for line in f:
            filename, timestr, tzstr, revnum = line.strip().split()
            dt = datetime.datetime.fromtimestamp(int(timestr))
            rev_data[filename] = (dt, int(revnum))
    print now() - t


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

                defs = defaultdict(list)
                for match in def_re.finditer(data):
                    prop = match.group(1).lower()
                    name = match.group(2)
                    if prop in deffields:
                        defs[deffields[prop]].append(name)
                defs = dict((k, " ".join(v)) for k, v in defs.iteritems())

                refs = defaultdict(list)
                for match in charclass_re.finditer(data):
                    prop = match.group("cls").lower()
                    ref = match.group("ref")
                    if prop in reffields:
                        refs[reffields[prop]].append(ref)
                refs = dict((k, " ".join(v)) for k, v in refs.iteritems())

                extras = {}
                extras.update(refs)
                extras.update(defs)

                data = charclass_re.sub("\g<ref>", data)

                title = None
                title_match = title_re.search(data)
                if title_match:
                    title = title_match.group(1)

                if filepath in rev_data:
                    revdate, revnum = rev_data[filepath]
                else:
                    revdate = revnum = None

                path = filepath[len(sourcedir):]

                w.add_document(path=path,
                               title=title, tgrams=title,
                               content=data,
                               chapter=chapter,
                               size=size,
                               rev=revnum, revised=revdate,
                               **extras)

    print "-", now() - t

print now() - t

