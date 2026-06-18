import pytest
from playwright.sync_api import expect

@pytest.fixture(autouse=True)
def set_expect_timeout():
    # Set the global default expect timeout to 10 seconds (10,000 milliseconds)
    expect.set_options(timeout=10_000)
