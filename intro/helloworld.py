import subprocess as sp
import os
def hello_world():
  output = sp.getoutput('echo "hello world"')
  os.environ["SECRET_DATA"] = str(output)
  myenv = os.environ.get("SECRET_DATA")
  print(myenv)
  return myenv