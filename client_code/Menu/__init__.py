from ._anvil_designer import MenuTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Menu(MenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def logout_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    open_form("StartUpModule")

  def manage_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Manage')

  def projects_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Projects')

  def invoices_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Invoices")

  def team_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Team')

  def time_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Time')





    





