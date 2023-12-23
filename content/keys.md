# 6. The GBA buttons (a.k.a. keys) {#ch-}

<!-- toc -->

## Introduction {#sec-intro}

As you no doubt already know, the GBA has one 4-way directional pad (D-pad); two control buttons (Select and Start); two regular fire buttons (A and B) and two shoulder buttons (L and R), making a total of 10 <dfn>keys</dfn>. This is all you have in terms of user-GBA interaction, and for most purposes it is plenty. The principles of key-handling are pretty simple: you have one register with the keystates and you see which buttons are pressed based on whether its bits are set or cleared. I will cover this, but I'll also give some more advanced functions that you will probably want to have at some point.

## Keypad registers {#sec-regs}

### The keypad register, REG_KEYINPUT {#ssec-reg-keys}

As said, the GBA has ten buttons, often referred to as keys. Their states can be found in the first 10 bits of the `REG_KEYINPUT` register at location `0400:0130h` (a.k.a. `REG_P1`). The exact layout is shown below. I will refrain from giving a bit-by-bit description because it should be quite obvious. The names of the defined constants I use are "`KEY_`*x*", where *x* is the name of the button, in caps.

<div class="reg">
  <table class="reg" id="tbl-reg-keys" border=1 frame=void cellpadding=4 cellspacing=0>
    <caption class="reg">REG_KEYINPUT (REG_P1) @ <code>0400:0130h</code></caption>
    <tr class="bits rof">
      <td>F E D C B A</td>
      <td>9</td>
      <td>8</td>
      <td>7</td>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr class="bf">
      <td> -</td>
      <td class="rclr3">L</td>
      <td class="rclr3">R</td>
      <td class="rclr0">down</td>
      <td class="rclr0">up</td>
      <td class="rclr0">left</td>
      <td class="rclr0">right</td>
      <td class="rclr2">start</td>
      <td class="rclr2">select</td>
      <td class="rclr1">B</td>
      <td class="rclr1">A</td>
    </tr>
  </table>
</div>

Checking whether a key is pressed (down) or not would be obvious, if it weren't for one little detail: the bits are *clear*ed when a key is down. So the default state of `REG_KEYINPUT` is `0x03FF`, and not `0`. As such, checking if `key` is down goes like this:

```c
#define KEY_DOWN_NOW(key)  (~(REG_KEYINPUT) & key)
```

In case your bit-operation knowledge is a bit hazy (get it cleared up. Fast!), this first inverts `REG_KEYINPUT` to a more intuitive (and useful) ‘bit is set when down’ setting and then masks it with the key(s) you want to check. Note that `key` can in fact be a combination of multiple keys and the result will be the combination of keys that are actually down.

<div class="note">
  <div class="nhcare">Key states are inverted</div>

  The key bits are low-active, meaning that they are **cleared** when a button is pressed and **set** when they're not. This may be a little counter-intuitive, but that's the way it is.
</div>

### The key control register, REG_KEYCNT {#ssec-reg-keycnt}

Just about everything you will ever need in terms of key-handling can be done with `REG_KEYINPUT`. That said, you might like to know there is another key-register for some extra control. The register in question is `REG_KEYCNT`, the key control register. This register is used for keypad [interrupts](interrupts.html), much like `REG_DISPSTAT` was used for video interrupts. The layout is the same as for `REG_KEYINPUT`, except for the top two bits, see the table below. With `REG_KEYCNT`\{14\} you can enable the keypad interrupt. The conditions for raising this interrupt are determined by `REG_KEYCNT`\{0-9\}, which say what keys to watch out for and `REG_KEYCNT`\{15\}, which state the exact conditions. If this bit is clear, then any of the aforementioned keys will raise the interrupt; if set, then they must all be down for the interrupt to be raised. I wouldn't be surprised if this is how you can reset most games by pressing Start+Select+B+A. Of course, to make use of this register you need to know how to work with [interrupts](interrupts.html) first.

