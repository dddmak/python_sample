import csv
with open('test.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow([1,'spam','500'])
    writer.writerow([2,'egg','168'])
    writer.writerow([3,'bbcorn','1,250'])
