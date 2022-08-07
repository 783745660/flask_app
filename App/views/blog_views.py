# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/7 22:18'


from flask import Blueprint


# 创建蓝图对象
blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/index")
def blog_index():
    return "博客首页"