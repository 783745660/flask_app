# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/7 22:05'

# 作为App包的默认文件，App被导入时候自动启动本文件

from flask import Flask

from settings import DevelpmentConfig
from .views.blog_views import blog_bp
from .views.home_views import home_bp


# 初始化app
def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(DevelpmentConfig)

    # 把模块蓝图注册到主程序
    app.register_blueprint(blog_bp, url_prefix="/blog")
    app.register_blueprint(home_bp, url_prefix="/user")
    return app
