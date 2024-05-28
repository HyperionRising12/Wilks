import tkinter as tk
from tkinter import ttk

# Wilks coefficients for males
MALE_COEFF = [-216.0475144, 16.2606339, -0.002388645, -0.00113732, 7.01863e-6, -1.291e-8]
# Wilks coefficients for females
FEMALE_COEFF = [594.31747775582, -27.23842536447, 0.82112226871, -0.00930733913, 4.731582e-5, -9.054e-8]

def calculate_wilks(bodyweight, total_lifted, is_male):
    # Select the appropriate coefficients based on gender
    coeffs = MALE_COEFF if is_male else FEMALE_COEFF
    a, b, c, d, e, f = coeffs
    wilks_score = total_lifted * 500 / (a + b * bodyweight + c * bodyweight**2 + d * bodyweight**3 + e * bodyweight**4 + f * bodyweight**5)
    return wilks_score

def on_calculate():
    try:
        # Retrieve user inputs
        bodyweight = float(bodyweight_entry.get())
        total_lifted = float(total_lifted_entry.get())
        is_male = gender_var.get() == 'Male'
        
        # Calculate the Wilks Score
        wilks_score = calculate_wilks(bodyweight, total_lifted, is_male)
        result_var.set(f'Wilks Score: {wilks_score:.2f}')
    except ValueError:
        # Handle invalid input
        result_var.set('Please enter valid numbers')

# GUI setup
root = tk.Tk()
root.title('Wilks Calculator')

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and Entries for Bodyweight
ttk.Label(mainframe, text="Bodyweight (kg):").grid(row=1, column=1, sticky=tk.W)
bodyweight_entry = ttk.Entry(mainframe)
bodyweight_entry.grid(row=1, column=2, sticky=(tk.W, tk.E))

# Labels and Entries for Total Lifted Weight
ttk.Label(mainframe, text="Total Lifted (kg):").grid(row=2, column=1, sticky=tk.W)
total_lifted_entry = ttk.Entry(mainframe)
total_lifted_entry.grid(row=2, column=2, sticky=(tk.W, tk.E))

# Gender selection using radio buttons
gender_var = tk.StringVar(value='Male')
ttk.Label(mainframe, text="Gender:").grid(row=3, column=1, sticky=tk.W)
ttk.Radiobutton(mainframe, text='Male', variable=gender_var, value='Male').grid(row=3, column=2, sticky=tk.W)
ttk.Radiobutton(mainframe, text='Female', variable=gender_var, value='Female').grid(row=3, column=2, sticky=tk.E)

# Display the result
result_var = tk.StringVar()
ttk.Label(mainframe, textvariable=result_var).grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E))

# Calculate button
calculate_button = ttk.Button(mainframe, text="Calculate", command=on_calculate)
calculate_button.grid(row=5, column=1, columnspan=2)

# Grid configuration for consistent padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
