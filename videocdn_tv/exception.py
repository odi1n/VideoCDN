class ApiFailedError(Exception):
    def __init__(self, response_status: str, response_text: str) -> None:
        super().__init__(response_status)
        self.response_text = response_text


class ApiTokenInvalidError(Exception):
    pass
