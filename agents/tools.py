from langchain.tools import tool
from users import users_data
from dotenv import load_dotenv
import logging
from objects import PurchaseItem
from datetime import date, datetime


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

@tool
def get_user_purchase_history(users:str) -> dict:
    """This tool takes username and return a dict and return a dictinoay of the user purchanse history
    only if the user exists"""
    logging.info(f"using get_user_purchase_history tool to get user: {users} ")
    if users_data.get(users):
        return users_data[users]
    else:
        return {'status':'No username found'}
    

@tool
def Calculate_right_refund(user:str, items:list[PurchaseItem]) -> str:
    """This tool takes a list of items and user to be returned and how much refund worth"""

    logging.info(f"Getting Calculate_right_refund tool to get uses: {user} refund")

    if users_data.get(user):
        total_refund_amt = 0

        for item in items:
            if users_data[user].get(item.name):
                total_refund_amt +=  users_data[user][item.name]['price']
        return f'the value of the total refund is: {total_refund_amt}'
    
    return {'status': 'User not found'}


@tool
def Issue_refund_ticket(user:str, Items:list[PurchaseItem]) -> str:
    """
    This tool will sent a ticket to return a refund
    """

    logging.info(f"Using Issue_refund_ticket tool for user: {user}")

    refund_amount = 0

    eligible_items = []
    ineligible_items = []
    today = date.today()

    for item in Items:
        purchase = users_data[user].get(item.name)

        if not purchase:
            continue

        purchase_date = datetime.strptime(
            purchase['date'], '%Y-%m-%d'
        ).date()

        days_passed = (today - purchase_date).days

        if days_passed <= 7:
            refund_amount += purchase['price']
            eligible_items.append(item.name)

        else:
            ineligible_items.append(item.name)

        

    
    return f"a refund ticket has been issuesed for user:{user}. "\
           f"Refund amount {refund_amount}. "\
           f"eligible items{eligible_items}. "\
           f'ineligible items{ineligible_items}'


@tool
def check_current_date(user:str) -> str:
    """
    This tool get current time 
    """
    logging.info(f'Using check_current_date tool to fetch current time')
    return str(date.today())


## Testing
# print(get_user_purchase_history.invoke('user123'))
pen = PurchaseItem(name='pen')
book = PurchaseItem(name='book')
# print(Calculate_right_refund.invoke({'user':'user123', 'items':[pen, book]}))
# print(Issue_refund_ticket.invoke({'user':'user123', 'Items':[book]}))






