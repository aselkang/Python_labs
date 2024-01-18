def find_common_participants(str1, str2, sep_value=','):
    list1 = str1.split(sep=sep_value)
    list2 = str2.split(sep=sep_value)
    common_participants = []
    for i in list1:
        for j in list2:
            if i == j:
                common_participants.append(i)
    return sorted(common_participants)

str1 = 'Иванов,Смирнов,Кузнецов,Попов,Васильев,Петров,Михайлов,Новиков,Фёдоров,Морозов,'
str2 = 'Морозов,Иванов,Волков,Алексеев,Васильев,Семенов,Смирнов'
print(find_common_participants(str1, str2))
