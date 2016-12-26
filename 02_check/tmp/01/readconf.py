import ConfigParser

config = ConfigParser.ConfigParser()
# config = ConfigParser.ConfigParser()

config.read("G:\\05_pypro\\01\\1.conf")
# onfig.read("G:\\05_pypro\\01\\test.conf")
sections = config.sections()
# sections = config.sections()
print sections
# print sections
#! /usr/bin/env python
#coding=utf-8
# import ConfigParser
#
# config = ConfigParser.ConfigParser()
# config.read("odbc.ini")
#
# sections = config.sections()
# print sections
# print dir(config)

# ['OPTCRE', 'OPTCRE_NV', 'SECTCRE', '_KEYCRE', '__doc__', '__init__', '__module__', '_boolean_states', '_defaults',
# '_dict', '_get', '_interpolate', '_interpolation_replace', '_optcre', '_read', '_sections', 'add_section',
# 'defaults', 'get', 'getboolean', 'getfloat', 'getint', 'has_option', 'has_section', 'items', 'options', 'optionxform',
# 'read', 'readfp', 'remove_option', 'remove_section', 'sections', 'set', 'write']
# print help(confdig.options)
options = config.options('db')
print options
value_c = config.items('db')
print value_c
v1 = config.get('db', 'db_port')
print v1
