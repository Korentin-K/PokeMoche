class MocheBalls:
    ballType: str
    catchRate: int

    def __init__(self, ballType="", catchRate=1):
        self._type = ballType
        self._catchRate = catchRate

    @property
    def ballType(self) -> str:
        return self._type

    @property
    def catchRate(self) -> int:
        return self._catchRate

    @ballType.setter
    def ballType(self, value: str) -> None:
        self._type = value

    @catchRate.setter
    def catchRate(self, value: int) -> None:
        self._catchRate = value
