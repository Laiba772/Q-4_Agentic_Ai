# mood_handoff.py


import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.tool import function_tool

load_dotenv()

# 🎵 Music Tool
@function_tool
def suggest_music(mood: str) -> str:
    if "happy" in mood.lower():
        return "How about 'Happy' by Pharrell Williams?"
    elif "sad" in mood.lower():
        return "Try 'Someone Like You' by Adele."
    else:
        return "Try lo-fi beats to relax your mood."

# 🎬 Movie Tool
@function_tool
def suggest_movie(mood: str) -> str:
    if "happy" in mood.lower():
        return "Watch 'The Pursuit of Happyness' – it’ll uplift you more!"
    elif "sad" in mood.lower():
        return "Maybe try 'Inside Out' – it’s comforting."
    else:
        return "Try 'Forrest Gump' – always a good pick."

# 🧘‍♀️ Activity Tool
@function_tool
def suggest_activity(mood: str) -> str:
    if "happy" in mood.lower():
        return "Go for a walk or dance to your favorite music!"
    elif "sad" in mood.lower():
        return "Try journaling or some light meditation."
    else:
        return "Try a creative activity like painting or doodling."

# Create specialized agents
music_agent = Agent(name="🎵 Music Suggestions", tools=[suggest_music])
movie_agent = Agent(name="🎬 Movie Suggestions", tools=[suggest_movie])
activity_agent = Agent(name="🧘‍♀️ Activities", tools=[suggest_activity])

# Handoff Agent
main_agent = Agent(
    name="Mood Assistant",
    instructions="Route to music, movie, or activity agents based on user preference.",
    agents=[music_agent, movie_agent, activity_agent]
)

if __name__ == "__main__":
    user_input = input("👤 How are you feeling today or what would you like (music/movie/activity)?\n> ")
    result = Runner().run_sync(agent=main_agent, input=user_input)
    print(f"\n✅ Response:\n{result.output}")
