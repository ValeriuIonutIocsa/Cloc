@echo off

py -3 -m PyInstaller -F -n ClocC --distpath C:\IVI\Apps\Scripts\General\ClocC .\cloc_c.py
py -3 -m PyInstaller -F -n ClocCpp --distpath C:\IVI\Apps\Scripts\General\ClocCpp .\cloc_cpp.py
py -3 -m PyInstaller -F -n ClocCs --distpath C:\IVI\Apps\Scripts\General\ClocCs .\cloc_cs.py
py -3 -m PyInstaller -F -n ClocJava --distpath C:\IVI\Apps\Scripts\General\ClocJava .\cloc_java.py
py -3 -m PyInstaller -F -n ClocJs --distpath C:\IVI\Apps\Scripts\General\ClocJs .\cloc_js.py
py -3 -m PyInstaller -F -n ClocPy --distpath C:\IVI\Apps\Scripts\General\ClocPy .\cloc_py.py
py -3 -m PyInstaller -F -n ClocTs --distpath C:\IVI\Apps\Scripts\General\ClocTs .\cloc_ts.py
