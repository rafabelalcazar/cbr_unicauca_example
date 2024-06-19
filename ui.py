import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Hygeia: Cleaning Datasets in Knowledge Discovery Tasks")

# Define the frames
top_frame = tk.Frame(root)
top_frame.pack(side=[tk.TOP], fill=tk.X)

mid_frame = tk.Frame(root)
mid_frame.pack(side=tk.TOP, fill=tk.X)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.TOP, fill=tk.X)

# Top Frame Elements
task_label = tk.Label(top_frame, text="Knowledge discovery tasks")
task_label.pack(side=tk.TOP, padx=10, pady=10)

classification_task = tk.Radiobutton(top_frame, text="Classification task")
classification_task.pack(side=tk.LEFT, padx=5)

regression_task = tk.Radiobutton(top_frame, text="Regression task")
regression_task.pack(side=tk.LEFT, padx=5)

# Middle Frame Elements
dataset_info_frame = tk.Frame(mid_frame, borderwidth=2, relief=tk.SUNKEN)
dataset_info_frame.pack(side=tk.LEFT, padx=10, pady=10)

dataset_label = tk.Label(dataset_info_frame, text="Dataset information")
dataset_label.pack(anchor='w', padx=5, pady=5)

instances_label = tk.Label(dataset_info_frame, text="Instances: 45211")
instances_label.pack(anchor='w', padx=5)

attributes_label = tk.Label(dataset_info_frame, text="Attributes: 16")
attributes_label.pack(anchor='w', padx=5)

missing_label = tk.Label(dataset_info_frame, text="Missing values: 0.0%")
missing_label.pack(anchor='w', padx=5)

duplicate_label = tk.Label(dataset_info_frame, text="Duplicate instances: 0.0%")
duplicate_label.pack(anchor='w', padx=5)

attributes_frame = tk.Frame(mid_frame, borderwidth=2, relief=tk.SUNKEN)
attributes_frame.pack(side=tk.LEFT, padx=10, pady=10)

attributes_label = tk.Label(attributes_frame, text="Attributes")
attributes_label.pack(anchor='w', padx=5, pady=5)

attributes_listbox = tk.Listbox(attributes_frame, height=10)
attributes_listbox.pack(padx=5, pady=5)

attributes = [
    "housing", "loan", "contact", "day", "month", "duration", 
    "campaign", "pdays", "previous", "poutcome", "y"
]

for attribute in attributes:
    attributes_listbox.insert(tk.END, attribute)

buttons_frame = tk.Frame(mid_frame)
buttons_frame.pack(side=tk.LEFT, padx=10, pady=10)

open_button = tk.Button(buttons_frame, text="Open data set")
open_button.pack(pady=5)

start_button = tk.Button(buttons_frame, text="Start cleaning")
start_button.pack(pady=5)

attribute_info_frame = tk.Frame(mid_frame, borderwidth=2, relief=tk.SUNKEN)
attribute_info_frame.pack(side=tk.LEFT, padx=10, pady=10)

attribute_info_label = tk.Label(attribute_info_frame, text="Attribute information")
attribute_info_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

measure_label = tk.Label(attribute_info_frame, text="Measure")
measure_label.grid(row=1, column=0, padx=5)

value_label = tk.Label(attribute_info_frame, text="Value")
value_label.grid(row=1, column=1, padx=5)

measures = [
    "Maximum", "Minimum", "1st Quartile", "3rd Quartile", "Mean",
    "Median", "Standard deviation", "Skewness", "Kurtosis", 
    "Candidate outliers", "Missing values"
]

values = [
    "4,918", "0", "103", "319", "258.163", "180", "257.528",
    "3.144", "21.152", "0.072", "0"
]

for i, measure in enumerate(measures):
    tk.Label(attribute_info_frame, text=measure).grid(row=i+2, column=0, padx=5)
    tk.Label(attribute_info_frame, text=values[i]).grid(row=i+2, column=1, padx=5)

# Bottom Frame Elements
charts_frame = tk.Frame(bottom_frame, borderwidth=2, relief=tk.SUNKEN)
charts_frame.pack(side=tk.LEFT, padx=10, pady=10)

charts_label = tk.Label(charts_frame, text="Charts")
charts_label.pack(anchor='w', padx=5, pady=5)

attribute_button = tk.Button(charts_frame, text="Attribute")
attribute_button.pack(pady=5)

histogram_button = tk.Button(charts_frame, text="Histogram")
histogram_button.pack(pady=5)

box_plot_button = tk.Button(charts_frame, text="Box plot")
box_plot_button.pack(pady=5)

bar_button = tk.Button(charts_frame, text="Bar")
bar_button.pack(pady=5)

# Run the application
root.mainloop()
