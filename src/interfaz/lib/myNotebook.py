#!/usr/bin/env python

import gtk

""" Clase principal de Interfaz """
class myNotebook:

    """ Constructor """
    def __init__ (self,titulo,icono,widget,xScreen,yScreen,diccConfig):
        self.cantidad = 0
        self.x = 10
        self.y = 10
        
        self.xScreen = xScreen
        self.yScreen = yScreen
        
        """ Calculo cantidad de iconos """       
        self.sizeIconoX = int(diccConfig["sizeiconox"])
        self.sizeIconoY = int(diccConfig["sizeiconoy"])       
        self.sizeEspaciadoIconosX = int(diccConfig["sizeespaciadoiconosx"])
        self.sizeEspaciadoIconosY = int(diccConfig["sizeespaciadoiconosy"])
        
        self.cantidadPorLinea = int(self.xScreen / (self.sizeIconoX + self.sizeEspaciadoIconosX)) - 1 

        """ Genero un hbox y le agrego el label """
        self.hbox = gtk.HBox(False,0)
        
        """ Genero el label que sera el nombre del tabs. """
        self.label = gtk.Label(titulo)
        
        """ Imagen X para poder luego cerrar es parte del boton """
        imagen =  gtk.image_new_from_file("/usr/share/interfaz-1.0/"+icono)
   
        """ Creo el boton con el grafico del icono del tabs """
        self.boton = gtk.Button()
        self.boton.add(imagen)
        
        """ Muestro primero el icono y luego la etiqueta """
        self.hbox.pack_start(self.boton,False,False)
        self.hbox.pack_start(self.label)

        """ Le cambio el estilo al boton para que no tenga
            echo un recuadro.
        """
        style = gtk.RcStyle()
        style.xthickness = 0
        style.ythickness = 0
        self.boton.modify_style(style)
        
        self.hbox.show_all()
        
        """ Agrego un fixed para luego colocar los datos en el fixed2 donde
            pondremos los botones como imagenes
        """
        self.fixed = gtk.Fixed()
        
        """ Inserta a la izquierda """
        widget.append_page(self.fixed,self.hbox)
        
        """ Creo la imagen del Logo """
        self.logoCentrux =  gtk.Image()
        self.logoCentrux.set_from_file("/usr/share/interfaz-1.0/imagenes/centrux.png")
        """ Incorporo Imagen Logo """                    
        self.fixed.put(self.logoCentrux,self.xScreen - 500 ,self.yScreen - 110)
        
    """ crearBotones
    
        Parametros :
            - grafico         = Nombre del grafico del boton.
            - descripcion     = Descripcion cuando uno se apoyoa el mouse sobre el boton.
            - ejecutar        = La aplicacion que ejecuta con el path completo.
            - onClickListener = Nombre de la funcion cuando realiza el click en el boton.
            - textoLabel      = Texto del programa que se muestra debajo del boton.
    """
    def crearBotones (self,grafico,descripcion,ejecutar,onClickListener,textoLabel):
        self.botonNuevo = gtk.Button()
        self.botonNuevo.set_tooltip_text(descripcion)
        self.botonNuevo.set_border_width(0)
        self.botonNuevo.set_relief(gtk.RELIEF_NONE)

        self.imagen     = gtk.Image()
        self.imagen.set_from_file("/usr/share/interfaz-1.0/imagenes/"+grafico)
        
        label = gtk.Label(str)
        label.set_size_request(self.sizeIconoX,self.sizeEspaciadoIconosY/2)
        
        label.set_text(textoLabel)
        
        label.set_justify(gtk.JUSTIFY_CENTER)
        
        """ Agrego un nuevo dato al objeto boton TAG """
        self.botonNuevo.Tag = ejecutar
        self.botonNuevo.connect("clicked", onClickListener)
        
        self.botonNuevo.add (self.imagen)
        self.botonNuevo.set_size_request(self.sizeIconoX,self.sizeIconoY)
        self.botonNuevo.show()
        
        self.cantidad = self.cantidad + 1
        
        if ( self.cantidad > self.cantidadPorLinea ):
            self.x = self.sizeEspaciadoIconosX
            self.y = self.y + self.sizeIconoY + self.sizeEspaciadoIconosY
            self.cantidad = 1
            
        elif ( self.cantidad > 1 and self.cantidad <= self.cantidadPorLinea):
            self.x = self.x + self.sizeIconoX + self.sizeEspaciadoIconosX
        else:
            self.x = self.sizeEspaciadoIconosX

        """ Lo incorporo """            
        self.fixed.put(self.botonNuevo,self.x,self.y)
        self.fixed.put(label,self.x,self.y + self.sizeIconoY + 5)
