#######################################
#                package              #
#######################################
import plotly.graph_objects as go
import os

#######################################
#                 Data                #
#######################################

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
data_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
data_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
data_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]

#######################################
#                  Fig                #
#######################################

fig = go.Figure()

fig.add_trace(go.Scatter(x=month, y=data_2014, name='2014',
                         line=dict(color='#FF4C00', width=4)
                        )
              )

fig.add_trace(go.Scatter(x=month, y=data_2007, name='2007',
                         line=dict(color='rosybrown', width=4,dash='dashdot') # dash options include 'dash', 'dot', and 'dashdot'
                        )
              )
fig.add_trace(go.Scatter(x=month, y=data_2000, name='2000',
                         line = dict(color='skyblue', width=4, dash='dot')
                         )
              )

#######################################
#                Layout               #
#######################################

fig.update_layout(title='Average Temperatures in New York',
                   xaxis_title='Month',
                   yaxis_title='Temperature (degrees F)')

#######################################
#              Save Fig               #
#######################################

if os.path.exists('Fig_Save') :
    pass
else :
    os.mkdir('Fig_Save')

fig.write_html(r'Fig_Save\Line_lab.html')