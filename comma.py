items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(list(tuple(reversed(words)))))