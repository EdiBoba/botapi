from botapi.viber.utils.exceptions import ApiViberException, ApiHttpException, \
    ApiInvalidJsonException
from botapi.viber.utils.helpers import get_status_description


async def check_response(method, response) -> dict:
    """
    Checks response after request before response is closes

    :param method: api method
    :param response: response from api request
    :return: dict - response json
    :raises: ApiHttpException if response code not 200
    :raises: ApiInvalidJsonException if response not contain json body
    :raises: ApiViberException if json response contain viber api error
    """
    try:
        response_json = await response.json()
    except ValueError:
        if response.status != 200:
            raise ApiHttpException(
                response.status,
                response.reason,
                await response.text()
            )
        else:
            raise ApiInvalidJsonException(await response.text())
    else:
        if response_json['status'] != 0:
            raise ApiViberException(
                method,
                get_status_description(response_json['status'])
            )
        return response_json
