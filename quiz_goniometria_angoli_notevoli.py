import fractions
import math

def generate_angles():
    angles = set()  # Using a set to avoid duplicates
    for i in range(1, 13):
        angle_30 = 30 * i
        angle_45 = 45 * i
        if angle_30 <= 360:
            angles.add(angle_30)
        if angle_45 <= 360:
            angles.add(angle_45)
    return sorted(angles)  # Sorting the angles before returning

def main():
    angles = generate_angles()
    incorrect_answers = 0
    mistaken_angles = []
    
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
                incorrect_answers += 1
                mistaken_angles.append(angle)
        except ValueError:
            print("Invalid input. Please enter the fraction in the format 'a/b'.")
    
    print("\nSummary:")
    print(f"Total incorrect answers: {incorrect_answers}")
    print("Angles mistaken:")
    for angle in mistaken_angles:
        print(angle)

if __name__ == "__main__":
    main()
