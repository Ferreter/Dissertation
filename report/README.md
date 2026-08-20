# Dissertation report workspace

This folder is the working LaTeX version of the final dissertation. The submitted interim source is preserved under `archive/interim/` and is not compiled directly.

## Build

Run from this folder:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Clean generated LaTeX files with:

```powershell
latexmk -c
```

`main.pdf` is a working draft and still contains visible draft-task boxes. Remove every draft box before the supervisor draft is submitted.
