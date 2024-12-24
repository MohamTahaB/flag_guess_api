
import uuid
from utils.utils import randomCountryName
from typing import List


class Session:
    def __init__(self):
        self.id: str = uuid.uuid4().hex
        self.country: str = randomCountryName()

        self.resemblance: int = 0
        self.prior_guesses: List[str] = list()
        # TODO! Add the 2D table of the render so far
        self.render: List[List[int]]

    def compute_guess(self, guess: str):
        """Takes the user's guess and computes the new render and resemblance

        Args:
            guess (str): user's Country guess
        """

        self.prior_guesses.append(guess)
        pass
