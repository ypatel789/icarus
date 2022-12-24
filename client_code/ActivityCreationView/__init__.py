from ._anvil_designer import ActivityCreationViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ActivityCreationView(ActivityCreationViewTemplate):
  def __init__(self, row=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    tasks = anvil.server.call('get_task')
    if row == None: 
      self.task.items = [(r["task"],r) for r in tasks]
    # --------------------------------------------------------------------
    self.row = row
    if row != None:
      self.title_activity.text = "Edit Activity"
      self.task.visible=False
      self.activity_name.text = row["activity"]
      
      self.save_activity.set_event_handler("click", self.update_activity)
    # Any code you write here will run before the form opens.
  def update_activity(self, **event_args):
    """This method is called when editing an existing client"""

    input_activity_name = self.activity_name.text
    
    if (input_activity_name == ""):
      n = Notification("Please enter activity!", title="Error", style="danger").show()
    else:
      anvil.server.call('update_activity_by_id', self.row.get_id(), input_activity_name)
      self.raise_event("x-close-alert", value="updated")
      
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value="ur_mum")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_task = self.task.selected_value
    input_activity_name = self.activity_name.text

    if (input_activity_name == ""):
      n = Notification("Please enter activity", title="Error", style="danger").show()
    elif input_task != None:
      anvil.server.call('create_activity', input_task, input_activity_name)
      self.raise_event("x-close-alert", value="success")
    else:
      n = Notification("Please select a valid task!", title="Error", style="danger").show()
