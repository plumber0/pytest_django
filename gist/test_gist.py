import pytest

# pytest file_to_test -v
# -v for detail info
def test_our_first_test() -> None:
    assert 2 == 2

#Skipping test (default marker)

@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2

@pytest.mark.skipif(4 > 1, reason="Skipped because 4>1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2

# XFail, XPass (default marker) : it's okay to fail

@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 1

# create marker

# pytest file_to_test -v -p no:warnings
# ignore warning message

# pytest file_to_test -m slow
# run only slow marked test

@pytest.mark.slow
def test_with_custom_mark1() -> None:
    assert 2 == 2

@pytest.mark.slow
def test_with_custom_mark2() -> None:
    assert 2 == 2

