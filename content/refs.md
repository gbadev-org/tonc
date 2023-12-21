# F. References and links {#ch-}

<!-- toc -->

## General sites {#sec-gen}

### Essentials {#ssec-essential}

- [www.devkitpro.org](http://www.devkitpro.org/). Home of **devkitARM**, the toolchain of choice for GBA development. And NDS and more. Updated regularly and you can find a **libgba** and sample code here too.
- [www.gbadev.org](http://www.gbadev.org). GBA development hub. Tools, documents, tutorials can all be found here. A visit to the [forum](http://forum.gbadev.org) is highly recommended if you're just starting, whether you have problems or not. If you do have a problem, chances are you're not the first and that it has been solved before here. Just remember the [rules of posting](http://www.albinoblacksheep.com/flash/posting.php) before you start a topic.
- [No\$gba](http://nocash.emubase.de/). Martin Korth's site. You can find the immensely complete (though Spartan) [GBATek](https://problemkaputt.de/gbatek.htm) reference document and the most accurate emulator [here](http://nocash.emubase.de/gba.htm), both of which are insanely great. Though the freeware version doesn't have any debug screens, the \$15 homebrew version does.
- [vba.ngemu.com](http://vba.ngemu.com), The **VisualBoy Advance** emulator. Not as accurate as no\$gba when it comes to timings, but still very, very good, and has a more friendly interface and all kinds of cool viewers for tiles, maps, IO registers and the like.

### Alternative dev environments {#ssec-altdev}

- [www.ngine.de](http://www.ngine.de), Host of **HAM**. HAM is a full C developer environment for the GBA, complete with IDE, palette and map editor and, of course, compiler. There is also an extension library called [HEL](http://www.console-dev.de) with extra (and optimized) code. Taking a look at that would be a good idea.
- **DragonBasic**. If you don't like all the intricacies of C/asm, you might try this BASIC-like environment. The project is a little, uhm, asleep right now, though.
- [Catapult](http://www.nocturnal-central.com/). Don't know too much about Catapult, but from what I've seen, it seems to work a little bit like Gamemaker: you create images/sound and scripts that Catapult ties together into a ROM image. Catapult comes complete with graphic, map and sound editors, tutorials, samples, emulator and probably more.

### Personal sites {#ssec-personal}

A few sites of (high-ranked) forum-dwellers. These guys have been around for a while and you can learn a lot from playing their demos and browsing through their source code.

- [darkfader.net](http://darkfader.net/main/). Darkfader's site, with information, tools, demos, code not only for GBA development, but many other systems as well.
- [deku.gbadev.org](http://deku.gbadev.org/). DekuTree64's site has more than just the sound mixer; there's also some demos (with source) and tools like **quither**, a quantizer / ditherer for 16 color tiles.
- Headspin had put together [this overview](http://members.iinet.net.au/~freeaxs/gbacomp/) of various items, incluning the different compression routines and music players available.
- [www.thingker.com](http://www.thingker.com/gba/). Scott Lininger's site with a number of demos, including **multiplayer** code, which seems very hard to come by.
- [www.console-dev.de](http://www.console-dev.de). Peter Schaut's site, with VisualHam, the HAMlib IDE; HEL, the HAM addon library; katie, a data-management tool and more.
- [www.pineight.com](http://www.pineight.com/). Site of gbadev faq maintainer, tepples. There are a number of interesting things here. Special mentions for **Tetanus on Drugs**, a zonked-out version of tetris (can't call it a clone as it is so much more), and **GBFS**, a file system for the GBA.

## Documents {#sec-doc}

### Tutorials {#ssec-tut}

- [www.belogic.com](http://www.belogic.com). Pretty much _the_ site on GBA sound programming. Has info on all the registers, and a set of _very_ complete demos.
- If you're looking for **C/C++ tutorials**, there seems to be some good stuff [here](http://www.cprogramming.com/tutorial.html)
- DekuTree's [sound mixing tutorial](https://stuij.github.io/deku-sound-tutorial/). Whereas Belogic shows the basics of sound programming, this sight guides you through the steps of making a sound/music mixer.
- [www.drunkencoders.com](http://www.drunkencoders.com). This is the new home of **the PERN project**, the original series of tutorials for gba development. PERN was set for a complete renewal, but that seems to have been deprioritised in favor of the DS, which you will also find a lot about there.
- jake2431 has been gathering **NDS / C / GBA tutorial links** on the gbadev [forum:8353](http://forum.gbadev.org/viewtopic.php?t=8353)

### Reference documents {#ssec-ref}

- The [**comp.lang.c FAQ**](http://c-faq.com/). Pretty long, but very useful if you're learning C as well as GBA programming.
- A document on [**C coding standards**](http://www.jetcafe.org/~jim/c-style.html), one of many floating around. If you've based your code on any of the non-tonc tutorials out there you **_need_** to read this. The standard doesn't have to be followed religiously, but adopting most of them would be a good idea and would solve a lot of the bad habits the other sites teach.
- Mr Lee has a few things to say about [optimization](http://leto.net/docs/C-optimization.php). These are simple optimization that cost nothing or little in readability.
- The [**gbadev forum FAQ**](http://forum.gbadev.org/viewtopic.php?t=418). Essential reading, whether you're new or not. Bookmark it, make a local copy, print it out; I don't care, but get FAQed.
- The [**GBATek**](https://problemkaputt.de/gbatek.htm). reference document. This is basically the GBA-coders' bible (only this one _is_ a worthwhile read). The information density is very high and maybe a little perplexing if you're just starting, but when you get the hang of it, it's pretty much all you'll require. Is also part of HAMLib's documentation.
- The [CowBite Spec](http://www.cs.rit.edu/~tjh8300/CowBite/CowBiteSpec.htm), a another reference document. At least partially based on GBATek. Not as rich, but probably more understandable.
- [www.gnu.org](http://www.gnu.org/manual/manual.html#Development). **GCC documentation** in various formats. CHM versions (with search functions) can be found [here](http://htmlhelp.berlios.de/books/chm.php). These sites have manuals on the GCC toolchains and other things. Get the files for the assembler (**AS**), compiler (**GCC**), linker (**LD**) and preferably the maketool (**make**) as well. The preprocessor manual (**cpp**) may be useful as well.

### ARM docs {#ssec-arm}

Naturally, the ARM site itself also has useful documents. Note that most of these are pdfs.

- [miscPDF 8031](http://www.arm.com/miscPDFs/8031.pdf). The **Arm Architecture Procedure Call Standard** (AAPCS). Explains how parameters are passed between functions. Required reading if you want to do assembly.
- [PDF DAI0034A](http://www.arm.com/pdfs/DAI0034A_efficient_c.pdf). **Writing efficient C for ARM**. Although it's written with ARM's own compiler in mind, some tips will work for other toolchains as well.
- [PDF DDI0210B](http://www.arm.com/pdfs/DDI0210B_7TDMI_R4.pdf) The big one: the complete **technical reference manual** for the ARM7TDMI.
- **Instruction set reference sheets**. [ARM](http://www.arm.com/pdfs/QRC0001H_rvct_v2.1_arm.pdf) and [THUMB](http://www.arm.com/pdfs/QRC0001H_rvct_v2.1_thumb.pdf) versions.
- Support faqs on **alignment issues**: [faqdev 1228](http://www.arm.com/support/faqdev/1228.html), [faqdev 1469](http://www.arm.com/support/faqdev/1469.html), and [faqip 3661](http://www.arm.com/support/faqip/3661.html).

## Tools {#sec-tools}

### Source code tools {#ssec-tools-text}

If you're still using Notepad to write your GBA code, don't. Do yourself a favor and just … don't, OK? Though I personally use Visual C for writing code, there are some other very nice tools for the job, both in terms of general text editors as IDEs.

- **[ConTEXT](http://www.fixedsys.com/context)**. A while back there was a thread where someone asked for a replacement editor for Notepad since, and I quote, “Notepad SUCKS!”. The name ConTEXT popped up a couple of times, and I find it very nice indeed, and not just for coding purposes. It allows for custom highlighters, integrated shell commands (to run makefiles for example) and attachable help files
- [**Programmer's Notepad**](http://www.pnotepad.org/) (PN). Good and versatile text editor. Comes with the devkitPRO installation.
- **[Eclipse IDE](http://www.eclipse.org)**. While I haven't had time to work with it firsthand, a good number of gbadev forum-dwellers swear by it. You can read how to set it up for GBA development in [forum:5271](http://forum.gbadev.org/viewtopic.php?t=5271).
- **[Dev-C++](http://www.bloodshed.net/)**. Dev-C++ is another IDE that comes up often and maybe worth a look. [forum:1736](http://forum.gbadev.org/viewtopic.php?t=1736) has info on how to set it up, but it's an old thread so you may have to do a little extra work.

### Graphics tools {#ssec-tools-gfx}

Just as Notepad sucks for coding (and anything apart from the simplest text editing), MS-Paint is hell on Earth when it comes to the kind of graphics you need in GBA games. What you need is a tool that allows full control over the bitmap's palette, and MS-Paint fails spectacularly in that respect. So, I might add, does Visual C's native bitmap editor. And even big and bulky photo-editing tools like PhotoShop and Paint Shop Pro have difficulty here, or so I'm told. So here are some tools that do allow the kind of control that you need. Whatever tool you plan on using: **make sure it doesn't screw up the palette**! Some editors are known to throw entries around.

- **[gfx2gba](http://www.ohnehirn.de/tools/)**. Command-line converter of graphics with interesting features such as tile-stripping, palette merging and supports all bitdepths and BIOS compression routines. Note that there are two converters named gfx2gba; you'll want the one my Markus. The HAM distribution includes this tool.
- **[The GIMP](http://www.gimp.com)**. Very complete GNU-based bitmap/photo editor.
- **[Graphics Gale](http://www.tempest-j.com/gale/e/)** is a very complete graphics editor. It has all the tools you would expect a bitmap editor to have, a proper palette editor and an animation tool.
- **[Usenti](http://www.coranac.com/projects/#usenti)**. This is my own bitmap editor. It may not be as advanced as Graphics Gale, but that does make the interface a lot easier. Aside from that it has some very interesting palette tweaking options like a palette swapper and sorter, and can export to GBA formats in binary, ASM and C code.

### Map Editors {#ssec-tools-map}

While the maps that I've used in Tonc were created on the fly, for any serious work you need a map editor. Here are a few.

- **[MapEd](http://nessie.gbadev.org)**, by Nessie. Allows multiple layers, collision tiles and custom exporters. Yum.
- **[Mappy](http://www.tilemap.co.uk/mappy.php)**. This is a general purpose map editor which can be used for a lot of different types of maps
- **[Mirach](http://www.coranac.com/projects/#mirach)**. This is my own map editor, but lack of time means that I haven't been able to get all the tools that I wanted in yet `:(`.

### Misc tools {#ssec-tools-misc}

- **[excellut](http://www.coranac.com/projects/#excellut)**. One thing you do not want in GBA programming is to call mathematical functions. You want [look-up tables](luts.html) to get the proper values. Excellut sets up MS Excel to enable you to create any kind of LUT you can think of within seconds (well, OK, minutes). If you haven't created a LUT builder of your own (and maybe even if you have)it's definitely worth a look.

## Books {#sec-books}

- Douglas Adams, “_The Hitchhiker's Guide to the Galaxy_”. OK, so this isn't exactly a reference, but recommended nonetheless. If only to know the significance of the number 42 and the origin of the Babel Fish.
- Edward Angel, “_Interactive Computer Graphics with Open GL_”. Though this is a book on 3D, Lots of the linear algebra can be applied to 2D as well. Relevant chapters are 4 (matrix transformations) and 5 (perspective (Mode 7 anyone?)). Make sure you have the 3<sup>rd</sup> edition, there are too many embarassing errors in the second.
- George B. Arfken & Hans J. Weber, “_Mathematical Methods for Physicists_” If physics were an RPG, this would be the Monster's Manual. Chapters 1-3 deal with vectors and matrices in great detail.
- André LaMothe, “_Black Art of 3D Game Programming_”. For the DOS-era, so may be hard to find. Deals with 3D programming under heavy hardware constraints (just like the GBA). Very nice.
- André LaMothe “_Tricks of the Windows Game Programming Gurus_”. Another 1000+ page tome by Mr LaMothe; one of many), an excellent guide to game programming in general, and to DirectX in particular.
- David C. Lay, “_Linear Algebra and its Applications_”. Nearly everything on my [matrix](matrix.html) page comes out of this book.
- O'Reilly pocket references for “_CSS_” and “_HTML_” by Eric Meyer and Jennifer Niederst, respectively. Absolute lifesavers for something like this site.
- Steve Oualline, “_How Not to Program in C++_”. The cover features a computer sticking its tongue out at you; the first sentence of the introduction is “Pain is a wonderful learning tool”. You just know this is gonna be good. This book gives you 111 broken code problems to solve, ranging from obvious to crafted by the Dark Lord himself. If you can't recognize yourself in at least half of these problems, you haven't been coding in C for very long.
