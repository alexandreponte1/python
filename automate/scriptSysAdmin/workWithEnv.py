from doctest import OutputChecker
import os

stage = os.environ["STAGE"].upper()
output = f"we're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output) 
