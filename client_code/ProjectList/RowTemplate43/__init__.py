from ._anvil_designer import RowTemplate43Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate43(RowTemplate43Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.client_name.text = self.item["client_name"]

    # Any code you write here will run before the form opens.
