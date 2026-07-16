# 256. Relative Ranks
# Given an integer array score where score[i] is the score of the ith athlete,
# return an array of strings where answer[i] is the rank of the ith athlete.
# Top 3 get "Gold Medal", "Silver Medal", "Bronze Medal".

def find_relative_ranks(score):
    """
    Sort indices by score in descending order, then assign ranks.
    Time: O(n log n), Space: O(n)
    """
    # Create sorted indices (highest score first)
    sorted_indices = sorted(range(len(score)), key=lambda i: score[i], reverse=True)

    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    result = [""] * len(score)

    for rank, idx in enumerate(sorted_indices):
        if rank < 3:
            result[idx] = medals[rank]
        else:
            result[idx] = str(rank + 1)

    return result


# Example usage
if __name__ == "__main__":
    scores = [5, 4, 3, 2, 1]
    print(f"Scores: {scores}")
    print(f"Ranks: {find_relative_ranks(scores)}")
    # Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    scores2 = [10, 3, 8, 9, 4]
    print(f"\nScores: {scores2}")
    print(f"Ranks: {find_relative_ranks(scores2)}")
    # Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
