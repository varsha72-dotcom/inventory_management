
#
#######################################################
#            INVENTORY MANAGEMENT SYSTEM             #
#   Mini Project using only basic Python concepts    #
#   (lists, loops, if-else) -- no functions/classes  #
#   Now with table-formatted output                  #
#######################################################

# ---------------- Data Storage (Lists) ----------------

item_names = []      # stores item names
item_prices = []     # stores cost price of each item
item_quantities = []  # stores quantity in stock
item_sell_prices = []  # stores selling price of each item

user_names = []      # stores registered user names
user_mobiles = []    # stores registered user mobile numbers
user_carts_items = []   # list of lists -> each user's cart items
user_carts_qty = []     # list of lists -> each user's cart quantities

total_revenue = 0       # total money earned from sales
total_profit = 0        # total profit earned

# Some sample starting data so the project isn't empty
item_names.append("Rice (1kg)")
item_prices.append(40)
item_sell_prices.append(50)
item_quantities.append(100)

item_names.append("Sugar (1kg)")
item_prices.append(35)
item_sell_prices.append(45)
item_quantities.append(80)

item_names.append("Oil (1L)")
item_prices.append(110)
item_sell_prices.append(130)
item_quantities.append(60)


print("#####################################################")
print("#        WELCOME TO INVENTORY MANAGEMENT SYSTEM       #")
print("#####################################################")

main_running = True

