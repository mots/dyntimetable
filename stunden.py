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
        file.close()
        self.lessondict = yamllist[1]
        self.lessonteachers = yamllist[0]

    def getDicts(self):
        return (self.lessondict, self.lessonteachers)

    def getLessons(self):
        file = open('timetable.txt')
        yamlstuff = yaml.load(file)
        self.lessons = []
        self.rooms = []
        for day in yamlstuff:
            templessons = []
            temprooms = []
            for lesson in day:
                if lesson:
                    templessons.append(lesson[0])
                    temprooms.append(lesson[1])
                else:
                    templessons.append('')
                    temprooms.append('')
            self.lessons.append(templessons)
            self.rooms.append(temprooms)
        return self.lessons, self.rooms

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
                            suppl = plan[i][z]
                            if suppl[4]:
                                if suppl[4] in self.lessons[x.weekday()]:
                                    supplist.append([x.weekday(), suppl[2] - 1,
                                            suppl[3], suppl[5], suppl[8]])
                            elif plan[i][z][6]:
                                try:
                                    teacher = self.lessonteachers[self.lessons[x.weekday()][suppl[2]-1]]
                                except:
                                    teacher = ''
                                if suppl[6] == teacher: 
                                    supplist.append([x.weekday(), suppl[2] - 1, 
                                            suppl[3], suppl[5], suppl[8]])
                            else:
                                supplist.append([x.weekday(), suppl[2] - 1, 
                                        suppl[3], suppl[5], suppl[8]])
            return supplist

    def _datetoweekday(self):
           return dt.weekday() 
