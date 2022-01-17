import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("reiser.csv", index_col = 0, skiprows = (0,1), sep = ";", encoding = "latin-1")
data = data.transpose()
plt.plot(data)
plt.xticks(fontsize=8)
plt.legend(bbox_to_anchor = (1,1))
plt.show()