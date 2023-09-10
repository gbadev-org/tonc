Title: Regular tiled backgrounds
Date: 2003-09-01
Modified: 2023-09-09
Authors: Cearn

# 9. Regular tiled backgrounds {#ch-}

[TOC]

## Tilemap introduction {#sec-intro}

Tilemaps are the bread and butter for the GBA. Almost every commercial GBA game makes use of tile modes, with the bitmap modes seen only in 3D-like games that use ray-tracing. Everything else uses tiled graphics.

The reason why tilemaps are so popular is that they're implemented in hardware and require less space than bitmap graphics. Consider {@fig:map}a. This is a 512 by 256 image, which even at 8bpp would take up 128 KiB of VRAM, and we simply don't have that. If you were to make one big bitmap of a normal level in a game, you can easily get up to 1000×1000 pixels, which is just not practical. And *then* there's the matter of scrolling through the level, which means updating all pixels each frame. Even when your scrolling code is fully optimized that'd take quite a bit of time.

Now, notice that there are many repeated elements in this image. The bitmap seems to be divided into groups of 16×16 pixels. These are the <dfn>tiles</dfn>. The list of unique tiles is the <dfn>tileset</dfn>, which is given in {@fig:map}b. As you can see, there are only 16 unique tiles making up the image. To create the image from these tiles, we need a <dfn>tilemap</dfn>. The image is divided into a matrix of tiles. Each element in the matrix has a <dfn>tile index</dfn> which indicates which tile should be rendered there; the tilemap can be seen in {@fig:map}c.

Suppose both the tileset and map used 8-bit entries, the sizes are 16×(16×16) = 4096 bytes for the tileset and 32×16 = 512 bytes for the tilemap. So that's 4.5 KiB for the whole scene rather than the 128 KiB we had before; a size reduction of a factor of 28.

<div class="cblock">
<table width=70% id="fig:map">
<tbody valign="top">
<tr>
<td colspan=2 align="center">
  <div class="cpt" style="width:512px">
  <img src="img/bgs/brin3-full.png" alt="Brinstar map">
  <b>{*@fig:map}a</b>: image on screen.
  </div>
<tr>
<td colspan=2>
  The tile mapping process. Using the tileset of 
  {@fig:map}b, and the tile map of 
  {@fig:map}c, the end-result is 
  {@fig:map}a. 
<tr>
<td>
  <div class="cpt" style="width:48px">
  <img src="img/bgs/brin3-meta-2x.png" height=264
    alt="(meta)tileset for the map"><br>
  <b>{*@fig:map}b</b>: the tile set.
  </div>		
<td>
  <div class="cpt" style="width:528px">
  <img src="img/bgs/brin3-map-2x.png" width=528
	alt="Superimposed tile-map"><br>
  <b>{*@fig:map}c</b>: the tile map (with the proper 
    tiles as a backdrop).
  </div>
</tbody>
</table></div>

That's basically how tilemaps work. You don't define the whole image, but group pixels together into tiles and describe the image in terms of those groups. In the {@fig:map}, the tiles were 16×16 pixels, so the tilemap is 256 times smaller than the bitmap. The unique tiles are in the tileset, which can (and usually will) be larger than the tilemap. The size of the tileset can vary: if the bitmap is highly variable, you'll probably have many unique tiles; if the graphics are nicely aligned to tile boundaries already (as it is here), the tileset will be small. This is why tile-engines often have a distinct look to them.

### Tilemaps for the GBA {#ssec-intro-gba}

In the tiled video-modes (0, 1 and 2) you can have up to four backgrounds that display tilemaps. The size of the maps is set by the control registers and can be between 128×128 and 1024×1024 pixels. The size of each tile is always 8×8 pixels, so {@fig:map} isn't *quite* the way it'd work on the GBA. Because accessing the tilemaps is done in units of tiles, the map sizes correspond to 16×16 to 128×128 tiles.

Both the tiles and tilemaps are stored in VRAM, which is divided into <dfn>charblocks</dfn> and <dfn>screenblocks</dfn>. The tileset is stored in the charblocks and the tilemap goes into the screenblocks. In the common vernacular, the word “tile” is used for both the graphical tiles and the entries of the tilemaps. Because this is somewhat confusing, I'll use the term <dfn>screen entry</dfn> (<dfn>SE</dfn> for short) as the items in the screenblocks (i.e., the map entries) and restrict tiles to the tileset.

64 KiB of VRAM is set aside for tilemaps (`0600:0000h`-`0600:FFFFh`). This is used for both screenblocks *and* charblocks. You can choose which ones to use freely through the control registers, but be careful that they can overlap (see {@tbl:cbb-sbb}). Each screenblock is 2048 (`800h`) bytes long, giving 32 screenblocks in total. All but the smallest backgrounds use multiple screenblocks for the full tilemap. Each charblock is 16 KiB (`4000h` bytes) long, giving four blocks overall.

<div class="cblock">
<table id="tbl:cbb-sbb"
  border=1 cellpadding=3 cellspacing=0 rules=groups>
<caption align="bottom">
  <b>{*@tbl:cbb-sbb}</b>:
  charblock and screenblock overlap.
</caption>
<colgroup span=1 style="background-color:#D0D0D0;"></colgroup>
<colgroup span=3 style="background-color:#B0B0B0;"></colgroup>
<colgroup span=3 style="background-color:#D0D0D0;"></colgroup>
<colgroup span=3 style="background-color:#B0B0B0;"></colgroup>
<colgroup span=3 style="background-color:#D0D0D0;"></colgroup>

<tbody align="left"><tr>
  <th>Memory
  <th colspan=3> 0600:0000 <th colspan=3> 0600:4000
  <th colspan=3> 0600:8000 <th colspan=3> 0600:C000
</tbody>
<tbody align="center"><tr>
  <th>charblock
  <td colspan=3> 0 <td colspan=3> 1 <td colspan=3> 2 <td colspan=3> 3 
</tbody>
<tbody><tr>
  <th>screenblock
  <td>0 <td>&hellip; <td>7		<td>8 <td>&hellip; <td>15
  <td>16 <td>&hellip; <td> 23	<td>24 <td>&hellip; <td>31
</tbody>
</table>
</div>

<div class="note" markdown>
<div class="nhcare">
Tiles vs ‘tiles’
</div>

Both the entries of the tilemap and the data in the tileset are often referred to as ‘tiles’, which can make conversation confusing. I reserve the term ‘tile’ for the graphics, and ‘screen(block) entry’ or ‘map entry’ for the map's contents.
</div>

<div class="note" markdown>
<div class="nhcare">
Charblocks vs screenblocks
</div>

Charblocks and screenblocks use the same addresses in memory. Each charblock overlaps eight screenblocks. When loading data, make sure the tiles themselves don't overwrite the map, or vice versa.
</div>

Size was one of the benefits of using tilemaps, speed was another. The rendering of tilemaps in done in hardware and if you've ever played PC games in hardware and software modes, you'll know that hardware is good. Another nice point is that scrolling is done in hardware too. Instead of redrawing the whole scene, you just have to enter some coordinates in the right registers.

As I said in the overview, there are three stages to setting up a tiled background: control, mapping and image-data. I've already covered most of the image-data in the [overview](objbg.html), as well as some of the control and mapping parts that are shared by sprites and backgrounds alike; this chapter covers only things specific to backgrounds in general and regular backgrounds in particular. I'm assuming you've read the overview.

