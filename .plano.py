from plano import *

@command
def build():
    check_program("certtool")

    make_dir("build")

    run("certtool --generate-privkey --bits 4096 --outfile build/server-key.pem")
    run("chmod 600 build/server-key.pem")
    run("certtool --generate-self-signed --load-privkey build/server-key.pem --outfile build/server-cert.pem --template server.template")
    run("certtool --certificate-info --infile build/server-cert.pem")

    run("certtool --generate-privkey --bits 4096 --outfile build/client-key.pem")
    run("chmod 600 build/client-key.pem")
    run("certtool --generate-self-signed --load-privkey build/client-key.pem --outfile build/client-cert.pem --template client.template")
    run("certtool --certificate-info --infile build/client-cert.pem")

@command
def clean():
    remove("build")
    remove(find("__pycache__"))

@command
def verify():
    check_program("openssl")

    run("openssl verify -trusted build/server-cert.pem build/server-cert.pem")
    run("openssl verify -trusted build/client-cert.pem build/client-cert.pem")

@command
def run_server():
    check_program("openssl")

    run("openssl s_server -cert build/server-cert.pem -key build/server-key.pem -trusted build/client-cert.pem -verify 1")

@command
def run_client():
    check_program("openssl")

    run("openssl s_client -cert build/client-cert.pem -key build/client-key.pem -trusted build/server-cert.pem")

@command
def server_info():
    check_program("openssl")

    run("openssl x509 -in build/server-cert.pem -text")

@command
def client_info():
    check_program("openssl")

    run("openssl x509 -in build/client-cert.pem -text")
