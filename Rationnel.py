# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:44:56 2021

@author: hdafa
"""

class Rationnel:
    
    # constructeur
    def __init__(self, numer, denom):
        assert denom != 0
        self.numer = numer
        self.denom = denom
        
    # accesseurs
    def getNumer(self):
        return self.numer
    
    def setNumer(self, val):
        self.numer = val
        #return self
        
    def getDenom(self):
        return self.denom
        
    def setDenom(self, val):
        assert val != 0
        self.denom = val
        #return self
    
    # to string
    def __str__(self):
        return str(self.getNumer()) +'/'+ str(self.getDenom())
    
    # simplification
    
    @staticmethod
    def pgcd(a, b):
        while b!= 0:
            r = a%b
            a, b = b, r
        return a
    
    def simplifier(self):
        h = Rationnel.pgcd(self.getNumer(), self.getDenom())
        if h != 1:
            self.setNumer(self.getNumer() // h)
            self.setDenom(self.getDenom() // h)
        return self
    
    # arithmetiques : +, *, -, /
    def __add__(self, r):
        return Rationnel(
            self.getNumer() * r.getDenom() + r.getNumer() * self.getDenom(),
            self.getDenom() * r.getDenom()).simplifier()
    
    @staticmethod
    def oppose(a):
        return -a
    
    def __sub__(self, r):
        autre = Rationnel(Rationnel.oppose(r.getNumer()), r.getDenom())
        return (self + autre).simplifier()
        # return self.__add__(autre)
    
    def __mul__(self, r):
        return Rationnel(
            self.getNumer() * r.getNumer(),
            self.getDenom() * r.getDenom()).simplifier()
    
    def __invert__(self):
        return Rationnel(self.getDenom(), self.getNumer())
    
    def __floordiv__(self, r):
        x = self * (~r)
        return x.simplifier()
    
    # cast
    def __int__(self):
        return int(self.getNumer()/self.getDenom())
    
    def __float__(self):
        return float(self.getNumer()/self.getDenom())

    
    
    