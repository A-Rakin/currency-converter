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

```json
{
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "INR": 74.0,
    "JPY": 110.0,
    "AUD": 1.35,
    "CAD": 1.25,
    "CHF": 0.92,
    "CNY": 6.47,
    "HKD": 7.78,
    "NZD": 1.42,
    "SGD": 1.36,
    "KRW": 1180.0,
    "BRL": 5.25,
    "ZAR": 14.6,
    "RUB": 73.5,
    "MXN": 20.0,
    "SAR": 3.75,
    "AED": 3.67,
    "SEK": 8.6,
    "NOK": 8.8,
    "DKK": 6.3,
    "TRY": 8.85,
    "THB": 32.8,
    "IDR": 14250.0,
    "BDT": 109.5
}
