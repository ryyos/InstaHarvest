class ExpiredExceptions(KeyError):
    def __init__(self) -> None:
        super().__init__('your COOKIES or IG CLAIM is Expired, Update Please!')