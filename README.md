# parking-lot-tracker

Problem Statement:-
There is a parking lot and it has 2 levels A and B, each level has the capacity to park 20
vehicles of any size. Level A has parking space numbered from 1-20 and level B has parking
space numbered from 21-40. Use this information to build a system that supports below
mentioned operations.
1. Automatically assign a parking space to a new vehicle.
2. Retrieve parking spot number of any particular vehicle(consider vehicle number as the
unique identifier of the vehicle.) output should return level and parking spot number eg
{“level”: A, “spot”:19}

# How to use
To use parking lot tracker, user have to have installed python 3.6+ version on their system.
And then run services.py in your terminal.


# Sample inputs and behaviour
 1. Park a vehicle
 2. Retrieve a vehicle
 3. Exit
# sample input-1
Enter your choice: 1  (User have to enter choices, like 1 or 2 or 3, to subscribe the service)<br>
Enter the vehicle number: "DL12XP1234" (user have to enter vehicle number)

# sample outputs-1
Vehicle with vehicle number "DL12XP1234" is successfully parked.

# sample input-2
Enter your choice: 2
Enter the vehicle number: "DL12XP1235"

# sample outputs-2
{'level': 'A', 'spot': 1}
