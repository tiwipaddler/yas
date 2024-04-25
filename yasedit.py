import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
response = client.images.edit(
  model="dall-e-2",
  image=open("yas.png", "rb"),
  mask=open("yasmask.png", "rb"),
  prompt=input("Describe what you are after:"),
  n=1,
  size="1024x1024"
)
print(f"Edit: {response.data[0].url}")