import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    people = []
    with open(sys.argv[1], "r") as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            people.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence_file:
        sequence = sequence_file.read()

    # Find longest match of each STR in DNA sequence
    keys = list(people[0].keys())
    STRs = keys[1:]
    matches = []
    for i in range(len(STRs)):
        longest_run = longest_match(sequence, STRs[i])
        matches.append(longest_run)

    # Check database for matching profiles
    for i in range(len(people)):
        cnt = 0
        for j in range(len(STRs)):
            if int(people[i][STRs[j]]) == int(matches[j]):
                cnt += 1
        if cnt == len(STRs):
            print(people[i]["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
