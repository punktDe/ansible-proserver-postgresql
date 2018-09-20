# [proserver-ansible-postgresql](https://github.com/punktDe/proserver-ansible-postgresql)

Ansible role to configure PostgreSQL on a proServer.

## Requirements

- A proServer
- Ansible >=2.6.4
- Ansible option `hash_behaviour` set to `merge`

## Configuration

**1)** Add the role to your playbook.
You could add this repository as submodule to your Ansible project's Git repository.

```
git submodule add https://github.com/punktDe/proserver-ansible-postgresql.git roles/postgresql
```

```yaml
---
- name: postgresql
  hosts: all
  become: yes
  roles:
    - postgresql
```

**2)** Configure which databases and users you'd like to have (in host vars, group vars or wherever).

```yaml
---
postgresql:
  databases:
    cms:
      name: mydb
      # "~cms" will have the same effect as "myuser" in this scenario
      owner: ~cms
  users:
    cms:
      username: myuser
      password: mypass
```

With these variables the role will ensure that

- there is a database `mydb`
- there is a user `myuser@localhost` with password `mypass`
- `myuser` will be the owner of `mydb`

The value `cms_all` is never used and `cms` is only used for the quick user
reference feature (`~cms`).
You can use those keys to override previously defined variables
(e.g. override options from group vars in host vars).

## Full example

This example shows all available variables.

```yaml
---
postgresql:
  database_defaults:
    encoding: UTF-8
    lc_collate: en_US.UTF-8
    lc_ctype: en_US.UTF-8
    template: template0
  databases:
    example_db:
      encoding: UTF-8
      lc_collate: de_DE.UTF-8
      lc_ctype: de_DE.UTF-8
      template: template1
      name: example
      owner: example
  users:
    example_user:
      username: example
      password: example
```
