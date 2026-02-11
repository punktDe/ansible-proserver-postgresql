<!-- BEGIN_ANSIBLE_DOCS -->
<!--
Do not edit README.md directly!

This file is generated automatically by aar-doc and will be overwritten.

Please edit meta/argument_specs.yml instead.
-->
# ansible-proserver-postgresql

postgresql role for Proserver

## Supported Operating Systems

- Debian 12, 13
- Ubuntu 24.04, 22.04
- FreeBSD [Proserver](https://infrastructure.punkt.de/de/produkte/proserver.html)

## Role Arguments

This entrypoint has no options.

## Dependencies
None.

## Installation
Add this role to the requirements.yml of your playbook as follows:
```yaml
roles:
  - name: ansible-proserver-postgresql
    src: https://github.com/punktDe/ansible-proserver-postgresql
```

Afterwards, install the role by running `ansible-galaxy install -r requirements.yml`

## Example Playbook

```yaml
- hosts: all
  roles:
    - name: postgresql
```

<!-- END_ANSIBLE_DOCS -->
