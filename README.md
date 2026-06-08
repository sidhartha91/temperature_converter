# Temperature Converter

A Python program that converts temperatures between Fahrenheit, Celsius, and
Kelvin. The user enters a value and chooses the conversion direction. Built as
part of an internship task.

## Objective

Let users input a temperature and choose the conversion direction between
Fahrenheit and Celsius (Kelvin conversions added as a bonus).

## Conversion formulas

| Conversion              | Formula                  |
|-------------------------|--------------------------|
| Celsius to Fahrenheit   | `F = C * 9/5 + 32`       |
| Fahrenheit to Celsius   | `C = (F - 32) * 5/9`     |
| Celsius to Kelvin       | `K = C + 273.15`         |
| Kelvin to Celsius       | `C = K - 273.15`         |

Fahrenheit-Kelvin conversions are done by going through Celsius.

## Files

- `converter.py` — conversion functions plus an interactive menu
- `test_converter.py` — tests against known reference points

## How to run

You only need Python 3 (no external libraries).

Run the converter:

```bash
python converter.py
```

Run the tests:

```bash
python test_converter.py
```

## Example session

```
========================================
 Temperature Converter
========================================

Choose a conversion direction:
  1. Celsius to Fahrenheit
  2. Fahrenheit to Celsius
  3. Celsius to Kelvin
  4. Kelvin to Celsius
  5. Fahrenheit to Kelvin
  6. Kelvin to Fahrenheit
  0. Exit

Your choice (0-6): 1
Enter the temperature value: 37
  Celsius to Fahrenheit: 98.60 F
```

## How it is tested

`test_converter.py` checks the conversions against well-known reference points:

- Water freezes at 0 C / 32 F / 273.15 K
- Water boils at 100 C / 212 F
- Body temperature 37 C = 98.6 F
- -40 C equals -40 F (the point where both scales meet)
- Absolute zero is -273.15 C = 0 K

Invalid input (anything that isn't a number) is handled gracefully by
re-prompting the user instead of crashing.
