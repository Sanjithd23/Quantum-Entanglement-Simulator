import numpy as np 
zero = np.array([1,0])
one = np.array([0,1])

print("Zero:", zero)
print("One:", one)

def tensor(a,b):
    return np.kron(a,b)
psi = tensor(zero,zero)

print("state |00>:", psi)
H = (1/np.sqrt(2)) * np.array([[1,1],[1,-1]])
I = np.eye(2)
H1 = np.kron(H,I)
psi = H1@psi
print("After Hadamard:", psi)
CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])
psi = CNOT @ psi
print("After CNOT:", psi)
#compute probabilitties
probs = np.abs(psi)**2

print("Probabilites:", probs)
states = ["00","01","10","11"]
outcome = np.random.choice(states, p=probs)

print("measurement outcomes:", outcome)

def collapse(outcomes):
    if outcome == "00":
        return np.array([1,0,0,])
    elif outcomes == "01":
        return np.array([0,1,0,0])
    elif outcome == "10":
        return np.array([0,0,1,0])
    elif outcome == "11":
        return np.array([0,0,0,1])
    
psi = collapse(outcome)

print("Collapsed state:" , psi)

counts = {"00":0, "01":0, "10":0, "11":0}

for _ in range(1000):
    outcome = np.random.choice(states, p=probs)
    counts[outcome] += 1

print("Measurement counts: " , counts)