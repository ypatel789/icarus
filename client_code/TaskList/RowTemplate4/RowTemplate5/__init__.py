from ._anvil_designer import RowTemplate5Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....ActivityCreationView import ActivityCreationView

class RowTemplate5(RowTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.activity_name.text = self.item["activity"]

    # Any code you write here will run before the form opens.

  def edit_activity_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=ActivityCreationView(self.item), buttons=None, large=True, dismissible=False)
    if new_popup == "updated":
      notif = Notification("Activity updated successfully", title="Success", style="success").show()
      self.parent.parent.parent.parent.parent.form_refreshing_data_bindings()
    elif new_popup == "deleted":
      notif = Notification("Activity deleted", title="Success", style="success").show()
      self.parent.parent.parent.parent.parent.form_refreshing_data_bindings()




