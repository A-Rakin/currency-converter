# Currency Converter GUI Application

A simple **Currency Converter** application built using **Python Tkinter**. This application allows users to convert between multiple currencies using exchange rates stored in a JSON file.  

---

## Features

- Convert between **26+ world currencies** including USD, EUR, INR, BDT, JPY, and more.
- User-friendly **GUI interface** built with Tkinter.
- Loads exchange rates from a **JSON file** (`exchange_rates.json`) for easy updates.
- Handles invalid inputs gracefully with proper error messages.

## Technologies Used

- **Python 3.x**
- **Tkinter** – for building the GUI.
- **JSON** – for storing and reading currency exchange rates.

---

## How It Works

1. The application loads currency exchange rates from a JSON file:
2. User enters the amount, selects From Currency and To Currency from dropdown menus.
3. Pressing the Convert button calls a function that calculates the converted amount