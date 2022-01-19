from manim import *

class CreateGraph(Scene):
    def construct(self):
        MATHalino = Tex(
            "M",            #0
            "A",            #1
            "T",            #2
            "H",            #3
            "$\\alpha$",    #4
            "l",            #5
            "i",            #6
            "n",            #7
            "o"             #8
        )
        MATHalino[0].set_color(YELLOW_D)
        MATHalino[1].set_color(YELLOW_D)
        MATHalino[2].set_color(YELLOW_D)
        MATHalino[3].set_color(YELLOW_D)
        MATHalino[4].set_color(RED_D)
        MATHalino[5].set_color(YELLOW_D)
        MATHalino[6].set_color(YELLOW_D)
        MATHalino[7].set_color(YELLOW_D)
        MATHalino[8].set_color(YELLOW_D)

        MATHalino.scale(2)

        delta = ValueTracker(0.01)
        PolarCoordinates = PolarPlane(
            # azimuth_units="PI radians",
            size=6.5,
            radius_max=10,
            azimuth_step=24,
            background_line_style={
                "stroke_color": GREY_BROWN
            #    "stroke_width": 0.8,
            #    "stroke_opacity": 0.8
            }
            #radius_step=0.5,
            # azimuth_label_font_size=33.6,
            # radius_config={"font_size": 33.6},
        ).add_coordinates()
        Leaf1 = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(10*np.sin(3*t), t),
            t_range = [0, delta.get_value()], color = BLUE)
        )
        dotLeaf1 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Leaf1.get_end())
        )

        self.play(Write(PolarCoordinates), run_time=3)
        self.play(Write(MATHalino, run_time=2))
        self.wait(0.5)
        self.add(Leaf1, dotLeaf1)
        self.play(delta.animate.set_value(PI), run_time = 5, rate_func = linear)
        self.wait()

class LemniscateCOS(Scene):
    def construct(self):
        varA = 9
        varB = 12
        delta = ValueTracker(0.01)
        polarCoords = PolarPlane(
            # azimuth_units="PI radians",
            size=6.5,
            radius_max=np.sqrt(varA),
            azimuth_step=24,
            background_line_style={"stroke_color": GREY_BROWN},
            #radius_step=0.5
        ).add_coordinates()

        lem1 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords.polar_to_point(np.sqrt(varA)*np.sqrt(np.cos(2*t)), t),
            t_range = [0, delta.get_value()], color = BLUE)
        )
        lem2 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords.polar_to_point(np.sqrt(varA)*np.sqrt(np.cos(2*t)), t),
            t_range = [2*TAU, delta.get_value()], color = BLUE)
        )

        dotlem1 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(lem1.get_end())
        )
        dotlem2 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(lem1.get_end())
        )

        self.play(Write(polarCoords), run_time=3)
        self.wait(0.5)
        self.add(lem1, dotlem1, dotlem2)
        self.play(delta.animate.set_value(PI), run_time=1, rate_func = linear)
        self.wait()

class PolarCoordinates(Scene):
    def construct(self):
        #self.camera.background_color = WHITE
        polarCoords = PolarPlane(
            azimuth_units="PI radians",
            size=6.5,
            radius_max=5,
            azimuth_step=24,
        ).add_coordinates()
        polarCoords.set_color(GREY)

        self.add(polarCoords)

class ThreeLeaf(Scene):
    def construct(self):
        PolarCoordinates = PolarPlane(
            size=6.5,
            radius_max=10,
            azimuth_step=24
        )

        ThreeLeafRose = ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(10*np.sin(3*t), t),
            t_range = [0, TAU], color = BLUE)

        self.add(ThreeLeafRose)

class Butterfly(Scene):
    def construct(self):
        self.camera.background_color = "#212121"
        delta = ValueTracker(0.01)
        PolarCoordinates = PolarPlane(
            azimuth_units="degrees",
            size=6.5,
            azimuth_step=24,
            background_line_style={
                "stroke_color": BLUE_E
            }
        ).add_coordinates()
        # polarCoordinates.set_color(GREY)

        ButterflyGraph = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(np.exp(np.sin(t)) - 2*np.cos(4*t) + (np.sin((2*t - PI)/24))**5, t),
            t_range = [0, delta.get_value()], color = YELLOW))

        dotButterflyGraph = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(ButterflyGraph.get_end())
        )

        self.add(PolarCoordinates)
        self.wait()
        self.add(ButterflyGraph, dotButterflyGraph)
        self.play(delta.animate.set_value(24*TAU), run_time=24, rate_func = linear)
        self.remove(dotButterflyGraph)
        self.wait(2)

