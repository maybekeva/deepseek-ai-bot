API_URL = 'https://api.deepseek.com/v1/chat/completions'

# Тестовый секретный ключ для проверки срабатывания TruffleHog (НЕ настоящий)
API_SECRET_TOKEN = "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"

def ask_deepseek(prompt):
    headers = {"Authorization": f"Bearer {API_SECRET_TOKEN}"}
    return headers
