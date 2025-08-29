import pandas as pd
from colorama import Fore, Back, Style
import cv2 as cv
import os

# -------------------- Simple Welcome --------------------
def welcome_screen():
    print("\n\t\t\tWelcome to Joy Cafe")
    print("\t\t\tSince 1991 - www.joycafe1991.com\n")

# -------------------- Menu & Order --------------------
class JoyCafe:
    def __init__(self):
        self.menu = {
            "Indian": {"Rajma Chaval":120, "Dal Roti":240, "Paneer Tikka":150, "Lassi":50, "Green Salad":100, "Samosa":30},
            "German": {"Bratwurst":250, "Sauerbraten":450, "Pretzel":100, "Spaetzle":150, "Kartoffelsalat":120},
            "Italian": {"Pizza":300, "Pasta":250, "Lasagna":400, "Risotto":350, "Tiramisu":150},
            "Korean": {"Kimchi":150, "Bibimbap":250, "Bulgogi":300, "Tteokbokki":120, "Japchae":200}
        }
        self.order_list = []

    def show_categories(self):
        print("\nAvailable Categories:")
        for i, cat in enumerate(self.menu.keys(),1):
            print(f"{i}. {cat}")

    def select_category(self):
        while True:
            self.show_categories()
            choice = input("\nEnter category: ").title()
            if choice in self.menu:
                self.select_items(choice)
                break
            else:
                print("Invalid category!")

    def select_items(self, category):
        items = self.menu[category]
        df = pd.DataFrame({"Item": list(items.keys()), "Price": list(items.values())}, index=[i for i in range(1,len(items)+1)])
        print("\nMenu:\n")
        print(df)

        while True:
            try:
                item_no = int(input("\nEnter item number to order: "))
                if item_no not in df.index:
                    print("Invalid item number!")
                    continue
                qty = int(input("Enter quantity: "))
                self.order_list.append({"Item": df['Item'][item_no], "Price": df['Price'][item_no], "Qty": qty})
            except ValueError:
                print("Enter valid numbers!")
                continue

            more = input("Do you want to order more? (yes/no): ").lower()
            if more == "no":
                break

    def order_summary(self):
        print("\n------ Order Summary ------\n")
        total = 0
        summary_df = pd.DataFrame(self.order_list)
        summary_df['Subtotal'] = summary_df['Price']*summary_df['Qty']
        total = summary_df['Subtotal'].sum()
        tax = total*0.05
        grand_total = total + tax
        print(summary_df)
        print(f"\nSubtotal: {total}")
        print(f"Tax (5%): {tax}")
        print(f"Grand Total: {grand_total}")
        return grand_total, summary_df

    def payment(self, amount, summary_df):
        pay = input("\nEnter payment mode (cash/online): ").lower()
        if pay == "cash":
            print("\nPayment successful! Thank you.\n")
        elif pay == "online":
            qr_path = r"D:\carDataAnalysis\Cafe Management\qr.png"
            if os.path.exists(qr_path):
                img = cv.imread(qr_path)
                cv.imshow("Scan QR Code to Pay", img)
                cv.waitKey(0)
                cv.destroyAllWindows()
                print("\nPayment successful! Thank you.\n")
            else:
                print("QR code image not found!")
        else:
            print("Invalid payment option!")

        # Print final bill
        print("\n----- Your Bill -----\n")
        print(summary_df)
        print(f"\nSubtotal: {summary_df['Subtotal'].sum()}")
        print(f"Tax (5%): {summary_df['Subtotal'].sum()*0.05}")
        print(f"Grand Total: {amount}")
        print("\nPlease collect your bill. Thank you for visiting Joy Cafe!\n")

# -------------------- Program Start --------------------
welcome_screen()
cafe = JoyCafe()
cafe.select_category()
total_amount, summary = cafe.order_summary()
cafe.payment(total_amount, summary)
