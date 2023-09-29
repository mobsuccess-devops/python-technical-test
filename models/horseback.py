import json


class Horseback:
    date: str
    place: str
    discipline: str
    category: str
    ranking: str

    @property
    def points(self) -> int:
        """Calculs the points earned for this instance."""
        # To be implemented
        return 0

    def to_json(self):
        """Returns the JSON representation."""

        def get_object_dict(obj):
            d = obj.__dict__.copy()
            for key, value in obj.__class__.__dict__.items():
                if isinstance(value, property):
                    d[key] = getattr(obj, key)
            return d

        return json.dumps(self, default=lambda o: get_object_dict(o))
