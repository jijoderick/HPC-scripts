
# Installing the OpenSSH  

Try the following in powershell (run as administrator)

# Run the following command check available OpenSSH features
```
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

# Install OpenSSH Client
```
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0 
```

# Install OpenSSH Server (if needed):
```
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```


# Start SSH Service (if server is installed)
```
Start-Service sshd
```

Checking the status of OpenSSH
```
Get-Service sshd
```





