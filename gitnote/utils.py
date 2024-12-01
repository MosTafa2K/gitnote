from huggingface_hub import HfApi
from huggingface_hub.errors import (
    BadRequestError,
    LocalTokenNotFoundError,
)
from requests import HTTPError
from requests.exceptions import ConnectionError, ConnectTimeout


def validate_token(token: str) -> bool:
    api = HfApi()
    try:
        api.whoami(token)
        return True
    except (
        BadRequestError,
        LocalTokenNotFoundError,
        HTTPError,
    ):
        print(
            "Token is required or provided token is invalid!\n\
Please provide a valid token using `gitnote setapikey <token>` command."
        )
        return False
    except (
        ConnectionError,
        ConnectTimeout,
    ):
        print("Connection Error! Please check your internet connection and try again.")
        return False
