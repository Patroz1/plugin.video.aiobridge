class Catalog:

    def __init__(
        self,
        catalog_id,
        catalog_type,
        name,
        extra=None,
    ):
        self.id = catalog_id
        self.type = catalog_type
        self.name = name
        self.extra = extra or []

    def __repr__(self):
        return (
            f"Catalog("
            f"id={self.id}, "
            f"type={self.type}, "
            f"name={self.name})"
        )