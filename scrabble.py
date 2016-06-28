import os
import csv
import numpy as np
import operator
import matplotlib.pyplot as plt

Scrabble_score = {
'France' : {"E":1, "A":1, "I":1, "N":1, "O":1, "R":1, "S":1, "T":1, "U":1, "L":1,
"D":2, "M":2, "G":2,
"B":3, "C":3, "P":3,
"F":4, "H":4, "V":4,
"J":8, "Q":8,
"K":10, "W":10, "X":10, "Y":10, "Z":10},

# U et A de l'allemand
'Suisse' : {"E":1, "A":1, "I":1, "N":1, "O":1, "R":1, "S":1, "T":1, "U":1, "L":1,
"D":2, "M":2, "G":2,
"B":3, "C":3, "P":3,
"F":4, "H":4, "V":4,
"J":8, "Q":8,
"K":10, "W":10, "X":10, "Y":10, "Z":10},

'Angleterre' : {"E":1, "A":1, "I":1, "N":1, "O":1, "S":1, "R":1, "T":1, "U":1, "L":1,
"D":2, "G":2,
"B":3, "C":3, "M":3, "P":3,
"F":4, "H":4, "V":4, "W":4, "Y":4, 
"K":5,
"J":8, "X":8,
"Q":10, "Z":10},

'Allemagne' : {"E":1, "N":1, "S":1, "I":1, "R":1, "T":1, "U":1, "A":1, "D":1,
"H":2, "G":2,"L":2,"O":2,
"M":3, "B":3, "W":3, "Z":3,
"C":4, "F":4, "K":4, "P":4, 
"J":6, "V":6,
"X":8,
"Q":10, "Y":10},

'Autriche' : {"E":1, "N":1, "S":1, "I":1, "R":1, "T":1, "U":1, "A":1, "D":1,
"H":2, "G":2,"L":2,"O":2,
"M":3, "B":3, "W":3, "Z":3,
"C":4, "F":4, "K":4, "P":4, 
"J":6, "V":6,
"X":8,
"Q":10, "Y":10},

'Belgique' : {"E":1, "N":1, "A":1, "O":1, "I":1,
"D":2, "R":2,"T":2,"S":2,
"G":3, "K":3, "L":3, "M":3, "B":3, "P":3,
"U":4, "H":4, "J":4, "V":4, "Z":4, "F":4,
"C":6, "W":6,
"X":8, "Y":8,
"Q":10},

'Croatie' : {"A":1, "I":1, "E":1, "O":1, "N":1, "R":1, "S":1, "T":1, "J":1, "U":1,
"K":2, "M":2, "P":2,"V":2,
"D":3, "G":3, "L":3, "Z":3, "B":3,
"C":4, "H":4,
"F":8},

# Utilisation V W K Y Q du dico anglais
'Eire' : {"A":1, "H":1, "I":1, "N":1, "R":1, "E":1, "S":1,
"C":2, "D":2, "L":2, "O":2, "T":2, "G":2, "U":2,
"F":4, "M":4, "V":4, "W":4, "Y":4,
"K":5,
"Q":10, "B":10, "P":10},

'Espagne' : {"A":1, "E":1, "O":1, "I":1, "S":1, "N":1, "R":1, "U":1, "L":1, "T":1,
"D":2, "G":2,
"C":3, "B":3, "M":3, "P":3,
"H":4, "F":4, "V":4, "Y":4,
"Q":5,
"J":8, "X":8,
"Z":10},

'Hongrie' : {"A":1, "E":1, "K":1, "T":1, "L":1, "N":1, "R":1, "I":1, "M":1, "O":1, "S":1,
"B":2, "D":2, "G":2,
"H":3, "V":3,
"F":4, "J":4, "P":4, "U":4, "Z":4,
"C":5,
"Y":8},

# Utilisation V W K Y Q du dico anglais
'IrlandeNord' : {"A":1, "H":1, "I":1, "N":1, "R":1, "E":1, "S":1,
"C":2, "D":2, "L":2, "O":2, "T":2, "G":2, "U":2,
"F":4, "M":4, "V":4, "W":4, "Y":4,
"K":5,
"Q":10, "B":10, "P":10},

'Islande' : {"A":1, "I":1, "N":1, "R":1, "E":1, "S":1, "U":1, "T":1,
"G":2, "K":2, "L":2, "M":2,
"F":3, "O":3, "H":3, "V":3,
"D":4,
"J":5,
"B":6,
"Y":7,
"P":8,
"X":10},

# Ajout de W Y
'Italie' : {"O":1, "A":1, "I":1, "E":1,
"C":2, "R":2, "S":2, "T":2,
"L":3, "M":3, "N":3, "U":3,
"B":5, "D":5, "F":5, "P":5, "V":5,
"G":8, "H":8, "Z":8,
"Q":10, "W":10, "Y":10,},

'Turquie' : {"A":1, "E":1, "K":1, "L":1, "R":1, "N":1, "T":1,
"I":2, "M":2, "O":2, "S":2, "U":2,
"B":3, "D":3, "Y":3,
"C":4, "Z":4, 
"H":5, "P":5, "G":5,
"F":7, "V":7,
"J":10},

# Ajout Q W
'Suede' : {"A":1, "R":1, "S":1, "T":1, "E":1, "N":1, "D":1, "I":1, "L":1,
"O":2, "G":2, "K":2, "M":2, "H":2,
"F":3, "V":3,
"U":4, "B":4, "P":4, 
"J":7, "Y":7,
"C":8, "X":8,
"Z":10, "Q":0, "W":0},

# Anglais
'PaysDeGalles' : {"E":1, "A":1, "I":1, "N":1, "O":1, "S":1, "R":1, "T":1, "U":1, "L":1,
"D":2, "G":2,
"B":3, "C":3, "M":3, "P":3,
"F":4, "H":4, "V":4, "W":4, "Y":4, 
"K":5,
"J":8, "X":8,
"Q":10, "Z":10},

# Ajout K
'Roumanie' : {"A":1, "I":1, "E":1, "R":1, "T":1, "N":1, "U":1, "C":1, "O":1, "S":1, "L":1,
"D":2, "P":2,
"M":4,
"F":8, "V":8, 
"B":9, "G":9,
"H":10, "J":10, "X":10, "Z":10, "K":10},

'Pologne' : {"A":1, "I":1, "E":1, "O":1, "N":1, "Z":1, "R":1, "S":1, "W":1,
"Y":2, "C":2, "D":2, "K":2, "L":2, "M":2, "P":2, "T":2,
"B":3, "G":3, "H":3, "J":3, "U":3,
"F":5},

'Portugal' : {"A":1, "I":1, "O":1, "S":1, "U":1, "M":1, "R":1, "E":1, "T":1,
"C":2, "P":2, "D":2, "L":2,
"N":3, "B":3,
"F":4, "G":4, "H":4, "V":4,
"J":5,
"Q":6,
"X":8, "Z":8},

'RepTcheque' : {"O":1, "A":1, "E":1, "N":1, "I":1, "S":1, "T":1, "V":1, "D":1, "K":1, "L":1, "P":1, "R":1,
"C":2, "H":2, "M":2, "U":2, "J":2, "Y":2, "Z":2,
"B":3,
"F":5, "G":5,
"X":10},

'Russie' : {"O":1, "A":1, "E":1, "N":1, "I":1, "R":1, "S":1, "T":1, "V":1,
"K":2, "M":2, "U":2, "L":2, "D":2,
"G":3, "B":3,
"Y":4,
"H":5, "Z":5, "C":5,
"F":10},

# Ajout Y W
'Slovaquie' : {"E":1, "A":1, "I":1, "O":1, "N":1, "R":1, "S":1, "J":1, "L":1, "T":1,
"D":2, "V":2,
"K":3, "M":3, "P":3, "U":3,
"B":4, "G":4, "Z":4,
"H":5, "Y":5, 
"C":8,
"F":10, "W":10},

'Ukraine' : {"O":1, "A":1, "H":1, "B":1, "E":1, "I":1, "T":1,
"K":2, "P":2, "C":2,
"M":3,
"J":4,
"X":5,
"Q":8,
"G":10
}

}

