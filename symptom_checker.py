import tkinter as tk
from tkinter import messagebox

# Your hardcoded data
disease_database = {
    "Common Cold": ["Runny nose", "Sneezing", "Sore throat", "Cough", "Congestion"],
    "Flu": ["Fever", "Body aches", "Fatigue", "Headache", "Chills"],
    "Allergies": ["Itchy eyes", "Sneezing", "Runny nose", "Congestion", "Itchy throat"],
    "Migraine": ["Severe headache", "Nausea", "Light sensitivity", "Vision changes", "Fatigue"],
    "Food Poisoning": ["Nausea", "Vomiting", "Diarrhea", "Stomach cramps", "Fever"],
}
#Flattens all symptoms into a set to remove duplicates, then sorts them alphabetically.
common_symptoms = sorted({symptom for symptoms in disease_database.values() for symptom in symptoms})
#Starts the GUI symptom checker logic.
def symptom_checker():
    #Inner function that is called when the "Check Symptoms" button is clicked.
    def submit():
        name = name_entry.get()
        gender = gender_var.get()
        age = age_entry.get()
       #Loops through all checkboxes. If the checkbox is selected (.get() is True), it adds the symptom.
        selected_symptoms = [symptom for symptom in symptom_vars if symptom_vars[symptom].get()]
       #Basic validation. If any required field is missing, show an error.
        if not name or not age or not selected_symptoms:
            messagebox.showerror("Input Error", "Please fill all fields and select at least one symptom.")
            return

        # Basic matching
        max_match = 0
        likely_disease = "Unable to determine"
        for disease, symptoms in disease_database.items():
            matches = len(set(symptoms) & set(selected_symptoms))
            if matches > max_match:
                max_match = matches
                likely_disease = disease
       #Shows the result in a message box.
        result_text = f"Hello, {name}!\nLikely disease: {likely_disease}\nSymptoms matched: {', '.join(selected_symptoms)}"
        messagebox.showinfo("Diagnosis Result", result_text)

    # GUI setup/Creates the window and sets the title.
    root = tk.Tk()
    root.title("Symptom Checker")
   #Label and text field for name.
    tk.Label(root, text="Name").grid(row=0, column=0, sticky='e')
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)
   #buttons for gender selection.
    tk.Label(root, text="Gender").grid(row=1, column=0, sticky='e')
    gender_var = tk.StringVar(value='male')
    tk.Radiobutton(root, text='Male', variable=gender_var, value='male').grid(row=1, column=1, sticky='w')
    tk.Radiobutton(root, text='Female', variable=gender_var, value='female').grid(row=1, column=2, sticky='w')
    #Age input field.
    tk.Label(root, text="Age").grid(row=2, column=0, sticky='e')
    age_entry = tk.Entry(root)
    age_entry.grid(row=2, column=1)
   #A frame to contain all symptom checkboxes.
    tk.Label(root, text="Symptoms").grid(row=3, column=0, sticky='ne')
    symptom_vars = {}
    symptom_frame = tk.Frame(root)
    symptom_frame.grid(row=3, column=1, columnspan=2, sticky='w')

    #generates checkboxes in a grid layout.
    for i, symptom in enumerate(common_symptoms):
        var = tk.BooleanVar()
        symptom_vars[symptom] = var
        tk.Checkbutton(symptom_frame, text=symptom, variable=var).grid(row=i // 3, column=i % 3, sticky='w')
    #Adds a button that triggers the submit() function.
    tk.Button(root, text='Check Symptoms', command=submit).grid(row=4 + len(common_symptoms) // 3, column=1)
    #Starts the event loop — the GUI will stay open and responsive.
    root.mainloop()
#Calls the function to start the app.
symptom_checker()