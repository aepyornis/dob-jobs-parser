install: venv
	./venv/bin/pip3 install -r requirements.txt

venv:
	python3 -m venv venv	

.PHONY: test
test:
	./venv/bin/pytest ./test

.PHONY: setup
setup:
	./venv/bin/python3 setup.py install
