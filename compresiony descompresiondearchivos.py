#zip
import zipfile
from zipfile import ZipFile

with zipfile.ZipFile('zip.zip','w') as fzip:
    fzip.write('Python.docx')
    fzip.write('Archivo.docx')
    fzip.write('pythonl.jpg')
    fzip.printdir()
    fzip.extractall()

#gzip
import gzip
with open('Python.docx','rb') as original:
    with gzip.open('archivo.txt.gz','wb') as archivo1:# aca se hace la compresion del archivo
        archivo1.writelines(original)

#bzip
import bz2

cadena=b"Cadena Cadena Cadena Cadena"
cadena_c=bz2.compress(cadena)

print(cadena_c)
print(bz2.decompress(cadena_c))

#compromiendo con tarball
import tarfile
archivotar=tarfile.open('primer.tar.gz','w:gz')
archivotar.add('Python.docx')
archivotar.add('pythonl.jpg')
archivotar.add('Archivo.docx')
archivotar.close

print(archivotar)
