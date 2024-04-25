# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Form, AllSlotsReset
from rasa_sdk.types import DomainDict

    
#----------------------CAREER ASSISTANCE FLOW------------------------

class ValidatePreferenceForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_preference_form"

    def validate_preference1(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference1' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference1": None}

        return {"preference1": slot_value}

    def validate_preference2(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference2' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference2": None}

        return {"preference2": slot_value}

    def validate_preference3(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference3' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D","E", "F"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D, E, F ")
            return {"preference3": None}

        return {"preference3": slot_value}

    def validate_preference4(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference4' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference4": None}

        return {"preference4": slot_value}

    def validate_preference5(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference5' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference5": None}

        return {"preference5": slot_value}

    def validate_preference6(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference6' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference6": None}

        return {"preference6": slot_value}

    def validate_preference7(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference7' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference7": None}

        return {"preference7": slot_value}

    def validate_preference8(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference8' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference8": None}

        return {"preference8": slot_value}

    def validate_preference9(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference9' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference9": None}

        return {"preference9": slot_value}

    def validate_preference10(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference10' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference10": None}

        return {"preference10": slot_value}

    def validate_preference11(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'preference11' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D")
            return {"preference11": None}

        return {"preference11": slot_value}

    def count_preferences(self, tracker: Tracker, dispatcher: CollectingDispatcher) -> Dict[Text, int]:
        """Counts the occurrences of each preference value and sends a message."""
        preferences = {}
        for i in range(1, 11):
            slot_name = f"preference{i}"
            preference = tracker.get_slot(slot_name)
            if preference:
                preferences[slot_name] = preference


    def all_slots_filled(self, tracker: Tracker) -> bool:
        """Check if all preference slots are filled."""
        for i in range(1, 12):
            slot_name = f"preference{i}"
            if tracker.get_slot(slot_name) is None:
                return False
        return True

    def send_recommendation(
            self, dispatcher: CollectingDispatcher, tracker: Tracker) -> None:
        """Send the recommendation message based on preferences."""
        preferences = []
        for i in range(1,12):
            preferences.append(tracker.get_slot("preference"+str(i)))

        MapAnswerToValue = {"a": 4, "b": 3, "c": 2, "d": 1}
        criteria = {"experience": 0, "skills":0, "interest": 0}
        courses = {"BSIT": criteria.copy(),"BSCS": criteria.copy(),"BSIS": criteria.copy(),
                   "LibSci": criteria.copy(),"GameDev": criteria.copy(),"DigiAni": criteria.copy(),}

        def add_to_course_score (course,critias,letter):
            weight_map = {"experience": .2, "skills": .5, "interest": .3}
            increment_value = MapAnswerToValue[letter.lower()] * weight_map[critias]
            courses[course][critias] += increment_value

        def calculate_best_course(course_obj):
            total_score_list = []
            for k in courses:
                cscore = 0
                for c in courses[k]:
                    cscore += courses[k][c]
                total_score_list.append((k, cscore))
            best_course = max(total_score_list, key=lambda x: x[1])
            return "Best course for you is " + best_course[0] + " with " + str(round(best_course[1]/6 * 100,2)) + "% compatibility"

        def show_course_scores(course_obj):
            total_score_list = []
            for k in courses:
                cscore = 0
                for c in courses[k]:
                    cscore += courses[k][c]
                total_score_list.append((k,cscore/6*100))
            return total_score_list



        if preferences[0]:
            add_to_course_score("GameDev","interest",preferences[0])
            add_to_course_score("DigiAni", "interest", preferences[0])


        if preferences[1]:
            add_to_course_score("BSIT", "interest", preferences[1])
            add_to_course_score("BSCS", "interest", preferences[1])
            add_to_course_score("BSIS", "interest", preferences[1])
            add_to_course_score("LibSci", "interest", preferences[1])


        if preferences[2] == "A":
            add_to_course_score("BSIT", "interest", "a")
        if preferences[2] == "B":
            add_to_course_score("BSCS", "interest", "a")
        if preferences[2] == "C":
            add_to_course_score("BSIS", "interest", "a")
        if preferences[2] == "D":
            add_to_course_score("LibSci", "interest", "a")
        if preferences[2] == "E":
            add_to_course_score("GameDev", "interest", "a")
        if preferences[2] == "F":
            add_to_course_score("DigiAni", "interest", "a")

        if preferences[3]:
            add_to_course_score("BSIT","skills",preferences[3])
        if preferences[4]:
            add_to_course_score("BSCS","skills",preferences[4])
        if preferences[5]:
            add_to_course_score("BSIS","skills",preferences[5])
        if preferences[6]:
            add_to_course_score("LibSci","skills",preferences[6])
        if preferences[7]:
            add_to_course_score("GameDev","skills",preferences[7])
        if preferences[8]:
            add_to_course_score("DigiAni","skills",preferences[8])




        if preferences[9] == "A":
            add_to_course_score("BSIT", "experience", "a")
            add_to_course_score("BSCS", "experience", "a")
            add_to_course_score("BSIS", "experience", "a")
        if preferences[9] == "B":
            add_to_course_score("GameDev", "experience", "a")
        if preferences[9] == "C":
            add_to_course_score("LibSci", "experience", "a")
        if preferences[9] == "D":

            add_to_course_score("DigiAni", "experience", "a")

        if preferences[10] == "A":
            add_to_course_score("BSIT", "experience", "a")
            add_to_course_score("BSCS", "experience", "a")
            add_to_course_score("BSIS", "experience", "a")
        if preferences[10] == "B":
            add_to_course_score("GameDev", "experience", "a")
        if preferences[10] == "C":
            add_to_course_score("DigiAni", "experience", "a")
        if preferences[10] == "D":
            add_to_course_score("LibSci", "experience", "a")





        scorelist = show_course_scores(courses)
        for i in scorelist:
            dispatcher.utter_message(i[0]+ ": " + str(round(i[1],2)) + "%")

        dispatcher.utter_message(calculate_best_course(courses))
        encouraging_message1 = "I believe this course is a great fit for you\n"
        encouraging_message2 ="As long as you study hard and keep yourself motivated, You can easily pass this course.\n"
        encouraging_message3 ="Feel free to try again if you think there are inaccuracies with the results.\n"
        encouraging_message4 ="Also don't hesitate to reach out to friends, parents, or even counselors if you are still unsure of what course to take."
        dispatcher.utter_message(encouraging_message1+encouraging_message2+encouraging_message3+encouraging_message4)
    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if self.all_slots_filled(tracker):
            self.send_recommendation(dispatcher, tracker)

            return []

        return []
    

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]