import subprocess

print(subprocess.call(['ls', '-la']))


proc = subprocess.Popen(["echo", "Hello from Ivan"], stdout=subprocess.PIPE)
out, err = proc.communicate()
print(out.decode('utf-8'))
