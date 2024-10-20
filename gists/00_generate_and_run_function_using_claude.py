import anthropic

client = anthropic.Anthropic()

def generate_code(prompt):
    return client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    ).content[0].text

def write_function(module_name, code):
    f = open(module_name + ".py", "w")
    f.write(code)
    f.close()

def run_function(module_name, function_name, a, b):
    module = __import__(module_name)
    print(getattr(module, function_name)(a, b))

if __name__ == '__main__':
    module_name = "maths"
    function_name = "is_even"
    prompt = f"Write a function in Python called {function_name}. "
    prompt += "The function should accept two integers. "
    prompt += "The function should return a boolean. "
    prompt += "The function should do the following: "
    prompt += "1. Return true if the sum of the integers is even. "
    prompt += "2. Return false if the sum of the integers is odd. "
    prompt += "Do not include any markdown, code block indicators or description. "

    code = generate_code(prompt)
    write_function(module_name, code)
    run_function(module_name, function_name, 2, 3)
    run_function(module_name, function_name, 5, 7)