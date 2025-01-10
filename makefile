all:
	python hot_reload.py

main:
	python main.py

db:
	python init_db.py

clean:
	rm -f *.db
	rm -rf __pycache__