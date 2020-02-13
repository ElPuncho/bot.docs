#!/bin/bash

function installPython3()
{
	if [ -x "$(command -v python3)" ]
	then
		echo "python3 allready installed"
	else
		cd Python-3.8.1
		./configure
    	make
    	make test
    	sudo make install
		echo "python3 installed"
		cd ..
	fi
}

function installPythonLibraries()
{
	libs=(requests sys os beautifulsoup4 numpy sklearn2 scikit-learn scipy nltk)
	for lib in ${lips[@]}
	do
		python3 -m pip $lib
		echo "Installing Python Library $lib"
	done
}

function installVsCode()
{
	cd vscode
	if [ -x "$(command -v dpkg)" ]
	then
		dpkg -i "code_1.42.0-1580986622_amd64.deb"
	else
		rpm -i "code-1.42.0-1580986751.el7.x86_64.rpm"
	fi
	cd ..
}

function installNodeJs()
{
	if [ -x "$(command -v dpkg)" ]
	then
		curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
		sudo apt-get install -y nodejs
	else
		curl -sL https://rpm.nodesource.com/setup_13.x | sudo bash -
	fi
}

function installVsCodeExtenstion()
{
	code "./codehelper/codehelper.vsix"
}

function movingFilesFromInstallDirToLocalExtenstionDir()
{
	cp "" "$HOME/.vscode/codehelper"
}

echo "Bot Docs B 'CodeHelper' Installer Linux"
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
