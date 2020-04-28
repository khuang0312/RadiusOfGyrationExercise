# Assignment1.py
# Kevin Huang
# huangk11@uci.edu

#!/usr/bin/env python

import glob
import numpy as np


import os
import matplotlib.pyplot as plt 

def ReadPdb( PdbFile ):
    """Reads a PDB file with a name provided in the argument. 
       Assumes the PDB file contains only ATOM and TER entries; TER entries are skipped.
       
       RETURNS:
        - Pos, an (Nx3) dimensional NumPy array of positions of alpha carbons
        - ResNames, a list of residue names.
    """
    
    # ENTER YOUR CODE TO GET Pos, ResNames here. 
    # Manipulate them until you get them in the required format, 
    #  then use the return statement below to return these... 
    ResNames = []

     
    with open(PdbFile) as pdb:
        for line in pdb:
            # that means line is "TER" or the end
            if line[0:3] == "TER":
                break
            
            atom_name = line[12:16].strip()

            if atom_name == "CA":
                ResName = line[17:20].strip()
                ResNames.append(ResName)
                 
                x_coord = float(line[30:38].strip())
                y_coord = float(line[38:46].strip())
                z_coord = float(line[46:54].strip())

                coords =  np.array([x_coord, y_coord, z_coord])
                
                # this allows subsequent coordinates to be stacked below
                if line[22:26].strip() == '1':                      
                    Pos = coords
                else:
                    Pos = np.vstack((Pos, coords)) # stack Pos on top of newly created array

    #Return
    return Pos, ResNames


def ResHydrophobic( ResNames ):
    """Take list of three letter codes for residue names; 
       returns a list, IsPhobic, of True/False values 
       depending on whether residues are hydrophobic or not."""

    #Enter your code to identify whether residues or hydrophobic or not here.
    #Use the return statement below to return them.
    
    def isHydrophobic(residue):
        return residue in {"ALA", "CYS", "PHE", "ILE", "LEU", "MET", "PRO", "VAL", "TRP"}

    return [isHydrophobic(i) for i in ResNames]


def RadiusOfGyration( Pos ):
    """Take an Nx3 dimensional array of positions; return the radius of gyration."""

    #Enter your code to compute the radius of gyration here. 
    #Use the return statement below to return it. 
    N = Pos.shape[0] # get the number of rows in Pos
    
    # find r bar
    r_bar = np.zeros(3)
    
    for i in Pos:
        r_bar += i

    r_bar = np.divide(r_bar, N)
     
    # find r-sub g
    r_g_squared = 0

    for r_i in Pos:
        r_g_squared += np.power(np.linalg.norm(r_i - r_bar), 2)
    
    r_g_squared = np.divide(r_g_squared, N)
    Rg = np.sqrt(r_g_squared)
    return Rg


#SOME SAMPLE SKELETON CODE TO SET UP USE OF THOSE FUNCTIONS FOLLOWS BELOW

#This next if statement is optional; this specifies a block of code that will only execute if the Python program is RUN but NOT if it is imported. Since our intent here is to run the code (not import it) this is unnecessary, but sometimes this is useful.
if __name__=='__main__':
   
    #Obtain list of pdbfiles
    pdbfiles = glob.glob('*.pdb')

    #Create some empty lists for storing data
    Rglist = []
    Rgphobiclist = []
    nres = []

    #YOUR CODE GOES HERE -- YOU WOULD SET UP A LOOP OVER THE PDB FILES AND DO THE CALCULATIONS
    #Note for testing purposes you should pick a particular PDB file and try your functions on it. 
    #In fact, the function for checking residue names can be tested without a PDB file...
    for pdb in pdbfiles:
        Pos, ResNames = ReadPdb(pdb)
        hydrophobicIndices = []
        
        isPhobic = ResHydrophobic(ResNames)
         
        # we need to figure out which indices contain the hydrophobic residues
        for i in range(len(isPhobic)):
            if isPhobic[i]:
                hydrophobicIndices.append(i)
        
        # radius of gyration of all residues
        Rg = RadiusOfGyration(Pos)
                
        # radius of gyration of only hydrophobic residues
        PhobicPos = Pos[hydrophobicIndices[0]]
        
        for i in hydrophobicIndices[1:]:
            PhobicPos = np.vstack((PhobicPos, Pos[i]))
        
        Rgphobic = RadiusOfGyration(PhobicPos)
        
        # total number of residues
        N = Pos.shape[0]
        
        # store them
        Rglist.append(Rg)
        Rgphobiclist.append(Rgphobic)
        nres.append(N)

    #ONCE YOU ARE DONE LOOKING AT ALL PDB FILES, YOU WANT TO MAKE SOME PLOTS.
    plot_data = {x : (y, z) for x, y, z in zip(nres, Rglist, Rgphobiclist)}
    nres = sorted(plot_data)
    Rglist = [plot_data[n][0] for n in nres]
    Rgphobiclist = [plot_data[n][1] for n in nres]
    RgOverRgphobic = [x/y for x, y in zip(Rglist, Rgphobiclist)]
    
    # plot 1 (combined)
    plt.plot(nres, Rglist, color='#444444', linestyle='--', marker='.', label='Rg')
    plt.plot(nres, Rgphobiclist, color='#00FF00', linestyle='-', marker='D',  label='Rg,phobic')

    plt.xlabel('Chain Length (number of residues)')
    plt.title('Radius of Gyration of Amino Acids (all vs. hydrophobic) to Number of Residues')
    plt.legend()
    plt.show()
    
    #Plot 2
    plt.plot(nres, RgOverRgphobic, color='#444444', linestyle='--', marker='.')
    plt.xlabel('Chain Length (number of residues)')
    plt.ylabel('Rg/Rg,phobic')
    plt.show() 
