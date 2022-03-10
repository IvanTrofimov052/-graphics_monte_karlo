import plotly.express as px
import plotly.graph_objects as go
import random
import math
random.seed(version = 2)


def rnd40_64():
    u = [1, 0]
    m = [45887173, 11368]
    x = [pow(2.0, -40.0), pow(-2.0, -14.0)]
    c0 = m[0]*u[0]
    c1 = m[0] * u[1] + m[1] * u[0]
    u[0] = c0 - ((c0 >> 26) << 26)
    n = c1 + (c0 >> 26)
    u[1] = n - ((n >> 14) << 14)
    return u[0] * x[0] + u[1] * x[1]

class RandomSchedule:
    def init(self, k):
        self.len = k
        self.a=[]
        self.x=[]
        self.y=[]

        for i in range(k):
            a1, a2, a3 = random.random(), random.random(), random.random()

            self.a.append([a1, a2, a3])

    def update(self):

        u=0
        while u < 100:
            u += 0.001
            sumi = 0
            for k in range(self.len):
                sumi += math.sqrt(-2*math.log1p(self.a[k][0]-1))*math.cos(u*self.a[k][1]+6.14*self.a[k][2])

            self.x.append(u)
            self.y.append(sumi)

    def show(self, fig):
        fig.add_trace(go.Scatter(
        x=self.x,
        y=self.y,
        name='Gaps',
        ))
            

fig = go.Figure()


for i in range(4):
    a = RandomSchedule(k=2)
    a.update()
    a.show(fig)

print("END")
        



fig.show()
