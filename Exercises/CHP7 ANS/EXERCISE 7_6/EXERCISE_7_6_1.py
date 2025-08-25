with open("./Materials/Exercises/CHP7 ANS/EXERCISE 7_6/MEMBER.txt", "r") as f:
    lines = f.readlines()
    members = {line.split(",")[0]: ([line.split(",")[2].strip()+ " " + line.split(",")[1].strip()]) for line in lines}

with open("./Materials/Exercises/CHP7 ANS/EXERCISE 7_6/BOOK.txt", "r") as f:
    lines = f.readlines()
    books = {line.split(",")[0].strip(): line.split(",")[1].strip() for line in lines}

with open("./Materials/Exercises/CHP7 ANS/EXERCISE 7_6/LOAN.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        entry, member_id, book_id, date, status = line.split(",")
        if member_id in members:
            members[member_id].append(books[book_id])
            members[member_id].append(status.strip())

def task_1(requested_id):
    if requested_id in members:
        for i in range(1, (len(members[requested_id])-1)//2):
            if members[requested_id][i+1] == "TRUE":
                print(f"{members[requested_id][i]} (Returned)")
            else:
                print(f"{members[requested_id][i]} (Not Returned)")

def task_2():
    ans = []
    for member_id, details in members.items():
        entry = []
        entry.append(f"{members[member_id][0]}")
        for i in range(1, (len(members[member_id])-1)//2):
            if members[member_id][i+1] == "FALSE":
                entry.append(f"{members[member_id][i]}")
        if len(entry) > 1:
            ans.append(entry)
    return ans

