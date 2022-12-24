from ._anvil_designer import TaskCreationViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TaskCreationView(TaskCreationViewTemplate):
  def __init__(self, row=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.row = row
    if row != None:
      self.title_task.text = "Edit Task"
      self.task_name.text = row["task"]
      self.save_task.set_event_handler("click", self.update_task)
    # Any code you write here will run before the form opens.
  def update_task(self, **event_args):
    """This method is called when editing an existing task"""
    input_task = self.task_name.text

    anvil.server.call('update_task_by_id', self.row.get_id(), input_task)
    self.raise_event("x-close-alert", value="updated")

  def save_task_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_task = self.task_name.text

    if (input_task == ""):
      n = Notification("Please enter task name", title="Error", style="danger").show()
    else:
      anvil.server.call('create_task', input_task)
      self.raise_event("x-close-alert", value="success")


  def cancel_task_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value="ur_mum")