<br>
<div class="reg">
  <table class="reg" id="tbl-reg-keycnt" border=1 frame=void cellpadding=4 cellspacing=0>
    <caption class="reg">REG_KEYCNT (REG_P1CNT) @ <code>0400:0132h</code></caption>
    <tr class="bits">
      <td>F</td>
      <td>E</td>
      <td>D C B A</td>
      <td>9</td>
      <td>8</td>
      <td>7</td>
      <td>6</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr class="bf">
      <td class="rclr1">Op</td>
      <td class="rclr0">I</td>
      <td>-</td>
      <td class="rclr9">L</td>
      <td class="rclr9">R</td>
      <td class="rclr9">down</td>
      <td class="rclr9">up</td>
      <td class="rclr9">left</td>
      <td class="rclr9">right</td>
      <td class="rclr9">start</td>
      <td class="rclr9">select</td>
      <td class="rclr9">B</td>
      <td class="rclr9">A</td>
    </tr>
  </table>
  <br>
  <table>
    <col class="bits" width=40>
    <col class="bf" width="8%">
    <col class="def" width="12%">
    <tr align="left">
      <th>bits</td>
      <th>name</td>
      <th>define</td>
      <th>description</td>
    </tr>
    <tbody valign="top">
      <tr class="bg0">
        <td>0-9</td>
        <td class="rclr9">keys</td>
        <td>KEY_<i>x</i></td>
        <td>keys to check for raising a key interrupt.</td>
      </tr>
      <tr class="bg1">
        <td>E<td class="rclr0">I</td>
        <td>KCNT_IRQ</td>
        <td>Enables keypad interrupt</td>
      </tr>
      <tr class="bg0">
        <td>F</td>
        <td class="rclr1">Op</td>
        <td>KCNT_OR, KCNT_AND</td>
        <td>Boolean operator used for determining whether to raise a key- interrupt or not. If clear, it uses an OR (raise if any of the keys of bits 0-9 are down); if set, it uses an AND (raise if all of those keys are down).</td>
      </tr>
    </tbody>
  </table>
</div>

## Beyond basic button states {#sec-adv-keys}

While checking for the keystate with `KEY_DOWN_NOW()` is nice and simple, there are better and/or more preferable methods of key-state handling. I will discuss two (or three) of them here. First, <dfn>synchronous keystates</dfn>. This is just a fancy way of reading the key-state at a given point and using that variable, instead of repeated reads of REG_KEYINPUT when you process input. An outshoot of this is <dfn>transitional states</dfn>, where you track not only the current state, but also the previous one. This lets you test for *changes* in keystates, rather than just the keystates themselves.. Lastly, <dfn>tribools</dfn>: three-state variables (in this cases −1, 0 and +1) that can be used to simplify direction processing.

### Synchronous and transitional key states {#ssec-adv-sync}

The use of `KEY_DOWN_NOW()` is a form of <dfn>asynchronous</dfn> key handling: you check the state at the time the code needs it. While it works, it's not always the best approach. Firstly, it is less efficient in terms of code because the register is loaded and read every time it is necessary (it's volatile, remember?). A secondary concern is that a simultaneous multi-button tap may not be registered as such because the code reading the button states are a little apart.

But those are just minor concerns; the main issue is that there's just little you can really do with them. You can get the current state, but that's it. As a simple example of why this is insufficient for games, consider (un)pausing a game. This is usually done by pressing Start, and then Start again for unpausing. That's fine until you consider that the game runs faster than you can react (this is a basic fact of life; the only reason you can win games is because the game lets you. Deal), so the `Start` button will be down for multiple frames. With `KEY_DOWN_NOW()`, the game will pause *and* unpause during this time; the state of the game when you finally release the button is essentially random. Needless to say, this is a Bad Thing™.

Enter synchronous states. Simply read the state once, at the beginning of the frame for example, and use that as ‘the’ state for the whole frame. That takes care of the excess readings of REG_KEYINPUT, and potentially missed simultaneity. For tracking state changes, we also save the state of the previous frame. So at the very least, we need two variables and a function that updates them, and for good measure, some functions that check the states. Because these will be quite small, it makes sense to inline them as well.

```c
// === (tonc_core.c) ==================================================
// Globals to hold the key state
u16 __key_curr=0, __key_prev=0;
```

