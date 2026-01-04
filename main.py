import gradio as gr
import subprocess

# Define the base file path for Python scripts
file_path = 'c:/Users/mayank.c/OneDrive - Optimus Information Inc/Desktop/Chatbot_Project/Chatbot/PythonFiles/'

# Define functions to call each file
def run_getting_medicine_details(user_input):
    try:
        result = subprocess.run(
            ["python", f"{file_path}Getting_Medicine_Details.py", user_input],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout  # Return the output from the script
    except subprocess.CalledProcessError as e:
        return f"Error executing Getting_Medicine_Details.py: {e.stderr}"

def run_medicine_related_details(user_input):
    try:
        result = subprocess.run(
            ["python", f"{file_path}Medicine_Related_Details.py", user_input],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout  # Return the output from the script
    except subprocess.CalledProcessError as e:
        return f"Error executing Medicine_Related_Details.py: {e.stderr}"

def run_medical_report_analysis(file):
    try:
        result = subprocess.run(
            ["python", f"{file_path}MedicalReportAnalysis.py", file.name],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout  # Return the output from the script
    except subprocess.CalledProcessError as e:
        # Capture both stdout and stderr for debugging
        error_message = f"Error executing MedicalReportAnalysis.py: {e.stderr}"
        print(f"Error stdout: {e.stdout}")
        print(f"Error stderr: {e.stderr}")
        return error_message

def run_side_effects_of_medicine(user_input):
    try:
        result = subprocess.run(
            ["python", f"{file_path}SideEffectsOfMedicine.py", user_input],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout  # Return the output from the script
    except subprocess.CalledProcessError as e:
        return f"Error executing SideEffectsOfMedicine.py: {e.stderr}"

def run_symptom_diagnosis(user_input):
    try:
        result = subprocess.run(
            ["python", f"{file_path}SymptomDiagnosis.py", user_input],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout  # Return the output from the script
    except subprocess.CalledProcessError as e:
        return f"Error executing SymptomDiagnosis.py: {e.stderr}"

# Main function to handle user input
def handle_user_choice(choice, user_input=None, file=None):
    if choice == "Get Medicine Details":
        return run_getting_medicine_details(user_input)
    elif choice == "Medical Related Questions like (What is Blood Pressure?)":
        return run_medicine_related_details(user_input)
    elif choice == "Analyze Medical Report":
        if file is None:
            return "Please upload a document to analyze."
        return run_medical_report_analysis(file)
    elif choice == "Check Side Effects of Medicine":
        return run_side_effects_of_medicine(user_input)
    elif choice == "Diagnose Symptoms":
        return run_symptom_diagnosis(user_input)
    else:
        return "Invalid choice. Please select a valid option."

# Gradio interface
def dynamic_inputs(choice):
    """
    Dynamically show inputs based on the selected option.
    """
    if choice == "Analyze Medical Report":
        return gr.update(visible=False), gr.update(visible=True)
    else:
        return gr.update(visible=True), gr.update(visible=False)

description = """
# Welcome to the Health Chatbot! 🤖
This chatbot helps you with the following tasks:
1. **Get Medicine Details**: Search for medicines, sideEffects and their details.
2. **Medicine Related Questions**: Get additional information about your question.
3. **Analyze Medical Report**: Upload a medical report for analysis.
4. **Check Side Effects of Medicine**: Find side effects of medicines.
5. **Diagnose Symptoms**: Diagnose health conditions based on symptoms.
"""

with gr.Blocks() as interface:
    with gr.Row():
        gr.Markdown(description)
    with gr.Row():
        choice = gr.Dropdown(
            choices=[
                "Get Medicine Details",
                "Medical Related Questions like (What is Blood Pressure?)",
                "Analyze Medical Report",
                "Check Side Effects of Medicine",
                "Diagnose Symptoms"
            ],
            label="Select an option",
            interactive=True
        )
    with gr.Row():
        user_input = gr.Textbox(label="Enter your input", visible=True, placeholder="Type here...")
        file_input = gr.File(label="Upload a document (for Medical Report Analysis)", visible=False)
    with gr.Row():
        submit = gr.Button("Submit", elem_id="submit-button")
    with gr.Row():
        output = gr.Textbox(label="Result", interactive=False)

    # Update inputs dynamically based on the selected option
    choice.change(dynamic_inputs, inputs=[choice], outputs=[user_input, file_input])

    # Handle user input and file upload
    submit.click(
        handle_user_choice,
        inputs=[choice, user_input, file_input],
        outputs=output
    )

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch()



#################################################################################################################################


import gradio as gr
import subprocess
file_path = 'c:/Users/mayank.c/OneDrive - Optimus Information Inc/Desktop/Chatbot_Project/Chatbot/PythonFiles/'
def run_getting_medicine_details(user_input):
    return _run_script("Getting_Medicine_Details.py", user_input)
def run_medicine_related_details(user_input):
    return _run_script("Medicine_Related_Details.py", user_input)
def run_side_effects_of_medicine(user_input):
    return _run_script("SideEffectsOfMedicine.py", user_input)
def run_symptom_diagnosis(user_input):
    return _run_script("SymptomDiagnosis.py", user_input)
def run_medical_report_analysis(file):
    return _run_script("MedicalReportAnalysis.py", file.name)
def run_brain_tumor_detection(file):
    return _run_script_abs("C:/Users/mayank.c/OneDrive - Optimus Information Inc/Desktop/Chatbot_Project/Early-Cancer-Prediction/Notebooks/brain_tumor_predict.py", file.name)
def run_oral_cancer_detection(file):
    return _run_script_abs("C:/Users/mayank.c/OneDrive - Optimus In formation Inc/Desktop/Chatbot_Project/Early-Cancer-Prediction/Notebooks/oral_cancer_predict.py", file.name)
def _run_script(script_name, input_arg):
    try:
        result = subprocess.run(
            ["python", f"{file_path}{script_name}", input_arg],           
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running {script_name}: {e.stderr}"
def _run_script_abs(script_path, input_arg):
    try:
        result = subprocess.run(
            ["python", script_path, input_arg],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running {script_path}: {e.stderr}"
def handle_user_choice(task, user_input=None, file=None):
    if task == "Get Medicine Details":
        return run_getting_medicine_details(user_input)
    elif task == "Medical Info":
        return run_medicine_related_details(user_input)
    elif task == "Side Effects":
        return run_side_effects_of_medicine(user_input)
    elif task == "Symptom Diagnosis":
        return run_symptom_diagnosis(user_input)
    elif task == "Analyze Medical Report":
        if not file:
            return "⚠️ Please upload a medical report file."
        return run_medical_report_analysis(file)
    elif task == "Brain Tumor":
        if not file:
            return "⚠️ Please upload a brain MRI image."
        return run_brain_tumor_detection(file)
    elif task == "Oral Cancer":
        if not file:
            return "⚠️ Please upload an oral scan image."
        return run_oral_cancer_detection(file)
    else:
        return "❌ Invalid task selected."
TASK_DESCRIPTIONS = {
    "Get Medicine Details": "🔎 Enter a medicine name to get its details, uses, and dosage information.",
    "Medical Info": "📘 Ask any general medical question (e.g., 'What is blood pressure?').",
    "Side Effects": "⚠️ Enter a medicine name to check its possible side effects.",
    "Symptom Diagnosis": "🤒 Describe your symptoms to get a possible diagnosis suggestion.",
    "Analyze Medical Report": "📄 Upload a medical report (PDF or image) to get an AI-powered analysis.",
    "Brain Tumor": "🧠 Upload a brain MRI image to detect the presence and type of brain tumor.",
    "Oral Cancer": " Upload an oral scan image to detect signs of oral cancer."
}
with gr.Blocks() as interface:
    gr.Markdown("## 🩺 AI Health Assistant Chatbot")
    selected_task = gr.State("")
    with gr.Row():
        with gr.Column(scale=2):
            buttons = {
                "💊 Get Medicine Details": "Get Medicine Details",
                "📘 Medical Info": "Medical Info",
                "⚠️ Side Effects": "Side Effects",
                "🤒 Symptom Diagnosis": "Symptom Diagnosis",
                "📄 Analyze Medical Report": "Analyze Medical Report",
                "🧠 Brain Tumor": "Brain Tumor",
                " Oral Cancer": "Oral Cancer"
            }
            button_components = {}
            for label, task in buttons.items():
                button_components[task] = gr.Button(label)
        with gr.Column(scale=3):
            task_description = gr.Textbox(label="Task Description", lines=4, interactive=False)
    with gr.Row():
        user_input = gr.Textbox(label="Enter your query", visible=True, placeholder="Type your input here...")
        file_input = gr.File(label="Upload file", file_types=[".png", ".jpg", ".jpeg", ".pdf"], visible=False)
    with gr.Row():
        submit = gr.Button("Run Task")
    output = gr.Textbox(label="Result", lines=12, interactive=False)
    def show_inputs(task):
        is_file_task = task in ["Analyze Medical Report", "Brain Tumor", "Oral Cancer"]
        return (
            gr.update(visible=not is_file_task),
            gr.update(visible=is_file_task),
            task,
            gr.update(value=TASK_DESCRIPTIONS[task])
        )
    for task, btn in button_components.items():
        btn.click(
            fn=lambda t=task: show_inputs(t),
            outputs=[user_input, file_input, selected_task, task_description]
        )
    submit.click(
        fn=handle_user_choice,
        inputs=[selected_task, user_input, file_input],
        outputs=output
    )
if __name__ == "__main__":
    interface.launch()
