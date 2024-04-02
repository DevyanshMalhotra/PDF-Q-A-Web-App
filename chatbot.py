import os
import re
from collections import Counter

from llama_index import (
    ServiceContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
    set_global_service_context,
)
from llama_index.embeddings import GradientEmbedding
from llama_index.llms import GradientBaseModelLLM
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def top_keywords(text):
    keyword_pattern = r'\d+\.\s*([^\n]+)'
    matches = re.findall(keyword_pattern, text)
    return matches

llm = GradientBaseModelLLM(
    base_model_slug="llama2-7b-chat",
    max_tokens=400,
)

embed_model = GradientEmbedding(
    gradient_access_token=os.environ["GRADIENT_ACCESS_TOKEN"],
    gradient_workspace_id=os.environ["GRADIENT_WORKSPACE_ID"],
    gradient_model_slug="bge-large",
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    chunk_size=256,
)

set_global_service_context(service_context)

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents, service_context=service_context)
query_engine = index.as_query_engine()