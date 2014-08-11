import zipfile

#Open zipfile en show content
zf = zipfile.ZipFile("/home/jasper/key.zip",  "r")
print zf.namelist()
