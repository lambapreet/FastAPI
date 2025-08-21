from fastapi import FastAPI
from tabels import create_table
from services import create_user, create_post,get_user,get_all, get_post, update_user, delete_post


app = FastAPI()

create_table()

# name = input("Enter the name: ")
email = input("Enter the email: ")

# create_user(name,email)

user_id = int(input("Enter the User id:"))
# title = input("Enter the title: ")
# content = input("Enter the content: ")

# create_post(user_id,title,content)

# print(get_user(user_id))

# print(get_all())

# print(get_post(1))

# update_user(user_id, email)

delete_post()
