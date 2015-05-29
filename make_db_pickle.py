__author__ = 'User'

from initdata import db
import pickle

dfile = open('people-pickle', 'wb')
pickle.dump(db, dfile)
dfile.close()