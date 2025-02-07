
# Installing the OpenSSH  

Try the following in powershell (run as administrator)

Run the following command check available OpenSSH features
```
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

 Install OpenSSH Client
```
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0 
```

Install OpenSSH Server (if needed):
```
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```


Start SSH Service (if server is installed)
```
Start-Service sshd
```

Checking the status of OpenSSH
```
Get-Service sshd
```

# Setting up the new firewall rule
Check If SSH is Listening on Port 22

```
netstat -an | findstr :22
```
# Correct Firewall Rules   
Even though SSH is listening, your Windows Firewall might still be blocking external SSH connections.  
Run the following to check firewall rules:

```
New-NetFirewallRule -Name sshd -DisplayName "OpenSSH Server" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

```

If nothing appears, SSH is not listening on port 22.  Solution: Restart SSHD:

```
Restart-Service sshd
```



