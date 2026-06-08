#TASK-3- PYTHON MINI CHALLANGES

def list_ops():
    while True:
        print("-"*10,"List Problems","-"*10)
        print("1. Find Smallest And Largest Number")
        print("2. Remove Duplicate element")
        print("3. Count Even And Odd Numbers")
        print("4. Exit")
        ch = int(input("Entr Choice(1-4): "))
        if ch == 1:
            lst = eval(input("Enter List Of Numbers: "))
            largest = max(lst)
            smallest = min(lst)
            print("Largest Number:", largest)
            print("Smallest Number:", smallest)
        elif ch == 2:
            lst = eval(input("Enter List Of Numbers: "))
            uni_no = list(set(lst))                         
            print("List without duplicates:", uni_no)
        elif ch == 3:
            lst = eval(input("Enter List Of Numbers: "))
            even_count = 0
            odd_count = 0
            for num in lst:
                if num % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            print("Even Numbers:", even_count)
            print("Odd Numbers:", odd_count)
        elif ch == 4:
            break
        else:
            print("Invalid Choice")

def string_ops():
    while True:
        print("-"*10, "String Problems", "-"*10)
        print("1. Reverse a String")
        print("2. Count Vowels")
        print("3. Check Palindrome")
        print("4. Exit")
        ch = int(input("Enter Choice(1-4): "))
        if ch == 1:
            text = input("Enter a String: ")
            reversed_text = text[::-1]
            print("Reversed String:", reversed_text)
        elif ch == 2:
            st = input("Enter a Sentence: ")
            vowels = "aeiouAEIOU"
            count = 0
            for char in st:
                if char in vowels:
                    count += 1
            print("Number of Vowels:", count)
        elif ch == 3:
            text = input("Enter a String: ")
            if text == text[::-1]:
                print("Palindrome")
            else:
                print("Not a Palindrome")
        elif ch == 4:
            break
        else:
            print("Invalid Choice")

def dict_ops():
    while True:
        print("-"*10, "Dictionary Problems", "-"*10)
        print("1. Count Character Frequency")
        print("2. Merge Two Dictionaries")
        print("3. Student Marks Average")
        print("4. Exit")
        ch = int(input("Enter Choice(1-4): "))
        if ch == 1:
            text = input("Enter a String: ")
            freq = {}
            for char in text:
                freq[char] = freq.get(char, 0) + 1

            print("Character Frequency:", freq)
        elif ch == 2:
            d1 = eval(input("Enter First Dictionary: "))
            d2 = eval(input("Enter Second Dictionary: "))
            merge = d1.copy()
            merge.update(d2)
            print("Merged Dictionary:", merge)
        elif ch == 3:
            marks = {}
            n = int(input("Enter Number of Subjects: "))
            for i in range(n):
                subject = input("Enter Subject Name: ")
                mark = float(input("Enter Marks: "))
                marks[subject] = mark
            average = sum(marks.values()) / len(marks)
            print("Student Marks:", marks)
            print("Average Marks:", average)
        elif ch == 4:
            break
        else:
            print("Invalid Choice")

while True:
        print("-"*10, "Menu", "-"*10)
        print("1. List Operations")
        print("2. Dictionary Operations")
        print("3. String Operations")
        print("4. Exit")
        ch = int(input("Enter Choice(1-4): "))
        if ch == 1:
            list_ops()
        elif ch == 2:
            dict_ops()
        elif ch == 3:
            string_ops()
        elif ch == 4:
            break
        else:
            print("Invalid Choice")
            


