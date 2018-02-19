from pygments.lexer import _inherit

from openerp import fields, models, api

class Ditefacts_product_template(models.Model):

    _name = 'product.template'
    _inherit = 'product.template'


    calories = fields.Integer("Calories")
    servingsize = fields.Float("Serving Size")
    lastupdate = fields.Date('Last Update')
    dietitem = fields.Boolean("Diet Item")
    nutrient_ids = fields.One2many('product.template.nutrient', 'product_id','Nutrient')

class DiteFacts_res_users_meal(models.Model):

    _name = "res.users.meal"

    name = fields.Char("Meal Name")
    meal_date = fields.Datetime("Meal Deal")
    user_id = fields.Many2one("res.users", "Meal User")
    notes = fields.Text('Meal Notes')
    item_ids = fields.One2many('res.users.mealitem','meal_id')
    @api.one
    @api.depends('item_ids','item_ids.serving')
    def _calcalories(self):
        current = 0
        for x in self.item_ids:
            current += x.item_id.calories * x.serving
        self.totalcalories = current

    totalcalories = fields.Integer(string='Total Meal Caories',store=True,compute='_calcalories')

class DiteFacts_res_users_mealitems(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template','Meal Items')
    serving = fields.Float('Serving')
    notes = fields.Text('Meal Item Notes')
    calories = fields.Integer(related='item_id.calories',string='Calories Per Serving',store=True,readonly=True)


class Ditefacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char('Nutrient Name')
    uom_id = fields.Many2one('product.uom', 'Unite de Mesure')
    description = fields.Text('Description')

class Ditefacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient', string='Nutrient')
    product_id = fields.Many2one('product.template', string='Diel item')
    value = fields.Float('Valeur')
    dailypercentage = fields.Float('Daily Pourcentage')
    dailyofmeasure = fields.Char(related='nutrient_id.uom_id.name',string='Unite de Mesure',readonly=True)