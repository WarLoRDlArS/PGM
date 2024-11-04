import numpy as np

states = ["rainy", "sunny"]
hidden_states = ["walk", "shop", "clean"]

start_probability = [0.6, 0.4]
tsm = [
    [0.7, 0.3],  
    [0.4, 0.6],
]

tsm = np.array(tsm).astype(np.float32)  

epm = [
    [0.1, 0.4, 0.5], 
    [0.6, 0.3, 0.1],
]
 
def forward_algorithm(obs_sequence):
    n_states = len(states)
    n_observations = len(obs_sequence)
     
    alpha = np.zeros((n_states, n_observations), dtype=np.float64)
 
    for i in range(n_states):
        alpha[i][0] = start_probability[i] * epm[i][hidden_states.index(obs_sequence[0])]
     
    for t in range(1, n_observations):
        for j in range(n_states): 
            alpha[j][t] = (alpha[:, t - 1].dot(tsm[:, j])) * epm[j][hidden_states.index(obs_sequence[t])]

    overall_probability = sum(alpha[:, n_observations - 1])
    
    print("Alpha matrix:")
    print(alpha)
    print("Overall probability:", overall_probability)

    return alpha, overall_probability
  
forward_algorithm(["clean", "walk", "shop"])
print()

def viterbi(obs_sequence):
    n_states = len(states)
    n_observations = len(obs_sequence)
 
    alpha_values = np.zeros((n_observations, n_states), dtype=np.float64)
 
    for i in range(n_states):
        alpha_values[0][i] = start_probability[i] * epm[i][hidden_states.index(obs_sequence[0])]

    best_sequence = [states[np.argmax(alpha_values[0])]]
    print("Alpha values for the first observation:", alpha_values[0])
 
    for t in range(1, n_observations):
        for j in range(n_states): 
            max_prob = max(alpha_values[t - 1][i] * tsm[i, j] for i in range(n_states))
            alpha_values[t][j] = max_prob * epm[j][hidden_states.index(obs_sequence[t])]

        best_sequence.append(states[np.argmax(alpha_values[t])]) 

    print("Final alpha values for all observations:\n", alpha_values)
    print("Best sequence:", best_sequence)
    return alpha_values, best_sequence
   
alpha, sequence = viterbi(["clean", "walk", "shop"])
