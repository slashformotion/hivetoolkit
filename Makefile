test:
	python -m unittest discover  tests

testv:
	python -m unittest -v discover  tests

black:
	black .

send:
	twine upload dist/*

wheel:
	python3 setup.py sdist bdist_wheel