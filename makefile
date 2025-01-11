all:
	python main.py

dev:
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

db:
	python init_db.py

clean:
	rm -f *.db
	rm -rf __pycache__

backup:
	mkdir -p backup
	cp *.db backup/