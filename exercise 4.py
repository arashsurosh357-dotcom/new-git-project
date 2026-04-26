numbers = []

while True:
    user_input = input("Enter a number (or type 'exit'): ")

    # Stop the loop
    if user_input.lower() == "exit":
        break

    try:
        num = float(user_input)

        # Ignore negative numbers
        if num < 0:
            continue

        numbers.append(num)

    except ValueError:
        print("Invalid input, try again.")

# Check if empty
if len(numbers) == 0:
    print("No valid numbers entered.")
else:
    # Print numbers
    print("\nNumbers entered:", numbers)

    # Max, Min, Average
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)

    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", average)

    # Mode
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())

    if max_freq == 1:
        print("Mode: No mode (all numbers appear once)")
    else:
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        print("Mode:", modes)