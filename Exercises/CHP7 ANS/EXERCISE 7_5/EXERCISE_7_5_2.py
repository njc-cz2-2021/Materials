import csv

with open("/workspaces/Materials/Exercises/CHP7 ANS/EXERCISE 7_5/Ex_7_4_scores.csv", "r") as f:
    scores = f.readlines()
    scores = [score.strip().split(",") for score in scores[1:]]

with open("/workspaces/Materials/Exercises/CHP7 ANS/EXERCISE 7_5/Ex_7_4_competitor.csv", "r") as f:
    competitors = f.readlines()
    competitors = [competitor.strip().split(",") for competitor in competitors[1:]]


final = []
for competitor in competitors:
    competitor_info = []
    competitor_info.extend([competitor[0], competitor[1]])
    for score in scores:
        if competitor[0] == score[0]:
            competitor_info.extend([score[2]])
    final.append(competitor_info) 

def task2(n):
    returned = []
    if n == 1:
        for entry in final:
            try:
                returned.append([entry[1], entry[2]])
            except IndexError:
                pass
    elif n == 2:
        for entry in final:
            try:
                returned.append([entry[1], entry[3]])
            except IndexError:
                pass
    elif n == 3:
        for entry in final:
            try:
                returned.append([entry[1], entry[4]])
            except IndexError:
                pass
    else: 
        return "Invalid task number. Please enter 1, 2, or 3."
    
    return sorted(returned, key=lambda x: x[1], reverse=True)

def meann():
    mean_scores = []
    for entry in final:
        rounds = len(entry) - 2
        total = 0
        for i in range(2, len(entry)):
            try:
                total += float(entry[i])
            except ValueError:
                continue
        mean_scores.append([entry[1], f"{total/rounds:.2f}"])
    return sorted(mean_scores, key=lambda x: x[0])

def qual():
    qualified = []
    for entry in final:
        total = 0
        for i in range(2, len(entry)):
            try:
                total += float(entry[i])
            except ValueError:
                continue
        if total > 250:
            qualified.append([entry[1], total])
    return sorted(qualified, key=lambda x: x[0])