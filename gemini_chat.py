import os
import dotenv
import google.generativeai as genai

# Load environment variables from .env file
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env file.")
    exit(1)

# Ask the user to set temperature value
try:
    temperature = float(input("🌡️ Enter temperature (0.0 - 1.0): ").strip())
    if not (0.0 <= temperature <= 1.0):
        raise ValueError
except ValueError:
    print("⚠️ Invalid temperature. Using default 0.7.")
    temperature = 0.7

# Configure the Gemini API
genai.configure(api_key=api_key)

# Create a chat model with temperature
model = genai.GenerativeModel("gemini-1.5-flash")
chat_session = model.start_chat(history=[])

print("\n🤖 Gemini Context-Aware Chatbot")
print("Type 'exit' to quit the chat.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    try:
        response = chat_session.send_message(user_input, generation_config={"temperature": temperature})
        print(f"Gemini: {response.text.strip()}\n")
    except Exception as e:
        print(f"❌ Error: {e}")
