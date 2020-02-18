@ECHO OFF

echo "Bot Docs B 'CodeHelper' Installer Windows 64 Bit"
echo

echo "Installing Python3..."
CD python-3.8.1-amd64
START /W python-3.8.1-amd64.exe
CD ..
echo "python3 installed"
echo

echo "Installing Python3 Libraries..."
SET libs=(requests sys os beautifulsoup4 numpy sklearn2 scikit-learn scipy nltk)
(FOR %%a in %libs% DO (
	echo "Installing Python Library %%a"
	py -3 -m pip install %%a
))
echo "Installed all Python3 Libraries"
echo

echo "Installing VS Code..."
CD vscode
START /W VSCodeUserSetup-x64-1.42.1.exe
CD ..
echo "Installed VS code"
echo

echo "Installing Node JS..."
CD nodejs
START /W node-v12.16.0-x64.msi
CD ..
echo "Installed Node JS"
echo

echo "Installing VS Code Extenstion 'CodeHelper'..."
code --install-extension codehelper\codehelper-0.0.1.vsix
code
echo "Installed VS Code Extenstion 'CodeHelper'"

PAUSE