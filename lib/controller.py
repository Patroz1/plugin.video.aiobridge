from lib.api import API
from lib.settings import Settings

import xbmcgui


class Controller:

    def movies(self):

        settings = Settings()

        api = API("https://aiostreamsfortheweebsstable.midnightignite.me/stremio/734da09a-a865-4665-9564-fadb76d263ac/eyJpIjoiSHJnNldweHRLeHNrVlN1bjF2OWEydz09IiwiZSI6InZnQ2UzMW4wQ1haV09aOXFEQWdEN2ZpcXVRUWtKMTNMNmNBOE1DVThKakU9IiwidCI6ImEifQ/manifest.json")

        manifest = api.get_manifest()

        if manifest is None:

            xbmcgui.Dialog().ok(
                "AIOBridge",
                "Impossibile leggere il Manifest."
            )

            return

        name = manifest.get("name", "Unknown")
        version = manifest.get("version", "Unknown")
        catalogs = len(manifest.get("catalogs", []))

        xbmcgui.Dialog().ok(
            "AIOBridge",
            f"Addon: {name}\n"
            f"Version: {version}\n"
            f"Cataloghi: {catalogs}"
        )

    def series(self):
        xbmcgui.Dialog().ok("AIOBridge", "Serie TV")

    def settings(self):
        xbmcgui.Dialog().ok("AIOBridge", "Settings")

    def about(self):
        xbmcgui.Dialog().ok("AIOBridge", "Versione 0.1")