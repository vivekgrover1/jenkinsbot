import pickledb

def get_status(user):

  db = pickledb.load('jenkinsbot.db', False)
  return db.get(user)

def update_status(user):

  db = pickledb.load('jenkinsbot.db', False)
  db.set(user, 'Approved')
  print (db.get(user))
  db.dump()


def add_user(user):

  db = pickledb.load('jenkinsbot.db', False)
  db.set(user, 'Not Approved')
  db.dump()


