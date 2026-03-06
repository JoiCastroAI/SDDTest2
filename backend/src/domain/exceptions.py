class DomainError(Exception):
    pass


class NotFoundError(DomainError):
    def __init__(self, entity: str, identifier: str | int) -> None:
        super().__init__(f"{entity} not found: {identifier}")
        self.entity = entity
        self.identifier = identifier


class ValidationError(DomainError):
    pass


class ConflictError(DomainError):
    pass
