# Useful Linux Commands

This document contains the useful linux commands that I need personally quite often when I learnt linux.

## SSH

SSH is the act of remotely accessing a machine. SSH allows you to run commands interactively on the remote machine. This is done through the use of a program on the target machine, which allows the ssh client to interface with the target host.

SSH works through a command line, meaning anything done on the target machine will be done through a command prompt similar to this.

Depending on the operating system, like Windows have PuTTY and linux has command line option of ssh.

```bash
ssh user_name@MACHINE_IP

#for example
ssh bob@10.10.203.34
```

After this it would prompt to ask for the password and, after that we can interact with the remote machine through command line.

## MAN

To check the manual of each command we can use the man command and to check the flag associated with each command, all info related to flags is stored in DESCRIPTION section.

```bash
man echo
```

Another useful command that I often use along with man command is **grep** command

```bash
man ls | grep -e "long list"
```

It would search the manual of the ls command and output those lines which contains this expression "long list". It makes it easier to search the manual and look for the flags.

## LS

ls is a command that lists information about every file/directory in the directory. Just running the ls command outputs the name of every file in the directory.

```bash
#To list every file/directory in the given directory
ls

#To list all files/directories including the hidden one in the given directory
ls -a

#To list in long list format
ls -l
```

## CAT

It outputs the contents of the files to the console.

```bash
# To output the contents of the file on the console.
cat a.txt

# To output the contents of the file along with line number
cat -n a.txt
```

## TOUCH

touch is a pretty simple command, it creates files.

```bash
# To simply create the file
touch a.txt
```
