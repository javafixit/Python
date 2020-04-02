#List Operations 
animals = ['cat', 'dog', 'rat', 'lion', 'elephant', 'rhino']

keyValue = [[1,2,3], ['blue', 'red', 'green']]

#Accessing elements
print("Animals of 2", animals[2])
print ("Animals of -3",animals[-3])

print("key value of 1 2",keyValue[1][2])

print("key value of 0 -1",keyValue[0][-1])

print("Animals value between 1 and 3 ", animals[1:3])

#Inserting and Replacing

animals[1] = "tiger"

print("Animals after replacing ",animals)

animals.append("dino")

print("Animals after inserting ", animals)

animals.pop(3)

print("Animals after pop ", animals)

animals.remove("rat")

print("Animals after remove ", animals)

