import json
from typing import Tuple, Union

import requests
from requests import Response

from models.content import ContentModel
from params import *


def get_request(self,
                link: str,
                params: Union[ParamsContent, ParamsSeason, ParamsEpisode]) -> Tuple[Response, ContentModel]:
    params = {**self.params, **params.__str__()}
    response = requests.get(link, params=params)
    return response, ContentModel(**json.loads(response.text))
