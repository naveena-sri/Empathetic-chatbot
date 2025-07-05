import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
