# import sqlite3
#
#
# connection = sqlite3.connect('data.db')
#
# # Responible for queries on the database
# cursor = connection.cursor()
#
# create_table = "CREATE TABLE users (id int, username text, password text)"
# cursor.execute(create_table)
#
#
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# #cursor.execute(insert_query, user)
#
# users = [
#     (1, 'jose', 'sdf'),
#     (1, 'demi', 'asdf'),
#     (1, 'liz', 'lkjh')
# ]
#
# cursor.executemany(insert_query, users)
#
# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)
#
# connection.commit()
#
# connection.close()
