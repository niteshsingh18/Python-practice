from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

command = '''

[15:03, 02/09/2024] Maa: Hi kya aap mujhe coding k baare me bata sakte h
[15:03, 02/09/2024] Nitesh: haan mai pahle aapko coding laguages k baare me batata hu

'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Nitesh who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Nitesh"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)