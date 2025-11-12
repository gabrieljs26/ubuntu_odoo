from odoo import models, fields

class MiModulo(models.Model):
    _name = 'mi_modulo.mi_modulo'
    _description = 'Modelo principal de mi módulo'

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')

