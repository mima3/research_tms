import ssl
import os
import pytest

# 自己認証対策
ssl._create_default_https_context = ssl._create_unverified_context

os.environ["TCMS_PRODUCT"] = "製品A"
os.environ["TCMS_PRODUCT_VERSION"] = "ver1.0"
os.environ["TCMS_BUILD"] = "unspecified"


def test_should_pass_when_assertion_passes():
    assert True


def test_should_fail_when_assertion_fails():
    assert 1 == 2


@pytest.mark.skip("We've decided not to test this")
def test_should_skip_if_marked_as_such():
    assert True
