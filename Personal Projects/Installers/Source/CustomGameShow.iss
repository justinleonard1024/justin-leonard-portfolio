; Custom Game Show Installer
; CustomGameShow.iss
; Created by Justin Leonard

[Setup]
AppId={{92D040CA-4457-447A-9339-11C2DF42F866}
AppName=Custom Game Show
AppVersion=1.0
AppPublisher=Justin Leonard
PrivilegesRequired=admin
DefaultDirName={pf64}\Custom Game Show
DisableDirPage=yes
DefaultGroupName=Custom Game Show
DisableProgramGroupPage=yes
OutputDir=<Target Directory>
OutputBaseFilename=CustomGameShow_Setup
SetupIconFile=<Directory>\Icons\main.ico
UninstallDisplayName=Custom Game Show
UninstallDisplayIcon={app}\CustomGameShow.exe
Compression=lzma
SolidCompression=yes
CloseApplications=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[InstallDelete]
Type: filesandordirs; Name: "{app}"
Type: filesandordirs; Name: "{localappdata}\Custom Game Show"

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
  MsgBox('Make sure to save any custom media files from "<User Name>/AppData/Local/Custom Game Show/Media" before install or uninstall. They will be reset or deleted.', mbInformation, MB_OK);

  Result := True;
end;

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
 
[Files]
Source: "<Directory>\Application\*"; DestDir: "{app}"; Flags: ignoreversion
Source: "<Directory>\Media\*"; DestDir: "{localappdata}\Custom Game Show\Media\"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Custom Game Show"; Filename: "{app}\CustomGameShow.exe"
Name: "{commondesktop}\Custom Game Show"; Filename: "{app}\CustomGameShow.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\CustomGameShow.exe"; Description: "{cm:LaunchProgram,Custom Game Show}"; Flags: runascurrentuser nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
Type: filesandordirs; Name: "{localappdata}\Custom Game Show"