import pytest
from lib.palindrome import longest_palindromic_substring

def test_babad():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_single_char():
    assert longest_palindromic_substring("a") == "a"

def test_two_diff_chars():
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_numeric_palindrome():
    assert longest_palindromic_substring("123321") == "123321"

def test_prefix_palindrome():
    assert longest_palindromic_substring("abcddcbafg") == "abcddcba"

def test_all_same_char():
    assert longest_palindromic_substring("aaaaa") == "aaaaa"

