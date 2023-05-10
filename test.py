import requests
import json
          
url = "https://api.openai.com/v1/completions"


headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}
headers1 = {'User-Agent': 'ceilometerclient.openstack.common.apiclient',
           'X-Auth-Token': 'A0007898393509957505790!adt6eTHtqQjWWShVg+wmKgLdsIvdV7eNJ59whybllS03n2d/k6NFvlatI8dCgEBtfakqMA4UxE38XEPBuwSY7KdnAyE='
           }
#res = requests.get("https://core-api.partner-shared-sandbox.tmachine.io/v1/balances/2348_4ae44aae-cb36-4f6a-8d30-f9f543f1eb1d",headers=headers)
#print(res.json())

print("___________________________________________________________________________________________________________________________")

# open the json file
with open('tranjson.json', 'r') as f:
    # load the data
    data = json.load(f)


# convert the data to jsonlines
jsonlines = json.dumps(data, indent=4, sort_keys=True)

# print the jsonlines
#print(jsonlines)




print("---------------------------------------------------------------------------------")


data = {
  "model": "text-davinci-003",
  "prompt":jsonlines+"| how many UP transactions greater than 500?",
  "temperature": 0,
  "max_tokens": 100,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
#print(response.json())
jData= json.dumps(response.json())
parsed_data = json.loads(jData)
outp=parsed_data["choices"]
#print(outp)
reply=outp[0]
print(reply["text"])















