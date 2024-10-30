from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import List, Dict, Any

class ActionGiveInfo(Action):

    def name(self) -> str:
        return "action_give_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List:

        # Retrieve the current category and index from the slots
        category = tracker.get_slot("category")
        info_index = tracker.get_slot("list_index") or 0

        # Log category for debugging
        #print(f"Category: {category}")  # Add this line for debugging

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
                "He has undertaken numerous projects in NLP, ML, and Data Science - check out the projects page on this site!",
                "He was Head of English at Shackleton International School (Valencia, 2022-2024)."
            ],
            "personality": [
                "Gavin is an avid musician and plays a number of instruments, including guitar, fiddle, concertina, mandolin and banjo.",
                "He has a new puppy called Mica. She's very cute",
                "He also like to do woodwork in his free time."
            ]
        }

        # Ensure category is correctly set, or default to "skills" if none
        if category not in info_data:
            dispatcher.utter_message(text="I didn't understand the category. Please ask about 'skills', 'qualifications', 'experience' or 'personality'.")
            return []

        # Determine which list to use based on the category
        info_list = info_data.get(category, [])

        # Check if we have exhausted the information
        if info_index >= len(info_list):
            dispatcher.utter_message("I'm bored, ask me something else!")
            return [SlotSet("list_index", 0), SlotSet("category", None)]  # Reset slots

        # Provide the current piece of information
        dispatcher.utter_message(text=info_list[info_index])
        
        # Increment the index for the next round
        info_index += 1

        # Prompt the user to continue
        dispatcher.utter_message(text=f"Would you like to hear more about Gavin's {category}?")

        # Update the slot with the new index
        return [SlotSet("list_index", info_index)]