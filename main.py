class UnitConverter:
    def __init__(self):
        # Define conversion factors for different units
        self.conversion_factors = {
            'length': {
                'meter': 1.0,
                'kilometer': 1000.0,
                'centimeter': 0.01,
                'millimeter': 0.001,
                'inch': 0.0254,
                'foot': 0.3048,
                'yard': 0.9144,
                'mile': 1609.34
            },
            'mass': {
                'kilogram': 1.0,
                'gram': 0.001,
                'milligram': 1e-6,
                'pound': 0.453592,
                'ounce': 0.0283495
            },
            'temperature': {
                'celsius': 1.0,
                'fahrenheit': lambda c: (c * 9/5) + 32,
                'kelvin': lambda c: c + 273.15
            },
            'time': {
                'second': 1.0,
                'minute': 60.0,
                'hour': 3600.0,
                'day': 86400.0,
                'week': 604800.0
            },
            'volume': {
                'liter': 1.0,
                'milliliter': 0.001,
                'gallon': 3.78541,
                'quart': 0.946353,
                'pint': 0.473176,
                'cup': 0.24
            }
        }

    def convert(self, value, from_unit, to_unit, category):
        """
        Convert a value from one unit to another within a given category.
        """
        if category not in self.conversion_factors:
            raise ValueError(f"Category '{category}' not supported.")

        units = self.conversion_factors[category]

        if from_unit not in units or to_unit not in units:
            raise ValueError(f"Unit '{from_unit}' or '{to_unit}' not supported for category '{category}'.")

        # Handle temperature conversions separately due to their non-linear nature
        if category == 'temperature':
            if from_unit == 'celsius':
                if to_unit == 'fahrenheit':
                    return units[to_unit](value)
                elif to_unit == 'kelvin':
                    return units[to_unit](value)
                else:
                    return value  # No conversion needed
            elif from_unit == 'fahrenheit':
                if to_unit == 'celsius':
                    return (value - 32) * 5/9
                elif to_unit == 'kelvin':
                    return (value - 32) * 5/9 + 273.15
            elif from_unit == 'kelvin':
                if to_unit == 'celsius':
                    return value - 273.15
                elif to_unit == 'fahrenheit':
                    return (value - 273.15) * 9/5 + 32
            raise ValueError("Unsupported temperature conversion.")

        # For other categories, use the conversion factors
        from_factor = units[from_unit]
        to_factor = units[to_unit]

        # Convert to base unit first, then to target unit
        base_value = value * from_factor
        converted_value = base_value / to_factor

        return converted_value

    def get_supported_categories(self):
        """Return a list of supported conversion categories."""
        return list(self.conversion_factors.keys())

    def get_supported_units(self, category):
        """Return a list of supported units for a given category."""
        if category not in self.conversion_factors:
            raise ValueError(f"Category '{category}' not supported.")
        return list(self.conversion_factors[category].keys())

    def suggest_units(self, category):
        """Provide suggestions for units based on the category."""
        suggestions = {
            'length': "Common units: meter, kilometer, inch, foot, mile",
            'mass': "Common units: kilogram, gram, pound, ounce",
            'temperature': "Common units: celsius, fahrenheit, kelvin",
            'time': "Common units: second, minute, hour, day",
            'volume': "Common units: liter, gallon, milliliter, cup"
        }
        return suggestions.get(category, "No suggestions available for this category.")

    def interactive_conversion(self):
        """Interactively ask the user for input and perform conversions."""
        print("Welcome to the Unit Converter!")
        print("Supported categories:", ", ".join(self.get_supported_categories()))

        # Ask for category
        while True:
            category = input("Enter the category of units (e.g., length, mass, temperature): ").strip().lower()
            if category in self.get_supported_categories():
                break
            else:
                print(f"Category '{category}' is not supported. Please try again.")
                print("Supported categories:", ", ".join(self.get_supported_categories()))

        # Display supported units and suggestions
        print(f"\nSupported units for '{category}': {', '.join(self.get_supported_units(category))}")
        print("Tip:", self.suggest_units(category))

        # Ask for the value to convert
        while True:
            try:
                value = float(input(f"\nEnter the value you want to convert: ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Ask for the source unit
        while True:
            from_unit = input(f"Enter the source unit (e.g., {self.get_supported_units(category)[0]}): ").strip().lower()
            if from_unit in self.get_supported_units(category):
                break
            else:
                print(f"Unit '{from_unit}' is not supported for category '{category}'. Please try again.")
                print(f"Supported units: {', '.join(self.get_supported_units(category))}")

        # Ask for the target unit
        while True:
            to_unit = input(f"Enter the target unit (e.g., {self.get_supported_units(category)[1]}): ").strip().lower()
            if to_unit in self.get_supported_units(category):
                break
            else:
                print(f"Unit '{to_unit}' is not supported for category '{category}'. Please try again.")
                print(f"Supported units: {', '.join(self.get_supported_units(category))}")

        # Perform the conversion
        try:
            result = self.convert(value, from_unit, to_unit, category)
            print(f"\nConversion Result: {value} {from_unit} = {result:.4f} {to_unit}")
        except Exception as e:
            print(f"Error during conversion: {e}")


# Run the interactive converter
if __name__ == "__main__":
    converter = UnitConverter()
    converter.interactive_conversion()