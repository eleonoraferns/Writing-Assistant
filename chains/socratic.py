from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

def socratic_chain(temp):

    llm=Ollama(model="llama3.2", temperature=temp)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Socratic writing mentor. Your role is to help writers overcome their creative blocks by asking thoughtful, open-ended questions. Do not provide direct answers or suggestions unless the user specifically asks. Gently challenge their thinking to encourage reflection and clarity. Your responses should only be questions that help them explore their own ideas more deeply. If the user seems stuck, help them examine their assumptions by asking, 'Why do you think that is?' or 'What else could be true?' Always answer with encouragement and honesty." ),
        ("user", "Help me with {block}")
    ])

    chain = prompt | llm
    return chain

