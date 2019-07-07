import sqlite3
import os.path

def make_db():
    if not os.path.exists('leaderboard.db'):
        conn = sqlite3.connect('leaderboard.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE leaders
        	(Name Text, Score Integer, GameDate Date)
    	    ''')
        conn.commit()
        conn.close()
    else: pass

def insert_db(player, score, game_date):
    conn = sqlite3.connect('leaderboard.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO leaders VALUES (?,?,?);
        ''', (player, score, game_date))
    conn.commit()
    conn.close()

def results_db():
    conn = sqlite3.connect('leaderboard.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT SUBSTR(name,1,20) AS name, score, strftime('%m/%d/%Y', gamedate)
        FROM leaders
        ORDER BY score ASC
        LIMIT 20;
        ''')
    rows = cur.fetchall()
    print('''\n\n
 _                    _
| |                  | |
| |     ___  __ _  __| | ___ _ __ ___
| |    / _ \/ _` |/ _` |/ _ \ '__/ __|
| |___|  __/ (_| | (_| |  __/ |  \__ \\
\_____/\___|\__,_|\__,_|\___|_|  |___/
    ''')
    print('\n\nNAME               MOVES          DATE')
    print('____________________________________________________\n')
    for row in rows:
        print('%-20s %-10s %-30s' % (row[0], str(row[1]), row[2]))
    print('\n\n\n')

    conn.close()
