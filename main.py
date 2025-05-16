import os, chainlit as cl
import chainlit as cl
from langchain_community.chat_models import ChatOpenAI
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv
import os, openai, elevenlabs


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs.set_api_key(os.getenv("ELEVENLABS_API_KEY"))

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

@cl.on_message
async def main(message: cl.Message):
    prompt = f"You are Virtual Edy, a senior AI + networking architect. Answer like a Senior Arhitect: {message.content}"
    response = llm.predict(prompt)

    # ✅ Generate voice
    audio = generate(
        text=response,
        voice="Aria",  # <- Voce free
        model="eleven_monolingual_v1"
    )

    # 💬 Text + 🔊 Voce
    await cl.Message(content=response).send()
    await cl.Message(author="Virtual Edy", content="[voice]", audio=audio).send()
    play(audio)
