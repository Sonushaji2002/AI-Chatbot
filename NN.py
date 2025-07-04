from dotenv import load_dotenv
from typing import TypedDict,List
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,BaseMessage,ToolMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.utils.function_calling import convert_to_openai_tool
from prop.visit_web import visit_web,math

load_dotenv()

#Define state
class AgentState(TypedDict):
    input:str
    messages:List[BaseMessage]

#Set up model and tools
model=ChatGroq(model_name="llama3-8b-8192",temperature=0)
tools=[DuckDuckGoSearchResults(),visit_web,math]
openai_tools=[convert_to_openai_tool(t) for t in tools]

#Set up prompt
prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant.Use tools if needed,and explain answers clearly."),
    MessagesPlaceholder(variable_name="messages"),
    ("human","{input}")
])
chain = prompt | model.bind_tools(openai_tools)

#Core logic
def call_agent(query:str)->str:
    messages = [HumanMessage(content=query)]
    
    # Step 1:Model thinks
    response = chain.invoke({"input":query,"messages":messages})
    messages.append(response)

    # Step 2:If tools are used
    if hasattr(response,"tool_calls") and response.tool_calls:
        for call in response.tool_calls:
            tool = next((t for t in tools if t.name ==call["name"]),None)
            if tool:
                try:
                    result = tool.invoke(call.get("args",{}))
                except Exception as e:
                    result = f"Error: {e}"
                messages.append(ToolMessage(content=str(result),tool_call_id=call["id"]))

        # Step 3:Model summarizes
        final = chain.invoke({"input":query,"messages":messages})
        messages.append(final)

    return messages[-1].content.strip()
