from typing import Tuple, Union
from src.db import insert_credentials
from src.models import ErrorResponse, ServerResponse, UserAuth


async def check_login(user, password):
    return True, "someRandomSessionId"


async def create_user(info: UserAuth, api_key: str) -> Union[ServerResponse, ErrorResponse]:
    """
    returns [success, message]
    """

    # TODO: Check api_key

    username = info.username
    password = info.password
    id = await insert_credentials(username, password)

    if id == -1:
        return ErrorResponse(message="Failed to add user", code=0)

    return ServerResponse(message="Success", code=1)
