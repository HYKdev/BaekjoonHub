result = ["Equilateral", "Isosceles", "Scalene", "Invalid"]

while True:
    x, y, z = map(int, input().split())
    
    if x == 0 and y == 0 and z == 0:
        break

    if x == y == z:
        print(result[0])

    elif (x+y+z) <= 2 * max(x,y,z):
        print(result[3])
    
    elif x == y or y == z or x == z:
        print(result[1])
    
    elif x != y and y != z and x != z:
        print(result[2])