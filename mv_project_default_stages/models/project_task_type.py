from odoo import models, fields

class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    is_default_stage = fields.Boolean(
        string="Is Default Stage",
        default=False,
        help="If checked, this stage will be automatically added to any newly created project."
    )
