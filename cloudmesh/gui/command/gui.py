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
                gui profile
                gui mongo [user]
                gui cloud CLOUD [--show]
                gui edit KEY [--show]


          This command allows configuration of cloudmesh with a GUI

          Options:
              -f      specify the file
              --show  shows also the password
        """

        arguments.show = arguments["--show"]

        if arguments.activate:
            Gui.activate()

        elif arguments.profile:
            Gui.edit("cloudmesh.profile")


        elif arguments.mongo and arguments.user:
            Gui.edit_list(["cloudmesh.data.mongo.MONGO_USERNAME",
                           "cloudmesh.data.mongo.MONGO_PASSWORD"],
                     caps=False,
                     show=arguments.show)

        elif arguments.mongo:
            Gui.edit(f"cloudmesh.data.mongo",
                     caps=False,
                     show=arguments.show)

        elif arguments.cloud:
            cloud = arguments.CLOUD
            Gui.edit(f"cloudmesh.cloud.{cloud}.credentials",
                     caps=False,
                     show=arguments.show)

        elif arguments.edit:
            key = arguments.KEY
            if not key.startswith("cloudmesh."):
                key = "cloudmesh." + key
            Gui.edit(key, caps=False, show=arguments.show)

        return ""
