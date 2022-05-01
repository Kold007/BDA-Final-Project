import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import pandas as pd


#Function for plotting classification report from sklearn
def plot_clf_report(clf_report, title, cmap):
    plt.figure(figsize = (5,4), dpi = 170)
    fig = sns.heatmap(pd.DataFrame(clf_report).iloc[:-1, :].T, annot=True, cmap = cmap)
    fig.set_title(title)
    plt.show()

