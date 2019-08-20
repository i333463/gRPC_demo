import mysql.connector

config = {
    'user': 'root',
    'password': 'helloworld01',
    'host': 'db',
    'port': '3306',
    'database': 'grpc'
}

def get_connection():

  return mysql.connector.connect(**config)

def select_user_by_user_id(conn, user_id):

    cursor = conn.cursor(buffered=True)

    query = (
        "SELECT user_id, user_name FROM user"
        "WHERE user_id = %s")

    cursor.execute(query, (user_id))

    user = None
    for (id, name) in cursor:

      user : {
          "user_id": id,
          "user_name": name
      }
    cursor.close()

    return user

def create_user(conn, user):

    cursor = conn.cursor(buffered=True)
    user_id = user.get["user_id"]
    user_name = user.get["user_name"]
    password = user.get["password"]
    password_confirm = user.get["password_confirm"]

    insert_user = (
        "INSERT INTO user (user_id, user_name, password)"
        "VALUES (%s, %s, %s)")

    cursor.execute(insert_user, (user.get["user_id"], user.get["user_name"], user.get["password"]))

    cursor.commit()
    cursor.close()




