P = python
backup = backup/

all:
	$(P) main.py

dev:
	$(P) -m unittest tests/*.py
	$(P) hot_reload.py

build:
	pyinstaller main.py
	cd dist/main && ./main

fresh:
	rm -f *.db
	rm -rf __pycache__
	$(P) hot_reload.py

freshbuild:
	rm -f *.spec
	rm -rf __pycache__
	rm -rf build
	rm -rf dist

test:
	$(P) -m unittest tests/*.py

db:
	$(P) init_db.py

backup: .FORCE
	mkdir -p $(backup)
	cp *.db $(backup)
	cp *.csv $(backup)

.FORCE:

.PHONY: backup