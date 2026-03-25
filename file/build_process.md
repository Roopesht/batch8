This document outlines the build process for setting up this common module repo.


1. Add setup.py, update the required fields
2. Add project.toml, and update the required fields, make sure both in setup.py and toml set the same version number.
3. Add the required files to the repo
4. Add the __init__.py to the required folders
5. install build
   python -m pip install --upgrade build


Run the below commands

1. python -m build
2. python -m twine upload dist/* --verbose -u roopesht -p A$nme#$%

This will upload the package to pypi.org
