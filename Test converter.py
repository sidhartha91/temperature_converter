"""
Tests for the temperature converter
===================================

Verifies the conversion functions against well-known reference points
(freezing, boiling, body temperature, absolute zero).

Run with:  python test_converter.py
"""

from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
)

# A small tolerance for floating-point comparisons.
TOL = 1e-9


def approx(a, b):
    return abs(a - b) < TOL


def run_tests():
    cases = [
        # (description, actual, expected)
        ("Water freezes: 0 C -> 32 F", celsius_to_fahrenheit(0), 32),
        ("Water boils: 100 C -> 212 F", celsius_to_fahrenheit(100), 212),
        ("Body temp: 37 C -> 98.6 F", celsius_to_fahrenheit(37), 98.6),
        ("Equal point: -40 C -> -40 F", celsius_to_fahrenheit(-40), -40),
        ("Water freezes: 32 F -> 0 C", fahrenheit_to_celsius(32), 0),
        ("Water boils: 212 F -> 100 C", fahrenheit_to_celsius(212), 100),
        ("Absolute zero: -273.15 C -> 0 K", celsius_to_kelvin(-273.15), 0),
        ("Water freezes: 0 C -> 273.15 K", celsius_to_kelvin(0), 273.15),
        ("Room temp: 300 K -> 26.85 C", kelvin_to_celsius(300), 26.85),
    ]

    passed = 0
    for desc, actual, expected in cases:
        if approx(actual, expected):
            print(f"PASS  {desc}")
            passed += 1
        else:
            print(f"FAIL  {desc}  (got {actual}, expected {expected})")

    print(f"\n{passed}/{len(cases)} tests passed.")


if __name__ == "__main__":
    run_tests()
