
import numpy as np

state = {
    0: "E4",
    1: "E2",
    2: "G4",
    3: "C3",
    4: "D8",
    5: "E",
    6: "F4",
    7: "F3",
    8: "F8",
    9: "E8",
    10: "D4",
    11: "C"
}

A = np.array([[0.4285714286,0.2857142857,0.1428571429,0,0,0,0,0,0,0.1428571429,0,0], [1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0.5,0.5,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0], [0,0,0,0,0,1,0,0,0,0,0,0], [0,0,0,0,0,0,1,0,0,0,0,0],[0.25,0,0,0,0,0,0.25,0.25,0,0,0.25,0],[0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0.5,0,0,0,0,0,0,0.5,0,0],[0,0,0,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,0,0,0]])

n = 48
start_state = 0
print(state[start_state], "--->", end=" ")
prev_state = start_state

while n-1:
    curr_state = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11],p=A[prev_state])
    print(state[curr_state], "--->", end=" ")
    prev_state = curr_state
    n-=1

print("stop")

n = 48
start_state = np.random.choice([0,2,6])
print(state[start_state], "--->", end=" ")
prev_state = start_state

while n-1:
    curr_state = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11],p=A[prev_state])
    print(state[curr_state], "--->", end=" ")
    prev_state = curr_state
    n-=1

print("stop")