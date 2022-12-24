from ._anvil_designer import ClientListTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ClientCreationView import ClientCreationView
from ..ContactCreationView import ContactCreationView

class ClientList(ClientListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.form_refreshing_data_bindings()

    # Any code you write here will run before the form opens.

  def new_client_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=ClientCreationView(), buttons=None, large=True, dismissible=False)
    if new_popup == "success":
      notif = Notification("Client created successfully", title="Success", style="success").show()
      self.form_refreshing_data_bindings()

  def form_refreshing_data_bindings(self, query=None, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    
    clients = anvil.server.call('get_clients')
    self.repeating_panel_clients.items = clients

  def add_contact_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=ContactCreationView(), buttons=None, large=True, dismissible=False)
    if new_popup == "success":
      notif = Notification("Contact created successfully", title="Success", style="success").show()
      self.form_refreshing_data_bindings()

  def search_bar_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.search_bar.text == "":
      self.form_refreshing_data_bindings()
    else:
      self.repeating_panel_clients.items = anvil.server.call('search_clients', self.search_bar.text)
    


 




