from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


chat = ChatOpenAI(temperature=0.8)
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to Chinese."),
    HumanMessage(content="Translate this sentence from English to Chinese. I love programming.")
]
resp = chat(messages)

print(resp)


