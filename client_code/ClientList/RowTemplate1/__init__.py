from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...ClientCreationView import ClientCreationView

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.client_name.text = self.item["client_name"]
    self.repeating_panel_contacts.items = self.item["contacts"]

    # Any code you write here will run before the form opens.

  def edit_client_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=ClientCreationView(self.item), buttons=None, large=True, dismissible=False)
    if new_popup == "updated":
      notif = Notification("Client updated successfully", title="Success", style="success").show()
      self.parent.parent.parent.form_refreshing_data_bindings()



