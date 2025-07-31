import anthropic
from sentence_transformers import SentenceTransformer
from search_faiss import search_sentence_in_faiss
from dotenv import load_dotenv

load_dotenv()  # Load from .env if exists


def prompt_claude_with_rag(question):
    """
    Prompts Claude API with RAG (Retrieval-Augmented Generation).
    Claude acts as a solution architect for designing data ingestion into SIEM.

    Args:
        question (str): The user's question.
        context_docs (list of str): List of relevant context documents.

    Returns:
        str: Claude's response.
    """
    # Build the context for RAG
    with open("data_model_schema.txt", "r") as f:
        dm_schema = f.read()
    with open("xql_stages.txt", "r") as f:
        xql_stages = f.read()
    with open("xql_functions.txt", "r") as f:
        xql_functions = f.read()

    faiss_results = search_sentence_in_faiss(question)
    example_text = ""
    for i, (spl, xql) in enumerate(faiss_results):
        example_text += f"""
        Example {i+1}:
        - SPL Query: {spl}
        - Equivalent XQL Query: {xql}

"""

    context = f"""
You are a skilled SIEM engineer specializing in writing searches in XQL in Cortex XSIAM.
Your task is to analyze the provided search query in Splunk SPL and convert it to Cortex XSIAM XQL.

Given the following example search queries in Splunk SPL and the corresponding converted XQL query, your task is to to the same for the required search query.
{example_text}

Refer to the list of XQL stages and functions and the field schema below to help you with the conversion. Use data model query and fields where as much as possible where applicable.
- XQL Stages:
{xql_stages}

- XQL Functions:
{xql_functions}

- XQL Data model field Schema:
{dm_schema}

        """

    content = f"Context:\n{context}\n\n"
    content += f"Convert this query to Cortex XQL using Data Model query datamodel dataset where possible: {question}\n"

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": content},
        ]
    )
    return message.content[0].text

if __name__ == "__main__":
    # For testing purposes, can run this script directly
    print(prompt_claude_with_rag("""
'`wineventlog_security` EventCode=4624 OR EventCode=4742 TargetUserName="ANONYMOUS
  LOGON" LogonType=3 | stats count min(_time) as firstTime max(_time) as lastTime
  by action app authentication_method dest dvc process process_id process_name process_path
  signature signature_id src src_port status subject user user_group vendor_product
  | `security_content_ctime(firstTime)` | `security_content_ctime(lastTime)` | `detect_computer_changed_with_anonymous_account_filter`'
                                 """))