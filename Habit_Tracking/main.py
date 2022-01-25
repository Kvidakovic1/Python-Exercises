import requests
from datetime import datetime

USERNAME = "kristijan"
TOKEN = "hafdaga134312"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hafdaga134312",
    "username": "kristijan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"

}


today = datetime.now()

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages have you red today? "),

}




#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#response = requests.delete(url="https://pixe.la/v1/users/kristijan/graphs/graph1/20220125", headers=headers)
#print(response.text)

response = requests.post(url="https://pixe.la/v1/users/kristijan/graphs/graph1", json=pixel, headers=headers)
print(response.text)

