from pydantic import BaseModel


class CausalChain(BaseModel):

    chain: list[str]