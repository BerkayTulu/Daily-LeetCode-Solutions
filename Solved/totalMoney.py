def totalMoney(n):
        """
        :type n: int
        :rtype: int
        """
        def weeklySave(start,days):
                total = 0
                for i in range(days):
                        total += start + i
                return total
        
        fullWeeks = n // 7
        lastWeekDay = n % 7
        total = 0

        for week in range(fullWeeks):
                total += weeklySave(1 + week, 7)
        
        total += weeklySave(fullWeeks+1, lastWeekDay)

        return total

totalMoney(175)