<div class="note" markdown>
<div class="nhgood">
Essential tilemap steps
</div>

-   Load the graphics: tiles into charblocks and colors in the background palette.
-   Load a map into one or more screenblocks.
-   Switch to the right mode in `REG_DISPCNT` and activate a background.
-   Initialize that background's control register to use the right CBB, SBB and bitdepth.
</div>

## Background control {#sec-ctrl}

### Background types {#ssec-ctrl-bgs}

Just like sprites, there are two types of tiled backgrounds: regular and affine; these are also known as text and rotation backgrounds, respectively. The type of the background depends of the video mode (see {@tbl:bg-types}). At their cores, both regular and affine backgrounds work the same way: you have tiles, a tile-map and a few control registers. But that's where the similarity ends. Affine backgrounds use more and different registers than regular ones, and even the maps are formatted differently. This page only covers the regular backgrounds. I'll leave the [affine ones](affbg.html) till after the page on the [affine matrix](affine.html).

<div class="lblock">
<table id="tbl:bg-types"
  border=1 cellpadding=2 cellspacing=0>
<caption align="bottom">
  <b>{*@tbl:bg-types}</b>: video modes and 
  background type
</caption>
<tbody align="center">
<tr>
  <th>mode	<th>BG0	<th>BG1	<th>BG2	<th>BG3
<tr>
  <td>0     <td>reg	<td>reg	<td>reg	<td>reg
<tr>
  <td>1     <td>reg	<td>reg	<td>aff	<td> -
<tr>
  <td>2     <td>-	<td>-	<td>aff	<td>aff
</tbody>
</table>
</div>

### Control registers {#ssec-ctrl-regs}

All backgrounds have 3 primary control registers. The primary control register is `REG_BGxCNT`, where *x* indicates the backgrounds 0 through 3. This register is where you say what the size of the tilemap is, and which charblock and screenblock it uses. The other two are the scrolling registers, `REG_BGxHOFS` and `REG_BGxVOFS`.

Each of these is a 16-bit register. `REG_BG0CNT` can be found at `0400:0008`, with the other controls right behind it. The offsets are paired by background, forming coordinate pairs. These start at `0400:0010`

<div class="lblock">
<table id="tbl:ctrl-ofs"
  border=1 cellpadding=2 cellspacing=0>
<caption align= bottom>
  <b>{*@tbl:ctrl-ofs}</b>: Background register 
    addresses
</caption>
<col span=2 align="right">
  <tr><th>Register      <th>length  <th>address
  <tr><th>REG_BGxCNT    <td>2       <td>0400:0008h + 2·<i>x</i>
  <tr><th>REG_BGxHOFS   <td>2       <td>0400:0010h + 4·<i>x</i>
  <tr><th>REG_BGxVOFS   <td>2       <td>0400:0012h + 4·<i>x</i>
</table>
</div>

The description of `REG_BGxCNT` can be found below. Most of it is pretty standard, except for the size: there are actually *two* lists of possible sizes; one for regular maps and one for affine maps. The both use the same bits you may have to be careful that you're using the right `#define`s.

<div class="reg">
<table class="reg" id="tbl-reg-bgxcnt"
  border=1 frame=void cellpadding=4 cellspacing=0>
<caption class="reg">
  REG_BGxCNT @ <code>0400:0008</code> + 2<i>x</i>
</caption>
<tr class="bits">
	<td>F E<td>D<td> C B A 9 8
	<td>7<td>6<td>5 4<td>3 2<td>1 0
<tr class="bf">
	<td class="rclr2">Sz
	<td class="rclr6">Wr
	<td class="rclr1">SBB
	<td class="rclr3">CM
	<td class="rclr5">Mos
	<td>-
	<td class="rclr0">CBB
	<td class="rclr4">Pr
</table>

<table>
  <col class="bits" width=40>
  <col class="bf" width="8%">
  <col class="def" width="12%">
<tr align="left"><th>bits<th>name<th>define<th>description
<tbody valign="top">
<tr class="bg0">	
  <td>0-1<td class="rclr4">Pr
  <td><i>BG_PRIO#</i>
  <td><b>Priority</b>. Determines drawing order of backgrounds.
<tr class="bg1">	
  <td>2-3<td class="rclr0">CBB
  <td><i>BG_CBB#</i>
  <td><b>Character Base Block</b>. Sets the charblock that serves as 
    the base for character/tile indexing. Values: 0-3.
<tr class="bg0">	
  <td> 6 <td class="rclr5">Mos
  <td>BG_MOSAIC
  <td><b>Mosaic</b> flag. Enables mosaic effect.
<tr class="bg1">	
  <td> 7 <td class="rclr3">CM
  <td>BG_4BPP, BG_8BPP
  <td><b>Color Mode</b>. 16 colors (4bpp) if cleared; 
    256 colors (8bpp) if set. 
<tr class="bg0">	
  <td>8-C<td class="rclr1">SBB
  <td><i>BG_SBB#</i>
  <td><b>Screen Base Block</b>. Sets the screenblock that serves as 
    the base for screen-entry/map indexing. Values: 0-31.
<tr class="bg1">	
  <td> D <td class="rclr6">Wr
  <td>BG_WRAP
  <td><b>Affine Wrapping</b> flag. If set, affine background wrap 
    around at their edges. Has no effect on regular backgrounds as 
    they wrap around by default.
<tr class="bg0">	
  <td>E-F<td class="rclr2">Sz
  <td><i>BG_SIZE#</i>, <i class="mini">see below</i>
  <td><b>Background Size</b>. Regular and affine backgrounds have 
      different sizes available to them. The sizes, in tiles and in 
      pixels, can be found in {@tbl:bg-size}.
</tbody>
</table>
</div>

<div class="cblock">
<table width="100%" id="tbl:bg-size">
<tr align="center">
<td>
  <table id="tbl-reg-size" border=1 cellpadding=2  cellspacing=0>
  <caption align="bottom">
    <b>{*@tbl:bg-size}a</b>: regular bg sizes
  </caption>
  <col><col class="def">
  <tbody align="center">
    <tr><th>Sz-flag	<th>define    <th>(tiles)<th>(pixels)
    <tr><td> 00   <td><code>BG_REG_32x32</code> <td> 32×32 <td> 256×256 
    <tr><td> 01   <td><code>BG_REG_64x32</code> <td> 64×32 <td> 512×256 
    <tr><td> 10   <td><code>BG_REG_32x64</code> <td> 32×64 <td> 256×512 
    <tr><td> 11   <td><code>BG_REG_64x64</code> <td> 64×64 <td> 512×512 
  </tbody>
  </table>
<td>
  <table id="tbl-aff-size" border=1 cellpadding=2 cellspacing=0>
  <caption align="bottom">
    <b>{*@tbl:bg-size}b</b>: affine bg sizes
  </caption>
  <col><col class="def">
  <tbody align="center">
    <tr><th>Sz-flag	<th>define    <th>(tiles) <th>(pixels)
    <tr><td> 00   <td><code>BG_AFF_16x16</code>  <td> 16×16  <td> 128×128 
    <tr><td> 01   <td><code>BG_AFF_32x32</code>  <td> 32×32  <td> 256×256 
    <tr><td> 10   <td><code>BG_AFF_64x64</code>  <td> 64×64  <td> 512×512 
    <tr><td> 11   <td><code>BG_AFF_128x128</code><td>128×128 <td>1024×1024
  </tbody>
  </table>
