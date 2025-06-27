from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from prompt import resume_prompt, parser


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-4o",
    openai_api_key=api_key
)

chain = LLMChain(llm=llm, prompt=resume_prompt, output_parser=parser)
