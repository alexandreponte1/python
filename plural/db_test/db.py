import sqlite3

conn = sqlite3.connect("server_inventory.db")
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    os TEXT NOT NULL,
    status TEXT NOT NULL
    )
'''

cursor.execute(create_table_query)
conn.commit()
conn.close()


def insert_server(name, ip_address, os, status):
    conn = sqlite3.connect("server_inventory.db")
    cursor = conn.cursor()
    insert_query = "INSERT INTO servers (name, ip_address, os, status) VALUES (?, ?, ?, ?)"
    cursor.execute(insert_query,(name, ip_address, os, status))

    conn.commit()
    conn.close()

def get_servers():
    conn = sqlite3.connect("server_inventory.db")
    cursor = conn.cursor()

    select_query = "SELECT * FROM servers"
    cursor.execute(select_query)
    servers = cursor.fetchall()

    conn.close()
    return servers

def update_server_status(server_id, new_status):
    conn = sqlite3.connect("server_inventory.db")
    cursor = conn.cursor()

    update_query = "UPDATE servers SET status = ? WHERE id  = ?"
    cursor.execute(update_query, (new_status, server_id))

    conn.commit()
    conn.close()


def delete_server(server_id):
    conn = sqlite3.connect("server_inventory.db")
    cursor = conn.cursor()

    delete_query = "DELETE FROM servers WHERE id  = ?"
    cursor.execute(delete_query, (server_id,))

    conn.commit()
    conn.close()


insert_server("web Server", "192.168.1.100", "Ubuntu", "Active")
insert_server("Database Server", "192.168.1.100", "CentOS", "Active")


servers = get_servers()
for srv in servers:
    print(srv)


update_server_status(1, "Maintenance")
delete_server(3)

servers = get_servers()
for srv in servers:
    print(srv)