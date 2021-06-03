.PHONY: clean-pyc

default: test

clean-pyc:
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete

clean-dist:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info

clean: clean-pyc clean-dist

test:
	pytest -vvv

dev: clean
	pip3 install -r requirements.txt

dist: clean
	pip3 install -r requirements.txt
	python3 setup.py sdist
	python3 setup.py bdist_wheel

version: dist
	python3 setup.py --version

license: dist
	python3 setup.py --license

