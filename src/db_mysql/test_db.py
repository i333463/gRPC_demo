import db as db

conn = db.get_connection()
if db.select_user_by_user_id(conn, '1333463'):

  user : {
      "user_id": "1333463",
      "user_name": "Eric Wu",
      "password": "123456"
  }
  db.create_user(conn, user)

