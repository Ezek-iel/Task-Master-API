import requests

BASE = "http://127.0.0.1:5000"

data = {"details" : 'Wash The car'}
requests.put(url = BASE + "/task/54cd061d-8184-4815-93d0-447862fd28e7", data = data)

