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

Note: cat supports the **--help** flag meaning that you can **see useful flags** without going to the man page!

## TOUCH

touch is a pretty simple command, it creates files.

```bash
# To simply create the file
touch a.txt
```

## ABSOLUTE AND RELATIVE PATHS

The below shows the relative paths.

1. Current Directory .
2. Directory Before the current directory ..
3. The User's home directory ~ => ~/hello_world

In Absolute path terms

3. /home/(current user) => /home/(current_user)/hello_world

## BINARY FILE

It is a file stored in binary format. A binary file is computer readable not human readable.

What is hexdump?

The **hd** or **hexdump** command in Linux is used to filter and display the specified files, or standard input in a human readable specified format

- -b : One-byte octal display. Display the input offset in hexadecimal, followed by sixteen space-separated, three column, zero-filled, bytes of input data, in octal, per line.

  ![Image of hexdump -b](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-17-00-59-07.png)

  The first column of the output represents the input offset in file.

- -c : One-byte character display. Display the input offset in hexadecimal, followed by sixteen space-separated, three column, space-filled, characters of input data per line.

  ![Image of hexdump -c ](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-17-01-09-00.png)

- -C : Canonical hex+ASCII display. Display the input offset in hexadecimal, followed by sixteen space-separated, two column, hexadecimal bytes, followed by the same sixteen bytes in %\_p format enclosed in “|” characters.

  ![Image of hexdump -C ](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-17-01-14-30.png)

- -d : Two-byte decimal display. Display the input offset in hexadecimal, followed by eight space-separated, five column, zero-filled, two-byte units of input data, in unsigned decimal, per line.
  ![Image of hexdump -d ](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-17-01-16-49.png)

- -n length : Where length is an integer. Interprets only ‘length’ bytes of output.

  ![Image of hexdump -dn ](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-17-01-19-53.png)

To get to know about another flags associated with hexdump refer to:
https://www.geeksforgeeks.org/hexdump-command-in-linux-with-examples/

```bash
# To run a binary file
./shiba1

# To see the contents of the binary file
hexdump -C shiba1
```

## SU

su is a command that allows you to change the user, without logging out and logging back in again.

Note : Typing **su** on its own is equivalent to typing **su root**.

## USERMOD UTILITY

In Unix/Linux distributions, the command **usermod** is used to modify or change any attributes of a already created user account via command line.

After creating user accounts, in some scenarios where we need to change the attributes of an existing user such as, change user’s home directory, login name, login shell, password expiry date, etc, where in such case ‘usermod’ command is used.

When we execute ‘usermod‘ command in terminal, the following files are used and affected.

- /etc/passwd – User account information.
- /etc/shadow – Secure account information.
- /etc/group – Group account information.
- /etc/gshadow – Secure group account information.
- /etc/login.defs – Shadow password suite configuration..

### Change User Shell

The user login shell can be changed or defined during user creation with useradd command or changed with ‘usermod‘ command **using option ‘-s‘** (shell). For example, the user ‘babin‘ has the **/bin/bash** shell by default, now I want to change it to **/bin/sh**.

```bash
grep -E --color 'babin' /etc/passwd
usermod -s /bin/sh babin
```

After changing user shell, verify the user shell using the following command.

```bash
grep -E --color 'babin' /etc/passwd
```

![Image of changing user shell](https://www.tecmint.com/wp-content/uploads/2014/11/Change-User-Login-Shell.png)

### Adding the Group to an Existing User

```bash
usermod -a -G tecmint_test0 tecmint

id tecmint
```

![Image of adding an existing user to the group](https://www.tecmint.com/wp-content/uploads/2014/11/Add-Group-to-User.png)

**Note:** Be careful, while adding a new groups to an existing user with ‘-G’ option alone, will remove all existing groups that user belongs. So, always add the ‘-a‘ (append) with ‘-G‘ option to add or append new groups.

If we want to modify any detail of the already created user.

The complete guide to learn about **usermod** command is mentioned in th link below:
https://www.tecmint.com/usermod-command-examples/

## What is Shell?

The shell is the command interpretor in an operating system such as Unix or GNU/Linux, it is a program that executes other programs. It provides a computer user an interface to the Unix/GNU Linux system so that the user can run different commands or utilities/tools with some input data.

To check which shell is running on my system

```bash
# By default on Kali, it is bash shell.
# By default on Mac, it is zsh shell.

echo $SHELL

```

To learn about different types of shells:

https://www.tecmint.com/different-types-of-linux-shells/

## Linux Operators
