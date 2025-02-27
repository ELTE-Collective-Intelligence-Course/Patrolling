import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("mean_reward.csv")

steps = data["Step"].to_numpy() 
mean_reward = data["Value"].to_numpy()

plt.figure(figsize=(10, 6))
plt.plot(steps, mean_reward, label="Mean Reward", linewidth=2, color='blue')

plt.title("Average Reward During Evaluation", fontsize=16)
plt.xlabel("Evaluation Steps", fontsize=14)
plt.ylabel("Mean Reward", fontsize=14)

plt.grid(alpha=0.4)
plt.legend(fontsize=12)

plt.savefig("images/mean_reward.png", dpi=300)
plt.show()
