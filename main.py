import openai

openai.api_key = "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"

try:
    print(openai.Model.list())
except Exception as e:
    print(f"Error: {e}")

prompt = "Create a list of first names"
response = openai.Completion.create(model="text-davinci-003", prompt= prompt, max_tokens=30)

print(response)