# General Skills

- [x] [Obedient Cat (5)](#Obedient-Cat)
- [x] [Python Wrangling (10)](#Python-Wrangling)
- [x] [Wave a flag (10)](#Wave-a-flag)
- [x] [Nice netcat... (15)](#Nice-netcat...)
- [x] [Static ain't always noise (20)](#Atatic-aint-always-noise)
- [x] [Tab, Tab, Attack (20)](#Tab-Tab-Attack)
- [x] [Magikarp Ground Mission (30)](#Magikarp-Ground-Mission)

## Obedient Cat

### *Description*

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag).

<details>
    <summary>Hint 1</summary>
    Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
</details>
<details>
    <summary>Hint 2</summary>
    To get the file accessible in your shell, enter the following in the Terminal prompt: <code>$ wget https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag</code>
</details>
<details>
    <summary>Hint 3</summary>
    <code>$ man cat</code>
</details>


### *Writeup*

Running `cat flag` will print the flag.

```bash
└─$ cat flag
picoCTF{s4n1ty_v3r1f13d_28e8376d}
```

Flag: `picoCTF{s4n1ty_v3r1f13d_28e8376d}`

## Python Wrangling

### *Description*

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py) using [this password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt) to get [the flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)?

<details>
    <summary>Hint 1</summary>
    Get the Python script accessible in your shell by entering the following command in the Terminal prompt: <code>$ wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py</code>
</details>
<details>
    <summary>Hint 2</summary>
    <code>$ man python</code>
</details>


### *Writeup*

First install the cryptography python library by running `pip install cryptography`. Looking at `pw.txt` shows that it contains a password string, and running `python3 ende.py` shows the program needs either a -e or -d flag and a file to encrypt/decrypt. Running `python3 ende.py -d flag.txt.en` shows that it needs a password, so closing and running `python3 ende.py -d flag.txt.en < pw.txt` will decrypt the `flag.txt.en` file and pass in the contents of `pw.txt` as input for the password.

```bash
└─$ python3 ende.py -d flag.txt.en < pw.txt
Please enter the password:picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```

Flag: `picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}`

## Wave a flag

### *Description*

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm) has extraordinarily helpful information...

<details>
    <summary>Hint 1</summary>
    This program will only work in the webshell or another Linux computer.
</details>
<details>
    <summary>Hint 2</summary>
    To get the file accessible in your shell, enter the following in the Terminal prompt: <code>$ wget https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm</code>
</details>
<details>
    <summary>Hint 3</summary>
    Run this program by entering the following in the Terminal prompt: <code>$ ./warm</code>, but you'll first have to make it executable with <code>$ chmod +x warm</code>
</details>
<details>
    <summary>Hint 4</summary>
    -h and --help are the most common arguments to give to programs to get more information from them!
</details>
<details>
    <summary>Hint 5</summary>
    Not every program implements help features like -h and --help.
</details>


### *Writeup*

Running `./warm` prints a message that says to pass a -h flag, so running `./warm -h` prints the flag.

```bash
└─$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
```

Flag: `picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}`

## Nice netcat...

### *Description*

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22902`, but it doesn't speak English...

<details>
    <summary>Hint 1</summary>
    You can practice using netcat with this picoGym problem: <a href="https://play.picoctf.org/practice/challenge/34">what's a netcat?</a>
</details>
<details>
    <summary>Hint 2</summary>
    You can practice reading and writing ASCII with this picoGym problem: <a href="https://play.picoctf.org/practice/challenge/22">Let's Warm Up</a>
</details>


### *Writeup*

*To be completed*

## Static ain't always noise

### *Description*

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static)? This [BASH script](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh) might help!

### *Writeup*

Running `./ltdis.sh` shows that it needs a binary as an input to the shell file, so running `./ltdis.sh static` followed by `grep pico *` will search in all files in the current directory and return the flag.

```bash
└─$ grep pico *
grep: static: binary file matches
static.ltdis.strings.txt:   1020 picoCTF{d15a5m_t34s3r_ccb2b43e}
```

Flag: `picoCTF{d15a5m_t34s3r_ccb2b43e}`

## Tab, Tab, Attack

### *Description*

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip)

<details>
    <summary>Hint 1</summary>
    After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...
</details>


### *Writeup*

Running `unzip Addadshashanammu.zip` will decompress the zip file, and traverse into the nested folders by hitting tab 6 times. The last file is `fang-of-haynekhtnamet`, and running the `file` command on it shows it's an ELF binary. Running the binary will print the flag.

```bash
└─$ ./fang-of-haynekhtnamet
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}
```

Flag: `picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}`

## Magikarp Ground Mission

### *Description*

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `abcba9f7`

<button name="button">Launch Instance</button>

`ssh ctf-player@venus.picoctf.net -p 57345`

<details>
    <summary>Hint 1</summary>
    Finding a cheatsheet for bash would be really helpful!
</details>


### *Writeup*

Running `ssh` on the server on the open port for user `ctf-player` takes us to a directory, which has two text files: `1of3.flag.txt` and `instructions-to-2of3.txt`.

```bash
ctf-player@pico-chall$ cat *.txt
picoCTF{xxsh_
Next, go to the root of all things, more succinctly `/`
```

Next step is to change directory to the root directory, which has two text files: `2of3.flag.txt` and `instructions-to-3of3.txt`.

```bash
ctf-player@pico-chall$ cd / ; cat *.txt
0ut_0f_\/\/4t3r_
Lastly, ctf-player, go home... more succinctly `~`
```

Final step is to change directory to the home directory, which has one text file: `3of3.flag.txt`.

```bash
ctf-player@pico-chall$ cd ~ ; cat *.txt
21cac893}
```

Flag: `picoCTF{xxsh_0ut_0f_\/\/4t3r_21cac893}`