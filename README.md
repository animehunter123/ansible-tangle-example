# Description
This is a sample folder of code which is used for producing *.yml files from the *.org files in the ./playbooks folder, then you can run it with main.yml to target a host in the inventory.yml file.

# Requirements (on linux host)
* Linux Host to launch Ansible 
* You must have installed: emacs
* You must have installed: python3
* You must have installed: ansible  _(You can use ansible-core package, or my **portable ansible2.14.9 as ROOT USER**)_
* You must have your ssh key copied to the destination host. I.e: _ssh-copy-id `whoami`@192.168.x.x_
* cd ./playbooks
* ls *.yml *.yaml **make sure no yaml files exist**
* python3 ./tangle.py **this produces/overwrites and makes new yaml files**
* You must verify yaml files are valid. ./playbooks/*.yml
* You must verify inventory is valid: ./inventory/inventory.yml
* Launch the playbook via:
```bash
ansible-playbook -i inventory/inventory.yml playbooks/main.yml
```

# Example showcasing dynamically generated yaml
```bash
> ansible-playbook -i inventory/inventory.yml playbooks/main.yml
PLAY [My playbook] ************************************************************************************************************************************************************************************************************************************************
TASK [Gathering Facts] ********************************************************************************************************************************************************************************************************************************************ok: [192.168.0.287]

TASK [Print a message] ********************************************************************************************************************************************************************************************************************************************ok: [192.168.0.287] => {
    "msg": "Hello from the playbook!"
}

PLAY RECAP ********************************************************************************************************************************************************************************************************************************************************192.168.0.287               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```