import requests

response = requests.get("https://evisa.mfa.ir/en/")
print(response.status_code)