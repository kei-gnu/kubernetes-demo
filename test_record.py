from kubernetes import Kubernetes

k8s = Kubernetes("pod A1", "default")

print(k8s.pod_name)
