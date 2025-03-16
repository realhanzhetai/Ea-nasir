from lightrag import QueryParam
from lightrag_model_settings import rag

custom_prompt = """
    You are an expert assistant in economics. Provide detailed and structured answers with examples.
    ---Conversation History---
    {history}
    ---Knowledge Base---
    {context_data}
    ---Response Rules---
    - Target format and length: {response_type}
"""

user_question = ("Based on the information provided, explain the dynamics occurring in the market for Indian workers \
                 in outsourcing jobs as described in a 2004 New York Times report. The report highlighted concerns \
                 about India potentially losing its outsourcing advantage due to rising wages and projected that, \
                 if the country continued producing college graduates at the current rate, demand for workers in \
                 key outsourcing sectors would exceed supply by 20% by 2008.\
                 Specifically, analyze the following:\
                 Is the demand for Indian workers increasing or decreasing?\
                 Is the supply of Indian workers increasing or decreasing?\
                 Which is shifting at a faster rate—demand or supply?\
                 Provide reasoning and examples to support your explanation.")

if __name__ == "__main__":
    response = rag.query(user_question,
                         param=QueryParam(mode="hybrid"),
                         system_prompt=custom_prompt)

    print(response)