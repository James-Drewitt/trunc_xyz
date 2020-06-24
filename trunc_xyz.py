# AUTHOR: Dr James W E Drewitt
# Copyright 2020, James Drewitt
# james.drewitt@bristol.ac.uk; james.drewitt@gmail.com

inp1 = raw_input('Input File? (*.xyz): ')
frac = raw_input('Size of truncation (%): ')
#
#Read xyz file
print ' reading file',inp1,'....' 
#
f = open(inp1,'r')
data_list = f.readlines()
f.close()#close input xyz file
#
#number of atoms
#
s1 = data_list[0]
natoms = int(s1)
#
#determine number of iterations
#
numiter = len(data_list)
numiter = int(numiter)
niter = numiter / (natoms+2)
#
#determine how many lines to truncate
#
trunc = int((float(frac)/100)*niter*(natoms+2))
trunciter = trunc / (natoms+2)
print '\n there are',natoms,'atoms and',niter,'iterations\n truncating the first'\
        ,trunciter,'iterations (',trunc,'lines from total',numiter,')...'
del data_list[0:trunc]
#
#write new output
#
print ' writing file out.xyz ...'
fout = open('out.xyz','w')
fout.writelines(data_list)
fout.close()

