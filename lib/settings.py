import xbmcaddon


class Settings:

    def __init__(self):
        self.addon = xbmcaddon.Addon()

    @property
    def manifest_url(self):
        return self.addon.getSettingString("manifest_url")