</table>
</div><br>

Each background has two 16-bit scrolling registers to offset the rendering (`REG_BGxHOFS` and `REG_BGxVOFS`). There are a number of interesting points about these. First, because regular backgrounds wrap around, the values are essentially modulo *mapsize*. This is not really relevant at the moment, but you can use this to your benefit once you get to more advanced tilemaps. Second, these registers are **write-only**! This is a little annoying, as it means that you can't update the position by simply doing `REG_BG0HOFS++` and the like.

And now the third part, which may be the most important, namely what the values actually *do*. The simplest way of looking at them is that they give the coordinates of the screen on the map. Read that again, carefully: it's the position of the screen on the map. It is *not* the position of the map on the screen, which is how sprites work. The difference is only a minus sign, but even something as small as a sign change can wreak havoc on your calculations.

<div class="lblock">
  <div class="cpt" style="width:520px;">
    <img src="img/bgs/brin3-ofs-2x.png" id="fig:map-ofs" width=520
      alt="map-ofs-a"><br>
    <b>{*@fig:map-ofs}</b>: 
	Scrolling offset <b>dx</b> sets is the position of the screen 
	on the map. In this case, <b>dx</b> = (192, 64).
  </div>
</div>

So, if you increase the scrolling values, you move the screen to the right, which corresponds to the map moving *left* on the screen. In mathematical terms, if you have map position **p** and screen position **q**, then the following is true:

<table id="eq-bgr-dx">
<tr>
  <td class="eqnrcell">(9.1)
  <td class="eqcell">
  <table class="eqtbl" cellpadding=2 cellspacing=0>
  <col align="right">
  <col align="center">
  <col align="left">
  <tr>
    <td><b>q + dx</b>
	<td>=
	<td><b>p</b>
  <tr>
    <td><b>q</b>
	<td>= 
	<td><b>p &minus; dx</b>
  </table>
</table>

<div class="note" markdown>
<div class="nhcare">
Direction of offset registers
</div>

The offset registers REG_BGxHOFS and REG_BGxVOFS indicate which map location is mapped to the top-left of the screen, meaning positive offsets scroll the map left and up. Watch your minus signs.
</div>

<div class="note" markdown>
<div class="nhcare">
Offset registers are write only
</div>

The offset registers are **write-only**! That means that direct arithmetic like `+=` will not work.
</div>

### Useful types and #defines {#ssec-ctrl-types}

Tonc's code has several useful extra types and macros that can make life a little easier.

```c
// === Additional types (tonc_types.h) ================================

//! Screen entry conceptual typedef
typedef u16 SCR_ENTRY;

//! Affine parameter struct for backgrounds, covered later
typedef struct BG_AFFINE
{
    s16 pa, pb;
    s16 pc, pd;
    s32 dx, dy;
} ALIGN4 BG_AFFINE;

//! Regular map offsets
typedef struct BG_POINT
{
    s16 x, y;
} ALIGN4 BG_POINT;

//! Screenblock struct
typedef SCR_ENTRY   SCREENBLOCK[1024];


// === Memory map #defines (tonc_memmap.h) ============================

//! Screen-entry mapping: se_mem[y][x] is SBB y, entry x
#define se_mem          ((SCREENBLOCK*)MEM_VRAM)

//! BG control register array: REG_BGCNT[x] is REG_BGxCNT
#define REG_BGCNT      ((vu16*)(REG_BASE+0x0008))

//! BG offset array: REG_BG_OFS[n].x/.y is REG_BGnHOFS / REG_BGnVOFS
#define REG_BG_OFS      ((BG_POINT*)(REG_BASE+0x0010))

//! BG affine params array
#define REG_BG_AFFINE   ((BG_AFFINE*)(REG_BASE+0x0000))
```

Strictly speaking, making a `SCREEN_ENTRY` `typedef` is not necessary, but makes its use clearer. `se_mem` works much like `tile_mem`: it maps out VRAM into screenblocks screen-entries, making finding a specific entry easier. The other typedefs are used to map out arrays for the background registers. For example, `REG_BGCNT` is an array that maps out all `REG_BGxCNT` registers. `REG_BGCNT[0]` is `REG_BG0CNT`, etc. The `BG_POINT` and `BG_AFFINE` types are used in similar fashions. Note that `REG_BG_OFS` still covers the same registers as `REG_BGxHOFS` and `REG_BGxVOFS` do, and the write-only-ness of them has not magically disappeared. The same goes for `REG_BG_AFFINE`, but that discussion will be saved for another time.

In theory, it is also useful create a sort of background API, with a struct with the temporaries for map positioning and functions for initializing and updating the registers and maps. However, most of tonc's demos are not complex enough to warrant these things. With the types above, manipulating the necessary items is already simplified enough for now.

## Regular background tile-maps {#sec-map}

The screenblocks form a matrix of screen entries that describe the full image on the screen. In the example of {@fig:map}, the tilemap entries just contained the tile index. The GBA screen entries bahave a little differently.

For regular tilemaps, each screen entry is 16-bits long. Besides the tile index, it contains flipping flags and a palette bank index for 4bpp / 16-color tiles. The exact layout can be found in "Screen entry format" below. The affine screen entries are only 8 bits wide and just contain an 8-bit tile index.

<div class="reg">
<table class="reg" id="tbl-se"
  border=1 frame=void cellpadding=4 cellspacing=0>
<caption class="reg">
  Screen entry format for regular backgrounds
</caption>
<tr class="bits">
	<td>F E D C<td>B<td>A<td>9 8 7 6 5 4 3 2 1 0
<tr class="bf">
	<td class="rclr1">PB
	<td class="rclr2">VF
	<td class="rclr2">HF
	<td class="rclr0">TID
</table>

<table>
  <col class="bits" width=40>
  <col class="bf" width="8%">
  <col class="def" width=12%>
<tr align="left"><th>bits<th>name<th>define<th>description
<tbody valign="top">
<tr class="bg0">	
  <td>0-9<td class="rclr0">TID
  <td><i>SE_ID#</i>
  <td><b>Tile-index</b> of the SE.
<tr class="bg1">	
  <td>A-B<td class="rclr2">HF, VF
  <td>SE_HFLIP, SE_VFLIP. <i>SE_FLIP#</i>
  <td><b>Horizontal/vertical flipping</b> flags. 
<tr class="bg0">	
  <td>C-F<td class="rclr1">PB
  <td><i>SE_PALBANK#</i>
  <td><b>Palette bank</b> to use when in 16-color mode. Has no effect 
    for 256-color bgs (<code>REG_BGxCNT{6}</code> is set).
</tbody>
</table>
</div>

### Map layout {#ssec-map-layout}

VRAM contains 32 screenblocks to store the tilemaps in. Each screenblock is 800h bytes long, so you can fit 32×32 screen entries into it, which equals one 256×256 pixel map. The bigger maps simply use more than one screenblock. The screenblock index set in `REG_BGxCNT` is the <dfn>screen base block</dfn> which indicates the start of the tilemap.

