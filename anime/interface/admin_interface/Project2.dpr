program Project2;

uses
  Vcl.Forms,
  admin_interface in 'admin_interface.pas' {Form1};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
