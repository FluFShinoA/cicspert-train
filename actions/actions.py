# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from actions.conn import queryDB
from actions.assessment_questions import *
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTuitFee(Action):

    def name(self) -> Text:
        return "action_tuition_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sql = "SELECT response from responses WHERE name = 'tuition'"
        dispatcher.utter_message("Es ist "+ str(queryDB(sql))+ "\nWie viel deine units?")
        return []


class ActionCalcTuit(Action):

    def name(self) -> Text:
        return "action_calculate_tuition_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sql = "SELECT response from responses WHERE name = 'tuition'"
        numberUnits = tracker.get_slot("number_of_units")
        total = int(numberUnits) * int(queryDB(sql))
        dispatcher.utter_message("Der Total fur die nummer von units ist " + str(total) + "\n\n")
        return []

class ActionCalcTuit(Action):

    def name(self) -> Text:
        return "action_entry_grade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sql = "SELECT response from responses WHERE name = 'transfer_gwa'"
        sql2 = "SELECT response from responses WHERE name = 'freshmen_grade'"
        dispatcher.utter_message("Entry grade for freshmen is" + str(queryDB(sql)) +
                                 "For transferees, " + queryDB(sql2))
        return []

class ActionCalcTuit(Action):

    def name(self) -> Text:
        return "action_start_of_class"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sql = "SELECT response from responses WHERE name = 'start_of_class'"
        dispatcher.utter_message("Start of class for this school year is" + queryDB(sql))
        return []