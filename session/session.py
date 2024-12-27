
import uuid
from flag.flag import Flag
import io
import base64


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

    @property
    def render_base64(self) -> str:
        """Returns the flag render as Base64 string

        Returns:
            str: Flag render in Base64
        """
        buffer = io.BytesIO()
        self.flag.render.save(buffer, format="PNG")
        buffer.seek(0)

        return base64.b64encode(buffer.getvalue()).decode("utf-8")

    def add_guess(self, country: str) -> None:
        """Wraps the method add_guess from the Flag class

        Args:
            country (str): New guess
        """
        self.flag.add_guess(country)
