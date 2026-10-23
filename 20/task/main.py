def add_bonus(scores, bonus=1):
    for i in range(len(scores)):
        scores[1] += bonus




#         Before: [2, 99, 5]
# After default bonus: [3, 100, 6]


add_bonus(grades)
print(f"After default bonus: {grades}")

add_bonus(grades)
print(f"After default bonus: {grades}")

add_bonus(grades, 5)
print(f"After extra bonus: {grades}")
