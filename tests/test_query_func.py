import pytest

from patterns.query_object import query_func


def test_query_with_double_attributes():
    q = query_func.Query()

    q.SELECT('col1', 'col2', 'col1')
    q.FROM('table1', 'table2', 'table1')

    assert q.oneline() == 'SELECT col1, col2 FROM table1, table2'


if __name__ == "__main__":
    pytest.main([__file__, "-s", "-v", "--color=yes"])