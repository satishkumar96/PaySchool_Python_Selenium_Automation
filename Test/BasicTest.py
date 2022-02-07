import pytest
from Configuration.ConfigTest import init_driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
