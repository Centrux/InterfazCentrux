#!/usr/bin/env python

import os
import glob
from distutils.core import setup

logos=[( 'share/interfaz-1.0/iconos', glob.glob('config/iconos/*'))]
imagenes=[
	  ('share/interfaz-1.0/imagenes/',             glob.glob('config/imagenes/*.png')),
	  ('share/interfaz-1.0/imagenes/accesorios',   glob.glob('config/imagenes/accesorios/*.png')),
	  ('share/interfaz-1.0/imagenes/desarrollo',   glob.glob('config/imagenes/desarrollo/*.png')),
	  ('share/interfaz-1.0/imagenes/graficos',     glob.glob('config/imagenes/graficos/*.png')),
	  ('share/interfaz-1.0/imagenes/internet',     glob.glob('config/imagenes/internet/*.png')),
	  ('share/interfaz-1.0/imagenes/preferencias', glob.glob('config/imagenes/preferencias/*.png'))
]

dba=[('share/interfaz-1.0/dba',['config/dba/botonera.sqlite'])]
config=[('share/interfaz-1.0/conf',['config/conf/config.conf'])]
data = logos + imagenes + dba + config

setup(name='Interfaz',
	version='1.0',
	description='Interfaz sencilla de aplicaciones rapidas',
	long_description='Interfaz de acceso rapido a los programas',
	author='Marcos Pablo Russo',
	author_email='mrusso@centrux.org',
	maintainer='Marcos Pablo Russo',
	maintainer_email='mrusso@centrux.org',
	url='http://www.centrux.org',
	download_url='http://www.centrux.org/repositorio/python/interfaz-1.0.tar.bz2',
	platforms=['i386','AMD64'],
	license='GPL',
	package_dir={'':'src'},
	packages=['interfaz','interfaz.lib'],
	data_files = data,
	requires=['gtk','pygtk']
)
