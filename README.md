<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/amethyst-hollow-theme/main/assets/icon.png" alt="Amethyst Hollow Theme logo" width="128">
</p>

<h1 align="center">Amethyst Hollow Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.amethyst-hollow-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-7F5D99?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-9E7EB5?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-C4A4DA?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/amethyst-hollow-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

One violet, four depths. The light variant is near-white paper with violet ink and an amethyst title bar; the dark one drops into a crystal hollow where the same four shades glow from inside.

同一个紫色，四个深浅。浅色版是近白纸配紫墨与紫水晶标题栏，深色版沉进晶洞，同样的四档紫从里面透出光。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Amethyst Hollow Theme Light](https://raw.githubusercontent.com/vaxicy/amethyst-hollow-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Amethyst Hollow Theme Dark](https://raw.githubusercontent.com/vaxicy/amethyst-hollow-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FDFBFF` near-white | `#3A1B4E` crystal hollow |
| Foreground | `#3A2448` violet ink | `#EDE0F5` pale amethyst |
| Muted text / placeholders | `#8A7A94` | `#A995B8` |
| Side bar | `#F8F2FC` | `#331749` |
| Panel / terminal | `#FCF9FE` | `#351850` |
| Title bar | `#C4A4DA` with `#3A2448` text | `#2C143C` with `#D8C6E6` text |
| Tab bar / inactive tab | `#F0E7F7` | `#351850` |
| Active tab / indicator | `#2F1C3C` text, `#7F5D99` top border | `#F5EDFA` text, `#C4A4DA` top border |
| Activity bar | `#E9DCF2` with `#6B4A82` icons | `#291239` with `#C4A4DA` icons |
| Status bar | `#4C2365` with white text | `#4C2365` with `#F5EDFA` text |
| Selection | `#DCC6EA` | `#5A3570` |
| Current line | `#F7F1FB` | `#42205A` |
| Borders | `#E7DBF0` | `#552F6B` |
| Indent guides | `#EDE2F5` | `#452460` |
| Button | `#6B4A82` with white text (hover `#5A3B70`) | `#C4A4DA` with `#2C143C` text (hover `#DCC6EA`) |
| Badge | `#4C2365` with white text | `#C4A4DA` with `#2C143C` text |
| Cursor | `#6B4A82` | `#C4A4DA` |
| Links | `#6B4A82` | `#C4A4DA` |
| Errors / warnings | `#A8455F` / `#8A6B2E` | `#F0A0B4` / `#F0C9A8` |
| Git added / modified / deleted | `#5B7A5E` / `#8A6B2E` / `#A8455F` | `#B8D8C8` / `#F0C9A8` / `#F0A0B4` |

Deep `#4C2365`, mid `#7F5D99`, soft `#9E7EB5` and light `#C4A4DA` carry both variants, so a file still reads as "amethyst hollow" after switching.

深紫 `#4C2365`、中紫 `#7F5D99`、柔紫 `#9E7EB5` 与浅紫 `#C4A4DA` 贯穿明暗两版，切换后整个文件还是同一个晶洞。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#8A7A94` | `#9A85AC` |
| Keywords / storage | `#7A3F98` | `#D9B8EC` |
| Strings | `#9C4F7A` | `#E8B8D8` |
| Functions / methods | `#5B4F9C` | `#C4A4DA` |
| Types / classes | `#3F5F8C` | `#A8BCE8` |
| Numbers / constants | `#8A5A3A` | `#F0C9A8` |
| Variables | `#3A2448` | `#EDE0F5` |
| Parameters | `#5E4A6E` | `#CDBCDC` |
| Properties | `#6B4A82` | `#C4A4DA` |
| Operators | `#7A6A86` | `#B7A6C4` |
| Punctuation | `#8A7A94` | `#9A85AC` |
| HTML tags | `#7A3F98` | `#D9B8EC` |
| Attribute names | `#8A5A9C` | `#E8B8D8` |
| Regex | `#8A6B2E` | `#D9C48A` |
| Escape characters | `#8A5A3A` | `#F0C9A8` |

Semantic highlighting is enabled, so variables, parameters, properties, functions and types follow the same mapping in TypeScript, JavaScript, Go, Rust and Python.

已开启语义高亮，TypeScript、JavaScript、Go、Rust 与 Python 里的变量、参数、属性、函数与类型都会落到同一套配色。

## Install / 安装

1. 打开扩展面板 `Ctrl+Shift+X`。
2. 搜索 **Amethyst Hollow Theme** 并安装。
3. 按 `Ctrl+K Ctrl+T`，选择 `Amethyst Hollow Theme Light` 或 `Amethyst Hollow Theme Dark`。

也可以用命令行安装：

```bash
code --install-extension lilinhuang.amethyst-hollow-theme
```

## Build from source / 本地构建

```bash
py -3 scripts/build-theme.py       # regenerate both theme JSON files
py -3 scripts/generate-icon.py     # export assets/icon.png from the selected logo
py -3 scripts/capture-real-screenshots.py   # real VS Code screenshots
```

## License / 许可证

Non-Commercial License — free for personal, educational and non-commercial use. See [LICENSE](https://github.com/vaxicy/amethyst-hollow-theme/blob/main/LICENSE).

非商业许可证：个人、教育与非商业用途免费使用，详见 LICENSE。
