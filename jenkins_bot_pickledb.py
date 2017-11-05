from tinydb import TinyDB, Query

def get_status(user):

  db = TinyDB('tinydb.json')
  User = Query()
  userdata=db.search(User.username == user)
  if userdata == []:
   return None
  return userdata[0]['status']

def update_status(user):

  db = TinyDB('tinydb.json')
  User = Query()
  db.update({'status':'Approved'},User.username == user)


def add_user(user):

  db = TinyDB('tinydb.json')
  User = Query()
  userdata=db.search(User.username == user)
  if userdata == []:
   db.insert({'username': user, 'status': 'Not Approved'})
