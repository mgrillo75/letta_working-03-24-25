import logging

import pytest

from letta.services.organization_manager import OrganizationManager
from letta.services.user_manager import UserManager
from letta.settings import tool_settings


def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def mock_e2b_api_key_none():
    from letta.settings import tool_settings

    # Store the original value of e2b_api_key
    original_api_key = tool_settings.e2b_api_key

    # Set e2b_api_key to None
    tool_settings.e2b_api_key = None

    # Yield control to the test
    yield

    # Restore the original value of e2b_api_key
    tool_settings.e2b_api_key = original_api_key


@pytest.fixture
def check_e2b_key_is_set():
    from letta.settings import tool_settings

    original_api_key = tool_settings.e2b_api_key
    assert original_api_key is not None, "Missing e2b key! Cannot execute these tests."
    yield


@pytest.fixture
def default_organization():
    """Fixture to create and return the default organization."""
    manager = OrganizationManager()
    org = manager.create_default_organization()
    yield org


@pytest.fixture
def default_user(default_organization):
    """Fixture to create and return the default user within the default organization."""
    manager = UserManager()
    user = manager.create_default_user(org_id=default_organization.id)
    yield user


@pytest.fixture
def check_composio_key_set():
    original_api_key = tool_settings.composio_api_key
    assert original_api_key is not None, "Missing composio key! Cannot execute this test."
    yield
