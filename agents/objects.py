from pydantic import BaseModel, Field


# lowercase on purpose: the class name is the tool name the model must call, and it keeps writing "answer"
class answer(BaseModel):
    answer: str = Field(description='The answer for the user')
    conversation: bool = Field(description='This is an indicator to know if the conversation'\
                               'should still continue or not. if the agent has made the decision about the refund'\
                                'this should be False. '\
                                "if the conversation still need more talk then it's True", default=True)
    

class PurchaseItem(BaseModel):
    name: str = Field(description="The name of the purchased item")


    