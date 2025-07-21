# ✅ Assignment 3: Country Info Toolkit (Gemini Version with Agent SDK)
# This script provides basic country-related information using @function_tool and a Gemini-compatible Agent.

# country_info_toolkit.py - Gemini compatible version using @function_tool

import requests
from agents import Agent, Runner
from agents.tool import function_tool

@function_tool
def get_country_info(country: str) -> str:
    """Fetch basic country info from REST Countries API."""
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        name = data.get("name", {}).get("common", "N/A")
        capital = data.get("capital", ["N/A"])[0]
        region = data.get("region", "N/A")
        population = data.get("population", "N/A")
        currency_data = list(data.get("currencies", {}).values())[0]
        currency = currency_data.get("name", "N/A")

        return (f"🌍 Country: {name}\n"
                f"🏛️ Capital: {capital}\n"
                f"📍 Region: {region}\n"
                f"👥 Population: {population}\n"
                f"💰 Currency: {currency}")
    else:
        return f"Sorry, I couldn't find info about '{country}'. Please try another country."

if __name__ == "__main__":
    user_input = input("Enter a country name: ")
    agent = Agent(name="Country Info Agent", tools=[get_country_info])
    result = Runner().run_sync(agent=agent, input=user_input)
    print(f"\n🗺️ Info:\n{result.output}")
