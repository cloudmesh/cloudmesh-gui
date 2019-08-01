import PySimpleGUI as gui
from cloudmesh.common.console import Console
from cloudmesh.configuration.Config import Config


class Gui(object):

    @staticmethod
    def edit(key, caps=True):
        config = Config()

        entry = config[key]

        layout = [
            [gui.Text(f'Cloudmesh Configuration Editor: {key}')]
        ]

        for _key, _value in entry.items():
            if caps:
                label = _key.capitalize()
            else:
                label = _key

            field = [gui.Text(label, size=(15, 1)), gui.InputText(key=f"{key}.{_key}", default_text=_value)]
            layout.append(field)

        layout.append([gui.Submit(), gui.Cancel()])

        window = gui.Window('Cloudmesh Configuration Editor', layout)
        event, values = window.Read()
        window.Close()

        for _key, _value in values.items():
            config[_key] = _value
            Console.ok(f"{_key}={_value}")

        config.save()

    @staticmethod
    def activate():
        config = Config()
        clouds = list(config["cloudmesh.cloud"].keys())

        gui.SetOptions(text_justification='right')

        layout = [
            [gui.Text('Cloudmesh Cloud Activation', font=('Helvetica', 16))],
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

        window = gui.Window('Cloudmesh Configuration', layout, font=("Helvetica", 12))

        event, values = window.Read()

        for cloud in values:

            active = values[cloud] or False
            config[f"cloudmesh.cloud.{cloud}.cm.active"] = str(active)
            if active:
                Console.ok(f"Cloud {cloud} is active")

        config.save()
