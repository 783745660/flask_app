# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/6 22:01'


class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = ""


# 开发环境
class DevelpmentConfig(Config):
    DEBUG = True
    ENV = "development"


# 生产环境
class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"


# 测试环境
class TestingConfig(Config):
    TESTING = True