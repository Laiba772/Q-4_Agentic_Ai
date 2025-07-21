import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
from agents.run import RunConfig

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Gemini client setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

# Run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# ✅ TOOL FUNCTION
@function_tool
def suggest_health_product(symptom: str) -> str:
    symptom = symptom.lower()
    if "headache" in symptom:
        return "💊 *Panadol* – effective for relieving headaches due to paracetamol."
    elif "fever" in symptom:
        return "🌡️ *Ibuprofen* – commonly used to reduce fever and inflammation."
    elif "cough" in symptom:
        return "🧴 *Robitussin syrup* – helpful for dry or wet cough relief."
    elif "pain" in symptom:
        return "🦴 *Paracetamol or Naproxen* – general pain relievers for mild discomfort."
    else:
        return "❗ I'm not sure. Please consult a pharmacist or doctor."

# ✅ MAIN EXECUTION
if __name__ == "__main__":
    agent = Agent(
        name="Smart Store Agent",
        instructions="""
        You are a smart health product assistant. A user will describe a symptom, and you will suggest an appropriate OTC product (not medical advice).

        Use the `suggest_health_product` tool to give clear and short suggestions.
        Keep responses helpful, safe, and 1–2 lines long.
        """,
        tools=[suggest_health_product],
        model=model
    )

    user_input = input("👤 What symptom are you experiencing? \n> ")
    result = Runner.run_sync(agent=agent, input=user_input, run_config=config)
    print(f"\n✅ Suggested Product:\n{result.final_output}")
