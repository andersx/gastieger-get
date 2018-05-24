#!/usr/bin/env python2

import sys
import pybel


def get_charges(mol):

    return [atom.partialcharge for atom in mol]


def mol_from_coords(coordinates, atomtypes):

    temp_xyz = "%i\n\n" % len(atomtypes)
    
    for i, atom in atomtypes:
        temp_xyz += "%s %f %f %f\n" %(atom, coords[i][0],  coords[i][1], coords[i][2])

    mol = pybel.readstring("xyz", temp_xyz).next()

    return mol
    

if __name__ == "__main__":

    filename = sys.argv[1]
    extension = filename[-3:]

    print filename, extension
    mol = pybel.readfile(extension, filename).next()

    print get_charges(mol)