def histogramme(result,name):
    plt.figure(figsize=(20,10),dpi=150)
    x = np.array([])    
    y = np.array([])
    for i in result:
        x = np.append(x,i[0])
        y = np.append(y,i[1])
    
    bins = np.array([i for i in range(0,23,1)])
    print(name)
    print(x)
    print(y)
    plt.xticks(bins+0.3/2,x,rotation = 'vertical')
    plt.bar(bins,y,0.3,color = 'r')
    plt.savefig('histogramme_'+name)
    plt.close()


def ratio_surname(Scrabble_score):
    final_result_std= {}
    final_result_mean={}
    
    for filename in os.listdir('PASTI'):
    	country = filename[:len(filename)-4]
    	with open("PASTI/"+filename, 'rb') as csvfile:
    		spamreader = csv.reader(csvfile, delimiter=' ')
    		result = {}
    		
    		for name in spamreader:
    			score = 0
    			if (len(name[1]) != 0):
    				for letter in range(len(name[1])):
    					if name[1][letter].upper() in Scrabble_score[country]:
    						score += Scrabble_score[country][name[1][letter].upper()]
    					else:
    						print("ERROR:"+name[1][letter].upper()+" "+country)
    				result[name[1].upper()] = float(score)/len(name[1])
    		
    		final_result_std[country] = np.std(result.values())
    		final_result_mean[country] = np.mean(result.values())            
    # Sort the dictionary /!\ cast it into a list
    final_result_std = sorted(final_result_std.items(), key=operator.itemgetter(1))  
    final_result_mean = sorted(final_result_mean.items(), key=operator.itemgetter(1))
    return final_result_std,final_result_mean
  




final_result_std,final_result_mean = ratio_surname(Scrabble_score)
histogramme(final_result_std,"std")
histogramme(final_result_mean,"mean")
