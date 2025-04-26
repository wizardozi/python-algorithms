def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    """
    Given a list of words and an integer k, return the k most frequent words in the list.
    If two words have the same frequency, return them in alphabetical order.
    """
    from collections import Counter
    import heapq

    # Count the frequency of each word
    count = Counter(words)

    # Use a heap to get the k most common words
    return [word for word, _ in heapq.nsmallest(k, count.items(), key=lambda item: (-item[1], item[0]))]
# Test cases
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(top_k_frequent_words(words, k))  # Output: ["i", "love"]      
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(top_k_frequent_words(words, k))  # Output: ["the", "is", "sunny", "day"]
words = ["a", "b", "c", "a", "b", "a"]
k = 2
print(top_k_frequent_words(words, k))  # Output: ["a", "b"]
words = ["a", "b", "c", "d", "e", "f", "g"]
k = 3
print(top_k_frequent_words(words, k))  # Output: ["a", "b", "c"]
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
k = 2
print(top_k_frequent_words(words, k))  # Output: ["apple", "banana"]
