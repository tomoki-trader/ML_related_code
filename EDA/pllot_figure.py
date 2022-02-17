#one val for hist
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7,7))
fig, ax = plt.subplots(1,1)
ax.hist(y, label='test', alpha=0.7, density=False, )
ax.hist(x, label='train', alpha=0.3, density=False, )
ax.legend()