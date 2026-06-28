from lib.models import Catalog


class ManifestParser:

    def __init__(self, manifest):
        self.manifest = manifest

    def catalogs(self):

        catalogs = []

        for item in self.manifest.get("catalogs", []):

            catalogs.append(

                Catalog(
                    catalog_id=item.get("id"),
                    catalog_type=item.get("type"),
                    name=item.get("name", "Unknown"),
                    extra=item.get("extra", []),
                )

            )

        return catalogs