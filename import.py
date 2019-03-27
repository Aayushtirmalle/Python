import csv
import matplotlib.pyplot as plt
x=[]
y=[]
with open('myfile.csv','r') as csvfile:
	reader=csv.reader(csvfile)
	for i in reader:
		x.append(i[0])
		y.append(i[1])
plt.bar(x,y,color="cyan")
plt.show()
