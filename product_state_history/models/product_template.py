# Copyright 2020 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _prepare_product_state_history_values(self, state_id):
        """Prepare product state history values for create"""
        self.ensure_one()
        vals = {
            "product_template_id": self.id,
            "product_state_id": state_id,
        }
        return vals

    def _set_product_state_history(self, vals):
        """Create a list of history values"""
        history_obj = self.env["product.state.history"]
        history_vals = []
        state_id = vals["product_state_id"]
        for template in self:
            history_vals.append(
                template._prepare_product_state_history_values(state_id)
            )
        if history_vals:
            history_obj.create(history_vals)

    def write(self, vals):
        if "product_state_id" in vals:
            self._set_product_state_history(vals)
        res = super().write(vals)
        return res

    def action_product_state_history(self):
        action = self.env.ref("product_state_history.product_state_history_act_window")
        result = action.read()[0]
        result.update({"domain": [("product_template_id", "in", self.ids)]})

        return result
