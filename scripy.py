import sys
import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://google.com")
if __name__ == "__main__":
    print(r.status_code)
    print("HELLO~~~~")
