from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....ContactCreationView import ContactCreationView

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.contact_name.text = self.item["first_name"] + " " + self.item["last_name"] + " - " + self.item["email"] 

    # Any code you write here will run before the form opens.

  def edit_contact_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=ContactCreationView(self.item), buttons=None, large=True, dismissible=False)
    if new_popup == "updated":
      notif = Notification("Contact updated successfully", title="Success", style="success").show()
      self.parent.parent.parent.parent.parent.form_refreshing_data_bindings()
    elif new_popup == "deleted":
      notif = Notification("Contact deleted", title="Success", style="success").show()
      self.parent.parent.parent.parent.parent.form_refreshing_data_bindings()
    

