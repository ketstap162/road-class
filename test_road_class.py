import pytest

from app import Road


@pytest.mark.parametrize(
    "length,result",
    [
        pytest.param(
            24,
            "Ok",
            id="Create road with correct length",
        ),
        pytest.param(
            -5,
            "ValueError",
            id="Create road with length < 0"
        ),
        pytest.param(
            "25",
            "TypeError",
            id="Create road with not integer length"
        )
    ]
)
def test_road_create(length, result):
    action = "Ok"

    try:
        road = Road(length)

    except ValueError:
        action = "ValueError"

    except TypeError:
        action = "TypeError"

    assert action == result


@pytest.mark.parametrize(
    "first_len,second_len,result",
    [
        pytest.param(
            22,
            15,
            37,
        ),
        pytest.param(
            2,
            5,
            7,
        ),
        pytest.param(
            2,
            1,
            3,
        )
    ]
)
def test_road_add_road(first_len, second_len, result):
    road_1 = Road(first_len)
    road_2 = Road(second_len)

    road_3 = road_1 + road_2

    assert isinstance(road_3, Road)
    assert road_3.length == result


@pytest.mark.parametrize(
    "first_len,second_len",
    [
        pytest.param(x, 10 - x, id=f"Compare Road({x}) and Road({10 - x})")
        for x in range(1, 10)
    ]
)
def test_roads_compare(first_len, second_len):
    road_1 = Road(first_len)
    road_2 = Road(second_len)

    assert (road_1 == road_2) is (first_len == second_len)
    assert (road_1 > road_2) is (first_len > second_len)
    assert (road_1 >= road_2) is (first_len >= second_len)
    assert (road_1 < road_2) is (first_len < second_len)
    assert (road_1 <= road_2) is (first_len <= second_len)
    assert (road_1 != road_2) is (first_len != second_len)

@pytest.mark.parametrize(
    "other",
    [
        pytest.param(
            "15",
            id="Compare with string"
        ),
        pytest.param(
            15.5,
            id="Compare with float"
        ),
    ]
)
def test_road_compare_with_other_type(other):
    road = Road(15)
    action = "Ok"
    try:
        road == other
        road >= other
        road <= other
        road < other
        road > other
        road != other
    except TypeError:
        action = "TypeError"

    assert action == "TypeError"
