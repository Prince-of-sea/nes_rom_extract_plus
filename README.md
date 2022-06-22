# nes_rom_extract_plus

## Overview
  [nes_rom_extract](https://github.com/Plombo/romextract/blob/master/src/nes_rom_extract.py)の非公式機能追加版もどきです<br>
  fds変換(v0.2.0~)、bios抽出(v0.3.0~)機能もついています<br>
  本家および本家の作者とは一切関係ありません<br>
  <br>
  現時点で以下のデータに対応している**はず**(詳細未確認)<br>
   - [GC]ゼルダコレクションの.qdファイル{→.fds}
   - [GC]どうぶつの森+/e+の.qdファイル{→.fds}
   - [Wii]ファミコン系VC全般の0000000x.appファイル{→.nes/.fds}<br>
     - 一部非対応マッパーあり
   - [Wii]スマブラXのmain.dolファイル{→.nes/.fds}<br>
     - SFC系ROMは現時点では非対応
   - [Wii]20th カービィのFC_yume.dolファイル{→.nes}<br>
     - SFC系ROMは現時点では非対応
   - [Wii]25th DQ1/2/3のhvc.dolファイル{→.nes}<br>
     - DQ1のみ、FC2/3は非対応
   - [WiiU]ファミコンリミックス1+2の.binファイル{→.nes/.fds}<br>
   - [WiiU]タッチ! amiiboの.binファイル{→.nes/.fds}<br>
     - SFC系ROMは現時点では非対応


## Build
```
pyinstaller --onefile nes_rom_extract_plus.py
```
[＞＞ビルド済みファイルはこちら](https://github.com/Prince-of-sea/nes_rom_extract_plus/releases/latest)


## Usage
 - nesファイル抽出時
```
nes_rom_extract_plus.exe [options] input.dol output.nes
```
 - fdsファイル抽出時
```
nes_rom_extract_plus.exe [options] input.dol output.fds
```
 - fds bios抽出時 - CRC:5E607DCF
```
nes_rom_extract_plus.exe [options] input.dol output.rom
```

### Options
 - [ -l ]Legacy mode(.nes only)<br>
   原作の[nes_rom_extract](https://github.com/Plombo/romextract/blob/master/src/nes_rom_extract.py)と同じように、ROMデータ以下の不要部分の削除を行わなくなります<br>
   通常変換でエラーが起きた際に、この引数を使うと正常に変換できる可能性があります<br>
 - [ -nh ]No Header(.fds only)<br>
   出力するROMにヘッダを付加しなくなります<br>
   エミュレータで利用できなくなる可能性があります<br>
 - [ -nf ]No Fix(.nes / FDS BIOS)<br>
   抽出したBIOSに対して特定箇所のバイナリ修正を行わなくなります<br>
   CRCが一致しなくなり、エミュレータで利用できなくなる可能性があります<br>


## License
  [Apache License 2.0](LICENSE)
