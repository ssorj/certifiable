from plano import *

image_tag = "quay.io/ssorj/patient-portal-frontend"

@command
def build():
    run(f"podman build -t {image_tag} .")

@command(name="run")
def run_():
    build()
    run(f"podman run --net host {image_tag}")

@command
def push():
    build()
    run(f"podman push {image_tag}")

# hypercorn main:star --certfile service.cert --keyfile service.key --debug
