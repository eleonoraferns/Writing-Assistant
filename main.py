from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

from chains.reflective import reflective_chain
from chains.creative import creative_chain
from chains.socratic import socratic_chain

chain_type = input("What type of help do you need? R: reflective, C: creative, S: socratic")

if chain_type.upper()=="R":
    guide = reflective_chain()

elif chain_type.upper()=="C":
    guide = creative_chain()

else:
    guide = socratic_chain()

while True:
    user_input = input("speak")
    if user_input.lower()=="quit":
        break

    response = guide.invoke({"block": user_input})
    print("\n✒️",response, "\n")



# workflow = StateGraph(state_schema=MessagesState)

# llm=Ollama(model="llama3.2")

# def call_model(state: MessagesState):
#     response = llm.invoke(state["messages"])
#     return {"messages": response}

# workflow.add_edge(START, "model")
# workflow.add_node("model", call_model)

# memory = MemorySaver()
# app = workflow.compile(checkpointer=memory)