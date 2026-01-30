data = [22, "Hai", "Kya", 23, "Akshay", 32]

new_list = []

vowels = "aeiou"
result = {}

for i in data:
    if isinstance(i, str):
        new_list.append(i)

print(new_list)



for word in new_list:
    count = 0
    for ch in word.lower():
        if ch in vowels:
            count += 1
    result[word.lower()] = count

print(result)

