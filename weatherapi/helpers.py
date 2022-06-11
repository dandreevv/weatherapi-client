from http import HTTPStatus
from typing import Final

import httpx

from .enteties import ErrorCode
from .exceptions import (
    APIKeyInvalid,
    WeatherAPIException,
    APIKeyDisabled,
    APIKeyLimit,
    LocationNotFound,
    InternalError,
)

__all__ = (
    "raise_response_error",
)

ERROR_CODE_TO_EXCEPTION: Final = {
    ErrorCode.API_KEY_INVALID: APIKeyInvalid,
    ErrorCode.API_KEY_DISABLED: APIKeyDisabled,
    ErrorCode.REQUESTS_LIMIT: APIKeyLimit,
    ErrorCode.LOCATION_NOT_FOUND: LocationNotFound,
    ErrorCode.INTERNAL_ERROR: InternalError,
}


def raise_response_error(response: httpx.Response) -> None:
    if response.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNAUTHORIZED,
        HTTPStatus.FORBIDDEN,
    ):
        payload = response.json()
        error_code = payload["error"]["code"]
        exception = ERROR_CODE_TO_EXCEPTION[error_code]
        raise exception(payload["error"]["message"])
    message = f"WeatherAPI responded with {response.status_code}"
    raise WeatherAPIException(message)
