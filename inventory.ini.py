import os
import subprocess
from jinja2 import Environment, FileSystemLoader





##################Creating Python Environment###############

subprocess.run(["python3", "-m", "venv", "env"])
subprocess.run(["chmod", "+x", "env/bin/activate"])
subprocess.run(["env/bin/pip", "install", "ansible", "ansible-lint"])

print("\n")



#################Please do this after finishing##############
print("ennv folder has been created, please type: `source env/bin/activate`, to activate the environment after finishing up\n")
print("\n")

masters = list()
workers = list()
loadbalancer = list()
rancher = list()
float_ip = list()
only_ips = list()

remote_user = ""
print("------------------------------------------Masters----------------------------------------------\n")
num_master_hosts = input("How many number of master hosts (default: 1): ")
master_hostname = input(f"Enter the hostname of master (default: master) ")
with open("inventory.ini", "w") as file:
    file.write("[master]\n")
    if master_hostname and num_master_hosts:
        for i in range(1, int(num_master_hosts) + 1):
            print(f"\n------------------------------------------{master_hostname}-0{i}----------------------------------------------\n")
            master_ip = input(f"Enter the IP address of {master_hostname}-0{i}: ")
            only_ips.append(master_ip)
            masters.append(f"{master_hostname}-0{i},{master_ip}")
            master_user = input(f"Enter the username for {master_hostname}-0{i}: ")
            master_private_key = input(f"Enter the path to the private key for {master_hostname}-0{i} (default:~/.ssh/id_rsa): ")
            if not master_private_key:
                master_private_key =  "~/.ssh/id_rsa"
            print("\n")
            file.write(f"{master_hostname}-0{i} ansible_host={master_ip} ansible_user={master_user} ansible_ssh_private_key={master_private_key}\n")
    else:
        if not master_hostname and num_master_hosts:
            master_hostname = "master"
            for i in range(1, int(num_master_hosts) + 1):
                print(f"\n------------------------------------------{master_hostname}-0{i}----------------------------------------------\n")
                master_ip = input(f"Enter the IP address of {master_hostname}-0{i}: ")
                only_ips.append(master_ip)
                masters.append(f"{master_hostname}-0{i},{master_ip}")
                master_user = input(f"Enter the username for {master_hostname}-0{i}: ")
                master_private_key = input(f"Enter the path to the private key for {master_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                if not master_private_key:
                    master_private_key =  "~/.ssh/id_rsa"
                print("\n")
                file.write(f"{master_hostname}-0{i} ansible_host={master_ip} ansible_user={master_user} ansible_ssh_private_key={master_private_key}\n")
        elif not master_hostname and not num_master_hosts:
            master_hostname = "master"
            for i in range(1, 2):
                print(f"\n------------------------------------------{master_hostname}-0{i}----------------------------------------------\n")
                master_ip = input(f"Enter the IP address of {master_hostname}-0{i}: ")
                only_ips.append(master_ip)
                masters.append(f"{master_hostname}-0{i},{master_ip}")
                master_user = input(f"Enter the username for {master_hostname}-0{i}: ")
                master_private_key = input(f"Enter the path to the private key for {master_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                if not master_private_key:
                    master_private_key =  "~/.ssh/id_rsa"
                print("\n")
                file.write(f"{master_hostname}-0{i} ansible_host={master_ip} ansible_user={master_user} ansible_ssh_private_key={master_private_key}\n")
        else:
            for i in range(1, 2):
                print(f"\n------------------------------------------{master_hostname}-0{i}----------------------------------------------\n")
                master_ip = input(f"Enter the IP address of {master_hostname}-0{i}: ")
                only_ips.append(master_ip)
                masters.append(f"{master_hostname}-0{i},{master_ip}")
                master_user = input(f"Enter the username for {master_hostname}-0{i}: ")
                master_private_key = input(f"Enter the path to the private key for {master_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                if not master_private_key:
                    master_private_key =  "~/.ssh/id_rsa"
                print("\n")
                file.write(f"{master_hostname}-0{i} ansible_host={master_ip} ansible_user={master_user} ansible_ssh_private_key={master_private_key}\n")

print("------------------------------------------Workers----------------------------------------------\n")
num_worker_hosts = input("How many number of worker hosts (default:1): ")
worker_hostname = input(f"Enter the hostname of worker (default: worker): ")
with open("inventory.ini", "a") as file:
    file.write("\n[worker]\n")
    if worker_hostname and num_master_hosts:
        for i in range(1, int(num_worker_hosts) + 1):
            print(f"\n------------------------------------------{worker_hostname}-0{i}----------------------------------------------\n")
            worker_ip = input(f"Enter the IP address of {worker_hostname}-0{i}: ")
            only_ips.append(worker_ip)
            workers.append(f"{worker_hostname}-0{i},{worker_ip}")
            worker_user = input(f"Enter the username for {worker_hostname}-0{i}: ")
            worker_private_key = input(f"Enter the path to the private key for {worker_hostname}-0{i} (default:~/.ssh/id_rsa): ")
            if not worker_private_key:
                    worker_private_key =  "~/.ssh/id_rsa"
            print("\n")
            file.write(f"{worker_hostname}-0{i} ansible_host={worker_ip} ansible_user={worker_user} ansible_ssh_private_key={worker_private_key}\n")
    else:
        if not worker_hostname and num_worker_hosts:
            worker_hostname = "worker"
            for i in range(1, int(num_worker_hosts) + 1):
                print(f"\n------------------------------------------{worker_hostname}-0{i}----------------------------------------------\n")
                worker_ip = input(f"Enter the IP address of {worker_hostname}-0{i}: ")
                only_ips.append(worker_ip)
                workers.append(f"{worker_hostname}-0{i},{worker_ip}")
                worker_user = input(f"Enter the username for {worker_hostname}-0{i}: ")
                worker_private_key = input(f"Enter the path to the private key for {worker_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                if not worker_private_key:
                        worker_private_key =  "~/.ssh/id_rsa"
                print("\n")
                file.write(f"{worker_hostname}-0{i} ansible_host={worker_ip} ansible_user={worker_user} ansible_ssh_private_key={worker_private_key}\n")
    
        elif not worker_hostname and not num_worker_hosts:
             worker_hostname = "worker"
             for i in range(1, 2):
                print(f"\n------------------------------------------{worker_hostname}-0{i}----------------------------------------------\n")
                worker_ip = input(f"Enter the IP address of {worker_hostname}-0{i}: ")
                only_ips.append(worker_ip)
                workers.append(f"{worker_hostname}-0{i},{worker_ip}")
                worker_user = input(f"Enter the username for {worker_hostname}-0{i}: ")
                worker_private_key = input(f"Enter the path to the private key for {worker_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                if not worker_private_key:
                        worker_private_key =  "~/.ssh/id_rsa"
                print("\n")
                file.write(f"{worker_hostname}-0{i} ansible_host={worker_ip} ansible_user={worker_user} ansible_ssh_private_key={worker_private_key}\n") 
        else:
            for i in range(1, 2):
                print(f"\n------------------------------------------{worker_hostname}-0{i}----------------------------------------------\n")
                worker_ip = input(f"Enter the IP address of {worker_hostname}-0{i}: ")
                only_ips.append(worker_ip)
                workers.append(f"{worker_hostname}-0{i},{worker_ip}")
                worker_user = input(f"Enter the username for {worker_hostname}-0{i}: ")
                worker_private_key = input(f"Enter the path to the private key for {worker_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                if not worker_private_key:
                        worker_private_key =  "~/.ssh/id_rsa"
                print("\n")
                file.write(f"{worker_hostname}-0{i} ansible_host={worker_ip} ansible_user={worker_user} ansible_ssh_private_key={worker_private_key}\n")


print("------------------------------------------Loadbalancers----------------------------------------------\n")
num_loadbalancer_hosts = input("Enter the number of loadbalancer(default:0): ")

if num_loadbalancer_hosts:
    if int(num_loadbalancer_hosts) >=1:
            with open("inventory.ini", "a") as file:
                file.write("\n[loadbalancer]\n")
                loadbalancer_hostname = input(f"Enter the hostname of loadbalancer (default: Loadbalancer): ")
                if  loadbalancer_hostname:
                    for i in range(1, int(num_loadbalancer_hosts) + 1):
                        print(f"\n------------------------------------------{loadbalancer_hostname}-0{i}----------------------------------------------\n")
                        loadbalancer_ip = input(f"Enter the IP address of {loadbalancer_hostname}-0{i}: ")
                        only_ips.append(loadbalancer_ip)
                        loadbalancer.append(f"{loadbalancer_hostname}-0{i},{loadbalancer_ip}")
                        loadbalancer_user = input(f"Enter the username for {loadbalancer_hostname}-0{i}: ")
                        loadbalancer_private_key = input(f"Enter the path to the private key for {loadbalancer_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                        if not loadbalancer_private_key:
                            loadbalancer_private_key = "~/.ssh/id_rsa"
                        print("\n")
                        file.write(f"{loadbalancer_hostname}-0{i} ansible_host={loadbalancer_ip} ansible_user={loadbalancer_user} ansible_ssh_private_key={loadbalancer_private_key}\n")
                else:
                    loadbalancer_hostname = "Loadbalancer"
                    for i in range(1, int(num_loadbalancer_hosts) + 1):
                        print(f"\n------------------------------------------{loadbalancer_hostname}-0{i}----------------------------------------------\n")
                        loadbalancer_ip = input(f"Enter the IP address of {loadbalancer_hostname}-0{i}: ")
                        only_ips.append(loadbalancer_ip)
                        loadbalancer.append(f"{loadbalancer_hostname}-0{i},{loadbalancer_ip}")
                        loadbalancer_user = input(f"Enter the username for {loadbalancer_hostname}-0{i}: ")
                        loadbalancer_private_key = input(f"Enter the path to the private key for {loadbalancer_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                        if not loadbalancer_private_key:
                            loadbalancer_private_key = "~/.ssh/id_rsa"
                        print("\n")
                        file.write(f"{loadbalancer_hostname}-0{i} ansible_host={loadbalancer_ip} ansible_user={loadbalancer_user} ansible_ssh_private_key={loadbalancer_private_key}\n")
print("------------------------------------------Floating IP----------------------------------------------\n")
num_float_hosts = input("Enter the number of floating_ip (default:0): ")
if num_float_hosts:
    if int(num_float_hosts) == 1:
        with open("inventory.ini", "a") as file:
            file.write("\n[floating_ip]\n")
            float_hostname = input(f"Enter the hostname of floating_ip (default: float_ip): ")
            if float_hostname:
                    for i in range(1, int(num_float_hosts) + 1):
                        print(f"------------------------------------------{float_hostname}-0{i}----------------------------------------------\n")
                        float_ip1 = input(f"Enter the IP address of {float_hostname}-0{i}: ")
                        float_ip.append(f"{float_hostname}-0{i},{float_ip1}")
                        float_user = input(f"Enter the username for {float_hostname}-0{i}: ")
                        float_private_key = input(f"Enter the path to the private key for {float_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                        if not float_private_key:
                            float_private_key = "~/.ssh/id_rsa"
                        print("\n")
                        file.write(f"{float_hostname}-0{i} ansible_host={float_ip1} ansible_user={float_user} ansible_ssh_private_key={float_private_key}\n")
            else:
                float_hostname = "float_ip"
                for i in range(1, int(num_float_hosts) + 1):
                    print(f"------------------------------------------{float_hostname }-0{i}----------------------------------------------\n")
                    float_ip1 = input(f"Enter the IP address of {float_hostname }-0{i}: ")
                    float_ip.append(f"{float_hostname }-0{i},{float_ip1}")
                    float_user = input(f"Enter the username for {float_hostname}-0{i}: ")
                    float_private_key = input(f"Enter the path to the private key for {float_hostname }-0{i} (default:~/.ssh/id_rsa): ")
                    if not float_private_key:
                        float_private_key = "~/.ssh/id_rsa"
                    print("\n")
                    file.write(f"{float_hostname }-0{i} ansible_host={float_ip1} ansible_user={float_user} ansible_ssh_private_key={float_private_key}\n")


print("------------------------------------------Ranchers----------------------------------------------\n")
num_rancher_hosts = input("Enter the number of rancher (default:0): ")
if num_rancher_hosts:
    if int(num_rancher_hosts) >=1:
        with open("inventory.ini", "a") as file:
            file.write("\n[rancher]\n")
            rancher_hostname = input(f"Enter the hostname of rancher (default: rancher): ")
            if rancher_hostname:
                    for i in range(1, int(num_rancher_hosts) + 1):
                        print(f"------------------------------------------{rancher_hostname}-0{i}----------------------------------------------\n")
                        rancher_ip = input(f"Enter the IP address of {rancher_hostname}-0{i}: ")
                        only_ips.append(rancher_ip)
                        rancher.append(f"{rancher_hostname}-0{i},{rancher_ip}")
                        rancher_user = input(f"Enter the username for {rancher_hostname}-0{i}: ")
                        rancher_private_key = input(f"Enter the path to the private key for {rancher_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                        if not rancher_private_key:
                            rancher_private_key = "~/.ssh/id_rsa"
                        print("\n")
                        file.write(f"{rancher_hostname}-0{i} ansible_host={rancher_ip} ansible_user={rancher_user} ansible_ssh_private_key={rancher_private_key}\n")
            else:
                rancher_hostname = "rancher"
                for i in range(1, int(num_rancher_hosts) + 1):
                    print(f"------------------------------------------{rancher_hostname}-0{i}----------------------------------------------\n")
                    rancher_ip = input(f"Enter the IP address of {rancher_hostname}-0{i}: ")
                    only_ips.append(rancher_ip)
                    rancher.append(f"{rancher_hostname}-0{i},{rancher_ip}")
                    rancher_user = input(f"Enter the username for {rancher_hostname}-0{i}: ")
                    rancher_private_key = input(f"Enter the path to the private key for {rancher_hostname}-0{i} (default:~/.ssh/id_rsa): ")
                    if not rancher_private_key:
                        rancher_private_key = "~/.ssh/id_rsa"
                    print("\n")
                    file.write(f"{rancher_hostname}-0{i} ansible_host={rancher_ip} ansible_user={rancher_user} ansible_ssh_private_key={rancher_private_key}\n")

with open('hosts_lists.txt', 'w') as fp:
    for host in only_ips:
         fp.writelines(f"{host}\n")

print(f"\n--------------- The inventory.ini file has been created inside your project {os.getcwd()}  -------------")