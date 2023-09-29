import numpy as np
import scipy.linalg

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

steps = 10**6
start_state = 0
pi = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
pi[start_state] = 1
prev_state = start_state

i=0
while i<steps:
    curr_state = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11], p=A[prev_state])
    pi[curr_state]+=1
    prev_state = curr_state
    i +=1


print("yas = ", pi/steps)
print("")

steps = 10**3
A_n= A

i=0
while i<steps:
    A_n = np.matmul(A_n, A)
    i+=1

print("A^n = \n", A_n, "\n")
print("yas = ", A_n[0])
print ("")

values, left = scipy.linalg.eig(A, right=False, left = True)

print("left eigen vectors = \n", left, "\n")
print("eigen values = \n", values)
print("")

pi = left[:,0]
pi_normalized = [(x/np.sum(pi)).real for x in pi]
print (pi_normalized)