import json
from datetime import datetime


def serialize_event(event):

    def default_serializer(obj):

        if isinstance(obj, datetime):

            return obj.isoformat()

        return str(obj)

    return json.dumps(
        event,
        default=default_serializer
    ).encode("utf-8")