def expand_around_center(s, left, right):
    """
    Expand around the center to find the length of the palindrome.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    if not s:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)      # Odd length
        len2 = expand_around_center(s, i, i + 1)  # Even length
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]
