row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

indexed = list(position)
index_c = int(indexed[0])
index_r = int(indexed[1])

map[index_r-1][index_c-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
