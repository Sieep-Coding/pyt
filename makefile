all:
	python main.py

dev:
	python hot_reload.py

build:
	pyinstaller main.py

fresh:
	rm -f *.db
	rm -rf __pycache__
	python hot_reload.py

db:
	python init_db.py

clean:
	rm -f *.db
	rm -rf __pycache__