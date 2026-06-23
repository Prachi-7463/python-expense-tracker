# Expense Tracker
# Mini Project: 3

expenses = []

while True:
    print("-------------------------------------------------------------------------")
    print("=======Menu=======")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Your Total Spending")
    print("4. Exit")
    
    choice = int(input("Enter Your Choice: "))
    
    # Add Expenses
    if choice == 1:
        
        date = input("Enter the Date (DD-MM-YYYY): ")
        category = input("Enter the Category: ")
        description = input("Enter the description: ")
        amount = int(input("Enter the Amount: "))
        
        while amount <= 0:
            print("Invalid Amount!")
            choice = int(input("Try Again: "))
        print("Amount Details are Valid!")
        print("Expenses Added Successfully.")
    
        expense = {
           "Date": date,
           "Category": category,
           "Description": description,
           "Amount": amount
        }
    
        expenses.append(expense)
    
    # View expenses
    elif choice == 2:
        if len(expenses)==0:
            print("You Do Not Have Expenses Yet. First Add Some Expenses.")
            
        else:
            count = 1
            for expense in expenses:
                print(f"Expense{count} => {expense["Date"]}, {expense["Category"]}, {expense["Description"]}, {expense["Amount"]}")
                print("Your Expenses are Sucessfully Shown")
                count = count + 1
                
    # View total Spending        
    elif choice == 3:
        if len(expenses)==0:
            print("Since, you Do Not Have Expenses, You spend nothing.")
            print("Add Some Expenses.")
        else:
            totalSpending = 0
            for expense in expenses:
              totalSpending = totalSpending + expense["Amount"]
              print(f"You Spent Total Rs.{totalSpending} For Your Expenses.")
    
    elif choice == 4:
        print("You Have Exit From the Process Of Expense Tracking.")
        
    else: 
        print("Invalid Choice.")