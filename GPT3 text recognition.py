pip install openai
import openai

# Set your OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT-3 engine
        prompt=prompt,
        max_tokens=100  # Adjust max_tokens as needed
    )

    generated_text = response.choices[0].text
    return generated_text

# Example usage
prompt = "Once upon a time"
generated_text = generate_text(prompt)

print("Generated Text:")
print(generated_text)
