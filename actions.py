# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2
conn = psycopg2.connect(database = "exam", user = "postgres", password = "1234", host = "localhost", port = "5432")
cur = conn.cursor()

class ActionWeather(Action):

     def name(self) -> Text:
         return "action_weather"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         city = tracker.get_slot('city')
         print(city)
         sql="SELECT TEMPERATURE FROM WEATHER WHERE city='%s'"%city.upper()
         cur.execute(sql)
         print(sql)
         record = cur.fetchone()
         print(record,record[0])
         temp=str(record[0])
         speech="The temperature in " + city + " is " + temp
         dispatcher.utter_message(speech)

         return []








