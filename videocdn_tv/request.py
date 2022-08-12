import json
from json import JSONDecodeError
from typing import Union, Any

import requests

from videocdn_tv.exception import ApiFailedException, ApiTokenInvalid
from videocdn_tv.params import *


def get_request(self,
                link: str,
                params: Union[ParamsContent, ParamsSeason, ParamsEpisode] = None) -> Any:
    if params is not None:
        params = {**self.params, **params.__str__()}
    else:
        params = self.params

    response = requests.get(link, params=params)

    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except JSONDecodeError:
            raise ApiTokenInvalid
    elif response.status_code == 500:
        raise ApiFailedException(response.status_code, response.text)
    else:
        raise Exception(response.status_code, response.text)
