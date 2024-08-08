import os



stage = os.getenv("STAGE", default="dev").upper()

# stage = os.environ["STAGE"].upper()

output = f"we're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)



#export STAGE=staging
#export STAGE=prod