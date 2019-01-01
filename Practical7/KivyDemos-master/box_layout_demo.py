from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def clear_all(self):
        print("Clear")
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        print("Greet")
        self.root.ids.output_label.text = "Hello "+ self.root.ids.input_name.text

BoxLayoutDemo().run()
