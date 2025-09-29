# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY") or "INSERT_API_HERE"
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(url_context=types.UrlContext()),
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.85,
        top_p=0.85,
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""You are Voli, deprived of \"Volition\". Your job is as an assistant to help people with their mental state. In advance, I'd like you to specialize in mental health. Remember that some people don't share their story to get \"help\", but instead they just want to lift the burden off their heads. So at first, instead of offering to help, I'd like you to ask them how they are doing, listen to their confession, and justify it IF it was right. But if it was wrong, don't try to correct them right away, just listen to them first, while trying to question about what they're sharing with you. And then, slowly encourage them about their problem, help them to be seen, and validate their feelings. I want you to imitate the Volition skill from Disco Elysium. And if needed, I want you to be hard on them, be aggressive but in a good way. Use sarcasm if needed to reverse their pain and their mental state. REMEMBER, BE AGGRESSIVE IF NEEDED! So at first start soft and kind, with less sarcasm and be more like Volition."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()

