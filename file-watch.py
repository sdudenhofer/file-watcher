import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import email_log
import fup

if __name__ == "__main__":
    logging.basicConfig(filename='logs/file_created.log', level=logging.INFO, format= '%(asctime)s %(message)s')
    #add logging to text file
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        print(f"file created: " + event.src_path)
        logging.info('file created: ' + event.src_path)
        email_log.email_log('setdud@mckweb.com', 'webadmin@mckweb.com', '', 'This is a test', 'logs/file_Created.log')
        fup.fup()
    def on_deleted(event):
        print(f"File deleted!" + event.src_path)
        logging.info('file deleted: ' + event.src_path)
    def on_modified(event):
        print(f"File Modified: "  + event.src_path)
        logging.info('file modified: ' + event.src_path)
    def on_moved(event):
        print(f"File moved: " + event.src_path)
        logging.info('file moved: ' + event.src_path)
    
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    path = "./files/"
    go_recursively = True
    observer = Observer()
    observer.schedule(event_handler, path, recursive=go_recursively)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()