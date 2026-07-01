from odoo import models, api, Command

class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.model_create_multi
    def create(self, vals_list):
        projects = super().create(vals_list)
        
        default_stages = self.env['project.task.type'].search([('is_default_stage', '=', True)])
        if default_stages:
            for project in projects:
                default_stages.write({
                    'project_ids': [Command.link(project.id)]
                })
                
        return projects
