import openai

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()
