import requests

req = request.get('https://www.daangn.com/')
html = req.text
print(html)