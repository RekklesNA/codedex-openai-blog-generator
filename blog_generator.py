import openai 
from dotenv import dotenv_values


config = dotenv_values(".env")
openai.api_key = config["API_KEY"]

def blog_generator(user_prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Generate a paragraph of a blog post based on user input: {user_prompt}",
        max_tokens = 512,
        temperature = 0.3,
    )
    return response.choices[0].text

user_prompt = input("Please enter a subject: ")
print(blog_generator(user_prompt))

user_answer = "Y"
while user_answer == "Y":
    user_answer = input("Do you still want the AI ​​to continue generating new paragraphs? Please enter Y or N: ")
    if user_answer == "Y":
        user_prompt = input("Please enter a new subject: ")
        print(blog_generator(user_prompt))
print("Thank you for your use")
    
