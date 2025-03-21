# Description
This is a example of a ansible playbook that is tangled with ORG mode to match the design that Mike showed us.

The goal of it is to produce *.yml files from the *.org files in the ./playbooks folder, then you can run it with main.yml to target a inventory host.

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