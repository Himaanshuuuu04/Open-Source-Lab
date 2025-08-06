words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'tab']

print("Original list of words:")
print(words)

print("\nAnagrams found:")

def find_anagrams(word_list):
    anagram_groups = {}
    
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    
    return anagram_groups

anagram_groups = find_anagrams(words)

for key, group in anagram_groups.items():
    if len(group) > 1:
        print(f"Anagrams: {group}")

print("\nAll anagram groups:")
for key, group in anagram_groups.items():
    print(f"{group}")
