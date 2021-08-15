import sys
import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://google.com")

print(r.status_code)
print(r.ok)
print("hello")


class Pyclass:
    def run(self):
        a = 5
        return a
