from kubeconfig import KubeConfig

k8s_con = KubeConfig("pod A1", "default")

# print(k8s_con.pod_name, k8s_con.uid, k8s_con.namespace)
uid = k8s_con.uid
