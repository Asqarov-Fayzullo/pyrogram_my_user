from loader import user

@user.on_message()
def all(client,message):
    message.forward('me')