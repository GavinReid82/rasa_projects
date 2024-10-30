from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from typing import List, Dict, Any

class ActionGiveInfo(Action):

    def name(self) -> str:
        return "action_give_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List:

        # Retrieve the current and last categories from slots
        category = tracker.get_slot("category")
        last_category = tracker.get_slot("last_category")
        info_index = tracker.get_slot("info_index") or 0

        # Define information lists for each category
        info_data = {
            "skills": [
                "Aside from being a lovely person, Gavin is proficient in Python programming for NLP and machine learning.",
                "He is experienced in using Rasa for conversational AI development.",
                "Gavin is skilled in web development using HTML, CSS, and JavaScript (he even built this website!).",
                "He's also competent in data analysis with tools like Pandas and NumPy.",
                "Gavin's an expert in version control with Git and GitHub.",
                "He's proficient in various programming languages including Python, JavaScript, SQL, and R.",
                "Gavin speaks English (Native), Spanish (Advanced), and French (Intermediate)."
            ],
            "qualifications": [
                "Gavin holds several qualifications, including a MA in Applied Linguistics and TESOL (University of Leicester, Distinction).",
                "He also completed a course in Data Scientist: Natural Language Processing (Codecademy, 2024).",
                "He finished CS50P: Programming with Python (Harvard) in 2024.",
                "In 2024 he gained the certificates Learn Git and GitHub, and Learn the Command Line (Codecademy).",
                "Gavin completed the Certificate in Responsive Web Design (FreeCodeCamp) in 2023, and built this website!",
                "He has also gained the Google Data Analytics Certificate (Google, 2022)."
            ],
            "experience": [
                "Gavin has extensive work experience including being Founder and Director of BuddyApp Ltd. (2024-present).",
                "He is also a Content Writer for educational institutions such as Cambridge, Trinity College London, and the British Council (2022-present).",
                "Gavin has been actively contributing to open-source projects related to AI.",
                "He has undertaken numerous projects in NLP, ML and Data Science - check out the projects page on this site!"
                "He was Head of English at Shackleton International School (Valencia, 2022-2024)."
                "Gavin has been actively contributing to open-source projects related to AI.",
            ],
            "personality": [
                "Gavin is an avid musician and plays a number of instruments, including guitar, fiddle, concertina, mandolin and banjo.",
                "He has a new puppy called Mica. She's very cute",
                "He also like to do woodwork in his free time."
            ]
        }

        # If category has changed, reset info_index to 0 and save the new category
        if category != last_category:
            info_index = 0
            dispatcher.utter_message(f"Switching to new category '{category}'")

        # Retrieve the relevant information based on the category and index
        if category in info_data and info_index < len(info_data[category]):
            info_text = info_data[category][info_index]
            dispatcher.utter_message(info_text)
            
            # Check if there is more info available in the category
            if info_index + 1 < len(info_data[category]):
                dispatcher.utter_message("Would you like to know more?")
                # Increment list_index only if the user affirms
                return [
                    SlotSet("list_index", info_index),
                    SlotSet("last_category", category),
                    FollowupAction(name="action_listen")  # Wait for user affirmation
                ]
        else:
            dispatcher.utter_message("No more information available in this category.")

        # Increment the index if there's no category change
        return [
            SlotSet("list_index", info_index + 1),
            SlotSet("last_category", category)
        ]
