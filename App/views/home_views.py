# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/7 22:18'


from flask import Blueprint


# 创建蓝图对象
home_bp = Blueprint("home", __name__)


@home_bp.route("/index")
def blog_index():
    return "用户首页"