# 管理样式css资源

stylesheet_instance = None

def get_stylesheet(name):
    global stylesheet_instance
    if not stylesheet_instance:
        stylesheet_instance = Stylesheets()
    return stylesheet_instance.get_stylesheet(name)


class Stylesheets(object):
    def __init__(self):
        self._stylesheets = {}
        self.make_stylesheet("main", "Cmaster/stylesheets/main.css")
        self.make_stylesheet("Widget", "Cmaster/stylesheets/Widget.css")
        self.make_stylesheet("Pane", "Cmaster/stylesheets/Pane.css")
        self.make_stylesheet("BigButton", "Cmaster/stylesheets/BigButton.css")
        self.make_stylesheet("SmallButton", "Cmaster/stylesheets/SmallButton.css")

    def make_stylesheet(self, name, path):
        with open(path) as data_file:
            stylesheet = data_file.read()

        self._stylesheets[name] = stylesheet

    def get_stylesheet(self, name):
        stylesheet = ""
        try:
            stylesheet = self._stylesheets[name]
        except KeyError:
            print("stylesheet " + name + " not found")
        return stylesheet
