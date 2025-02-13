# Data Extractor from Sherlock Simulation output File (Summary.xml)

Author : Sutirtha Chowdhury, STTD, IPE
WWID : 12140215

=============================================================================


**Background:**


We perform sherlock (image analysis software) simulation to understand the die defects / vision metrology data at Sort. Simulation is always beneficial to naviagate the issues prior to run online at SDX tool to see any issues, or if we need offline data for t/s. Once Engineer runs the sherlock simulations and read the defect / metrology data from a .xml file, it is very time consuming. To minimize the engeneering time, here we created a dataextractor for reading metrology information from a particular summary.xml file. 


**Example**


This extractor / Parser will take the .xml file and generate an incoming and outgoing corner metrology plot per unit. This corner metrology data will check by our SDX tool with a limit of +- 450 um limit and if the limit exceed during online run then sherlock algorithm flagged as incoming and outoging NOGO Once the NOGO trigger sherlock will flag the unit as 100520 (incominig corner X and Y metrology check) /100521 (incominig corner X and Y metrology check) Losscode. Here in this work, we generate this incoming and outgoing metrology data using this parser to see the distribution.

Below is a sample data from a summary.xml file :

![image](https://github.com/user-attachments/assets/30a28821-59f4-4053-8b66-2cd00d32ca10)
