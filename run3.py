import papermill as pm

# Define the function that executes the notebook
def run_notebook():
    notebook_input_path = r"C:\Users\Sangharsh\Desktop\git\Real-Time-Match-Result-Prediction\run1.ipynb"
    notebook_output_path = r"C:\Users\Sangharsh\Desktop\git\Real-Time-Match-Result-Prediction\output.ipynb"
    
    pm.execute_notebook(notebook_input_path, notebook_output_path)
    print("The notebook run1 was executed")

# Run the notebook
run_notebook()
