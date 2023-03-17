from typing import Tuple, Union
from pathlib import Path


async def parser(path: str) -> Tuple[int, Union[str, None]]:
    if not Path(path).exists():
        return -1, "Invalid path"
    return 1, None
