import os
llm_config = {
    'ChatGPT': {
        'api_key': os.environ.get('OPENAI_API_KEY'),
        'model_name': 'gpt-4o-mini',
        'base_url': 'https://api.openai.com/v1'
    },
    'DeepSeek': {
        'api_key': os.environ.get('DEEPSEEK_API_KEY'),
        'model_name': 'deepseek-chat',
        'base_url': 'https://api.deepseek.com/v1'
    }
}