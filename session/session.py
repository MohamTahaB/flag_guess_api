
import uuid
from flag.flag import Flag


class Session:
    def __init__(self, country: str | None = None):
        self.id: str = uuid.uuid4().hex
        self.flag: Flag = Flag(country)

    @property
    def resemblance(self) -> float:
        """Wraps the resemblance property in the Flag class

        Returns:
            float: resemblance to the initial flag
        """

        return self.flag.resemblance

    def add_guess(self, country: str) -> None:
        """Wraps the method add_guess from the Flag class

        Args:
            country (str): New guess
        """
        self.flag.add_guess(country)
