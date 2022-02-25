from manim import *

class PolyLogo(Scene):
    def construct(self):
        centerSphere = Sphere(
            radius=2,
            resolution=(101, 51),
        ).set_color(BLUE_E)

        rIN = 2.49
        rMID = 3.4
        rOUT = 3.9
        rTEXT = 3
        AngleBetInMid = 3
        AngleOUT = 8
        AngleMIDlen = 22.5 - AngleOUT - 2*AngleBetInMid
        AngleMIDstart = 0.5*AngleOUT + AngleBetInMid 

        arcIN = Arc(radius=rIN, start_angle=0, angle=-225*PI/180, stroke_width=2, stroke_color=BLUE_A)

        # I am still struggling with loops
        # If someone out there who can shorten the codes for arcs below using loops,
        # it will be highly appreciated
        arcOUT0 = Arc(radius=rOUT, start_angle=135*PI/180, angle=0.5*AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT1 = Arc(radius=rOUT, start_angle=(157.5 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT2 = Arc(radius=rOUT, start_angle=(180 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT3 = Arc(radius=rOUT, start_angle=(202.5 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT4 = Arc(radius=rOUT, start_angle=(225 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT5 = Arc(radius=rOUT, start_angle=(247.5 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT6 = Arc(radius=rOUT, start_angle=(270 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT7 = Arc(radius=rOUT, start_angle=(292.5 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT8 = Arc(radius=rOUT, start_angle=(315 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT9 = Arc(radius=rOUT, start_angle=(337.5 - 0.5*AngleOUT)*PI/180, angle=AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcOUT10 = Arc(radius=rOUT, start_angle=(360 - 0.5*AngleOUT)*PI/180, angle=0.5*AngleOUT*PI/180, stroke_width=2, stroke_color=BLUE_A)
        
        arcMID0 = Arc(radius=rMID, start_angle=(135 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID1 = Arc(radius=rMID, start_angle=(157.5 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID2 = Arc(radius=rMID, start_angle=(180 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID3 = Arc(radius=rMID, start_angle=(202.5 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID4 = Arc(radius=rMID, start_angle=(225 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID5 = Arc(radius=rMID, start_angle=(247.5 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID6 = Arc(radius=rMID, start_angle=(270 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID7 = Arc(radius=rMID, start_angle=(292.5 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID8 = Arc(radius=rMID, start_angle=(315 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)
        arcMID9 = Arc(radius=rMID, start_angle=(337.5 + AngleMIDstart)*PI/180, angle=AngleMIDlen*PI/180, stroke_width=2, stroke_color=BLUE_A)

        # The following are placeholders of the letters in the word MATHalino
        arcO = Arc(radius=rTEXT, start_angle=0, angle=15*PI/180)
        arcN = Arc(radius=rTEXT, start_angle=15*PI/180, angle=15*PI/180)
        arcI = Arc(radius=rTEXT, start_angle=30*PI/180, angle=15*PI/180)
        arcL = Arc(radius=rTEXT, start_angle=45*PI/180, angle=15*PI/180)
        arcALPHA = Arc(radius=rTEXT, start_angle=60*PI/180, angle=15*PI/180)
        arcH = Arc(radius=rTEXT, start_angle=75*PI/180, angle=15*PI/180)
        arcT = Arc(radius=rTEXT, start_angle=90*PI/180, angle=15*PI/180)
        arcA = Arc(radius=rTEXT, start_angle=105*PI/180, angle=15*PI/180)
        arcM = Arc(radius=rTEXT, start_angle=120*PI/180, angle=15*PI/180)

        MATHalino = Tex("$\\mathbb{M}$","$\\mathbb{A}$","$\\mathbb{T}$","$\\mathbb{H}$","$\\alpha$","l","i","n","o")
        MATHalino[0].move_to(arcM)
        MATHalino[1].move_to(arcA)
        MATHalino[2].move_to(arcT)
        MATHalino[3].move_to(arcH)
        MATHalino[4].move_to(arcALPHA).set_color(PURE_RED)
        MATHalino[5].move_to(arcL)
        MATHalino[6].move_to(arcI)
        MATHalino[7].move_to(arcN)
        MATHalino[8].move_to(arcO)

        poly_conf = {
            "stroke_width": 2,
            "stroke_color": BLUE_A,
            "fill_opacity": 1,
            "fill_color": "#0072BC",
        }
     
        polyArcs = ArcPolygonFromArcs(
            arcOUT0, arcMID0, arcOUT1, arcMID1, arcOUT2, arcMID2, arcOUT3, arcMID3, arcOUT4, arcMID4, 
            arcOUT5, arcMID5, arcOUT6, arcMID6, arcOUT7, arcMID7, arcOUT8, arcMID8, arcOUT9, arcMID9,
            arcOUT10, arcIN, **poly_conf,
        )
                
        self.play(
            DrawBorderThenFill(polyArcs),
            Write(centerSphere),
        )
        self.play(Create(MATHalino))
        self.wait()


# Shortened the code above by using For loop
# This is my first strong grasp of a loop command
# Needs more practice...
class PolyLogoForLoop(Scene):
    def construct(self):
        centerSphere = Sphere(
            radius=2,
            resolution=(101, 51),
        ).set_color(BLUE_E)

        rIN = 2.49
        rMID = 3.4
        rOUT = 3.9
        rTEXT = 3
        AngleBetInMid = 3
        AngleOUT = 8
        AngleMIDlen = 22.5 - AngleOUT - 2*AngleBetInMid
        AngleMIDstart = 0.5*AngleOUT + AngleBetInMid 

        arcOUTstart = Arc(
            radius=rOUT,
            start_angle=135*PI/180,
            angle=0.5*AngleOUT*PI/180,
            stroke_width=2,
            stroke_color=BLUE_A
        )

        arcOUTend = Arc(
            radius=rOUT,
            start_angle=(360 - 0.5*AngleOUT)*PI/180,
            angle=0.5*AngleOUT*PI/180,
            stroke_width=2,
            stroke_color=BLUE_A,
        )

        arcOUT = VGroup()
        for x in np.arange(157.5, 360, 22.5):
            arcOUT += Arc(
                radius=rOUT,
                start_angle=(x - 0.5*AngleOUT)*PI/180,
                angle=AngleOUT*PI/180,
                stroke_width=2,
                stroke_color=BLUE_A,
            )

        arcMID = VGroup()        
        for y in np.arange(135, 360, 22.5):
            arcMID += Arc(
                radius=rMID,
                start_angle= (y + AngleMIDstart)*PI/180,
                angle=AngleMIDlen*PI/180,
                stroke_width=2,
                stroke_color=BLUE_A,
            )
                        
        arcIN = Arc(
            radius=rIN,
            start_angle=0,
            angle=-225*PI/180,
            stroke_width=2,
            stroke_color=BLUE_A
        )
        
        arcMATHalino = VGroup()
        for z in np.arange(135, 0, -15):
            arcMATHalino += Arc(
                radius=rTEXT,
                start_angle= z*PI/180,
                angle=-15*PI/180,
                stroke_width=2,
                stroke_color=RED,
            )

        poly_conf = {
            "stroke_width": 2,
            "stroke_color": BLUE_A,
            "fill_opacity": 1,
            "fill_color": "#0072BC",
        }

        gearLogo = ArcPolygonFromArcs(
            arcOUTstart, arcMID[0], arcOUT[0], arcMID[1], arcOUT[1], arcMID[2], arcOUT[2], arcMID[3], arcOUT[3],
            arcMID[4], arcOUT[4], arcMID[5], arcOUT[5], arcMID[6], arcOUT[6], arcMID[7], arcOUT[7],
            arcMID[8], arcOUT[8], arcMID[9], arcOUTend, arcIN, **poly_conf,  
        )

        MATHalino = Tex("$\\mathbb{M}$","$\\mathbb{A}$","$\\mathbb{T}$","$\\mathbb{H}$","$\\alpha$","l","i","n","o")
        MATHalino[4].set_color(PURE_RED)
        for i in range(9):
            MATHalino[i].move_to(arcMATHalino[i])
        
        self.add(
            gearLogo,
            centerSphere,
            #arcMATHalino,
            MATHalino,
        )
