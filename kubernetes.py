from argparse import Namespace
# from plistlib import UID
import uuid


class Kubernetes:
    def __init__(self, pod_name, namespace):
        self.pod_name = pod_name
        self.namespace = namespace
        self.master_or_follower = None
        self.uid = uuid.uuid1()

    def setup(self):
        return 