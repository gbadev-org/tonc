# D. More on makefiles and compiler options

<!-- toc -->

:::warning This chapter may be outdated

This part may need an overhaul and some of the suggested tools or practices may be deprecated.

:::

## Introduction {#sec-intro}

Although I gave a quick introduction to makefiles and compiler flags in the [setup](setup.html) section, a more complex look into these items may prove useful as well. So I'll present and explain the makefiles that Tonc uses in more detail, as well as some other little things about makefiles and compiler/linker options. I hope that this will give you enough ammo to understand the makefiles that are out there and allow you to figure out the more complicated aspects of the make process yourself. This page is hardly a substitute for the full documentation on the maketool make, the assembler as, compiler gcc and the linker ld, but it'll have to do for now. You can get the full documentation on these tools at [GNU Manuals Online](https://www.gnu.org/manual/manual.html). You may also be interested in MrMrIce's make tutorial, which can be found in [gbadev.org](http://www.gbadev.org)'s documentation section.

By the way, I'm no expert at this stuff. I know a few tricks about makefiles and compiler options but that's it. If you have suggestions on improving my makefiles, do tell.

## My standard makefile {#sec-make}

<div class="note">

<div class="nhcare">

Update note

</div>

As of 20060428, I'm using a different style of makefiles, which means that this section is now largely out-of-date. I'll update when it reaches the top of my priority stack (which may be a while).

</div>

What follows is the makefile for my int_demo demo. This is a moderately complex makefile, using the assembler, implicit rules and pattern substitution. The things you'll see here should be sufficient for most everyday makefiles. Two notes before we begin: this is a makefile for devkitARM. Instructions for getting it to work on DKA are indicated by comments.

<div id="cd-make-full" markdown>

```makefile
#
# int_demo.mak
#
# makefile for a simple interrupt demo


# --- Project details ---
PROJ    := int_demo
EXT     := gba
UDIR    := ../toncllib

SFILES  := $(UDIR)/single_ints.s
CFILES  := int_demo.c gba_pic.c \
    $(UDIR)/core.c $(UDIR)/interrupt.c $(UDIR)/keypad.c $(UDIR)/vid.c

SOBJS   := $(SFILES:.s=.o)
COBJS   := $(CFILES:.c=.o)
OBJS    := $(SOBJS) $(COBJS)

#--- Tool settings ---
CROSS   := arm-none-eabi-                    # use arm-agb-elf- for DKA
AS      := $(CROSS)as
CC      := $(CROSS)gcc
LD      := $(CROSS)gcc
OBJCOPY := $(CROSS)objcopy


MODEL   := -mthumb-interwork -mthumb
SPECS   := -specs=gba.specs

ASFLAGS := -mthumb-interwork
CFLAGS  := -I./ -I$(UDIR) $(MODEL) -O2 -Wall
LDFLAGS := $(SPECS) $(MODEL)

#--- Build steps ---
build : $(PROJ).$(EXT)

$(PROJ).$(EXT) : $(PROJ).elf
    @$(OBJCOPY) -v -O binary $< $@
    -@gbafix $@

$(PROJ).elf : $(OBJS)
    @$(LD) $^ $(LDFLAGS) -o $@

#COBJS compiled automatically via implicit rules
#$(COBJS) : %.o : %.c
#   $(CC) -c $< $(CFLAGS) -o $@

$(SOBJS) : %.o : %.s
    $(AS) $(ASFLAGS) $< -o $@


# --- Clean ---
.PHONY : clean
clean : 
    @rm -fv $(COBJS) $(SOBJS)
    @rm -fv $(PROJ).$(EXT) 
    @rm -fv $(PROJ).elf 
```
</div>

As you can see, I've divided the file into four sections: project details, tool settings, building and clean. I'll go through these in order of appearance.

### 1: Project details {#ssec-make-proj}

```makefile
PROJ    := int_demo
EXT     := gba
UDIR    := ../tonclibs

SFILES  := $(UDIR)/single_ints.s
CFILES  := int_demo.c gba_pic.c \
    $(UDIR)/core.c $(UDIR)/interrupt.c $(UDIR)/keypad.c $(UDIR)/vid.c

SOBJS   := $(SFILES:.s=.o)
COBJS   := $(CFILES:.c=.o)
OBJS    := $(SOBJS) $(COBJS)
```

These are all just variable definitions. Variables can be defined in two ways (see make manual, 7.2: "The Two Flavors of Variables"):

```makefile
XX  = yy
AA := bb
```

The first flavour (`=`) is a <dfn>recursively expanded</dfn> variable; the second (`:=`) is a <dfn>simply expanded</dfn> variable. In either case, whenever you now write `$(XX)` the make tool will substitute it by `yy`. And yes, the parentheses are mandatory. The difference between the two can be made clear by looking what happens if you do this.

```makefile
XX = $(XX) -c
AA := $(AA) -c
```

You would like this to behave as the C operator `+=`, but in the first case the expansion is done recursively, meaning that you get an endless loop. The second version does what you expect to happen. Simply expanded variables make things more predictable, which is a good thing. See the make manual for more details on this. Oh, in case you were wondering, the assignment operator is available for makefiles as well.

In this case I've defined variables for the project's name (int_demo), the extension (gba) and the directory where I keep all my utility routines (../libtonc). It's a good practice to do this, because you can modify and use it to suit another project without too much trouble.

The second part defines the source files (not the object files, but the actual C and assembly files) of the project. Note the use of `$(UDIR)` in many of the names. Note also that the definition of `CFILES` is split over two lines using a backslash (`\`). When you do this, though, make *absolutely* sure it's the last character on the line. If you put, say, a space behind it, you'll regret it. Some editors have an option with which you can show non-printable characters; try it if you suspect these kinds of errors (will work for the tab requirement as well).

And the third part is where it gets interesting. The form

```makefile
$(var:a=b)
```

is called <dfn>substitution reference</dfn>, one of the many forms of pattern substitution. In this case it looks at variable *var* and if it finds the string *a* at the end of a word, it'll be replaced by string *b*. I've used this to turn the lists of .s and .c files into lists of object files. GNU Make is full of string-transformation commands such as this. Look at libtonc.mak for some others.

### 2: Tools settings {#ssec-make-tool}

```makefile
CROSS := arm-none-eabi-                      # use arm-agb-elf- for DKA
AS      := $(CROSS)as
CC      := $(CROSS)gcc
LD      := $(CROSS)gcc
OBJCOPY := $(CROSS)objcopy


MODEL   := -mthumb-interwork -mthumb
SPECS   := -specs=gba.specs

ASFLAGS := -mthumb-interwork
CFLAGS  := -I./ -I$(UDIR) $(MODEL) -O2 -Wall
LDFLAGS := $(SPECS) $(MODEL)
```

More variables. First, I list the tools I use for assembling (`arm-none-eabi-as`), compiling (`arm-none-eabi-gcc`) and linking (`arm-none-eabi-gcc`). Note that I'm using the same program for compiling and linking. You can also use the command that does the actual linking (`arm-none-eabi-ld`), but if you do that you have to tell it what standard libraries to use and where to find them. gcc does that for us, which saves us a lot of hassle. To indicate it really is a different step conceptually, I'm using a different variable name for the link-step. Now, in principle the variable names are yours to choose, you can call them HUEY, LOUIS and DEWEY for all I care, but AS, CC and LD are conventional, so you'd do the world a favour by sticking to that. And there's actually a second reason why using these names are preferred, which I'll go into later. Additionally, using a separate variable for the command prefix (the `CROSS` variable) makes switching to another devkit easier. Abstraction is your friend.

The rest are lists of assembler, compiler and linker flags. I want to tell you what these do later, since it has nothing to do with the make-process in itself. It's standard practice to do something like this, though. Again, by using variables for this stuff (especially with these precise names) rather than adding them to the actual build commands, makes it easier to switch to something that requires other flags. Abstraction is a very good friend.

### 3: The build commands {#ssec-make-cmd}

```makefile
build : $(PROJ).$(EXT)

$(PROJ).$(EXT) : $(PROJ).elf
    @$(OBJCOPY) -v -O binary $< $@
    -@gbafix $@

$(PROJ).elf : $(OBJS)
    @$(LD) $^ $(LDFLAGS) -o $@

#COBJS compiled automatically via implicit rules
#$(COBJS) : %.o : %.c
#   $(CC) $(CFLAGS) -c $< -o $@

$(SOBJS) : %.o : %.s
    $(AS) $(ASFLAGS) $< -o $@
```

And now for the real work. The actual build process is composed of a number of rules. If you've forgotten what a rule looks like, here it is again:

```makefile
target : prerequisite
    command
```

One thing to remember here is that the command *must* be preceded by a TAB, *not* spaces! Anyway, the commands will run only when the target is out of date. This is true when the target doesn't exist or is older than the prerequisites. By default, the first rule in the makefile starts the build-chain, but you can start at another rule in the command line (or the Project Settings). Let's trace through the rules one by one.

It starts at the `build` rule, which has one prerequisite, `int_demo.gba`. This has a rule too, and one that requires `int_demo.elf`, which in turn requires `the object  list`. The objects list is composed of two parts, `COBJS` and `SOBJS`. The percentage signs ('%') in their rules make them <dfn>pattern rules</dfn>. Taking `SOBJS` as an example, the rule says that for every file in the list that ends in ‘.o’, the prerequisite is its ‘.s’ counterpart. Here ends the `build` chain, as the sources have prerequisites. Now the commands come into play, in an stack-unwind manner.

In almost all the commands, you'll see unknown things with dollar signs: `$^`, `$<` and `$@`. These are <dfn>automatic variables</dfn>. These refer to the full prerequisite, a single item in the prerequisite and the target, respectively. Other things to not about some commands are the hyphen ('-') and the at sign ('@') in front of them. The '@' suppresses echoing that line. The hyphen lets make ignore errors. I'm using it in the gbafix command to keep the makefile running, even if you don't have the tool.

An observant reader may have noticed that the lines for compiling the C files have been commented out. So how can the files be compiled without a rule? Via <dfn>implicit rules</dfn>. For a good number of suffices GNUmake knows how to build them. For example, if you need an object file *foo.o* and *foo.c* is nearby, it'll use the rule

```makefile
$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
```

There's an implicit rule for assembly files too, only it uses `AS` and `ASFLAGS`, which is why I used those names. You can find a full list of implicit rules and the variables they use in the make manual.

### 4: cleaning up {#ssec-make-clean}

```makefile
# --- Clean ---
.PHONY : clean
clean :
    @rm -fv $(COBJS)
    @rm -fv $(PROJ).$(EXT)
    @rm -fv $(PROJ).elf
```

This rule is separate from the others and is used to remove the output and intermediaries of the project (but not the utility objects, because they may be used in another project as well). It's really simple: rm is the command for removing stuff, the flags tells it to keep going even if the file doesn't exist (`-f`) and to display what it's doing (`-v`). And that's it. Well, almost. There's one more thing, namely the `.PHONY` directive. Remember that I said that the commands are only run when the target doesn't exist or is older that its prerequisites. Since the target (clean) doesn't exist, it's always out of date and the commands always run. But what happens if there *is* a file called clean? Because there are no prerequisites the commands will never run. The `.PHONY` directive is used to indicate that the target is a target in name only and that the commands should always be executed.

There's a lot more fun to be had with makefiles. You can use makefiles that run other makefiles (which is actually how tonc.mak is set up) or include them in other makefiles. This last one can make your life a lot easier. For example, by proper use of variables, steps 3 and 4 will rarely change between projects. This means that you could put them into a master makefile and include them in all your project-makefiles, in which you will only have to write down the things that are really specific to the current project (for an example of this, see [HAM](http://www.ngine.de)). Abstraction wants to have your babies.

With the pattern substitution and wildcard rules you can practically make makefiles that write themselves! (see the [devkitARM](https://www.devkitpro.org) sample code). The full extent of makefile capabilities it beyond the scope of this tutorial, but trust me, there's a lot more cool stuff here.

## Common compiler flags {#sec-flags}

Knowing how to write a working makefile is only part of the problem of getting the GNU tools to work. What's even more important is knowing what options you can use with the assembler, compiler and linker. In an IDE, you can enable these by selecting them in check- and list-boxes and such. No such luck for command line tools, though, here you have to set all the options by including certain flags. The key is knowing which flags to use. I'm not going to list each and every one of these since there are literally hundreds of flags. But I am going to list the ones you're most likely to see in GBA programming.

- `-c`:   (gcc) Compile to object file, but do not link.
- `-E`:   (gcc) Stop after the preprocessor stage.
- `-g`:   (as, gcc) Generates debug-information for the gdb debugger. Haven't used myself this yet.
- `-Idir`:   (gcc) Add the directory dir to the list of directories to be searched for header files. (That's a capital 'i', by the way)
- `-llibrary`:   (gcc, ld) Search the library named *library* or *liblibrary.a* when linking. Important libraries are libm (math library), libgcc, libc and libstdc++; the last three are linked automatically when you use `gcc` as a linker, rather than calling `ld` directly. And that's a lowercase 'L', by the way. “lI1”, “oO0”, I do so hate the Latin alphabet sometimes.
- `-Ldir`:   (gcc, ld) Add directory dir to the list of directories to be searched for code libraries.
- `-M`:   (gcc) The family of `-M` flags generate dependency information for header files. Normally when you create rules, you only mention the source files, which are recompiled when they've been modified. But when you modify the headers that that file includes, the file itself is still considered up-to-date. You can either create a rule for the headers yourself or let make do it for you with these flags. Unfortunately, I haven't been able to make them work for me yet.
- `-Map mapfile`:   (ld) Creates a <dfn>map-file</dfn>, which indicates where the linker puts your functions and global variables. Since it is a pure linker option, you need to use -Wl,-Map,filename when linking with gcc.
- `-marm, -mthumb, -mthumb-interwork`
:   (as, gcc, ld) Indicates the CPU model to write object files for (ARM or Thumb). The default is ARM. With `-mthumb-interwork` you allow mixing between ARM and Thumb code, which you'll want to allow for even when you're not actually using it. This flags it actually *required* under devkitARM.
- `-nostartfiles`:   (gcc, ld) Do not use the standard system start-up files when linking. If you want to link a custom *crt0.o* you want this *so* bad. (Whether you want a custom crt0.o is another matter, though.)
- `-o file`:   (as, gcc, ld) Place output in file file.
- `-Onum`:   (gcc) Enables optimisation level `num`, where `num` is usually `g`, `1`, `s`, `2`, or `3`. If you want to use inline functions, you need at least one level of optimisation. See the gcc manual for details.
- `-S`:   (gcc) compile, but not assemble. This gives you an assembly file of the C file you just compiled. Very useful for finding out how ARM assembly works, you should do this at least once.
- `-specs=specfile`:   (gcc) use specfile to determine what switches need to be passed to gcc's subprocesses (`as`, `cc1`, `cc1plus`, `ld`) instead of the default specs. (gcc.info, line 5556. Fer IPU's sake, people, don't you guys read manuals? It's only 26k lines you know).
- `-T scriptfile`:   (ld) Use scriptfile as the linker script. (Like Jeff Frohwein's lnkscript.)
- `-Wall`:   (as, gcc) Enable common warnings. Options of the form `-Wfoo` are used for all kinds of warnings actually.
- `-Wl,opts`:   (gcc) passes options to the linker; opts is a comma-separated list.
