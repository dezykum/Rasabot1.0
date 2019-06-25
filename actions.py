# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
from __future__ import absolute_import,division,unicode_literals
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import sqlite3

class ActionDb(Action):
    def name(self) -> Text: 
        return 'action_db'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = sqlite3.connect('docdatabase.db')
        print("connected")
        cursor = db.cursor()
        PersonName = tracker.get_slot('categories')
        q = "select * from docdetails WHERE specialization = '{}';".format(PersonName)
        try:
            cursor.execute(q)
            if cursor.execute(q)==0:
                print("Sorry, could not find any relevant data. Please contact 1234 for further assistance.")
            # results = cursor.fetchall()
            # docarray = array[results]
            # print(results)
            # not all(results)
            col_names = [cn[0] for cn in cursor.description]
            rows = cursor.fetchall()
            print ("{:6} {:10} {:2} {:2}  {:10}  {:10}".format(col_names[0], col_names[1], col_names[2],col_names[3],col_names[4],col_names[5]))
            list = []
            for row in rows:

                data ="{:<6} {:<10}   {:2}   {:2}  {:10}  {:10}".format(row[0], row[1], row[2],row[3],row[4],row[5])
                list.append(data)
                print (list)
                print(type(list))


                # tup = data.split(',')
                # print (tup)
        except:
            print ("Error: unable to fetch data")
        finally:
            db.close()
        for value in list:
            response = "{}".format(value) 
        # response1 ="{:<6} {:<10}   {:2}   {:2}  {:10}  {:10}".format(row[0], row[1], row[2],row[3],row[4],row[5])
        # response2 ="{:<6} {:<10}   {:2}   {:2}  {:10}  {:10}".format(row[0], row[1], row[2],row[3],row[4],row[5])
        # response = """The detail is as follows {}.""".format(details)
        # response = """Doctor, {0[0]} is a {0[1]} having total experience {0[2]}, His/Her rating is {0[3]} and He/She is available on {0[4]}, time {0[5]}. \n""".format(tup)
            dispatcher.utter_message(response)
        # dispatcher.utter_message(response2)

        return [SlotSet('categories', PersonName)]

