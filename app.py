#including packages
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating prompts
prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#frontend uc Design using streamlit framework
st.title("My GPT")
input_text = st.text_input("ask your question")

# Ollama model integration
llm = Ollama(model="gemma2:latest ")
Output_Parser = StrOutputParser()
chain = prompt | llm | Output_Parser

#input validation
st.write(chain.invoke ({"question":input_text}))