import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.start_app()

    def start_app(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(["python", self.script_name])

    def on_modified(self, event):
        # Only track Python files under the frontend directory
        if event.src_path.endswith(".py") and "frontend/" in event.src_path:
            print(f"Change detected in {event.src_path}. Restarting app...")
            self.start_app()


if __name__ == "__main__":
    script_to_run = "main.py"
    event_handler = ReloadHandler(script_to_run)
    observer = Observer()
    # Watch the frontend directory for changes in Python files
    observer.schedule(event_handler, path="frontend/", recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
