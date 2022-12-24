import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def validate_login():
  if anvil.users.get_user() != None:
    return True
  else:
    return False

@anvil.server.callable
def create_client(name, address):
  if validate_login() == True:
    app_tables.clients.add_row(client_name=name, address=address)

@anvil.server.callable
def get_clients():
  if validate_login() == True:
    data = app_tables.clients.search(tables.order_by("client_name"))
    return data

@anvil.server.callable
def update_client_by_id(id, name, address):
  if validate_login() == True:
    client = app_tables.clients.get_by_id(id)
    client['address'] = address
    client['client_name'] = name

@anvil.server.callable
def search_clients(query):
  if validate_login() == True:
    result = app_tables.clients.search()
    filter = []
    for client in result:
      if query.lower() in client["client_name"].lower():
        filter += [client]    
    return filter

@anvil.server.callable
def create_contact(input_client, input_first_name, input_last_name, input_email, input_title, input_onumber, input_mnumber, input_fnumber):
  if validate_login() == True:
    row = app_tables.contacts.add_row( 
      first_name=input_first_name, 
      last_name=input_last_name, 
      email=input_email, 
      title=input_title, 
      office_number=input_onumber, 
      mobile_number=input_mnumber, 
      fax_number=input_fnumber)
    if input_client["contacts"] == None:
      input_client["contacts"] = [row]
    else:
      input_client["contacts"] += [row]
    

@anvil.server.callable
def get_contacts(id):
  if validate_login() == True:
    client = app_tables.clients.get_by_id(id)
    data = app_tables.contacts.search(tables.order_by("first_name"), client = client)
    return data

@anvil.server.callable
def get_contact_by_id(id):
  if validate_login() == True:
    contact = app_tables.contacts.get_by_id(id)
    return contact

@anvil.server.callable
def update_contact_by_id(id, input_first_name, input_last_name, input_email, input_title, input_onumber, input_mnumber, input_fnumber):
  if validate_login() == True:
    contact = app_tables.contacts.get_by_id(id)
    contact["first_name"]=input_first_name
    contact["last_name"]=input_last_name
    contact["email"]=input_email 
    contact["title"]=input_title
    contact["office_number"]=input_onumber 
    contact["mobile_number"]=input_mnumber 
    contact["fax_number"]=input_fnumber

@anvil.server.callable
def delete_contact(row):
  if validate_login() == True:
    clients = app_tables.clients.search()
    for client in clients:
      if client["contacts"] != None:
        for contact in client["contacts"]:
          if contact == row:
            client["contacts"].remove(row)
            break
    row.delete()

@anvil.server.callable
def create_task(task):
  if validate_login() == True:
    app_tables.tasks.add_row(task=task)

@anvil.server.callable
def get_task():
  if validate_login() == True:
    data = app_tables.tasks.search(tables.order_by("task"))
    return data

@anvil.server.callable
def update_task_by_id(id, task):
  if validate_login() == True:
    row = app_tables.tasks.get_by_id(id)
    row['task'] = task

@anvil.server.callable
def create_activity(input_task, input_activity_name):
  if validate_login() == True:
    row = app_tables.activity.add_row( 
      activity=input_activity_name)
    if input_task["activity"] == None:
      input_task["activity"] = [row]
    else:
      input_task["activity"] += [row]


@anvil.server.callable
def get_activity(id):
  if validate_login() == True:
    task = app_tables.tasks.get_by_id(id)
    data = app_tables.activity.search(tables.order_by("activity"), task=task)
    return data

@anvil.server.callable
def get_activity_by_id(id):
  if validate_login() == True:
    activity = app_tables.activity.get_by_id(id)
    return activity

@anvil.server.callable
def update_activity_by_id(id, input_activity_name):
  if validate_login() == True:
    activity = app_tables.activity.get_by_id(id)
    activity["activity"]=input_activity_name