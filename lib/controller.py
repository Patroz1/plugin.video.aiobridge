from lib.api import API
from lib.parser import ManifestParser
from lib.settings import Settings

import xbmcgui


class Controller:

    def movies(self):

        settings = Settings()

        api = API(settings.manifest_url)

        manifest = api.get_manifest()

        if manifest is None:

            xbmcgui.Dialog().ok(
                "AIOBridge",
                "Impossibile leggere il Manifest."
            )

            return

        parser = ManifestParser(manifest)

        catalogs = parser.catalogs()

        if not catalogs:

            xbmcgui.Dialog().ok(
                "AIOBridge",
                "Nessun catalogo trovato."
            )

            return

        text = ""

        for catalog in catalogs:

            icon = "🎬"

            if catalog.type == "series":
                icon = "📺"

            text += f"{icon} {catalog.name}\n"

        xbmcgui.Dialog().ok(
            "Cataloghi trovati",
            text
        )

    def series(self):
        xbmcgui.Dialog().ok("AIOBridge", "Serie TV")

    def settings(self):
        xbmcgui.Dialog().ok("AIOBridge", "Settings")

    def about(self):
        xbmcgui.Dialog().ok("AIOBridge", "Versione 0.1")