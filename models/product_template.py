# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import itertools
import logging
from collections import defaultdict

from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, RedirectWarning, UserError
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    default_code = fields.Char(
        'Internal Reference', default='Auto', store=True, readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('default_code', 'Auto') == 'Auto':
            vals['default_code'] = self.env['ir.sequence'].next_by_code('increment_product_internal_reference') \
                           or 'New'
        result = super(ProductTemplate, self).create(vals)

        return result
