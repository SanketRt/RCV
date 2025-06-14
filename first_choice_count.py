def count_first_choices(ballots):
    # Complete the function
    counts = {}
    for ballot in ballots:
        if not ballot: continue
        first = ballot[0]
        counts[first] = counts.get(first, 0) + 1
    return counts



def main():
    ballots = [
        ["A", "B"],
        ["A", "B"],
        ["B", "A"],
        ["C", "A"],
        ["C", "B"]
    ]
    result = count_first_choices(ballots)
    print("First choice counts:")
    for candidate, count in result.items():
        print(f"{candidate}: {count}")


if __name__ == "__main__":
    main()