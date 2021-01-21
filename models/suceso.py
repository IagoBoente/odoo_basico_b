# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suceso(models.Model):
    _name = 'odoo_basico_b.suceso'  #Será o nome da táboa
    _description = 'Exemplo modelo suceso'

    name = fields.Char(string="Título:",size=20,required=True)
    descripcion = fields.Text(string="A Descripción:")
    nivel  = fields.Selection([('Alto','Alto'),('Medio','Medio'),('Baixo','Baixo')],string="Nivel:")
    data_hora = fields.Datetime(string="Data e Hora")