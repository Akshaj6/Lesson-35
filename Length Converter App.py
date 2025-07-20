import tkinter as tk
from tkinter import ttk # For a slightly more modern look on the widgets

def convert_inches_to_cm():
    """
    Function to get the value from the entry box,
    convert it from inches to centimeters, and display the result.
    """
    try:
        # Get the value from the entry widget (it's a string)
        inches_value_str = inches_entry.get()

        # Convert the string to a floating-point number
        inches_value = float(inches_value_str)

        # Perform the conversion (1 inch = 2.54 cm)
        cm_value = inches_value * 2.54

        # Format the result string to 2 decimal places
        result_string = f"{inches_value} inches is equal to {cm_value:.2f} cm"

        # Update the result label with the new string
        result_label.config(text=result_string)

    except ValueError:
        # Handle the case where the input is not a valid number
        result_label.config(text="Error: Please enter a valid number.")
    except Exception as e:
        # Handle any other unexpected errors
        result_label.config(text=f"An error occurred: {e}")


# --- Create the main window ---
root = tk.Tk()
root.title("Length Converter App")

# Set the window size
window_width = 400
window_height = 200 # 400 height is a bit tall, 200 is more compact
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False) # Optional: prevent window from being resized

# --- Create a style object for modern widgets ---
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12, "bold"))
style.configure("TEntry", font=("Helvetica", 12))

# --- Create a frame to hold the widgets with some padding ---
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)


# --- Create the widgets ---

# 1. Label to instruct the user
input_label = ttk.Label(main_frame, text="Enter length in inches:")
input_label.pack(pady=5) # pady adds vertical space

# 2. Entry widget for user input
inches_entry = ttk.Entry(main_frame, width=20, justify="center")
inches_entry.pack(pady=5)
inches_entry.focus() # Automatically place the cursor in this entry box

# 3. Button to trigger the conversion
# The 'command' option links the button to our conversion function
convert_button = ttk.Button(main_frame, text="Convert", command=convert_inches_to_cm)
convert_button.pack(pady=10)

# 4. Label to display the result
result_label = ttk.Label(main_frame, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=5)


# --- Start the main event loop ---
# This keeps the window open and responsive to user actions
root.mainloop()