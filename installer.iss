; ------------------------------
; Inno Setup Script for Offline LLM Tool
; ------------------------------

[Setup]
AppName=Offline LLM Tool
AppVersion=1.0
DefaultDirName={pf}\Offline LLM Tool
DefaultGroupName=Offline LLM Tool
OutputDir=.
OutputBaseFilename=Offline_LLM_Tool_Installer
Compression=lzma
SolidCompression=yes
WizardStyle=modern
DiskSpanning=yes
DiskSliceSize=2100000000

[Files]
; Copy everything from your PyInstaller dist folder
Source: "dist\launcher\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
; Desktop shortcut
Name: "{commondesktop}\Offline LLM Tool"; Filename: "{app}\launcher.exe"
; Start Menu shortcut
Name: "{group}\Offline LLM Tool"; Filename: "{app}\launcher.exe"

[Run]
; Launch app after installation
Filename: "{app}\launcher.exe"; Description: "Launch Offline LLM Tool"; Flags: nowait postinstall skipifsilent
