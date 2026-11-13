import os

API_URL = 'https://api.deepseek.com/v1/chat/completions'

# Безопасное получение ключа из переменных окружения
API_SECRET_TOKEN = os.getenv("DEEPSEEK_API_KEY")

def ask_deepseek(prompt):
    headers = {"Authorization": f"Bearer {API_SECRET_TOKEN}"}
    return headers
