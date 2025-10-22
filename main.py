from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

def main():
    # Load local Ollama model
    model = ChatOllama(model="llama3.2")

    print("Welcome! I'm your local AI assistant (running on Ollama). Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye! 👋")
            break

        response = model.invoke([HumanMessage(content=user_input)])
        print("\nAssistant:", response.content)

if __name__ == "__main__":
    main()
