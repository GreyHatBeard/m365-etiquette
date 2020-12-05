import os

def runMerge(folderPath):
    dirFiles = os.listdir('./' + folderPath)
    dirFiles.sort(reverse=True)
    fileList = ""
    for foundFile in dirFiles:
        fileList += "\"${PWD}/" + folderPath + "/" + foundFile + "\" "
    print(fileList)

    os.system('mdmerge -o ' + folderPath + '.md ' + fileList)
    return

os.system('mdmerge -o docs/merged.md ${PWD}/docs/By-approach/asking-questionsorig.md ${PWD}/docs/By-approach/communicatingorig.md ${PWD}/docs/By-approach/files.md ${PWD}/docs/By-approach/liking-posts ${PWD}/docs/By-approach/voice.md ${PWD}/docs/By-approach/working-out-loud.md ${PWD}/docs/By-service/onenoteorig.md ${PWD}/docs/By-service/outlookorig.md ${PWD}/docs/By-service/plannerorig.md ${PWD}/docs/By-service/teamsorig.md')

runMerge('docs/By-approach/Asking-questions')
runMerge('docs/By-approach/Communicating')
runMerge('docs/By-approach/Liking-posts')
runMerge('docs/By-approach/Files')
runMerge('docs/By-approach/Voice')
runMerge('docs/By-approach/Working-out-loud')

runMerge('docs/By-service/OneNote')
runMerge('docs/By-service/Outlook')
runMerge('docs/By-service/Planner')
runMerge('docs/By-service/Teams')