import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
from desktop_cleaner import cleaner
import yaml

class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(event.src_path)
            cleaner()

         

event_handler = EventHandler()
observer = Observer()
with open('config.yml') as file:
    list = yaml.load(file, Loader=yaml.FullLoader)
path = list['path']
observer.schedule(event_handler,path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()            