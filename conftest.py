import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixrure = Application()
    request.addfinalizer(fixrure.destroy)
    return fixrure
