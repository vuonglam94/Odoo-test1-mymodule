# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mymodule(models.Model):
    _name = 'mymodule.mymodule'

    name = fields.Char(required=True)
    age = fields.Char()
    classroom = fields.Char()
    newclass_id = fields.Many2one('new.class', ondelete='set null')


class newclass(models.Model):
    _name = 'new.class'

    mymodule_ids = fields.One2many(
        'mymodule.mymodule', 'newclass_id')


    #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100