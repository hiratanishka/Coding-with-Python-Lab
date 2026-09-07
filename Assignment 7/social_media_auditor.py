"""
Program: AI Social Media Auditor
Purpose: Perform word-frequency analysis on text and compare follower
         lists from two social media platforms using dictionaries and sets.

Author: Tanishka Hira
Date: 07-09-2026
Task 1: Word Count
Before counting words, we need to clean up the text. Python treats words differently based on capitalization and punctuation—so "AI", "ai", and "AI," would end up as separate entries. To fix this, we convert everything to lowercase and strip off surrounding punctuation before logging each word's frequency.

Task 2:
When comparing follower lists across two platforms, Python sets make it straightforward to spot overlapping and unique users:

i.   Users on both platforms: Found using set intersection (set_a & set_b).
ii.  Platform A only: Found using set difference (set_a - set_b). Keep in mind that order matters here—set_a - set_b yields users unique to Platform A, whereas set_b - set_a isolates users on Platform B.
iii. Platform B only: Found using set difference (set_b - set_a).
iv.  Single-platform users: Found using symmetric difference (set_a ^ set_b). This extracts everyone who follows on only one platform, without breaking down which specific platform they use.
"""


'''--- Task 1 ---'''

import string

text = ("AI is changing the world. ai is powering new tools, and AI is helping researchers learn faster. The world loves AI, and the world depends on it more each year."
)

word_counts = {}

for raw_word in text.split():
    cleaned_word = raw_word.lower().strip(string.punctuation)

    if not cleaned_word:
        continue

    word_counts.setdefault(cleaned_word, 0)
    word_counts[cleaned_word] += 1

print("-- TASK 1: WORD FREQUENCY COUNTER --")

for word,count in word_counts.items():
    print(word, ":", count)



'''-- Task 2 --'''

platform_a_followers = ["u101", "u102", "u103", "u104", "u105"]
platform_b_followers = ["u103", "u104", "106", "u107"]

set_a = set(platform_a_followers)
set_b = set(platform_b_followers)

both_platforms = set_a & set_b # intersection
only_a = set_a - set_b         # unique to Platform A
only_b = set_b - set_a         # unique to Platform B

either_only = set_a ^ set_b    # only_a | only_b (symmetric difference operator)


print("\n")
print("-- TASK 2: The Follower Deduplicator --")
print("Follows on both platforms (&): ", both_platforms)
print("Unique to Platform A (-): ", only_a)
print("Unique to Platform B (-): ", only_b)
print("Unique to exactly one platform (^): ", either_only)



'''-- Edge Cases to Handle --'''
'''1. An empty paragraph'''

print("Edge Cases to Handle")
text = ""
word_counts = {}

for word in text.split():
    word = word.lower().strip(string.punctuation)
    
    if not word:
        continue

    word_counts.setdefault(word, 0)
    word_counts[word] += 1

print("1. An empty paragraph: ", word_counts)

'''2. A word that is punctuation only'''
text = "--"
word_counts = {}

for word in text.split():
    word = word.lower().strip(string.punctuation)
    
    if not word:
        continue

    word_counts.setdefault(word, 0)
    word_counts[word] += 1
print("2. A word that is punctuation only: ", word_counts)


'''3. Two follower lists with no overlap at all'''
platform_a_followers = ["u101", "u102", "u103"]
platform_b_followers = ["u104", "u105", "u106"]

set_a = set(platform_a_followers)
set_b = set(platform_b_followers)

both_platforms = set_a & set_b
only_a = set_a - set_b
only_b = set_b - set_a

print("3. Two follower lists with no overlap at all;")
print("Both:", both_platforms)
print("Only A:", only_a)
print("Only B:", only_b)


'''4. Two identical follower lists'''
platform_a_followers = ["u101", "u102", "u103"]
platform_b_followers = ["u101", "u102", "u103"]

set_a = set(platform_a_followers)
set_b = set(platform_b_followers)

both_platforms = set_a & set_b
only_a = set_a - set_b
only_b = set_b - set_a
print("4. Two identical follower lists; ")
print("Both:", both_platforms)
print("Only A:", only_a)
print("Only B:", only_b)














