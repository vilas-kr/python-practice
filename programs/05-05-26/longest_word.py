st = "I love data engineering"

words = st.split()

longest = max(words, key=len)
print(longest)