def add_time(start='00:00 AM', duration='00:00', day_week=''):
    # Total minutes in one day: 1440 min, 720 min till midday;
    import re
    new_time = ''
    next_day = next_day_aux = 0
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

    # Take the total minutes in the start string (transforming hour in minute);
    hour_start = int(re.findall('([0-9]*):', start)[0]) * 60
    minutes_start = int(re.findall(':([0-9]*)', start)[0])
    total_minutes_start = hour_start + minutes_start

    # Take the total minutes in the duration string (transforming hour in minute);
    hour_duration = int(re.findall('([0-9]*):', duration)[0]) * 60
    minutes_duration = int(re.findall(':([0-9]*)', duration)[0])
    total_minutes_duration = hour_duration + minutes_duration

    total_minutes = total_minutes_start + total_minutes_duration

    # If is AM or PM;
    hour_of_day = re.findall('[A-Z]+', start)[0]

    # Count how many days passed in the total sum of minutes;
    while total_minutes > 1440:
        total_minutes -= 1440
        next_day += 1

    # Defines if is AM or PM;
    if total_minutes < 720 and hour_of_day == 'AM':
        hour_of_day = 'AM'
    elif total_minutes >= 720 and hour_of_day == 'AM':
        hour_of_day = 'PM'
        if total_minutes >= 780:
            total_minutes -= 720
    elif total_minutes >= 720 and hour_of_day == 'PM':
        hour_of_day = 'AM'
        next_day += 1
        if total_minutes >= 780:
            total_minutes -= 720
    elif total_minutes < 720 and hour_of_day == 'PM':
        hour_of_day = 'PM'

    # Formating the hour and minutes in the string new_time;
    new_time += str(total_minutes // 60) + ':'

    if total_minutes % 60 < 10:
        new_time += '0' + str(total_minutes % 60)
    else:
        new_time += str(total_minutes % 60)

    new_time += ' ' + hour_of_day
    next_day_aux = next_day

    # If it takes day of week;
    if day_week != '':
        for c in range(0, 7):
            if days[c] == day_week.capitalize():
                next_day_aux += c
                while next_day_aux >= 7:
                    next_day_aux -= 7
                new_time += ', ' + days[next_day_aux]


    if next_day == 1:
        new_time += ' (next day)'
    elif next_day > 1:
        new_time += f' ({next_day} days later)'
    
                
    return new_time