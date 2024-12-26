init:
	pip3 install -r requirements.txt
test:
	python3 -m pytest -o log_cli=true
test-capture:
	python3 -m pytest -o log_cli=true -s

.PHONY: init test