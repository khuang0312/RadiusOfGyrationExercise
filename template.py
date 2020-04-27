#!/usr/bin/env python

import glob
from numpy import *
import os
import pylab as pp

def ReadPdb( PdbFile ):
    """Reads a PDB file with a name provided in the argument. 
       Assumes the PDB file contains only ATOM and TER entries; TER entries are skipped.
       
       RETURNS:
        - Pos, an (Nx3) dimensional NumPy array of positions of alpha carbons
        - ResNames, a list of residue names.
    """

    #ENTER YOUR CODE TO GET Pos, ResNames here. Manipulate them until you get them in the required format, then use the return statement below to return these... 


    #Return
    return Pos, ResNames


def ResHydrophobic( ResNames ):
    """Take list of three letter codes for residue names; 
       returns a list, IsPhobic, of True/False values 
       depending on whether residues are hydrophobic or not."""

    #Enter your code to identify whether residues or hydrophobic or not here. Use the return statement below to return them.

    return IsPhobic


def RadiusOfGyration( Pos ):
    """Take an Nx3 dimensional array of positions; return the radius of gyration."""

    #Enter your code to compute the radius of gyration here. Use the return statement below to return it. 

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




    #ONCE YOU ARE DONE LOOKING AT ALL PDB FILES, YOU WANT TO MAKE SOME PLOTS. 
