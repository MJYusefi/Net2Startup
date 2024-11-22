import requests
val = {"username" : "USR", "password" : "PASS"}
r = requests.post("https://net2.sharif.edu/login", params=val)
print(r.status_code)

