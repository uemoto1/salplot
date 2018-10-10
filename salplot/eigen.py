#!/usr/bin/env python3
import logging
import os

class EigenData():
    
    def __init__(self, sysname, directory=os.curdir):        
        self.sysname = sysname
        self.directory = directory
        self.load()

    def load(self):
        file_eigen = os.path.join(
            self.directory, "%s_eigen.data" % self.sysname
        )
        
        ik, ib, energy_tmp, occup_tmp = np.loadtxt(
            file_eigen, unpack=True, dtype="int,int,float,float"
        ) 
        
        self.nk = np.amax(ik)
        self.nb = np.amax(ib)
        self.energy = energy_tmp.reshape([self.nk, self.nb])
        self.occup = occup_tmp.reshape([self.nk, self.nb])
    