class PolarGraphExample(Scene):
    def construct(self):
        plane = PolarPlane(
            size=6,
            azimuth_units="degrees",
            azimuth_step=20,
            radius_config={
                "stroke_color": BLUE_B,
                "stroke_width": 2,
            },
            background_line_style={
                "stroke_color": BLUE_E,
            }
        ).add_coordinates()

        r = lambda theta: 4 * np.sin(theta * 5)
        graph = plane.plot_polar_graph(r, [0, TAU], color=YELLOW)
        self.play(Create(plane), run_time=3)
        self.wait()
        self.play(Write(graph), run_time=5)
        self.wait()
        # self.add(plane, graph)

class Graph1(Scene):
    def construct(self):
        delta = ValueTracker(0.01)
        PolarCoordinates = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            radius_max=5,
            azimuth_step=12,
            background_line_style={
                "stroke_color": GREY_BROWN,
                "stroke_width": 0.8,
                "stroke_opacity": 0.8
            },
            radius_step=1,
            azimuth_label_font_size=32,
            radius_config={
                #"font_size": 33,
                "color": RED
            },
        ).add_coordinates()
        Leaf = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(5*np.cos(3*t), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotLeaf = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Leaf.get_end())
        )

        self.play(Write(PolarCoordinates), run_time=3)
        self.wait(0.5)
        self.add(Leaf, dotLeaf)
        self.play(delta.animate.set_value(PI), run_time = 5, rate_func = linear)
        self.remove(dotLeaf)
        self.wait()

class PolarCoordinatesSet(Scene):
    def construct(self):
        self.camera.background_color = "#212121"

        polarCoords1 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords1.shift(LEFT*3+UP*2)
        polarCoords1.set_color(BLUE_D)

        polarCoords2 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords2.shift(RIGHT*3+UP*2)
        polarCoords2.set_color(BLUE_D)

        polarCoords3 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords3.shift(LEFT*3+DOWN*2)
        polarCoords3.set_color(BLUE_D)

        polarCoords4 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords4.shift(RIGHT*3+DOWN*2)
        polarCoords4.set_color(BLUE_D)

        self.play(
            Write(polarCoords1),
            Write(polarCoords2),
            Write(polarCoords3),
            Write(polarCoords4),
            run_time=3
        )

        self.wait(10)

class LeafGraphsSet(Scene):
    def construct(self):
        self.camera.background_color = "#212121"

        delta1 = ValueTracker(0.01)
        delta2 = ValueTracker(0.01)

        polarCoords1 = PolarPlane(
            # azimuth_units="PI radians",
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords1.shift(LEFT*3+UP*2)
        polarCoords1.set_color(BLUE_D)

        polarCoords2 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords2.shift(RIGHT*3+UP*2)
        polarCoords2.set_color(BLUE_D)

        polarCoords3 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords3.shift(LEFT*3+DOWN*2)
        polarCoords3.set_color(BLUE_D)

        polarCoords4 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords4.shift(RIGHT*3+DOWN*2)
        polarCoords4.set_color(BLUE_D)

        LeafCos3 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords1.polar_to_point(5*np.cos(3*t), t),
            t_range = [0, delta1.get_value()], color = YELLOW)
        )
        dotLeafCos3 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(LeafCos3.get_end())
        )

        LeafSin3 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords3.polar_to_point(5*np.sin(3*t), t),
            t_range = [0, delta1.get_value()], color = YELLOW)
        )
        dotLeafSin3 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(LeafSin3.get_end())
        )

        LeafCos4 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords2.polar_to_point(5*np.cos(2*t), t),
            t_range = [0, delta2.get_value()], color = YELLOW)
        )
        dotLeafCos4 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(LeafCos4.get_end())
        )

        LeafSin4 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords4.polar_to_point(5*np.sin(2*t), t),
            t_range = [0, delta2.get_value()], color = YELLOW)
        )
        dotLeafSin4 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(LeafSin4.get_end())
        )

        self.add(
            #polarCoords1,
            #polarCoords2,
            #polarCoords3,
            #polarCoords4,
            LeafCos3,
            dotLeafCos3,
            LeafSin3,
            dotLeafSin3,
            LeafCos4,
            dotLeafCos4,
            LeafSin4,
            dotLeafSin4
        )
        self.wait()
        self.play(
            delta1.animate.set_value(PI),
            delta2.animate.set_value(TAU),
            run_time = 5,
            rate_func = linear
        )
        self.remove(
            dotLeafCos3,
            dotLeafSin3,
            dotLeafCos4,
            dotLeafSin4
        )
        self.wait(5)
        """
        self.play(
            FadeOut(LeafCos3),
            FadeOut(LeafSin3),
            FadeOut(LeafCos4),
            FadeOut(LeafSin4)
        )
        self.wait()
        """

