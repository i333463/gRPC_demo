from __future__ import print_function
import functools
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

import grpc

from genproto import easyshop_pb2
from genproto import easyshop_pb2_grpc

bp = Blueprint("frontend", __name__, url_prefix="/frontend")

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")
    user_name = session.get("user_name")

    if user_id is None:
        g.user = None
    else:
        g.user.user_id = user_id
        g.user.user_name = user_name

@bp.route("/login", methods=("GET", "POST"))
def login():

  return render_template("frontend/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
  if request.method == "POST":
    user_id = request.form["user_id"]
    user_name = request.form["user_name"]
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]
    error = None

    if not user_id:
      error = "User ID is required."
    elif not user_name:
      error = "Username is required."
    elif not password:
      error = "Password is required."
    elif not password_confirm:
      error = "Password Confirm is required."
    elif (
      password != password_confirm
    ):
      error = "User {0} is already registered.".format(user_name)

    if error is None:
      # the name is available, store it in the database and go to
      # the login page

      with grpc.insecure_channel('localhost:50051') as channel:
          stub = easyshop_pb2_grpc.AccountServiceStub(channel)
          response = stub.register(easyshop_pb2.RegisterRequest(user_id=user_id, user_name=user_name, password=password, password_confirm=password_confirm))

      return redirect(url_for("frontend.login"))

    flash(error)

  return render_template("frontend/register.html")