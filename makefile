all:
	python main.py

dev:
	python -m unittest tests/*.py
	python hot_reload.py

build:
	pyinstaller main.py
	cd dist/main && ./main

fresh:
	rm -f *.db
	rm -rf __pycache__
	python hot_reload.py

freshbuild:
	rm -f *.spec
	rm -rf __pycache__
	rm -rf build
	rm -rf dist

test:
	python -m unittest tests/*.py

db:
	python init_db.py

backup:
	mkdir -p backup
	cp *.db backup/