from openupgradelib import openupgrade

xml_ids = ["product_state_active.product_state_form_view"]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xmlid(env, xml_ids)