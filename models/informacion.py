# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico_b.informacion'  #Será o nome da táboa
    _description = 'Tipos de datos básicos'

    name = fields.Char(string="Título:",size=20,required=True)
    descripcion = fields.Text(string="A Descripción:")
    autorizado = fields.Boolean(string="¿Está autorizado?",default=True)
    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')],string="Sexo:")
    alto_en_cms = fields.Integer(string="Alto en Cms.")
    ancho_en_cms = fields.Integer(string="Ancho en Cms.")
    longo_en_cms = fields.Integer(string="Longo en Cms.")
    volume = fields.Float(compute="_volume",store=True)
    peso = fields.Float(string="Peso:",digits=(6,2),default=2.7)
    densidade = fields.Float(compute="_densidade",store=True)

    @api.depends('alto_en_cms','ancho_en_cms','longo_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.ancho_en_cms) * float(rexistro.longo_en_cms)

    @api.depends('volume','peso')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = (float(rexistro.peso) / float(rexistro.volume)) * 100
            else:
                rexistro.densidade = 0

