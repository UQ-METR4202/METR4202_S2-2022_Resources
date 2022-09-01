if [ -n "$ZSH_VERSION" ]; then
  read -r "answer?"
else
  read -r answer
fi

pdflatex tex/$answer.tex > /dev/null
pdf2svg $answer.pdf $answer.svg
inkscape --export-type=png --export-filename=png/$answer.png $answer.svg -w 1024
rm $answer.aux $answer.log $answer.pdf $answer.svg