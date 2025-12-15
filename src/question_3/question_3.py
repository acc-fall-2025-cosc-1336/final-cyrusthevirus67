def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    len_s = len(dna_string1)
    len_t = len(dna_string2)

    for i in range(len_s - len_t + 1):
        if dna_string1[i:i + len_t] == dna_string2:
            positions.append(i + 1) 

    return tuple(positions)


def get_most_likely_ancestor_consenus(dna_string1, dna_string2):
    return get_most_likely_ancestor_consensus(dna_string1, dna_string2)


def main():
    while True:
        while True:
            dna1 = input("Enter DNA string (>8 chars and <=16): ").upper()
            if 8 < len(dna1) <= 16:
                break
            print("Invalid length.")

        while True:
            dna2 = input("Enter DNA substring (4 chars): ").upper()
            if len(dna2) == 4:
                break
            print("Invalid length.")

        result = get_most_likely_ancestor_consensus(dna1, dna2)

        if result:
            print("Substring found at positions:", *result)
        else:
            print("Substring not found.")

        again = input("Try again? (y/n): ").lower()
        if again != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
