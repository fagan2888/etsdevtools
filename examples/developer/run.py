#-------------------------------------------------------------------------------
#
#  Starts the Envisage environment.
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

import sys

from envisage.ui.workbench.api import WorkbenchApplication
from envisage.core_plugin import CorePlugin
from envisage.ui.workbench.workbench_plugin import \
         WorkbenchPlugin
from envisage.plugins.python_shell.python_shell_plugin import \
         PythonShellPlugin

# Enthought developer tool plugins:
from etsdevtools.developer.developer_plugin import EnthoughtDeveloperPlugin
from etsdevtools.developer.tools.fbi_plugin import FBIPlugin
from etsdevtools.developer.helper.fbi \
    import enable_fbi

#-------------------------------------------------------------------------------
#  Application entry point:
#-------------------------------------------------------------------------------

if __name__ == '__main__':

    # FIXME: Need to remove this. This is not necessary as the FBI plugin
    # calls enable_fbi.
    # Allow the FBI to handle any exceptions that occur:
    # enable_fbi()

    # Create an Envisage application:
    application = WorkbenchApplication(
        plugins = [CorePlugin(), WorkbenchPlugin(), PythonShellPlugin(),
                   EnthoughtDeveloperPlugin(),
                   FBIPlugin()
                   ],
        argv               = sys.argv,
        id                 = 'Enthought Developer Tools',
        requires_gui       = True
    )

    # Run the application
    application.run()
