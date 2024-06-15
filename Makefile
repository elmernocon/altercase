PYTHON := python

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

install:
	$(PYTHON) -m pip install .

clean:
	rm -vrf ./build ./dist ./**/*.egg-info ./**/*.pyc

build-image: clean
	docker buildx build --tag elmernocon/altercase:latest .
