import pytest
from patterns.db_connector import connector_cls
from patterns.query_object import query_raw


def test_connect_to_sqlite_db():

    with connector_cls.SqliteConnector() as connection:
        cursor = connection.cursor
        cursor.executescript(query_raw.create_table_script)
        cursor.executemany(query_raw.insert_query, query_raw.data)
        cursor.execute(query_raw.select_query)

        row: list[str, str] = cursor.fetchone()
        assert connection.cursor is not None
        assert row == ('John Doe', 'john@example.com')
    assert connection.cursor is None


if __name__ == "__main__":
    pytest.main([__file__, "-s", "-v", "--color=yes"])