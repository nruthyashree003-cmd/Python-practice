import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

try:
    position = int(input("Enter insertion position: "))
    element = input("Enter new sensor reading: ")

    if not element.isdigit():
        raise ValueError("Only integer values are allowed.")

    if position < 0 or position > len(arr):
        raise IndexError("Invalid insertion position.")

    arr = np.insert(arr, position, int(element))

    print("Updated Array:", arr)

except ValueError as e:
    print("Value Error:", e)

except IndexError as e:
    print("Index Error:", e)

finally:
    print("Sensor reading insertion process completed.")