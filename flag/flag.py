from utils.utils import randomCountryName, getFlag
from typing import List
from PIL import Image, ImageChops
import numpy as np

THRESHOLD: int = 30


class Flag:

    def __init__(self, _country: str | None = None):
        self.country: str = randomCountryName() if _country == None else _country

        self.flag: Image.Image = getFlag(self.country)
        self.render: Image.Image = Image.new(
            "RGBA", self.flag.size, (0, 0, 0, 0))
        self.prior_guesses: List[str] = list()

    @property
    def resemblance(self) -> float:
        """Returns the render resemblance to the initial flag

        Returns:
            float: resemblance to the initial flag
        """

        difference: Image.Image = ImageChops.difference(
            self.flag, self.render).convert("L")

        diff_array = np.array(difference)
        pixel_total: float = float(np.prod(diff_array.shape))

        return float(np.sum(diff_array < THRESHOLD)) / pixel_total

    def add_guess(self, country: str) -> None:
        """Adds a guess to the list of guesses, then calls for a render update

        Args:
            country (str): New guess
        """
        self.prior_guesses.append(country)
        self.update_render()

    def update_render(self) -> None:
        """Updates the render to consider the last guess
        """
        if len(self.prior_guesses) == 0:
            return

        last_guess_flag: Image.Image = getFlag(
            self.prior_guesses[-1]).resize(self.flag.size)

        difference: Image.Image = ImageChops.difference(
            last_guess_flag, self.flag).convert("L")

        diff_array = np.array(difference)

        # change values to 0 or 255 according to whether it is below or above the THRESHOLD
        diff_array[diff_array < THRESHOLD] = 0
        diff_array[diff_array > THRESHOLD] = 255

        self.render = Image.composite(
            self.render, self.flag, Image.fromarray(diff_array))
