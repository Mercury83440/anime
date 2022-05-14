object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Form1'
  ClientHeight = 308
  ClientWidth = 308
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object LabeledEdit1: TLabeledEdit
    Left = 80
    Top = 48
    Width = 121
    Height = 21
    EditLabel.Width = 79
    EditLabel.Height = 13
    EditLabel.Caption = 'Nom d'#39'utilisateur'
    TabOrder = 0
  end
  object LabeledEdit2: TLabeledEdit
    Left = 80
    Top = 104
    Width = 121
    Height = 21
    EditLabel.Width = 68
    EditLabel.Height = 13
    EditLabel.Caption = 'Nots de passe'
    TabOrder = 1
  end
  object RadioButton1: TRadioButton
    Left = 80
    Top = 144
    Width = 113
    Height = 17
    Caption = 'user'
    TabOrder = 2
  end
  object RadioButton2: TRadioButton
    Left = 151
    Top = 144
    Width = 113
    Height = 17
    Caption = 'Admin'
    TabOrder = 3
  end
  object Button1: TButton
    Left = 80
    Top = 192
    Width = 121
    Height = 33
    Caption = 'Valider'
    TabOrder = 4
  end
  object Button2: TButton
    Left = 80
    Top = 231
    Width = 121
    Height = 34
    Caption = 'S'#39'incrire'
    TabOrder = 5
  end
end
