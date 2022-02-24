import plotly.express as px
import plotly.graph_objects as go
import random
import math
random.seed(version = 2)
u = 0

x = []
y=[]

a1, a2, a3 = random.random(), random.random(), random.random()

while u < 100:
    u += 1
    sumi = 0
    for k in range(1, 11):
        sumi += math.sqrt(-2*math.log1p(a1-1))*math.cos(u*a2+6.14*a3)

    x.append(u)
    y.append(sumi)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    name='Gaps',
))

fig.show()

    
