.PHONY: install install_dev install_test clean
install:
	pip install -e .

install_dev:
	pip install -e '.[dev]'

install_test:
	pip install -e '.[test]'

clean:
	@find ./ -name '*pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .build
	@rm -rf .dist
	@rm -rf .*.egg-info
	@rm -rf .htmlcov
	@rm -rf .tox/
	@rm -rf .doces/_build