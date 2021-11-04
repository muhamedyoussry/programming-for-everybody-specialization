try:
    score = float(input("Enter Score: "))

    if (score < 0 or score > 1.0):
        raise
except:
    print("Error, the score should be between 0 and 1.0")
    quit()

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
else:
    print("Your score number is not in the 0 - 1 range.")
