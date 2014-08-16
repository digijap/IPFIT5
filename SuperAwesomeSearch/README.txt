$pip install whoosh
$pip install Flask
$pip install mako

download vanaf https://github.com/tzellman/flask-mako/archive/master.zip
$python flask-mako-master/setup.py install


--------------------------------------------------------------------
Volgende stappen gebeuren allemaal in de map /SuperAwesomeSearch map
--------------------------------------------------------------------

$hg clone http://hg.python.org/cpython

$python scripts/list_revisions.py cpython/Doc > revs.txt
$mkdir index
$python scripts/index_python.py cpython/Doc index revs.txt

$export SOURCE=cpython/Doc
$export INDEX=index

$python present.py

Nu runt de search engine op 127.0.0.1:5000