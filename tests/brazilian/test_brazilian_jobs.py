from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_translate = {
        "title": "Maquinista", "salary": "2000", "type": "trainee"
        }
    function_test = read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0]

    assert function_test == dict_translate
