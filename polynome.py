# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:57:40 2021

@author: Razer Blade
"""

from monome import Monome

class Polynome:
    def __init__(self, tete=None):
        """
        constructeur permet d'initialiser l'objet de type Polynome       
        Attributs
        ----------
        tete : Monome

        Returns
        -------
        None.

        """
        self.tete = tete # est de type Monome
        
    def getTete(self):
        """
        retourne le monome tete
        Returns
        -------
        Monome

        """
        return self.tete
    
    def setTete(self, t):
        """
        permet de modifier le monome tete
        Parameters
        ----------
        t : Monome

        Returns
        -------
        Polynome

        """
        self.tete = t
        return self
    
    def est_vide(self):
        """
        permet de verifier si le polynome est vide ou non
        Returns
        -------
        bool
        Retourne True si le polynome est vide
        Retourne False sinon

        """
        return self.getTete() == None
    
    def localiser(self, m):
        """
        localiser où situer convenablement un monome de même degré que m dans le polynome courant.
        Parameters
        ----------
        m : Monome
            monome à situer dans le polynome appelant.
        Returns
        -------
        Monome.
        """
        p = self.getTete()
        while p :
            suivant = p.getSuivant()
            if p.getSuivant() == None :
                return p          
            if suivant.getDeg() <= m.getDeg():
                if m.getDeg() == p.getSuivant().getDeg():
                    return p.getSuivant()
                return p  
            p = p.getSuivant()

    
    def dernier(self):
        """
        retourner le dernier Monome du Polynome
        Returns
        -------
        p : Monome

        """
        p = self.getTete()
        while p.getSuivant() != None:
            p = p.getSuivant()
        return p
    
    def ajouter(self, m):
        """
        inserer un nouveau monome convenablement dans le polynome courant.
        Parameters
        ----------
        m : Monome
            monome à inserer dans le polynome appelant.  
        """
        x= self.localiser(m)  
        if self.est_vide():
            self.setTete(m)   
        elif x == self.getTete():
            m.setSuivant(self.getTete())
            self.setTete(m)
        elif x.getDeg() == m.getDeg():
            x.setCoef(x.getCoef()+ m.getCoef()) 
        else:
            m.setSuivant(x.suivant)
            x.setSuivant(m)
            
    def __str__(self):
        """
        Returns
        -------
        s : str
            la representation str du polynome
        """
        s = ''
        p = self.getTete()
        while p != None :
            if p.getSuivant() == None :
                s = s+str(p)
            else : 
                s = s+str(p) + ' + '
            p = p.getSuivant()        
        return s
     
    def ajouter_plusieur(self, *ms):
        for m in ms:
            self.ajouter(m)
            

        
        
    
        
        
        
    
        