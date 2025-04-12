from scipy.stats import geom
import matplotlib.pyplot as plt

# Parameters
p = 1 / 6  # Probability of self-destruction per round
max_k = 15  # Calculate up to round 15

# Calculate cumulative probabilities (P(X ≤ k)) for k=1 to k=15
print(f"Round (k) | Cumulative Probability (P(X ≤ k))")
print("-" * 40)
for k in range(1, max_k + 1):
    cum_prob = geom.cdf(k, p)  # P(X ≤ k)
    print(f"{k:4}      | {cum_prob * 100:.2f}%")
    
# Generate data
k_values = list(range(1, max_k + 1))
cum_probs = [geom.cdf(k, p) * 100 for k in k_values]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(k_values, cum_probs, marker='o', linestyle='-', color='b')
plt.title("Cumulative Probability of Joker Self-Destructing by Round k")
plt.xlabel("Round (k)")
plt.ylabel("Probability (P(X ≤ k)) %")
plt.grid(True)
plt.xticks(k_values)
plt.show()
