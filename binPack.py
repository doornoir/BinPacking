def first_fit(items, capacity):
  bins = []

  for item in items:
    placed = False
  
    for i in range(len(bins)):
      if item <= bins[i]:
        bins[i] = bins[i] - item
        plaed = True
        break
  
    if placed == False:
      bins.append(capacity - item)

return len(bins)

def first_fit_decreasing(items, capacity):
    # First Fit Decreasing code


def best_fit(items, capacity):
    # Best Fit code


def best_fit_decreasing(items, capacity):
    # Best Fit Decreasing code


# Read bin.txt

# For each test case:
#     run first_fit
#     run first_fit_decreasing
#     run best_fit
#     run best_fit_decreasing
#     print results
