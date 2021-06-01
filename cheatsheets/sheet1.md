# Information Gathering

## Service Discovery
```
echo $IP_ADDRESS > target 
target=$(cat target)
```

```
nmap -sC -sV $target -oN nmap
nmap -p- -sV -sT -A $target

sudo arp-scan -I eth0 -l

netdiscover -r $target

nikto -h $target -p $port
```

### Web Service

```
dirb http://$target

sqlmap -r some.req
sqlmap -u http://$target
```

### BruteForce tools
```
hydra -e nsr -L /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -t 4 $target ssh

ncrack -p 22 --user root -P /usr/share/wordlists/rockyou.txt $target

patator ssh_login host=$target user=root password=FILE0 0=/usr/share/wordlists/rockyou.txt -x ignore:mesg='Authentication failed.'
```

## wordlists

- /usr/share/wordlists

