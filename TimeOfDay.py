import Helper


class TimeOfDay:
    """
    ---------------------------------------------------------------------------
    Class containing function to change monster buff based on time of day.
    ---------------------------------------------------------------------------
    """

    CurrentTime = 'perhaps'
    PreviousTime = CurrentTime
    MonsterBuff = 1

    @staticmethod
    def update_time_of_day(current_time):
        """
        =======================================================================
        Function to calculate buff of monsters based on current time of day.

        :param current_time: time in YYYY-MM-DD hh:mm:ss.SSSSSS format
        :return: message to be displayed - how strong enemies are.
        =======================================================================
        """

        message = ''
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
            message = ('It is now ' + TimeOfDay.CurrentTime
                       + Helper.TIME_OF_DAY[TimeOfDay.CurrentTime][2])
            TimeOfDay.PreviousTime = TimeOfDay.CurrentTime

        return message if len(message) > 0 else None

