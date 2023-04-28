import openai

openai.api_key = ""

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()
