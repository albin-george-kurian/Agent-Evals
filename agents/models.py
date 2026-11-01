from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os


load_dotenv()


model = init_chat_model('groq:openai/gpt-oss-120b')

# response = model.invoke('tell me about the a perfect romantic pitch line')
# print(response.content)


