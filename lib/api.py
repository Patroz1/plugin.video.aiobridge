import json
import urllib.request


class API:

    def __init__(self, manifest_url):
        self.manifest_url = manifest_url

    def get_manifest(self):

        with urllib.request.urlopen(self.manifest_url, timeout=15) as response:
            data = response.read().decode("utf-8")

        return json.loads(data)