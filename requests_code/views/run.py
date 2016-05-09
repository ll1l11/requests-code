# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.views import MethodView

bp = Blueprint('run', __name__)


class RunView(MethodView):

    def get(self, filename):
        """如果文件存在, 从本地读取代码返回到界面"""
        return 'code get'

    def post(self, filename):
        """将文件保存到指定文件中, 并执行, 返回执行后的结果"""
        return 'code post'
