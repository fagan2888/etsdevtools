#-------------------------------------------------------------------------------
#  
#  Package initialization for the Gotcha! Python profiling tool.
#  
#  Written by: David C. Morrill
#  
#  Date: 07/30/2003
#  
#  (c) Copyright 2003 by Enthought, Inc. 
#  
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from hotshot import Profile

import os
import os.path

#-------------------------------------------------------------------------------
#  Global Values:
#-------------------------------------------------------------------------------

profiler = None

#-------------------------------------------------------------------------------
#  Find the newest 'gotcha' profile in a specified directory:
#-------------------------------------------------------------------------------

def find_profile ( create = True, path = None ):
    if path is None:
        path = os.getcwd()
    highest = 0
    for file in os.listdir( path ):
        if (file[:7] == 'gotcha_') and (file[-5:] == '.prof'):
            try:
                highest = max( highest, int( file[7:-5] ) )
            except:
                pass
    if create:
        highest += 1
    return os.path.join( path, 'gotcha_%d.prof' % highest )

#-------------------------------------------------------------------------------
#  Begin profiling:
#-------------------------------------------------------------------------------

def begin_profiling ( ):
    global profiler, profile_name
    if profiler is None:
        profile_name = find_profile()
        profiler = Profile( profile_name )
       
#-------------------------------------------------------------------------------
#  End profiling:
#-------------------------------------------------------------------------------

def end_profiling ( ):
    global profiler
    if profiler is not None:
        profiler.close()
        profiler = None
    
#-------------------------------------------------------------------------------
#  Profile a specified function (if profiling is active):
#-------------------------------------------------------------------------------

def profile ( func, *args, **keywords ):
    global profiler
    if profiler is None:
        return apply( func, args, keywords )
    else:
        return profiler.runcall( func, *args, **keywords )

def stats(num_funcs = 20):
    import hotshot, hotshot.stats
    stats = hotshot.stats.load(profile_name)
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(num_funcs)
    return stats