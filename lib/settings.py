import xbmc
import xbmcaddon


class Settings:

    def __init__(self):
        xbmc.log("[AIOBridge] Creating Addon()", xbmc.LOGINFO)
        self.addon = xbmcaddon.Addon()
        xbmc.log("[AIOBridge] Addon created", xbmc.LOGINFO)

    @property
    def manifest_url(self):
        xbmc.log("[AIOBridge] Reading manifest_url", xbmc.LOGINFO)
        value = self.addon.getSettingString("manifest_url")
        xbmc.log(f"[AIOBridge] Value={value}", xbmc.LOGINFO)
        return value