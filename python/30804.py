n = int(input())
s = list(map(int, input().split()))

left = 0
max_length = 0
freq = {}  

for right in range(n):

    freq[s[right]] = freq.get(s[right], 0) + 1 # Count the frequency of the current element
    
    while len(freq) > 2: # More than 2 distinct elements in the window
        freq[s[left]] -= 1 # Decrease the frequency of the leftmost element
        if freq[s[left]] == 0:# Remove it from the dictionary if its frequency is 0
            del freq[s[left]]# Remove the element from the dictionary
        left += 1 # Move the left pointer to the right
        
    if len(freq) <= 2:
        max_length = max(max_length, right - left + 1)

print(max_length)
