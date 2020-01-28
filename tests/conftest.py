import pytest

@pytest.fixture
def socfaker_fixture():
    from socfaker import SocFaker
    return SocFaker(github_token='')