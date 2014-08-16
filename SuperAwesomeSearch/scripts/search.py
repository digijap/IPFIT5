import sys
import argparse

from whoosh import index, qparser

parser = argparse.ArgumentParser()
parser.add_argument("query")
args = parser.parse_args()

print args.group

indexdir = "/home/jasper/whoosh/index"

qs = " ".join(sys.argv[1:])

ix = index.open_dir(indexdir)
with ix.searcher() as s:
    q = qparser.QueryParser("body", ix.schema).parse(qs)
    r = s.search(q, limit=None)
    for hit in r:
        print hit["subject"]
    print r.runtime
