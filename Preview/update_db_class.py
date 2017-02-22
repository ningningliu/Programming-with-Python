"""
update records in the database
tom, sue are persistent object in the shelve database
"""

import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(.25)
db['sue']= sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()