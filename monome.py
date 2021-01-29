# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:56:43 2021

@author: Razer Blade
"""

class Monome:
    def __init__(self, coef, deg, suivant=None):
        """
        constructeur permet d'initialiser l'objet de type Monome
        Attributs
        ----------
        coef : float
        deg : int
        suivant : Monome, optional(The default is None.)
                permet d'indiquer le monome suivant
        Returns
        -------
        None.

        """
        # donnée :
        self.coef = coef # de type float
        self.deg = deg # de type int
        # une reference vers le prochain monome (par défault None)
        self.suivant = suivant # de type Monome
        
    def getCoef(self):
        """
        Returns
        -------
        coefficient
            retourner la valeur du coefficient

        """
        return self.coef
    
    def setCoef(self, val):
        """
        il permet de changer la valeur du coefficient
        Parameters
        ----------
        val : float
        
        Returns
        -------
        Monome
            retourne le monome modifié

        """
        self.coef = val
        return self
    
    def getDeg(self):
        """
        Returns
        -------
        degrée
            retourner la valeur du degré
        """
        return self.deg
    
    def setDeg(self, val):
        """
        il permet de changer la valeur du degré
        Parameters
        ----------
        val : int

        Returns
        -------
        degrée
            retourne le monome modifié

        """
        self.deg = val
        return self
    
    def getSuivant(self):
        """
        Returns
        -------
        Monome
            retourne le monome suivant

        """
        return self.suivant
    
    def setSuivant(self, m):
        """
        modifier le monome suivant
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne le monome dont on a modifié le suivant

        """
        self.suivant = m
        return self
    
    def __str__(self):
        """
        Returns
        -------
        str
            retourne la representation str du monome

        """
        return str(self.getCoef()) + 'X^' + str(self.getDeg())
    
    def __mul__(self, m):
        """
        operateur qui permet de realiser la multilication de deux monomes
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne le monome qui est le resultat de la multiplication des 2 monomes

        """
        return Monome(self.getCoef() * m.getCoef(), self.getDeg()+m.getDeg())
    
    def __add__(self, m):
        """
        operateur qui permet de realiser l'addition de deux monomes
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne le monome qui est le resultat de l'addition des 2 monomes

        """
        assert self.getDeg() == m.getDeg()
        return Monome(self.getCoef() + m.getCoef(), self.getDeg())
    
    def __sub__(self, m):
        """
        operateur qui permet de realiser la soustraction de deux monomes
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne le monome qui est le resultat de la soustraction des 2 monomes

        """       
        assert self.getDeg() == m.getDeg()
        return Monome(self.getCoef() - m.getCoef(), self.getDeg())
    
    def __truediv__(self, m):
        """
        operateur qui permet de realiser la division de deux monome
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne le monome qui est le resultat de la division des 2 monomes

        """       
        assert m.getCoef() != 0
        assert self.getDeg() - m.getDeg() >= 0
        return Monome(self.getCoef() / m.getCoef(), self.getDeg()-m.getDeg()  )
    
    
    @staticmethod
    def deriver(m):
        """
        methode static permet de deriver un monome m
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne la derivée du monome m

        """
        return Monome(m.getCoef()*m.getDeg(),m.getDeg()-1)
    
    @staticmethod
    def primitive(m):
        """
        methode static permet de donner la primitive du monome m
        Parameters
        ----------
        m : Monome
            
        Returns
        -------
        Monome
            retourne la primitive du monome m

        """        
        return Monome(m.getCoef()/m.getDeg()+1,m.getDeg()+1)
    
    
    