class CardioidSet(Scene):
    def construct(self):
        self.camera.background_color = "#212121"

        delta = ValueTracker(0.01)

        polarCoords1 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords1.shift(LEFT*3+UP*2)
        polarCoords1.set_color(BLUE_D)

        polarCoords2 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords2.shift(RIGHT*3+UP*2)
        polarCoords2.set_color(BLUE_D)

        polarCoords3 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords3.shift(LEFT*3+DOWN*2)
        polarCoords3.set_color(BLUE_D)

        polarCoords4 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords4.shift(RIGHT*3+DOWN*2)
        polarCoords4.set_color(BLUE_D)

        Cardioid1 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords1.polar_to_point(2.5*(1 + np.cos(t)), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotCardioid1 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Cardioid1.get_end())
        )

        Cardioid2 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords3.polar_to_point(2.5*(1 - np.cos(t)), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotCardioid2 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Cardioid2.get_end())
        )

        Cardioid3 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords2.polar_to_point(2.5*(1 + np.sin(t)), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotCardioid3 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Cardioid3.get_end())
        )

        Cardioid4 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords4.polar_to_point(2.5*(1 - np.sin(t)), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotCardioid4 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Cardioid4.get_end())
        )

        self.add(
            polarCoords1,
            polarCoords2,
            polarCoords3,
            polarCoords4,
            Cardioid1,
            dotCardioid1,
            Cardioid2,
            dotCardioid2,
            Cardioid3,
            dotCardioid3,
            Cardioid4,
            dotCardioid4
        )
        self.wait()
        self.play(
            delta.animate.set_value(TAU),
            run_time = 5,
            rate_func = linear
        )
        self.remove(
            dotCardioid1,
            dotCardioid2,
            dotCardioid3,
            dotCardioid4
        )

        self.wait(5)

        self.play(
            FadeOut(Cardioid1),
            FadeOut(Cardioid2),
            FadeOut(Cardioid3),
            FadeOut(Cardioid4)
        )
        self.wait()

class LimaconSet(Scene):
    def construct(self):
        self.camera.background_color = "#212121"

        delta = ValueTracker(0.01)

        polarCoords1 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords1.shift(LEFT*3+UP*2)
        polarCoords1.set_color(BLUE_D)

        polarCoords2 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords2.shift(RIGHT*3+UP*2)
        polarCoords2.set_color(BLUE_D)

        polarCoords3 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords3.shift(LEFT*3+DOWN*2)
        polarCoords3.set_color(BLUE_D)

        polarCoords4 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords4.shift(RIGHT*3+DOWN*2)
        polarCoords4.set_color(BLUE_D)

        Limacon1 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords1.polar_to_point(1.5+3.5*np.cos(t), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotLimacon1 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Limacon1.get_end())
        )

        Limacon2 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords3.polar_to_point(1.5-3.5*np.cos(t), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotLimacon2 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Limacon2.get_end())
        )

        Limacon3 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords2.polar_to_point(1.5+3.5*np.sin(t), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotLimacon3 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Limacon3.get_end())
        )

        Limacon4 = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords4.polar_to_point(1.5-3.5*np.sin(t), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotLimacon4 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(Limacon4.get_end())
        )

        self.add(
            polarCoords1,
            polarCoords2,
            polarCoords3,
            polarCoords4,
            Limacon1,
            dotLimacon1,
            Limacon2,
            dotLimacon2,
            Limacon3,
            dotLimacon3,
            Limacon4,
            dotLimacon4
        )
        self.wait()
        self.play(
            delta.animate.set_value(TAU),
            run_time = 5,
            rate_func = linear
        )
        self.remove(
            dotLimacon1,
            dotLimacon2,
            dotLimacon3,
            dotLimacon4
        )
        self.wait(5)

        self.play(
            FadeOut(Limacon1),
            FadeOut(Limacon2),
            FadeOut(Limacon3),
            FadeOut(Limacon4)
        )
        self.wait()

