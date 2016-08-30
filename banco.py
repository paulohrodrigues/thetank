# coding: utf8
import sqlite3

class Banco(object):
	def __init__(self):
		self.conexao  =sqlite3.connect('banco.db')
		self.conector = self.conexao.cursor()

	def criadorDeTabelas(self):
		self.conector.execute("CREATE TABLE IF NOT EXISTS jogo(id INTEGER PRIMARY KEY ASC,pontos INTEGER)")

	def inserir(self,pontos):
		if(self.busca()==[]):
			self.conector.execute("insert into jogo(pontos) values (?)",[int(pontos)])
			self.conexao.commit()
		elif(int(self.busca()[0][1])<int(pontos)):
			self.conector.execute("insert into jogo(pontos) values (?)",[int(pontos)])
			self.conexao.commit()
		else:
			return list([1,0]) 

	def busca(self):
		self.conector.execute('SELECT * FROM jogo ORDER BY pontos DESC')
		return self.conector.fetchall()
	
	def fechaConexao(self):
		self.conector.close()
		self.conexao.close()