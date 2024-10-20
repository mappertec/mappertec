import anthropic

client = anthropic.Anthropic()

content = "Write a function in Python called iseven(). "
content += "The function should accept two integers. "
content += "The function should return a boolean. "
content += "The function should do the following: "
content += "1. Return true if the sum of the integers is even. "
content += "2. Return false if the sum of the integers is odd. "
content += "Do not include any markdown, code block indicators or description. "

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": content}
    ]
)

def generateCode():
    f = open("utils.py", "w")
    f.write(message.content[0].text)
    f.close()

if __name__ == '__main__':
    generateCode()
    import utils
    print(utils.iseven(2, 3))