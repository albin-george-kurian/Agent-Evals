from models import model
from tools import get_user_purchase_history, Calculate_right_refund
from tools import Issue_refund_ticket, check_current_date
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from prompts import agent_system_prompt
from objects import answer
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from uuid import uuid4
load_dotenv()




agent = create_agent(
    model=model,
    tools=[get_user_purchase_history, Calculate_right_refund, Issue_refund_ticket, check_current_date],
    response_format=ToolStrategy(answer),
    system_prompt=agent_system_prompt,
    checkpointer=InMemorySaver()
)

def run_conversation():
    config = {'configurable':{'thread_id':str(uuid4())}}

    human_message = HumanMessage(content='I would like to request a refund')
    conversation = True

    while conversation:
        response = agent.invoke({'messages':human_message}, config=config)
        structured_response = response['structured_response']

        print(structured_response.answer)

        conversation = structured_response.conversation

        if conversation:
            user_input = input('replay: \n')
            human_message = HumanMessage(content=user_input)

    print('the job is done')


if __name__ == '__main__':
    run_conversation()




