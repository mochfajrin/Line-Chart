import pandas as pd
import re
from utils.converter import convert_to_mbps, convert_to_datetime

file = pd.read_fwf("data/soal_chart_bokeh.txt").to_string()
find_speed_regex = r"(\d+(\.\d+)?)\s*(\S+)\s*/sec.*sender"
find_timestamp_regex = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
sender_speed_list_raw = re.findall(find_speed_regex, file)
sender_timestamp_list = re.findall(find_timestamp_regex, file)
sender_speed_list = convert_to_mbps(sender_speed_list_raw)
sender_datetime_list = convert_to_datetime(sender_timestamp_list)

data = pd.DataFrame({
    "speed": sender_speed_list,
    "datetime": sender_datetime_list
})


data["datetime"] = pd.to_datetime(data["datetime"])
data_hour = data.groupby(
    pd.Grouper(key="datetime", freq="h")
).mean().reset_index().fillna(0)
