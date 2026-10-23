# -*- coding: utf-8 -*-
"""Build the Amethyst Hollow Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "amethyst-hollow-theme"
SLUG = "amethyst-hollow"
DISPLAY = "Amethyst Hollow Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/amethyst-hollow-theme"

UI = {
    "foreground": ("#3A2448", "#EDE0F5"),
    "editor.foreground": ("#3A2448", "#EDE0F5"),
    "terminal.foreground": ("#3A2448", "#EDE0F5"),
    "input.foreground": ("#2F1C3C", "#F5EBFA"),
    "dropdown.foreground": ("#2F1C3C", "#F5EBFA"),
    "quickInput.foreground": ("#2F1C3C", "#F5EBFA"),
    "editorWidget.foreground": ("#2F1C3C", "#F5EBFA"),
    "editorHoverWidget.foreground": ("#2F1C3C", "#F5EBFA"),
    "editorSuggestWidget.foreground": ("#2F1C3C", "#F5EBFA"),
    "notifications.foreground": ("#2F1C3C", "#F5EBFA"),
    "descriptionForeground": ("#8A7A94", "#A995B8"),
    "input.placeholderForeground": ("#8A7A94", "#A995B8"),
    "focusBorder": ("#6B4A82", "#C4A4DA"),
    "inputOption.activeBorder": ("#5A3B70", "#DCC6EA"),
    "input.border": ("#E7DBF0", "#552F6B"),
    "dropdown.border": ("#E7DBF0", "#552F6B"),
    "editor.background": ("#FDFBFF", "#3A1B4E"),
    "tab.activeBackground": ("#FDFBFF", "#3A1B4E"),
    "titleBar.activeBackground": ("#C4A4DA", "#2C143C"),
    "titleBar.activeForeground": ("#3A2448", "#D8C6E6"),
    "titleBar.inactiveBackground": ("#D7C0E6", "#331749"),
    "titleBar.inactiveForeground": ("#6B5578", "#A08BB2"),
    "activityBar.background": ("#E9DCF2", "#291239"),
    "activityBar.foreground": ("#6B4A82", "#C4A4DA"),
    "activityBar.activeBorder": ("#6B4A82", "#C4A4DA"),
    "activityBar.inactiveForeground": ("#A189B2", "#86729A"),
    "sideBar.background": ("#F8F2FC", "#331749"),
    "sideBar.foreground": ("#432C52", "#DCCBE8"),
    "sideBarSectionHeader.background": ("#EFE4F7", "#3B1D51"),
    "sideBarSectionHeader.foreground": ("#4E3560", "#E4D6EE"),
    "panel.background": ("#FCF9FE", "#351850"),
    "terminal.background": ("#FCF9FE", "#351850"),
    "panel.border": ("#E7DBF0", "#552F6B"),
    "editorGroup.border": ("#E7DBF0", "#552F6B"),
    "tab.border": ("#E7DBF0", "#552F6B"),
    "sideBar.border": ("#E7DBF0", "#552F6B"),
    "titleBar.border": ("#E7DBF0", "#552F6B"),
    "statusBar.background": ("#4C2365", "#4C2365"),
    "statusBar.noFolderBackground": ("#4C2365", "#4C2365"),
    "statusBar.foreground": ("#F5EDFA", "#F5EDFA"),
    "statusBar.noFolderForeground": ("#F5EDFA", "#F5EDFA"),
    "statusBarItem.hoverBackground": ("#5C2E78", "#5C2E78"),
    "statusBar.debuggingBackground": ("#8A5A3A", "#7A4A2E"),
    "statusBar.debuggingForeground": ("#FFF6EE", "#F7E8DC"),
    "editorGroupHeader.tabsBackground": ("#F0E7F7", "#351850"),
    "tab.inactiveBackground": ("#F0E7F7", "#351850"),
    "tab.activeForeground": ("#2F1C3C", "#F5EDFA"),
    "tab.activeBorderTop": ("#7F5D99", "#C4A4DA"),
    "tab.inactiveForeground": ("#8A7A94", "#A98BBF"),
    "tab.hoverBackground": ("#EADFF4", "#3B1D51"),
    "tab.activeModifiedBorder": ("#8A5A3A", "#F0C9A8"),
    "tab.inactiveModifiedBorder": ("#8A5A3A", "#F0C9A8"),
    "list.hoverBackground": ("#F5EDFA", "#3B1D51"),
    "list.activeSelectionBackground": ("#DCC6EA", "#5A3570"),
    "editorSuggestWidget.selectedBackground": ("#DCC6EA", "#5A3570"),
    "list.activeSelectionForeground": ("#2F1C3C", "#F5EDFA"),
    "list.inactiveSelectionForeground": ("#2F1C3C", "#F5EDFA"),
    "editorSuggestWidget.selectedForeground": ("#2F1C3C", "#F5EDFA"),
    "list.inactiveSelectionBackground": ("#EADFF4", "#4A2A61"),
    "list.highlightForeground": ("#6B4A82", "#C4A4DA"),
    "list.focusHighlightForeground": ("#6B4A82", "#C4A4DA"),
    "tree.indentGuidesStroke": ("#E4D6EE", "#552F6B"),
    "editorLineNumber.foreground": ("#B5A2C4", "#86729A"),
    "editorLineNumber.activeForeground": ("#6B4A82", "#C4A4DA"),
    "editor.lineHighlightBackground": ("#F7F1FB", "#42205A"),
    "editor.lineHighlightBorder": ("#EFE4F7", "#4A2A61"),
    "editorCursor.foreground": ("#6B4A82", "#C4A4DA"),
    "selection.background": ("#DCC6EA", "#5A3570"),
    "editor.selectionBackground": ("#DCC6EA", "#5A3570"),
    "terminal.selectionBackground": ("#DCC6EA", "#5A3570"),
    "editor.inactiveSelectionBackground": ("#EADFF4", "#4A2A61"),
    "editor.wordHighlightBackground": ("#DCC6EA80", "#6B4A8280"),
    "editor.wordHighlightStrongBackground": ("#DCC6EA80", "#6B4A8280"),
    "editor.selectionHighlightBackground": ("#DCC6EA66", "#6B4A8266"),
    "editor.findMatchHighlightBackground": ("#E6D2F0", "#5F3A78"),
    "editor.findMatchBackground": ("#D4B8E6", "#6B4A82"),
    "editor.findMatchBorder": ("#4C2365", "#DCC6EA"),
    "editorBracketMatch.background": ("#EDE0F5", "#4A2A61"),
    "editorBracketMatch.border": ("#7F5D99", "#9E7EB5"),
    "editorIndentGuide.background1": ("#EDE2F5", "#452460"),
    "editorIndentGuide.activeBackground1": ("#C4A4DA", "#7F5D99"),
    "editorWhitespace.foreground": ("#E4D6EE", "#552F6B"),
    "editorRuler.foreground": ("#F3EAFA", "#42205A"),
    "textLink.foreground": ("#6B4A82", "#C4A4DA"),
    "textLink.activeForeground": ("#5A3B70", "#DCC6EA"),
    "editorLink.activeForeground": ("#5A3B70", "#DCC6EA"),
    "quickInput.background": ("#FEFCFF", "#3B1D51"),
    "editorHoverWidget.background": ("#FEFCFF", "#3B1D51"),
    "notifications.background": ("#FEFCFF", "#3B1D51"),
    "input.background": ("#FFFFFF", "#331749"),
    "dropdown.background": ("#FFFFFF", "#331749"),
    "editorWidget.background": ("#FEFCFF", "#3B1D51"),
    "editorSuggestWidget.background": ("#FEFCFF", "#3B1D51"),
    "editorWidget.border": ("#E7DBF0", "#5F3A78"),
    "editorHoverWidget.border": ("#E7DBF0", "#5F3A78"),
    "editorSuggestWidget.border": ("#E7DBF0", "#5F3A78"),
    "notifications.border": ("#E7DBF0", "#5F3A78"),
    "button.background": ("#6B4A82", "#C4A4DA"),
    "button.foreground": ("#FFFFFF", "#2C143C"),
    "button.hoverBackground": ("#5A3B70", "#DCC6EA"),
    "button.secondaryBackground": ("#EFE4F7", "#4A2A61"),
    "button.secondaryForeground": ("#432C52", "#E4D6EE"),
    "button.secondaryHoverBackground": ("#E4D6EE", "#5A3570"),
    "badge.background": ("#4C2365", "#C4A4DA"),
    "activityBarBadge.background": ("#4C2365", "#C4A4DA"),
    "badge.foreground": ("#FFFFFF", "#2C143C"),
    "activityBarBadge.foreground": ("#FFFFFF", "#2C143C"),
    "scrollbarSlider.background": ("#B5A2C466", "#A995B888"),
    "scrollbarSlider.hoverBackground": ("#9E8AAF88", "#B9A6C899"),
    "scrollbarSlider.activeBackground": ("#87739A99", "#C4A4DA99"),
    "errorForeground": ("#A8455F", "#F0A0B4"),
    "editorError.foreground": ("#A8455F", "#F0A0B4"),
    "problemsErrorIcon.foreground": ("#A8455F", "#F0A0B4"),
    "gitDecoration.deletedResourceForeground": ("#A8455F", "#F0A0B4"),
    "editorGutter.deletedBackground": ("#A8455F", "#F0A0B4"),
    "editorWarning.foreground": ("#8A6B2E", "#F0C9A8"),
    "problemsWarningIcon.foreground": ("#8A6B2E", "#F0C9A8"),
    "editorInfo.foreground": ("#5B4F9C", "#B8C4F0"),
    "problemsInfoIcon.foreground": ("#5B4F9C", "#B8C4F0"),
    "gitDecoration.addedResourceForeground": ("#5B7A5E", "#B8D8C8"),
    "gitDecoration.untrackedResourceForeground": ("#5B7A5E", "#B8D8C8"),
    "editorGutter.addedBackground": ("#5B7A5E", "#B8D8C8"),
    "gitDecoration.modifiedResourceForeground": ("#8A6B2E", "#F0C9A8"),
    "editorGutter.modifiedBackground": ("#8A6B2E", "#F0C9A8"),
    "diffEditor.insertedTextBackground": ("#DCEBDCAA", "#4A2A6166"),
    "diffEditor.removedTextBackground": ("#F0D9E2AA", "#5F3A7866"),
    "diffEditor.insertedLineBackground": ("#DCEBDC66", "#4A2A6144"),
    "diffEditor.removedLineBackground": ("#F0D9E266", "#5F3A7844"),
    "terminal.ansiBlack": ("#3A2448", "#3B1D51"),
    "terminal.ansiRed": ("#A8455F", "#F0A0B4"),
    "terminal.ansiGreen": ("#5B7A5E", "#B8D8C8"),
    "terminal.ansiYellow": ("#8A6B2E", "#F0C9A8"),
    "terminal.ansiBlue": ("#5B4F9C", "#B8C4F0"),
    "terminal.ansiMagenta": ("#7A3F98", "#D9B8EC"),
    "terminal.ansiCyan": ("#4F7A80", "#A8D4DC"),
    "terminal.ansiWhite": ("#8A7A94", "#DCCBE8"),
    "terminal.ansiBrightBlack": ("#6B5578", "#86729A"),
    "terminal.ansiBrightRed": ("#BC5A72", "#F7B8C6"),
    "terminal.ansiBrightGreen": ("#6E8E70", "#CBE4D8"),
    "terminal.ansiBrightYellow": ("#A08038", "#F7DCC0"),
    "terminal.ansiBrightBlue": ("#6E60B0", "#CCD4F7"),
    "terminal.ansiBrightMagenta": ("#8A4FA8", "#E6CCF5"),
    "terminal.ansiBrightCyan": ("#5E8E94", "#C0E4EA"),
    "terminal.ansiBrightWhite": ("#2F1C3C", "#F5EDFA"),
}

TOKENS = [
    ("comment", ("#8A7A94", "#9A85AC"), "italic"),
    (("keyword", "storage"), ("#7A3F98", "#D9B8EC"), None),
    ("string", ("#9C4F7A", "#E8B8D8"), None),
    (("entity.name.function", "support.function"), ("#5B4F9C", "#C4A4DA"), None),
    (("entity.name.type", "support.type", "support.class"), ("#3F5F8C", "#A8BCE8"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#8A5A3A", "#F0C9A8"), None),
    ("variable", ("#3A2448", "#EDE0F5"), None),
    ("variable.parameter", ("#5E4A6E", "#CDBCDC"), None),
    (("variable.other.property", "support.variable.property"), ("#6B4A82", "#C4A4DA"), None),
    ("keyword.operator", ("#7A6A86", "#B7A6C4"), None),
    ("punctuation", ("#8A7A94", "#9A85AC"), None),
    ("entity.name.tag", ("#7A3F98", "#D9B8EC"), None),
    ("entity.other.attribute-name", ("#8A5A9C", "#E8B8D8"), None),
    ("string.regexp", ("#8A6B2E", "#D9C48A"), None),
    ("constant.character.escape", ("#8A5A3A", "#F0C9A8"), None),
    ("markup.heading", ("#2F1C3C", "#F5EDFA"), "bold"),
    ("markup.bold", ("#2F1C3C", "#F5EDFA"), "bold"),
    ("markup.italic", ("#2F1C3C", "#F5EDFA"), "italic"),
    ("invalid", ("#A8455F", "#F0A0B4"), None),
]

SEMANTIC = {
    "variable": "#3A2448|#EDE0F5",
    "parameter": "#5E4A6E|#CDBCDC",
    "property": "#6B4A82|#C4A4DA",
    "function": "#5B4F9C|#C4A4DA",
    "method": "#5B4F9C|#C4A4DA",
    "type": "#3F5F8C|#A8BCE8",
    "class": "#3F5F8C|#A8BCE8",
    "interface": "#3F5F8C|#A8BCE8",
    "variable.readonly": "#8A5A3A|#F0C9A8",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "A deep amethyst palette: near-white paper with violet ink in the light variant, a glowing crystal hollow in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "amethyst", "violet"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#3A1B4E", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
