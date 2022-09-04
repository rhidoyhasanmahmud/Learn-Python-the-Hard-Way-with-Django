language = 'Java'  # 4 Char = [0->J][1->a][2->v][3->a]
language2 = "Python"  # 6 Char = [0->P][1->y][2->t][3->h][4->o][5->n]

print(language[0])  # J
# print(language[5])  # IndexError: string index out of range

print(language[1:3])  # av
print(language[0:2])  # Ja
print(language[0:4])  # Java

print(language[:1])  # J
print(language[0:])  # Java

print(language[-1])  # v
