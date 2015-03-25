# visual_field_data_extraction

Several opthalmology studies use visual field analysis to quantify visual defects. However, many of the machines used either do not provide the database containing raw visual field data or are simply too old and provide only paper printouts of visual fields. For this reason, it was necessary to develop an OCR tool to download visual field data from *.PNG files of visual fields into a suiltable format. The *.PNG files were obtained from scanns of old machine printouts, or downloaded from the online OIS visual field file repository

- The vf_test.sh file uses the tesseract OCR to convert humphrey and octopus visual field *.PNG files into text files containing recognized characters. 
- Once the text files are created, the vf_ois.py file searches each text file one by one, looking for distinct pattern matches based on regular expressions. 
- Patterns were designed to match the following fields: MRN, test strategy, fixation losses, false positive error, false negative error, mean deviation, pattern standard deviation, and PSD p-value.
- The output text file containis the above fields in a table which can be importaed direclty to MS excel.
- 
