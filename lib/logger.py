import xbmc


class Logger:

    @staticmethod
    def info(message):
        xbmc.log(f"[AIOBridge] {message}", xbmc.LOGINFO)

    @staticmethod
    def error(message):
        xbmc.log(f"[AIOBridge] {message}", xbmc.LOGERROR)

    @staticmethod
    def warning(message):
        xbmc.log(f"[AIOBridge] {message}", xbmc.LOGWARNING)