class Spirals(Scene):
    def construct(self):
        # self.camera.background_color = "#212121"

        delta = ValueTracker(0.01)

        polarCoords1 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords1.shift(LEFT*3+UP*2)
        polarCoords1.set_color(BLUE_D)

        polarCoords2 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords2.shift(RIGHT*3+UP*2)
        polarCoords2.set_color(BLUE_D)

        polarCoords3 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords3.shift(LEFT*3+DOWN*2)
        polarCoords3.set_color(BLUE_D)

        polarCoords4 = PolarPlane(
            size=3,
            radius_max=5,
            azimuth_step=24
        ).add_coordinates()
        polarCoords4.shift(RIGHT*3+DOWN*2)
        polarCoords4.set_color(BLUE_D)

        ArchimedesSpiral = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords1.polar_to_point((5/TAU)*t, t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotArchimedesSpiral = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(ArchimedesSpiral.get_end())
        )

        ReciprocalSpiral = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords2.polar_to_point(5/(TAU*((1/TAU) + t)), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotReciprocalSpiral = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(ReciprocalSpiral.get_end())
        )

        TrumpetSpiral = always_redraw(lambda : ParametricFunction(
            lambda t : polarCoords3.polar_to_point(5/(TAU*np.sqrt((1/TAU**2) + t)), t),
            t_range = [0, delta.get_value()], color = YELLOW)
        )
        dotTrumpetSpiral = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).move_to(TrumpetSpiral.get_end())
        )

        self.add(
            polarCoords1,
            polarCoords2,
            polarCoords3,
            polarCoords4,
            ArchimedesSpiral,
            dotArchimedesSpiral,
            ReciprocalSpiral,
            dotReciprocalSpiral,
            TrumpetSpiral,
            dotTrumpetSpiral
        )
        self.wait()
        self.play(
            delta.animate.set_value(TAU),
            run_time = 5,
            rate_func = linear
        )

class Pantog(Scene):
    def construct(self):
        delta1 = ValueTracker(0.01)
        delta2 = ValueTracker(0.01)
        delta3 = ValueTracker(0.01)
        delta4 = ValueTracker(0.01)
        PolarCoordinates = PolarPlane(
            azimuth_units="degrees",
            size=6,
            radius_max=5,
            azimuth_step=12,
            radius_step=1,
            azimuth_label_font_size=32,
            background_line_style={
                "stroke_color": GREY_BROWN,
                "stroke_width": 0.8,
                "stroke_opacity": 0.8
            },
            radius_config={
                "font_size": 24,
                # "color": RED <-- di gumagana
            },
        ).add_coordinates()

        Pantog1 = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(5*np.sqrt(np.cos(t)), t),
            t_range = [0, delta1.get_value()], color = YELLOW)
        )
        Pantog2 = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(-5*np.sqrt(np.cos(t)), t),
            t_range = [0, delta2.get_value()], color = YELLOW)
        )
        Pantog3 = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(5*np.sqrt(np.cos(t)), -t),
            t_range = [0, delta3.get_value()], color = YELLOW)
        )
        Pantog4 = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(-5*np.sqrt(np.cos(t)), -t),
            t_range = [0, delta4.get_value()], color = YELLOW)
        )

        dotPantog1 = always_redraw(
            lambda : Dot(
                fill_color = RED,
                fill_opacity = 0.8
            ).move_to(Pantog1.get_end())
        )
        dotPantog2 = always_redraw(
            lambda : Dot(
                fill_color = RED,
                fill_opacity = 0.8
            ).move_to(Pantog2.get_end())
        )
        dotPantog3 = always_redraw(
            lambda : Dot(
                fill_color = RED,
                fill_opacity = 0.8
            ).move_to(Pantog3.get_end())
        )
        dotPantog4 = always_redraw(
            lambda : Dot(
                fill_color = RED,
                fill_opacity = 0.8
            ).move_to(Pantog4.get_end())
        )

        self.play(Write(PolarCoordinates), run_time=3)
        self.wait(0.5)
        self.add(
            Pantog1,
            Pantog2,
            dotPantog1,
            dotPantog2,
        )

        self.play(
            delta1.animate.set_value(
                PI/2
            ),
            delta2.animate.set_value(PI/2),
            run_time = 3,
            rate_func = linear
        )
        self.remove(
            dotPantog1,
            dotPantog2,
        )
        self.add(
            Pantog3,
            Pantog4,
            dotPantog3,
            dotPantog4,
        )
        self.play(
            delta3.animate.set_value(PI/2),
            delta4.animate.set_value(PI/2),
            run_time = 3,
            rate_func = linear
        )
        self.remove(
            dotPantog3,
            dotPantog4,
        )
        self.wait()

