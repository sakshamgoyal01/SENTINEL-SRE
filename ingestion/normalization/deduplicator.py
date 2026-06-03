import hashlib


seen_events = set()


def is_duplicate(event: dict):

    event_hash = hashlib.md5(

        str(event).encode()

    ).hexdigest()

    if event_hash in seen_events:

        return True

    seen_events.add(event_hash)

    return False