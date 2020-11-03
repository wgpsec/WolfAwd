import pyinotify
import os
from .WebSiteEventHandler import WebSiteEventHandler

WATCH_DIR = os.getcwd()+'/defense_inotify/www'


def main():
    wm = pyinotify.WatchManager()
    wm.add_watch(WATCH_DIR, pyinotify.ALL_EVENTS, rec=True)

    eh = WebSiteEventHandler()
    notifier = pyinotify.Notifier(wm, eh)

    notifier.loop()


if __name__ == '__main__':
    print(os.getcwd())
    main()
