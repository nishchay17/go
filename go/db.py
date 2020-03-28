import sqlite3
import os

class DB():

	def __init__(self):
		PATH = os.path.abspath(os.path.dirname(__file__)) + "/../dirName.db"
		self.conn = sqlite3.connect(PATH)
		self.cur = self.conn.cursor()
		self.cur.execute('CREATE TABLE IF NOT EXISTS dir (dir TEXT, name TEXT)')

	def entry(self, dir, name):
		self.cur.execute('INSERT INTO dir (dir, name) VALUES (?,?)',(dir, name))
		self.conn.commit()

	def read(self, name):
		self.cur.execute( 'SELECT * FROM dir WHERE name == (?)', (name, ))
		data = self.cur.fetchone()
		return data

	def getAll(self):
		self.cur.execute('SELECT * FROM dir')
		data = self.cur.fetchall()
		return data

	def find(self, name):
		self.cur.execute( 'SELECT COUNT(*) FROM dir WHERE name == (?)', (name, ))
		number = self.cur.fetchone()[0]
		return number
		
	def remove(self, name):
		if self.find(name) == 0:
			return False
		else:
			self.cur.execute('DELETE FROM dir WHERE name == (?)', (name, ))
			self.conn.commit()
			return True

	def close(self):
		self.cur.close()
		self.conn.close()	

