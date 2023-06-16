import pytest
from geometrical_layout import GeometricalLayoutApi


def  test_raises_with_info_alt() -> None:
    """
    Test for inproper argument
    """
    with  pytest.raises(TypeError)  as  exc_info:
        api = GeometricalLayoutApi()
        api.post_object(2,2)
    expected =  "missing 1 required positional argument"
    assert  expected  in  str(exc_info.value)


def test_to_dict() -> None:
    c1 = GeometricalLayoutApi()
    c2 = c1.post_object(0.5,1,5)
    c2_expected =  "<class 'dict'>"
    assert str(type(c2)) == c2_expected


if __name__ == "__main__":   
    pass