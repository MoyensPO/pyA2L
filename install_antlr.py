#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform as pf
from os import environ
from subprocess import call
from subprocess import check_call


VERSION = "4.13.1"
ANTLR = "https://www.antlr.org/download/antlr-{}-complete.jar".format(VERSION)


print("ENVIRON:", environ)
os = pf.system().lower()
uname = pf.uname()
print("UNAME:", uname)


def main():
    if os == "windows":
        call(["curl", "-O", "-C", "-", "-L", ANTLR])
        call(["dir"])
    else:
        call(["curl", "-O", "-C", "-", "-L", ANTLR])
        if os == "linux":
            call(
                """cat << 'EOF' > adoptopenjdk.repo
[AdoptOpenJDK]
name=AdoptOpenJDK
baseutl=http://adoptopenjdk.jfrog.io/artifactory/rpm/centos/$releasever/$basearch
enabled=1
gpgcheck=1
gpgkey=http://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public
EOF""",
                shell=True,
            )
            # call(["sudo", "yum", "install", "java-1.8.0-openjdk"])
            # call(["cp", "adoptopenjdk.repo", "/etc/yum.repos.d/"])
            # call(["yum", "install", "adoptopenjdk"])
            # call(["yum", "install", "openjdk-16-jre"])
            # call(["yum", "update"])
            # call(["yum", "search", "openjdk"])
            # call(["yum", "install", "java-12-openjdk"])
        elif os == "darwin":
            pass
        call(["ls", "-l", "-A"])


if __name__ == "__main__":
    main()
