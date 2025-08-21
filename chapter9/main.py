from fastapi import FastAPI
from tabels import create_table
from services import create_user, create_post, order_user, order_post, count_post, join_user


app = FastAPI()

create_table()


# create_user("sonam","sonam@gmail.com")
# create_user("raj","raj@gmail.com")
# create_post(1,"World","World Book")
# create_post(2,"Hello","Hello Book")

# print(order_user())

# print(order_post())


# print(count_post())

print(join_user())