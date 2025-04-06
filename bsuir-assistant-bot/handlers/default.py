from aiogram import Router
from aiogram.types import Message
from services.api_service import ApiService

# Инициализация сервиса
api_service = ApiService()

default_router = Router()

@default_router.message()
async def process_message(message: Message):
    model_answer = await api_service.get_response(message.text)

    if model_answer.startswith("Ассистент недоступен сейчас. Посмотрите на картинку кота:"):
        image_url = model_answer.split("\n")[-1]  
        await message.answer_photo(
            caption=model_answer.split("\n")[0],
            photo=image_url
        )
    else:
        await message.answer(
            text=model_answer
        )