#!/usr/bin/env python3
import os
import re
import json
import subprocess

class PostgresqlFacts:           
    def get_os_family(self) -> str:
        if os.path.exists("/etc/os-release"):
            os_vars = {}
            with open("/etc/os-release", "r", encoding="utf-8") as os_release:
                for line in os_release.readlines():
                    key, value = line.split("=")
                    os_vars.update({key: value})
            if os_vars.get("ID_LIKE"):
                os_family = str(os_vars.get("ID_LIKE")).lower().strip()
            else:
                os_family = str(os_vars.get("ID")).lower().strip()
        else:
            os_family = re.findall(r"debian|freebsd", os.uname().version.lower())
            if len(os_family) == 0:
                raise OSError(f"Unsupported OS family: {os.uname().version}")
            else:
                os_family = os_family[0]
        if os_family == "debian" or os_family == "freebsd":
            return os_family
        else:
            raise OSError(f"Unsupported OS family: {os_family}")

    def get_postgresql_version(self) -> int:
        os_family = self.get_os_family()
        if os_family == "debian":
            command='apt-cache search --names-only "^postgresql-[0-9]+$" | grep -Po "[0-9]+"'
        else:
            command='psql --version | sed "s/^.*\\([0-9][0-9]\\).*$/\1/"'
        command_output = subprocess.run(command, shell=True, capture_output=True)
        if len(command_output.stdout) > 0:
            return int(command_output.stdout.decode().strip())
        else:
            raise OSError(f"Error detecting the PostgreSQL version: command_output.stderr.decode()")

    def get_postgresql_dbdir(self) -> str:
        os_family = self.get_os_family()
        version = self.get_postgresql_version()
        if os_family == "debian":
            dbdir = f"/etc/postgresql/{version}/main/conf.d"
        else:
            if version >= 15:
                dbdir = "/var/db/postgres/data{version}"
            else:
                dbdir = "/var/db/postgresql/data{version}"
        return dbdir

    def generate_postgresql_facts(self) -> dict:
        return {
                'version': str(self.get_postgresql_version()),
                'prefix': {"config": self.get_postgresql_dbdir()},
                }

class Facts:
    def __str__(self):
        return json.dumps(PostgresqlFacts().generate_postgresql_facts())

if __name__ == '__main__':
    print(Facts())
