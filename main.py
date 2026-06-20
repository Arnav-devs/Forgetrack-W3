import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

# ------------------ SETUP -------------------- #
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("API Key not found!")
    exit()

client = genai.Client(api_key=API_KEY)

# ------------------ SYSTEM PROMPT -------------------- #
SYSTEM_PROMPT = """
You are a world-class mentor and Distinguished Principal Educator known for simplifying difficult subjects into beginner-friendly learning paths.

Generate a beginner-to-master roadmap.

Constraints:
- Structure into two phases:
  Phase 1: Fundamentals
  Phase 2: Advanced Application
- Maximum 250 words total.
- Each subtopic must be a single line.
- Use clean bullet points.
- DO NOT generate long paragraphs.
- DO NOT exceed the requested structure.

Output Format:

==================================================
            AI POWERED STUDY ASSISTANT
==================================================

1. Basics
• 5-6 important topics with one-line descriptions

2. Advanced Concepts
• 5-6 important topics with one-line descriptions

3. Practice
• 2-3 practice questions

Outcome
One sentence describing what the learner will achieve.

==================================================


"""

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)


# -------------------- FUNCTIONS -------------------- #
def generate_roadmap(chat_session, topic):
    try:
        response = chat_session.send_message(
            f"User Topic: {topic}"
        )

        return response.text if response.text else "No response generated."

    except APIError as e:
        return f"Error {e.code}: {e.message}"


def followup(chat_session, question):
    try:
        response = chat_session.send_message(question)

        return response.text if response.text else "No response generated."

    except APIError as e:
        return f"Error {e.code}: {e.message}"


# -------------------- MAIN PROGRAM -------------------- #
def main():

    print("=" * 50)
    print(f"{'AI POWERED STUDY ASSISTANT':^50}")
    print("=" * 50)

    topic = input("\nEnter a topic to study: ").strip()

    if not topic:
        print("Topic cannot be empty!")
        return

    # Generate roadmap
    roadmap = generate_roadmap(chat, topic)

    print("\n" + roadmap + "\n")

    question_count = 1

    while True:

        user_input = input(
            "\nAsk a follow-up question (type 'exit' to quit): "
        ).strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            break

        answer = followup(chat, user_input)

        print("\n" + answer + "\n")

        question_count += 1

    # Session Summary
    print("\n" + "=" * 50)
    print(f"{'SESSION SUMMARY':^50}")
    print("=" * 50)
    print(f"Topic Studied : {topic}")
    print(f"Questions Asked : {question_count}")
    print("=" * 50)


# -------------------- RUN PROGRAM -------------------- #
if __name__ == "__main__":
    main()