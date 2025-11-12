from odoo import models, fields
class EjemploModelo(models.Model):
    _name = 'ejemplo.modelo'
    _description = 'Modelo de Ejemplo'

    name = fields.Char(string='Nombre')
    
