#combing through a spreadsheet of subscale motor data and plotting it

import xlrd
import matplotlib.pyplot as plt

filename = "s-h-st-100_load.xls"

wb = xlrd.open_workbook(filename)
sheet_1 = wb.sheet_by_index(0)

time_stamp = []
load = []
sample_num = []

for col in range(0,sheet_1.ncols//4):
    for row in range(1,sheet_1.nrows):
        time_stamp.append(sheet_1.cell_value(row,(col*4)+3) * 86400)
        load.append(sheet_1.cell_value(row,(col*4)+1))
        sample_num.append(sheet_1.cell_value(row,(col*4)+0))

# plot stuff
fig, ax1 = plt.subplots()
ax1.plot(time_stamp,load) #trying to get rid of some pts so the plot can actually generate
ax1.set_xlabel('Time')
ax1.set_ylabel('Pounds')
ax2 = ax1.twiny()
ax2.plot(sample_num,load)
ax2.set_xlabel('Sample Number')
fig.tight_layout()
plt.grid()
plt.show()