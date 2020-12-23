# -*- coding: utf-8 -*-
"""
Spyder LScott

This is a temporary script file.
"""

import edempy.Deck as Deck
import xlsxwriter 

print("Loading h5 files...")
deck = Deck('BucketStraight.dem')
print("Calculting force and torque...")

tSteps = deck.numTimesteps

time = deck.timestepValues
cData = []

for i in range(0,tSteps):
    cData.append(deck.timestep[i].geometry[0].getCoords())
    
  
workbook = xlsxwriter.Workbook('StraightLift_coords.xlsx') 
worksheet = workbook.add_worksheet() 

print("write to excel...")
for j in range(len(cData)):
    row = 0
    col = j * 3 + 0
    string = "Time = "
    string += str(time[j])
    string += " (s)"
    worksheet.write(row, col, string)
    worksheet.write(row + 1, col + 0, "x")
    worksheet.write(row + 1, col + 1, "y")
    worksheet.write(row + 1, col + 2, "z")
    row = 2
    for i in range(0,len(cData[j])):
        worksheet.write(row, col + 0, cData[j][i][0])
        worksheet.write(row, col + 1, cData[j][i][1])
        worksheet.write(row, col + 2, cData[j][i][2])
        row+=1
workbook.close()

