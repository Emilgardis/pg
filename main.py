import pg

class App(pg.App):
    def setup(self):
        matrix = pg.Matrix()
        matrix = matrix.translate((0, 1, 0))
        matrix = matrix.perspective(45, 640 / 480.0, 0.1, 100)
        print matrix
        program = pg.Program('shaders/vertex.glsl', 'shaders/fragment.glsl')
        # program.matrix = matrix
        # program.position = pg.VertexBuffer(3, pg.FLOAT, [...])
        print program.get_attributes()
        print program.get_uniforms()
    def update(self, dt):
        pass
    def draw(self):
        self.clear()
    def teardown(self):
        pass

if __name__ == "__main__":
    app = App()
    app.run()
