def split_time(date: str, time: str):
    date_split = date.split("-")
    time_split = time.split(":")
    year = date_split[0]
    month = date_split[1]
    day = date_split[2]
    hour = time_split[0]
    minute = time_split[1]
    second = time_split[2]
    res = [year, month, day, hour, minute, second]
    return "-".join(res)

def get_joined(dates: list, times: list):
    res = []
    dN = len(dates)
    tN = len(times)
    i = 0
    while i < dN or i < tN:
        if not dates[i] or not times[i]:
            continue
        res.append(split_time(dates[i], times[i]))
        i+=1
    return res

def main():
    d1 = "2022-03-23"
    d2 = "2022-03-23"
    d3 = "2022-03-23"
    d4 = "2022-03-23"
    d5 = "2022-03-23"
    dates = [d1, d2, d3, d4, d5]

    t1 = "15:05:07"
    t2 = "15:05:07"
    t3 = "15:05:07"
    t4 = "15:05:07"
    t5 = "15:05:06"
    times = [t1, t2, t3, t4, t5]
    # print(split_time(dates[0], times[0]))
    # print(get_joined(dates, times))


if __name__ == "__main__":
    main()