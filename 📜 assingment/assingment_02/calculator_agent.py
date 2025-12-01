# assignment_02/simple_agent.py

from openai import OpenAI
import time


# 1️⃣ Create a client with your OpenAI API key
client = OpenAI()

# 2️⃣ Define a simple Python tool: adding two numbers
def add_numbers(a: float, b: float) -> float:
    return a + b

# 3️⃣ Register the tool with the agent (for OpenAI API, this is just metadata; the function is not actually called)
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Adds two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]


# 4️⃣ Create an assistant agent with the tool
assistant = client.beta.assistants.create(
    name="Calculator Agent",
    instructions="You are a calculator that adds two numbers. Use the add_numbers tool.",
    tools=tools,
    model="gpt-4o"
)

# 5️⃣ Create a thread for the conversation
thread = client.beta.threads.create()

# 6️⃣ Send a message to the agent
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Add 10 and 5 using the add_numbers tool."
)

# 7️⃣ Run the agent
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# 8️⃣ Poll for the run to complete

while True:
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run_status.status == "completed":
        break
    time.sleep(1)

# 9️⃣ Retrieve and display the result
messages = client.beta.threads.messages.list(thread_id=thread.id)
for msg in messages.data:
    if hasattr(msg, "content") and msg.content and hasattr(msg.content[0], "text"):
        print(f"{msg.role.upper()}: {msg.content[0].text.value}")
    elif hasattr(msg, "content") and msg.content and hasattr(msg.content[0], "function_call"):
        # If the assistant is requesting a function call, handle it manually
        func_call = msg.content[0].function_call
        if func_call.name == "add_numbers":
            args = func_call.arguments
            a = args.get("a")
            b = args.get("b")
            result = add_numbers(a, b)
            print(f"ASSISTANT: The result of adding {a} and {b} is {result}")

