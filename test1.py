import requests
import json
headers1 = {'User-Agent': 'ceilometerclient.openstack.common.apiclient',
           'X-Auth-Token': 'A0007898393509957505790!adt6eTHtqQjWWShVg+wmKgLdsIvdV7eNJ59whybllS03n2d/k6NFvlatI8dCgEBtfakqMA4UxE38XEPBuwSY7KdnAyE='
           }
url = "https://api.openai.com/v1/completions"


headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}

res = requests.get("https://core-api.partner-shared-sandbox.tmachine.io/v1/posting-instruction-batches?page_size=3&account_ids=LTIM43074690",headers=headers1)
json_lineData= json.dumps(res.json())
#print(json_lineData)

# Create the payload for the request
payload = {
    'context': []
}




# Read the JSON data from a file
#with open('Transactions.json') as json_data:

data = json.load(res.json())
    # Add the data to the payload
payload['context'].append(data)

# Send the request to the API
response = requests.post(url, headers=headers, data=json.dumps(payload))


print(response.status_code)
#print(response.json())
jData= json.dumps(response.json())
parsed_data = json.loads(jData)
outp=parsed_data["choices"]
#print(outp)
reply=outp[0]
print(reply["text"])
