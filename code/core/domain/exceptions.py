class InvalidUUidException(Exception):
    def __init__(self, error='ID must be a valid UUID') -> None:  
        super().__init__(error)

class InvalidContentTypeException(Exception):
    def __init__(self, error='Value must be a valid Content Type instance') -> None:  
        super().__init__(error)


class InvalidPermissionException(Exception):
    def __init__(self, error='Value must be a valid Permission instance') -> None:  
        super().__init__(error)