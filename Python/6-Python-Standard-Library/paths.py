from pathlib import Path

path = Path("ecommerce")

for p in path.iterdir():
    print(p)

# or use a list comprehension
paths = [p for p in path.iterdir() if p.is_dir()]
print("directories: ", str(paths))

# but if you wanna search with filters do:
py_files = [p for p in path.glob('*.py')]
print("files: ", str(py_files))

# but if you wanna search recursively do:
py_files = [p for p in path.rglob('*.py')]
print("all files recursively with their children: ", str(py_files))
