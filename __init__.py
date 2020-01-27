from google.appengine.api.users import User

def patch_email(self):
    return self._old_email().replace('@mongodb.com', '@10gen.com')

User._old_email = User.email
User.email = patch_email
