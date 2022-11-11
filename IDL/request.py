import requests

payload = {'content-type':'application/json', 'x-access-token':'5443b693E341cb0ab695Xb8'}
r = requests.get("https://safe-payy.herokuapp.com/api/v1/safepay/querypayment/initiated", headers=payload)

f = open("initiated_transactions.txt", "w")
f.write(r.text)
f.close