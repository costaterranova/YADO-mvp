import pandas as pd
from random import randint as rand

def activity_finder():
    all_activities = pd.read_csv('list_of_activities.csv')
    len_all_activities = len(all_activities)
    list_of_selected_activities = []
    random_activity_index = rand(0, len_all_activities-1)
    while random_activity_index in list_of_selected_activities:
        random_activity_index = rand(0, len_all_activities-1)
    list_of_selected_activities.append(random_activity_index)
    activity = all_activities['activity'][random_activity_index]
    return activity


def time_generator():
    number = rand(8,22)
    if number > 12:
        number -= 12
        hour = f'{str(number)} PM'
    elif number < 12:
        hour = f'{str(number)} AM'
    else:
        hour = f'{str(number)} PM'
    return hour