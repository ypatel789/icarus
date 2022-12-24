from ._anvil_designer import ContactCreationViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ContactCreationView(ContactCreationViewTemplate):
  def __init__(self, row=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    clients = anvil.server.call('get_clients')
    if row == None: 
      self.client.items = [(r["client_name"],r) for r in clients]
    # --------------------------------------------------------------------
    self.row = row
    if row != None:
      self.label_1.text = "Edit Contact"
      self.client.visible=False
      self.first_name.text = row["first_name"]
      self.last_name.text = row["last_name"]
      self.email.text = row["email"]
      self.title.text = row["title"]
      self.office_number.text = row["office_number"]
      self.mobile_number.text = row["mobile_number"]
      self.fax_number.text = row["fax_number"]
      
      self.button_1.set_event_handler("click", self.update_contact)
    # Any code you write here will run before the form opens.
  def update_contact(self, **event_args):
    """This method is called when editing an existing client"""

    input_first_name = self.first_name.text
    input_last_name = self.last_name.text
    input_email = self.email.text
    input_title = self.title.text
    input_onumber = self.office_number.text
    input_mnumber = self.mobile_number.text
    input_fnumber = self.fax_number.text

    if ((input_first_name == "") or (input_email == "")):
      n = Notification("Please enter first name and email!", title="Error", style="danger").show()
    else:
      anvil.server.call('update_contact_by_id',self.row.get_id(), input_first_name, input_last_name, input_email, input_title, input_onumber, input_mnumber, input_fnumber)
      self.raise_event("x-close-alert", value="updated")
      

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value="ur_mum")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_client = self.client.selected_value
    input_first_name = self.first_name.text
    input_last_name = self.last_name.text
    input_email = self.email.text
    input_title = self.title.text
    input_onumber = self.office_number.text
    input_mnumber = self.mobile_number.text
    input_fnumber = self.fax_number.text

    if ((input_first_name == "") or (input_email == "")):
      n = Notification("Please enter first name and email!", title="Error", style="danger").show()
    elif input_client != None:
      anvil.server.call('create_contact', input_client, input_first_name, input_last_name, input_email, input_title, input_onumber, input_mnumber, input_fnumber)
      self.raise_event("x-close-alert", value="success")
    else:
      n = Notification("Please select a valid client!", title="Error", style="danger").show()

  def delete_contact_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Do you wish to delete this contact?")
    if c:
      anvil.server.call("delete_contact", self.row)
      self.raise_event("x-close-alert", value="deleted")

    




