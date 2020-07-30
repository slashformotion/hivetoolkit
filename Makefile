test:
	python -m unittest discover  tests

testv:
	python -m unittest -v discover  tests

black:
	black .