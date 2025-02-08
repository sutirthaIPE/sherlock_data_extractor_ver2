Here we created a dataextractor for reading a particular summary.xml file. 

From the Sherleock simulation we generate the .xml file, where we have the sherlock metrology and defect informations.  

'''THis extractor will take the file and generate the incoming and outgoing corner metrology data by unit. This corner metrology data will check by our tool with a limit of +- 450 um limit 
and if the limit exceed then sherlock algorithm flagged as incoming and outoging GO/NOGO'''

Once the NOGO trigger sherlock will flag the unit as 100520 (incominig corner X and Y metrology check) /100521 (incominig corner X and Y metrology check) Losscode.

Below is a sample from a summary.xml file :

![image](https://github.com/user-attachments/assets/30a28821-59f4-4053-8b66-2cd00d32ca10)
