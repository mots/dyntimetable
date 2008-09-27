# coding: utf-8
from supppl import Supplierplan

sp = Supplierplan(school=101016, usr='schueler', pw='dsdns', cl='8bi')
if sp.check_supps():
    plan = sp.proc_html()
    #print plan
    for y in plan.keys():
        for x in plan[y]:
            print x[2]
            print x[5]
            print x[6]
            if x[8]:
                print x[8]
            #print x[2] + '. Stunde (im ' + x[5] + '): ' + 'Lehrer '+ x[6] + ' fehlt, Kommentar: ' + x[8]
