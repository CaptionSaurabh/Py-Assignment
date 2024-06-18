# Student scores
scores = [75, 88, 92, 67, 85, 94, 73, 81, 78, 90]

# 1. Calculate the total score of the class
total_score = 0
for score in scores:
    total_score += score
print("Total score of the class:", total_score)

# 2. Calculate the average score of the class
average_score = total_score / len(scores)
print("Average score of the class:", average_score)

# 3. Find and print the highest score in the class
highest_score = max(scores)
print("Highest score in the class:", highest_score)

# 4. Count how many students scored above the average score
above_average_count = 0
for score in scores:
    if score > average_score:
        above_average_count += 1
print("Number of students scored above the average:", above_average_count)

# 5. Print a list of scores in ascending order
sorted_scores = sorted(scores)
print("Scores in ascending order:", sorted_scores)