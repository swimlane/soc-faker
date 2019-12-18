import pytest

@pytest.fixture
def socfaker_fixture():
    #import swimlanefaker
    from socfaker import SocFaker
    return SocFaker()