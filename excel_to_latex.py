
# coding: utf-8
# Ismael Medina, 2017. github.com/literarybraids

"""  PARAMETERS """

filename = 'clipboard'   # Name of the file you want to read. If it is 'None' it will open an input form. 
                         # If it is 'clipboard', it will read whatever you've recently copied.
    
booktabs = True          # If 'True' it will make use of LaTeX package booktabs; 
                         # if 'False' it will use '\hline' for row separation.
    
sep = '\t'               # Character that separates columns, in case you are reading a text file. 
                         # Default is '\t', tab-stop.

which_h_lines = 'tmb'    # 'tmb': LaTeX tabular will have lines enclosing the header and at the bottom.
                         # 'all': all horizontal lines will be displayed.
                         # 'none': no horizontal line will be displayed.
        
write_to_file = None     # Name of the file you want to print the LaTeX tabular. If None, writes to no file.

print_to_screen = True   # By default prints the tabular on screen.


import pandas as pd



""" Here we read the data """

if filename == None:
    filename = raw_input("Filename (write 'clipboard' if you've copied some Excel cells): ")
    
""" Depending on the type of the file you are reading... """
if filename == 'clipboard':
    d = pd.read_clipboard(sep = sep)
elif filename[-4:] == '.txt' or filename[-4:] == '.csv':
    d = pd.read_csv(filename,sep = sep)
elif filename[-4:] == '.xls':
    d = pd.read_excel(filename)




""" We generate the latex code... """
lcode = d.to_latex(index = False)




"""... and format it to meet the parameters """

if booktabs == False:
    for command in ['\\midrule','\\toprule','\\bottomrule']:
        lcode = lcode.replace(command,'\\hline')
    
if which_h_lines == 'tmb':
    pass
elif which_h_lines == 'all':
    lcode = lcode.replace('\\\\\n','\\\\ \\hline \n').replace('\\hline \n\\midrule',' \n\\midrule').replace('\\hline \n\\bottomrule',' \n\\bottomrule')
elif which_h_lines == 'none':
    for command in ['\\midrule','\\toprule','\\bottomrule','\\hline']:
        lcode = lcode.replace(command,'')




""" Last but not least, we print it to screen or to a file """
if print_to_screen == True:
    if len(d) <= 100: #if the number of rows is less than 100
        print("\n")
        print(lcode)
    else:
        if write_to_file == None:
            wos = raw_input("It results a very long tabular.\nIf you want to print it to screen press 'Y'.\nIf you want to print it to a file, write the filename (all previous data in it will be lost): ")
            if wos == 'Y':
                print("\n")
                print(lcode)
            else:
                with open(wos,'w') as f:
                    f.write(lcode)
                    f.close
        else:
            print("It results in a very long tabular. Writing it to the file...")
            
if write_to_file != None: 
    with open(write_to_file,'w') as f:
    	f.write(lcode)
    	f.close


