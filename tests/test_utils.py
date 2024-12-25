from utils.utils import randomCountryName, getFlag


def test_randomCountryName_OK():
    random_country_output: str = randomCountryName()


def test_getFlag_OK():
    country: str = randomCountryName()
    print(f"country: {country}")
    im = getFlag(country)
    im.show(f"country: {country}")
