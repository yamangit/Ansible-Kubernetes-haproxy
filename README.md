# Ansible-Kubernetes-haproxy with keepalived
## Dependency Cluster for this playbook
|    Nodes     |            Nodes Count          |
|--------------|---------------------------------|
| Master       | 2 nodes (master-01, master-02)  |
| Worker       | As you wish                     |
| Load Balancer| 2 nodes (master and backup)      |


## Usage

### 1. Clone the repository
```bash
git clone https://github.com/yamangit/Ansible-Kubernetes-haproxy.git
```

### 2. Change the directory
```bash
cd Ansible-Kubernetes-haproxy
```

#### 3. Run `inventory.ini.py` script, it will create `hosts_lists.txt` and `inventory.ini` file in current directory
```bash
python3 inventory.ini.py
```

#### 4. Copy SSH-Key to targeted host machines and provide necessary `username and password having sudo privilege`
```bash
python3 copy_sshkey.py hosts_lists.txt
```

#### 5. To activate Python virtual environment run following command
```bash
source env/bin/activate
```
#### 6. Finally, Run the main playbook
```bash
ansible-playbook main_playbooks.yaml --ask-become-pass
```
## Enjoy!!!!


## Contact
### If you have any questions, please contact me at https://www.linkedin.com/in/yaman-singh-rana-57913254/
#### Thank you for using this playbook!
