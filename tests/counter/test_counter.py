from src.counter import count_ocurrences


def test_counter():
    word_javascript = count_ocurrences('src/jobs.csv', 'javascript')
    assert word_javascript == 122

    word_python = count_ocurrences('src/jobs.csv', 'python')
    assert word_python == 1639
