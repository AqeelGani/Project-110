import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics

df  = pd.read_csv('csv files/medium_data.csv')
data = df['claps'].tolist()
p_mean = statistics.mean(data)
p_stdev = statistics.stdev(data)
print('The Population Mean Is :', p_mean)
print('The Population Standard Deviation Is :', p_stdev)

def Graph(list):
    sample_mean = statistics.mean(list)
    sample_stdev = statistics.stdev(list)
    print('The Sampling Mean Is :', sample_mean)
    print('The Sampling Standard Deviation Is :', sample_stdev)
    fig = ff.create_distplot([list], ['Sampling Mean Distribution'], show_hist = False)
    fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 0.0035], mode = 'lines', name = 'Sample Mean'))
    fig.show()

def getSamples():
    dataset = []
    for i in range(30):
        index = random.randint(0, len(data) - 1)
        dataset.append(data[index])
    mean = statistics.mean(dataset)
    return mean

def setup():
    meanList = []
    for i in range(100):
        meanList.append(getSamples())
    Graph(meanList)

setup()