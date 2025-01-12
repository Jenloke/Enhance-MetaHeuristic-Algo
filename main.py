# Basic File Reading Python
file = [100,200,500,1000, 2000,5000,10000]
log = 0
for i in range(3):
  for x in file:
    file1 = open(f"./Dataset/{i+1}/{x}/knapPI_{i+1}_{x}_1000_1", "r")
    log = log + 1
    print(file1)

print(log)