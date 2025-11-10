import tkinter as tk
from backend import get_four_day_weather

def create_column_widgets(column, date_text, weather_text, weather_emoji, temperature, air_quality):
    date_label = tk.Label(column, text=date_text, font=("Helvetica", 18), bg=column.cget("bg")) # so it has the same bg as the column
    weather_emoji_label= tk.Label(column, text=weather_emoji, font=("Helvetica", 40), bg=column.cget("bg"))
    weather_label= tk.Label(column, text=weather_text, wraplength=180, justify=tk.LEFT,font=("Helvetica", 16),  bg=column.cget("bg"))
    temperature_label = tk.Label(column, text=temperature, font=("Helvetica", 18), bg=column.cget("bg"))
    air_quality_label = tk.Label(column, text=air_quality, wraplength=180, justify=tk.LEFT,bg=column.cget("bg"))
    
    date_label.pack(side=tk.TOP, expand=True, pady=10)
    weather_emoji_label.pack(side=tk.TOP, expand=True, pady=10)
    weather_label.pack(side=tk.TOP, expand=True, pady=10)
    temperature_label.pack(side=tk.TOP, expand=True, pady=10)
    air_quality_label.pack(side=tk.TOP, expand=True, pady=10)

def main():
    window = tk.Tk()
    window.title("COSC 117 Weather Forecast")
    window.geometry("1000x400")

    # Create a frame to hold all the columns
    column_container = tk.Frame(window)
    column_container.pack(fill=tk.BOTH, expand=True)

    # Create the four column frames
    yesterday_frame = tk.Frame(column_container, borderwidth=1, relief="sunken")
    today_frame = tk.Frame(column_container, bg="lightgrey", borderwidth=1, relief="sunken")
    tomorrow_frame = tk.Frame(column_container, borderwidth=1, relief="sunken")
    day_after_tomorrow_frame = tk.Frame(column_container, borderwidth=1, relief="sunken")

    # Pack the columns side-by-side
    yesterday_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    today_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tomorrow_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    day_after_tomorrow_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # create_column_widgets(yesterday_frame, "2025-11-01", "Rainy", "🌧", "-2.0 C", "")
    # create_column_widgets(today_frame, "2025-11-01", "Rainy", "🌧", "-2.0 C", "Good")
    # create_column_widgets(tomorrow_frame, "2025-11-01", "Rainy", "🌧", "-2.0 C", "")
    # create_column_widgets(day_after_tomorrow_frame, "2025-11-01", "Rainy", "🌧", "-2.0 C", "")

    data = get_four_day_weather()
    create_column_widgets(yesterday_frame, data[0][0] ,data[0][1], data[0][2], data[0][3],"")
    create_column_widgets(today_frame, data[1][0] ,data[1][1], data[1][2], data[1][3], data[1][4])
    create_column_widgets(tomorrow_frame, data[2][0] ,data[2][1], data[2][2], data[2][3], "")
    create_column_widgets(day_after_tomorrow_frame, data[3][0] ,data[3][1], data[3][2], data[3][3], "")


    window.mainloop()    


if __name__ == "__main__":
    main()