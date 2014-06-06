#!/usr/bin/env python

import sys
import sqlite3

class mySqlite:
    """ Constructor le paso el nombre de la base de datos """
    def __init__ (self,baseDatos):
        self.con = None
        self.tabs = {"nombreTabs":[],"idTabs":[],"pathIcono":[]}
        self.programas = {"ejecucion":[],"descripcion":[],"pathIcono":[]}
        
        """ Realizo la conexion de la base de datos"""
        try:
            self.con = sqlite3.connect(baseDatos)
            self.cursor = self.con.cursor()
        except sqlite3.Error, e:
            print "Error : %s" % e.args[0]
            sys.exit(1)


    """ Devuelvo la informacion de los tabs en un
        diccionario
    """
    def obtenerTabs(self):
        try:
            self.cursor.execute ("SELECT idTabs,nombre,pathIcono FROM tabs ORDER BY idTabs")
            self.datos = self.cursor.fetchall()
        except sqlite3.Error, e:
            print "Error al acceder a los datos: %s" % e.args[0]
            sys.exit(1)
            
        for datos in self.datos:
            self.tabs["idTabs"].append(datos[0])
            self.tabs["nombreTabs"].append(datos[1])
            self.tabs["pathIcono"].append(datos[2])

        return self.tabs


    """ Devuelvo la informacion de los tabs en un
        diccionario
    """
    def obtenerProgramas(self,id):
        sql="SELECT ejecucion,descripcion,pathIcono,label FROM programas WHERE idTabs=%d ORDER BY idTabs,idProgramas" % (id)
        
        self.programas = {"ejecucion":[],"descripcion":[],"pathIcono":[],"label":[]}
        try:
            self.cursor.execute (sql)
            self.datos = self.cursor.fetchall()
        
        except sqlite3.Error, e:
            print "Error al acceder a los datos: %s" % e.args[0]
            sys.exit(1)
        
        #print self.datos
        
        if len(self.datos) > 0:
                for datos in self.datos:
                    self.programas["ejecucion"].append(datos[0])
                    self.programas["descripcion"].append(datos[1])                           
                    self.programas["pathIcono"].append(datos[2])
                    self.programas["label"].append(datos[3])
    
                return self.programas
    
        else:
                return []

            
    """ Cierro la base de datos """
    def cerrarBase(self):
        self.con.close()
