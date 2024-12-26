from flag.flag import Flag
from utils.utils import getFlag


def test_resemblance_OK():
    flag: Flag = Flag()
    # When resemblance is checked on initialization, the value should be 0
    assert (flag.resemblance < 1e-2)

    # Here, when both the render and the flag are the same, the expected value should be one
    flag.render = flag.flag
    assert (flag.resemblance == 1)

    # Here is an example where the two flags are around 2/3 rds identical ...
    flag_france: Flag = Flag("france")

    flag_france.render = getFlag("italy")

    assert (abs(flag_france.resemblance - 0.66) < 1e-2)
