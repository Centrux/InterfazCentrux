#!/usr/bin/python
import os
import sys
import ConfigParser

class Configuracion:

    def __init__(self):
        # Error : el filesystem %s de espacio libre %.2f es menor que %.2
        # Indico el directorio de configuracion
        #
        # os.getcwd() - obtengo el directorio actual.
        #
        self.CONF_DIR = '/usr/share/interfaz-1.0/conf'
        #self.CONF_DIR = os.path.join(os.getcwd(),'conf')
        
        #
        # Nombre del archivo de configuracion
        #
        self.ARCHIVO_CONFIG = self.CONF_DIR + '/config.conf'
        
        self.verificar_archivo()
    #
    # Verifico si existe el directorio y el archivo
    # si no es asi los creo y tambien creo un archivo
    # de configuracion basica.
    #
    def verificar_archivo(self):
        
        #
        # Verifico si no existe el directorio
        #
        if not os.path.exists(self.CONF_DIR):
            
            #
            # Trato de crear el directorio
            #
            try:
                #
                # con makedirs crea el directorio padre e hijo
                #
                # con mkdir solo crea el hijo
                #
                os.makedirs(self.CONF_DIR)
            except Exception, err:
                print err
                exit(1)
        
        
        #
        # Verifico si existe el archivo de configuracion
        #
        self.config = ConfigParser.ConfigParser()
    
        if not os.path.isfile(self.ARCHIVO_CONFIG):
#            try:
                #
                # Copio el archivo existente en /usr/share/espacio/conf utilizando
                # shutil ya que os no tiene para copiar archivos.
                #
#                shutil.copy('/usr/share/espacio/conf/config.conf', os.path.join(self.CONF_DIR,'/config.conf'))
#            except Exception, err:
#                print err
#                print "Se procede a crear el archivo por defecto."
                
            #
            # Creo el archivo por defecto
            #
            try:
                self.config.add_section('PATH')
                self.config.set('PATH','path_raiz','/opt/interfaz')
                self.config.set('PATH','path_iconos','/iconos')
                self.config.set('PATH','path_imagenes','/imagenes')
                
        
        
                self.config.add_section('IMAGENES')
                self.config.set('IMAGENES','logo','/imagenes/centrux.png')
                
                self.config.add_section('APARIENCIA')
                self.config.set('APARIENCIA','yScreen','340')     
                self.config.set('APARIENCIA','sizeIconoX','100')     
                self.config.set('APARIENCIA','sizeIconoY','60')                               
                self.config.set('APARIENCIA','sizeEspaciadoIconosX','10')     
                self.config.set('APARIENCIA','sizeEspaciadoIconosY','30')     
                
        
                fd = open(self.ARCHIVO_CONFIG,'w')
                self.config.write(fd)
            except Exception, err:
                    print err
                    exit (1)
    def leer_configuracion(self):
        #
        # Tomo el archivo de configuracion.
        # y lo abro como solo lectura y cargo los datos
        # necesario para trabajar.
        #
        self.config.read(self.ARCHIVO_CONFIG)
        
        #
        # Guardo todo los datos en un
        # diccionario y lo devuelvo
        #
        self.diccionario = {}
        for valores in self.config.options('PATH'):
            self.diccionario[valores] = self.config.get('PATH',valores)
    
        for valores in self.config.options('IMAGENES'):
            self.diccionario[valores] = self.config.get('IMAGENES',valores)
            
        for valores in self.config.options('APARIENCIA'):
            self.diccionario[valores] = self.config.get('APARIENCIA',valores)
    
    
        return (self.diccionario)
