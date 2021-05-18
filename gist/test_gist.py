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

class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"


# use function as fixture

@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")

# pytest file_to_test -v -p no:warnings -s
# -s flag is for print statements

def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")

# pytest parametrize

@pytest.mark.parametrize(
    "company_name",
    ["TickTok", "Instagram", "Twitch"],
    ids=["TickTok test", "Instagram test", "Twitch test"]
)
def test_parametrized(company_name: str) -> None:
    print(f"\nTest with {company_name}")

#pytest.raises

def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)

# assert Exception

def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        """context manager 안에서 ValueError 가 raise 되는지 확인한다."""
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)


# assert Log
import logging
logger = logging.getLogger("CORONA_LOGS")

def function_that_logs_something() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")

# caplog is capture feature
def test_logged_warning_level(caplog) -> None:
    # 기본적으로 warning level 또는 above만 확인한다.
    function_that_logs_something()
    assert "I am logging CoronaVirus Exception" in caplog.text

def test_logged_info_level(caplog) -> None:
    # warning level 아래단계도 체크하고싶으면, context manager를 사용
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text


# show the durations
# tag --durations=0


# pytest file.py -k "sth"
# 위와같이 -k 플래그는 function name에 "sth"이 들어간 것만 테스트 한다

# pytest file.py -k "sth and not nth"
# 위와 같은 경우는 sth은 포함하지만 nth은 포함하지 않는다.

