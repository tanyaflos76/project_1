import sqlite3

con = sqlite3.connect('info_about_classes.sqlite')
for i in range(100, 430):
    s = f'floors/{str(i)}.png'
    cur = con.cursor()
    query1 = f'''select id_teacher from classrooms where num_class = "{i}"'''
    res1 = cur.execute(query1).fetchall()
    if res1:
        query2 = f'''UPDATE classrooms SET file_name = "{s}" WHERE num_class = "{i}"'''
        res2 = cur.execute(query2)
    con.commit()
con.close()
