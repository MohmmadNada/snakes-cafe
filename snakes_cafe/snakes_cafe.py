#array(list menu)
Appetizers=['Wings','Cookies','Spring Rolls']
Entrees=['Salmon','Steak','Meat Tornado','A Literal Garden']
Desserts=['Ice Cream','Cake','Pie']
Drinks=['Coffee','Tea','Unicorn Tears']
general_list=[Appetizers,Entrees,Desserts,Drinks]
# intro message
print(""" **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")
### the menu for the restaurant
print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************  """)
input_list=[]

def summary():
    if len(input_list)!=0:
        print(f"you choice {len(input_list)} items")
        
        for i in input_list :
            print(i)
    else:
        print("you didnt choice any items ")
# get user input
while True:
    user_input=input('>').lower().title()
    if user_input =='Quit':
        summary()
        quit()
    elif any(user_input in sl for sl in general_list):
        input_list.append(user_input)
        print(f'** {input_list.count(user_input)} orders of {user_input} have been added to your meal **')
    else:
        print("this option is not available ,any time you can type 'quit' to exit")

   
