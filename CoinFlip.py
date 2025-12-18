import random
n = int(input("Enter number of times to flip the coin: "))
heads=0
tails=0
for i in range(0,n,1):
    flip = random.random()
    if flip>=0.5:
        heads+=1
    else:
        tails+=1
        
heads=heads/n*100
tails=tails/n*100
print(f"Percentage of Heads:  {heads} %")
print(f"Percentage of Tails:  {tails} %")