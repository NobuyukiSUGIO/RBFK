f = open('result.sol', 'r')

# result.sol ---> list
data = f.read().split()
#print(data)

R = 50
total_AS = 0

for n in range(R+1):
    print("R =", n, ": ", end="")
    # 8-byte characteristics
    for i1 in range(8):
        for j1 in range(len(data)):
            if data[j1] == "x_" + str(n) + "_" + str(i1):
                print(data[j1+1], end="")
    print(", ", end="")

    # Number of active S-box
    AS=0
    for i2 in range(4):
        for j2 in range(len(data)):
            if data[j2] == "A_" + str(n) + "_" + str(i2):
                AS += int(data[j2+1])
    total_AS += AS
    print("AS =", AS)

print("Total_AS = ", total_AS)

f.close()