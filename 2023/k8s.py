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

class AppContainerInPod(Scene):
    def construct(self):
        docker_container = Square(color=BLUE)
        docker_container_label = Text("Containerized app", font_size=24)
        docker_container_label.next_to(docker_container, UP)
        docker_container_group = VGroup(docker_container, docker_container_label)

        k8s_pod = Circle(color=GREEN)
        k8s_pod.scale(2.5)
        k8s_pod_label = Text("Pod", font_size=36)
        k8s_pod_label.next_to(k8s_pod, UP) 
        k8s_pod_group = VGroup(k8s_pod, k8s_pod_label)

        self.play(Create(docker_container_group))
        self.wait(1)
        self.play(Create(k8s_pod_group))
        self.wait(1)
        
        self.play(docker_container.animate.move_to(k8s_pod.get_center()))
        self.wait(2)

        self.play(FadeOut(docker_container))
        self.play(FadeOut(docker_container_label))

        docker_container1 = Square(color=BLUE).scale(0.5)
        docker_container2 = Square(color=BLUE).scale(0.5)
        docker_container_label1 = Text("Containerized app", font_size=24).next_to(docker_container1, UP, buff=0.1)

        docker_container1.move_to(docker_container.get_center() + LEFT)
        docker_container2.move_to(docker_container.get_center() + RIGHT)
        docker_container_group = VGroup(docker_container1, docker_container_label1, docker_container2)
        
        self.play(Create(docker_container_group))
        self.wait(1)

        self.play(Create(k8s_pod_group))
        self.wait(1)
        
        self.play(docker_container_group.animate.move_to(k8s_pod.get_center()))
        self.wait(2)

        self.play(k8s_pod_group.animate.scale(0.5))
        self.play(docker_container_group.animate.scale(0.5))

        k8s_node = RegularPolygon(n=6, color=RED)
        k8s_node.scale(2.5)
        k8s_node_label = Text("Node", font_size=36)
        k8s_node_label.next_to(k8s_node, UP)
        k8s_node_group = VGroup(k8s_node, k8s_node_label)
        self.play(Create(k8s_node_group))

        self.play(k8s_pod_group.animate.move_to(k8s_node.get_center()))
        self.wait(2)