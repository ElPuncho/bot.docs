#!/bin/bash

function pause()
{
   read -p "$*"
}

function installPython3()
{
	if [ -x "$(command -v python3)" ]
	then
		echo "python3 allready installed"
	else
		sudo apt-get install python3
	fi
}

function installPythonLibraries()
{
	libs=(requests sys os beautifulsoup4 numpy sklearn2 scikit-learn scipy nltk)
	for lib in ${libs[@]}
	do
		python3 -m pip $lib
		echo "Installing Python Library $lib"
	done
}

function installVsCode()
{
	cd vscode
	sudo dpkg -i "code_1.42.0-1580986622_amd64.deb"
	cd ..
}

function installNodeJs()
{
	curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
	sudo apt-get install -y nodejs
}

function installVsCodeExtenstion()
{
	code "codehelper/codehelper.vsix"
}

function movingFilesFromInstallDirToLocalExtenstionDir()
{
	cp "" "$HOME/.vscode/codehelper"
}

echo "Bot Docs B 'CodeHelper' Installer Ubuntu-based Linux"
echo

echo "Installing Python3..."
installPython3
echo

echo "Installing Python3 Libraries..."
installPythonLibraries
echo "Installed all Python3 Libraries"
echo

echo "Installing VS Code..."
installVsCode
echo "Installed VS code"
echo

echo "Installing Node JS..."
installNodeJs
echo "Installed Node JS"

echo "Installing VS Code Extenstion 'CodeHelper'..."
installVsCodeExtenstion
echo "Installed VS Code Extenstion 'CodeHelper'"

pause 'Press [Enter] key to exit...'