# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/7 22:18'

import datetime

from flask import Blueprint, request, render_template, redirect


# 创建蓝图对象
home_bp = Blueprint("home", __name__)


@home_bp.route("/index")
def blog_index():
    uname = request.cookies.get("cookie_name")
    return render_template("index.html", uname=uname)


@home_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        if username == "xiaoli" and password == "123":
            print(111)
            response = redirect("/user/index")
            # response.set_cookie('cookie_name', request.form.get('username'))
            # response.set_cookie("cookie_name", username, max_age=7*24*3600)
            date = datetime.datetime(2023,1,1)
            response.set_cookie("cookie_name", username, expires=date)
            return response
        else:
            return "username or password not correct"


@home_bp.route("/logout")
def logout():
    response = redirect("/user/index")  # 绝对路径
    # 删除cookie
    response.delete_cookie("cookie_name")
    return response