```c
// === (tonc_input.h) =================================================
extern u16 __key_curr, __key_prev;

#define KEY_A        0x0001
#define KEY_B        0x0002
#define KEY_SELECT   0x0004
#define KEY_START    0x0008
#define KEY_RIGHT    0x0010
#define KEY_LEFT     0x0020
#define KEY_UP       0x0040
#define KEY_DOWN     0x0080
#define KEY_R        0x0100
#define KEY_L        0x0200

#define KEY_MASK     0x03FF

// Polling function
INLINE void key_poll()
{
    __key_prev= __key_curr;
    __key_curr= ~REG_KEYINPUT & KEY_MASK;
}

// Basic state checks
INLINE u32 key_curr_state()         {   return __key_curr;          }
INLINE u32 key_prev_state()         {   return __key_prev;          }
INLINE u32 key_is_down(u32 key)     {   return  __key_curr & key;   }
INLINE u32 key_is_up(u32 key)       {   return ~__key_curr & key;   }
INLINE u32 key_was_down(u32 key)    {   return  __key_prev & key;   }
INLINE u32 key_was_up(u32 key)      {   return ~__key_prev & key;   }
```

The key states are stored in `__key_curr` and `__key_prev`. The function that updates them is `key_poll()`. Note that this function already inverts REG_KEYINPUT, so that the variables are active high, which makes later operations more intuitive. For example, to test whether A is currently down (pressed), just mask `__key_curr` with `KEY_A`, the bit for A. This is what `key_is_down()` does. While `KEY_DOWN_NOW()` gives (almost) the same answer, I would still recommend using `key_is_down()` instead.

<div class="note">
  <div class="nhgood">Invert REG_KEYINPUT reads as soon as possible</div>
  The things that you might check the keystates for are simply easier in active-high settings. Therefore, it is a good idea to make the keystate variables work that way.
</div>

### Transitional states {#ssec-adv-trans}

Back to the pause/unpause issue. The nasty behaviour `KEY_DOWN_NOW()` causes is known as <dfn>key bounce</dfn>. This is because the macro only checks the current state. What you need for proper (un)pausing is something that checks whether a key is *going* down, rather than just down: you need to check the transition. That's where the previous state comes in. When a key is hit, i.e., the moment of it going down, it will be pressed in the current state, but not the one before. In other words, the keys that are ‘hit’ are down currently, and not before: `__key_curr&~__key_prev`. After that, checking for a particular key can be achieved with a simple mask as usual. This is done by `key_hit()`.

That's really all there is to it, and you can create similar functions to check for releases (before AND NOT now), if it is held (before AND now), et cetera. Again, it all seems so simple because the states were already inverted; when I first made these functions, I had a terrible time figuring out what the right bit-ops were because the active-low logic was throwing me off. Well okay, not *really* but it would have been easier if I had them inverted from the start.

```c
// Transitional state checks.

// Key is changing state.
INLINE u32 key_transit(u32 key)
{   return ( __key_curr ^  __key_prev) & key;   }

// Key is held (down now and before).
INLINE u32 key_held(u32 key)
{   return ( __key_curr &  __key_prev) & key;  }

// Key is being hit (down now, but not before).
INLINE u32 key_hit(u32 key)
{   return ( __key_curr &~ __key_prev) & key;  }

Key is being released (up now but down before)
INLINE u32 key_released(u32 key)
{   return (~__key_curr &  __key_prev) & key;  }
```

### Key tribool states {#ssec-adv-tri}

