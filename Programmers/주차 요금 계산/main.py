from math import ceil
def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    total_time = {}
    parking_lot = {}
    for record in records:
        record_time, car_num, flag = record.split()
        realtime = int(record_time.split(':')[0]) * 60 + int(record_time.split(':')[1])
        if flag == "IN":
            parking_lot[car_num] = realtime
            if car_num not in total_time.keys(): total_time[car_num] = 0

        elif flag == "OUT":
            intime = parking_lot[car_num]
            del parking_lot[car_num]
            duration = realtime - intime
            total_time[car_num] += duration


    realtime = 23 * 60 + 59
    for car_num in parking_lot:
        intime = parking_lot[car_num]
        duration = realtime - intime
        total_time[car_num] += duration

    all_fees = []
    for car_num in sorted(total_time.keys()):
        duration =  total_time[car_num]
        if duration <= default_time: all_fees.append(int(default_fee))
        else: all_fees.append(default_fee + ceil((duration - default_time) / unit_time) * unit_fee)

    return all_fees