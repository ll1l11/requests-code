# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, make_response
from flask.views import MethodView

from requests_code.forms import CodeForm

bp = Blueprint('run', __name__)


class RunView(MethodView):

    def get(self, filename):
        """如果文件存在, 从本地读取代码返回到界面"""
        if not filename:
            code = '# -*- coding: utf-8 -*-'
        else:
            code = ''
        return render_template('code-page.html', code=code)

    def post(self):
        """将文件保存到指定文件中, 并执行, 返回执行后的结果"""
        form = CodeForm()
        name = form.name.data
        code = form.code.data
        action = form.action.data
        if not name:
            name = 'test'
        if action == CodeForm.ACTION_EXEC:
            resp = make_response('temp')
            resp.mimetype = 'text/plain'
            return resp
        else:
            resp = make_response(code)
            resp.mimetype = 'text/plain'
            resp.headers['Content-Disposition'] = \
                'attachment; filename=main.py'
            return resp


view_func = RunView.as_view('run')
bp.add_url_rule('/run', defaults={'filename': None},
                view_func=view_func)
bp.add_url_rule('/run/<filename>',
                view_func=view_func)
