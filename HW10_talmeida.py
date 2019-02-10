# Activity X.X.X: An introduction to Python.
# File: HW10_talmeida.py
# Date: 15 November 2018
# By: Tessca Almeida
# talmeida
# Section: 2
# Team: 40
#
# ELECTRONIC SIGNATURE
# Tessca Almeida
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# This program outputs the five of the top and worst cereals decided by 
# ratings, and the average sugar, calories, protein, and potassium of 
# the two different groups. Please note that the best cereal is at 
# the bottom of the list and the worst one is at the bottom as well.
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
import csv

totalSugar = 0.0
totalCalories = 0.0
totalProtein=0.0
totalPotassium= 0.0

#---------------------------------------------------
#  Computations
#---------------------------------------------------
with open('cereal.csv', 'r', newline='') as file:
    reader= csv.reader(file,delimiter=',')
    cereal= []
    for row in reader:
        cereal.append(row)
    cereal.pop(0)
    
p= len(cereal)
for x in range(0, p):
        for y in range(0, p-x-1):
            if cereal[y][15] > cereal[y+1][15]:
                cereal[y], cereal[y+1] = cereal[y+1],cereal[y]
#---------------------------------------------------
#  Outputs
#---------------------------------------------------            
print('The top 5 rated cereals are:' )
for i in range (-1,-6,-1):
    print(cereal[i][0])
    totalSugar += float(cereal[i][9])
    totalCalories += float(cereal[i][3])
    totalProtein += float(cereal[i][4])
    totalPotassium += float(cereal[i][10])

avgSugar = totalSugar / 5
avgCalories = totalCalories / 5
avgProtein = totalProtein / 5
avgPotassium = totalPotassium / 5

print('\nTop cereals average sugar: ', str(avgSugar))
print('Top cereals average calories: ', str(avgCalories))
print('Top cereals average protein:', str(avgProtein))
print('Top cereals average potassium:', str(avgPotassium))

totalSugar = 0.0
totalCalories = 0.0
totalProtein = 0.0
totalPotassium = 0.0

print('\nThe worst 5 rated cereals are: ')
for j in range (4,-1,-1):
    print(cereal[j][0])
    totalSugar += float(cereal[j][9])
    totalCalories += float(cereal[j][3])
    totalProtein += float(cereal[j][4])
    totalPotassium += float(cereal[j][10])

avgSugar = totalSugar / 5
avgCalories = totalCalories / 5
avgProtein = totalProtein / 5
avgPotassium = totalPotassium / 5

print('\nWorst cereals average sugar: ', str(avgSugar))
print('Worst cereals average calories: ', str(avgCalories))
print('Worst cereals average protein:', str(avgProtein))
print('Worst cereals average potassium:', str(avgPotassium))