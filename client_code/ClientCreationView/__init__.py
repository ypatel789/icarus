from ._anvil_designer import ClientCreationViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ClientCreationView(ClientCreationViewTemplate):
  def __init__(self, row=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.row = row
    if row != None:
      self.label_1.text = "Edit Client"
      self.client_name.text = row["client_name"]
      self.address.text = row["address"]
      self.save_client.set_event_handler("click", self.update_client)
    # Any code you write here will run before the form opens.
  def update_client(self, **event_args):
    """This method is called when editing an existing client"""
    input_name = self.client_name.text
    input_address = self.address.text

    anvil.server.call('update_client_by_id', self.row.get_id(), input_name, input_address)
    self.raise_event("x-close-alert", value="updated")
    
  def save_client_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_name = self.client_name.text
    input_address = self.address.text
    
    if (input_name == ""):
      n = Notification("Please enter client name", title="Error", style="danger").show()
    else:
      anvil.server.call('create_client', input_name, input_address)
      self.raise_event("x-close-alert", value="success")
    

  def cancel_client_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value="ur_mum")

    



