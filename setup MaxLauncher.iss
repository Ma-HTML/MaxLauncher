[Setup]
AppName=MaxLuncher
AppVersion=1.0
DefaultDirName={pf}\MaxLuncher
DefaultGroupName=MaxLuncher
OutputDir=.\Output
OutputBaseFilename=MaxLuncher
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\slemaire\Downloads\MaxLuncher\main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\slemaire\Downloads\MaxLuncher"; DestDir: "{app}\resources"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\MaxLuncher"; Filename: "{app}\MaxLuncher.exe"

[Run]
Filename: "{app}\MaxLuncher.exe"; Description: "Lancer MaxLuncher"; Flags: nowait postinstall
