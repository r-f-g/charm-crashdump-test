import logging

import pytest


log = logging.getLogger(__name__)


@pytest.mark.abort_on_fail
async def test_build(ops_test):
    await ops_test.model.deploy("ch:ubuntu")
    await ops_test.model.wait_for_idle()


async def test_failure(ops_test):
    pytest.failure("haha")
