#	NotePad app using tkinter and Packing it into a executable file for mac and windows

   .app file 
   https://github.com/chiranjeevbitm/notepad-GUI-With-Executable-/blob/master/dist/notepad.app/Contents/MacOS/notepad

Description


	notepad.py is a GUI software of simple notepad software
	I have used the tkinter library for the GUI development
	About tkinter
		Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

			Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps −

				Import the tkinter module.

				Create the GUI application main window.

				Add one or more of the above-mentioned widgets to the GUI application.

				Enter the main event loop to take action against each event triggered by the user.

	notepad basic features
		new		cut
		open	copy
		save	paste
		exit	

# How to make .app file (for macOS)
	REQUIREMENTS

		Python 3
		py2App(pip install py2App)


	Step 1
	Create a setup.py file
		py2applet --make-setup notepad.py
	output -- Wrote setup.py


	Step 2
	Clean up your build directories
		rm -rf build dist


	Step 3
	Development with alias mode
		python setup.py py2app -A


	Step 4 (if you want to add your own icon to .app file) Optional
		you must have .icnc file 

		Edit the setup.py , add 

			OPTIONS = {
    		'iconfile':'icon.icns',
    		'plist': {'CFBundleShortVersionString':'0.1.0',}
			}
					to OPTION then run 
						python setup.py py2app -A




# How to make .exe file (for Windows)
	REQUIREMENTS
	
		Python 3
		py2exe(pip install py2exe)


	Step 1
	Create your setup script (setup.py)

	C:\Tutorial>python setup.py install
	output -- Wrote setup.py


	Step 2
	python setup.py py2exe


	Step 3
	C:\Tutorial>cd dist
	C:\Tutorial\dist>hello.exe
