from collections import deque
from datetime import datetime
from datetime import timedelta


class AggregationWindow:

    def __init__(
        self,
        minutes: int = 5
    ):

        self.window = deque()

        self.duration = timedelta(
            minutes=minutes
        )

    def add(
        self,
        event
    ):

        now = datetime.utcnow()

        self.window.append(
            (now, event)
        )

        self._cleanup()

    def _cleanup(self):

        cutoff = (
            datetime.utcnow()
            - self.duration
        )

        while (
            self.window
            and self.window[0][0]
            < cutoff
        ):
            self.window.popleft()

    def size(
        self
    ) -> int:

        self._cleanup()

        return len(
            self.window
        )

    def events(
        self
    ):

        self._cleanup()

        return [
            e
            for _, e
            in self.window
        ]