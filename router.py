from urllib.parse import urlencode

import xbmc
import xbmcgui
import xbmcplugin

from lib.logger import Logger
from lib.settings import Settings


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

        xbmc.log("[AIOBridge] Router.run() started", xbmc.LOGINFO)

        try:
            xbmc.log("[AIOBridge] Creating Settings()", xbmc.LOGINFO)
            settings = Settings()

            xbmc.log("[AIOBridge] Reading manifest_url", xbmc.LOGINFO)
            manifest = settings.manifest_url

            xbmc.log(f"[AIOBridge] Manifest: {manifest}", xbmc.LOGINFO)

            Logger.info("Settings loaded correctly")

        except Exception:
            import traceback

            xbmc.log(
                "[AIOBridge] Exception:\n" + traceback.format_exc(),
                xbmc.LOGERROR,
            )

        self.add_folder("Film", "movies")
        self.add_folder("Serie TV", "series")
        self.add_folder("Settings", "settings")
        self.add_folder("About", "about")

        xbmcplugin.endOfDirectory(self.handle)

        xbmc.log("[AIOBridge] Router.run() finished", xbmc.LOGINFO)