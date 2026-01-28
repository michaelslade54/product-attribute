from openupgradelib import openupgrade

xml_ids = ["product_state_history.product_template_form_view",
           "product_state_history.product_state_history_form_view",
           "product_state_history.product_state_history_search_view",
           "product_state_history.product_state_history_tree_view",
           "product_state_history.product_state_history_pivot_view",
           "product_state_history.product_state_history_wizard_form_view",
           "product_state_history.report_product_state_history"]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)