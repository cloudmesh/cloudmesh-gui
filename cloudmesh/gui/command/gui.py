from __future__ import print_function

from pprint import pprint

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
                gui profile
                gui cloud CLOUD

          This command allows configuration of cloudmesh with a GUI

          Options:
              -f      specify the file

        """

        if arguments.activate:
            Gui.activate()

        if arguments.profile:
            Gui.edit("cloudmesh.profile")

        if arguments.cloud:
            cloud = arguments.CLOUD
            Gui.edit(f"cloudmesh.cloud.{cloud}.credentials", caps=False)

        return ""
