install: venv
	./venv/bin/pip3 install -r requirements.txt
	./venv/bin/pip3 install -e .

venv:
	python3 -m venv venv	

.PHONY: test
test: setup
	./venv/bin/pytest ./test

.PHONY: setup
setup:
	./venv/bin/python3 setup.py install
