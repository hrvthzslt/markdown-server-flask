---
title: "My Favorite Tools From My Toolbox"
date: 2024-02-22T14:59:10Z
draft: false
---

# My Favorite Tools From My Toolbox

Since the second half of the last year I started to build a collection of shell scripts that make some of my special use cases easier to handle. I want to share some of them with you.

## Wave Goodbye for My Aliases (Most of Them)

I had a huge collection of aliases, lot of them are copied from other people, and it become a mess. There are two rules I made for handling this earth shattering crisis:

- If an alias is only used for typing less without complex commands, I delete it. I prefer to type more and forget less. (for example: remove `ga` alias, type `git add .`)
- If the alias had some sort of complex command, I convert it to a script.
- If I don't want to write down `docker compose` for the eleventh million time today, I create a command with a shorter name which can receive arguments and do the same thing.

I made some wrapper scripts that can make the base command shorter, receive all the same arguments, and can contain methods for use cases that I prefer.

So when I type `dc up` it is the same as `docker-compose up -d --remove-orphans`. This can sound like a contradiction to the first rule, but there is no time when I don't want to use `docker-compose up` without the `-d` and `--remove-orphans` flags. And it is easier to review in a script than a multi hundred line long alias list.

## Timeboxing

I used to love the Pomodoro technique, but it had too much rules for me, I just want to control my time spent at a computer. Still I made a script called `pom` (for tribute) for starting a countdown timer.

`pom -s 45` will store a file with the timestamp of the date and time when the countdown will expire. `pom` will read the timestamp and print the remaining time like this: `44:51`. This way it can be rendered with interval calls, which means its perfect for a status bar.

## Dev containers

The script called `devc` will pull a docker image, start a container and enter it with a shell. This itself is not a big deal, but after exit it automatically commits the changes of the container to a new image.

By the naming of the image and container, every time I run `devc ubuntu` I will work with the changes of the last time I used `devc ubuntu`. Let's say it together children: `devc ubuntu`.

## Running composer or php with exact versions in containers

I mostly work on php projects (no Lambo), sometimes it is handy to run a composer or php command with a specific version.

For example running composer install with a specific version of composer and php:

```bash
domp 7.0 install
```

Or starting a php 7.4 repl:

```bash
dhp 7.4 -a
```

## Emu

This is a wrapper for qemu, which is a "A generic and open source machine emulator and virtualizer", I use it for testing in other operating systems. The main motivation behind this script is qemu has a lot of flags and I just want a base command with the same flags every time.

```bash
 emu -s 23G -i uhu-linux-3.iso -m 4G -c 2
```

This command will start a virtual machine with 23GB of storage, 4GB of memory and 2 cores, and it will boot from the `uhu-linux-3.iso` file, and save my life. I could use Quickemu as well.

## Tmux sessionizer

Everyone and their grandmother has a spin on this topic, I keep mine for another time.

[mainpage](/)
