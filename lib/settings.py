import xbmc
import xbmcaddon


class Settings:

    def __init__(self):
        xbmc.log("[AIOBridge] Creating Settings()", xbmc.LOGINFO)

        self.addon = xbmcaddon.Addon("plugin.video.aiobridge")

        xbmc.log("[AIOBridge] Addon object created", xbmc.LOGINFO)

    @property
    def manifest_url(self):
        value = self.addon.getSettingString("manifest_url")
        xbmc.log(f"[AIOBridge] Manifest URL = {value}", xbmc.LOGINFO)
        return value