Now, suppose you have a tilemap that's *tw*×*th* tiles/SEs in size. You might expect that the screen entry at tile-coordinates (*tx*, *ty*) could be found at SE-number *n* = *tx*+*ty*·*tw*, because that's how matrices always work, right? Well, you'd be wrong. At least, you'd be *partially* wrong.

Within each screenblock the equation works, but the bigger backgrounds don't simply *use* multiple screenblocks, they're actually accessed as four separate maps. How this works can be seen in {@tbl:reg-layout}: each numbered block is a contingent block in memory. This means that to get the SE-index you have to find out which screenblock you are in and then find the SE-number inside that screenblock.

<div class="lblock">
<table class="reg" id="tbl:reg-layout"
  border=1 frame=void cellpadding=4 cellspacing=0>
<caption align="bottom">
  <b>{*@tbl:reg-layout}</b>: screenblock layout of 
  regular backgrounds.
 </caption>
<col span=4 align="center">
<tr><th>32×32<th>64×32<th>32×64<th>64×64
<tr>
<td>
  <table border=frame cellpadding= 8 cellspacing=0>
    <tr><td bgcolor=red><b>0</b>
  </table>
<td>
  <table border=frame cellpadding= 8 cellspacing=0>
    <tr><td bgcolor=red><b>0</b><td bgcolor= green><b>1</b>
  </table>
<td>
  <table border=frame cellpadding= 8 cellspacing=0>
    <tr><td bgcolor=red><b>0</b>
    <tr><td bgcolor=blue><b>1</b>
  </table>
<td>
  <table border=frame cellpadding= 8 cellspacing=0>
    <tr><td bgcolor=red><b>0</b><td bgcolor= green><b>1</b>
    <tr><td bgcolor=blue><b>2</b><td bgcolor= gray><b>3</b>
  </table>
</table>
</div>

This kind of nesting problem isn't as hard as it looks. We know how many tiles fit in a screenblock, so to get the SBB-coordinates, all we have to do divide the tile-coords by the SBB width and height: *sbx*=*tx*/32 and *sby*=*ty*/32. The SBB-number can then be found with the standard matrix→array formula. To find the in-SBB SE-number, we have to use *tx*%32 and *ty*%32 to find the in-SBB coordinates, and then again the conversion from 2D coords to a single element. This is to be offset by the SBB-number tiles the size of an SBB to find the final number. The final form would be:

<div id="cd-se-index" markdown>
```c
//! Get the screen entry index for a tile-coord pair
//  And yes, the div and mods will be converted by the compiler
uint se_index(uint tx, uint ty, uint pitch)
{
    uint sbb= (ty/32)*(pitch/32) + (tx/32);
    return sbb*1024 + (ty%32)*32 + tx%32;
}
```
</div>

The general formula is left as an exercise for the reader – one that is well worth the effort, in my view. This kind of process crops up in a number of places, like getting the offset for bitmap coordinates in tiles, and tile coords in 1D object mapping.

If all those operations make you queasy, there's also a faster version specifically for a 2×2 arrangement. It starts with calculating the number as if it's a 32×32t map. This will be incorrect for a 64t wide map, which we can correct for by adding 0x0400−0x20 (i.e., tiles/block − tiles per row). We need another full block correction is the size is 64×64t.

<div id="cd-se-index-fast" markdown>
```
//! Get the screen entry index for a tile-coord pair.
/*! This is the fast (and possibly unsafe) way.
*   \param bgcnt    Control flags for this background (to find its size)
*/

uint se_index_fast(uint tx, uint ty, u16 bgcnt)
{
    uint n= tx + ty*32;
    if(tx >= 32)
        n += 0x03E0;
    if(ty >= 32 && (bgcnt&BG_REG_64x64)==BG_REG_64x64)
        n += 0x0400;
    return n;
}
```
</div>

