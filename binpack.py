import time


# ------------------------------------------------------------
# FIRST FIT
# Place each item into the first bin where it fits.
# If the item does not fit in any current bin, create a new bin.
# ------------------------------------------------------------
def first_fit(items, capacity):

    # Stores the remaining capacity of each bin
    bins = []

    # Go through each item in the original order
    for item in items:

        # Assume the item has not been placed yet
        placed = False

        # Search through the existing bins in order
        for i in range(len(bins)):

            # Check if the item fits in this bin
            if item <= bins[i]:

                # Update the remaining capacity of the bin
                bins[i] = bins[i] - item

                # Mark the item as placed
                placed = True

                # First Fit stops at the first bin that works
                break

        # If no existing bin worked, create a new bin
        if placed == False:
            bins.append(capacity - item)

    # Return the total number of bins used
    return len(bins)


# ------------------------------------------------------------
# FIRST FIT DECREASING
# Sort items from largest to smallest, then use First Fit.
# ------------------------------------------------------------
def first_fit_decreasing(items, capacity):

    # Sort items in decreasing order
    sorted_items = sorted(items, reverse=True)

    # Run First Fit on the sorted list
    return first_fit(sorted_items, capacity)


# ------------------------------------------------------------
# BEST FIT
# Check all existing bins and choose the bin that leaves
# the least remaining space after the item is placed.
# ------------------------------------------------------------
def best_fit(items, capacity):

    # Stores the remaining capacity of each bin
    bins = []

    # Go through each item
    for item in items:

        # -1 means that no valid bin has been found yet
        best_bin = -1

        # Begin with a very large value
        smallest_remaining = float("inf")

        # Best Fit must check every existing bin
        for i in range(len(bins)):

            # Check if the item fits in this bin
            if item <= bins[i]:

                # Calculate the remaining capacity
                # if the item were placed here
                remaining = bins[i] - item

                # Check if this is the best fit found so far
                if remaining < smallest_remaining:
                    smallest_remaining = remaining
                    best_bin = i

        # If a valid bin was found, place the item there
        if best_bin != -1:
            bins[best_bin] = bins[best_bin] - item

        # Otherwise, create a new bin
        else:
            bins.append(capacity - item)

    # Return the total number of bins used
    return len(bins)


# ------------------------------------------------------------
# BEST FIT DECREASING
# Sort items from largest to smallest, then use Best Fit.
# ------------------------------------------------------------
def best_fit_decreasing(items, capacity):

    # Sort items in decreasing order
    sorted_items = sorted(items, reverse=True)

    # Run Best Fit on the sorted list
    return best_fit(sorted_items, capacity)


# ------------------------------------------------------------
# MAIN PROGRAM
# Read test cases from bin.txt and run all four algorithms.
# ------------------------------------------------------------
def main():

    # Open bin.txt and split all values into a list
    with open("bin.txt", "r") as file:
        data = file.read().split()

    # Keeps track of the current position in the input file
    index = 0

    # First value is the number of test cases
    num_test_cases = int(data[index])
    index += 1

    # Process each test case
    for test_case in range(1, num_test_cases + 1):

        # Read the bin capacity
        capacity = int(data[index])
        index += 1

        # Read the number of items
        num_items = int(data[index])
        index += 1

        # Read all item weights for this test case
        items = []

        for i in range(num_items):
            items.append(int(data[index]))
            index += 1

        # Print the test case number
        print("Test Case {}".format(test_case))


        # ----------------------------------------------------
        # FIRST FIT
        # ----------------------------------------------------
        start = time.perf_counter()

        result = first_fit(items, capacity)

        end = time.perf_counter()

        print(
            "First Fit: {}, Time: {:.6f}".format(
                result,
                end - start
            )
        )


        # ----------------------------------------------------
        # FIRST FIT DECREASING
        # ----------------------------------------------------
        start = time.perf_counter()

        result = first_fit_decreasing(items, capacity)

        end = time.perf_counter()

        print(
            "First Fit Decreasing: {}, Time: {:.6f}".format(
                result,
                end - start
            )
        )


        # ----------------------------------------------------
        # BEST FIT
        # ----------------------------------------------------
        start = time.perf_counter()

        result = best_fit(items, capacity)

        end = time.perf_counter()

        print(
            "Best Fit: {}, Time: {:.6f}".format(
                result,
                end - start
            )
        )


        # ----------------------------------------------------
        # BEST FIT DECREASING
        # ----------------------------------------------------
        start = time.perf_counter()

        result = best_fit_decreasing(items, capacity)

        end = time.perf_counter()

        print(
            "Best Fit Decreasing: {}, Time: {:.6f}".format(
                result,
                end - start
            )
        )

        # Blank line between test cases
        print()


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------
if __name__ == "__main__":
    main()