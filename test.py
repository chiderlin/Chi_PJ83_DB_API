# with open('2020-11-20_134018_Log.7z','rb') as f:
#     print(f.read())

# import py7zr

# with py7zr.SevenZipFile('2020-11-20_134018_Log.7z','r') as z:
#     print(z.read()) #解壓縮而已
# import zipfile
# with zipfile.ZipFile('2020-11-20_134018_Log.7z', 'r') as z:
#     print(z.read())

 
# import binascii 

filename = '2020-11-20_134018_Log.7z'
with open('2020-11-20_134018_Log.7z','rb') as f:
    binary = f.read()