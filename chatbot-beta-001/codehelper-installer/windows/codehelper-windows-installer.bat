@ECHO OFF

echo "Bot Docs B 'CodeHelper' Installer Windows 64 Bit"
echo

echo "Installing Python3..."
CALL :installPython3
echo "python3 installed"
echo

echo "Installing Python3 Libraries..."
CALL :installPythonLibraries
echo "Installed all Python3 Libraries"
echo

echo "Installing VS Code..."
CALL :installVsCode
echo "Installed VS code"
echo

echo "Installing Node JS..."
CALL :installNodeJs
echo "Installed Node JS"
echo

echo "Installing VS Code Extenstion 'CodeHelper'..."
CAll :installVsCodeExtenstion
echo "Installed VS Code Extenstion 'CodeHelper'"

PAUSE
EXIT /B %ERRORLEVEL% 

:installPython3
CD python-3.8.1-amd64
START /W "python-3.8.1-amd64.exe"
CD ..
EXIT /B 0

:installPythonLibraries
SET libs = requests sys os beautifulsoup4 numpy sklearn2 scikit-learn scipy nltk
(FOR %%lib in (%libs)
DO (
	echo "Installing Python Library %%lib"
	py -3 -m pip install %%lib
))
EXIT /B 0

:installVsCode
CD vscode
START /W "VSCodeUserSetup-x64-1.42.1.exe"
CD ..
EXIT /B 0

:installNodeJs
CD nodejs
START /W "node-v12.16.0-x64.msi"
CD ..
EXIT /B 0


:installVsCodeExtenstion
code --install-extension codehelper\codehelper-0.0.1.vsix
code
EXIT /B 0