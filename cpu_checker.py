#!/usr/bin/python3

import multiprocessingAAAAAAAAAAAAAAAAAAAAAAAAAA
import os
from slackclient import SlackClient

# VARS
core_count = float(multiprocessing.cpu_count())
fifteen_minute_load = os.getloadavg()[2]
one_minute_load = os.getloadavg()[0]


# FUNCTIONS
def send_message(signal):
    if signal == 'load_high_but_falling':
        return "send message to slack"
    if signal == 'load_high_and_climbing':
        return "send alternative msg to slack"


#LOGIC
if fifteen_minute_load > core_count:
    if one_minute_load <= fifteen_minute_load:
        send_message('load_high_but_falling')
    else:
        send_message('load_high_and_climbing')

print(fifteen_minute_load)
print(core_count)

#Testing ...

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#bus-routing-app",
  text="Hello from Python! :tada:"
)
