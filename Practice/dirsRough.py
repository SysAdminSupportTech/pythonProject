Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> dirs = os.listdir()
>>> print(dirs)
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python39.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> os.getcwd()
'C:\\Users\\DeptAdmin\\AppData\\Local\\Programs\\Python\\Python39'
>>> home = os.path.expanduser("~")
>>> setLocation = os.chdir(home)
>>> setLocation
>>> os.getcwd()
'C:\\Users\\DeptAdmin'
>>> dirs = os.listdir()
>>> dirs
['.bashrc', '.bash_history', '.bash_profile', '.docker', '.dotnet', '.ganttproject', '.gitconfig', '.gnutls', '.idlerc', '.minttyrc', '.pylint.d', '.templateengine', '.VirtualBox', '.vscode', '3D Objects', 'AppData', 'Application Data', 'Contacts', 'Cookies', 'Desktop', 'Documents', 'Downloads', 'Favorites', 'ganttproject.log', 'IntelGraphicsProfiles', 'java0.log', 'Links', 'Local Settings', 'Music', 'My Documents', 'NetHood', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TM.blf', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'OneDrive', 'Pictures', 'pip', 'PrintHood', 'Recent', 'rought sketched.docx', 'Saved Games', 'Searches', 'SendTo', 'Start Menu', 'Templates', 'Videos', 'VirtualBox VMs']
>>> directory = dirs
>>> directory
['.bashrc', '.bash_history', '.bash_profile', '.docker', '.dotnet', '.ganttproject', '.gitconfig', '.gnutls', '.idlerc', '.minttyrc', '.pylint.d', '.templateengine', '.VirtualBox', '.vscode', '3D Objects', 'AppData', 'Application Data', 'Contacts', 'Cookies', 'Desktop', 'Documents', 'Downloads', 'Favorites', 'ganttproject.log', 'IntelGraphicsProfiles', 'java0.log', 'Links', 'Local Settings', 'Music', 'My Documents', 'NetHood', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TM.blf', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'OneDrive', 'Pictures', 'pip', 'PrintHood', 'Recent', 'rought sketched.docx', 'Saved Games', 'Searches', 'SendTo', 'Start Menu', 'Templates', 'Videos', 'VirtualBox VMs']
>>> directory.count
<built-in method count of list object at 0x0000018B6C38B080>
>>> directory.sort()
>>> directory
['.VirtualBox', '.bash_history', '.bash_profile', '.bashrc', '.docker', '.dotnet', '.ganttproject', '.gitconfig', '.gnutls', '.idlerc', '.minttyrc', '.pylint.d', '.templateengine', '.vscode', '3D Objects', 'AppData', 'Application Data', 'Contacts', 'Cookies', 'Desktop', 'Documents', 'Downloads', 'Favorites', 'IntelGraphicsProfiles', 'Links', 'Local Settings', 'Music', 'My Documents', 'NTUSER.DAT', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TM.blf', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000002.regtrans-ms', 'NetHood', 'OneDrive', 'Pictures', 'PrintHood', 'Recent', 'Saved Games', 'Searches', 'SendTo', 'Start Menu', 'Templates', 'Videos', 'VirtualBox VMs', 'ganttproject.log', 'java0.log', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2', 'ntuser.ini', 'pip', 'rought sketched.docx']
>>> directory.index
<built-in method index of list object at 0x0000018B6C38B080>
>>> directory.index()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    directory.index()
TypeError: index expected at least 1 argument, got 0
>>> for i in directory:
	print(directory.index(1))

	
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    print(directory.index(1))
ValueError: 1 is not in list
>>> for i in directory:
	print(directory.index(i))

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
>>> for i in directory:
	print(directory.index(i), "{}".format(i))

	
0 .VirtualBox
1 .bash_history
2 .bash_profile
3 .bashrc
4 .docker
5 .dotnet
6 .ganttproject
7 .gitconfig
8 .gnutls
9 .idlerc
10 .minttyrc
11 .pylint.d
12 .templateengine
13 .vscode
14 3D Objects
15 AppData
16 Application Data
17 Contacts
18 Cookies
19 Desktop
20 Documents
21 Downloads
22 Favorites
23 IntelGraphicsProfiles
24 Links
25 Local Settings
26 Music
27 My Documents
28 NTUSER.DAT
29 NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TM.blf
30 NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000001.regtrans-ms
31 NTUSER.DAT{0f0ed02d-5ea8-11eb-ab70-38dead0d99b2}.TMContainer00000000000000000002.regtrans-ms
32 NetHood
33 OneDrive
34 Pictures
35 PrintHood
36 Recent
37 Saved Games
38 Searches
39 SendTo
40 Start Menu
41 Templates
42 Videos
43 VirtualBox VMs
44 ganttproject.log
45 java0.log
46 ntuser.dat.LOG1
47 ntuser.dat.LOG2
48 ntuser.ini
49 pip
50 rought sketched.docx
>>> 