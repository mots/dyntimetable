from supppl import Supplierplan

sp = Supplierplan(school=101016, usr='schueler', pw='dsdns', cl='8bi')
if sp.check_supps():
    plan = sp.proc_html()
    print plan

