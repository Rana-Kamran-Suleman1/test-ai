

def main():
    name = "My Official Mail is Kamran@oulookmail.com"


    # print("Chatbot ready! Type 'exit' to quit.\n")

    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() in ["exit", "quit"]:
    #         print("Exiting chatbot. Goodbye!")
    #         break

    #     try:
    #         response = ollama.chat(
    #             model="deepseek-r1:1.5b",
    #             messages=[{"role": "user", "content": user_input}]
    #         )
            
    #         # Extract the actual message text
    #         bot_message = response['message']['content']
    #         print("Bot:", bot_message)

    #     except Exception as e:
    #         print("Error:", str(e))

if __name__ == "__main__":
    main()

