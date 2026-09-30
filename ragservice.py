from dotenv import load_dotenv
import os

load_dotenv()
print("API KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))

from langchain_community.document_loaders import DirectoryLoader,TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma 
from langchain_groq import ChatGroq 

loader=DirectoryLoader(
    'documents',  glob ="*txt",
    loader_cls=TextLoader
)

documents=loader.load()
print("Documents loaded:", len(documents))
print([doc.metadata["source"] for doc in documents])


splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)
chunks=splitter.split_documents(documents)
print(len(chunks))


embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store=Chroma.from_documents(
    documents= chunks, embedding=embeddings 
)

reteriver=vector_store.as_retriever(
    search_kwargs={"k":3}
)
def askquestion(question):
    a=reteriver.invoke(question)
    context = ""
    source=[]
    for i in a:
        context=context+i.page_content+"\n\n"
        source.append(i.metadata["source"])
    
    prompt=f"""
    Answer the question using only the context below.
    If the answer is not present in the context, say:
    "Information is not available in the provided documents."
    Context:
    {context}
    Question:
    {question}
    """
    response=llm.invoke(prompt)
    return response.content,set(source) 

llm= ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


answer, sources = askquestion(
    "Who is the president of Pakistan?"
)

print("Answer:", answer)
print("Sources:", sources)