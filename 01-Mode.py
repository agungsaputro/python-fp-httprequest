from collections import Counter

def most_frequent(list):
    occurence_count = Counter(list)
    return occurence_count.most_common(1)[0][0]

def grade(grades):
    occurence_count = Counter(grades)
    return occurence_count.most_common(1)[0][0]


list = [1,2,3,4,5,6,6,8,8,6,9]
grades =  [87.5, 88.5, 60.5, 90.5, 88.5]

print(most_frequent(list))
print(grade(grades))
