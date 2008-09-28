#!/usr/bin/python
import datetime
import supppl
import yaml
class StundenPlan(object):
    def __init__(self, cls):
        self.cls=cls
        yamllist = []
        file = open('classes.txt')        
        for i in yaml.load_all(file):
            yamllist.append(i)
        self.lessondict = yamllist[1]
        self.lessonteachers = yamllist[0]

    def getDicts(self):
        return (self.lessondict, self.lessonteachers)

    def getLessons(self):
        self.lessons = [['PUP','M2','ETH','BIUK', 'INF', 'INF'], 
            ['','GSPB','SPA', 'CH3', 'CH3', 'E1', '', '', '', 'BSPK', 'BSPK'], 
            ['SPA', 'D', 'M2', 'PH3', 'GWK'],
            ['ETH', 'D', 'E1', 'M2', 'PUP', 'BIUK', '', 'MU4A', 'MU4A', 'INFW', 'INFW'],
            ['GWK', 'D', 'SPA', 'E1', 'GSPB', 'PH3']]
        self.lessonnames = []
        #for i in self.lessons:
         #   templist = []
          #  for x in i:
            #    if x in self.lessondict.keys():
             #       templist.append(self.lessondict[x])
              #  else:
               #     templist.append(x)
            #self.lessonnames.append(templist)

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
                            if plan[i][z][4]:
                                if plan[i][z][4] in self.lessons[x.weekday()]:
                                    supplist.append([x.weekday(), plan[i][z][2] - 1,
                                            plan[i][z][3], plan[i][z][5], plan[i][z][8]])
                            elif plan[i][z][6]:
                                if plan[i][z][6] == self.lessonteachers[self.lessons[x.weekday()][plan[i][z][2]]]:
                                    supplist.append([x.weekday(), plan[i][z][2] - 1, 
                                            plan[i][z][3], plan[i][z][5], plan[i][z][8]])
                            else:
                                supplist.append([x.weekday(), plan[i][z][2] - 1, 
                                        plan[i][z][3], plan[i][z][5], plan[i][z][8]])
            return supplist

    def _datetoweekday(self):
           return dt.weekday() 
