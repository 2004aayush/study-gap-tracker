import os
from datetime import datetime

file_name = "data.txt"

# add daily study
def add_data():
    hrs = input("Kitne ghante padhe aaj? ")

    if not hrs.isdigit():
        print("enrer number only")
        return

    today_date = datetime.now().strftime("%Y-%m-%d")

    with open(file_name, "a") as f:
        f.write(today_date + "," + hrs + "\n")

    if int(hrs) == 0:
        print("⚠️ No study Today")
    else:
        print("Entry Saved")

# show all entries
def show_data():
    if not os.path.exists(file_name):
        print("No Record")
        return

    with open(file_name, "r") as f:
        lines = f.readlines()

    print("\n--- Study Record ---")
    for line in lines:
        d, h = line.strip().split(",")
        print(d, "->", h, "hrs")

# check study gaps
def find_gap():
    if not os.path.exists(file_name):
        print("Data Not fouond")
        return

    with open(file_name, "r") as f:
        lines = f.readlines()

    date_list = []

    for line in lines:
        d, _ = line.strip().split(",")
        date_obj = datetime.strptime(d, "%Y-%m-%d")
        date_list.append(date_obj)

    date_list.sort()

    gap_flag = False

    for i in range(1, len(date_list)):
        diff = (date_list[i] - date_list[i-1]).days

        if diff > 1:
            print("⚠️ Gap mila:", diff-1, "din ka",
                  "(", date_list[i-1].date(), "to", date_list[i].date(), ")")
            gap_flag = True

    if not gap_flag:
        print("Good Lagatar padh rhe ho")

# weekly total (simple last 7 entries logic)
def weekly_hours():
    if not os.path.exists(file_name):
        print("Data Not Found")
        return

    with open(file_name, "r") as f:
        lines = f.readlines()

    last_7 = lines[-7:]  # last 7 records

    total = 0

    for line in last_7:
        _, h = line.strip().split(",")
        total += int(h)

    print("Last 7 entries ka total study:", total, "hrs")

# best day
def best_day():
    if not os.path.exists(file_name):
        print("Data not found")
        return

    with open(file_name, "r") as f:
        lines = f.readlines()

    max_h = 0
    best_d = ""

    for line in lines:
        d, h = line.strip().split(",")
        if int(h) >= max_h:
            max_h = int(h)
            best_d = d

    if best_d:
        print("Sabse jyada padha:", best_d, "->", max_h, "hrs")

# menu
def start():
    while True:
        print("\n--- Study Tracker ---")
        print("1. Add")
        print("2. Show")
        print("3. Check Gap")
        print("4. Weekly Total")
        print("5. Best Day")
        print("6. Exit")

        ch = input(" Select Choice: ")

        if ch == "1":
            add_data()
        elif ch == "2":
            show_data()
        elif ch == "3":
            find_gap()
        elif ch == "4":
            weekly_hours()
        elif ch == "5":
            best_day()
        elif ch == "6":
            print("Exit the programme")
            break
        else:
            print("Wrong option")

start()