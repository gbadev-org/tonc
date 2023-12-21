# G. Change Log {#ch-}

### Mar 2013 (1.4.1)

Maintaince update. also includes things from the [errata page](http://www.coranac.com/documents/tonc-errata/)

- ![fix](./img/log/bul_excl.png) Changed from `arm-eabi` to `arm-none-eabi`.
- ![upgrade](./img/log/bul_upgr.png) Little html fixes here and there. Thank Glod for directory search-and-replace tools.
- ![fix](./img/log/bul_excl.png) `all code`: since GCC 4.7 broke my assembly functions, I've recompiled all code with the latest devkitArm (currently 40) for asm compatilibity. The examples and tonclib should all work again. I still have to adjust the text to match though.
- `asm.htm`: fixed non-matching variable names in [data sections](asm.html#ssec-gas-dsec)'s code snippet. Thanks, Gdogg
- `gfx.htm`: removed a lost semicolon in the [blending demo](gfx.html#ssec-bld-demo).
- `hardware.htm`: IO-ram upper limit was given as `0401:03FF`, which should be `0400:03FF`. Thanks, G M.
- code: Fixed links to grit for `m7_demo`, `m7_ex`, `tte_demo`.
- [objaff.htm 11.5](objaff.html#sec-combo): fixed spurious `sina` and `cosa` calculations in `obj_rotscale_ex()` and `oac_rotscale()`. Thanks, dasi.
- GNU assembler manual has moved to <http://sourceware.org/binutils/docs/as/index.html> (thanks, Joseph).
- Code snippet at §23.2.1:Basic operations. “x68 asm” should, of course, be “x86 asm” (thanks, Wladimir).
- Some of the memory map entries in §1.3 were … imprecise (thanks Pius).

### Oct 2008 (1.4)

… Or maybe not. Silly little errors.

- ![fix](./img/log/bul_excl.png) text: the `se_index_fast()` function in [regbg:map-layout](regbg.html#ssec-map-layout) was wrong; the second condition should have used \``(bgcnt&BG_REG_64x64) == BG_REG_64x64`'. Fixed.
- ![fix](./img/log/bul_excl.png) text: the `ldm` example in [asm:memory](asm.html#ssec-arm-mem) did not list the right values for `ldmda` and `ldmdb`. Fixed.
- ![fix](./img/log/bul_excl.png) code: removed `void*` arithmetic in `tonc_surface.h` (hopefully) and fixed `berk.c` from the timer demo so that it compiles now. Thanks for noticing, elwing and Ealdor.
- Fixed a few random typos here and there

### May 2008 (1.4)

- ![fix](./img/log/bul_excl.png) text: Last batch of spelling/grammar fixes. Thanks guys. Especially Jake.
- text: changed the stuff on #include for less hyperbole and more explanations.

I think that'll be all then.

### May 2008 (1.3)

- ![upgrade](./img/log/bul_upgr.png) code: All demos that use text now use TTE to do it. Variable width text just looks prettier than fixed width.
- ![upgrade](./img/log/bul_upgr.png) code: Some of the advanced demos use grit to convert the graphics.
- ![new](./img/log/bul_new.png) text: added TTE chapter with information about creating (fast) text renderers for every occasion.
- ![upgrade](./img/log/bul_upgr.png) text: I've revamped the [setup chapter](setup.html). It now covers template makefiles and some potential problems with the installation.
- ![swap](./img/log/bul_swap.png) text/code: the [irq chapter](interrupts.html) and its demo uses the new master ISR.
- ![fix](./img/log/bul_excl.png) text: Fixed the brown text in the pdf. For anyone who has the same problem with CutePDF, go to `CutePDF printer->Properties->Paper/Quality->Advanced->Graphic->Image Color Management` and make sure `ICM Method` is not set to `Host system`. How silly of me not to look there first.
- text: Finally removed the obsolete section for IRQ-handling with older devkits.
- ![new](./img/log/bul_new.png) tonclib: There is a new system for text called TTE. It's pretty cool. Read more about it in [tte.htm](tte.html).
- ![new](./img/log/bul_new.png) tonclib: New rendering functions. There are now ‘TSurface’ structs defining a rendering surface and basic primitive renderers for different surface types. Functionality includes: pixel, line rectangle renderers, a blitter and floodfill. Key surface types: 16bpp bitmap, 8bpp bitmap and 4bpp tiles.
- ![new](./img/log/bul_new.png) tonclib: Color adjustment functions. Fading, blending, brightness and more.
- ![new](./img/log/bul_new.png) tonclib: Added [tonccpy and toncset](http://www.coranac.com/2008/01/25/tonccpy/), memcpy and memset replacements that actually work for VRAM as well.
- ![new](./img/log/bul_new.png) tonclib: Put tonclib documentation online: [http://www.coranac.com/man/tonclib/index.htm](http://www.coranac.com/man/tonclib/index.htm).
- ![new](./img/log/bul_new.png) tonclib: Added `tonc_libgba.h`, a header with most of the libgba constants and functions names mapped to tonc equivalents.
- ![swap](./img/log/bul_swap.png) tonclib: Changed the master ISR to one that doesn't automatically enable interrupt nesting. It's a bit of a downgrade, but it's probably more appropriate. This shouldn't affect anyone that didn't use nested interrupts. The old version is still available, it's just not the default.

### Dec 2007 (1.3b)

- ![new](./img/log/bul_new.png) Upgraded the [recommendations](first.html#sec-notes) section with a longer list and examples. If you've read other tutorials then **please read this**!
- ![fix](./img/log/bul_excl.png) More spelling and grammar fixes (thanks [Patater](http://patatersoft.info/))
- ![fix](./img/log/bul_excl.png) Fix in the template makefile for c++. It's `-fno-exceptions`, not `-fno-expections`, you silly boy. (Thanks muff).
- ![swap](./img/log/bul_swap.png) All projects now default to cart-boot, not multiboot. This is partially because multiboot doesn't work in devkitPro r21 (at least, not directly), but also because that's how it's normally done anyway.
- Changed `git` to `grit` where appropriate. Also fixed the download links of everything to point to the new site.

### Feb 2007 (v1.3b)

As every programmer knows, you're supposed to write down the changes you make while making them. As every programmer also knows, this has a tendency to be forgotten <span class="kbd">\^\_\^;;</span>. I probably missed a few things here.

Text:

- ![new](./img/log/bul_new.png) There's now a PDF version too, made by CutePDF. It's a nice tool, but apparently sometimes messes up pictures a little. Page-breaks also occur in unfortunate places, but this is a browser problem. It's _supposed_ to be countered by CSS's `page-break-inside`, but I guess that's not widely supported yet. If anyone knows of a potential fix, let me know. Additionally, if anyone knows of a html→PDF converter that keeps headers for the table of contents, I'd be very interested in that. Mind you, it needs to be able to print a 1.4 MB file, and print it **correctly**! Some PHP html2pdf tools don't render correctly. Word/OpenOffice are probably no good either, as they have a problem with floating divs and `pre` tags. Also, Word nearly crashes on reading the file. Hehehehe.
- ![new](./img/log/bul_new.png) hardware: GBA pictures and capabillity description. Anyone have a GBA Micro pic I can borrow?
- ![new](./img/log/bul_new.png) first: hardware pictures.
- ![new](./img/log/bul_new.png) bitmaps: new demo discussion for drawing primitives in modes 3/5. The page flipping demo has been moved forward in the chapter, and the mode 3/4/5 demo moved back to after the data discussion.
- ![new](./img/log/bul_new.png) objbg: note and pic on reading tiles as bitmaps, as this this still happens to some occasionally.
- ![new](./img/log/bul_new.png) regbg: pic to show what the offset registers really do.
- ![new](./img/log/bul_new.png) affine: added inverse 2x2 matrix equation.
- ![new](./img/log/bul_new.png) affbg: new structs for affine backgrounds, plus new typedefs and a very nifty method of initializing the affine parameters.
- ![new](./img/log/bul_new.png) mode7ex: across the board upgrades and new stuff. It now uses proper graphics, making everything look a lot nicer. New background, new fade, sprite rotation-animation and sorting and different methods of motion.
- ![new](./img/log/bul_new.png) asm: the proper form of the chapter is materializing. New structure of sections, beginning with a one on general ASM. More examples and more ways of doing the same thing for comparative purposes. Has a section on common constructs now too.
- ![new](./img/log/bul_new.png) New subsection on linear interpolation of luts.
- ![upgrade](./img/log/bul_upgr.png) Chapter indexing. All references are how of the form ‘ch.foo’.
- ![upgrade](./img/log/bul_upgr.png) Some chapters have been renamed. _tonctonc_ is now _intro_, _toncmake_ is now _makefile_. Also, _luts_ has been merged into _fixed_, and the parts on makefiles and editors in _setup_ has been moved to a separate file called _edmake_. Might move that into _makefile_ too.
- ![upgrade](./img/log/bul_upgr.png) All register and register-like tables now use alternating background colors for easier reading.
- ![upgrade](./img/log/bul_upgr.png) regobj: Different structure for `obj_demo` discussion.
- ![upgrade](./img/log/bul_upgr.png) regbg: deleted `BGINFO` stuff, as it was never used much and impractical to boot.
- ![upgrade](./img/log/bul_upgr.png) regbg: New graphics besed on Super Metriod's Brinstar instead of the original Norfair. 's prettier now. Also rearranged stuff.
- ![upgrade](./img/log/bul_upgr.png) affine: updated ‘finishing up’ for new routines.
- ![upgrade](./img/log/bul_upgr.png) dma: discussion of upgraded DMA demo
- ![upgrade](./img/log/bul_upgr.png) interrupts: discussions of the new and (much) improved interrupt handler and its demo.
- ![upgrade](./img/log/bul_upgr.png) Inline functions for fixed-point functionality.
- ![fix](./img/log/bul_excl.png) Every chapter has been checked for spelling and grammar. Again. Sigh.

Code:

- ![new](./img/log/bul_new.png) tonclib: All new tonclib, with new file structure. All files are prefixed with `tonc` so the don't interfere with outside files. The types, memory map and register #defines are centralized in _types_, _memmap_ and _memdef_. The main file to include is now `tonc.h`.

- ![new](./img/log/bul_new.png) tonclib: Doxygen comments all around. The resulting documentation can be found in `tonclib.chm`.

- ![new](./img/log/bul_new.png) tonclib: a few of the new items. A brand new interrupt handler for nested, prioritized interrupts. Mode 3/5 line drawers. A new .12f sine LUT with support functions as well as lerping functions. All fixed-point macros are now inlines.

- ![new](./img/log/bul_new.png) tonclib: The `BGINFO` struct and functions are gone. Wasn't worth much anyway. Also removed are internal OAM shadows; it's better that you can define them when needed and can save IWRAM by potentially storing them in EWRAM. All OAM functions now use general object pointers, rather than buffers.

- ![new](./img/log/bul_new.png) tonclib: yet another Great Renaming. Among other things: The leading underscore for zero-#defines are gone. I thought it was a good way if guarding against potential unsafe operations, but they just look too weird to use. And there was much rejoicing. Some macros have lots their `_ON` prefix when it's obvious that that's what they do. OAM structs are now `OBJ_ATTR` and `OBJ_AFFINE` and supporting functions are now prefixed `obj_` and `obj_aff_`. `BGAFF_EX` is now `BG_AFFINE` and used in most affine BG functions. A complete list can be found in `tonc_legacy.h`, which you can #include to keep compatibility with older code.

- ![new](./img/log/bul_new.png) projects: the structure of the projects hierarchy has been altered. The demos have been categorized as basic, extended or advanced, which correspond with the tonc-text parts. Basic demos are simpler, with simple makefiles. They are completely self-sufficient, which should help learning the ropes. The extended demos have more complete makefiles and make use of tonclib. The advanced demos have devkitPro-like makefiles. As much as I'd like to, the actual DKP templates don't quite suit my purposes (sorry, Dave <span class="kbd">:P</span>) so I rolled my own. The advanced demos also make use of assembly files for data.

  The project folders also contain `.pnproj` files, which can be opened and run from Programmer's Notepad.

- ![new](./img/log/bul_new.png) projects: New projects. `m3_demo`, for drawing in mode 3. There are also a couple of new ones in the `lab` folder. They don't have discussions yet, but they're worth checking out. `bigmap` should be of particular interest.

- ![upgrade](./img/log/bul_upgr.png) projects: Update projects. All projects have been updated to the new tonclib. The DMA, irq and mode 7 demos have had drastic changes in content. `dma_demo` is now about using HDMA effects, in this case making a circular window. `irq_demo` uses the new irq handler to uts fullests with nested interrupts and changing irq priorities. As for `mode7ex`, well, you'd better just see for yourself.

### Jul 23, 2006 (v1.2.4)

- ![new](./img/log/bul_new.png) Added a rather long chapter on [ARM/THUMB assembly](asm.html). This is still a draft version, though. Most of the content is there, but I still need to reshuffle sections and spell/grammer check the whole thing.
- And yet more spell fixes <span class="kbd">\>\_\<</span>.

### Jun 3, 2006 (v1.2.3)

- ![upgrade](./img/log/bul_upgr.png) Changed makefiles and build instructions to use devkitARM r19.
- ![upgrade](./img/log/bul_upgr.png) All sections and subsections are now numbered, w00t!
- ![fix](./img/log/bul_excl.png) Added alignment attributes to most structs, as those are now pretty much _required_ if you want struct-copies to work properly. For more, see [here](bitmaps.html#ssec-data-align)

### Apr 28, 2006 (v1.2.2)

- ![new](./img/log/bul_new.png) Finally realized what caused the 1 pixel offset I've been seeing in affine objects sometimes (thanks NEiM0D). Updated [affobj.htm](affobj.html) and `obj_aff` for it.
- ![swap](./img/log/bul_swap.png) Moved the new off-center affine object stuff to its [proper place](affobj.html).
- ![upgrade](./img/log/bul_upgr.png) Some small sed usage to convert from GCC error-reports to Visual C++ format, based on [this](http://www.devkitpro.org/devstudio.shtml).
- ![upgrade](./img/log/bul_upgr.png) Now that my html auto-numbering system works (at least a first trial), text.htm is now de-reffed. Yay.
- Small changes to interrupts and gfx.
- Added Javascript to make the id attributes visible. Will probably add more later.

### Apr 28, 2006 (v1.2.1)

- ![fix](./img/log/bul_excl.png) Apparently no\$gba doesn't like it if you use section mirroring, like I did for REG_INTMAIN and REG_IFBIOS. These now use the proper addresses.
- ![fix](./img/log/bul_excl.png) Spelling fixes in intro.htm. Thanks again, Mick.
- ![upgrade](./img/log/bul_upgr.png) New makefiles for extended and advanced projects. It does mean that makefile.htm is now pretty much behind the times.
- ![upgrade](./img/log/bul_upgr.png) Updated [setup.htm](setup.html) for devkitARM changes. Changed the figures a little too.
- ![new](./img/log/bul_new.png) New chapter called [the lab](lab.html), where I'll place new stuff that's almost, but not quite, ready. Currently contains text for priorities and sprite sorting, and a discussion on affine transformations around a non-center reference point. Both come with new demos called `prio_demo` and `oacombo`.
- ![new](./img/log/bul_new.png) Added instructions on how to run makefiles via context or PN in [setup.htm](setup.html).
- ![new](./img/log/bul_new.png) Added gfx2gba and grit conversion instructions in a few places.
- More notes in bitmaps.htm's [data section](bitmaps.html#sec-data).

<div class="nh">

Probable upcoming changes

</div>

I intend to make a few changes in tonc's code. First, I'll try to decouple the code in the basic demos from tonclib, which should make them easier to understand as you won't have to browse through all the other stuff. Second, this will allow me to rework and optimize tonclib, which is now hampered in some areas by me having to keep a number of things simpler than I'd like to. Now, this is what I'd _like_ to do; I can't really tell when (if) I will get round to it.

Also, I have half a mind of changing the current DMA demo to [this one](http://forum.gbadev.org/viewtopic.php?t=9023), which simply looks a lot cooler, even though there's is a lot more magic going on. Meh, we'll see.

### Mar 21, 2006 (v1.2)

More non-final updates. Quite a lot actually.

- ![fix](./img/log/bul_excl.png) More typos fixed.
- ![fix](./img/log/bul_excl.png) `bg_init()` never initialized the `BGINFO` position. Oops.
- ![swap](./img/log/bul_swap.png) Tossed chapter order around a bit. I've moved [keys](keys.html) up to right after [bitmaps](bitmaps.html), which is a much better place for it anyway.
- ![upgrade](./img/log/bul_upgr.png) Updated [First Demo](first.html), [Bitmap Modes](bitmaps.html), [Regular sprites](regobj.html), [Regular Backgrounds](regbg.html), [Affine Sprites](affobj.html), [Affine Backgrounds](affbg.html), [Graphic effects](gfx.html), and [Timers](timers.html) with full or nearly full code of their demos.
- ![upgrade](./img/log/bul_upgr.png) [First Demo](first.html) now has two demos, one purely with hardcode numbers (muwahaha!), and one according to more sound programming principles. Also described these in much more detail.
- ![upgrade](./img/log/bul_upgr.png) Added two demos to [Regular Backgrounds](regbg.html), one of which introduces tonclib and its text functions, which will come back a lot lateron. Speaking of which …
- ![upgrade](./img/log/bul_upgr.png) Recoded `bld_demo`, `m7_demo`, `mos_demo`, `obj_aff`, and `tmr_demo` to use tonclib's text so that it's clearer what you're changing.
- ![upgrade](./img/log/bul_upgr.png) Replaced copiers/fillers with tonclib's `memcpy16/32` and `memset16/32` in most demos after [its introduction](regbg.html#ssec-demo-hello).
- ![upgrade](./img/log/bul_upgr.png) Added [field defines](intro.html#ssec-note-reg) to a lot of register tables.
- ![upgrade](./img/log/bul_upgr.png) Restructed part of [keys.htm](keys.html) for better explanations of the various functions I use.
- ![new](./img/log/bul_new.png) Added a nasty piece on [division by reciprocal multiplication](fixed.html#sec-rmdiv). Not for the squeemish.
- Added a simple template makefile and discussion for the [second demo](first.html#ssec-2nd-make).
- ![new](./img/log/bul_new.png) Added a subsection on [tribool keystates](keys.html#ssec-adv-tri). In fact, nearly all of the demos that might benefit from these have been altered to use them. One line of code instead of four lines, and faster to boot. Seems like a win to me.
- ![new](./img/log/bul_new.png) Added a subsection on the [proper build procedure](bitmaps.html#ssec-data-proc), which was still missing from that whole section. This is pretty much **required reading** for anyone how has been following non-tonc tutorials and adopted their coding standards.
- Merged the fixed-point and LUT chapters, and rewrote most of both.
- jake2431 has been gathering a lot of useful links in this thread: [forum:8353](http://forum.gbadev.org/viewtopic.php?t=8353). If you're new to C and/or GBA/NDS programming, I recommend you check it out.

### Jan 27, 2006 (v1.1)

Heh, so that wasn't not the final update after all <span class="kbd">:P</span>.

- Added a little note to [setup](setup.html) on how to get rid of them useless directories that MSVC 6.0 insists on creating all the time.
- ![fix](./img/log/bul_excl.png) Fixed devkitARM URL and revision. (don't know why I bother with that, though, as there will be a new version the second I post this. Gawddammit, Dave, quit it! <span class="kbd">\>\_\<</span>)
- ![upgrade](./img/log/bul_upgr.png) More code in the text. At least for the earlier pages.
- Two new chapters: one on [Text system fundamentals](text.html) and [producing beeps](sndsqr.html). The latter isn't quite finished yet, but should be enough to get you going. There are 5 new demos that go with these: 4 for text, one for sound.
- ![swap](./img/log/bul_swap.png) More name changes. This time in demo-names only, though, so don't worry there.
- Added/moved a section on [How to deal with data](bitmaps.html#sec-data). This explains some of the nastiness you may or may not encounter. But if you do, it's nice to know why they happen and how to fix it, no?

### Jun 28, 2005 (v1.0)

Final update. Probably. Not because I'm done with this thing, but because there is so much to change and to add that it's easier to start from scratch again. When I started tonc I still knew very little about GBA programming and tried to do the best I could as I went along. Now I'm a little older and wiser (well, older at any rate), know a lot more about proper procedure, what's useful to have and what isn't and also where people can get stuck on (thank you newbie forum dwellers for all your questions!) From the ideas I'm having, tonc 2 will be a _lot_ bigger, better, and have more explosions! Errr, demos. Tonclib will get a major overhaul with new names and new, optimised functions including text for all modes, memory routines and more. But it'll take a while to get there, so I thought I'd update the original one last time.

- ![fix](./img/log/bul_excl.png) Many, many spelling and grammar fixes. Too many in fact. C'mon people, tell me about these things!
- ![fix](./img/log/bul_excl.png) `DMA_SRC_RESET` is `0x01800000`, not `0x00600000`. This is what made the outcome of `dma_demo` so weird. Also fixed `sbb_aff`'s black cross-hairs, which had its _x_ and _y_ values swapped in OAM. Stupid attribute x,y order.
- ![swap](./img/log/bul_swap.png) Name changes. Lots of them. This partially falls under keeping to GBA community standards (`OBJ_ATTR`, charblock, screenblock, swi naming) and other classification issues (`DCNT_x` for `REG_DISPCNT` and such; prefix underscore for bit-defines that are zero, trust me this is a good thing). I've taken the liberty of creating a `legacy.h` that redefines all those old names into the newer ones so that you won't have to do all the renaming yourself if you don't want to. The older names are depreciated, though. This renaming is only part of the full tonc2 renaming, but I can't do functions yet because that _would_ break old code.
- ![upgrade](./img/log/bul_upgr.png) Some small functionality changes. Most notably, `key_poll()` now _already inverts_ `REG_KEYINPUT` (formerly `REG_P1`). This is a good thing, because now the synchronous functions will actually make more sense. Also, `m4_plot()` (formerly `_vid_plot8`) really does plot per pixel, not per two.
- ![upgrade](./img/log/bul_upgr.png) The memory routines `memcpy16/32` and `memset16/32` are optimised in assembly, and probably the fastest you'll come across. Rivals the speed of `CpuFastSet`, but none of the alignment / size requirements.
- ![upgrade](./img/log/bul_upgr.png) `swi.s` has calls for all BIOS routines. Some extras have been relocated to `swi_ex.s`
- Added `x_BUILD` macros for setting bit-flags in clusters. May be useful, maybe not.
- Added rectangle drawers for the bitmap modes. Fairly optimised.
- ![fix](./img/log/bul_excl.png) Fixed list-margins for Firefox. Or rather, fixed list-margins to what the standard requires, but which MSIE doesn't follow. (Now if I can only figure out what to do about that \<col\> tag)
- ![upgrade](./img/log/bul_upgr.png) Restyled the register tables.
- ![upgrade](./img/log/bul_upgr.png) I finally realised how I could do matrices in pure html instead of images so pretty much _all_ equations are now html. I expect it's quite close to MathML, but since MSIE doesn't support it natively and I don't want to worry you with an extra download (which may not even work on older versions), this'll do for now. (Now if you'll excuse me, I going to lie down to get the feeling in my brain back)
- ![upgrade](./img/log/bul_upgr.png) All sections, equations, tables etc now have id's for linking too and (maybe) automatic numbering if I figure out how.
- ![upgrade](./img/log/bul_upgr.png) `int_demo` now uses a separate file for the direct isr and makes proper use of sections and ARM/THUMB code. See the [demo description](interrupts.html#sec-demo) for more.

That's about it I think, but it should be enough. I hve bits and pieces of the tonc2 text, examples and lib, though maybe not in their final forms. They are available, but only on request. If anyone has suggestions or requests I'll see what I can do. This also goes for mistakes (the ones that the compiler/linker can't catch) you've made that you think others might make too. I know a good number of them already from the forum (like that you should <span class="ack">NOT</span> use bytes or halfwords for local variables, since it can really kill performance, `int` or `u32` only, **_please!_**. Pretty please. With sugar on top. And frosting and whipped-cream.) Don't need to know every little thing though, especially if it's already covered by the well-done [gbadev forum FAQ](http://forum.gbadev.org/viewtopic.php?t=418) or already covered in here somewhere.

If anyone knows how I can keep track of all the header/equation/figure numbering automatically (without CSS2, which isn't properly supported by MSIE <kbd>:(</kbd> ) that would be _very_ helpful. Actually, the numbering itself isn't the problem, _referencing_ them is.

Also, I could use more real-life examples of tile-map/sprite collision detection _and_ response. I know the bounding box stuff and the basics of detection (even pixel-perfect), but no matter what I do I seem to be getting stuck on some of the particulars of diagonal movement and when things move at more than one pixel/frame. I'd very much like to see how it's done in real platform games for complex scenes that have multiple sprite-sprite and sprite-background collisions, not just single sprite-bg.

### Dec 5, 2004 (v0.99.6)

Added the [numbers](numbers.html) page about number systems, bits and bit operations. I should warn you that it's rather large. It's been a while since I added something and I think I got a little carried away <kbd>:\\</kbd>. I may break it up into smaller pieces later. Maybe.

DragonBASIC is in the process of being transferred to a new domain, so the old URL is invalid now. At the moment you can still find the forums [here](http://forums.zhilaware.starfusion.orgb/), but the compiler itself is still in limbo for the time being.

### Aug 3, 2004 (v0.99.5)

- ![fix](./img/log/bul_excl.png) Made some minor corrections all round. The first mode7 demo and page now use a different name for the camera position, so it won't clash with **v** from mode7d.
- Added a rudimentary text demo in the form of `txt_demo`.

I think this will be the last update for a while, for a number of reasons. Firstly, I think I have to actually use some of this stuff, to see what's wrong with it. Secondly, I think I may have to put in some more work into a converter and how to add pure binary files to the demos in a friendly way. Thirdly, PERN's back with a vengeance. As such, there seems little point in developing Tonc any further right now, as it seems that the new PERN is going to be very, very complete.

### Jul 16, 2004 (v0.99.5)

- ![fix](./img/log/bul_excl.png) Fixed `aff_rotscale2`, which should _not_ have shrunk the source-angle, but rather a copy of it. Defined `MAPBLOCK` to contain 1024 (=32\*32) tegels, not 512. Was confused with tile-blocks.
- ![upgrade](./img/log/bul_upgr.png) Made a _lot_ of small changes to tiles/map functionality. All map/tile structures are now simple typedefs so you can access their internals via a simple array-access rather than (inline) functions. The inline functions themselves have been removed.
- Changed then `BGINFO` struct a bit, and added some map functions.

I'm sorry if any of these changes causes you any inconvenience, but I think it's better in the long run.

### Jul 11, 2004 (v0.99.4)

- Deprioritized MSVC makefile projects in [setup](setup.html).
- Mopped up several minor and not so minor errors in [mode7ex](mode7ex.html). Well, I did say there'd be some I hadn't discovered yet.
- ![swap](./img/log/bul_swap.png) Renamed the interrupt requests for registers `REG_DISPSTAT` from `X_INT` to `X_IRQ`, which is more proper.
- ![upgrade](./img/log/bul_upgr.png) Modified [swi.htm](swi.html) to show how to use pure assembly for this purpose and added a small section on the aapcs. Also renamed some of the affine structs and functions; you have been warned.
- And yet more typo fixes, where the h311 do they keep coming from? I swear if I find one more "it's"/"its" mixup I'm going to scream. \[Later that day\] Right, that's it: _AAAAAAAARRRRHRHRHRRGGGHHHH!!!_
- ![fix](./img/log/bul_excl.png) Fixed a number of rot-scale equations that had the rotation and scaling ops wrong in the intermediate steps. Oops.
- ![fix](./img/log/bul_excl.png) Fixed a window control macros (forgot some shifts). Should work properly now. Should.
- Added `geom.h|.c` to the library, as I intend to use points and rectangles more often. Also added `ABS`, `SGN` and `SWAP` macros.
- All multiboot demos (i.e., all of them) now have the extension `mb.gba` to indicate them as such.
- Renamed `key_pressed()` to `key_hit()`, which should cause less confusion about what the function actually does (thank's\^H\^Hs for the name Dark Angel (see? The apostrophe occurs almost automatically <span class="kbd">:(</span> ).

I'm working on a nice text system right now. If anyone has any requests I'll see what I can do.

### June 27, 2004 (v0.99.3)

Ahhh, home at last, where I have a proper computer and Kink-FM blasting through my stereo, excccellent! <span class="kbd">=)</span>

- ![upgrade](./img/log/bul_upgr.png) Added `-Map` and `-Wl` command-line options to the [flags list](makefile.html#sec-flags).
- ![swap](./img/log/bul_swap.png) Moved the graphics data that is only used once into the demo-folder where they are used; the gfx directory now only has shared graphics in it.
- ![swap](./img/log/bul_swap.png) Had to write `swi.s` again because the \`utils clean' command destroys all .s files if there is a .c with the same title. Make sure that there is no `swi.c` in your `utils` directory when copying the the new stuff.
- ![upgrade](./img/log/bul_upgr.png) The [mode7ex.htm](mode7ex.html) page is finally complete. Yes I know it's long and full of nasty linear algebra; if you have trouble getting through it and/or have suggestions on making it more readable, plz, do tell.
- ![upgrade](./img/log/bul_upgr.png) The accompanying `mode7d` demo is just about where I wanted it.Sure there are still some minor problems, but it should be enough to get you started.

### June 21, 2004 (v0.99.2)

- ![upgrade](./img/log/bul_upgr.png) I made a lot of changes to `mode7d`; all the real mode 7 code is now in separate files so using it in other projects is easier now. Though mode7ex.htm still needs a lot of work, you can find most of the text in draft-form in [m7theory.zip](../files/m7theory.zip). Yes, it's a Word document; yes, I know that sucks; yes, I will convert it to html when I the text is stable and understandable (please tell me what I need to change in this respect); and yes, I will do this conversion manually, since Word should be allowed to approach HTML to within 500 yards. Perhaps more.
- ![fix](./img/log/bul_excl.png) Made some minor fixes to the [matrix](matrix.html) page. Silly me, I got the cross-product definition all wrong.
- ![upgrade](./img/log/bul_upgr.png) Added info on `REG_P1CNT` to the [keypad](keys.html) page. Yet another thing which only this site covers <span class="kbd">:)</span>.

Devving on a P2-300 with 24MB RAM: VBA runs at 50% (and 23% for mode7d) and minimizing a window takes a few seconds. Man, this sucks.

### June 11, 2004 (v0.99.1)

- ![fix](./img/log/bul_excl.png) Fixed the style sheets so that the background image, colors and borders, etc, etc, appear as I had intented on Mozilla. Sorry about that, didn't know the the wrong comments would screw it up so much. Made a vallidation run and got rid of all nonvalidities ... except one: the \<nobr\> tags that I need to keep certain things together.
- ![swap](./img/log/bul_swap.png) All BIOS calls are now inside `swi.s`, in assembly. Which is where they belongs, really.

### June 3, 2004 (v0.99)

- ![fix](./img/log/bul_excl.png) Found out about the [wrapping artifact](affobj.html#sec-wrap), and changed the sprite pages accordingly. `obj_aff` now allows moving the sprite so you can see this artifact for yourself.
- ![swap](./img/log/bul_swap.png) Finally got over my dislike of near-empty directories (the files get so lonely that way) and put all the demo-code in separate directories. Now, if only I could get over my ifphobia as well...
- Added a section on vsyncing with interrupts in [swi.htm](swi.html#sec-vsync2) and an accompanying demo, `swi_vsync`. You need to see these.
- Added `int_enable_ex` and `int_disable_ex`, which should make working with interrupts easier. However, I am not 100% sure if I got all the registers and flags right.
- ![fix](./img/log/bul_excl.png) C++ doesn't like it when you try to use a struct-copy on a volatile variable, like `bga_update_ex` does. Or did, I should say.
- Learned some new CSS tricks and am busy updating and structuring the layout of _all_ pages. It's mostly subtle stuff though, like standardizing the equation layout and giving code and register listings a subtle border that makes it stand out in printing. Non-subtle is that ever image should have a caption now.
- ![upgrade](./img/log/bul_upgr.png) Resumed work on [mode7ex.htm](mode7ex.html) and its accompanying demo, `mode7d`. Adding variable pitch turned out to be easier than I thought, w00t! It's still a little buggy, though.

With all these changes, it is adviced to save or remove older Tonc stuff when upgrading to avoid double files and other inconsistencies.

### May 24, 2004 (v0.98.5)

- ![upgrade](./img/log/bul_upgr.png) devkitARM is now the primary devkit for Tonc. Makefiles and text are updated to match the change.
- ![upgrade](./img/log/bul_upgr.png) Using a separate interrupt file now instead of a custom crt0.S and got The Point® of the critter in the process. The text is modified to reflect newer insights, as is `int_demo.c`
- Started work on a [glossary](glossary.html).
- Added instructions on how to run makefiles without Visual C++ in the the Tonc-code readme. Silly that I never thought of that before.
- ![fix](./img/log/bul_excl.png) `REG_IF` is at `0400:0202`, not `0400:0200`, doh!
- As you can see, I'm trying to use context-specific bullets for log entries. I still need to figure out what images to use for what purpose, though.
- Rewritten the `build_all` and `clean_all` targets in `tonc.mak`.They're quite nasty now, but act more correctly and allow me to switch to a "one demo, one dir" structure if people finds having everything in the `examples` folder a bit messy.

I am soooo tired right now so I wouldn't be surprised if I messed up somewhere. I'll get it fixed when I've had a chance to sssslssszzzzzzz....

### May 16, 2004 (v0.98)

- ![fix](./img/log/bul_excl.png) Lot's of changes. First of all, I finally have a means to test on hardware, Wheeeee!! However, it did point out that you can't use the object tileblocks for backgrounds after all `:(`. Added my early experiences with hardware tests on a number of the pages.
- ![fix](./img/log/bul_excl.png) Including in the [windowing](gfx.html#sec-win) section. It seems that you need to be really careful with the vertical settings of windowing. Updated the windowing demo to not use u16 arithmetic for the window size (which is given in bytes), and more precise movement.
- ![swap](./img/log/bul_swap.png) Threw the DMA code around. I'm now using `dma_memcpy()` for general copies, and renamed the old `DMA_CPY()` macro to `DMA_TRANSFER`, and rearranged the order of arguments to match `memcpy`. Makes more sense that way.
- ![swap](./img/log/bul_swap.png) Also changed `oi_set` to `oi_set_attr` and `oi_pos` to `oi_set_pos`.
- The `Tonc Utils` configuration now compiles the utility code into a library. Required for `mode7d`.
- Created a `build_all` rule in `tonc.mak`. Rebuilding everything by hand was really getting on my nerves.
- More random clean-ups. The images on the entrance page are now links as well. Important notes are now in red boxes, for extra visibility. Added the demo-code of `bm_mode.c`, to show the basic steps of loading a picture and using keys. I should still post full code that earlier in the tutorials. Added an example of a fixed point identity matrix on [affine.htm](affine.html#sec-finish) to make sure people don't try to use floats.
- ![fix](./img/log/bul_excl.png) Fixed [swi.htm](swi.html). _Again!_ I swear, if I find one more error here some somebody is gonna get hurt. And it won't be me. This time the range of arctan2 was wrong (should be full circle). What makes this error even worse is that I should (and did) know it's supposed to be the full-circle all along; it is the raison d'être of arctan2 after all.
- [Matrix page](matrix.html) is done.
- Practically fell out of my chair laughing at [villainsupply.com](http://www.villainsupply.com). Ouch.
- Nearly drowned in my own drool after watching the Nintendo stuff at E3. Gargle.
- The picture used in `key_demo` had the palette-indices of `KEY_START` and `KEY_SELECT` switched. I never really noticed because emulators don't have real start and select buttons. So once again, hardware testing saves the day.

### Apr 29, 2004 (v0.97)

- Added links to devkitARM as well as instructions on how to get it working. There is a very real possibility that I'll switch to this toolchain in the future.
- Converted most of the macros to inline functions. Safer, easier to read and just as fast. Yes, plz.
- Some more diagrams about tile-counting and the affine transformations.
- Still to do: finishing the matrix page (and perhaps the mode7ex page). And now that I have my [tile-map editor Mirach](http://www.coranac.com/projects/#mirach), I may be able to do something with that as well. And I really, really need to get working on a text-system.

### Apr 9, 2004 (v0.97)

The object affine functions have a background counterpart now, and `mode7d` is coming along nicely.

### Apr 4, 2004 (v0.96)

Renamed OAM structs and related items. _Again_. When is this gonna be final?!? Also, thanks to Lupin's problems with sprite-placement in 3D I finally got my matrix-transform sense back. Now that I get it again, I hope to expand the mode7 section in the near future. I already got a working example for 3d-sprite placement already in the form of `mode7d`.

### Mar 31, 2004 (v0.96)

Working on a vector/matrix page, some reshuffling of page-order and yet more random little cleanups.

### Mar 24, 2004 (v0.96)

Replaced the assembly listing in [swi.htm](swi_htm) with the proper THUMB listing. I'd forgotten I wasn't using ARM code anymore.

### Mar 20, 2004 (v0.96)

And just when you think you're finished you find another 2 things you can improve upon. Argh. Anyway, I've changed the way sine and cosine are retrieved. They're both macros now, using one 512-entry long `s16` sine-LUT. Also, I finally realized how to XOR the `vid_page` directly for page-flipping. And, oh yeah, the compiler flag for compile, but not assemble should be `-S`, not `-s`. Oops.  
I think I finally know how I can modify my affine functions to apply to backgrounds without having to use the `OBJ_AFFINE` structure, but it may be a while before I actually do that.

### Mar 17, 2004 (v0.95)

Added ArcTan2 function to `swi_demo` and fixed the errors that `swi.htm` still contained. Argh, and I thought I'd been thorough in weeding out all inconsistencies after the recent name and code modifications.

### Mar 14, 2004 (v0.95)

First entry in the log. I've rewritten the parts about sprites and backgrounds, changed glyphs to tiles and tiles to tegels (hope I got them all `:]`), updated all the code one last time and written sections on how to set up DKA, MSVC and makefiles. I think Tonc's ready for use now, wheee!
