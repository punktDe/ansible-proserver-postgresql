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



#### Options for `postgresql`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `version` | Major version of PostgreSQL to install/configure. Ignored on FreeBSD Proservers (version is determined by the system). | int | no | 13 |
| `prefix` |  | dict of 'prefix' options | no |  |
| `users` | Dict of PostgreSQL users to create (key is an arbitrary id, value defines the user). | dict of 'users' options | no | {} |
| `privileges` | Dict of privileges to assign (key is arbitrary id). Each entry grants a role access to a database or object. | dict of 'privileges' options | no | {} |
| `databases` | Dict of databases to create (key is arbitrary id). At least the root database entry is required by defaults. | dict of 'databases' options | no |  |
| `database_defaults` | Defaults applied to database creation when not set per-database. | dict of 'database_defaults' options | no |  |
| `postgresql.conf` | Key-value options written to the role-managed include file (ansible.conf), included from postgresql.conf. Consult PostgreSQL documentation for valid settings. | dict | no |  |
| `repository` | Package repository used to install PostgreSQL (Linux/Debian). | dict of 'repository' options | no |  |
| `timescaledb` | TimescaleDB installation and tuning (Linux/Debian only). | dict of 'timescaledb' options | no |  |

#### Options for `postgresql.prefix`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `config` | Directory for PostgreSQL configuration (e.g. pg_hba.conf, postgresql.conf include). Defaults depend on system; see defaults/main.yaml (e.g. /etc/postgresql/{{ version }}/main/conf.d on Linux). | str | no |  |

#### Options for `postgresql.users`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `username` | Login name of the user. | str | no |  |
| `password` | Password for the user (optional). | str | no |  |
| `role_attributes` | Role attributes (e.g. SUPERUSER, CREATEROLE); values are joined for role_attr_flags. | dict | no |  |
| `hosts` | List of client addresses (e.g. 127.0.0.1) for which a pg_hba.conf host entry is added. Used together with privileges to allow password authentication from those hosts. | list of 'str' | no |  |

#### Options for `postgresql.privileges`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `username` | Role name to grant the privilege to. | str | no |  |
| `database` | Database the privilege applies to. | str | no |  |
| `type` | Type of object (e.g. table, database, schema). | str | no | table |
| `objs` | Object name(s) for the grant (optional for type database). | str | no |  |
| `schema` | Schema name (optional). | str | no |  |
| `privs` | List of privilege names (e.g. ALL, SELECT, INSERT). | list of 'str' | no |  |

#### Options for `postgresql.databases`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `name` | Name of the database. | str | no |  |
| `owner` | Owner of the database. Use ~<user_key> to reference a user from postgresql.users by key (e.g. ~molecule). | str | no |  |
| `encoding` | Character encoding (defaults to database_defaults.encoding). | str | no |  |
| `lc_collate` | Locale for collation order (defaults to database_defaults.lc_collate). | str | no |  |
| `lc_ctype` | Locale for character classification (defaults to database_defaults.lc_ctype). | str | no |  |
| `template` | Template database to use (defaults to database_defaults.template). | str | no |  |
| `import_file` | Path to a dump file to restore into the database after creation (optional). | path | no |  |

#### Options for `postgresql.database_defaults`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `encoding` |  | str | no | UTF-8 |
| `lc_collate` |  | str | no | en_US.UTF-8 |
| `lc_ctype` |  | str | no | en_US.UTF-8 |
| `template` |  | str | no | template0 |

#### Options for `postgresql.repository`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `apt` |  | dict of 'apt' options | no |  |

#### Options for `postgresql.repository.apt`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `key_url` |  | str | no | https://www.postgresql.org/media/keys/ACCC4CF8.asc |
| `repository` | APT repository URI (default uses apt.postgresql.org). | str | no |  |
| `suites` | Suite(s) for the repo (default uses distribution release and -pgdg). | list of 'str' | no |  |
| `package` | Package name (defaults to postgresql-{{ postgresql.version }}). | str | no |  |

#### Options for `postgresql.timescaledb`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `enabled` | Whether to install and enable TimescaleDB. | bool | no | False |
| `autotune` | Whether to run timescaledb-tune after installation. | bool | no | True |
| `repository` |  | dict of 'repository' options | no |  |

#### Options for `postgresql.timescaledb.repository`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `apt` |  | dict of 'apt' options | no |  |

#### Options for `postgresql.timescaledb.repository.apt`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `key_url` | GPG key URL for the TimescaleDB repo. | str | no |  |
| `repository` | APT repository line(s) for TimescaleDB. | str | no |  |
| `package` | Package name (e.g. timescaledb-2-postgresql-{{ postgresql.version }}). | str | no |  |

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
