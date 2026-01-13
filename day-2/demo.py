import re

text = "go go go no no no yes yes yes yes"
N = 3

# Outer group captures full repeated sequence
pattern = rf"(\b(\w+)\s+(\2\b){{{N-1}}})"
matches = re.findall(pattern, text)

# Extract full repeated sequences
full_matches = [m[0] for m in matches]
print(full_matches)
