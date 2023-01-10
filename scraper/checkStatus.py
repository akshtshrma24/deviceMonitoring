import subprocess

#checks if Ip is up 
def is_up(ip):
    try:
        p = subprocess.check_call(["curl -I {}".format(ip)], shell=True, timeout=30)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False
    else:
        return True