This is a little technique taken from the [PA_Lib wiki](https://web.archive.org/web/20110318222049/http://www.palib.info/wiki/doku.php?id=day3). It isn't so much about keys per se, but a shorthand in how you can use the functions, and you will have to make up for yourself whether what's discussed in this subsection is right for you.

Imagine you have a game/demo/whatever in which you can move stuff around. To make a character move left and right, for example, you might do use something like this.

```c
// variable x, speed dx
if(key_is_down(KEY_RIGHT))
    x += dx;
else if(key_is_down(KEY_LEFT))
    x -= dx;
```

Thing moves right, *x* increases; thing moves left, *x* decreases, simple enough. Works fine too. However, and this may just be my ifphobia acting up, it's not very pretty code. So let's see if we can find something smoother.

Take a look at what the code is actually doing. Depending on two choices, the variable is either increased (+), decreased (−), or unchanged (0). That's a pretty good definition of a <dfn>tribool</dfn>, a variable with three possible states, in this case +1, 0 and −1. What I'm after is something that lets you use these states to do the following.

```c
x += DX*key_tri_horz();
```

I suppose I could just wrap the `if`s in this function, but I prefer to do it via bit operations. All I need to do for this is shift the bits for specific keys down, mask that with one, and subtract the results.

```c
// === (tonc_core.h) ==================================================
// tribool: 1 if {plus} on, -1 if {minus} on, 0 if {plus}=={minus}
INLINE int bit_tribool(u32 x, int plus, int minus)
{   return ((x>>plus)&1) - ((x>>minus)&1);  }
```

```c
// === (tonc_input.h) =================================================
enum eKeyIndex
{
    KI_A=0, KI_B, KI_SELECT, KI_START,
    KI_RIGHT, KI_LEFT, KI_UP, KI_DOWN,
    KI_R, KI_L, KI_MAX
};

// --- TRISTATES ---
INLINE int key_tri_horz()       // right/left : +/-
{   return bit_tribool(__key_curr, KI_RIGHT, KI_LEFT);  }

INLINE int key_tri_vert()       // down/up : +/-
{   return bit_tribool(__key_curr, KI_DOWN, KI_UP);     }

INLINE int key_tri_shoulder()   // R/L : +/-
{   return bit_tribool(__key_curr, KI_R, KI_L);         }

INLINE int key_tri_fire()       // B/A : -/+
{   return bit_tribool(__key_curr, KI_A, KI_B);         }
```

The inline function `bit_tribool()` creates a tribool value from any two bits in a number (register or otherwise). The rest of the functions listed here use the current keystate and the key-bits to create tribools for horizontal, vertical, shoulder and fire buttons; others can be creates with relative ease. These functions make the code look cleaner and are faster to boot. You will be seeing them quite often.

While the functions mentioned above only use `__key_curr`, it is easy to write code that uses other key-state types. For example, a right-left `key_hit` variant might look something like this:

```c
// increase/decrease x on a right/left hit
x += DX*bit_tribool(key_hit(-1), KI_RIGHT, KI_LEFT);
```

It's just a call to `bit_tribool()` with using `key_hit()` instead of `__key_curr`. In case you're wondering what the “−1” is doing there, I just need it to get the full hit state. Remember that −1 is `0xFFFFFFFF` in hex, in other words a full mask, which will be optimized out of the final code. You will see this use of tribools a couple of times as well.

## A simple key demo {#sec-demo}

<div class="cpt_fr" style="width:120px;">
<img alt="key_demo screenshot" src="./img/demo/gba_sm.png" id="fig:key-demo">

**{*@fig:key-demo}**: key_demo screenshot, with L and B held.
</div>

The *key_demo* demo illustrates how these key functions can be used. It shows a mode 4 picture of a GBA (a 240x160 8bit bitmap); the colors change according to the button presses. The normal state is grey; when you press the key, it turns red; when you release it, it goes yellow; and as long as it's held it's green. {*@fig:key-demo} shows this for the L and B buttons. Here's the code that does the real work:

<div id="cd-key-demo">

```c
#include <string.h>

#include "toolbox.h"
#include "input.h"

#include "gba_pic.h"

#define BTN_PAL_ID  5
#define CLR_UP   RGB15(27,27,29)

int main()
{
    int ii;
    u32 btn;
    COLOR clr;
    int frame=0;

    memcpy(vid_mem, gba_picBitmap, gba_picBitmapLen);
    memcpy(pal_bg_mem, gba_picPal, gba_picPalLen);

    REG_DISPCNT= DCNT_MODE4 | DCNT_BG2;

    while(1)
    {
        vid_vsync();
        // slowing down polling to make the changes visible
        if((frame & 7) == 0)
            key_poll();
        // check state of each button
        for(ii=0; ii<KI_MAX; ii++)
        {
            clr=0;
            btn= 1<<ii;
            if(key_hit(btn))
                clr= CLR_RED;
            else if(key_released(btn))
                clr= CLR_YELLOW;
            else if(key_held(btn))
                clr= CLR_LIME;
            else
                clr= CLR_UP;
            pal_bg_mem[BTN_PAL_ID+ii]= clr;
        }
        frame++;
    }

    return 0;
}
```
</div>

`BTN_PAL_ID` is the starting index of the palette-part used for the buttons and `CLR_UP` is a shade of grey; the rest of the colors should be obvious. To make sure that you can actually see the changes in button colors I'm only polling the keys once every 8 frames. If I didn't do that, you'll hardly ever see a red or yellow button. (By the way, I don't actually change the buttons' colors, but only the palette color that that button's pixels use; palette animation is a Good Thing™).
