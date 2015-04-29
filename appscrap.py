#!/usr/bin/env python
# encoding: utf-8

# © APPSCRAP2015 - author: Joel Crespo
# This file is part of Appscrap.
#
# Appscrap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Appscrap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Scrapy.  If not, see <http://www.gnu.org/licenses/>.



from src import scrapy
from sys import argv
from os import environ, system
import time
from getpass import getpass


def start():
	if len(argv)==7:
		for i in xrange(1,7):
			if argv[i]=='-u' or argv[i]=='--user':
				user=argv[i+1]
			elif argv[i]=='-p' or argv[i]=='--password':
				password=argv[i+1]

	elif environ.has_key("SUSER") and environ.has_key("SPASSWD"):
		user=environ["SUSER"]
		password=environ["SPASSWD"]
	else:
		user=str(raw_input("\n Usuario: "))
		password=getpass(" Contraseña:")










	if len(argv)>0:


		if argv[1] in ('bbva', 'BBVA', 'Bbva'):
			if argv[2]=='saldo' or argv[2]=='balance':
				system('clear')
				print "\033[90m [\033[30mSCRA\033[31mPY\033[90m] :\033[0m "+"\033[34m BBVA \033[96mProvincial\033[0m"
				bbva = scrapy.bbva(str(user),str(password))
				bbva.balance()
				bbva.close()
			elif argv[2]=='movimientos' or argv[2]=='transactions':
				system('clear')
				print "\033[90m [\033[30mSCRA\033[31mPY\033[90m] :\033[0m "+"\033[34m BBVA \033[96mProvincial\033[0m"
				bbva = scrapy.bbva(str(user),str(password))
				bbva.balance()
				bbva.transactions()
				bbva.close()


		elif argv[1]=='mercantil' or argv[1]=='Mercantil' or argv[1]=='MERCANTIL':
			if argv[2]=='saldo' or argv[2]=='balance':
				system('clear')
				print "\033[90m [\033[30mSCRA\033[31mPY\033[90m] :\033[0m "+"\033[31m Banco \033[91mMercantil\033[0m"
				mercantil = scrapy.mercantil('501878200055812004',"l\/vTQwJw\/2yDw03cdGp4Oebp2U34cAjdsvO6tBeTTMkHkoBKc+DENfjJ\/o34wF6\/iZslNck4PTzFCi0asd0tGKVNtnvEVcG4rqJNRC\/YMVjhSu\/jUedpAuT1imH\/l09GedsHQ3qXwA8QRZvPiz4xFdnyJq0pF8JMWn3kqVYqG0jHvf4upzpZ6w3lKzDFAl3MFMesa8HOYBsDFtPoR8iPvdVh5Sh\/qbDy6PgEuEQNNA3ZAngnLTBcjHdp7SkINyZ9h4iUwtX4q1SMfWmebSnP2sEgGROo3CaxmNVXM0E90NROdGCIYoRsYqDOV5eAjjS4yD9G4z3hXYF\/YsUHvRe5fg==")
				#mercantil = scrapy.mercantil(str(user),str(password))
				mercantil.close()
			elif argv[2]=='movimientos' or argv[2]=='transactions':
				system('clear')
				print "\033[90m [\033[30mSCRA\033[31mPY\033[90m] :\033[0m "+"\033[31m Banco \033[91mMercantil\033[0m"
				mercantil = scrapy.mercantil('501878200055812004',"l\/vTQwJw\/2yDw03cdGp4Oebp2U34cAjdsvO6tBeTTMkHkoBKc+DENfjJ\/o34wF6\/iZslNck4PTzFCi0asd0tGKVNtnvEVcG4rqJNRC\/YMVjhSu\/jUedpAuT1imH\/l09GedsHQ3qXwA8QRZvPiz4xFdnyJq0pF8JMWn3kqVYqG0jHvf4upzpZ6w3lKzDFAl3MFMesa8HOYBsDFtPoR8iPvdVh5Sh\/qbDy6PgEuEQNNA3ZAngnLTBcjHdp7SkINyZ9h4iUwtX4q1SMfWmebSnP2sEgGROo3CaxmNVXM0E90NROdGCIYoRsYqDOV5eAjjS4yD9G4z3hXYF\/YsUHvRe5fg==")
				#mercantil = scrapy.mercantil(str(user),str(password))
				mercantil.transactions()
				mercantil.close()


start()
