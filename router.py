from urllib.parse import urlencode, parse_qs

import xbmcplugin
import xbmcgui

from lib.controller import Controller


class Router:

    def __init__(self, argv):
        self.argv = argv
        self.handle = int(argv[1])

    def build_url(self, query):
        return f"{self.argv[0]}?{urlencode(query)}"

    def add_folder(self, label, action):

        item = xbmcgui.ListItem(label=label)

        xbmcplugin.addDirectoryItem(
            handle=self.handle,
            url=self.build_url({"action": action}),
            listitem=item,
            isFolder=True,
        )

    def run(self):

        params = parse_qs(self.argv[2][1:])
        action = params.get("action", [None])[0]

        controller = Controller()

        if action == "movies":
            controller.movies()
            xbmcplugin.endOfDirectory(self.handle)
            return

        elif action == "series":
            controller.series()
            xbmcplugin.endOfDirectory(self.handle)
            return

        elif action == "settings":
            controller.settings()
            xbmcplugin.endOfDirectory(self.handle)
            return

        elif action == "about":
            controller.about()
            xbmcplugin.endOfDirectory(self.handle)
            return

        # Menu principale
        self.add_folder("Film", "movies")
        self.add_folder("Serie TV", "series")
        self.add_folder("Settings", "settings")
        self.add_folder("About", "about")

        xbmcplugin.endOfDirectory(self.handle)