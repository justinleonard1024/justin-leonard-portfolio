; Unreal Half Life Installer
; UnrealHalfLife.iss
; Created by Justin Leonard

[Setup]
AppId={{22ADF620-2398-461C-AEE6-5AF3E2E3E71C}
AppName=Unreal Half Life
AppVersion=1.0
AppPublisher=Justin Leonard
PrivilegesRequired=admin
DefaultDirName={pf64}\Unreal Half Life
DisableDirPage=yes
DefaultGroupName=Unreal Half Life
DisableProgramGroupPage=yes
OutputDir=<Target Directory>
OutputBaseFilename=UnrealHalfLife_Setup
SetupIconFile=<Directory>\Icons\unreal_hl2_icon.ico
UninstallDisplayName=Unreal Half Life 
UninstallDisplayIcon={app}\Unreal Half Life.exe
Compression=lzma
SolidCompression=yes
CloseApplications=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[InstallDelete]
Type: filesandordirs; Name: {app}
Type: filesandordirs; Name: "{pf}\Steam\SteamApps\common\Half-Life 2\hl2\unreal"

[Code]
procedure InitializeWizard;
begin
  with TNewStaticText.Create(WizardForm) do
  begin
    Parent := WizardForm.FilenameLabel.Parent;
    Left := WizardForm.FilenameLabel.Left;
    Top := WizardForm.FilenameLabel.Top;
    Width := WizardForm.FilenameLabel.Width;
    Height := WizardForm.FilenameLabel.Height;
  end;
  WizardForm.FilenameLabel.Visible := False;
end;

function InitializeSetup(): Boolean;
begin
  MsgBox('Make sure Half-Life 2 is installed on your main drive or the game cannot be played.', mbInformation, MB_OK);

  Result := True;
end;

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
 
[Files]
Source: "<Directory>\Setup Files\*"; DestDir: "{app}"; Flags: ignoreversion
Source: "<Directory>\Game Assets\*"; DestDir: "{pf}\Steam\steamapps\common\Half-Life 2\hl2"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Unreal Half Life"; Filename: "{app}\UnrealHalfLife.exe"
Name: "{commondesktop}\Unreal Half Life"; Filename: "{app}\UnrealHalfLife.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\UnrealHalfLife.exe"; Description: "{cm:LaunchProgram,Unreal Half Life}"; Flags: runascurrentuser nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: {app}
Type: filesandordirs; Name: "{pf}\Steam\SteamApps\common\Half-Life 2\hl2\unreal"