I would like to remind you that *n* here is the SE-number, not the address. Since the size of a regular SE is 2 bytes, you need to multiply *n* by 2 for the address. (Unless, of course, you have a pointer/array of `u16`s, in which case *n* will work fine.) Also, this works for regular backgrounds only; affine backgrounds use a linear map structure, which makes this extra work unnecessary there. By the way, both the screen-entry and map layouts are different for affine backgrounds. For their formats, see the [map format](affbg.html#sec-map) section of the affine background page.

### Background tile subtleties {#ssec-map-subtle}

There are two additional things you need to be aware of when using tiles for tile-maps. The first concerns tile-numbering. For sprites, numbering went according to 4-bit tiles (s-tiles); for 8-bit tiles (d-tiles) you'd have use multiples of 2 (a bit like u16 addresses are always multiples of 2 in memory). In tile-maps, however, d-tiles are numbered by the d-tile. To put it in other words, for sprites, using index *id* indicates the same tile for both 4 and 8-bit tiles, namely the one that starts at *id*·20h. For tile-maps, however, it starts at *id*·20h for 4-bit tiles, but at *id*·40h for 8-bit tiles.

<div class="lblock">
<table id="tbl:bg-tids"
  border=1 cellpadding=2 cellspacing=0>
<caption align="bottom">
  {*@tbl:bg-tids}: tile counting 
  for backgrounds, sticks to its bit-depth.
</caption>
<tbody align="center">
<tr>
  <th>memory offset<th>000h<th>020h <th>040h<th>060h <th>080h<th>100h <th>...
<tr>
  <th>4bpp tile <td>0      <td>1  <td>2    <td>3  <td>4    <td>5 <td>...
<tr>
  <th>8bpp tile <td colspan=2>0   <td colspan=2>1 <td colspan=2>2<td>...
</tbody>
</table>
</div>

The second concerns, well, also tile-numbering, but more how many tiles you can use. Each map entry for regular backgrounds has 10 bits for a tile index, so you can use up to 1024 tiles. However, a quick calculation shows that a charblock contains 4000h/20h= 512 s-tiles, or 4000h/40h= 256 d-tiles. So what's the deal here? Well, the charblock index you set in `REG_BGxCNT` is actually only the block where tile-counting starts: its <dfn>character base block</dfn>. You can use the ones after it as well. Cool, huh? But wait, if you can access subsequent charblocks as well; does this mean that, if you set the base charblock to 3, you can use the sprite blocks (which are basically blocks 4 and 5) as well?

The answer is: yes. And <span class="ack">NO</span>!

Emulators from the early 2000s allow you to do this. However, a real GBA doesn't. It does output *something*, though: the screen-entry will be used as tile-data itself, but in a manner that simply defies explanation. Trust me on this one, okay? Of the current tonc demos, this is one of the times that VBA gets it wrong.

<div class="note" markdown>
<div class="nh">
Available tiles
</div>

For both 4bpp and 8bpp regular bgs, you can access 1024 tiles. The only caveat here is that you cannot access the tiles in the object charblocks even if the index would call for it.
</div>

Another thing you may be wondering is if you can use a particular screenblock that is within a currently used charblock. For example, is it allowed to have a background use charblock 0 and screenblock 1. Again, yes you can do this. This can be useful since you're not likely to fill an entire charblock, so using its later screenblocks for your map data is a good idea. (A sign of True Hackerdom would be if you manage to use the same data for both tiles and SEs and still get a meaningful image (this last part is important). If you have done this, please let me know.)

<div class="note" markdown>
<div class="nh">
Tilemap data conversion via CLI
</div>

A converter that can tile images (for objects), can also create a tileset for tilemaps, although there will likely be many redundant tiles. A few converters can also reduce the tileset to only the unique tiles, and provide the tilemap that goes with it. The Brinstar bitmap from {@fig:map} is a 512×256 image, which could be tiled to a 64×32 map with a 4bpp tileset reduced for uniqueness in tiles, including palette info and mirroring.

```sh
# gfx2gba
# (C array; u8 foo_Tiles[], u16 foo_Map[], 
# u16 master_Palette[]; foo.raw.c, foo.map.c, master.pal.c)
    gfx2gba -fsrc -c16 -t8 -m foo.bmp
```

```sh
# grit
# (C array; u32 fooTiles[], u16 fooMap[], u16 fooPal[]; foo.c, foo.h)
    grit foo.bmp -gB4 -mRtpf
```

Two notes on gfx2gba: First, it merges the palette to a single 16-color array, rearranging it in the process. Second, while it lists metamapping options in the readme, it actually doesn't give a metamap and meta-tileset, it just formats the map into different blocks.
</div>

## Tilemap demos {#sec-demo}

There are four demos in this chapter. The first one is *brin_demo*, which is very, very short and shows the basic steps of tile loading and scrolling. The next ones are called *sbb_reg* and *cbb_demo*, which are tech demos, illustrating the layout of multiple screenblocks and how tile indexing is done on 4bpp and 8bpp backgrounds. In both these cases, the map data is created manually because it's more convenient to do so here, but using map-data created by map editors really isn't that different.

### Essential tilemap steps: brin_demo {#ssec-demo-brin}

As I've been using a 512×256 part of Brinstar throughout this chapter, I thought I might as well use it for a demo.

There are a few map editors out there that you can use. Two good ones are Nessie's [MapEd](https://nessie.gbadev.org){target="_blank"} or [Mappy](https://www.tilemap.co.uk/mappy.php){target="_blank"}, both of which have a number of interesting features. I have my own map editor, [mirach](https://www.coranac.com/projects/#mirach){target="_blank"}, but it's just a very basic thing. Some tutorials may point you to GBAMapEditor. Do *not* use this editor as it's pretty buggy, leaving out half of the tilemaps sometimes. Tilemaps can be troublesome enough for beginners without having to worry about whether the map data is faulty.

In this cause, however, I haven't used any editor at all. Some of the graphics converters can convert to a tileset+tilemap – it's not the standard method, but for small maps it may well be easier. In this case I've used Usenti to do it, but grit and gfx2gba work just as well. Note that because the map here is 64×32 tiles, which requires splitting into screenblocks. In Usenti this is called the ‘sbb’ layout, in grit it's ‘-mLs’ and for gfx2gba you'd use ‘-mm 32’ … I think. In any case, after a conversion you'd have a palette, a tileset and a tilemap.

<div class="cblock">
<table id="fig:brin" width=100%>
<tr>
  <td valign="top" width=160>
    <div class="cpt">
    <img src="img/demo/brin_demo_pal.png" 
      alt=""><br>
    <b>{*@fig:brin}a</b>: <tt>brin_demo</tt> palette.
	</div>
  <td rowspan=2 markdown>
```c
const unsigned short brinMap[2048]=
{
    // Map row 0
    0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x3001,0x3002,
    0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,
    0x3001,0x3002,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,
    0x3001,0x3002,0x0000,0x0000,0x3001,0x3002,0x0000,0x0000,

    // Map row 1
    0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x3003,0x3004,
    0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,
    0x3003,0x3004,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,
    0x3003,0x3004,0x0000,0x0000,0x3003,0x3004,0x0000,0x0000,

    // Map row 2
    0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,
    0x3001,0x3002,0x3005,0x3006,0x3007,0x3008,
    // ... etc
```
<tr>
  <td valign="bottom">
    <div class="cpt">
    <img src="img/demo/brin_demo_tiles.png" alt=""><br>
    <b>{*@fig:brin}b</b>: <tt>brin_demo</tt> tileset.
    </div>
</table>
</div>

In {@fig:brin} you can see the full palette, the tileset and part of the map. Note that the tileset of {@fig:brin}b is not the same as that of {@fig:map}b because the former uses 8×8 tiles while the latter used 16×16 tiles. Note also that the screen entries you see here are either 0 (i.e., the empty tile) or of the form `0x3xxx`. The high nybble indicates the palette bank, in this case three. If you'd look to the palette ({@fig:brin}a) you'd see that this gives bluish colors.

Now on to using these data. Remember the essential steps here:

-   Load the graphics: tiles into charblocks and colors in the background palette.
-   Load a map into one or more screenblocks.
-   Switch to the right mode in `REG_DISPCNT` and activate a background.
-   Initialize that background's control register to use the right CBB, SBB and bitdepth.

If you do it correctly, you should have something showing on screen. If not, go to the tile/map/memory viewers of your emulator; they'll usually give you a good idea where the problem is. A common one is having a mismatch between the CBB and SBB in `REG_BGxCNT` and where you put the data, which most likely would leave you with an empty map or empty tileset.

The full code of *brin_demo* is given below. The three calls to `memcpy()` load up the palette, tileset and tilemap. For some reason, probably related to where the NES and 8-bit Game Boy put screenblocks in video memory, it's become conventional to place the maps in the last screenblocks on GBA as well. In this case, that's 30 rather than 31 because we need two blocks for a 64×32t map. For the scrolling part, I'm using two variables to store and update the positions because the scrolling registers are write-only. I'm starting at (192, 64) here because that's what I used for the scrolling picture of {@fig:map-ofs} earlier.

<div id="cd-brin-demo" markdown>
```c
#include <string.h>

#include "toolbox.h"
#include "input.h"
#include "brin.h"

int main()
{
    // Load palette
    memcpy(pal_bg_mem, brinPal, brinPalLen);
    // Load tiles into CBB 0
    memcpy(&tile_mem[0][0], brinTiles, brinTilesLen);
    // Load map into SBB 30
    memcpy(&se_mem[30][0], brinMap, brinMapLen);

    // set up BG0 for a 4bpp 64x32t map, using
    //   using charblock 0 and screenblock 31
    REG_BG0CNT= BG_CBB(0) | BG_SBB(30) | BG_4BPP | BG_REG_64x32;
    REG_DISPCNT= DCNT_MODE0 | DCNT_BG0;

    // Scroll around some
    int x= 192, y= 64;
    while(1)
    {
        vid_vsync();
        key_poll();

        x += key_tri_horz();
        y += key_tri_vert();

        REG_BG0HOFS= x;
        REG_BG0VOFS= y;
    }

    return 0;
}
```
</div>

<div class="cblock">
<table id="fig:brin-demo">
<tr>
  <td>
	<div class="cpt" style="width:240px;">
	  <img src="img/demo/brin_demo.png"
		alt=""><br>
	  <b>{*@fig:brin-demo}a</b>: <tt>brin_demo</tt> 
	    at <b>dx</b>=(192, 64).
	</div>
  <td>
	<div class="cpt" style="width:240px;">
	  <img src="img/demo/brin_demo0.png"
		alt=""><br>
	  <b>{*@fig:brin-demo}b</b>: <tt>brin_demo</tt> 
	    at <b>dx</b>=(0, 0).
	</div>
</table>
</div>

#### Interlude: Fast-copying of non sbb-prepared maps

This is not exactly required knowledge, but should make for an interesting read. In this demo I use a multi-sbb map that was already prepared for that. The converter made sure that the left block of the map came before the right block. If this weren't the case then you couldn't load the whole map in one go because the second row of the left block would use the first row of the right block and so on (see {@fig:brin-bad}).

<div class="lblock">
	<div class="cpt" style="width:512px;">
	  <img src="img/demo/brin_demo_bad.png" id="fig:brin-bad"
		alt=""><br>
	  <b>{*@fig:brin-bad}</b> <tt>brin_demo</tt> 
	  without blocking out into SBB's first.
	</div>
</div>

There are few simple and slow ways and one simple and fast way of copying a non sbb-prepared map to a multiple screenblocks. The slow way would be to perform a double loop to go row by row of each screenblock. The fast way is through struct-copies and pointer arithmetic, like this:

<div id="lin2sbb-fast" markdown>
```c
typedef struct { u32 data[8]; } BLOCK;

int iy;
BLOCK *src= (BLOCK*)brinMap;
BLOCK *dst0= (BLOCK*)se_mem[30];
BLOCK *dst1= (BLOCK*)se_mem[31];

for(iy=0; iy<32; iy++)
{
    // Copy row iy of the left half
   *dst0++= *src++;     *dst0++= *src++;

     // Copy row iy of the right half
   *dst1++= *src++;     *dst1++= *src++;
}
```

A `BLOCK` struct-copy takes care of half a row, so two takes care of a whole screenblock row (yes, you could define `BLOCK` as a 16-word struct, but that wouldn't work out anymore. Trust me). At that point, the `src` pointer has arrived at the right half of the map, so we copy the next row into the right-hand side destination, `dst1`. When done with that, `src` points to the second row of the left side. Now do this for all 32 lines. Huzzah for struct-copies, and pointers!

### A screenblock demo {#ssec-demo-sbb}

The second demo, *sbb_reg*, uses a 64×64t background to indicate how multiple screenblocks are used for bigger maps in more detail. While the *brin_demo* used a multi-sbb map as well, it wasn't easy to see what's what because the map was irregular; this demo uses a very simple tileset so you can clearly see the screenblock boundaries. It'll also show how you can use the `REG_BG_OFS` registers for scrolling rather than `REG_BGxHOFS` and `REG_BGxVOFS`.

<div id="cd-demo-sbb" markdown>
```
#include "toolbox.h"
#include "input.h"

#define CBB_0  0
#define SBB_0 28

#define CROSS_TX 15
#define CROSS_TY 10

BG_POINT bg0_pt= { 0, 0 };
SCR_ENTRY *bg0_map= se_mem[SBB_0];


uint se_index(uint tx, uint ty, uint pitch)
{
    uint sbb= ((tx>>5)+(ty>>5)*(pitch>>5));
    return sbb*1024 + ((tx&31)+(ty&31)*32);
}

void init_map()
{
    int ii, jj;

    // initialize a background
    REG_BG0CNT= BG_CBB(CBB_0) | BG_SBB(SBB_0) | BG_REG_64x64;
    REG_BG0HOFS= 0;
    REG_BG0VOFS= 0;

    // (1) create the tiles: basic tile and a cross
    const TILE tiles[2]=
    {
        {{0x11111111, 0x01111111, 0x01111111, 0x01111111,
          0x01111111, 0x01111111, 0x01111111, 0x00000001}},
        {{0x00000000, 0x00100100, 0x01100110, 0x00011000,
          0x00011000, 0x01100110, 0x00100100, 0x00000000}},
    };
    tile_mem[CBB_0][0]= tiles[0];
    tile_mem[CBB_0][1]= tiles[1];

    // (2) create a palette
    pal_bg_bank[0][1]= RGB15(31,  0,  0);
    pal_bg_bank[1][1]= RGB15( 0, 31,  0);
    pal_bg_bank[2][1]= RGB15( 0,  0, 31);
    pal_bg_bank[3][1]= RGB15(16, 16, 16);

    // (3) Create a map: four contingent blocks of 
    //   0x0000, 0x1000, 0x2000, 0x3000.
    SCR_ENTRY *pse= bg0_map;
    for(ii=0; ii<4; ii++)
        for(jj=0; jj<32*32; jj++)
            *pse++= SE_PALBANK(ii) | 0;
}

int main()
{
    init_map();
    REG_DISPCNT= DCNT_MODE0 | DCNT_BG0 | DCNT_OBJ;

    u32 tx, ty, se_curr, se_prev= CROSS_TY*32+CROSS_TX;

    bg0_map[se_prev]++; // initial position of cross
    while(1)
    {
        vid_vsync();

        key_poll();

        // (4) Moving around
        bg0_pt.x += key_tri_horz();
        bg0_pt.y += key_tri_vert();

        // (5) Testing se_index 
        // If all goes well the cross should be around the center of
        // the screen at all times.
        tx= ((bg0_pt.x>>3)+CROSS_TX) & 0x3F;
        ty= ((bg0_pt.y>>3)+CROSS_TY) & 0x3F;

        se_curr= se_index(tx, ty, 64);
        if(se_curr != se_prev)
        {
            bg0_map[se_prev]--;
            bg0_map[se_curr]++;
            se_prev= se_curr;
        }

        REG_BG_OFS[0]= bg0_pt;  // write new position
    }
    return 0;
}
```
</div>

<div class="cpt_fr" style="width:240px">
<img src="img/demo/sbb_reg.png" id="fig:sbb-reg"
  alt="sbb_reg"><br>
<b>{*@fig:sbb-reg}</b>: <tt>sbb_reg</tt>. 
  Compare {@tbl:reg-layout}, 64×64t background. 
  Note the little cross in the top left corner.
</div>

The `init_map()` contains all of the initialization steps: setting up the registers, tiles, palettes and maps. Unlike the previous demo, the tiles, palette and the map are all created manually because it's just easier in this case. At point (1), I define two tiles. The first one looks a little like a pane and the second one is a rudimentary cross. You can see them clearly in the screenshot ({@fig:brin-demo}). The pane-like tile is loaded into tile 0, and is therefore the ‘default’ tile for the map.

The palette is set at point (2). The colors are the same as in {@tbl:reg-layout}: red, green, blue and grey. Take note of which palette entries I'm using: the colors are in different palette banks so that I can use palette swapping when I fill the map. Speaking of which …

Loading the map itself (point (3)) happens through a double loop. The outer loop sets the palette-bank for the screen entries. The inner loop fills 1024 SEs with palette-swapped tile-0's. Now, if big maps used a flat layout, the result would be a big map in four colored bands. However, what actually happens is that you see *blocks*, not bands, proving that indeed regular maps are split into screenblocks just like {@tbl:reg-layout} said. Yes, it's annoying, but that's just the way it is.

That was creating the map, now we turn to the main loop in `main()`. The keys (point (4)) let you scroll around the map. The RIGHT button is tied to a positive change in *x*, but the map itself actually scrolls to the *left*! When I say it like that it may seem counter-intuitive, but if you look at the demo you see that it actually makes sense. Think of it from a hypothetical player sprite point of view. As the sprite moves through the world, you need to update the background to keep the sprite from going off-screen. To do that, the background's movement should be the opposite of the sprite's movement. For example, if the sprite moves to the *right*, you have to move the background to the *left* to compensate.

Finally, there's one more thing to discuss: the cross that appears centered on the map. To do this as you scroll along, I keep track of the screen-entry at the center of the screen via a number of variables and the `se_index()` function. Variables `tx` and `ty` are the tile coordinates of the center of the screen, found by shifting and masking the background pixel coordinates. Feeding these to `se_index()` gives me the screen-entry offset from the screen base block. If this is different than the previous offset, I repaint the former offset as a pane, and update the new offset to the cross. That way, the cross seems to move over the map; much like a sprite would. This was actually designed as a test for `se_index()`; if the function was flawed, the cross would just disappear at some point. But it doesn't. Yay me <kbd>^_^</kbd>

### The charblock demo {#ssec-demo-cbb}

The third demo, *cbb_demo*, covers some of the details of charblocks and the differences in 4bpp and 8bpp tiles. The backgrounds in question are BG 0 and BG 1. Both will be 32×32t backgrounds, but BG 0 will use 4bpp tiles and CBB 0 and BG 2 uses 8bpp tiles and CBB 2. The exact locations and contents of the screenblocks are not important; what is important is to load the tiles to the starts of all 6 charblocks and see what happens.

<div id="cd-cbb-demo" markdown>
```c
#include <toolbox.h>
#include "cbb_ids.h"

#define CBB_4 0
#define SBB_4 2

#define CBB_8 2
#define SBB_8 4

void load_tiles()
{
    int ii;
    TILE *tl= (TILE*)ids4Tiles;
    TILE8 *tl8= (TILE8*)ids8Tiles;

    // Loading tiles. don't get freaked out on how it looks
    // 4-bit tiles to blocks 0 and 1
    tile_mem[0][1]= tl[1];      tile_mem[0][2]= tl[2];
    tile_mem[1][0]= tl[3];      tile_mem[1][1]= tl[4];
    // and the 8-bit tiles to blocks 2 though 5
    tile8_mem[2][1]= tl8[1];    tile8_mem[2][2]= tl8[2];
    tile8_mem[3][0]= tl8[3];    tile8_mem[3][1]= tl8[4];
    tile8_mem[4][0]= tl8[5];    tile8_mem[4][1]= tl8[6];
    tile8_mem[5][0]= tl8[7];    tile8_mem[5][1]= tl8[8];

    // And let's not forget the palette (yes, obj pal too)
    u16 *src= (u16*)ids4Pal;
    for(ii=0; ii<16; ii++)
        pal_bg_mem[ii]= pal_obj_mem[ii]= *src++;
}

void init_maps()
{
    // se4 and se8 map coords: (0,2) and (0,8)
    SB_ENTRY *se4= &se_mem[SBB_4][2*32], *se8= &se_mem[SBB_8][8*32];
    // show first tiles of char-blocks available to bg0
    // tiles 1, 2 of char-block CBB_4
    se4[0x01]= 0x0001;      se4[0x02]= 0x0002;

    // tiles 0, 1 of char-block CBB_4+1
    se4[0x20]= 0x0200;      se4[0x21]= 0x0201;

    // show first tiles of char-blocks available to bg1
    // tiles 1, 2 of char-block CBB_8 (== 2)
    se8[0x01]= 0x0001;      se8[0x02]= 0x0002;

    // tiles 1, 2 of char-block CBB_8+1
    se8[0x20]= 0x0100;      se8[0x21]= 0x0101;

    // tiles 1, 2 of char-block CBB_8+2 (== CBB_OBJ_LO)
    se8[0x40]= 0x0200;      se8[0x41]= 0x0201;

    // tiles 1, 2 of char-block CBB_8+3 (== CBB_OBJ_HI)
    se8[0x60]= 0x0300;      se8[0x61]= 0x0301;
}

int main()
{
    load_tiles();
    init_maps();

    // init backgrounds
    REG_BG0CNT= BG_CBB(CBB_4) | BG_SBB(SBB_4) | BG_4BPP;
    REG_BG1CNT= BG_CBB(CBB_8) | BG_SBB(SBB_8) |  BG_8BPP;
    // enable backgrounds
    REG_DISPCNT= DCNT_MODE0 | DCNT_BG0 | DCNT_BG1 | DCNT_OBJ;

    while(1);

    return 0;
}
```
</div>

The tilesets can be found in *cbb_ids.c*. Each tile contains two numbers: one for the charblock I'm putting it and one for the tile-index in that block. For example, the tile that I want in charblock 0 at tile 1 shows ‘01’, CBB 1 tile 0 shows ‘10’, CBB 1, tile 1 has ‘11’, etc. I have twelve tiles in total, 4 s-tiles to be used for BG 0 and 8 d-tiles for BG 1.

Now, I have six pairs of tiles and I intend to place them in the first tiles of each of the 6 charblock (except for CBBs 0 and 2, where tile 0 would be used as default tiles for the background, which I want to keep empty). Yes six, I'm loading into the sprite charblocks as well. I could do this by hand, calculating all the addresses manually (`0600:0020` for CBB 0, tile 1, etc) and hope I don't make a mistake and can remember what I'm doing when revisiting the demo later, or I can just use my `tile_mem` and `tile8_mem` memory map matrices and get the addresses quickly and without any hassle. Even better, C allows struct assignments so I can load the individual tiles with a simple assignment! That is exactly what I'm doing in `load_tiles()`. The source tiles are cast to `TILE` and `TILE8` arrays for 4bpp and 8bpp tiles respectively. After that, loading the tiles is very simple indeed.

The maps themselves are created in `init_maps()`. The only thing I'm interested in for this demo is to show how and which charblocks are used, so the particulars of the map aren't that important. The only thing I want them to do is to be able to show the tiles that I loaded in `load_tiles()`. The two pointers I create here, `se4` and `se8`, point to screen-entries in the screenblocks used for BG 0 and BG 1, respectively. BG 0's map, containing s-tiles, uses 1 and 512 offsets; BG 1's entries, 8bpp tiles, carries 1 and 256 offsets. If what I said before about tile-index for different bitdepths is true, then you should see the contents of all the loaded tiles. And looking at the result of the demo ({@fig:cbb-demo}), it looks as if I did my math correctly: background tile-indices follow the bg's assigned bitdepth, in contrast to sprites which always counts in 32 byte offsets.

There is, however, one point of concern: on hardware, you won't see the tiles that are actually in object VRAM (blocks 4 and 5). While you might expect to be able to use the sprite blocks for backgrounds due to the addresses, the actual wiring in the GBA seems to forbid it. This is why you should test on hardware is important: emulators aren't always perfect. But if hardware testing is not available to you, test on multiple emulators; if you see different behaviour, be wary of the code that produced it.

<div class="lblock">
<table id="fig:cbb-demo">
<tr valign="top">
<td>
  <div class="cpt" style="width:240px">
  <img src="img/demo/cbb_demo_vba.png" alt="cbb_demo on VBA"><br>
  <b>{*@fig:cbb-demo}a</b>: <tt>cbb_demo</tt> on 
  obsolete emulators (such as VBA and Boycott Adv).
  </div>
<td>
  <div class="cpt" style="width:240px">
  <img src="img/demo/cbb_demo_hw.png" alt="cbb_demo on hardware"><br>
  <b>{*@fig:cbb-demo}b</b>: <tt>cbb_demo</tt> on 
    hardware. Spot the differences!
  </div>
</table>
</div>

### Bonus demo: the 'text' in text bg and introducing tonclib {#ssec-demo-hello}

Woo, bonus demo! This example will serve a number of purposes. The first is to introduce tonclib, a library of code to make life on the GBA a bit easier. In past demos, I've been using *toolbox.h/c* to store useful macros and functions. This is alright for very small projects, but as code gets added, it becomes very hard to maintain everything. It's better to store common functionality in [libraries](https://en.wikipedia.org/wiki/Library_(computing)){target="_blank"} that can be shared among projects.

The second reason is to show how you can output text, which is obviously an important ability to have. Tonclib has an extensive list of options for text rendering – too much to explain here – but its interface is pretty easy. For details, visit the [Tonc Text Engine chapter](tte.html).

Anyway, here's the example.

<div id="cd-hello" markdown>
```c
#include <stdio.h>
#include <tonc.h>

int main()
{
    REG_DISPCNT= DCNT_MODE0 | DCNT_BG0;

    // Init BG 0 for text on screen entries.
    tte_init_se_default(0, BG_CBB(0)|BG_SBB(31));

    tte_write("#{P:72,64}");        // Goto (72, 64).
    tte_write("Hello World!");      // Print "Hello world!"

    while(1);

    return 0;
}
```
</div>

<div class="lblock">
<table id="fig:hello">
<tbody valign="top">
<tr>
  <td>
    <div class="cpt" style="width:112px;">
      <img src="img/demo/hello.png" alt=""><br>
      <b>{*@fig:hello}a</b>: <tt>hello</tt> demo.
    </div>
  <td>
    <div class="cpt" style="width:256px;">
      <img src="img/demo/hello_tiles.png" alt=""><br>
      <b>{*@fig:hello}b</b>: tileset of the <tt>hello</tt> demo.
    </div>
</tbody>
</table>
</div>

Yes, it is indeed a “hello world” demo, the starting point of nearly every introductory C/C++ tutorial. However, those are usually for meant for PC platforms, which have native console functionality like `printf()` or `cout`. These do not exist for the GBA. (Or “didn't”, I should say; there are ways to make use of them nowadays. See [tte:conio](tte.html#ssec-misc-conio) for details.)

Tonc's support for text goes through `tte_` functions. In this case, `tte_init_se_default()` sets up background 0 for tile-mapped text. It also loads the default 8×8 font into charblock 0 (see {@fig:hello}b). After that, you can write to text with `tte_write`. The sequence `#{P:x,y}` is the formatting command that TTE uses to position the cursor. There are a number of these, some of which you'll also see in later chapters.

From this point on, I'll make liberal use of tonclib's text capabilities in examples for displaying values and the like. This will mostly happen without explanation, because that won't be part of the demo. Again, to see the internals, go to the [TTE chapter](tte.html).

#### Creating and using code libraries

Using the functions themselves is pretty simple, but they are spread out over multiple files and reference even more. This makes it a hassle to find which files you need to add to the list of sources to compile a project. You could add everything, of course, but that's not a pleasant prospect either. The best solution is to pre-compile the utility code into a library.

Libraries are essentially clusters of object files. Instead of linking the objects into an executable directly, you <dfn>archive</dfn> them with arm-none-eabi-ar. The command is similar to the link step as well. Here is how you can create the library libfoo.a from objects foo.o, bar.o and baz.o.

```makefile
# archive rule
libfoo : foo.o bar.o baz.o
    arm-none-eabi-ar -crs libfoo.a foo.o bar.o baz.o
# shorthand rule: $(AR) rcs $@ $^
```

The three flags stand for **c**reate archive, **r**eplace member and create **s**ymbol table, respectively. For more on these and other archiving flags, I will refer you to the manual, which is part of the [binutils](https://sourceware.org/binutils/){target="_blank"} toolset. The flags are followed by the library name, which is followed by all the objects (the ‘members’ you want to archive).

To use the library, you have to link it to the executable. There are two linker flags of interest here: `-L` and `-l`. Upper- and lowercase ‘L’. The former, `-L` adds a library path. The lowercase version, `-l`, adds the actual library, but there is a twist here: only need the root-name of the library. For example, to link the library *libfoo.a*, use `-lfoo`. The prefix *lib* and extension *.a* are assumed by the linker.

```makefile
# using libfoo (assume it's in ../lib)
$(PROJ).elf : $(OBJS)
    $(LD) $^ $(LDFLAGS) -L../lib -lfoo -o $@
```

Of course, these archives can get pretty big if you dump a lot of stuff in there. You might wonder if all of it is linked when you add a library to your project. The answer is no, it is not. The linker is smart enough to use only the files which functions you're actually referencing. In the case of this demo, for example, I'm using various text functions, but none of the [affine](affine.html) functions or tables, so those are excluded. Note that the exclusion goes by *file*, not by *function*. If you only have one file in the library (or `#include`d everything, which amounts to the same thing), everything will be linked.

I intend to use tonclib in a number of later demos. In particular, the memory map, text and copy routines will be present often. Don't worry about what they do for the demo; just focus on the core content itself. Documentation of tonclib can be found in the *tonclib* folder (`tonc/code/libtonc`) and at [Tonclib's website](https://www.coranac.com/man/tonclib/){target="_blank"}.

<div class="note" markdown>
<div class="nhgood" markdown>
Better copy and fill routines: `memcpy16`/`32` and `memset16`/`32`
</div>

Now that I am using tonclib as a library for its text routines, I might as well use it for its copy and fill routines as well. Their names are `memcpy16()` and `memcpy32()` for copies and `memset16()` and `memset32()` for fill routines. The 16 and 32 denote their preferred datatypes: halfwords and words, respectively. Their arguments are similar to the conventional `memcpy()` and `memset()`, with the exception that the size is the number of items to be copied, rather than in bytes.

```c
void memset16(void *dest, u16 hw, uint hwcount);
void memcpy16(void *dest, const void *src, uint hwcount);

void memset32(void *dest, u32 wd, uint wcount) IWRAM_CODE;
void memcpy32(void *dest, const void *src, uint wcount) IWRAM_CODE;
```

These routines are optimized assembly so they are [fast](text.html#ssec-demo-se2). They are also safer than the [dma routines](dma.html#sec-func), and the [BIOS routine](swi.html) `CpuFastSet()`. Basically, I highly recommend them, and I will use them wherever I can.
</div>

<div class="note" markdown>
<div class="nhcare">
Linker options: object files before libraries
</div>

In most cases, you can change the order of the options and files freely, but in the linker's case it is important the object files of the projects are mentioned *before* the linked libraries. If not, the link will fail. Whether this is standard behaviour or if it is an oversight in the linker's workings I cannot say, but be aware of potential problems here.
</div>

## In conclusion {#sec-conc}

Tilemaps are essential for most types of GBA games. They are trickier to get to grips with than the bitmap modes or sprites because there are more [steps to get exactly right](#ssec-demo-brin). And, of course, you need to be sure the editor that gave you the map actually supplied the data you were expecting. Fool around with the demos a little: run them, change the code and see what happens. For example, you could try to add scrolling code to the brin_demo so you can see the whole map. Change screen blocks, change charblock, change the bitdepth, mess up *intentionally* so you can see what can go wrong, so you'll be prepared for it when you try your own maps. Once you're confident enough, only then start making your own. I know it's the boring way, but you will benefit from it in the long run.
