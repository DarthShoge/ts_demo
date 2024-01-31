import pandas as pd
import json 
import os

profiles = pd.read_csv('./data/profile.csv')

with open("./data/poap_holders.json") as json_file:
    json_data = json.load(json_file)


print(profiles.head())
# print(json_data)
profiles_by_user = profiles.groupby('owned_by').size()
profiles['date'] =  pd.to_datetime(profiles['timestamp']).dt.date

profiles_by_date =  profiles.groupby('date').size()

all_profiles_set = set(profiles['owned_by'].apply(lambda x: str(x).lower()))

def check_event_holders(event):
    holders_set = set(event['holders'])
    intersects = all_profiles_set.intersection(holders_set)
    return len(intersects)


for event in json_data:
    holder_count = check_event_holders(event)
    if holder_count > 0:
        print(f'event {event['event_id']} has a count of {holder_count}')
        break
    