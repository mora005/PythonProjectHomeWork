import pytest

from src.decorators import log, my_function


def test_log():
    with pytest.raises(Exception):
        my_function()


def test_log_capsys(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    captured.out == "my_function ok"
