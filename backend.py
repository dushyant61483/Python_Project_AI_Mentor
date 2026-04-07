import os
from dotenv import load_dotenv
from groq import Groq
from instructions import mentor_instructions

load_dotenv()


MODEL_NAME = "llama-3.1-8b-instant"
MAX_TOKENS = 1500
TEMPERATURE = 0.7
MAX_HISTORY = 6

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def trim_messages(messages):
    """
    Keep only last N messages to reduce token usage.
    """
    return messages[-MAX_HISTORY:]


def build_context(messages, mode=None):
    """
    Builds full context with system instructions + optional mode.
    """
    system_prompt = mentor_instructions

    if mode:
        system_prompt += f"\n\nCurrent Mode: {mode}"

    return [{"role": "system", "content": system_prompt}] + messages


def get_ai_response(messages, mode=None):
    """
    Main function to get AI response.
    Handles:
    - memory trimming
    - system prompt
    - error handling
    """

    if not client:
        return "⚠️ Error: GROQ_API_KEY not found."

    try:
        # 🧠 Trim memory
        trimmed_messages = trim_messages(messages)

        # 🧩 Build context
        full_context = build_context(trimmed_messages, mode)

        # 🤖 API Call
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=full_context,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
        )

        reply = response.choices[0].message.content.strip()

        # 🛡️ Safety fallback
        if not reply:
            return "⚠️ Empty response from AI. Try again."

        return reply

    except Exception as e:
        return f"❌ Error: {str(e)}"
