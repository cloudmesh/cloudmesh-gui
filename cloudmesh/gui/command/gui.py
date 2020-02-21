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
                gui quick


          This command allows configuration of cloudmesh with a GUI

          Options:
              -f      specify the file
              --show  shows also the password

          Description:
                gui activate

                  activates clouds by selecting them

                gui profile

                  lets you fill out the profile

                gui mongo [user]

                  lets you fill out the mongo information

                gui cloud CLOUD [--show]

                  lets you fill out the specific cloud

                gui edit KEY [--show]

                  lets you fill out any data identified by the Key in the yaml
                  file in dot notation

                gui quicke

                  lets you fill out a combination that is good enough to get
                  you started in class (this is experiemental)

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


        elif arguments.quick:
            Gui.edit_list([
                "cloudmesh.profile.firstname",
                "cloudmesh.profile.lastname",
                "cloudmesh.profile.email",
                "cloudmesh.profile.user",
                "cloudmesh.profile.github",
                "cloudmesh.data.mongo.MONGO_USERNAME",
                "cloudmesh.data.mongo.MONGO_PASSWORD",
                "cloudmesh.data.mongo.MODE",
                "cloudmesh.cloud.chameleon.credentials.auth.username",
                "cloudmesh.cloud.chameleon.credentials.auth.password",
            ],
            caps=False,
            show=arguments.show)

        return ""
