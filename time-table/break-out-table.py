def time_in_min(time_string):
    # assumes 24h times
    (hour, minutes) = [int(t) for t in time_string.split(":")]
    return hour * 60 + minutes 

def min_to_time(time_min):
    minutes = time_min % 60
    hours = (time_min - minutes) / 60
    # return hour:minutes with leading zero
    return "{0}:{1:02d}".format(hours,minutes)

with open('output.csv', 'w') as out_f:
    out_f.write("id,in_id,time\n")
    with open('input.csv', 'r') as in_f:
        # skip the header row
        in_f.next()

        for row in in_f:
            # assign the rows to 
            (in_id,time_start,time_end,frequency) = row.split(",")

            start_min = time_in_min(time_start)
            end_min = time_in_min(time_end)

            for (out_id, time_step) in enumerate(range(start_min, end_min+1, int(frequency)), start=1):
                formatted_time = min_to_time(time_step)
                # write an output row
                out_f.write("{},{},{}\n".format(out_id, in_id, formatted_time))
