from pathlib import Path
from zipfile import ZipFile

# compress files
with ZipFile("files.zip", "w") as zip:
    # because rglob returns an object generator, we iterate over each with for loop
    # *.* = all types of files
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

# read files
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
