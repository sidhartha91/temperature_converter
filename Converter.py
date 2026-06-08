"""
Temperature Converter
=====================

Converts temperatures between Fahrenheit and Celsius (with Kelvin as a bonus).

The user enters a temperature value and chooses the conversion direction.
Each conversion is a small, self-contained function so the logic is easy to
test and reuse.
"""


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit:  F = C * 9/5 + 32"""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius:  C = (F - 32) * 5/9"""
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin:  K = C + 273.15"""
    return c + 273.15


def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius:  C = K - 273.15"""
    return k - 273.15


def fahrenheit_to_kelvin(f):
    """Convert Fahrenheit to Kelvin (via Celsius)."""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k):
    """Convert Kelvin to Fahrenheit (via Celsius)."""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


# Maps a menu choice to (label, conversion function, output unit symbol).
CONVERSIONS = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "F"),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "C"),
    "3": ("Celsius to Kelvin", celsius_to_kelvin, "K"),
    "4": ("Kelvin to Celsius", kelvin_to_celsius, "C"),
    "5": ("Fahrenheit to Kelvin", fahrenheit_to_kelvin, "K"),
    "6": ("Kelvin to Fahrenheit", kelvin_to_fahrenheit, "F"),
}


def get_temperature():
    """Prompt until the user enters a valid number, then return it."""
    while True:
        try:
            return float(input("Enter the temperature value: ").strip())
        except ValueError:
            print("That's not a valid number. Try again.")


def main():
    print("=" * 40)
    print(" Temperature Converter")
    print("=" * 40)

    while True:
        print("\nChoose a conversion direction:")
        for key, (label, _, _) in CONVERSIONS.items():
            print(f"  {key}. {label}")
        print("  0. Exit")

        choice = input("\nYour choice (0-6): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in CONVERSIONS:
            print("Invalid choice. Please pick a number from 0 to 6.")
            continue

        label, func, unit = CONVERSIONS[choice]
        temp = get_temperature()
        result = func(temp)
        print(f"  {label}: {result:.2f} {unit}")


if __name__ == "__main__":
    main()
