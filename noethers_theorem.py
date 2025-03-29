from manim import *
import logging
from random import choice, uniform

# Set up logging to debug rendering issues
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NoethersTheorem(Scene):
    def construct(self):
        logger.info("Starting Noether's Theorem animation")

        # Scene 1: Introduction
        intro_title = Text("Noether's Theorem", font_size=48, color=YELLOW)
        intro_subtitle = Text("Symmetry and Conservation Laws", font_size=36, color=WHITE)
        intro_group = VGroup(intro_title, intro_subtitle).arrange(DOWN)
        self.play(Write(intro_group))
        self.wait(2)
        self.play(FadeOut(intro_group))
        self.remove(*intro_group)  # Explicitly remove objects
        self.clear()  # Ensure a clean slate

        # Scene 2: What is Symmetry?
        symmetry_objects = VGroup()  # Track all objects in this scene
        symmetry_title = Text("What is Symmetry?", font_size=40, color=BLUE).to_edge(UP)
        symmetry_objects.add(symmetry_title)

        circle = Circle(radius=1.5, color=WHITE, fill_opacity=0.2).shift(LEFT * 3)
        dot = Dot(point=circle.get_center() + RIGHT * 1.5, color=RED)
        system = VGroup(circle, dot)
        system_label = Text("Physical System", font_size=24, color=WHITE).next_to(circle, DOWN)
        symmetry_objects.add(system, system_label)

        symmetry_desc1 = Tex("Rotational Symmetry: The system", font_size=32, color=WHITE)
        symmetry_desc2 = Tex("looks the same after a rotation.", font_size=32, color=WHITE)
        symmetry_desc = VGroup(symmetry_desc1, symmetry_desc2).arrange(DOWN, buff=0.2).shift(RIGHT * 3)
        symmetry_objects.add(symmetry_desc)

        self.play(Write(symmetry_title))
        self.play(Create(system), Write(system_label))
        self.play(Write(symmetry_desc))
        self.play(Rotate(system, angle=2 * PI, about_point=circle.get_center()), run_time=3)
        self.wait(2)

        # Fade out all objects from Scene 2
        self.play(FadeOut(symmetry_objects))
        self.remove(*symmetry_objects)  # Explicitly remove objects
        self.clear()  # Ensure a clean slate

        # Scene 3: Noether's Theorem Statement
        theorem_objects = VGroup()  # Track all objects in this scene
        theorem_title = Text("Noether's Theorem", font_size=40, color=BLUE).to_edge(UP)
        theorem_objects.add(theorem_title)

        theorem_text1 = Tex("For every continuous symmetry", font_size=36, color=WHITE)
        theorem_text2 = Tex("in a physical system,", font_size=36, color=WHITE)
        theorem_text3 = Tex("there is a corresponding", font_size=36, color=WHITE)
        theorem_text4 = Tex("conserved quantity.", font_size=36, color=WHITE)
        theorem_statement = VGroup(theorem_text1, theorem_text2, theorem_text3, theorem_text4).arrange(DOWN, buff=0.2).shift(UP * 2)
        theorem_objects.add(theorem_statement)

        noether_fact = Tex("Emmy Noether proved this in 1915.", font_size=32, color=GREEN).next_to(theorem_statement, DOWN, buff=0.5)
        theorem_objects.add(noether_fact)

        self.play(Write(theorem_title))
        self.play(Write(theorem_statement))
        self.play(Write(noether_fact))
        self.wait(3)

        # Fade out all objects from Scene 3
        self.play(FadeOut(theorem_objects))
        self.remove(*theorem_objects)  # Explicitly remove objects
        self.clear()  # Ensure a clean slate

        # Scene 4: Proof of Noether's Theorem
        proof_objects = VGroup()  # Track all objects in this scene
        proof_title = Text("Proof of Noether's Theorem", font_size=40, color=BLUE).to_edge(UP)
        proof_objects.add(proof_title)

        # Step 1: Define the Action and Lagrangian
        action_text1 = Tex(r"The action $S = \int_{t_1}^{t_2}$", font_size=32, color=WHITE)
        action_text2 = Tex(r"$L(q, \dot{q}, t) \, dt$,", font_size=32, color=WHITE)
        action_text3 = Tex(r"where $L$ is the Lagrangian.", font_size=32, color=WHITE)  # Fixed misspelling
        action_group = VGroup(action_text1, action_text2, action_text3).arrange(DOWN, buff=0.2).shift(UP * 1).to_edge(LEFT)
        proof_objects.add(action_group)

        self.play(Write(proof_title))
        self.play(Write(action_group))
        self.wait(2)

        # Step 2: Euler-Lagrange Equations
        euler_text1 = Tex(r"Euler-Lagrange equation:", font_size=32, color=WHITE)
        euler_text2 = Tex(r"$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0$", font_size=32, color=WHITE)
        euler_group = VGroup(euler_text1, euler_text2).arrange(DOWN, buff=0.2).shift(UP * 1)
        proof_objects.add(euler_group)

        self.play(Write(euler_group))
        self.wait(2)

        # Step 3: Symmetry Transformation
        symmetry_text1 = Tex(r"A symmetry transformation", font_size=32, color=WHITE)
        symmetry_text2 = Tex(r"(e.g., $q \to q + \epsilon$)", font_size=32, color=WHITE)
        symmetry_text3 = Tex(r"leaves $S$ invariant: $\delta S = 0$.", font_size=32, color=WHITE)
        symmetry_group = VGroup(symmetry_text1, symmetry_text2, symmetry_text3).arrange(DOWN, buff=0.2).shift(UP * 1).to_edge(RIGHT)
        proof_objects.add(symmetry_group)

        self.play(Write(symmetry_group))
        self.wait(2)

        # Step 4: Noether Current (Conserved Quantity)
        noether_text1 = Tex(r"The conserved quantity (Noether current):", font_size=32, color=WHITE)
        noether_text2 = Tex(r"$\frac{\partial L}{\partial \dot{q}}$", font_size=32, color=WHITE)
        noether_text3 = Tex(r"is constant if $L$ is invariant.", font_size=32, color=WHITE)
        noether_group = VGroup(noether_text1, noether_text2, noether_text3).arrange(DOWN, buff=0.2).shift(DOWN * 2)
        proof_objects.add(noether_group)

        self.play(Write(noether_group))
        self.wait(2)

        # Step 5: Free Particle Example
        example_title = Text("Example: Free Particle", font_size=36, color=GREEN).shift(UP * 2)
        proof_objects.add(example_title)

        lagrangian_text1 = Tex(r"Lagrangian: $L = \frac{1}{2} m \dot{q}^2$", font_size=32, color=WHITE)
        lagrangian_text2 = Tex(r"(free particle).", font_size=32, color=WHITE)
        lagrangian_group = VGroup(lagrangian_text1, lagrangian_text2).arrange(DOWN, buff=0.2).shift(UP * 1)
        proof_objects.add(lagrangian_group)

        number_line = NumberLine(x_range=[-4, 4, 1], length=8).shift(DOWN * 1)
        particle = Dot(point=number_line.n2p(-2), color=RED)
        particle_label = Text("Particle", font_size=24, color=WHITE).next_to(particle, UP)
        particle_group = VGroup(number_line, particle, particle_label)
        proof_objects.add(particle_group)

        spatial_text1 = Tex(r"Spatial Symmetry ($q \to q + a$):", font_size=32, color=WHITE)
        spatial_text2 = Tex(r"$\frac{\partial L}{\partial \dot{q}} = m \dot{q}$", font_size=32, color=WHITE)
        spatial_text3 = Tex(r"Momentum $p = m \dot{q}$ is conserved.", font_size=32, color=WHITE)
        spatial_group = VGroup(spatial_text1, spatial_text2, spatial_text3).arrange(DOWN, buff=0.2).to_edge(DOWN)
        proof_objects.add(spatial_group)

        # Fade out previous proof steps to show the example
        self.play(FadeOut(action_group), FadeOut(euler_group), FadeOut(symmetry_group), FadeOut(noether_group))
        self.play(Write(example_title))
        self.play(Write(lagrangian_group))
        self.play(Create(particle_group))
        self.play(particle.animate.shift(RIGHT * 4), run_time=2)
        self.play(Write(spatial_group))
        self.wait(3)

        # Fade out all objects from the proof section
        # self.play(FadeOut(proof_objects))
        self.remove(*proof_objects)  # Explicitly remove all objects
        self.clear()  # Ensure a clean slate

        # Scene 5: Examples of Symmetries and Conservations
        examples_objects = VGroup()  # Track all objects in this scene
        examples_title = Text("Symmetries and Conservations", font_size=40, color=BLUE).to_edge(UP)
        examples_objects.add(examples_title)

        # Create a table-like layout for examples
        examples_list = VGroup(
            Tex("Time Symmetry $\\rightarrow$ Energy Conservation", font_size=28, color=WHITE),
            Tex("Spatial Symmetry $\\rightarrow$ Momentum Conservation", font_size=28, color=WHITE),
            Tex("Rotational Symmetry $\\rightarrow$ Angular Momentum Conservation", font_size=28, color=WHITE),
            Tex("Gauge Symmetry $\\rightarrow$ Charge Conservation", font_size=28, color=WHITE),
            Tex("Time Reversal Symmetry $\\rightarrow$ No Conservation (Classical)", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(UP * 1).to_edge(LEFT)

        examples_objects.add(examples_list)

        # Visuals for each example
        # Time Symmetry: Clock
        clock = Circle(radius=0.5, color=WHITE, fill_opacity=0.1).next_to(examples_list[0], RIGHT, buff=2)
        clock_hour = Line(clock.get_center(), clock.get_center() + UP * 0.3, color=RED)
        clock_minute = Line(clock.get_center(), clock.get_center() + RIGHT * 0.4, color=RED)
        clock_visual = VGroup(clock, clock_hour, clock_minute)

        # Spatial Symmetry: Moving particle
        spatial_line = NumberLine(x_range=[-2, 2, 1], length=4).next_to(examples_list[1], RIGHT, buff=2)
        spatial_dot = Dot(spatial_line.n2p(-1), color=YELLOW)
        spatial_visual = VGroup(spatial_line, spatial_dot)

        # Rotational Symmetry: Rotating disk
        disk = Circle(radius=0.5, color=WHITE, fill_opacity=0.3).next_to(examples_list[2], RIGHT, buff=2)
        disk_marker = Dot(disk.get_center() + RIGHT * 0.5, color=RED)
        disk_visual = VGroup(disk, disk_marker)

        # Gauge Symmetry: Charge with field lines
        charge = Dot(color=RED).next_to(examples_list[3], RIGHT, buff=2)
        field_lines = VGroup(
            Arrow(charge.get_center(), charge.get_center() + UP * 0.5, color=YELLOW, buff=0),
            Arrow(charge.get_center(), charge.get_center() + DOWN * 0.5, color=YELLOW, buff=0),
            Arrow(charge.get_center(), charge.get_center() + LEFT * 0.5, color=YELLOW, buff=0),
            Arrow(charge.get_center(), charge.get_center() + RIGHT * 0.5, color=YELLOW, buff=0)
        )
        gauge_visual = VGroup(charge, field_lines)

        # Time Reversal Symmetry: Reversible motion
        time_line = NumberLine(x_range=[-2, 2, 1], length=4).next_to(examples_list[4], RIGHT, buff=2)
        time_dot = Dot(time_line.n2p(-1), color=GREEN)
        time_visual = VGroup(time_line, time_dot)

        examples_visuals = VGroup(clock_visual, spatial_visual, disk_visual, gauge_visual, time_visual)
        examples_objects.add(examples_visuals)

        # Display and animate examples
        self.play(Write(examples_title))
        self.play(Write(examples_list))
        self.play(Create(examples_visuals))
        self.play(
            Rotate(clock_hour, angle=2 * PI, about_point=clock.get_center()),
            Rotate(clock_minute, angle=4 * PI, about_point=clock.get_center()),
            spatial_dot.animate.shift(RIGHT * 2),
            Rotate(disk_visual, angle=2 * PI, about_point=disk.get_center()),
            field_lines.animate.scale(1.2),
            time_dot.animate.shift(RIGHT * 2),
            run_time=3
        )
        self.play(time_dot.animate.shift(LEFT * 2), run_time=2)
        self.wait(2)

        # Fade out all objects from the examples section
        self.play(FadeOut(examples_objects))
        self.remove(*examples_objects)  # Explicitly remove all objects
        self.clear()  # Ensure a clean slate

        # Scene 6: Conclusion
        conclusion_objects = VGroup()  # Track all objects in this scene
        conclusion_title = Text("Why Noether's Theorem Matters", font_size=40, color=BLUE).to_edge(UP)
        conclusion_objects.add(conclusion_title)

        conclusion_text1 = Tex("Symmetries govern the laws", font_size=36, color=YELLOW)
        conclusion_text2 = Tex("of nature, revealing conserved", font_size=36, color=YELLOW)
        conclusion_text3 = Tex("quantities that shape physics!", font_size=36, color=YELLOW)
        conclusion_group = VGroup(conclusion_text1, conclusion_text2, conclusion_text3).arrange(DOWN, buff=0.3).shift(UP * 1)
        conclusion_objects.add(conclusion_group)

        self.play(Write(conclusion_title))
        self.play(Write(conclusion_group))
        self.wait(2)

        # Fun ending: Particles celebrating
        particles = VGroup(*[Dot(color=choice([RED, YELLOW, GREEN, BLUE])).shift(UP * uniform(-2, 2) + RIGHT * uniform(-4, 4)) for _ in range(20)])
        conclusion_objects.add(particles)

        self.play(Create(particles))
        self.play(particles.animate.shift(DOWN * 0.5), run_time=2, rate_func=wiggle)
        self.wait(2)

        # Fade out all objects from the conclusion section
        self.play(FadeOut(conclusion_objects))
        self.remove(*conclusion_objects)  # Explicitly remove all objects
        self.clear()  # Ensure a clean slate
        self.wait(1)
        logger.info("Finished Noether's Theorem animation")
