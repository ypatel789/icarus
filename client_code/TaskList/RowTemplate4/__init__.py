from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...TaskCreationView import TaskCreationView

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.task_name.text = self.item["task"]
    self.repeating_panel_activity.items = self.item["activity"]

    # Any code you write here will run before the form opens.

  def edit_task_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_popup = alert(content=TaskCreationView(self.item), buttons=None, large=True, dismissible=False)
    if new_popup == "updated":
      notif = Notification("Task updated successfully", title="Success", style="success").show()
      self.parent.parent.parent.form_refreshing_data_bindings()
    

