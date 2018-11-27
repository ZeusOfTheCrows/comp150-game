import Helper
import Entity


class TimeOfDay:

    CurrentTime = 'perhaps'
    PreviousTime = CurrentTime
    MonsterBuff = 1

    @staticmethod
    def update_time_of_day(current_time):
        if Helper.TIME_OF_DAY['morning'][0][0] \
                >= current_time.hour * 100 + current_time.minute \
                < Helper.TIME_OF_DAY['morning'][0][1]:
            TimeOfDay.CurrentTime = 'morning'
            TimeOfDay.MonsterBuff = 1
        elif Helper.TIME_OF_DAY['noon'][0][0] \
                >= current_time.hour * 100 + current_time.minute \
                < Helper.TIME_OF_DAY['noon'][0][1]:
            TimeOfDay.CurrentTime = 'noon'
            TimeOfDay.MonsterBuff = 0.85
        elif Helper.TIME_OF_DAY['evening'][0][0] \
                >= current_time.hour * 100 + current_time.minute \
                < Helper.TIME_OF_DAY['evening'][0][1]:
            TimeOfDay.CurrentTime = 'evening'
            TimeOfDay.MonsterBuff = 1
        else:
            TimeOfDay.CurrentTime = 'night'
            TimeOfDay.MonsterBuff = 1.25

        if TimeOfDay.CurrentTime \
                != TimeOfDay.PreviousTime:
            print('It is now ' + TimeOfDay.CurrentTime
                  + Helper.TIME_OF_DAY[TimeOfDay.CurrentTime][2])
            TimeOfDay.PreviousTime = TimeOfDay.CurrentTime

