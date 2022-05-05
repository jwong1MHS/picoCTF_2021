# picoCTF 2021

A beginner-style CTF hosted on picoGym at https://play.picoctf.org/practice?originalEvent=34

## Table of Contents

| Categories                                         | Completed | Progress                                                     |
| -------------------------------------------------- | --------- | ------------------------------------------------------------ |
| [Binary Exploitation](#Binary_Exploitation)        | 0/11      | ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0) |
| [Cryptography](#Cryptography)                      | 1/15      | ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/7) |
| [Forensics](#Forensics)                            | 2/12      | ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/17) |
| [General Skills](General_Skills/General_Skills.md) | 7/7       | ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100) |
| [Reverse Engineering](#Reverse-Engineering)        | 0/17      | ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0) |
| [Web Exploitation](#Web-Exploitation)              | 0/16      | ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0) |

# Cryptography

- [x] [Mod 26 (10)](#Mod-26)

## information

### *Description*

Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}`

<details>
    <summary>Hint 1</summary>
    This can be solved online if you don't want to do it by hand!
</details>


### *Writeup*

Use a tool to shift all letters by 13.

```bash
└─$ echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}
```

Flag: `picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}`

# Forensics

- [x] [information (10)](#information)
- [x] [Matryoshka doll (30)](#Matryoshka-doll)

## information

### *Description*

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg)

<details>
    <summary>Hint 1</summary>
    Look at the details of the file
</details>
<details>
    <summary>Hint 2</summary>
    Make sure to submit the flag as picoCTF{XXXXX}
</details>


### *Writeup*

Running `exiftool` on `cat.jpg` shows the license string to be in base64, so using the decoder gives the flag.

```bash
└─$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 --decode
picoCTF{the_m3tadata_1s_modified}
```

Flag: `picoCTF{the_m3tadata_1s_modified}`

## Matryoshka doll

### *Description*

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg)

<details>
    <summary>Hint 1</summary>
    Wait, you can hide files inside files? But how do you find them?
</details>
<details>
    <summary>Hint 2</summary>
    Make sure to submit the flag as picoCTF{XXXXX}
</details>


### *Writeup*

Running `binwalk` on `dolls.jpg` shows there is a zip file hidden in the picture, so unpack it with `binwalk -e`.

```bash
└─$ binwalk -e dolls.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378956, uncompressed size: 383938, name: base_images/2_c.jpg
651614        0x9F15E         End of Zip archive, footer length: 22
```

```bash
└─$ binwalk -e 2_c.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg
383805        0x5DB3D         End of Zip archive, footer length: 22
383916        0x5DBAC         End of Zip archive, footer length: 22
```

```bash
└─$ binwalk -e 3_c.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79808, name: base_images/4_c.jpg
201423        0x312CF         End of Zip archive, footer length: 22
```

```bash
└─$ binwalk -e 4_c.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 64, uncompressed size: 81, name: flag.txt
79786         0x137AA         End of Zip archive, footer length: 22
```

The extraction of `4_c.jpg` gives `flag.txt`, which contains the flag.

```bash
└─$ cat flag.txt
picoCTF{336cf6d51c9d9774fd37196c1d7320ff}
```

Flag: `picoCTF{336cf6d51c9d9774fd37196c1d7320ff}`
