# Time frames
# 0000-800, 800-1200, 1200-1700, 1700 - 0000
first_Shift = range(0, 700, 100)
second_Shift = range(700, 1200, 100)
third_Shift = range(1200, 1700, 100)
fourth_Shift = range(1700, 2400, 100)

def regular_shift(start, stop):
    earlyMorning = 0
    morning = 0
    afternoon = 0
    evening = 0
    if start_Time < end_Time:
        for i in range(start, stop):
            if i in first_Shift:
                earlyMorning += 1
            if i in second_Shift:
                morning += 1
            if i in third_Shift:
                afternoon += 1
            if i in fourth_Shift:
                evening += 1
    # Do math for the wages
    total_wage = (earlyMorning * shiftList[0]["rate"]) + (
        morning * shiftList[1]["rate"] + (afternoon * shiftList[2]["rate"]) + (evening * shiftList[3]["rate"]))
    total_hours = earlyMorning + morning + afternoon + evening
    print(f"{earlyMorning}, {morning}, {afternoon}, {evening}")
    print(f"You worked a total of {total_hours} hours and your total charge comes to ${total_wage:.2f}")

def overnight_long(shiftList):
    earlyMorning = 0
    morning = 0
    afternoon = 0
    evening = 0

    if start_Time not in first_Shift and end_Time in first_Shift:
        print(f"{start_Time} > {end_Time} and not in same Range")
    elif start_Time > end_Time:
        if start_Time < first_Shift[-1] and end_Time in first_Shift:
            earlyMorning = (((first_Shift[-1] - start_Time) + end_Time) / 100) + ((shiftList[1]["morningShift"] +
                                                                                   shiftList[2]["afternoonShift"] +
                                                                                   shiftList[3]["eveningShift"]) / 100)
        elif second_Shift[0] < start_Time < second_Shift[-1] and end_Time in second_Shift:
            morning = (((second_Shift[-1] - start_Time) + (end_Time - second_Shift[0])) / 100) + ((shiftList[0][
                                                                                                       "earlyMorningShift"] +
                                                                                                   shiftList[2][
                                                                                                       "afternoonShift"] +
                                                                                                   shiftList[3][
                                                                                                       "eveningShift"]) / 100)
        elif third_Shift[0] < start_Time < third_Shift[-1] and end_Time in third_Shift:
            afternoon = (((third_Shift[-1] - start_Time) + (end_Time - third_Shift[0])) / 100) + ((shiftList[0][
                                                                                                       "earlyMorningShift"] +
                                                                                                   shiftList[1][
                                                                                                       "morningShift"] +
                                                                                                   shiftList[3][
                                                                                                       "eveningShift"]) / 100)
        elif fourth_Shift[0] < start_Time < fourth_Shift[-1] and end_Time in fourth_Shift:
            evening = (((fourth_Shift[-1] - start_Time) + (end_Time - fourth_Shift[0])) / 100) + ((shiftList[0][
                                                                                                       "earlyMorningShift"] +
                                                                                                   shiftList[1][
                                                                                                       "morningShift"] +
                                                                                                   shiftList[2][
                                                                                                       "afternoonShift"]) / 100)
    elif start_Time < end_Time:
        print(f"{start_Time} < {end_Time}")

    total_wage = earlyMorning + morning + afternoon + evening
    print(f"Your total charge comes to ${total_wage:.2f}")

def loop_shifts(start_time, end_time):
    current_time = start_time
    earlyMorning = 0
    morning = 0
    afternoon = 0
    evening = 0
    while current_time != end_time:
        if current_time in first_Shift:
            earlyMorning += 1
        elif current_time in second_Shift:
            morning += 1
        elif current_time in third_Shift:
            afternoon += 1
        elif current_time in fourth_Shift:
            evening += 1
        current_time = (current_time + 100) % 2400
    # print(earlyMorning, morning, afternoon, evening)
    # return earlyMorning, morning, afternoon, evening
    # Do math for the wages
    total_wage = (earlyMorning * shiftList[0]["rate"]) + (
        morning * shiftList[1]["rate"] + (afternoon * shiftList[2]["rate"]) + (evening * shiftList[3]["rate"]))
    total_hours = earlyMorning + morning + afternoon + evening
    print(f"{earlyMorning}, {morning}, {afternoon}, {evening}")
    print(f"You worked a total of {total_hours} hours and your total charge comes to ${total_wage:.2f}")

begin = None
while True:
    # Adding rate for time frames
    shift1_Rate = int(input("Please enter a rate for First Shift (0000 - 0800) \n"))
    shift2_Rate = int(input("Please enter a rate for Second Shift (0800 - 1200) \n"))
    shift3_Rate = int(input("Please enter a rate for Third Shift (1200 - 1700) \n"))
    shift4_Rate = int(input("Please enter a rate for Fourth Shift (1700 - 0000) \n"))

    # Selecting start and stop times
    work_Shift = [int(t) for t in input("Please enter a Start Time and End Time (24hr format):\n").split()]
    start_Time = work_Shift[0]
    end_Time = work_Shift[1]

    # master dict of shift stuff
    shiftList = [
        {"start": 0, "end": 800, "earlyMorningShift": (first_Shift[-1] - first_Shift[0]) * shift1_Rate,
         "rate": shift1_Rate},
        {"start": 800, "end": 1200, "morningShift": (second_Shift[-1] - second_Shift[0]) * shift2_Rate,
         "rate": shift2_Rate},
        {"start": 1200, "end": 1700, "afternoonShift": (third_Shift[-1] - third_Shift[0]) * shift3_Rate,
         "rate": shift3_Rate},
        {"start": 1700, "end": 2400, "eveningShift": (fourth_Shift[-1] - fourth_Shift[0]) * shift4_Rate,
         "rate": shift4_Rate}
    ]
    # function start
    if start_Time > end_Time:
        loop_shifts(start_Time, end_Time)
    else:
        regular_shift(start_Time, end_Time)

    # Begin the Loop
    begin = input("Please enter '1' to calculate wages or press '0' to Exit ")
    if begin != "0":
        begin = None
    else:
        print("Thank you, goodbye.")
        break