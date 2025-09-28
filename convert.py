import tkinter as tk
from tkinter import ttk
import json

def load_exchange(file_path="exchange_rates.json"):  #takes a file path
    try:
        with open(file_path, "r") as file:  #Open the file in read mode
            return json.load(file) #Reads the JSON content and converts it into a Python dictionary
    except FileNotFoundError: #If the file doesn’t exist, we catch the error and print a message instead of crashing the program.
        print("Exchange rate file not found!")
        return {}  #Returns an empty dictionary if the file is missing.

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def handle_conversion():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_dropdown.get()
        to_currency = to_currency_dropdown.get()
        rates = load_exchange()
        result = convert_currency(amount, from_currency, to_currency, rates)
        if result is not None:
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            result_label.config(text="Conversion Error!")
    except ValueError:
        result_label.config(text="Invalid Amount!")

root = tk.Tk() #Creates the main window of the application.
root.title("Currency Converter")
root.geometry("400x300")

# Amount Entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5) #Places it in the window and adds vertical padding of 5 pixels.
amount_entry = tk.Entry(root) #Adds a text input box for the user to type the amount.
amount_entry.pack(pady=5) #Displays the entry box with padding.

# From Currency Dropdown Menu
from_currency_label = tk.Label(root, text="From Currency:") 
from_currency_label.pack(pady=5)
from_currency_dropdown = ttk.Combobox( #Creates a dropdown menu.
    root,
    values=[
        "USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF", "CNY", "HKD",
        "NZD", "SGD", "KRW", "BRL", "ZAR", "RUB", "MXN", "SAR", "AED", "SEK",
        "NOK", "DKK", "TRY", "THB", "IDR", "BDT"
    ]
)
from_currency_dropdown.pack(pady=5)

# To Currency Dropdown
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_dropdown = ttk.Combobox(
    root,
    values=[
        "USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF", "CNY", "HKD",
        "NZD", "SGD", "KRW", "BRL", "ZAR", "RUB", "MXN", "SAR", "AED", "SEK",
        "NOK", "DKK", "TRY", "THB", "IDR", "BDT"
    ]
)
to_currency_dropdown.pack(pady=5)

# Convert Button (Creates a button widget.)
convert_button = tk.Button(root, text="Convert", command=handle_conversion)
convert_button.pack(pady=10) #Displays it with vertical padding.

result_label = tk.Label(root, text="", font=("Arial", 14)) #text="" → Starts empty; will be updated after conversion.
result_label.pack(pady=10) #Places it nicely below the button

root.mainloop() #Tells Tkinter: “Keep the window open and listen for user interactions” (clicks, typing, etc.).
















# rates = load_exchange_rates()
# amount = 100
# converted = convert_currency(amount, "USD", "JPY", rates)
# print(f"Converted {amount} USD to JPY: {converted:.2f}")


