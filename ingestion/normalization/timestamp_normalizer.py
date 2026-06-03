from datetime import datetime, timezone


def normalize_timestamp(timestamp):

    try:

        if isinstance(timestamp, datetime):

            return timestamp.astimezone(
                timezone.utc
            ).isoformat()

        if isinstance(timestamp, (int, float)):

            return datetime.fromtimestamp(
                timestamp,
                tz=timezone.utc
            ).isoformat()

        if isinstance(timestamp, str):

            parsed = datetime.fromisoformat(
                timestamp.replace("Z", "+00:00")
            )

            return parsed.astimezone(
                timezone.utc
            ).isoformat()

    except Exception:

        return datetime.utcnow().replace(
            tzinfo=timezone.utc
        ).isoformat()

    return datetime.utcnow().replace(
        tzinfo=timezone.utc
    ).isoformat()