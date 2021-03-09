import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

complete = pd.read_csv('complete.csv', index_col=False)
nj = complete[complete['State'] == 'new_jersey']
nj = nj.loc[15:]
fig = go.Figure(layout=go.Layout(
        updatemenus=[dict(type="buttons", direction="right", x=0.9, y=1.16)], title="New Jersey - Sports Betting Revenue"))
# Add traces
init = 1
fig.add_trace(go.Scatter(x=nj['Date'], y=nj['Revenue'], name='New Jersey'))
# Animation
fig.update(frames=[go.Frame(data=[go.Scatter(x=nj['Date'][:k], y=nj['Revenue'][:k])]) for k in range(init, len(nj)-1)])
# Buttons
fig.update_layout(updatemenus=[dict(buttons=list([dict(label="Play", method="animate", args=[None, {"frame": {"duration": 1000}}])]))])
fig.update_layout(xaxis_title="Date", yaxis_title="Revenue", template='seaborn', legend_title="Comparison", paper_bgcolor='rgba(0,0,0,0)', font=dict(family='Tahoma', size=12))
fig.show()