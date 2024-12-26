import random
import requests
from PIL import Image
from io import BytesIO
from pathlib import Path

# REST countries project url
URL: str = "https://restcountries.com/v2/"
ROOT_PATH: Path = Path(__file__).resolve().parent.parent


def randomCountryName() -> str:
    """Returns a random country name from the REST COUNTRY Project. If the request is not of status OK, it returns Morocco.

    Returns:
        str: Random chosen country.
    """

    response = requests.get(f"{URL}all")

    if response.status_code != 200:
        return "Morocco"

    countries_list = response.json()
    return "Morocco" if len(countries_list) == 0 else random.choice(countries_list).get("name", "Morocco")


def getFlag(country: str) -> Image.Image:
    """Given a country's name, returns the flag corresponding to the most likely country to correspond to the provided name ( the first result of the countries project response )

    Args:
        country (str): Name of the country

    Returns:
        Image.Image: The country's flag
    """

    fallback_path: Path = Path("public/ma.png")

    response = requests.get(f"{URL}name/{country}")

    if response.status_code != 200:
        return Image.open(ROOT_PATH / fallback_path).convert("RGBA")

    flag_url: str = response.json()[0]["flags"]["png"]
    flag_response = requests.get(flag_url)

    if flag_response.status_code != 200:
        return Image.open(ROOT_PATH / fallback_path).convert("RGBA")

    flag_image: Image.Image = Image.open(
        BytesIO(flag_response.content))

    return flag_image.convert("RGBA")
