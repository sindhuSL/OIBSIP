def calculate_bmi():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters: "))
            
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be positive numbers. Please try again.\n")
                continue
            
            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)
            
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi <= 24.9:
                category = "Normal"
            elif 25 <= bmi <= 29.9:
                category = "Overweight"
            else:
                category = "Obese"
            
            print(f"\nYour BMI is: {bmi}")
            print(f"Category: {category}\n")
            break
            
        except ValueError:
            print("Error: Please enter valid numeric values only.\n")

if __name__ == "__main__":
    print("=== BMI Calculator ===\n")
    calculate_bmi()