#loops

name = "MySpace"

#if else
if name != "MySpace":
	print("The name ",name," is not MySpace")
else:
	print("The name is MySpace")

#if elif
if name=="MySpace":
	print("Its my Space")
elif name == "YourSpace":
	print("Its your space")
else:
	print("No Match")

#for loop
for i in range(5):
	print("Its the range (5): ",str(i))

for i in range(5,7):
	print("Its the range (5,7): ",str(i))

for i in range(0,10,2):
	print("i=i+2 concept from 0 = 10: ",str(i))

name = "Spacious" #changing to test while loop

#while
while (name != 'MySpace'):
	print("Its not MySpace, its Different")
	name = "MySpace"