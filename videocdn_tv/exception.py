class ApiFailedException(Exception):
    def __init__(self, response_status, response_text) -> None:
        super().__init__(response_status)
        self.response_text = response_text


class ApiTokenInvalid(Exception):
    pass
