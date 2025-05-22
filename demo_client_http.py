import http.client

host = "132.168.57.253"
conn = http.client.HTTPConnection(host, 5000)
conn.request("GET", "/config")
response = conn.getresponse()
content = response.read().decode()
print(content)