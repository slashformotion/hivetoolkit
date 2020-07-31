test:
	python -m unittest discover  tests

testv:
	python -m unittest discover tests -v -f

black:
	black .

send:
	twine upload dist/*

wheel:
	python3 setup.py sdist bdist_wheel


clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {} 

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

todo:
	@code TODO.todo