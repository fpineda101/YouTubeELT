from datetime import timedelta, datetime

def parse_duration(duration_str):
    """
    Parses a duration string formatted as 'HH:MM:SS' and returns the total duration in seconds.

    Args:
        duration_str (str): Duration string in the format 'HH:MM:SS'.

    Returns:
        int: Total duration in seconds.
    """

    duration_str = duration_str.replace('P', '').replace('T', '')

    components = ['D','H','M','S']
    values = {'D':0,'H':0,'M':0,'S':0}

    for component in components:
        if component in duration_str:
            value, duration_str = duration_str.split(component)
            values[component] = int(value)

    total_duration = timedelta(days=values['D'], hours=values['H'], minutes=values['M'], seconds=values['S'])

    return total_duration

def transform_data(row):

    duration_td = parse_duration(row['duration'])

    row['Duration'] = (datetime.min + duration_td).time()

    row['Vidio_Type'] = 'Short' if duration_td < timedelta(minutes=60) else 'Normal'

    return row 

 
