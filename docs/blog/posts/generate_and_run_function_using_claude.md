---
draft: false
date: 2024-10-20
categories:
  - ai, claude, python
comments: true
---

# Python Code Generation using the API for Claude AI

Generating and running a simple Python function using Anthropic Claude APIs.

<!-- more -->

The following shows how we can use the Anthropic Claude LLM API to generate a simple Python function and run it.  We tell the API what we want our function to do; Claude AI API generates the code; we save this code to a file and function; then run it.

The code (also found [here](https://github.com/mappertec/mappertec/blob/1ce53c183a704ea5e360e78e4b9890687f9fc3a2/gists/00_simple_ai_code_gen.py)):


```python
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
```

We're using the [Anthropic SDK library for Python](https://github.com/anthropics/anthropic-sdk-python) to access the API:

```python
import anthropic
```

If you want to run this example you'll have to install it:

`pip install anthropic`

Then we create a client:

```python
client = anthropic.Anthropic()
```

By default, the SDK looks at the value of `ANTHROPIC_API_KEY` which was set to the key secret beforehand.  See [here](https://docs.anthropic.com/en/api/getting-started) for instructions on how to request an API key, note that this requires setting up billing.  Generating the example here costs fractions of a UK penny.

We create a function that takes a string `prompt` and returns the text containing the result of running the prompt on the API.  The `model`, `max_tokens` and `messages` attributes are set; `messages` takes the prompt string as a dictionary attribute.

```python
def generate_code(prompt):
    return client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    ).content[0].text
```

We create a function to write the API response to a python file.  This function takes two arguments, `module_name` and `code`:

```python
def write_function(module_name, code):
    f = open(module_name + ".py", "w")
    f.write(code)
    f.close()
```

Now we have a Python module containing the response from the API and we know the module name and function name we can create a function to run it and print the results:

```python
def run_function(module_name, function_name, a, b):
    module = __import__(module_name)
    print(getattr(module, function_name)(a, b))
```

This function imports the module name and runs the function, passing in two parameters `a` and `b`, printing the output.

Finally we can create a `main` block, create a prompt by concatenating strings and run the functions:

```python
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
```

We are saving the function `is_even` in a module named `maths`.  The string prompt we are passing to the API is:

```text
Write a function in Python called is_even.
The function should accept two integers.
The function should return a boolean.
The function should do the following:
1. Return true if the sum of the integers is even.
2. Return false if the sum of the integers is odd.
Do not include any markdown, code block indicators or description.
```

The content of maths.py (which is the response from the Claude API to the prompt) is:

```python
def is_even(num1, num2):
    return (num1 + num2) % 2 == 0
```

And when the script is run this is the output:

```shell
False
True
```

Which is correct since 2 + 3 is odd and 5 + 7 is even.