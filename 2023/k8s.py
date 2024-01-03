from manim import *

class KubernetesToK8s(Scene):
    def construct(self):
        kubernetes_text = Text("Kubernetes", font_size=72)
        
        k8s_text = Text("K8s", font_size=72)
        
        k8s_text.move_to(kubernetes_text.get_center())
        
        self.play(Write(kubernetes_text))
        self.wait(1)

        self.play(FadeOut(kubernetes_text[1:9]))
        self.play(
            kubernetes_text[0].animate.move_to(k8s_text[0].get_center()),
            kubernetes_text[-1].animate.move_to(k8s_text[-1].get_center())
        )
        self.wait(0.5)

        self.play(TransformMatchingShapes(kubernetes_text[0], k8s_text[0]))
        self.play(TransformMatchingShapes(kubernetes_text[-1], k8s_text[-1]))
        self.play(Write(k8s_text[1]))

        self.wait(2)
