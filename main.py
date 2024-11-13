from bokeh.plotting import figure, show
from bokeh.models import DatetimeTickFormatter
from utils.read_file import data_hour
import sys


plot = figure(
    title="Testing jaringan",
    x_axis_type="datetime",
    y_range=(0, 125),
    sizing_mode="stretch_width",
    width=1000,
    height=500,
    x_axis_label="DATE TIME",
    y_axis_label="Speed(Mbps)",
)

plot.xaxis[0].formatter = DatetimeTickFormatter(years="%d/%m/%Y\n%H:%M:%S",
                                                hours="%d/%m/%Y\n%H:%M:%S",
                                                months="%d/%m/%Y\n%H:%M:%S",
                                                days="%d/%m/%Y\n%H:%M:%S",
                                                )
plot.title.text_font_size = "20pt"
plot.xaxis.axis_label_text_font_size = "14pt"
plot.xaxis.axis_label_text_font_style = "normal"
plot.yaxis.axis_label_text_font_size = "14pt"
plot.yaxis.axis_label_text_font_style = "normal"
plot.ygrid.minor_grid_line_color = "navy"
plot.ygrid.minor_grid_line_alpha = 0.1
plot.line(data_hour["datetime"], data_hour["speed"], line_width=1)
plot.scatter(data_hour["datetime"], data_hour["speed"],
             color="navy", line_width=1)

show(plot)
