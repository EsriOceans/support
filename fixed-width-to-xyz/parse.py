def parse_line(line):
    column_pos = range(0, len(header), 10)
    return [line[i:i+10].strip() for i in column_pos]

with open('mon_jan_tempS.txt', 'r') as f:
    header = f.readline().strip()
    column_pos = range(0, len(header), 10)
    longitudes = parse_line(header)
    print("longitude,latitude,value")

    for line in f:
        row = parse_line(line)
        latitude = row[0]
        for (i, col) in enumerate(row[1:]):
            if col != 'NaN':
                print(",".join([longitudes[i], latitude, col]))
