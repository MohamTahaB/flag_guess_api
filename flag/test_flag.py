from flag.flag import Flag
from utils.utils import getFlag


def test_resemblance_OK():
    flag: Flag = Flag()
    flag.render = flag.flag
    assert (flag.resemblance == 1)

    # Here is an example where the two flags are around 2/3 rds identical ...
    flag_france: Flag = Flag("france")

    flag_france.render = getFlag("italy")

    assert (abs(flag_france.resemblance - 0.66) < 1e-2)
