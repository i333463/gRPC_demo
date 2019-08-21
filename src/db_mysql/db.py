import mysql.connector



def get_connection():
  config = {
        'user': 'root',
        'password': 'helloworld01',
        'host': 'db',
        'port': '3306',
        'database': 'grpc'
    }
  return mysql.connector.connect(**config)

def select_user_by_user_id(conn, id):

    cursor = conn.cursor(buffered=True)

    query = ("SELECT u.user_id, u.user_name FROM user AS u WHERE user_id = %s")

    cursor.execute(query, (id,))

    user = None
    for (user_id, user_name) in cursor:

      user : {
          "user_id": user_id,
          "user_name": user_name
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




