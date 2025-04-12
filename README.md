# OpenAI Blog Generator

This is my final project for the Codedex Python Beginner course. I chose the "Generate a Blog with OpenAI" project.

## Project Description
This program uses OpenAI's API to generate blog paragraphs based on user input. The user provides a subject, and the AI generates a blog paragraph about it. Users can continue to generate more paragraphs on different subjects or exit the program.

## Features
- Uses OpenAI's GPT-3.5-turbo-instruct model
- Generates blog paragraphs on any subject
- Interactive command-line interface
- Ability to generate multiple paragraphs in one session

## Requirements
- Python 3.10
- python-dotenv 0.21.0
- openai 1.0.0

## Setup
1. Clone this repository
2. Create a `.env` file in the project directory
3. Add your OpenAI API key to the `.env` file: `API_KEY=your_openai_api_key`
4. Install required packages: `pip install openai python-dotenv`
5. Run the program: `python blog_generator.py`

## Usage
1. When prompted, enter a subject for your blog
2. The program will generate a paragraph about that subject
3. You will be asked if you want to continue
4. If you enter 'Y', you can enter a new subject
5. If you enter 'N', the program will exit

## Note
You need an OpenAI API key to use this program. You can get one from the [OpenAI website](https://platform.openai.com/account/api-keys). 