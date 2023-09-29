import json


class Horse:
    """Represent the Horse entity"""

    name: str
    horsebacks: list

    def __init__(self):
        self.horsebacks = []

    def to_json(self):
        """Returns the JSON representation."""

        def get_object_dict(obj):
            d = obj.__dict__.copy()
            for key, value in obj.__class__.__dict__.items():
                if isinstance(value, property):
                    d[key] = getattr(obj, key)
            return d

        return json.dumps(self, default=lambda o: get_object_dict(o))
