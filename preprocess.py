import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

# pip install -r requirements.txt


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
