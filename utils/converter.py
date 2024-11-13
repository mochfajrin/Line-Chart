from datetime import datetime


def convert_to_mbps(speed_list: list):
    result = []
    for sender_speed in speed_list:
        number = sender_speed[0]
        unit = sender_speed[2]
        if (unit == "Kbits"):
            mbits = float(number) / 1000
            result.append(mbits)
        else:
            result.append(float(number))
    return result


def convert_to_datetime(timestamp_list: list):
    results = []
    for timestamp_str in timestamp_list:
        datetime_object = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        results.append(datetime_object)
    return results


def get_data_per_hours():
    pass
