; Give AppVer and SourceFolder from command line, eg:
; "C:\Program Files (x86)\Inno Setup 5\iscc" /dAppVer=1.13 /dSourceFolder=build inno_setup.iss 
;#define AppVer "0.11"
;#define InstallerPrefix "thonny"
;#define SourceFolder "C:\workspaces\python_stuff\thonny\packaging\windows\dummy"
#define AppUserModelID "Thonny.Thonny"
#define ThonnyPyProgID "Thonny.py"


[Setup]
AppId=ThonnyPy4t
AppName=ThonnyPy4t
AppVersion={#AppVer}
AppVerName=ThonnyPy4t {#AppVer}
;AppComments string is displayed on the "Support" dialog of the Add/Remove Programs Control Panel applet
AppComments=Thonny is Python IDE for beginners
AppPublisher=Aivar Annamaa (Py4t :Wen-Hung Chang)
AppPublisherURL=https://thonny.org (https://beardad1975.github.io/py4t)
AppSupportURL=https://thonny.org (https://beardad1975.github.io/py4t)
AppUpdatesURL=https://thonny.org (https://beardad1975.github.io/py4t)

; Actual privileges depend on how user started the installer
PrivilegesRequired=lowest
MinVersion=6.0

; Will show important info on welcome page
DisableWelcomePage=no

DisableProgramGroupPage=yes
DefaultGroupName=ThonnyPy4t

; Note that DefaultDirName can be overridden with installer's /DIR=... parameter
DefaultDirName={code:ProposedDir}
DisableDirPage=auto
DirExistsWarning=auto
UsePreviousAppDir=yes

DisableReadyPage=no
AlwaysShowDirOnReadyPage=yes


; Request extra space for precompiling libraries
ExtraDiskSpaceRequired=25000000
OutputDir=dist
OutputBaseFilename={#InstallerPrefix}-{#AppVer}
Compression=lzma2/ultra
SolidCompression=yes

LicenseFile=license-for-win-installer.txt
WizardImageFile=screenshot_with_logo_semidark.bmp
WizardSmallImageFile=small_logo.bmp 
ChangesAssociations=yes

; Signing
; Certum Unizeto provides free certs for open source
; http://www.certum.eu/certum/cert,offer_en_open_source_cs.xml
; http://pete.akeo.ie/2011/11/free-code-signing-certificate-for-open.html
; http://blog.ksoftware.net/2011/07/exporting-your-code-signing-certificate-to-a-pfx-file-from-firefox/
; http://certhelp.ksoftware.net/support/solutions/articles/17157-how-do-i-export-my-code-signing-certificate-from-internet-explorer-or-chrome-
; http://blog.ksoftware.net/2011/07/how-to-automate-code-signing-with-innosetup-and-ksign/
; https://www.digicert.com/code-signing/signcode-signtool-command-line.htm
; http://www.jrsoftware.org/ishelp/index.php?topic=setup_signtool
;
; signtool prefix to be configured in Tools => Configure sign tools:
; $qC:\Program Files (x86)\kSign\signtool.exe$q sign /f $qcertfile.p12$q /p password $p
;SignTool=signtool /tr http://timestamp.digicert.com /td sha256 /fd sha256 /d $qInstaller for Thonny {#AppVer}$q /du $qhttps://thonny.org$q $f


[Languages]
;Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinese_trad"; MessagesFile: "compiler:Languages\ChineseTraditional.isl"

[InstallDelete]
; Clean old installation before copying new files
; (list specific subdirectories to avoid disaster when user selects a wrong directory for installation)
Type: filesandordirs; Name: "{app}\DLLs"
Type: filesandordirs; Name: "{app}\Doc"
Type: filesandordirs; Name: "{app}\include"
Type: filesandordirs; Name: "{app}\Lib"
Type: filesandordirs; Name: "{app}\libs"
Type: filesandordirs; Name: "{app}\Scripts"
Type: filesandordirs; Name: "{app}\tcl"
Type: filesandordirs; Name: "{app}\Tools"
Type: filesandordirs; Name: "{app}\python*"

; Delete old shortcut
Type: filesandordirs; Name: "{userstartmenu}\Thonny"
Type: filesandordirs; Name: "{userstartmenu}\Thonny.lnk"


; LEFTOVERS FROM OBSOLETE VERSIONS
; Delete old format settings. New filename is configuration.ini
Type: filesandordirs; Name: "{%USERPROFILE}\.thonny\preferences.ini"
; Delete backend directory (Thonny occasionally fails to delete it at runtime)
Type: filesandordirs; Name: "{%USERPROFILE}\.thonny\backend"
; Delete old 3rd party libs
Type: filesandordirs; Name: "{%USERPROFILE}\.thonny\Python35"
; TEMP
;Type: filesandordirs; Name: "{%USERPROFILE}\.thonny\BundledPython36"
Type: filesandordirs; Name: "{%USERPROFILE}\.thonny\Py36"

[Tasks]
Name: CreateDesktopIcon; Description: "建立桌面圖示"
; Flags: unchecked;

[Files]
Source: "{#SourceFolder}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{userprograms}\ThonnyPy4t"; Check: StartedForThisUser; Filename: "{app}\thonny.exe"; IconFilename: "{app}\thonny.exe"
Name: "{code:GetActualCommonPrograms}\Thonny"; Check: StartedForAllUsers; Filename: "{app}\thonny.exe"; IconFilename: "{app}\thonny.exe"

Name: "{userdesktop}\ThonnyPy4t"; Check: StartedForThisUser; Filename: "{app}\thonny.exe"; IconFilename: "{app}\thonny.exe"; Tasks: CreateDesktopIcon
Name: "{code:GetActualCommonDesktop}\Thonny"; Check: StartedForAllUsers; Filename: "{app}\thonny.exe"; IconFilename: "{app}\thonny.exe"; Tasks: CreateDesktopIcon


[Registry]
; Check is used to select HKCU or HKLM based on how the installer was started.

; Register the application
; http://msdn.microsoft.com/en-us/library/windows/desktop/ee872121%28v=vs.85%29.aspx
; https://docs.microsoft.com/en-us/windows/desktop/shell/app-registration
; TODO: investigate also SupportedProtocols subkey of this key
Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Microsoft\Windows\CurrentVersion\App Paths\thonny.exe"; ValueType: string; ValueName: "";                 ValueData: "{app}\thonny.exe"; Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Microsoft\Windows\CurrentVersion\App Paths\thonny.exe"; ValueType: string; ValueName: "";                 ValueData: "{app}\thonny.exe"; Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe";                       ValueType: string; ValueName: "";                 ValueData: "Thonny";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe";                       ValueType: string; ValueName: "";                 ValueData: "Thonny";  Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe";                       ValueType: string; ValueName: "FriendlyAppName";  ValueData: "Thonny";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe";                       ValueType: string; ValueName: "FriendlyAppName";  ValueData: "Thonny";  Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe";                       ValueType: string; ValueName: "AppUserModelID";   ValueData: "{#AppUserModelID}";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe";                       ValueType: string; ValueName: "AppUserModelID";   ValueData: "{#AppUserModelID}";  Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe\SupportedTypes";        ValueType: string; ValueName: ".py";              ValueData: "";        Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe\SupportedTypes";        ValueType: string; ValueName: ".py";              ValueData: "";        Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe\SupportedTypes";        ValueType: string; ValueName: ".pyw";             ValueData: "";        Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe\SupportedTypes";        ValueType: string; ValueName: ".pyw";             ValueData: "";        Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe\shell\open\command";    ValueType: string; ValueName: "";                 ValueData: """{app}\thonny.exe"" ""%1"""; Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe\shell\open\command";    ValueType: string; ValueName: "";                 ValueData: """{app}\thonny.exe"" ""%1"""; Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Applications\thonny.exe\shell\Edit with Thonny\command";   ValueType: string; ValueName: "";      ValueData: """{app}\thonny.exe"" ""%1"""; Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Applications\thonny.exe\shell\Edit with Thonny\command";   ValueType: string; ValueName: "";      ValueData: """{app}\thonny.exe"" ""%1"""; Flags: uninsdeletekey

; Add link to Thonny under existing Python.File ProgID
Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Python.File\shell\Edit with Thonny"; ValueType: none; Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Python.File\shell\Edit with Thonny"; ValueType: none; Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\Python.File\shell\Edit with Thonny\command"; ValueType: string; ValueName: ""; ValueData: """{app}\thonny.exe"" ""%1""";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\Python.File\shell\Edit with Thonny\command"; ValueType: string; ValueName: ""; ValueData: """{app}\thonny.exe"" ""%1""";  Flags: uninsdeletekey

; Create separate ProgID (Thonny.py) which represents Thonny's ability to handle Python files
; These settings will be used when user chooses Thonny as default program for opening *.py files
Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "";                 ValueData: "Python file";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "";                 ValueData: "Python file";  Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "FriendlyTypeName"; ValueData: "Python file";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "FriendlyTypeName"; ValueData: "Python file";  Flags: uninsdeletekey

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "AppUserModelID"; ValueData: "{#AppUserModelID}";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "AppUserModelID"; ValueData: "{#AppUserModelID}";  Flags: uninsdeletekey

;Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "EditFlags"; TODO: https://docs.microsoft.com/en-us/windows/desktop/api/Shlwapi/ne-shlwapi-filetypeattributeflags
;Root: HKCU; Check: StartedForAllUsers; Subkey: "Software\Classes\{#ThonnyPyProgID}"; ValueType: string; ValueName: "EditFlags"; TODO: https://docs.microsoft.com/en-us/windows/desktop/api/Shlwapi/ne-shlwapi-filetypeattributeflags

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\{#ThonnyPyProgID}\shell\open\command";     ValueType: string; ValueName: ""; ValueData: """{app}\thonny.exe"" ""%1""";  Flags: uninsdeletekey
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\{#ThonnyPyProgID}\shell\open\command";     ValueType: string; ValueName: ""; ValueData: """{app}\thonny.exe"" ""%1""";  Flags: uninsdeletekey

; Relate this ProgID with *.py and *.pyw extensions
; https://docs.microsoft.com/en-us/windows/desktop/shell/how-to-include-an-application-on-the-open-with-dialog-box
Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\.py\OpenWithProgIds";  ValueType: string; ValueName: "{#ThonnyPyProgID}";   Flags: uninsdeletevalue
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\.py\OpenWithProgIds";  ValueType: string; ValueName: "{#ThonnyPyProgID}";   Flags: uninsdeletevalue

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\.pyw\OpenWithProgIds"; ValueType: string; ValueName: "{#ThonnyPyProgID}";   Flags: uninsdeletevalue
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\.pyw\OpenWithProgIds"; ValueType: string; ValueName: "{#ThonnyPyProgID}";   Flags: uninsdeletevalue

; Add "Python file" to Explorer's "New" context menu (don't remove on uninstallation)
Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\.py\ShellNew";  ValueType: string; ValueData: "Python.File";  
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\.py\ShellNew";  ValueType: string; ValueData: "Python.File";  

Root: HKCU; Check: StartedForThisUser; Subkey: "Software\Classes\.py\ShellNew";  ValueType: string; ValueName: "NullFile"; ValueData: "";  
Root: HKLM; Check: StartedForAllUsers; Subkey: "Software\Classes\.py\ShellNew";  ValueType: string; ValueName: "NullFile"; ValueData: "";  

; Cleaning up old stuff
; Was: Restore "Edit with IDLE" when selecting Thonny as default opener
Root: HKCU; Subkey: "Software\Classes\{#ThonnyPyProgID}\shell\Edit with IDLE"; ValueType: none; Flags: deletekey dontcreatekey uninsdeletekey

[Run]
Filename: "{app}\pythonw.exe"; Parameters: "-m compileall ."; StatusMsg: "正在編譯標準函式庫... (需花費一些時間)"


[UninstallDelete]
Type: filesandordirs; Name: "{app}\*"
Type: filesandordirs; Name: "{app}"

[Messages]
FinishedHeadingLabel=Great success!



[Code]

var
  QuoteLabel: TLabel;
  Upgraded : Boolean;

function GetActualCommonPrograms(Param: String): String;
begin
    // Can't use {commonprograms} because I have PrivilegesRequired=lowest
    Result := GetShellFolderByCSIDL($17, True);
end;

function GetActualCommonDesktop(Param: String): String;
begin
    // Can't use {commondesktop} because I have PrivilegesRequired=lowest
    Result := GetShellFolderByCSIDL($19, True);
end;

function StartedForAllUsers(): Boolean;
begin
    Result := IsAdminLoggedOn();
end;

function StartedForThisUser(): Boolean;
begin
    Result := not IsAdminLoggedOn();
end;

function InstalledForAllUsers(): Boolean;
begin
    Result := RegKeyExists(HKEY_LOCAL_MACHINE, 'Software\Classes\Applications\thonny.exe');
end;

function InstalledForThisUser(): Boolean;
begin
    Result := RegKeyExists(HKEY_CURRENT_USER, 'Software\Classes\Applications\thonny.exe');
end;


function ProposedDir(Param: String): String;
begin
    if ExpandConstant('{param:DIR|-}') <> '-' then
      Result := ExpandConstant('{param:DIR}')
    else if StartedForAllUsers() then
      Result := ExpandConstant('{pf}\Thonny')
    else
      Result := ExpandConstant('{userpf}\Thonny');
end;

function GetRandomQuote(): String;
var
    Quotes: array[0..9] of string;
begin
    Quotes[0] := 'Ninety-ninety rule: The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time.'#13#10'– Tom Cargill ';
    Quotes[1] := 'Now is better than never.'#13#10'– Tim Peters ';
    Quotes[2] := 'Give someone a program, frustrate them for a day; teach them how to program, frustrate them for a lifetime.'#13#10#13#10'– David Leinweber ';
    Quotes[3] := 'Talk is cheap. Show me the code.'#13#10#13#10'– Linus Torvalds ';
    Quotes[4] := 'Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.'#13#10#13#10'– Patrick McKenzie ';
    Quotes[5] := 'Formal education will make you a living. Self-education will make you a fortune.'#13#10#13#10'– Jim Rohn ';
    Quotes[6] := 'First do it, then do it right, then do it better.'#13#10#13#10'– Addy Osmani ';
    Quotes[7] := 'If you want to set off and go develop some grand new thing, you don''t need millions of dollars of capitalization. You need enough pizza and Diet Coke to stick in your refrigerator, a cheap PC to work on and the dedication to go through with it.'#13#10'– John Carmack ';
    Quotes[8] := 'Computers are useless. They can only give you answers.'#13#10#13#10'– Pablo Picasso ';
    Quotes[9] := 'The best way to predict the future is to invent it.'#13#10#13#10'– Alan Kay ';

    Result := Quotes[StrToInt(GetDateTimeString('ss', #0, #0)) mod Length(Quotes)];
end;

procedure InitializeWizard;
var
  MoreInfoLabel: TLabel;
  DualWarningLabel: TLabel;
begin
  Upgraded := False;
  WizardForm.WelcomeLabel1.Caption := '安裝 ThonnyPy4t 整合環境';

  MoreInfoLabel := TLabel.Create(WizardForm);
  DualWarningLabel := TLabel.Create(WizardForm);

  if StartedForAllUsers() then
  begin
    WizardForm.WelcomeLabel2.Caption := '安裝程式正在為所有使用者安裝 ThonnyPy4t {#AppVer}.';
    MoreInfoLabel.Caption := '';
    if InstalledForThisUser() then
    begin    
      DualWarningLabel.Caption := '警告!'
          + ''#13#10''
          + ''#13#10''
          + '目前使用者已經安裝 ThonnyPy4t . 為了避免混亂, 建議你取消安裝程式, 把原本的thonnyPy4t先移除';
    end
    else if InstalledForAllUsers() then
    begin
      WizardForm.WelcomeLabel2.Caption := '安裝程式將會升級 ThonnyPy4t 到版本{#AppVer}.';
      Upgraded := True;
    end;
  end
  else  // single user
  begin
    WizardForm.WelcomeLabel2.Caption := '安裝程式將會為你的帳號安裝 ThonnyPy4t {#AppVer} ';
    if InstalledForAllUsers() then
    begin    
      MoreInfoLabel.Caption := '如果想要為所有使用者安裝 ThonnyPy4t, 請取消安裝程式並將thonnyPy4t解除安裝後，再以管理員執行安裝'
          + '(於安裝檔按滑鼠右鍵並選擇"以管理員身份執行").';
      DualWarningLabel.Caption := 'Warning!'
        + ''#13#10''
        + ''#13#10''
        + '看起來已為所有使用者安裝了 ThonnyPy4t. 為了避免混亂, 建議你取消安裝程式, 把原本的thonnyPy4t先移除.';
    end
    else if InstalledForThisUser() then
    begin
      WizardForm.WelcomeLabel2.Caption := '安裝程式將會升級 ThonnyPy4t到版本 {#AppVer}.';
      MoreInfoLabel.Caption := '如果你想要為所有使用者安裝 ThonnyPy4t, 請取消程式後,移除ThonnyPy4t後, 以管理員身份執行'
          + '(於安裝檔按滑鼠右鍵並選擇"以管理員身份執行").';
      Upgraded := True;
    end
    else
    begin
      MoreInfoLabel.Caption := '如果你想要為所有使用者安裝 ThonnyPy4t, 請取消程式後以管理員身份執行'
          + '(於安裝檔按滑鼠右鍵並選擇"以管理員身份執行").';
    end;

  end;


  WizardForm.WelcomeLabel2.AutoSize := True;

  MoreInfoLabel.Parent := WizardForm.WelcomePage;
  MoreInfoLabel.AutoSize := True;
  MoreInfoLabel.WordWrap := True;
  MoreInfoLabel.Left := WizardForm.WelcomeLabel2.Left;
  MoreInfoLabel.Width := WizardForm.WelcomeLabel2.Width;
  MoreInfoLabel.Font.Style := [fsItalic];
  MoreInfoLabel.Top := WizardForm.WelcomeLabel2.Top + WizardForm.WelcomeLabel2.Height + ScaleY(20);

  DualWarningLabel.Parent := WizardForm.WelcomePage;
  DualWarningLabel.AutoSize := True;
  DualWarningLabel.WordWrap := True;
  DualWarningLabel.Left := WizardForm.WelcomeLabel2.Left;
  DualWarningLabel.Width := WizardForm.WelcomeLabel2.Width;
  DualWarningLabel.Font.Style := [fsBold];
  //DualWarningLabel.Color := clRed;
  DualWarningLabel.Top := WizardForm.WelcomePage.Height - DualWarningLabel.Height - ScaleY(20);
  
  // Quotes
  QuoteLabel := TLabel.Create(WizardForm);
  QuoteLabel.Caption := GetRandomQuote();

  QuoteLabel.Parent := WizardForm.FinishedPage;

  // make accepting license the default
  WizardForm.LicenseAcceptedRadio.Checked := True;

end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  if (CurPageID = wpSelectDir) and (pos('&', WizardDirValue) > 1) then
  begin
    MsgBox('Directory paths containing "&" are known to cause problems in Thonny'
          + ''#13#10''
          + 'Please choose another directory!', mbError, MB_OK);
    Result := False
  end
  else
  begin
    Result := True
  end;
end;

procedure CurPageChanged(CurPageID: Integer);
begin
    if CurPageID = wpFinished then
    begin
      if Upgraded then
        WizardForm.FinishedLabel.Caption := 'ThonnyPy4t已升級.'
      else
        WizardForm.FinishedLabel.Caption := 'ThonnyPy4t已安裝完成.'
      end;
      WizardForm.FinishedLabel.Caption := WizardForm.FinishedLabel.Caption 
        + ' Run it via shortcut or right-click a *.py file and select "Edit with Thonny".';

      WizardForm.FinishedLabel.AutoSize := True;

      QuoteLabel.WordWrap := True;
      QuoteLabel.Width := round(WizardForm.FinishedLabel.Width * 0.8);
      QuoteLabel.AutoSize := True;
      
      // for some reason AutoSize doesn't work for longer quotes -- they are cropped from the bottom
      QuoteLabel.Height := ScaleY(60);
      if Length(QuoteLabel.Caption) > 100 then
      begin
        QuoteLabel.Height := ScaleY(80);
      end;
      QuoteLabel.Left := WizardForm.FinishedLabel.Left + (WizardForm.FinishedLabel.Width - QuoteLabel.Width);
      QuoteLabel.Alignment := taRightJustify;
      //QuoteLabel.Font.Style := [fsItalic]; // causes cropping in leftmost letters
      
      QuoteLabel.Top := WizardForm.FinishedPage.Height - QuoteLabel.Height - ScaleY(20);
    end;
end.