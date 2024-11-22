import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

# pip install -r requirements.txt


def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post["text"])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post["tags"]
        new_tags = {unified_tags[tag] for tag in current_tags}
        post["tags"] = list(new_tags)

    with open(processed_file_path, encoding="utf-8", mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")