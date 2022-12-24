from ._anvil_designer import ProjectListTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ProjectCreationView import ProjectCreationView

class ProjectList(ProjectListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.form_refreshing_data_bindings()

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, query=None, **event_args):
      """This method is called when refreshing_data_bindings is called"""
      
      clients = anvil.server.call('get_clients')
      self.repeating_panel_clients.items = clients

