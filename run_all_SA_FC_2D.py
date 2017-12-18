from protein_class import Protein

# import algorithms
from algorithms.SA_FC import simulated_annealing_control2D

import csv

def main():

    with open('B2_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "HPHPPHHPHPPHPHHPPHPH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)          
            datawriter.writerow([i] + [protein.winning_score])

    with open('B3_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)          
            datawriter.writerow([i] + [protein.winning_score])

    with open('B4_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)  
            datawriter.writerow([i] + [protein.winning_score])

    with open('C1_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)     
            datawriter.writerow([i] + [protein.winning_score])

    with open('C2_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)            
            datawriter.writerow([i] + [protein.winning_score])

    with open('C3_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)          
            datawriter.writerow([i] + [protein.winning_score])

    with open('C4_2D_SA_FC.csv', 'a', newline='') as datafile:
        datawriter = csv.writer(datafile)

        for i in range(50):
            print("Piep: " + str(i))
            protein_string = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
            protein = Protein(protein_string.upper(), len(protein_string), [], [], [], [], 0, [])
            protein.init_grid()
            protein = simulated_annealing_control2D(protein)        
            datawriter.writerow([i] + [protein.winning_score])


if __name__ == '__main__':
	main()

