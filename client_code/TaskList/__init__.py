from ._anvil_designer import TaskListTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ActivityCreationView import ActivityCreationView
from ..TaskCreationView import TaskCreationView


class TaskList(TaskListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.form_refreshing_data_bindings()

    # Any code you write here will run before the form opens.

  def new_task_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=TaskCreationView(), buttons=None, large=True, dismissible=False)
    if new_popup == "success":
      notif = Notification("Task created successfully", title="Success", style="success").show()
      self.form_refreshing_data_bindings()

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""

    tasks = anvil.server.call('get_task')
    self.repeating_panel_tasks.items = tasks

  def add_activity_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=ActivityCreationView(), buttons=None, large=True, dismissible=False)
    if new_popup == "success":
      notif = Notification("Activity created successfully", title="Success", style="success").show()
      self.form_refreshing_data_bindings()

  def search_bar_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.search_bar.text == "":
      self.form_refreshing_data_bindings()
    else:
      self.form_refreshing_data_bindings(self.search_bar.text)



