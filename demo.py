import requests
import json
url = "https://api.openai.com/v1/completions"


headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}

data =  open('Transactions.json', 'r')
Jsondata=data.read()
obj=json.loads(Jsondata)
print(len(obj))

for i in range(len(obj["Sheet 1"])):
  data1 = {
           "model": "text-davinci-003",
           "prompt":str(obj["Sheet 1"][i])+"| how many UP transactions greater than 500? show me those only ",
           "temperature": 0,
           "max_tokens": 100,
           "top_p": 1,
           "frequency_penalty": 0,
           "presence_penalty": 0}
  response = requests.post(url, headers=headers,json=data1)
  #print(response.status_code)
    #print(response.json())
  jData= json.dumps(response.json())
  parsed_data = json.loads(jData)
  outp=parsed_data["choices"]
    #print(outp)
  reply=outp[0]
  print(reply["text"])
