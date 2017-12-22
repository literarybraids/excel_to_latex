# excel_to_latex

A simple Python script that turns Excel (among other formats) to LaTeX tabulars.

## Requisites

Having Python installed in your computer.
excel_to_latex also makes use of Python module pandas, so you'll have to have it installed too.
Soon I'll upload a .exe file too.

## Default use

Simple: select the cells you want from an Excel or OpenOffice file, copy them and call excel_to_latex: <br>
``` python excel_to_latex.py ```

It will read your clipboard and get you a LaTeX tabular. Of course you can as well run it from a Python console.

## Other uses

If you open the file excel_to_latex.py you will find some parameteres you can change. These are:

<ul>
  <li>filename: Default is 'clipboard'. It encodes the name of the file you want to read. If it is 'clipboard', it will read whatever you've recently copied. Nevertheless you can also read files from your computer: 
    <ul>
    <li> If instead of 'clipboard' you have simply None, the program will open an input form for you to write the file you desire to open. 
     <li> Also you can write directly the name of your file, (for example filename = '\Documents\data.txt')  and it will read that file. Supported filetypes are .xls, .txt and .csv.
</ul>
  <li>booktabs: Default is True, in which case it will make use of LaTeX package booktabs. If False it will use '\hline' for row separation.</li>
  <li>sep: Default is '\t'. Character that separates columns, in case you are reading a text file. </li>
  <li>which_h_lines: Default is 'tmb', in which case LaTeX tabular will have horizontal lines lines enclosing the header and at the bottom. If it's 'all', all horizontal lines will be displayed. If it's 'none', no horizontal line will be displayed.</li>
  <li>write_to_file: Default is None, in which case it writes no file. If it is 'bla.txt', it writes the code for the tabular to bla.txt.</li>
  <li>print_to_screen: Default is True, in which case prints the tabular on screen.</li>
</ul>
