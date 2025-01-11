from backend.database import init_database
from frontend.gui import create_gui

if __name__ == "__main__":
    init_database()
    create_gui()
