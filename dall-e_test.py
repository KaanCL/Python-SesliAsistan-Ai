from openai import OpenAI
import credentials

OPENAI_API_KEY=credentials.OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.generate(
  model="dall-e-2",
  prompt="köpekler parkta kedilerle oynuyor",
  size="512x512",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)