#-------------------------------------------------------------------------------
#
#  Useful functions.
#
#  Written by: David C. Morrill
#
#  Date: 08/11/2006
#
#  (c) Copyright 2006 by David C. Morrill
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

import sys

#-------------------------------------------------------------------------------
#  Truncates a specified string at a maximum specified length:
#-------------------------------------------------------------------------------

def truncate ( s, n = 80 ):
    if len( s ) >= n:
        return s

    return '%s...%s' % ( s[ :(n - 2)/2 ], s[ -(n/2): ] )

#-------------------------------------------------------------------------------
#  Attempts to import a specified module:
#-------------------------------------------------------------------------------

def import_module ( module_name ):
    """ Attempts to import a specified module.
    """
    module = sys.modules.get( module_name )
    if module is not None:
        return module

    try:
        module     = __import__( module_name )
        components = module_name.split( '.' )
        for component in components[1:]:
            module = getattr( module, component )

        return module
    except:
        pass

    return None

#-------------------------------------------------------------------------------
#  Attempts to import a specified symbol from a specified module:
#-------------------------------------------------------------------------------

def import_symbol ( symbol_name ):
    """ Attempts to import a specified symbol from a specified module.
    """
    components = module_name.split( '.' )
    try:
        return getattr( import_module( '.'.join( components[:-1] ) ),
                        components[-1], None )
    except:
        return None

