import openai
openai.api_key = "enterApi"



def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


user = input(">>> ")
strip_text = user.split(">>> ")

def convert_to_text(stripped_text):
    raw = ""

    return raw.join(stripped_text)


result = get_completion(convert_to_text(strip_text))
print(result)