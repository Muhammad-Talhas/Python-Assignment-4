def average(a: float, b: float) -> float:
    """
    Returns the average (midpoint) between a and b.
    """
    return (a + b) / 2  # Directly return the calculated average.

def main():
    # Calculate the averages
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    # Calculate the final average of the two previous averages
    final_avg = average(avg_1, avg_2)
    
    # Display results
    print(f"avg_1: {avg_1}")
    print(f"avg_2: {avg_2}")
    print(f"final average: {final_avg}")

# Ensure that the program only runs when executed directly
if __name__ == '__main__':
    main()
