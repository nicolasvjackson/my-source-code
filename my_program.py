import os
import requests

actions = ["POST", "PUT"]

api_key = "ff7b6a574f9e054809f49ade185d30f5"

for action:
    print(requests(f"{action} Bearer: {api_key}"))
