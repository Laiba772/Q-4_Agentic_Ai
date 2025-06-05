
import os 
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# Load environment variables from .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Define the model to use
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# Create an agent with the model.
agent = Agent(
    name="Greeting Agent",
    instructions="You are a Greeting Agent, Your task is to greet the user with a friendly message, when someone hi you've reply back with salam with Laiba Naz, if someone says bye then reply with Khuda Hafiz with Laiba Naz, when someone asks other than greeting than say Laiba is here just for greeting, i can't answer anyting else soory.",
    model=model,
)


# Create a runner to run the agent.

user_question = input("Enter your question: ")

result = Runner.run_sync(agent, user_question)

# Print the result
print(result.final_output)

