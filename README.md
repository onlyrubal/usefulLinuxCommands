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

![](https://imgur.com/uqIivIH.jpg)

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

## SU AND SUDO

su is a command that allows you to change the user, without logging out and logging back in again.

Note : Typing **su** on its own is equivalent to typing **su root**.

**Interactive:** As the term implies: Interactive means that the commands are run with user-interaction from keyboard. E.g. the shell can prompt the user to enter input.

**Non-interactive:** the shell is probably run from an automated process so it can't assume if can request input or that someone will see the output. E.g Maybe it is best to write output to a log-file.

**Login:** Means that the shell is run as part of the login of the user to the system. Typically used to do any configuration that a user needs/wants to establish his work-environment.

**Non-login:** Any other shell run by the user after logging on, or which is run by any automated process which is not coupled to a logged in user.

How to switch the User to root.

The main difference between these commands is in the way they restrict access to their functions.

su (which means "substitute user" or "switch user") - does exactly that, it starts another shell instance with privileges of the target user. To ensure you have the rights to do that, it asks you for the password of the target user. So, to become root, you need to know root password. If there are several users on your machine who need to run commands as root, they all need to know root password - note that it'll be the same password. If you need to revoke admin permissions from one of the users, you need to change root password and tell it only to those people who need to keep access - messy.

sudo (hmm... what's the mnemonic? Super-User-DO?) is completely different. It uses a config file (`/etc/sudoers`) which lists which users have rights to specific actions (run commands as root, etc.) When invoked, it asks for the password of the user who started it - to ensure the person at the terminal is really the same "joe" who's listed in `/etc/sudoers`. To revoke admin privileges from a person, you just need to edit the config file (or remove the user from a group which is listed in that config). This results in much cleaner management of privileges.

As a result of this, in many Debian-based systems root user has no password set - i.e. it's not possible to login as root directly.

Also, `/etc/sudoers` allows to specify some additional options - i.e. user X is only able to run program Y etc.

The often-used sudo su combination works as follows: first sudo asks you for your password, and, if you're allowed to do so, invokes the next command (su) as a super-user. Because su is invoked by root, it does not require you to enter the target user's password. So, sudo su allows you to open a shell as another user (including root), if you're allowed super-user access by the `/etc/sudoers` file.

Refer this stackoverflow link:  
https://askubuntu.com/questions/70534/what-are-the-differences-between-su-sudo-s-sudo-i-sudo-su

Another useful link:

http://researchhubs.com/post/computing/linux-cmd/sudo-command.html

### SUDO

sudo is Linux's run as administrator button, and the syntax goes `sudo <command>`.

![](https://imgur.com/ejD2Dib.jpg)

Note: whoami is just a command that states your current user.

As you can see when using sudo the command is run as root. It is important to note that **you need to have your current user's password to use it.**

NOTE:

Not every user has the permission to use sudo. Only those users who are mentioned in the config file `/etc/sudoers`

Login as root and give permission to the user for the sudo access.

```bash
# Adding user to the sudo group
usermod -aG sudo username
```

```bash
# To list your current sudo privileges(what commands you can run, who you can run them as etc.

sudo -l
```

Refer this link to add some authorization rules while giving sudo permission.

https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/

## USERMOD UTILITY

In Unix/Linux distributions, the command **usermod** is used to modify or change any attributes of a already created user account via command line.

After creating user accounts, in some scenarios where we need to change the attributes of an existing user such as, change user’s home directory, login name, login shell, password expiry date, etc, where in such case ‘usermod’ command is used.

When we execute ‘usermod‘ command in terminal, the following files are used and affected.

- /etc/passwd – User account information.
- /etc/shadow – Secure account information.
- /etc/group – Group account information.
- /etc/gshadow – Secure group account information.
- /etc/login.defs – Shadow password suite configuration..

### ADD USER OR GROUP

NOTE:

Only root user has the permission to perform this below commands.

To add a new user or group,

```bash
sudo adduser username
```

![](https://imgur.com/wWwteJA.jpg)

```bash
sudo addgroup groupname
```

![](https://imgur.com/sEWC06K.jpg)

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

### **">" operator**

">" is the operator for output redirection. Meaning that you can redirect the output of any command to a file.
For example if I were to run echo hello > file, then instead of outputting hello to the console, it would save that output to a file called file.

```bash
echo "This is the text" > fileName
```

It is worth noting that if you were to use this operator on a file that already exists, it would completely erase the contents of that file and replace it with the output from your command

![Image of > operator](https://imgur.com/qpvaaLO.jpg)

### **">>" operator**

">>" does mainly the same thing as >, with one key difference. >> appends the output of a command to a file, instead of erasing it.

```bash
echo "This is the text" >> fileName
```

![Image of >> operator](https://imgur.com/QHZHCdt.jpg)

### **"&&" operator**

&& allows you to execute a second command after the first one has executed successfully.

Meaning `ls && echo hello` will work fine, but `dljahfrsdkjlhfsdhjklfsdhkljfh && echo hello` will fail.

![Image of &&](https://imgur.com/2LcM4I3.jpg)

This is the command that we oftenly use in our day to day commands.

```bash
echo hello >> file && cat file
```

We created something in the first command and used it in the second command.

### **"&" command**

& is a shell backgrounding operator.

Much unlike &&, & has nothing to do with and at all. & is a background operator, meaning say you run a command that takes 10 seconds to run, normally you wouldn't be able to run commands during that period; however, with & that command will still execute and you'll be able to run other commands.

![](https://imgur.com/5XPAUBq.jpg)

## **"\$" operator**

It is used to denote environment variables.These are variables set by the computer(you can set them yourself but we'll get into that) that are used to affect different processes and how they work. Meaning that if you edit these variables you can change how certain processes work on your computer.

If we want to read any environment variables, we can read it using \$ operator.

```bash
#Outputs the current user who has logged in.

echo $USER

## To display the shell that we are currently using.

echo $SHELL

## Display the value of home environment variable

echo $HOME
```

## **Understanding Environment variables**

### Set the environment variable.

```bash
export nootnoot = 1111

echo $nootnoot

#Shows the value set 1111
```

![](https://imgur.com/qjCpT08.jpg)

### Unset the environment variable

```bash
unset VARIABLE_NAME
```

### List all the environment variables.

```bash
set
```

## PIPE "|" Operator

The | operator allows you to take the output of a command and use it as input for a second command.

![](https://imgur.com/psOTao5.jpg)

## ";" Operator

The ; operator works a lot like &&, however it does not require the first command to execute successfully.

![](https://imgur.com/3FjiVnU.jpg)

## CHMOD

chmod allows you to set the different permissions for a file, and control who can read it.

They're set using a three digit number, where each digit controls a specific permission, meaning

First digit - controls the permissions for a user

Second digit - controls the permission for a group

Third digit - controls permissions for everyone that's not a part of the user or group.

| Digit | Meaning                                         |
| ----- | ----------------------------------------------- |
| 1     | That file can be executed                       |
| 2     | That file can be written to                     |
| 3     | That file can be executed and written to        |
| 4     | That file can be read                           |
| 5     | That file can be read and executed              |
| 6     | That file can be written to and read            |
| 7     | That file can be read, written to, and executed |

The way these values are calculated is this. The digit 1 means the file can be executed, the digit 2 means it can be written to, and the digit 4 means it can be read. You get the different permissions by adding these digits together. For example 1+2 is 3 meaning that file can be executed and written to. Now let's see how it all works in perspective.

Now, understanding the permissions of the different files.

- chmod 341 file : The file can be executed and written to by the user that owns the file. The file can be read by the group that owns the file. The file can be executed by everyone else.

- chmod 777 file : The file can be read, written to, and executed by the user that owns the file. The file can be read, written to, and executed by the group that owns the file. The file can be read, written to, and executed by everyone else

**ls** provides a helpful way of viewing the permissions of files in the current directory.

![](https://imgur.com/MPSlodl.jpg)

Recall that file permissions are divided into three sections, user and group and everyone else. The same is true here; however, everything starts from the second hyphen not the first, so we can just forget the first hyphen for now.

The first three characters control permissions for the user, the second three characters control permissions for the group, and the final three characters control permissions for everyone else

![](https://imgur.com/ZNaY6Iw.jpg)
(U = user, G = group, E = everyone else)

rw means as you might expect "read and write", meaning the user has read write perms to the file. Following that logic, that means members of the group and everyone else have only read perms. To convert that to numbers the permissions for that file in number form are 644. We can test this by trying to change the permissions

![](https://imgur.com/hu9mkJC.jpg)

Note: It is possible to give someone no perms to a file, You can just put 0 as the digit. 770 Means that everyone that isnt a part of the user or group cant do anything to the file.

## CHOWN COMMAND

Recall that ls allows shows us our username twice in one of it's fields.

![](https://imgur.com/8kYdiUp.jpg)

These attributes are the user, and group attributes resepectively.

Chown command, which allows us to change the user and group for any file.

Note: You can only use chown if you are "above" that other user, meaning that chown is best done with the root(administrator) user.

```bash
chown owner : group file
```

![](https://imgur.com/Q0NwmUk.jpg)

You can also use chown without specifying a group. So you can just use chown user file if you only wanted to change the user but keep the group.

```bash
chown owner : file
```

If we want change the owner or group name permission in each of the file in the root directory at once.

```bash
chown -R owner : group file
```

## rm Command

rm can make the linux system completely useless if we use it carelessly.

```bash
rm file
```

It is not worth noting that you need write permissions to the file to deleted so you cant just delete any file if you're a regular user.

![](https://imgur.com/UkPkxAh.png)

To remove every file in the directory, we need to use **-r** flag.

```bash
rm -r directory

# To supress the warning prompts

rm -f file
```

## mv Command

mv allows you to move files from one place to another. The syntax for the command is:

```bash
# To move the file to the user's home directory (relative path)

mv file ~
```

Note: You can also use mv to change the name of file.

```bash
mv file ~/renamedFile
```

## cp Command

cp does mainly the same thing as mv, except instead of moving the file it duplicates(copies) it.

```bash
cp file ~/renamedFile
```

## cd and mkdir

Linux allows you to change the location of the current directory through the use of the cd command.

![](https://imgur.com/Wd1D6H4.jpg)

For eg, to move to the user's home directory,

```bash
cd ~
```

## ln

ln is a weird one, because it has two different main uses. One of those is what's known as **"hard linking"**, which completely duplicates the file, and links the duplicate to the original copy. Meaning What ever is done to the created link, is also done to the original file.

```bash
ln source destination
```

![](https://imgur.com/GFFFO2u.jpg)

It's important to be very careful with hard links, as depending on what you're doing it can be very easy to erase data from a file.

The next form of linking is **symbolic linking(symlink)**.

While a hard linked file contains the data in the original file, a symbolic link is just a glorified reference. Meaning that the actual symbolic link has no data in it at all, it's just a reference to another file.

The syntax for a symbolic link is the exact same, but it uses the -s flag, so to create a symbolic link, you would run

```bash
ln -s file destination
```

![](https://imgur.com/9E6e92K.jpg)

NOTE:

ls even shows that its a symbolic link with the arrow pointing to what the link is referencing. It is important to note the permissions on the symlink. It has full 777 perms meaning that in theory you can execute the symlink, however since it is just a reference, in reality it has the same perms as the original file.

![](https://imgur.com/7r8Jmow.jpg)

## FIND COMMAND

**find** is an incredibly powerful, but incredibly simple command. It allows you to do just as it says, find files. It does this by listing every file in the current directory,

It is worth noting that find is recursive, so it searches every directory that is in the original directory you provided.

```bash
# To find every file in the user's home directory
find ~/

# To list every file in the OS.
find /
```

NOTE:

Only those files or directories would be listed for whom that particular user has the permission, means you cant list every file for every user.

```bash
# To list every file owned by particular user.
find dir -user username


# To list every file owned by particular group.
find dir -group groupname


#To find all *.c file belongs to a group called “ftpusers” in /data/project directory, run:

find /data/project -group ftpusers -name "*.c"

# To do case insensitive search

find /data/project -group ftpusers -iname "*.c"

#Find files by two users vivek and wendy

### match files only ##

find / -type f -user vivek -o -user wendy

### match dirs only ##

find / -type d -user vivek -o -user wendy
```

### Find the files with particular permissions.

```bash
find -perm mode
```

We can specify the MODE in three different ways as listed below.

- If we specify the mode without any prefixes, it will find files of **exact** permissions.

- If we use “-“ prefix with mode, **at least** the files should have the given permission, not the exact permission.

- If we use “/” prefix, either the owner, the group, or other should have permission to the file.

Refer this link for more info. https://www.ostechnix.com/find-files-based-permissions/

## GREP

The most useful command in linux command line.

It allows you find data inside of data. When working with large files, or a large output, it is arguably the best way to narrow the output down to better find what your looking for.

To find the file **test1234** in the whole OS whose location is unknown.

```bash
find /* | grep test1234
```

![](https://imgur.com/IR7M08S.jpg)

We can use the grep to find the content string in the file, and we can list the line number using **-n** flag.

```bash
grep "string" testFile -n
```

![](https://imgur.com/xPWWXQe.jpg)

NOTE:

We can use the **regular expressions** instead of strings.

### NANO

nano is a terminal based text editor. The syntax for nano is `nano <file you want to write to>`

### IMPORTANT FILES AND DIRECTORIES
