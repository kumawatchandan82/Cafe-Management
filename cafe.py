import pandas as pd
from colorama import Fore, Back, Style
import cv2 as cv
import os

class PythonCafeTalk:
    def __init__(self):
        print("\t\t\t\tPython Cafe Talk")
        print("\t\t\t\tsince-1991")
        print("\t\t\t\twww.pythoncafe91.com")
        print("\n\n\t\t\t\t\tMENU")
        self.menu = ["Indian", "German", "Italian", "Korean"]
        for j, i in enumerate(self.menu, 1):
            print(f"\n\n\t {j} . {i}")

    def show_menu(self, items, prices):
        df = pd.DataFrame({"Food Items": items, "Price": prices}, index=[i for i in range(1, len(items)+1)])
        print("\n\n Menu\n\n")
        print(df)
        return df

    def order_food(self, df):
        total_list = []
        while True:
            try:
                a = int(input("Enter the position of the item: "))
                if a not in df.index:
                    print("Invalid item number!")
                    continue
                b = int(input("Enter the quantity: "))
            except ValueError:
                print("Please enter valid numbers!")
                continue

            cost = df["Price"][a] * b
            total_list.append(cost)

            e = input("Do you want to re-order? (yes/no): ").lower()
            if e == "no":
                print("Thank you for your order!")
                break
            elif e == "yes":
                continue
            else:
                print("Invalid input, exiting order.")
                break

        amt = sum(total_list)
        tax = amt * 0.05
        total_amt = amt + tax
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + f"\nTotal Amount: {amt}")
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + f"Service Tax: {tax}")
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + f"Total Amount Including Service Tax: {total_amt}")

    # Indian Food
    def indian(self):
        items = ["Rajma Chaval", "Dal Roti", "Paneer Tikka", "Lassi", "Green Salad", "Samosa"]
        prices = [120, 240, 150, 50, 100, 30]
        df = self.show_menu(items, prices)
        self.order_food(df)

    # German Food
    def german(self):
        items = ["Bratwurst", "Sauerbraten", "Pretzel", "Spaetzle", "Kartoffelsalat"]
        prices = [250, 450, 100, 150, 120]
        df = self.show_menu(items, prices)
        self.order_food(df)

    # Italian Food
    def italian(self):
        items = ["Pizza", "Pasta", "Lasagna", "Risotto", "Tiramisu"]
        prices = [300, 250, 400, 350, 150]
        df = self.show_menu(items, prices)
        self.order_food(df)

    # Korean Food
    def korean(self):
        items = ["Kimchi", "Bibimbap", "Bulgogi", "Tteokbokki", "Japchae"]
        prices = [150, 250, 300, 120, 200]
        df = self.show_menu(items, prices)
        self.order_food(df)


# ------------------- Program Start -------------------

a = PythonCafeTalk()
choice = input("\nEnter your choice (Indian/German/Italian/Korean): ").lower()

if choice == "indian":
    a.indian()
elif choice == "german":
    a.german()
elif choice == "italian":
    a.italian()
elif choice == "korean":
    a.korean()
else:
    print("Invalid choice!")

payment = input('\nEnter the payment mode (cash/online): ').lower()
if payment == "cash":
    print("Thank you for your payment!")
elif payment == "online":
    qr_path = r"D:\carDataAnalysis\qr.png" 
    if os.path.exists(qr_path):
        img = cv.imread(qr_path)
        cv.imshow("Scan QR Code to Pay", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        print("Thank you for your payment!")
    else:
        print("QR code image not found!")
else:
    print("Invalid payment option!")
