import pyinotify
import os
from .aWebSiteEventHandler import WebSiteEventHandler
from .config import WATCH_DIR,WATCH_FLAG_ACCESS

def get_watch_dir(dir_entry, result=[]):
    result.append(dir_entry)
    watch_entry = os.listdir(dir_entry)
    for i in watch_entry:
        i = os.path.join(dir_entry, i)
        if os.path.isdir(i):
            get_watch_dir(i, result)
    return result


def main():
    wm = pyinotify.WatchManager()

    dir_list = get_watch_dir(WATCH_DIR)
    # watch_entry.append(WATCH_DIR)
    for i in dir_list:
        wm.add_watch(i, pyinotify.ALL_EVENTS, rec=True)
    if os.path.isfile(WATCH_FLAG_ACCESS):
        wm.add_watch(WATCH_FLAG_ACCESS, pyinotify.ALL_EVENTS, rec=True)
    eh = WebSiteEventHandler()
    notifier = pyinotify.Notifier(wm, eh)

    notifier.loop()


if __name__ == '__main__':
    print(os.getcwd())
    main()
