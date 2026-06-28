import sys
import xbmc

from router import Router


def main():
    xbmc.log("[AIOBridge] Starting addon", xbmc.LOGINFO)
    Router(sys.argv).run()


if __name__ == "__main__":
    main()