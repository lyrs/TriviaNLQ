import openai
openai.api_key = "[API KEY]"

def translate_to_sparql(text):
  prompt = f"translate the following text to SPARQL: {text}"
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )
  return response["choices"][0]["text"]

text = input("Ask a Question: ")
sparql_query = translate_to_sparql(text)
print(sparql_query)