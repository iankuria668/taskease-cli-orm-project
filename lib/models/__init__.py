import sqlite3

CONN = sqlite3.connect('taskease.db')
CURSOR = CONN.cursor()
