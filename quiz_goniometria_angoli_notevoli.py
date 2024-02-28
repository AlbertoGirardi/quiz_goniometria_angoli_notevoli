import fractions
import math

def main():
    angles = [30, 45]  # Angles in degrees
    for angle in angles:
        radians = math.radians(angle)  # Convert angle to radians
        fraction = fractions.Fraction(radians / math.pi).limit_denominator()  # Convert radians to fraction of pi
        user_input = input(f"What is the value of {angle} degrees in radians as a fraction of pi? ")
        try:
            user_fraction = fractions.Fraction(user_input)
            if user_fraction == fraction:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {fraction}.")
        except ValueError:
            print("Invalid input. Please enter the fraction in the format 'a/b'.")

if __name__ == "__main__":
    main()
