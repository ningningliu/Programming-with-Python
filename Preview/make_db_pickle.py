from initdata import db
import pickle
dbfile = open('people-pickle','wb') # binary mode files
pickle.dump(db, dbfile)  # data is bytes not str
dbfile.close()

