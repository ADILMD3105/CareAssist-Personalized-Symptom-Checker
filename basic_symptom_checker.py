# Disease detection database/ database — a dictionary mapping each disease to a list of common symptoms.
disease_database = {
    "Common Cold": ["Runny nose", "Sneezing", "Sore throat", "Cough", "Congestion"],
    "Flu": ["Fever", "Body aches", "Fatigue", "Headache", "Chills"],
    "Allergies": ["Itchy eyes", "Sneezing", "Runny nose", "Congestion", "Itchy throat"],
    "Migraine": ["Severe headache", "Nausea", "Light sensitivity", "Vision changes", "Fatigue"],
    "Food Poisoning": ["Nausea", "Vomiting", "Diarrhea", "Stomach cramps", "Fever"],
}

# Common symptoms list/A flat list of all symptoms used for displaying numbered options to users.
common_symptoms = [
    "Fever", "Headache", "Fatigue", "Body aches", "Cough",
    "Runny nose", "Sore throat", "Congestion", "Sneezing",
    "Nausea", "Vomiting", "Diarrhea", "Stomach cramps",
    "Itchy eyes", "Light sensitivity", "Vision changes",
    "Chills", "Itchy throat"
]
#Displays all symptoms with a number for the user to choose from.
def display_symptoms():
    print("Select your symptoms by entering the corresponding numbers (comma-separated):")
    for i, symptom in enumerate(common_symptoms, start=1):
        print(f"{i}. {symptom}")
#Asks the user to input numbers like 1,3,5.
def get_selected_symptoms():
    display_symptoms()
    selected_indices = input("Enter the numbers of your symptoms: ")
    selected_indices = selected_indices.split(',')
    #Filters out invalid inputs (non-digit or out-of-range).
    selected_symptoms = [
        common_symptoms[int(index) - 1]
        for index in selected_indices
        if index.strip().isdigit() and 0 < int(index) <= len(common_symptoms)
    ]
    #Returns the list of user-selected symptoms.
    return selected_symptoms
#Starts with no matching disease.
def detect_disease(selected_symptoms):
    max_match = 0
    likely_disease = "Unable to determine"

    # Simple matching algorithm/Converts symptoms to sets and finds the intersection (common symptoms).
    for disease, symptoms in disease_database.items():
        matches = len(set(symptoms) & set(selected_symptoms))
        if matches > max_match:
            max_match = matches
            likely_disease = disease
#Returns the most likely disease.
    return likely_disease

def main():
    print("Welcome to the Symptom Checker")
    print("This is a basic symptom checker for educational purposes only.")
    print("It is not a substitute for professional medical advice, diagnosis, or treatment.")
    
    selected_symptoms = get_selected_symptoms()
    
    if selected_symptoms:
        diagnosis = detect_disease(selected_symptoms)
        print(f"\nBased on your selected symptoms, you may have: {diagnosis}")
    else:
        print("No symptoms selected. Please try again.")

if __name__ == "__main__":
    main()
