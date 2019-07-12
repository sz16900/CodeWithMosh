from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path. unlink()
# print(path.stat())
# for human time
# print(ctime(path.stat().st_ctime))

# path.read_bytes()
# path.read_text()
# path.write_text()
# path.write_bytes()

# for copying a file you could do this:
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"
# target.write_text(source.read_text())

# but a better way to do this is:
shutil.copy(source, target)
