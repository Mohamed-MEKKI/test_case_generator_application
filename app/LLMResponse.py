import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class LLMConnector:
    def __init__(self,scenario):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.scenario = scenario
        self.temperature = float(os.getenv("TEMP"))

    def LLMResponseGenerator(self):
        stream = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role":"system", "content":
                    """
                    1. You are an expert on the QA engineering coding tool called Cumcumber Studios.
                    2. You can detect scenarios and you answer the user's questions about how to generate test cases. 
                    3. You should know what are the scenarios to prioritize. 
                    4. Your answer should be always in English and Markdown syntax and between ```                    
                    
                    """
                },
                {"role": "user", "content": "generate in gherkin format relevant test cases for this or these scenario:"+self.scenario}
                ],
            temperature= self.temperature
        )      
        return stream.choices[0].message.content
