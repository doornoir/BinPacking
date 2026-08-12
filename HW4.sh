#!/bin/bash

echo "CS 325 Homework 4 - Bin Packing"
echo

# Select the submitted program.
if [ -f binpack.cpp ]; then
    echo "C++ submission detected."
    g++ binpack.cpp -std=c++11 -o binpack

    if [ $? -ne 0 ]; then
        echo "ERROR: Compilation failed."
        exit 1
    fi

    COMMAND="./binpack"

elif [ -f binpack.py ]; then
    echo "Python submission detected."
    COMMAND="python3 binpack.py"

else
    echo "ERROR: binpack.py or binpack.cpp was not found."
    exit 1
fi

# Verify that the public test files are present.
if [ ! -f bin.txt ]; then
    echo "ERROR: bin.txt was not found."
    exit 1
fi

if [ ! -f BinPackingSolution.txt ]; then
    echo "ERROR: BinPackingSolution.txt was not found."
    exit 1
fi

echo
echo "Running binpack..."
timeout 60s $COMMAND > my_results.txt
STATUS=$?

if [ $STATUS -eq 124 ]; then
    echo "ERROR: The program exceeded the 60-second time limit."
    exit 1
elif [ $STATUS -ne 0 ]; then
    echo "ERROR: The program did not finish successfully."
    exit 1
fi

echo
echo "Program output:"
cat my_results.txt

echo
echo "Comparing the reported numbers of bins with the sample solution..."

# Remove carriage returns and timing information before comparison.
# Expected result-line format:
# First Fit: 4, Time: 0.000012
#
# The timing value and unit may vary, so only the algorithm name
# and number of bins are compared.
tr -d '\r' < my_results.txt \
    | sed -E 's/,[[:space:]]*[Tt]ime([[:space:]]*\([^)]*\))?[[:space:]]*:[[:space:]]*.*$//' \
    | sed '/^[[:space:]]*$/N;/^\n$/D' \
    > my_bins.txt

tr -d '\r' < BinPackingSolution.txt > expected_bins.txt

echo
diff -y -B -b \
    --report-identical-files \
    --suppress-common-lines \
    my_bins.txt \
    expected_bins.txt

DIFF_STATUS=$?

echo
if [ $DIFF_STATUS -eq 0 ]; then
    echo "All public output values match."
else
    echo "Differences were found. Review the output shown above."
fi

echo
echo "Passing the public test does not guarantee full credit."
echo "Additional hidden test cases will be used during grading."
