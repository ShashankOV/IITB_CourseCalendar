"""
ColorIDs for Events
---------------------
    Id    Name     Hex
    1 : Lavender  #a4bdfc (LIGHT VIOLET)
    2 : Sage      #7ae7bf (LIGHT GREEN)
    3 : Grape     #dbadff (VIOLET)
    4 : Flamingo  #ff887c (PINK)
    5 : Banana    #fbd75b (YELLOW)
    6 : Tangerine #ffb878 (ORANGE)
    7 : Peacock   #46d6db (LIGHT BLUE)
    8 : Graphite  #e1e1e1 (GREY)
    9 : Blueberry #5484ed (INDIGO)
    10: Basil     #51b749 (GREEN)
    11: Tomato    #dc2127 (RED)
"""
DAYS = {
    'MO' : 0,
    'TU' : 1,
    'WE' : 2,
    'TH' : 3,
    'FR' : 4,
    'SA' : 5,
    'SU' : 6
}

SLOT_DATA = {
    '1' : [{'day' : [0], 'start' : '08:30:00.000', 'end' : '09:25:00.000', 'color' : '10', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=MO'}, {'day' : [1], 'start' : '09:30:00.000', 'end' : '10:25:00.000', 'color' : '10', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TU'}, {'day' : [3], 'start' : '10:35:00.000', 'end' : '11:30:00.000', 'color' : '10', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TH'}],
    '2' : [{'day' : [0], 'start' : '09:30:00.000', 'end' : '10:25:00.000', 'color' : '9', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=MO'}, {'day' : [1], 'start' : '10:35:00.000', 'end' : '11:30:00.000', 'color' : '9', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TU'}, {'day' : [3], 'start' : '11:35:00.000', 'end' : '12:30:00.000', 'color' : '9' , 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TH'}],
    '3' : [{'day' : [0], 'start' : '10:35:00.000', 'end' : '11:30:00.000', 'color' : '6', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=MO'}, {'day' : [1], 'start' : '11:35:00.000', 'end' : '12:30:00.000', 'color' : '6', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TU'}, {'day' : [3], 'start' : '08:30:00.000', 'end' : '09:25:00.000', 'color' : '6' , 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TH'}],
    '4' : [{'day' : [0], 'start' : '11:35:00.000', 'end' : '12:30:00.000', 'color' : '3', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=MO'}, {'day' : [1], 'start' : '08:30:00.000', 'end' : '09:25:00.000', 'color' : '3', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TU'}, {'day' : [3], 'start' : '09:30:00.000', 'end' : '10:25:00.000', 'color' : '3', 'recurrence': 'RRULE:FREQ=WEEKLY;BYDAY=TH'}],
    '5' : [{'day' : [2, 4], 'start' : '09:30:00.000', 'end' : '10:55:00.000', 'color' : '1', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE,FR'}],
    '6' : [{'day' : [2, 4], 'start' : '11:05:00.000', 'end' : '12:30:00.000', 'color' : '2', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE,FR'}],
    '7' : [{'day' : [2, 4], 'start' : '08:30:00.000', 'end' : '09:25:00.000', 'color' : '4', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE,FR'}],
    '8' : [{'day' : [0, 3], 'start' : '14:00:00.000', 'end' : '15:25:00.000', 'color' : '5', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=MO,TH'}],
    '9' : [{'day' : [0, 3], 'start' : '15:35:00.000', 'end' : '17:00:00.000', 'color' : '1', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=MO,TH'}],
    '10' : [{'day' : [1, 4], 'start' : '14:00:00.000', 'end' : '15:25:00.000', 'color' : '2', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=TU,FR'}],
    '11' : [{'day' : [1, 4], 'start' : '15:35:00.000', 'end' : '17:00:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=TU,FR'}],
    '12' : [{'day' : [0, 3], 'start' : '17:30:00.000', 'end' : '18:55:00.000', 'color' : '2', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=MO,TH'}],
    '13' : [{'day' : [0, 3], 'start' : '19:00:00.000', 'end' : '20:25:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=MO,TH'}],
    '14' : [{'day' : [1, 4], 'start' : '17:30:00.000', 'end' : '18:55:00.000', 'color' : '4', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=TU,FR'}],
    '15' : [{'day' : [1, 4], 'start' : '19:00:00.000', 'end' : '20:25:00.000', 'color' : '5', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=TU,FR'}],
    'L1' : [{'day' : [0], 'start' : '14:00:00.000', 'end' : '16:55:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=MO'}],
    'L2' : [{'day' : [1], 'start' : '14:00:00.000', 'end' : '16:55:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=TU'}],
    'L3' : [{'day' : [3], 'start' : '14:00:00.000', 'end' : '16:55:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=TH'}],
    'L4' : [{'day' : [4], 'start' : '14:00:00.000', 'end' : '16:55:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=FR'}],
    'L5' : [{'day' : [2], 'start' : '09:30:00.000', 'end' : '12:30:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'L6' : [{'day' : [4], 'start' : '09:30:00.000', 'end' : '12:30:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=FR'}],
    'LX' : [{'day' : [2], 'start' : '09:30:00.000', 'end' : '12:30:00.000', 'color' : '7', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'X1' : [{'day' : [2], 'start' : '14:00:00.000', 'end' : '14:55:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'X2' : [{'day' : [2], 'start' : '15:00:00.000', 'end' : '15:55:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'X3' : [{'day' : [2], 'start' : '16:00:00.000', 'end' : '16:55:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'XA' : [{'day' : [2], 'start' : '14:00:00.000', 'end' : '15:25:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'XB' : [{'day' : [2], 'start' : '15:35:00.000', 'end' : '17:00:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'XC' : [{'day' : [2], 'start' : '17:30:00.000', 'end' : '18:55:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}],
    'XD' : [{'day' : [2], 'start' : '19:00:00.000', 'end' : '20:25:00.000', 'color' : '8', 'recurrence' : 'RRULE:FREQ=WEEKLY;BYDAY=WE'}]
}
