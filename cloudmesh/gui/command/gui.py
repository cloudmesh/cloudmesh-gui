from __future__ import print_function

from cloudmesh.gui.Gui import Gui
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command


class GuiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_gui(self, args, arguments):
        """
        ::

          Usage:
                gui activate

          This command allows configuration of cloudmesh with a GUI

          Options:
              -f      specify the file

        """

        if arguments.activate:
            Gui.activate()

        return ""
