MODEL = 'deepseek-chat'
TEMPERATURE = 0.7
MAX_TOKENS = 1000
VERSION = '1.0.0'
TOP_P = 0.9

def get_config():
    return {
        "model": MODEL,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": MAX_TOKENS
    }
