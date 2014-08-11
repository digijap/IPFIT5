import zipfile

zf = zipfile.ZipFile("/home/jasper/key.zip",  "r")
print zf.namelist()
