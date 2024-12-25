from utils.utils import randomCountryName, getFlag
from typing import List
from PIL import Image


class Flag:

    def __init__(self):
        self.country: str = randomCountryName()

        self.flag: Image.Image = getFlag(self.country)
        self.render: Image.Image = Image.new(
            "RGBA", self.flag.size, (0, 0, 0, 0))
        self.prior_guesses: List[str] = list()
