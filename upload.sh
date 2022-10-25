# only for the author, uploads the module to pypi
python -m build
twine upload dist/*