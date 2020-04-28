import subprocess # Used to interact with command line
import os

DEFAULT_FME_LOCATION = "C:\\Program Files\\FME\\fme.exe"
WORKSPACE_RELATIVE_PATH = ".\\" # located in the same directory

def wrapInQuotes(str):
    return "\"{0}\"".format(str)

def runRevitConverter(fmeLocation, sourceDataset, outputDir, resultFileName=None):
    if resultFileName is None:
        resultFileName = os.path.basename(sourceDataset).replace(".rvt", "_rvt")
    workspaceLocation = os.path.abspath(os.path.join(WORKSPACE_RELATIVE_PATH, "revitNativeToCsv.fmw"))
    command = "{0} {1} --SourceDataset_REVITNATIVE_3 {2} --DestDataset_CSV2 {3} --FEATURE_TYPES \"\" --resultFileName {4}"
    command = command.format(
        wrapInQuotes(fmeLocation),
        wrapInQuotes(workspaceLocation),
        wrapInQuotes(sourceDataset),
        wrapInQuotes(outputDir),
        wrapInQuotes(resultFileName)
    )
    print("Running command " + command)

    # https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        shell=True,
        universal_newlines=True
    )
    for line in iter(process.stdout.readline, ""):
        print(line.strip())

    process.stdout.close()
    result = process.wait()
    print("Process returned {0}".format(result))
    return os.path.join(os.path.abspath(outputDir), resultFileName + ".csv")

def convert(fmeLocation, sourceDataset, outputDir, resultFileName=None):
    extention = os.path.splitext(os.path.basename(sourceDataset))[1]
    output = None
    if extention == ".rvt":
        output = runRevitConverter(fmeLocation, sourceDataset, outputDir, resultFileName)
    else:
        raise ValueError("Don't have a converter for file type \"{0}\"".format(extention))

    print("Wrote to {0}".format(output))
