# pyFMSFilesListParser
pyFMSFilesListParser

Program I wrote to help create HTML table of links to all hosted solutions on a FileMaker Server using the output of fmsadmin list files.

Usage:  On your FileMaker Server, run ```fmsadmin list files > servername_files_list.txt```.

Then run ```pyFMSFilesListParser <input_file> <fmp_server> <output_file>```.

Example:  ```pyFMSFilesListParser servername_files_list.txt filemaker.example.com servername_files_list.html```