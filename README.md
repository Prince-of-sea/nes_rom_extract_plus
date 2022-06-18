# nes_rom_extract_plus

## Overview
  [nes_rom_extract](https://github.com/Plombo/romextract/blob/master/src/nes_rom_extract.py)の非公式機能追加版もどきです<br>
  本家および本家の作者とは一切関係ありません<br>


## Build
```
pyinstaller --onefile nes_rom_extract_plus.py
```


## Usage
```
nes_rom_extract_plus.exe [options] input.dol output.nes
```
### Options

 - [-r]Legacy mode(.nes only)<br>
   原作の[nes_rom_extract](https://github.com/Plombo/romextract/blob/master/src/nes_rom_extract.py)と同じように、ROMデータ以下の不要部分の削除を行わなくなります<br>
   通常変換でエラーが起きた際に、この引数を使うと正常に変換できる可能性があります<br>


## License
  [Apache License 2.0](LICENSE)
