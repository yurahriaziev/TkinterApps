import sqlite3
conn = sqlite3.connect('BankAccount')
c = conn.cursor()

def create_table(table_name, *args):
    columns = ', '.join(args)
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'

    c.execute(query)

    conn.commit()

def add_new_user(table_name, **col_data):
    colums = ', '.join(col_data.keys())
    placeholders = ', '.join('?' * len(col_data))
    print(placeholders)

    query = f'INSERT INTO {table_name} ({colums}) VALUES ({placeholders})'

    values = tuple(col_data.values())
    print(values)

    c.execute(query, values)

    conn.commit()

def view_db():
    data = c.execute('SELECT * FROM users').fetchall()

    for row in data:
        print(row)




if __name__ == "__main__":
    view_db()
