import sqlite3
from types import TracebackType
from typing import Optional, Type

from patterns.query_object import query_raw


class SqliteConnector:

    def __init__(self, db_file: str = ':memory:'):
        self.db_file = db_file

        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print("Connected to SQLite database")
        except sqlite3.Error as e:
            print("Error connecting to SQLite database:", e)

    def close(self):
        if self.connection:
            self.cursor.close()
            self.cursor = None
            self.connection.close()
            self.connection = None
            print("SQLite connection is closed")

    def __enter__(self):
        """Enter context manager by returning Connector object"""
        self.connect()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Exit context manager by closing Connector"""
        self.close()
