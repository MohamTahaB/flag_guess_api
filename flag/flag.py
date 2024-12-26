from utils.utils import randomCountryName, getFlag
from typing import List
from PIL import Image, ImageChops
import numpy as np


class Flag:

    def __init__(self, _country: str = None):
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

        return float(np.sum(diff_array < 30)) / pixel_total
