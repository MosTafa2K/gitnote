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
        ConnectionError,
        ConnectTimeout,
    ):
        print("Connection Error: Please check your internet connection and try again.")
        return False
    except (
        HTTPError,
        BadRequestError,
        LocalTokenNotFoundError,
    ):
        print(
            "Invalid user token.\nPlease provide a valid token using command `gitnote set-token <token>`."
        )
        return False
