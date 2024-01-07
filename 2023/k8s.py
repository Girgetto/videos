from manim import *

class KubernetesToK8s(Scene):
    def construct(self):
        # Create the initial 'Kubernetes' text
        kubernetes_text = Text("Kubernetes", font_size=72)
        
        # Create the final 'K8s' text
        k8s_text = Text("K8s", font_size=72)
        
        # Position 'K8s' in the same place as 'Kubernetes'
        k8s_text.move_to(kubernetes_text.get_center())
        
        # Add 'Kubernetes' text to the scene
        self.play(Write(kubernetes_text))
        self.wait(1)

        # Animate the transition from 'Kubernetes' to 'K8s'
        # Fade out the middle letters 'ubernete'
        self.play(FadeOut(kubernetes_text[1:9]))
        # Move the 'K' and 's' closer together to form 'K8s'
        self.play(
            kubernetes_text[0].animate.move_to(k8s_text[0].get_center()),
            kubernetes_text[-1].animate.move_to(k8s_text[-1].get_center())
        )
        self.wait(0.5)

        # Since the actual '8' character is different, we substitute 'Ks' with 'K8s'
        self.play(TransformMatchingShapes(kubernetes_text[0], k8s_text[0]))
        self.play(TransformMatchingShapes(kubernetes_text[-1], k8s_text[-1]))
        self.play(Write(k8s_text[1]))

        self.wait(2)


class K8sNode(Scene):
    def construct(self):
        # Create a square to represent the Docker container
        docker_container = Square(color=BLUE)
        docker_container_label = Text("Containerized app", font_size=24)
        docker_container_label.next_to(docker_container, UP)  # Position label at the top of the square
        docker_container_group = VGroup(docker_container, docker_container_label)

        # Create a hexagon to represent the Kubernetes pod
        k8s_pod = Circle(color=GREEN)
        k8s_pod.scale(2.5)  # Make the hexagon larger to enclose the square
        k8s_pod_label = Text("Pod", font_size=36)
        k8s_pod_label.next_to(k8s_pod, UP)  # Position label at the top of the hexagon
        k8s_pod_IP = Text("10.0.0.0", font_size=24).next_to(k8s_pod, DOWN, buff=0.1)
        k8s_pod_group = VGroup(k8s_pod, k8s_pod_label, k8s_pod_IP)

        # Add the shapes to the scene
        self.play(Create(docker_container_group))
        self.wait(1)
        self.play(Create(k8s_pod_group))
        self.wait(1)
        
        # Animate the Docker container moving into the Kubernetes pod
        # Move only the square, keep the label stationary
        self.play(docker_container.animate.move_to(k8s_pod.get_center()))
        self.wait(2)

        self.play(FadeOut(docker_container))
        self.play(FadeOut(docker_container_label))

        docker_container1 = Square(color=BLUE).scale(0.5)
        docker_container2 = Square(color=BLUE).scale(0.5)
        docker_container_label1 = Text("Containerized app", font_size=24).next_to(docker_container1, UP, buff=0.1)
        # random IP address label
   
        # Position the two smaller squares where the large square was
        docker_container1.move_to(docker_container.get_center() + LEFT)
        docker_container2.move_to(docker_container.get_center() + RIGHT)
        docker_container_group = VGroup(docker_container1, docker_container_label1, docker_container2)
        
        # Animate the appearance of the two smaller squares
        self.play(Create(docker_container_group))
        self.wait(1)
        
        # Animate the two Docker containers moving into the Kubernetes pod
        self.play(docker_container_group.animate.move_to(k8s_pod.get_center()))
        self.wait(2)

        # create a group for the pod and containers
        pod_and_containers = VGroup(k8s_pod_group, docker_container_group)

        # scale the pod and containers down
        self.play(pod_and_containers.animate.scale(0.5))

        # Create exagon to represent the Kubernetes node
        k8s_node = RegularPolygon(n=6, color=RED)
        k8s_node.scale(2.5)
        k8s_node_label = Text("Node", font_size=36)
        k8s_node_label.next_to(k8s_node, UP)
        k8s_node_group = VGroup(k8s_node, k8s_node_label)
        self.play(Create(k8s_node_group))

        # Animate the Kubernetes pod moving into the Kubernetes node
        self.play(pod_and_containers.animate.move_to(k8s_node.get_center()))
        self.wait(2)

        # scale pod and containers down
        self.play(pod_and_containers.animate.scale(0.5))

        # move the pod and containers to the right
        self.play(pod_and_containers.animate.shift(RIGHT))

        # duplicate the pod and containers
        pod_and_containers_copy = pod_and_containers.copy()

        # move the pod and containers to the left 2x
        self.play(pod_and_containers_copy.animate.shift(LEFT*2))

        # create group with node and pod and containers
        node_pod_and_containers = VGroup(k8s_node_group, pod_and_containers, pod_and_containers_copy)
        # scla the group down
        self.play(node_pod_and_containers.animate.scale(0.5))

        # move the group to the right
        self.play(node_pod_and_containers.animate.shift(RIGHT * 2))

        # duplicate the group
        node_pod_and_containers_copy = node_pod_and_containers.copy()
        self.play(node_pod_and_containers_copy.animate.shift(LEFT*4))

        # octagon to represent the Kubernetes master
        k8s_master = RegularPolygon(n=8, color=ORANGE)
        k8s_master_label = Text("Master", font_size=24)
        k8s_master_label.next_to(k8s_master, UP)
        k8s_master_group = VGroup(k8s_master, k8s_master_label)
        # move down
        k8s_master_group.shift(DOWN)
        self.play(Create(k8s_master_group))
        self.wait(2)

        # label inside the master
        k8s_master_label_inside = Text("Deployment", font_size=20)
        # center the label inside the master
        k8s_master_label_inside.move_to(k8s_master.get_center())
        self.play(Write(k8s_master_label_inside))

        # Create a rectangle to wrap both of the node groups
        rectangle = Rectangle(height=2, width=8, color=WHITE)
        
        # Convert the rectangle into a dashed version
        dashed_rectangle = DashedVMobject(rectangle, num_dashes=62, color=WHITE)

        # Display the dashed rectangle
        self.play(Create(dashed_rectangle))
        self.wait(2)

        # Create a label for the service
        service_label = Text("Service", font_size=24)
        service_label.next_to(dashed_rectangle, UP)
        self.play(Write(service_label))
        self.wait(2)

