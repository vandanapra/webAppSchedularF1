
from email.policy import default
import os
from matplotlib.pyplot import plot
import pandas
import logging
import plotly.express
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.figure_factory as ff


logger = logging.getLogger("outputs")


def generate(request,agent, output_folder):
    logger.info("Generating Schedule Gantt Chart and Machine Loading Chart in {}".format(output_folder))
    # jobMachineChart = []
    df = pandas.DataFrame(agent.schedule)
    fig_machine = plotly.express.timeline(
        df, x_start="Start Time", x_end="End Time", y="Machine",
        hover_data=["Input", "Output", "Coach Variant Manufactured"],
        color="Coach Variant", title=agent.title
    )
    jobMachineChart =plotly.express.timeline(
        df, x_start="Start Time", x_end="End Time", y="Machine",
        hover_data=["Input", "Output", "Coach Variant Manufactured"],
        color="Coach Variant", title=agent.title
    )
    fig_operation = plotly.express.timeline(
        df, x_start="Start Time", x_end="End Time", y="Operation",
        hover_data=["Input", "Output", "Coach Variant Manufactured"],
        color="Coach Variant")

    # fig_machine.update_yaxes(autorange="reversed")
    fig_machine.update_layout(
        # title=title,
        # xaxis_title="Time",
        yaxis_title="Machines",
        # legend_title="Legend Title",
        title_font=dict(
            family="Times New Roman",
            size=14,
            color="RebeccaPurple"
        ),
        font_family="Courier New, monospace",
        font_color='#222A2A'
        # font_color="RebeccaPurple"
    )
    fig_machine.update_yaxes(categoryorder='category ascending')
    fig_machine.update_yaxes(autorange="reversed")
    layout = {
        'title':'machine_lodaing',
        'xaxis_title':'Time',
        'yaxis_title':'Machines',
        'height':420,
        'width':560,
    }
    fig_operation.update_yaxes(autorange="reversed")
    fig_machine.write_html(os.path.join(output_folder, "machine_loading_fig.html"),full_html = False)
    fig_operation.write_html(os.path.join(output_folder, "operations_chart_fig.html"),full_html = False)
    