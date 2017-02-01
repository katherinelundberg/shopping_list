needed_items = raw_input("What do you need to buy?")

shopping_list = ["milk", "eggs", "apples", "soap"]


def check_shopping_list(items):
    items = items.lower()
    if items in shopping_list:
        print "This is already on your list."
    else:
        shopping_list.append(items)
        print "This now added to your list."
    shopping_list.sort()
    
check_shopping_list(needed_items)

print shopping_list

