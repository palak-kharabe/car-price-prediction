import tkinter as tk

root = tk.Tk()
root.title("Car Price Predictor")
root.geometry("450x550")
root.configure(bg="#f0f4f7")

# Title
title = tk.Label(root, text="Car Price Predictor",
                 font=("Arial", 18, "bold"),
                 bg="#f0f4f7")
title.pack(pady=10)

# Frame
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack()

# Entry fields
def create_field(text):
    label = tk.Label(frame, text=text, bg="#f0f4f7")
    label.pack()
    entry = tk.Entry(frame)
    entry.pack(pady=5)
    return entry

year_entry = create_field("Year")
price_entry = create_field("Present Price")
kms_entry = create_field("Kms Driven")

# Dropdowns
fuel_var = tk.StringVar()
fuel_menu = tk.OptionMenu(frame, fuel_var, "Petrol", "Diesel", "CNG")
fuel_menu.pack(pady=5)

seller_var = tk.StringVar()
seller_menu = tk.OptionMenu(frame, seller_var, "Dealer", "Individual")
seller_menu.pack(pady=5)

trans_var = tk.StringVar()
trans_menu = tk.OptionMenu(frame, trans_var, "Manual", "Automatic")
trans_menu.pack(pady=5)

owner_entry = create_field("Number of Owners")

# Prediction function
def predict_price():
    try:
        fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
        seller_map = {"Dealer": 0, "Individual": 1}
        trans_map = {"Manual": 0, "Automatic": 1}

        data = [
            float(year_entry.get()),
            float(price_entry.get()),
            float(kms_entry.get()),
            fuel_map[fuel_var.get()],
            seller_map[seller_var.get()],
            trans_map[trans_var.get()],
            float(owner_entry.get())
        ]

        prediction = model.predict([data])

        result_label.config(
            text=f"Estimated Price: {round(prediction[0], 2)} lakhs"
        )

    except:
        result_label.config(text="Enter valid data!")

# Button
btn = tk.Button(root, text="Predict Price",
                command=predict_price,
                bg="#4CAF50", fg="white",
                font=("Arial", 12, "bold"))
btn.pack(pady=15)

# Result
result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg="#f0f4f7")
result_label.pack()

root.mainloop()