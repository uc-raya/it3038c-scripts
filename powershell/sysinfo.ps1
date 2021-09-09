function getIP {
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
$USER = $env:USERNAME
$HOSTNAME = $env:COMPUTERNAME
$VERSION = $host.Version
$DATE = Get-Date -Format "dddd MM/dd/yyyy"
$BODY = "This machine's IP address is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell version $VERSION. Today's date is $DATE"
## $BODY = This machine's IP is ...., user is $USER, Hostname, PowerShell version, today's date

Send-MailMessage -To "raya9@mail.uc.edu" -From "andrewray317@gmail.com" -Subject "IT3038c Windows SysInfo" -Body $BODY -smtpserver smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)