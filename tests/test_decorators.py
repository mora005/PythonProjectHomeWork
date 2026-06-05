import pytest
import tempfile

from src.decorators import log, my_function, filename_exist


def test_log():
    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)


def test_log_capsys():
    result = my_function(1, 2)
    assert result == 0.5
    with open("mylog.txt", "r", encoding="utf-8") as f:
        read_result = f.read()
        assert "my_function ok" in read_result


def test_message(capsys):
    filename_exist("qwerty")
    captured = capsys.readouterr()
    assert "qwerty" in captured.out


def test_log_tempfile():  # способ 1
    with tempfile.TemporaryDirectory() as tmpdir:  # метод тестов в котором не возникает  ложноположительной ошибки

        @log(tmpdir + r"\temp.log")  # потому что создаётся новый файл при проверке, который сразу удаляется
        def foo():
            return "qwerty"

        result = foo()
        assert result == "qwerty"
        with open(tmpdir + r"\temp.log", "r", encoding="utf-8") as f:
            read_result = f.read()
            assert "foo ok" in read_result


def test_log_tmp_path(tmp_path):  # Спосооб 2
    filename = str(
        tmp_path / "temp.log"
    )  # файл создаётся и удаляется в папке temp и удаляется после завершения программы

    @log(filename)  # обертываем в декоратор для проверки его работы
    def foo():
        return "qwerty"

    result = foo()
    assert result == "qwerty"
    with open(filename, "r", encoding="utf-8") as f:  # f это имя файла
        read_result = f.read()
        assert "foo ok" in read_result  # проверяем есть ли в созданнои файле поддтерждение коректности функции


# коментарии к обоим способам общие
