import httpx


async def get_llm_response(message: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "HTTP-Referer": "https://your-site.com",
        "X-Title": "Your Site Name"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
