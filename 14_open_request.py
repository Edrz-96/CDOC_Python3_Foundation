import os, json, openai

key = "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"


def ask_open_ai(p, k):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=p,
                                        temperature=0.1,
                                        max_tokens=100,
                                        top_p=1,
                                        n=1,
                                        stop=None,
                                        frequency_penalty=0,
                                        presence_penalty=0,
                                        api_key=k)
    return response.choices[0].text


try:
    output = ask_open_ai(input(), key)
except Exception as e:
    print(e)
else:
    print(output)
