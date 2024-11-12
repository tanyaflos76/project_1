import sqlite3

con = sqlite3.connect('info_about_classes.sqlite')
cur = con.cursor()
with open('teachers_and_classes.txt', encoding='utf-8', mode='r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        teacher, subject, class_num, classes = line.split('\t')
        if class_num.isdigit():
            floor = int(str(class_num)[0])
        else:
            if class_num == 'class_num':
                floor = 1
            if class_num in ['спортзал_2 (малый)', 'спортзал_1 (большой)', 'спортзал_2 (большой)']:
                floor = 2
        query1 = f'''INSERT INTO teachers(id_teacher, name, subject, whom_teaches) VALUES({i + 1},'{teacher}','{subject}','{classes}')'''
        res1 = cur.execute(query1)
        query2 = f'''INSERT INTO classrooms(num_class, id_floor) VALUES('{class_num}','{floor}')'''
        res2 = cur.execute(query2)
        con.commit()

con.close()
