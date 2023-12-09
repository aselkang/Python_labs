users = list(map(str, input().split()))
visits = {
    "Общее количество":0,
    "Уникальные посещения":0
}
visits["Общее количество"] = len(users)
unique_users = set(users)
visits["Уникальные посещения"] = len(unique_users)
print(visits)