from abc import ABC
from abc import abstractmethod


class BasePersistenceHandler(
    ABC
):

    @abstractmethod
    async def persist(
        self,
        payload: dict,
    ) -> None:
        pass