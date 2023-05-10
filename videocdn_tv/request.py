import json
from json import JSONDecodeError
from typing import Any, Optional, Union

import requests

from videocdn_tv.exception import ApiFailedError, ApiTokenInvalidError
from videocdn_tv.params import ParamsContent, ParamsEpisode, ParamsSeason


def get_request(
    self,
    link: str,
    params: Optional[Union[ParamsContent, ParamsSeason, ParamsEpisode]] = None,
) -> Any:
    if params is not None:
        params.validate()
        params = {**self.params, **params.as_dict()}
    else:
        params = self.params

    response = requests.get(link, params=params, timeout=90)

    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except JSONDecodeError as error:
            raise ApiTokenInvalidError(error) from error
    elif response.status_code == 500:
        raise ApiFailedError(response.status_code, response.text)
    else:
        raise Exception(response.status_code, response.text)
