import psycopg2
import sys
import csv

print('loading employees ...')
filename=sys.argv[1]

with open(filename) as csvfile:
    data = list(csv.reader(csvfile))
c = psycopg2.connect(user="postgres",
                     port="5432",
                     host="127.0.0.1",
                     database="skischool")
cur = c.cursor()
count = 0
line = 1
for d in data:
    if d[1]!='lastname':
        if d[5]=='':
            d[5] = None
        cur.callproc('add_employee',[d[0],d[1],d[2],d[3],d[4],d[5],])
        result = cur.fetchall()
        for r in result:
            if r[0][-6:]!='added!':
                print """Error at line %s on employee %s %s """ % (line,d[0], d[1])
            else:
                count+=1
    line+=1
print """added %s entries """ % (count)
c.commit()
cur.close()
c.close()