while main_running:
    print("\n--------- START ---------")
    print("Select Role:")
    print("1. OWNER")
    print("2. USER")
    print("3. EXIT PROGRAM")

    role_choice = input("Enter your choice (1/2/3): ")

    # =========================================================
    #                      OWNER SECTION
    # =========================================================
    if role_choice == "1":

        owner_running = True
        while owner_running:
            print("\n========== OWNER SECTION ==========")
            print("1. Add Items to Inventory")
            print("2. Remove Item")
            print("3. Update Item")
            print("4. View Inventory")
            print("5. View Users Details")
            print("6. View Report (Total Revenue & Itemized Profit)")
            print("7. Exit Owner Section")

            owner_choice = input("Enter your choice (1-7): ")

            # ---------------- ADD ITEM ----------------
            if owner_choice == "1":
                print("\n--- ADD ITEM TO INVENTORY ---")
                new_name = input("Enter item name: ")
                new_cost_price = int(input("Enter cost price: "))
                new_sell_price = int(input("Enter selling price: "))
                new_qty = int(input("Enter quantity: "))

                item_names.append(new_name)
                item_prices.append(new_cost_price)
                item_sell_prices.append(new_sell_price)
                item_quantities.append(new_qty)

                print(new_name, "added successfully!")

            # ---------------- REMOVE ITEM ----------------
            elif owner_choice == "2":
                print("\n--- REMOVE ITEM ---")
                print("Current Items:")
                if len(item_names) == 0:
                    print("No items in inventory to remove.")
                else:
                    print(f"{'No.':<5}{'Item Name':<20}")
                    print("-" * 25)
                    index = 0
                    while index < len(item_names):
                        print(f"{index + 1:<5}{item_names[index]:<20}")
                        index = index + 1

                    remove_choice = int(input("Enter item number to remove: "))
                    if remove_choice >= 1 and remove_choice <= len(item_names):
                        pos = remove_choice - 1
                        print(item_names[pos], "removed from inventory.")
                        item_names.pop(pos)
                        item_prices.pop(pos)
                        item_sell_prices.pop(pos)
                        item_quantities.pop(pos)
                    else:
                        print("Invalid item number.")

            # ---------------- UPDATE ITEM ----------------
            elif owner_choice == "3":
                print("\n--- UPDATE ITEM ---")
                print("Current Items:")
                if len(item_names) == 0:
                    print("No items in inventory to update.")
                else:
                    print(f"{'No.':<5}{'Item Name':<20}")
                    print("-" * 25)
                    index = 0
                    while index < len(item_names):
                        print(f"{index + 1:<5}{item_names[index]:<20}")
                        index = index + 1

                    update_choice = int(input("Enter item number to update: "))
                    if update_choice >= 1 and update_choice <= len(item_names):
                        pos = update_choice - 1
                        print("Updating:", item_names[pos])
                        print("Leave blank (just press enter) to keep old value.")

                        new_name = input("New name [" + item_names[pos] + "]: ")
                        if new_name != "":
                            item_names[pos] = new_name

                        new_cost = input("New cost price [" + str(item_prices[pos]) + "]: ")
                        if new_cost != "":
                            item_prices[pos] = int(new_cost)

                        new_sell = input("New selling price [" + str(item_sell_prices[pos]) + "]: ")
                        if new_sell != "":
                            item_sell_prices[pos] = int(new_sell)

                        new_qty = input("New quantity [" + str(item_quantities[pos]) + "]: ")
                        if new_qty != "":
                            item_quantities[pos] = int(new_qty)

                        print("Item updated successfully!")
                    else:
                        print("Invalid item number.")

            # ---------------- VIEW INVENTORY ----------------
            elif owner_choice == "4":
                print("\n--- CURRENT INVENTORY ---")
                if len(item_names) == 0:
                    print("Inventory is empty.")
                else:
                    header = f"{'No.':<5}{'Item Name':<20}{'Cost Price':<12}{'Sell Price':<12}{'Quantity':<10}"
                    print(header)
                    print("-" * len(header))
                    index = 0
                    while index < len(item_names):
                        print(f"{index + 1:<5}{item_names[index]:<20}{item_prices[index]:<12}"
                              f"{item_sell_prices[index]:<12}{item_quantities[index]:<10}")
                        index = index + 1

            # ---------------- VIEW USERS DETAILS ----------------
            elif owner_choice == "5":
                print("\n--- REGISTERED USERS ---")
                if len(user_names) == 0:
                    print("No users have registered yet.")
                else:
                    index = 0
                    while index < len(user_names):
                        print(f"\n{index + 1}. {user_names[index]}  |  Mobile: {user_mobiles[index]}")
                        if len(user_carts_items[index]) == 0:
                            print("   Cart is empty.")
                        else:
                            header = f"   {'Item Name':<20}{'Quantity':<10}"
                            print(header)
                            print("   " + "-" * (len(header) - 3))
                            j = 0
                            while j < len(user_carts_items[index]):
                                print(f"   {user_carts_items[index][j]:<20}{user_carts_qty[index][j]:<10}")
                                j = j + 1
                        index = index + 1

            # ---------------- VIEW REPORT ----------------
            elif owner_choice == "6":
                print("\n--- VIEW REPORT ---")
                print("Total Revenue Generated: Rs.", total_revenue)
                print("Total Profit Earned: Rs.", total_profit)
                print("\nItemized Current Stock Value:")
                header = f"{'Item Name':<20}{'Stock Value (Rs.)':<20}"
                print(header)
                print("-" * len(header))
                index = 0
                while index < len(item_names):
                    stock_value = item_sell_prices[index] * item_quantities[index]
                    print(f"{item_names[index]:<20}{stock_value:<20}")
                    index = index + 1

            # ---------------- EXIT OWNER SECTION ----------------
            elif owner_choice == "7":
                print("Exiting Owner Section...")
                owner_running = False

            else:
                print("Invalid choice! Please try again.")

    # =========================================================
    #                       USER SECTION
    # =========================================================
    elif role_choice == "2":

        print("\n========== USER SECTION ==========")
        current_user = input("Enter your name: ").strip()

        # check if user already exists, else register new user
        # (compares names ignoring case/extra spaces so the same
        #  person typing their name slightly differently still
        #  matches their existing cart instead of creating a new one)
        user_found = False
        user_index = 0
        i = 0
        while i < len(user_names):
            if user_names[i].strip().lower() == current_user.lower():
                user_found = True
                user_index = i
            i = i + 1

        if user_found == False:
            current_mobile = input("Enter your mobile number: ")
            user_names.append(current_user)
            user_mobiles.append(current_mobile)
            user_carts_items.append([])
            user_carts_qty.append([])
            user_index = len(user_names) - 1
            print("New user registered:", current_user)
        else:
            print("Welcome back,", current_user, "!")

        user_running = True
        while user_running:
            print("\n--- USER MENU ---")
            print("1. Add to Cart")
            print("2. Remove from Cart")
            print("3. Modify Cart")
            print("4. View Cart")
            print("5. Billing")
            print("6. Exit User Section")

            user_choice = input("Enter your choice (1-6): ")

            # ---------------- ADD CART ----------------
            if user_choice == "1":
                print("\n--- AVAILABLE ITEMS ---")
                if len(item_names) == 0:
                    print("No items available in inventory.")
                else:
                    header = f"{'No.':<5}{'Item Name':<20}{'Price':<10}{'In Stock':<10}"
                    print(header)
                    print("-" * len(header))
                    index = 0
                    while index < len(item_names):
                        print(f"{index + 1:<5}{item_names[index]:<20}{item_sell_prices[index]:<10}"
                              f"{item_quantities[index]:<10}")
                        index = index + 1

                    item_choice = int(input("Enter item number to add: "))
                    if item_choice >= 1 and item_choice <= len(item_names):
                        pos = item_choice - 1
                        qty_choice = int(input("Enter quantity: "))

                        if qty_choice <= item_quantities[pos] and qty_choice > 0:
                            user_carts_items[user_index].append(item_names[pos])
                            user_carts_qty[user_index].append(qty_choice)
                            print(qty_choice, "x", item_names[pos], "added to cart.")
                        else:
                            print("Not enough stock available!")
                    else:
                        print("Invalid item number.")

            # ---------------- REMOVE CART ----------------
            elif user_choice == "2":
                print("\n--- YOUR CART ---")
                if len(user_carts_items[user_index]) == 0:
                    print("Your cart is empty.")
                else:
                    header = f"{'No.':<5}{'Item Name':<20}{'Quantity':<10}"
                    print(header)
                    print("-" * len(header))
                    index = 0
                    while index < len(user_carts_items[user_index]):
                        print(f"{index + 1:<5}{user_carts_items[user_index][index]:<20}"
                              f"{user_carts_qty[user_index][index]:<10}")
                        index = index + 1

                    remove_choice = int(input("Enter item number to remove from cart: "))
                    if remove_choice >= 1 and remove_choice <= len(user_carts_items[user_index]):
                        pos = remove_choice - 1
                        print(user_carts_items[user_index][pos], "removed from cart.")
                        user_carts_items[user_index].pop(pos)
                        user_carts_qty[user_index].pop(pos)
                    else:
                        print("Invalid choice.")

            # ---------------- MODIFY CART ----------------
            elif user_choice == "3":
                print("\n--- YOUR CART ---")
                if len(user_carts_items[user_index]) == 0:
                    print("Your cart is empty.")
                else:
                    header = f"{'No.':<5}{'Item Name':<20}{'Quantity':<10}"
                    print(header)
                    print("-" * len(header))
                    index = 0
                    while index < len(user_carts_items[user_index]):
                        print(f"{index + 1:<5}{user_carts_items[user_index][index]:<20}"
                              f"{user_carts_qty[user_index][index]:<10}")
                        index = index + 1

                    modify_choice = int(input("Enter item number to modify quantity: "))
                    if modify_choice >= 1 and modify_choice <= len(user_carts_items[user_index]):
                        pos = modify_choice - 1
                        new_qty = int(input("Enter new quantity: "))
                        if new_qty > 0:
                            user_carts_qty[user_index][pos] = new_qty
                            print("Cart updated.")
                        else:
                            print("Quantity must be greater than 0.")
                    else:
                        print("Invalid choice.")

            # ---------------- VIEW CART ----------------
            elif user_choice == "4":
                print("\n--- YOUR CART ---")
                if len(user_carts_items[user_index]) == 0:
                    print("Your cart is empty.")
                else:
                    cart_total = 0
                    header = f"{'Item Name':<20}{'Quantity':<10}{'Line Total (Rs.)':<18}"
                    print(header)
                    print("-" * len(header))
                    index = 0
                    while index < len(user_carts_items[user_index]):
                        item_name_in_cart = user_carts_items[user_index][index]
                        qty_in_cart = user_carts_qty[user_index][index]

                        # find price of that item from inventory lists
                        price_of_item = 0
                        j = 0
                        while j < len(item_names):
                            if item_names[j] == item_name_in_cart:
                                price_of_item = item_sell_prices[j]
                            j = j + 1

                        line_total = price_of_item * qty_in_cart
                        cart_total = cart_total + line_total

                        print(f"{item_name_in_cart:<20}{qty_in_cart:<10}{line_total:<18}")
                        index = index + 1

                    print("-" * len(header))
                    print("Cart Total: Rs.", cart_total)

            # ---------------- BILLING ----------------
            elif user_choice == "5":
                print("\n--- BILLING ---")
                if len(user_carts_items[user_index]) == 0:
                    print("Your cart is empty. Add items before billing.")
                else:
                    bill_total = 0
                    bill_profit = 0

                    print("------ FINAL BILL ------")
                    header = f"{'Item Name':<20}{'Quantity':<10}{'Line Total (Rs.)':<18}"
                    print(header)
                    print("-" * len(header))
                    index = 0
                    while index < len(user_carts_items[user_index]):
                        item_name_in_cart = user_carts_items[user_index][index]
                        qty_in_cart = user_carts_qty[user_index][index]

                        # find item position in inventory
                        item_pos = -1
                        j = 0
                        while j < len(item_names):
                            if item_names[j] == item_name_in_cart:
                                item_pos = j
                            j = j + 1

                        if item_pos != -1:
                            sell_price = item_sell_prices[item_pos]
                            cost_price = item_prices[item_pos]

                            line_total = sell_price * qty_in_cart
                            line_profit = (sell_price - cost_price) * qty_in_cart

                            bill_total = bill_total + line_total
                            bill_profit = bill_profit + line_profit

                            print(f"{item_name_in_cart:<20}{qty_in_cart:<10}{line_total:<18}")

                            # reduce stock quantity after billing
                            item_quantities[item_pos] = item_quantities[item_pos] - qty_in_cart

                        index = index + 1

                    print("-" * len(header))
                    print("Grand Total: Rs.", bill_total)
                    print("Thank you for shopping,", current_user, "!")

                    # update overall revenue and profit
                    total_revenue = total_revenue + bill_total
                    total_profit = total_profit + bill_profit

                    # empty the cart after billing
                    user_carts_items[user_index] = []
                    user_carts_qty[user_index] = []

            # ---------------- EXIT USER SECTION ----------------
            elif user_choice == "6":
                print("Exiting User Section...")
                user_running = False

            else:
                print("Invalid choice! Please try again.")

    # =========================================================
    #                      EXIT PROGRAM
    # =========================================================
    elif role_choice == "3":
        print("\nThank you for using Inventory Management System. Goodbye!")
        main_running = False

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
