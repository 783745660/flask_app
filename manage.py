# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/7 22:05'

# 启动文件

from App import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
