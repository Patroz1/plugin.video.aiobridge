import json
import urllib.request
import urllib.error

from lib.logger import Logger


class API:

    def __init__(self, manifest_url):
        self.manifest_url = manifest_url

    def get_manifest(self):

        Logger.info(f"Downloading manifest: {self.manifest_url}")

        try:

            with urllib.request.urlopen(self.manifest_url, timeout=15) as response:

                data = response.read().decode("utf-8")

            Logger.info("Manifest downloaded successfully")

            return json.loads(data)

        except urllib.error.HTTPError as e:

            Logger.error(f"HTTP Error: {e.code}")

        except urllib.error.URLError as e:

            Logger.error(f"URL Error: {e.reason}")

        except json.JSONDecodeError:

            Logger.error("Invalid JSON")

        except Exception as e:

            Logger.error(str(e))

        return None