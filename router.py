from lib.logger import Logger
from lib.settings import Settings
import sys
from urllib.parse import urlencode

import xbmcgui
import xbmcplugin


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

        settings = Settings()

        Logger.info(f"Manifest URL: {settings.manifest_url}")

        self.add_folder("🎬 Film", "movies")

        self.add_folder("📺 Serie TV", "series")

        self.add_folder("⚙️ Settings", "settings")

        self.add_folder("ℹ️ About", "about")

        xbmcplugin.endOfDirectory(self.handle)