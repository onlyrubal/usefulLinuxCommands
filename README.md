# Useful Linux Commands

This document contains the useful linux commands that I need personally quite often when I learnt linux.

## SSH

SSH is the act of remotely accessing a machine. SSH allows you to run commands interactively on the remote machine. This is done through the use of a program on the target machine, which allows the ssh client to interface with the target host.

SSH works through a command line, meaning anything done on the target machine will be done through a command prompt similar to this.

Depending on the operating system, like Windows have PuTTY and linux has command line option of ssh.

```bash
ssh user_name@MACHINE_IP
```
After this it would prompt to ask for the password and, after that we can interact with the remote machine through command line.
