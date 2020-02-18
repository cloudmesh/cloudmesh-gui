import PySimpleGUI as gui
from cloudmesh.common.console import Console
from cloudmesh.configuration.Config import Config
from cloudmesh.common.FlatDict import FlatDict

gui.theme('SystemDefault1')

class Gui(object):

    @staticmethod
    def edit(key, caps=True, show=False):
        config = Config()

        entry = dict(FlatDict(config[key], sep='.'))

        layout = [
            [gui.Text(f'Cloudmesh Configuration Editor: {key}')]
        ]

        length = 1
        for _key, _value in entry.items():
            length = max(length, len(_key))

        length = length + 3

        for _key, _value in entry.items():
            if caps:
                label = _key.capitalize()
            else:
                label = _key

            secrets = Config.secrets()

            if _key in secrets and not show:
                field = [gui.Text(label, size=(length, 1)),
                         gui.InputText(key=f"{key}.{_key}",
                                       password_char="*",
                                       default_text=_value)]
            else:
                field = [gui.Text(label, size=(length, 1)),
                         gui.InputText(key=f"{key}.{_key}",
                                       default_text=_value)]
            layout.append(field)

        layout.append([gui.Submit(), gui.Cancel()])

        window = gui.Window('Cloudmesh Configuration Editor',
                            layout,
                            background_color="white"
                            )
        event, values = window.Read()
        window.Close()

        if event == "Submit":
            for _key, _value in values.items():
                config[_key] = _value
                if show:
                    Console.ok(f"{_key}={_value}")
            config.save()
        else:
            print (event)

    @staticmethod
    def edit_list(keys, caps=True, show=False):
        config = Config()


        layout = [
            [gui.Text(f'Cloudmesh Configuration Editor')]
        ]

        length = 1
        for _key in keys:
            length = max(length, len(_key))

        length = length + 3

        for _key in keys:
            _value = config[_key]
            if caps:
                label = _key.capitalize()
            else:
                label = _key

            secrets = Config.secrets()

            if _key.rsplit(".", 1)[1] in secrets and not show:
                field = [gui.Text(label, size=(length, 1)),
                         gui.InputText(key=f"{_key}",
                                       password_char="*",
                                       default_text=_value)]
            else:
                field = [gui.Text(label, size=(length, 1)),
                         gui.InputText(key=f"{_key}",
                                       default_text=_value)]
            layout.append(field)

        layout.append([gui.Submit(), gui.Cancel()])

        window = gui.Window('Cloudmesh Configuration Editor',
                            layout,
                            background_color="white"
                            )
        event, values = window.Read()
        window.Close()

        if event == "Submit":
            for _key, _value in values.items():
                config[_key] = _value
                if show:
                    Console.ok(f"{_key}={_value}")
            config.save()
        else:
            print (event)



    @staticmethod
    def activate():
        config = Config()
        clouds = list(config["cloudmesh.cloud"].keys())

        gui.SetOptions(text_justification='right')

        layout = [
            [gui.Text('Cloudmesh Cloud Activation',
                      font=('Helvetica', 16))],
            [gui.Text('Compute Services')]]

        layout.append([gui.Text('_' * 100, size=(65, 1))])

        for cloud in clouds:
            tbd = "TBD" in str(config[f"cloudmesh.cloud.{cloud}.credentials"])
            active = config[f"cloudmesh.cloud.{cloud}.cm.active"]
            if tbd:
                color = 'red'
            else:
                color = "green"

            choice = [gui.Checkbox(cloud,
                                   key=cloud,
                                   text_color=color,
                                   default=active)]
            layout.append(choice)

        layout.append([gui.Text('_' * 100, size=(65, 1))])

        layout.append([gui.Submit(), gui.Cancel()])

        window = gui.Window('Cloudmesh Configuration',
                            layout,
                            font=("Helvetica", 12))

        event, values = window.Read()

        if event == "Submit":
            for cloud in values:

                active = values[cloud] or False
                config[f"cloudmesh.cloud.{cloud}.cm.active"] = str(active)
                if active:
                    Console.ok(f"Cloud {cloud} is active")

            config.save()
        else:
            print (event)