class PantogDuha(Scene):
    def construct(self):

        delta = ValueTracker(1.5*PI)

        PolarCoordinates = PolarPlane(size=6).add_coordinates()

        Pantog = always_redraw(lambda : ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(4*np.sqrt(np.cos(t)), t),
            t_range = [1.5*PI, delta.get_value()], color = YELLOW)
        )

        dotPantog = always_redraw(
            lambda : Dot(
                fill_color = RED,
                fill_opacity = 0.8
            ).move_to(Pantog.get_end())
        )

        self.add(PolarCoordinates, Pantog, dotPantog)

        self.play(
            delta.animate.set_value(2*PI),
            run_time = 2,
            rate_func = linear
        )
        self.remove(dotPantog)
        self.wait()

#The following is from Theorem of Beethoven based on old codes
#Revised to work for Manim Community Edition
class EpicycloidScene(Scene):
    def construct(self):
       radius1 = 2.4
       radius2 = radius1/3
       self.epy(radius1,radius2)

    def epy(self,r1,r2):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=PURPLE).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        # .points[0] return the start path coordinate
        # .points[-1] return the end path coordinate
        dot = Dot(c2.points[0],color=RED)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=RED)
        # Path can't have the same coord twice, so we have to dummy point
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        # Alpha, from 0 to 1:
        alpha = ValueTracker(0)

        self.play(Write(line),Write(c1),Write(c2),GrowFromCenter(dot))

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            # See manimlib/mobject/types/vectorized_mobject.py
            old_path.append_vectorized_mobject(Line(old_path.points[-1],mob.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),mob.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c):
            c.become(c.start)
            c.rotate(TAU*alpha.get_value(),about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha.get_value(),about_point=c.get_center())

        path_group.add_updater(update_group)
        c2.add_updater(update_c2)
        self.add(c2,path_group)
        self.play(
                alpha.animate.set_value(1),
                rate_func=linear,
                run_time=6
                )
        self.wait(2)
        c2.clear_updaters()
        path_group.clear_updaters()
        self.play(FadeOut(VGroup(c1,c2,path_group)))

class RoseCurves(Scene):
    def construct(self):
        #nVar = ValueTracker(1)
        #nVar = ValueTracker(2)
        #nVarOdd =
        PolarCoordinates = PolarPlane(
            axes_color = GREY_BROWN,
            stroke_width = 0.8,
            size=6.5,
            radius_max=5,
            azimuth_step=24,
            background_line_style = {
                "stroke_color": GREY,
                "stroke_width": 0.8,
                "stroke_opacity": 0.8
            }
        ).add_coordinates()

        RoseOdd = ParametricFunction(
            lambda t : PolarCoordinates.polar_to_point(5*np.sin(2*t), t),
            t_range = [0, TAU],
            color = BLUE,
            stroke_width = 3
        )

        self.play(Write(PolarCoordinates), run_time=3)
        self.wait()
        self.play(Write(RoseOdd), run_time=5)
        self.wait()
