Here is how you can run a powershell script that I created, which uses the powershell module called "PSWindowsUpdate." This module allows you to install all available Windows updates, exclude Windows Updates and lets you check your Windows update history.

First, you need to open up powershell and install the PSWindowsUpdate module with the following command:

Install-Module -Name PSWindowsUpdate

Next, create a Powershell script. This script will show all available Windows updates for your machine and then allow you install all of them at once. Inside the script, write the following line of code:

Get-WindowsUpdate

Install-WindowsUpdate -AcceptAll -AutoReboot

Create another Powershell script. This one will allow you to exclude any Windows updates you do not want to install. First, display all available updates with the command we used earlier and then use the KB number of the update that you do not want to install. Here is an example:

Hide-WindowsUpdate -KBArticleID KB2267602

Lastly, create another Powershell script that will show all Windows updates that have been installed for your machine. Use the following command:

Get-WUHistory
