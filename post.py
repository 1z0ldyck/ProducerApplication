# module for posting on the api

import requests
import json

usuario = {
  "People": {
    "name": "Lucas",
    "age": 20
  }
}

# post person data in api
r = requests.post("http://localhost:5000/post_person", data=json.dumps(usuario))


print(f"Status code: {r.status_code}, message: {r.text}")
