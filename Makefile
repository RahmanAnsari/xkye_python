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
	@pytest -vvv

dev: clean
	@pip3 install -r requirements.txt

lint: clean
	@printf "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@black xkye
	@printf "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8
	@printf "\n${BLUE}Running Bandit against source files...${NC}\n"
	@bandit -r --ini setup.cfg
	@printf "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@pylint --rcfile=setup.cfg **/*.py

dist: clean
	@pip3 install -r requirements.txt
	@python3 setup.py sdist
	@python3 setup.py bdist_wheel

version: dist
	@python3 setup.py --version

license: dist
	@python3 setup.py --license

testpy:	dist
	@python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

deploy: dist
	@python3 -m twine upload dist/*
