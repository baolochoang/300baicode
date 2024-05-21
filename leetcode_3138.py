""" 
3138. Minimum Length of Anagram Concatenation
Hint
You are given a string s, which is known to be a concatenation of anagrams of some string t.
Return the minimum possible length of the string t.
An anagram is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

"""


from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        word = s
        if len(set(word)) == 1:
            return 1

        if len(set(word)) == len(word):
            return len(word)

        divisors = find_divisors(len(word))
        for i in divisors:
            chunks = divide_chunks(word, i)
            count = 0
            for j in range(0, len(chunks) - 1):
                first_segment_freq = Counter(chunks[j])
                segment_freq = Counter(chunks[j+1])
                if first_segment_freq == segment_freq:
                    count += 1
                    continue
                else:
                    break

            if count == len(chunks) - 1:
                len_anagram_chars = len(chunks[0])
                return len_anagram_chars

        return len(word)


def find_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)
  return divisors


def divide_chunks(word, size):
    chunks = [word[i:i+size] for i in range(0, len(word), size)]
    return chunks