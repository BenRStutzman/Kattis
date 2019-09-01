x_coords = []
y_coords = []

for i in range(3):
    coords = input().split()
    x_coords.append(coords[0])
    y_coords.append(coords[1])

for x_coord in x_coords:
    if x_coords.count(x_coord) == 1:
        print(x_coord, end = ' ')

for y_coord in y_coords:
    if y_coords.count(y_coord) == 1:
        print(y_coord)
    
