import requests
import json
          
url = "https://api.openai.com/v1/completions"


headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}

print("--------------------------------------------------------")
import openai
openai.api_key = "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"



def get_response(input_text):
 print("hi ")
# Initialize the conversation with the first chunk of input
 conversation = openai.Moderation.create(
 #engine="davinci",
 prompt=input_text[:2048],
 max_tokens=2048,
 stop=None)
 response_chunks = [conversation.latest_message().text]
 # Loop over the remaining chunks of input and send them to ChatGPT
 for i in range(2048, len(input_text), 2048):
     chunk = input_text[i:i+2048]
     conversation = openai.Conversation.retrieve(conversation.id)
     response = conversation.append(chunk, max_tokens=2048, stop=None)
     response_chunks.append(response.choices[0].text)
     
 # Combine the response chunks to form the complete response
 response = "".join(response_chunks)
 return response
 
 
 
 # Read the JSON data from a file
with open('Transactions.json') as json_data:
 data = json.load(json_data)
 jsonlines=json.dumps(data)
 
response= get_response("Hello, how are you?")
print(response)