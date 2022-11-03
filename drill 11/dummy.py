table = {
    "SLEEP" : {"HIT" : "WAKE"},
    "WAKE" : {"TIMER1", "SLEEP"}
}

cur_state = "SLEEP"
next_state = table[cur_state]["HIT"]