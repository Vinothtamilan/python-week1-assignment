#TASK-2-EXPENSE TRACKER

import csv
import os

f_name = "Exp_tracker.csv"

def add_exp():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    
    try:
        with open(f_name,'a',newline= "") as f:
            w = csv.writer(f)
            w.writerow([date,category,description,amount])
        print("Added Expenses Succesfully!")
    except FileNotFoundError:
        print("FIle Does Not Exist!")

def view_exp():
    try:
        with open(f_name,'r',newline= "") as f:
            r = csv.reader(f)
            print("-"*10,"Expense Details","-"*10)
            for i in r:
                print("Date:", i[0])
                print("Category:", i[1])
                print("Description:", i[2])
                print("Amount:", i[3])
                print()
    except:
        print("File Doe Not Exist!")

def calculate_total():
    total = 0

    try:
        with open(f_name, "r") as f:
            r = csv.reader(f)
            for i in r:
                total += float(i["Amount"])
            print(f"Total Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("File Doe Not Exist")

def report():
    total = 0
    entries = 0
    hi_expense = 0
    hi_category = 0
    try:
        with open(f_name, "r") as f:
            r = csv.reader(f)

            for i in r:
                amount = float(i["Amount"])
                total += 1
                entries += 1

                if amount>hi_expense:
                    hi_expense = amount
                    hi_category = i["Category"]
        
        print("-"*10,"Expense Report","-"*10)
        print("Total Amount: ", float(total))
        print("Total Entries: ", entries)
        print("Highest Expense: ", hi_category,"->",float(hi_expense))
    
    except FileNotFoundError:
        print("File Doe Not Exist")
        

while True:
        print("-"*10,"Expense Tracker","-"*10)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Summary Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_exp()

        elif choice == "2":
            view_exp()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            report()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


