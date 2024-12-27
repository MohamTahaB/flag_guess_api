from session.session import Session
from utils.utils import getFlag


def test_resemblance_OK():
    session: Session = Session()
    # When resemblance is checked on initialization, the value should be 0
    assert (session.resemblance < 1e-2)

    # Here, when both the render and the flag are the same, the expected value should be one
    session.flag.render = session.flag.flag
    assert (session.resemblance == 1)

    # Here is an example where the two flags are around 2/3 rds identical ...
    session_france: Session = Session("france")

    session_france.flag.render = getFlag("italy")

    assert (abs(session_france.resemblance - 0.66) < 1e-2)
