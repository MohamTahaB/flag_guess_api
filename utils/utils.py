import random
import requests


def randomCountryName() -> str:
    """Returns a random country name from the REST COUNTRY Project. If the request is not of status OK, it returns Morocco.

    Returns:
        str: Random chosen country.
    """

    # REST countries project url
    url: str = "https://restcountries.com/v2/"

    response = requests.get(f"{url}all")

    if response.status_code != 200:
        return "Morocco"

    return "Morocco" if len(response.json()) == 0 else random.choice(response.json()).get("name", "Morocco")
