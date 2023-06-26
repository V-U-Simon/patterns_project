# сырые запросы в БД
create_table_script = """
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
"""

data = [("John Doe", "john@example.com"), ("Jane Smith", "jane@example.com"), ("Bob Johnson", "bob@example.com")]
insert_query = "INSERT INTO customers (name, email) VALUES (:name, :email)"  # именованные (:)
select_query = 'SELECT name, email FROM customers'

drop_table_script = "DROP TABLE IF EXISTS customers;"