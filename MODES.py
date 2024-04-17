current_mode = 'happy'
grocery_bag = ["chocolate"]

# uprage your mode
current_mode += " and Excited" 
print(f"Today, I'm feeling {current_mode}. That's is a major mood upgarade!")

mode = input("Are you feeeling happy now?").lower()
if current_mode != "Happy":
    snack = input("Any snack you like?")
    if "chocolate" in grocery_bag:
        print(
            "There is the chocolate! I hope you feeling better with other snack anyway"
            )
    else:
        print("Found chocolate in the bag! keep smiling...")
        print("i hope you have good day")