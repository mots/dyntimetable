#!/usr/bin/python
import datetime
import supppl
class StundenPlan(object):
    def __init__(self, cls):
        self.cls=cls

    def getLessons(self):
        self.lessons = [['PUP','MA','ETH','BIUK', 'INF', 'INF'], 
            ['','GSPB','SPA', 'CH3', 'CH3', 'E', '', '', '', 'BUSP', 'BUSP'], 
            ['SPA', 'D', 'MA', 'PH', 'GWK'],
            ['ETH', 'D', 'E', 'MA', 'PUP', 'BIUK', '', 'MU', 'MU', 'INF+', 'INF+'],
            ['GWK', 'D', 'SPA', 'E', 'GSPB', 'PH']]
        return self.lessons

    def getCurrentSups(self):
        sp = supppl.Supplierplan(101016, self.cls, 'schueler', 'dsdns')
        supplist = []
        if sp.check_supps():
            plan = sp.proc_html()
            datelist = []
            now = datetime.datetime.today()
            for i in xrange(7):
                day = (now + datetime.timedelta(days = i))
                if day.weekday() <= 4:
                    datelist.append(day)
            for i in plan.keys():
                for x in datelist:
                    if i.date() == x.date():
                        for z in xrange(len(plan[i])):
                            if not (plan[i][z][4] and plan[i][z][4] not in self.lessons[x.weekday()]):
                                supplist.append([x.weekday(), int(plan[i][z][2]) - 1, \
                                        plan[i][z][3], plan[i][z][5], plan[i][z][8]])
            return supplist

    def _datetoweekday(self):
           return dt.weekday() 
