from ._anvil_designer import ManageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Manage(ManageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def tasks_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.manage_clients_card.visible = False
    self.manage_tasks_card.visible = True

  def clients_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.manage_clients_card.visible = True
    self.manage_tasks_card.visible = False




    

