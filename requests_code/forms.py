# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask_wtf import Form
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import Optional, Required

from requests_code.models import Code


class RequestDataForm(Form):
    host = StringField('Host', [Optional()])
    data = TextAreaField('Request raw', [Required()])
    action = StringField('action', [Required()])


class CodeForm(Form):
    name = StringField('name', [Optional()])
    code = TextAreaField(u'代码')
    action = StringField('action')

    ACTION_EXEC = 'exec'
    ACTION_DOWNLOAD = 'download'

    @staticmethod
    def generate_name():
        """获取唯一的文件名"""
        max_id = Code.get_max_id()
        print(max_id)
        return 'abc'
