def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height**2)
    print(f"BMI =  {bmi:.2f}")
    if bmi<18:
        print("Under Weight")
        return -1
    elif bmi<24.9:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1
calculate_bmi(weight=57, height=1.73)
