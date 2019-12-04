flake8:
	@if command -v flake8 > /dev/null; then \
		echo "Running flake8"; \
		python -m flake8 `find . -name \*.py | grep -v setup.py | grep -v /doc/ | grep -v __init__.py`; \
	else \
		echo "flake8 not found, please install it!"; \
		exit 1; \
	fi;
	@echo "flake8 passed"

test:
	python -m pytest -v --pyargs lrspectrum --cov-report term-missing --cov=lrspectrum 
