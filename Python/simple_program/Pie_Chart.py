#######################################
#                package              #
#######################################
import plotly.graph_objects as go
import os

#######################################
#                 Data                #
#######################################

labels = ['Label_1','Label_2','Label_3','Label_4']
values = [4300, 2200, 1053, 500]

#######################################
#                  Fig                #
#######################################

fig = go.Figure()
fig.add_trace(go.Pie(labels=labels,
                     values=values ,
                     hoverinfo='label+value'
                     )
              )

#######################################
#                Layout               #
#######################################

fig.update_layout(title = 'Pie Plot' ,
                  width = 1000 ,
                  height = 600,
                 )

#######################################
#              Save Fig               #
#######################################

if os.path.exists('Fig_Save') :
    pass
else :
    os.mkdir('Fig_Save')

fig.write_html(r'Fig_Save\Pie_lab.html')