#!/usr/bin/env python

import gtk
import sys
import subprocess
import keybinder
import pynotify
import pygtk
pygtk.require('2.0')
import cairo


""" Propios """
from interfaz.lib.config     import Configuracion
from interfaz.lib.myNotebook import myNotebook
from interfaz.lib.mySqlite   import mySqlite

""" Clase principal de Interfaz """
class Interfaz:
    """ Constructor """
    def __init__ (self):
        """ Creo el objeto de configuracion """
        configuracion = Configuracion()
        self.diccConfig = {}
        self.diccConfig = configuracion.leer_configuracion()
       
        """ Seteo el tab por defecto """        
        self.tab = int(self.diccConfig["defaulttab"])
        
        """ Le asigno 340 de alto """
        self.yScreen = int(self.diccConfig["yscreen"])

	""" Le asigno la tecla que corresponde para bajar la interfaz """
	self.bindtecla = self.diccConfig["bindtecla"]
       
        """ Creo la ventana """
        self.window = gtk.Window()
        
        """ Centro la ventana """
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_modal(True)
        
        """ Sin decoracion """
        self.window.set_decorated(False)
        
        
        """ Creo el fixed y se lo asigno """
        self.fixed = gtk.Fixed()
        
        """ Se lo asigno a la ventana creada """
        self.window.add (self.fixed)
        
        """ Creo el notebook """
        self.notebook = gtk.Notebook()
        self.notebook.set_tab_pos(gtk.SCROLL_PAGE_UP)
        
        """ Obtengo el tamanio de la ventan """
        screen = self.window.get_screen()
        self.xScreen = screen.get_width()
        		
        self.window.resize(self.xScreen, self.yScreen)
        self.notebook.set_size_request(self.xScreen,self.yScreen)
        
        """ Dejo a la ventana siempre por arriba """
        self.window.set_keep_above(True)
        
        """ Le asigno  el notebook al fixed """
        self.fixed.add(self.notebook)
        
        """ self.tabs es utilizado para la creacion de los distintos tabs """
        self.tabs = []
        self.programas = {"ejecucion":[],"descripcion":[],"pathIcono":[]}
        
        """ Se utilza para la obtencion de los datos de la base de datos """
        self.tabs_datos = []
        self.mi_base = mySqlite("/usr/share/interfaz-1.0/dba/botonera.sqlite")


    """ Creo los Tabs """
    def crearTabs (self):
        """ Recorro los datos obtenidos """
        self.tabs_datos = self.mi_base.obtenerTabs()

        """ De los datos de tabs creo las solapas """        
        for indice in range(0,len(self.tabs_datos["idTabs"])):
            self.tabs.append(myNotebook(self.tabs_datos["nombreTabs"][indice],self.tabs_datos["pathIcono"][indice],self.notebook,self.xScreen,self.yScreen,self.diccConfig))
            
            self.programas=[]
            self.programas = self.mi_base.obtenerProgramas(indice+1)
            
            if len(self.programas) > 0: 
                """ ejecucion
		    descripcion
		    pathIcono
		"""
                for datos in range(0,len(self.programas["ejecucion"])):
                    self.tabs[indice].crearBotones(self.programas["pathIcono"][datos],self.programas["descripcion"][datos],self.programas["ejecucion"][datos],self.onClickListener,self.programas["label"][datos])
    
    
	""" Ejecuta el aplicativo y se oculta la interfaz """
    def onClickListener(self,widget):
        print str(widget.Tag)
        PID = subprocess.Popen(str(widget.Tag).split(' '), shell=False).pid
        self.hide(0,0)

        
    """ Vista principal """
    def main(self):
        """ Oculto todo lo que corresponda a la pantalla """    
        self.window.hide_all()
        self.window.isHide = True
        
        gtk.main()
        
    """ Cerrar ventana """
    def destroy(self,event):
        """ Cierro la base de datos """
        self.mi_base.cerrarBase()
        gtk.main_quit()

    """ ocultarMostrar """
    def ocultarMostrar (self, widget, data=None):
        if(self.window.isHide):
            self.window.move(0,25)
            self.notebook.grab_focus()
            self.window.show_all()
            self.window.isHide = False
            self.notebook.set_current_page(self.tab)
        else:
            self.tab = self.notebook.get_current_page()
            self.window.hide_all()  
            self.window.isHide = True
            
            
    """ hide """
    def hide (self, widget, data=None):           
        self.tab = self.notebook.get_current_page()
        self.window.hide_all()  
        self.window.isHide = True

if __name__ == "__main__":
    interfaz = Interfaz()

    pynotify.init("Proyecto Centrux")
    nota = pynotify.Notification("Huemul - GNU/Linux Forense", message="Al pulsar "+interfaz.bindtecla+" se desplegara la barra de accesos rapidos", icon="emblem-debian")
    nota.set_timeout(5000)
    nota.show()
    
    interfaz.crearTabs()
    keystr = interfaz.bindtecla
    keybinder.bind(keystr, interfaz.ocultarMostrar, "None")
    
    keystr = "<Ctrl>e"
    keybinder.bind(keystr, interfaz.hide, "None")

    interfaz.window.show_all()
    interfaz.window.hide_all()  
    
    interfaz.main()
