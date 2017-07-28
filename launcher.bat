SET HPCInfo= /jobtemplate:core /priority:"Lowest"  /scheduler:monsoon 
NET USE L: "%PathRoot1%"    /persistent:no
start /b job submit %HPCInfo% /jobname:Turbsimtesrer ". tester.bat"
