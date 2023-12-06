import http.client
conn = http.client.HTTPSConnection("api.ultramsg.com")
payload = "token=1v941eyo9eqixrsi&to=14155552671&body=WhatsApp API on UltraMsg.com works good&priority=10&referenceId="
headers = { 'content-type': "application/x-www-form-urlencoded" }
conn.request("POST", "/instance16/messages/chat", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))