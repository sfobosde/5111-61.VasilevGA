import UserController

user1 = UserController.User_Controller()
user2 = UserController.User_Controller()

print(user2.encode_text(user1.send_message("My name")))