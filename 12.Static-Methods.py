class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        fahrenheit = (celsius * 9/5) + 32
        print(f"[Converter] {celsius}°C = {fahrenheit}°F")
        return fahrenheit



def main():
    print("Temperature Conversion:")
    c1 = 0
    c2 = 25
    c3 = 100

    TemperatureConverter.celsius_to_fahrenheit(c1)
    TemperatureConverter.celsius_to_fahrenheit(c2)
    TemperatureConverter.celsius_to_fahrenheit(c3)


if __name__ == "__main__":
    main()
