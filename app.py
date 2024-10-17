import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reports import report1, report2#, <report3>, ... (placeholders lang to HAHAHA change this when we have queries :D)
from database import connect

def display_report(report_func):
    conn = connect()
    fig = report_func(conn)  
    conn.close()

    # Create window for da report
    report_window = tk.Toplevel()
    report_window.title("Databse Report")

    # Embed the matplotlib figure into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=report_window)
    canvas.draw()
    canvas.get_tk_widget().pack()  # Display the plot

# Tkinter GUI setup
root = tk.Tk()
root.title("Database Reports")

# Button to display report 1
btn1 = tk.Button(root, text="Report 1", 
                                 command=lambda: display_report(report1))
btn1.pack()

# Button to display report 2
btn2 = tk.Button(root, text="Report 2", 
                              command=lambda: display_report(report2))
btn2.pack()

# Button to display report 3
btn3 = tk.Button(root, text="Pogi ni joaqui", 
                              command=lambda: display_report(report2))
btn3.pack()

root.mainloop()  # Start the GUI