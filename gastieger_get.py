#!/usr/bin/env python2

import sys
import pybel


def get_charges(mol):

    return [atom.partialcharge for atom in mol]


def write_xyz(coords, atomtypes, filename):

    output = "%i\n\n" % len(atomtypes)
    
    for i, atom in atomtypes:
        output += "%s %f %f %f\n" %(atom, coords[i][0],  coords[i][1], coords[i][2])

    f = open(filename, "w")
    f.write(output)
    f.close()

    
def mol_from_coords(coordinates, atomtypes):

    temp_xyz = "temp.xyz"
    write_xyz(coordinatess, atomtypes, temp_xyz)
    mol = pybel.readfile("xyz", temp_xyz).next()

    return mol
    

if __name__ == "__main__":

    filename = sys.argv[1]
    extension = filename[-3:]

    print filename, extension
    mol = pybel.readfile(extension, filename).next()

    print get_charges(mol)
