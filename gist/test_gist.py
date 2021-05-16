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