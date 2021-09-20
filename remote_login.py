import paramiko


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect(hname,port,uname,pswd):
    ssh_client.connect(hostname=hname,port=port,username=uname,password=pswd)

def disconnect():
    if ssh_client.get_transport().is_active() == True:
        ssh_client.close()
        
def free_mem():
    stdin,stdout,stderr = ssh_client.exec_command("free -h | grep ^Mem \n")
    x = stdout.read().decode().split()[1:]
    total,used,free,avail = x[0],x[1],x[2],x[5]
    return total,used,free,avail

def Load_avg():
    stdin,stdout,stderr = ssh_client.exec_command("cat /proc/loadavg \n")
    return stdout.read().decode()

def routing():
    stdin,stdout,stderr = ssh_client.exec_command("ip route show\n")
    return stdout.read().decode()

def uptime():
    stdin,stdout,stderr = ssh_client.exec_command("uptime -p \n")
    return stdout.read().decode()

