import pytest

from patterns.query_object import query_cls


def test_query_with_double_attributes():
    q = query_cls.Query()

    q.SELECT('col1', 'col2', 'col1')
    q.FROM('table1', 'table2', 'table1')

    assert str(q) == 'SELECT col1, col2 FROM table1, table2;'


def test_query_with_where():
    q = query_cls.Query()

    q.SELECT('col1', 'col2', 'col1')
    q.WHERE(col1='11', col2='22')
    q.FROM('table1', 'table2', 'table1')

    assert str(q) == 'SELECT col1, col2 WHERE col1=11 AND col2=22 FROM table1, table2;'


if __name__ == "__main__":

    pytest.main([__file__, "-s", "-v", "--color=yes"])