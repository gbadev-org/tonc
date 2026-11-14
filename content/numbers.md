# A. Numbers, bits and bit operations

<!-- toc -->

## Numbers {#sec-num}

### The true meaning of symbols {#ssec-num-intro}

> “There are 10 kinds of people in the world, those that understand binary and those that don't.”

If you don't get the joke, you belong in the latter category. Just like everyone else, in your youth you've probably learned that the combination of numerals ‘1’ and ‘0’ means ten. Not so—not exactly. The primary problem here is the meaning of symbols. Now, what I'm about to tell you is key to understanding mystifying stuff out there, so gather around and let me tell you something about what they really mean. Listening? All right then. Your basic everyday symbol, like ‘1’ and ‘0’ and such, your basic symbol means exactly **SQUAT**!

That's right: zilch, zip, nada, noppes, dick, and all the other synonyms you can think of that mean ‘nothing’. In and of themselves, symbols have no meaning; rather, meaning *is imposed* on them by us humans. Symbols are means of communication. There's a lot of stuff in the world—objects, people, feelings, actions—and we label these things with symbols to tell them apart. The symbols themselves mean nothing; they're just <dfn>representations</dfn>, labels that we can make up as we see fit. Unfortunately, this is something that is rarely mentioned when you're growing up, the only thing they tell you is which symbol is tied to which concept, which can lead people to confuse the thing itself with its representation. There are people that do just this, but still realise that the symbols are just social constructs, and start believing that the things they represent, stuff like gravity and the number π, are just social constructs too. (Yet these same people aren't willing to demonstrate this by, say, stepping out of a window on the 22nd floor.)

As a simple example of symbol(s), consider the word “chair”. The word itself has no intrinsic relationship with a “piece of furniture for one person to sit on, having a back and, usually, four legs.” (Webster's); it's just handy to have a word for such an object so that we know what we're talking about in a conversation. Obviously, this only works if all parties in the conversation use the same words for the same objects, so at some point in the past a couple of guys got together and decided on a set of words and called it the English language. Since words are just symbols with no intrinsic meaning, different groups can and have come up with a different set of words.

Such an agreement between people for the sake of convenience is called a <dfn>convention</dfn> (basically, a fancy word for standard). Conventions can be found everywhere. That's part of the problem: they are so ubiquitous that they're usually taken for granted. At some point in time, a convention has become so normal that people forget that it was merely an agreement made to facilitate communication, and will attach real meaning to the thing convened upon: the convention is now a “tradition”.

Back to numbers. Numbers are used for two things: quantities and identifications (cardinal and ordinal numbers, respectively). It's primarily quantities we're concerned with here: one banana, two bananas, three bananas, that sort of thing. The way numbers are written down—represented by symbols—is merely a convention; for most people, it's probably even a tradition. There are a couple of different ways to represent numbers: by words (one, two, three, four, five) by carvings (*I, II, III, IIII, ~~IIII~~*), Roman numerals (I, II, III, IV, V). You have all seen these at some point or another. The system most commonly used, however, is a variant of what's called the <dfn>base-*N* positional system</dfn>.

### The Base-*N* Positional System {#ssec-num-basen}

“So, Mike, what is the base-n positional system?” Well, it's probably the most convenient system to use when you have to write down long numbers and/or do arithmetic! The basic idea is that you have *N* symbols—numerals—at your disposal, for 0 up to *N*−1, and you represent each possible number by a *string* of *m* numerals. The numeral at position *i* in the string, *a*<sub>i</sub>, is a multiplier of the *i*-th power of the base number. The complete number *S* is the sum of the product of the powers *N*<sup>i</sup> and their multipliers *a*<sub>i</sub>.

<!--
S={\Sigma}a_iN^i
-->
<table id="eq:sum-aini">
<tr>
  <td class="eqnrcell">({!@eq:sum-aini})</td>
  <td class="eqcell">
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle displaystyle="true" scriptlevel="0">
    <mrow data-mjx-texclass="ORD">
      <mtable rowspacing=".5em" columnspacing="1em" displaystyle="true">
        <mtr>
          <mtd>
            <mi>S</mi>
            <mo>=</mo>
            <mrow data-mjx-texclass="ORD">
              <mi mathvariant="normal">&#x3A3;</mi>
            </mrow>
            <msub>
              <mi>a</mi>
              <mi>i</mi>
            </msub>
            <msup>
              <mi>N</mi>
              <mi>i</mi>
            </msup>
          </mtd>
        </mtr>
      </mtable>
    </mrow>
  </mstyle>
</math>
  </td>
</tr>
</table>

Another way of thinking about the system is by looking at these numbers as a set of counters, like old-style odometers in cars and old cassette players. Here you have a number of revolving wheels with *N* numerals on each. Each wheel is set so that they will increment the counter before it after a revolution has been completed. You start with all zeros, and then begin to turn the last wheel. After *N* numbers have passed, you will have a full revolution: this counter will be back to zero, and the one next to it will increase by one. And again after *N* more counts, and after *N*<sup>2</sup> the second counter will be full as well and so a third counter will increase, etc, etc.

Here's an example using the familiar case of *N* is ten: the decimal system. Base-ten means ten different symbols (digits): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Note that the form of these symbols is arbitrary, but this is how we got/stole them from the Arabs centuries ago. Note also the zero symbol. The zero is one of the key discoveries in mathematics, and makes the positional system possible. Now, for our sample string of numerals, consider “1025”, which is to be read as:

<div class="lblock">
<table>
<tr><td>1025<sub>ten</sub></td>
  <td>=</td><td> 1·10<sup>3</sup><sub>ten</sub></td>
  <td>+</td><td> 0·10<sup>2</sup><sub>ten</sub></td>
  <td>+</td><td> 2·10<sup>1</sup><sub>ten</sub></td>
  <td>+</td><td> 5·10<sup>0</sup><sub>ten</sub></td></tr>
<tr><td></td>
  <td>=</td><td> 1·1000<sub>ten</sub></td>
  <td>+</td><td> 0·100<sub>ten</sub></td>
  <td>+</td><td> 2·10<sub>ten</sub></td>
  <td>+</td><td>5·1</td></tr>
<tr><td></td><td>=</td><td colspan=7> one thousand twenty five</td></tr>
</table>
</div>

You may have noticed I'm using words for numbers a lot of the time. The thing is that if you write the ‘*N*’ in ‘base-*N*’ in its own base, you will always write ‘base-10’, because the string “10” *always* denoted the base number. That's kind of the point. To point out which “10” you're talking about, I've followed the usual convention and subscripted it with the word “ten”. But because it's a big hassle to subscript every number, I'll use another convention that if the number isn't subscripted, it's a base-ten number. Yes, like everyone has been doing all along, only I've taken the effort of explicitly mentioning the convention.

### base-2: binary {#ssec-num-bin}

What you have to remember is that there's nothing special about using 10 (that is, ten) as the base number; it could have just as well been 2 (binary), 8 (octal), 16 (hexadecimal). True story: in the later decades of the 18th century, when the French were developing the metric system to standardize, well, everything, there were also proposals for going to a duodecimal (base-12) system, because of its many factors. The only reason base-ten is popular is because humans have ten fingers, and that's all there is to it.

As an example, let's look at the binary (base-2) system. This system is kinda special in that it is the simplest base-*N* system, using only two numbers 0 and 1. It is also perfect for clear-cut choices: on/off, black/white, high/low. This makes it ideal for computer-systems and since we're programmers here, you'd better know something about binary.

As said, you only have two symbols (BInary digiTs, or bits) here: 0 and 1. In the decimal system, you have ten symbols before you have to add a new numeral to the string: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. But in a binary system you'll already need a second numeral for two: 0, 1, 10 (with two represented by ‘10’). This means that you get large strings fairly quickly. For example, let's look the number 1025 again. To write this down in binary we have to find the multipliers for the powers of two that will add up to 1025. First, of course, we need the powers of two themselves. The first 11 are:

<div class="lblock">
<table id="tbl:pot" class="table-data">
<caption align="bottom"><b>{*@tbl:pot}</b>: powers of two</caption>
<col span=3 align="right">
<tr align="center"><th>exponent</th><th>binary</th><th>decimal</th></tr>
<tr><td> 0</td> <td>1</td>			<td>1</td></tr>
<tr><td> 1</td> <td>10</td>			<td>2</td></tr>
<tr><td> 2</td> <td>100</td>			<td>4</td></tr>
<tr><td> 3</td> <td>1000</td>			<td>8</td></tr>

<tr><td> 4</td> <td>1,0000</td>		<td>16</td></tr>
<tr><td> 5</td> <td>10,0000</td>		<td>32</td></tr>
<tr><td> 6</td> <td>100,0000</td>		<td>64</td></tr>
<tr><td> 7</td> <td>1000,0000</td>	<td>128</td></tr>

<tr><td> 8</td> <td>1,0000,0000</td>	<td>256</td></tr>
<tr><td> 9</td> <td>10,0000,0000</td>	<td>512</td></tr>
<tr><td>10</td> <td>100,0000,0000</td><td>1024</td></tr>
</table>
</div>

As you can see, the length of binary numbers rises really quickly. With longer numbers it's often difficult to see the actual size of the critter, so I comma-separated them into numeral groups of 4. If you're serious about programming, you *need* to know the powers of two, preferably up to 16. The nice thing about binary is that you won't have to worry much about the multiplication factors of the powers, as the only possibilities are 0 and 1. This makes decimal↔binary conversions relatively easy. For 1025, it is:

<div class="lblock">
<table>
<tr><td>1025<sub>ten</sub></td>
  <td>=</td><td> 1024</td> <td>+</td><td> 1</td></tr>
<tr><td></td>
  <td>=</td><td> 2<sup>10</sup></td> <td>+</td><td> 2<sup>0</sup></td></tr>
<tr><td></td>
  <td>=</td><td colspan=4>100,0000,0001<sub>bin</sub></td></tr>
</table>
</div>

An interesting and completely fortuitous factoid about binary is that 2<sup>10</sup>=1024 is almost 10<sup>3</sup>=1000. Because of this, you will often find powers of 1024 indicated by metric prefixes: kilo-, mega-, giga- etc. The correspondence isn't perfect, of course, but it is a good approximate. It also gives salesmen a good swindling angle: since in the computer world powers of 2 reign supreme, one Megabyte (MB) is 1.05 bytes, but with some justification you could also use the traditional 1M = one million in memory sizes, and thus make it *seem* that your product has 5% more memory. You will also see both notations used randomly in Windows programs, and it's almost impossible to see whether or not that file that Explorer says is 1.4MB will fit on your floppy disk or not.

For this reason, in 1999, the IEC began to recommend a separate set of binary prefixed units based on powers of 1024. These include kibibyte (KiB) for 1024 bytes, mebibyte (MiB) for 1048576 bytes, and gibibyte (GiB) for 1073741824 bytes.

### base-16, hexadecimal {#ssec-num-hex}

<div class="cpt_fr" style="width:160px">

**{*@tbl:count}**: counting to twenty in decimal, binary, hex and octal. Note the alternating sequences in the binary column.

<div class="cblock">
<table id="tbl:count" class="table-data rules-cols">
<col span=4 align="right">
<tr><th> dec</th>	<th> bin</th>	<th> hex</th>	<th> oct</th></tr>
<tr><td>   0</td>	<td>    0</td>	<td>   0</td>    <td>   0</td></tr>
<tr><td>   1</td>	<td>    1</td>	<td>   1</td>    <td>   1</td></tr>
<tr><td>   2</td>	<td>   10</td>	<td>   2</td>    <td>   2</td></tr>
<tr><td>   3</td>	<td>   11</td>	<td>   3</td>    <td>   3</td></tr>
<tr><td>   4</td>	<td>  100</td>	<td>   4</td>    <td>   4</td></tr>
<tr><td>   5</td>	<td>  101</td>	<td>   5</td>    <td>   5</td></tr>
<tr><td>   6</td>	<td>  110</td>	<td>   6</td>    <td>   6</td></tr>
<tr><td>   7</td>	<td>  111</td>	<td>   7</td>    <td>   7</td></tr>
<tr><td>   8</td>	<td> 1000</td>	<td>   8</td>    <td>  10</td></tr>
<tr><td>   9</td>	<td> 1001</td>	<td>   9</td>    <td>  11</td></tr>
<tr><td>  10</td>	<td> 1010</td>	<td>   a</td>    <td>  12</td></tr>
<tr><td>  11</td>	<td> 1011</td>	<td>   b</td>    <td>  13</td></tr>
<tr><td>  12</td>	<td> 1100</td>	<td>   c</td>    <td>  14</td></tr>
<tr><td>  13</td>	<td> 1101</td>	<td>   d</td>    <td>  15</td></tr>
<tr><td>  14</td>	<td> 1110</td>	<td>   e</td>    <td>  16</td></tr>
<tr><td>  15</td>	<td> 1111</td>	<td>   f</td>    <td>  17</td></tr>
<tr><td>  16</td>	<td>10000</td>	<td>  10</td>    <td>  20</td></tr>
<tr><td>  17</td>	<td>10001</td>	<td>  11</td>    <td>  21</td></tr>
<tr><td>  18</td>	<td>10010</td>	<td>  12</td>    <td>  22</td></tr>
<tr><td>  19</td>	<td>10011</td>	<td>  13</td>    <td>  23</td></tr>
<tr><td>  20</td>	<td>10100</td>	<td>  14</td>    <td>  24</td></tr>
</table>
</div>

</div>

In itself, binary isn't so difficult, it's just that the numbers are so large! The solution for this given above was using commas to divide them into groups of four. There is a better solution, namely hexadecimal.

Hexadecimal is the name for the base-16 system, also known as <dfn>hex</dfn>. That an abbreviation exists should tell you something about its prevalence. As you should be able to guess by now, there are 16 symbols in hex. This presents a small problem because we only have 10 symbols associated with numbers. Rather than invent new symbols, the first letters of the alphabet are used, so the sequence becomes: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f. Hex is more concise than binary. In fact, since 16 is 2<sup>4</sup>, you can exactly fit four bits into one hex digit, so hex is exactly 4 times as short as binary. This is also why I used groups of four earlier on. If you know the powers of 2, then you automatically know the powers of 16 too, but rather than decompose numbers into powers of 16, it's often easier to go to binary first, make groups and convert those to hex.

<div class="lblock">
<table>
<tr><td>1025<sub>ten</sub></td>
  <td>=</td><td colspan=4>100,0000,0001<sub>bin</sub></td></tr>
<tr><td></td>
  <td>=</td><td>401<sub>bin</sub>·16<sup>2</sup></td> <td>+</td><td>1·16<sup>0</sup></td></tr>
<tr><td></td>
  <td>=</td><td colspan=4>401<sub>hex</sub></td></tr>
</table>
</div>

A hexadecimal digit is often called a <dfn>nybble</dfn> or a nibble, which fits in nicely with the bit and the byte. Speaking of bytes, bytes are conventionally made up of 8 bits, and hence 2 nybbles. So you can conveniently write down bytes and multiple byte types in nybbles. My personal preference in dealing with hex numbers in to always use an even number of nybbles, to correspond with the whole bytes, but that's just me. Hexadecimal is so engrained in the computer world that it not only has an abbreviation, but also a number of shorthand notations indicating numbers are indeed hex: C uses the prefix `0x`, in assembly you might find `\$`, and in normal text the affix `h` is sometimes used.

Depending on how low-level you do your programming, you will see any of the three systems mentioned above. Aside from decimal, binary and hexadecimal, you might also encounter octal (C prefix `0`) from time to time. Now, even if you know never intend to use octal, you might use it accidentally. If you would like to align your columns of numbers by padding them with zeros, you are actually converting them to octal! Yet one more of those fiendish little bugs that will have you tearing your hair out.

### Using the positional system {#ssec-num-base-use}

Using a base-*N* positional system has a number of advantages over the other number systems. For starters, numbers don't get nearly as long as the carving system; and you don't have to invent new symbols for higher numbers, like in the Roman system. It's also easier to compare two numbers using either the lengths of the strings or just the first number. There's also a tie with probability theory: each individual digit has *N* possibilities, so a number-string with length *m* has *N<sup>m</sup>* possibilities.

Where it really comes into its own is arithmetic. The positions in a number-string are equivalent, so the steps for adding ‘3+4’ are the same for ‘30+40’. This will allow you to break up large calculations into smaller, easier ones. If you can do calculations for single-symbol numbers, you can do them all. What's more, the steps themselves are the same, regardless of which base you use. I won't show you how to do addition in binary or hex, as that's rather trivial, but I will demonstrate multiplication. Here's an example of calculating ‘123 × 456’, in decimal and hexadecimal. I've also given the multiplication tables for convenience.

<div class="cblock" id="tbl:multiply">
  <table class="table-data">
  <caption><b>{*@tbl:multiply}a</b>: decimal multiplication table</caption>
  <col span=11 align="right">
  <tr><th> x</th>
    <th> 1</th> <th> 2</th> <th> 3</th> <th> 4</th> <th> 5</th>
	<th> 6</th> <th> 7</th> <th> 8</th> <th> 9</th> <th>10</th></tr>
  <tr><th> 1</th>
    <td> 1</td> <td> 2</td> <td> 3</td> <td> 4</td> <td> 5</td>
	<td> 6</td> <td> 7</td> <td> 8</td> <td> 9</td> <td>10</td></tr>
  <tr><th> 2</th>
    <td> 2</td> <td> 4</td> <td> 6</td> <td> 8</td> <td>10</td>
	<td>12</td> <td>14</td> <td>16</td> <td>18</td> <td>20</td></tr>
  <tr><th> 3</th>
    <td> 3</td> <td> 6</td> <td> 9</td> <td>12</td> <td>15</td>
	<td>18</td> <td>21</td> <td>24</td> <td>27</td> <td>30</td></tr>
  <tr><th> 4</th>
    <td> 4</td> <td> 8</td> <td>12</td> <td>16</td> <td>20</td>
	<td>24</td> <td>28</td> <td>32</td> <td>36</td> <td>40</td></tr>
  <tr><th> 5</th>
    <td> 5</td> <td>10</td> <td>15</td> <td>20</td> <td>25</td>
	<td>30</td> <td>35</td> <td>40</td> <td>45</td> <td>50</td></tr>
  <tr><th> 6</th>
    <td> 6</td> <td>12</td> <td>18</td> <td>24</td> <td>30</td>
	<td>36</td> <td>42</td> <td>48</td> <td>54</td> <td>60</td></tr>
  <tr><th> 7</th>
    <td> 7</td> <td>14</td> <td>21</td> <td>28</td> <td>35</td>
	<td>42</td> <td>49</td> <td>56</td> <td>63</td> <td>70</td></tr>
  <tr><th> 8</th>
    <td> 8</td> <td>16</td> <td>24</td> <td>32</td> <td>40</td>
	<td>48</td> <td>56</td> <td>64</td> <td>72</td> <td>80</td></tr>
  <tr><th> 9</th>
    <td> 9</td> <td>18</td> <td>27</td> <td>36</td> <td>45</td>
	<td>54</td> <td>63</td> <td>72</td> <td>81</td> <td>90</td></tr>
  <tr><th>10</th>
    <td> 10</td> <td> 20</td> <td> 30</td> <td> 40</td> <td> 50</td>
	<td> 60</td> <td> 70</td> <td> 80</td> <td> 90</td> <td>100</td></tr>
  </table>

  <table class="table-data">
  <caption><b>{*@tbl:multiply}b</b>: hex multiplication table</caption>
  <col span=17 align="right">
  <tr><th> x</th>
    <th> 1</th> <th> 2</th> <th> 3</th> <th> 4</th> <th> 5</th> <th> 6</th> <th> 7</th> <th> 8</th>
    <th> 9</th> <th> A</th> <th> B</th> <th> C</th> <th> D</th> <th> E</th> <th> F</th> <th>10</th></tr>
  <tr><th> 1</th>
    <td> 1</td> <td> 2</td> <td> 3</td> <td> 4</td> <td> 5</td> <td> 6</td> <td> 7</td> <td> 8</td>
    <td> 9</td> <td> A</td> <td> B</td> <td> C</td> <td> D</td> <td> E</td> <td> F</td> <td>10</td></tr>
  <tr><th> 2</th>
    <td> 2</td> <td> 4</td> <td> 6</td> <td> 8</td> <td> A</td> <td> C</td> <td> E</td> <td>10</td>
    <td>12</td> <td>14</td> <td>16</td> <td>18</td> <td>1A</td> <td>1C</td> <td>1E</td> <td>20</td></tr>
  <tr><th> 3</th>
    <td> 3</td> <td> 6</td> <td> 9</td> <td> C</td> <td> F</td> <td>12</td> <td>15</td> <td>18</td>
    <td>1B</td> <td>1E</td> <td>21</td> <td>24</td> <td>27</td> <td>2A</td> <td>2D</td> <td>30</td></tr>
  <tr><th> 4</th>
    <td> 4</td> <td> 8</td> <td> C</td> <td>10</td> <td>14</td> <td>18</td> <td>1C</td> <td>20</td>
    <td>24</td> <td>28</td> <td>2C</td> <td>30</td> <td>34</td> <td>38</td> <td>3C</td> <td>40</td></tr>
  <tr><th> 5</th>
    <td> 5</td> <td> A</td> <td> F</td> <td>14</td> <td>19</td> <td>1E</td> <td>23</td> <td>28</td>
    <td>2D</td> <td>32</td> <td>37</td> <td>3C</td> <td>41</td> <td>46</td> <td>4B</td> <td>50</td></tr>
  <tr><th> 6</th>
    <td> 6</td> <td> C</td> <td>12</td> <td>18</td> <td>1E</td> <td>24</td> <td>2A</td> <td>30</td>
    <td>36</td> <td>3C</td> <td>42</td> <td>48</td> <td>4E</td> <td>54</td> <td>5F</td> <td>60</td></tr>
  <tr><th> 7</th>
    <td> 7</td> <td> E</td> <td>15</td> <td>1C</td> <td>23</td> <td>2A</td> <td>31</td> <td>38</td>
    <td>3F</td> <td>46</td> <td>4D</td> <td>54</td> <td>5B</td> <td>62</td> <td>69</td> <td>70</td></tr>
  <tr><th> 8</th>
    <td> 8</td> <td>10</td> <td>18</td> <td>20</td> <td>28</td> <td>30</td> <td>38</td> <td>40</td>
    <td>48</td> <td>50</td> <td>58</td> <td>60</td> <td>68</td> <td>70</td> <td>78</td> <td>80</td></tr>
  <tr><th> 9</th>
    <td> 9</td> <td>12</td> <td>1B</td> <td>24</td> <td>2D</td> <td>36</td> <td>3F</td> <td>48</td>
    <td>51</td> <td>5A</td> <td>63</td> <td>6C</td> <td>75</td> <td>7D</td> <td>87</td> <td>90</td></tr>
  <tr><th> A</th>
    <td> A</td> <td>14</td> <td>1E</td> <td>28</td> <td>32</td> <td>3C</td> <td>46</td> <td>50</td>
    <td>5A</td> <td>64</td> <td>6E</td> <td>78</td> <td>82</td> <td>8C</td> <td>96</td> <td>A0</td></tr>
  <tr><th> B</th>
    <td> B</td> <td>16</td> <td>21</td> <td>2C</td> <td>37</td> <td>42</td> <td>4D</td> <td>58</td>
    <td>63</td> <td>6E</td> <td>79</td> <td>84</td> <td>8F</td> <td>9A</td> <td>A5</td> <td>B0</td></tr>
  <tr><th> C</th>
    <td> C</td> <td>18</td> <td>24</td> <td>30</td> <td>3C</td> <td>48</td> <td>54</td> <td>60</td>
    <td>6C</td> <td>78</td> <td>84</td> <td>90</td> <td>9C</td> <td>A8</td> <td>B4</td> <td>C0</td></tr>
  <tr><th> D</th>
    <td> D</td> <td>1A</td> <td>27</td> <td>34</td> <td>41</td> <td>4E</td> <td>5B</td> <td>68</td>
    <td>75</td> <td>82</td> <td>8F</td> <td>9C</td> <td>A9</td> <td>B6</td> <td>C3</td> <td>D0</td></tr>
  <tr><th> E</th>
    <td> E</td> <td>1C</td> <td>2A</td> <td>38</td> <td>46</td> <td>54</td> <td>62</td> <td>70</td>
    <td>7E</td> <td>8C</td> <td>9A</td> <td>A8</td> <td>B6</td> <td>C4</td> <td>D2</td> <td>E0</td></tr>
  <tr><th> F</th>
    <td> F</td> <td>1E</td> <td>2D</td> <td>3C</td> <td>4B</td> <td>5A</td> <td>69</td> <td>78</td>
    <td>87</td> <td>96</td> <td>A5</td> <td>B4</td> <td>C3</td> <td>D2</td> <td>E1</td> <td>F0</td></tr>
  <tr><th>10</th>
    <td>10</td> <td>20</td> <td>30</td> <td>40</td> <td>50</td> <td>60</td> <td>70</td> <td>80</td>
    <td>90</td> <td>A0</td> <td>B0</td> <td>C0</td> <td>D0</td> <td>E0</td> <td>F0</td> <td>100</td></tr>
  </table>
</div>

<div class="cblock">
<table>
<tr>
  <td>
  <table class="table-data">
  <caption>123 &times; 456, base ten</caption>
  <col span=5 align="right">
  <tr><td>&times;</td> <th> 100</th>  <th>   20</th> <th>    3</th>	<th> sum</th></tr>
  <tr><th> 400</th>    <td>40000</td> <td> 8000</td> <td> 1200</td> <td> 49200</td></tr>
  <tr><th>  50</th>    <td> 5000</td> <td> 1000</td> <td>  150</td> <td>  6150</td></tr>
  <tr><th>   6</th>    <td>  600</td> <td>  120</td> <td>   18</td> <td>   738</td></tr>
  <tr><th colspan=4>Result</th>                      <th> 56088</th></tr>
  </table></td>

  <td width=32></td>
  <td>
  <table class="table-data">
  <caption>123 &times; 456, base 16</caption>
  <col span=5 align="right">
  <tr><td>&times;</td> <th> 100</th>  <th>   20</th> <th>    3</th>	<th> sum</th></tr>
  <tr><th> 400</th>    <td>40000</td> <td> 8000</td> <td>  C00</td> <td> 48C00</td></tr>
  <tr><th>  50</th>    <td> 5000</td> <td>  A00</td> <td>   F0</td> <td>  5AF0</td></tr>
  <tr><th>   6</th>    <td>  600</td> <td>   c0</td> <td>   12</td> <td>   6D2</td></tr>
  <tr><th colspan=4>Result</th>                      <th> 4EDC2</th></tr>
  </table></td></tr>
</table>
</div>

In both cases, I followed exactly the same procedure: break up the big numbers into powers of *N*, lookup the individual multiplications in the tables and stick the right number of zeros behind them, and then add them all up. You can check with a calculator to see that these numbers are correct. Hexadecimal arithmetic isn't any harder than decimal; it just *seems* harder because they haven't drilled it into your brain at a young age.

I should point out that 4EDC2<sub>sixteen</sub> is actually 323010<sub>ten</sub>, and not 56088<sub>ten</sub>. And it shouldn't be, because the second multiplication was *all* in hex: 123<sub>sixteen</sub> × 456<sub>sixteen</sub>, which actually corresponds to 291<sub>ten</sub> × 1110<sub>ten</sub>. This is why implicit conventions can cause trouble: in different conventions, the *same* number-string can mean completely *different* things. Please keep that in mind. (Incidentally, facts like this also disprove that mental virus known as numerology. Of course, it doesn't in the eyes of its adherents, because that's one of the characteristics of belief systems: belief actually grows as evidence mounts against them, instead of diminishing it.)

#### Look, it floats! {#num-float}

Something that is only possible in a positional system is the use of a floating point. Each numeral in a number-string represents a multiplier for a power of *N*, but why use only positive powers? Negative powers of *x* are successive multiplications of 1/*x*: *x*<sup>−n</sup> = (1/*x*)<sup>n</sup>. For example, π can be broken down like this:

<div class="lblock">
<table class="table-data">
<col span=9 width=32>
<tr align="center">
  <th>exp</th>
  <td> 3</td> <td> 2</td> <td> 1</td> <th> 0</th> <td> -1</td> <td> -2</td> <td> -3</td> <td> -4</td> <td>...</td></tr>
<tr align="center">
  <th>pow</th>
  <td> 1000</td> <td> 100</td> <td> 10</td> <th> 1</th>
  <td> <sup>1</sup>/<sub>10</sub></td>   <td> <sup>1</sup>/<sub>100</sub></td>
  <td> <sup>1</sup>/<sub>1000</sub></td> <td> <sup>1</sup>/<sub>10000</sub></td>
  <td> ...</td></tr>
<tr align="center">
  <th>&pi;</th>
  <td> 0</td> <td> 0</td> <td> 0</td> <th> 3</th> <td> 1</td> <td> 4</td> <td> 1</td> <td> 6</td> <td> ...</td></tr>
</table>
</div>

You can't simply use a number-string for this; you need to know where the negative powers start. This is done with a period: π≈3.1416. At least, the English community uses the period; over here in the Netherlands, people use a comma. That's yet another one of those convention mismatches, one that can *seriously* mess up your spreadsheets.

Since each base-*N* system is equivalent, you can do this just as well in binary. π in binary is:

<div class="lblock">
<table class="table-data">
<col span=9 width=16>
<tr align="center">
  <th>exp</th>
  <td> 3</td> <td> 2</td> <td> 1</td> <th> 0</th> <td> -1</td> <td> -2</td> <td> -3</td> <td> -4</td> <td> ...</td></tr>
<tr align="center">
  <th>pow</th>
  <td> 8</td> <td> 4</td> <td> 2</td> <th> 1</th>
  <td> <sup>1</sup>/<sub>2</sub></td>   <td> <sup>1</sup>/<sub>4</sub></td>
  <td> <sup>1</sup>/<sub>8</sub></td> <td> <sup>1</sup>/<sub>16</sub></td>
  <td> ...</td></tr>
<tr align="center">
  <th>&pi;</th>
  <td> 0</td> <td> 0</td> <td> 1</td> <th> 1</th> <td> 0</td> <td> 0</td> <td> 1</td> <td> 0</td> <td> ...</td></tr>
</table>
</div>

So π in binary is 11.0010<sub>two</sub>. Well, yes and no. Unfortunately, 11.0010<sub>two</sub> is actually 3.1250, not 3.1416. The problem here is that with 4 bits you can only get a precision to the closest 1/16 = 0.0625. For 4 decimals of accuracy you'd need about 12 bits (11.001001000100 ≈ 3.1416). You could also use hex instead of binary, in which case the number is 3.243F<sub>sixteen</sub>.

#### Conversion between bases

You might wonder how I got these conversions. It's actually not that hard: all you have to do is divide by the base number and strip off the remainders until you have nothing left; the string of the remainders is the converted number. Converting decimal 1110 to hex, for example, would go like this:

<div class="lblock">
<table class="table-data rules-cols">
<tr><th> num</th>  <th> / 16</th> <th> %16</th></tr>
<tr><td> 1110</td> <td> 69</td>   <td> 6</td></tr>
<tr><td>   69</td> <td> 4</td>    <td> 5</td></tr>
<tr><td>    4</td> <td> 0</td>    <td> 4</td></tr>
<tr><th>result:</th><td colspan=2>456h</td></tr>
</table>
</div>

This strategy will also work for floating point numbers, but it may be smart to break the number up in an integer and fractional part first. And remember that dividing by a fraction is the same as multiplying by its reciprocal. Grab your calculator and try it.

There are actually a number of different ways you can convert between bases. The one given using divisions is the easiest one to program, but probably also the slowest. This is especially true for the GBA, which has no hardware division. You can read about another strategy in ["Binary to Decimal Conversion in Limited Precision" by Douglas W. Jones](https://homepage.divms.uiowa.edu/~jones/bcd/decimal.html).

#### Scientific notation {#num-sci}

Another thing that a positional system is useful for is what is known as the <dfn>scientific notation</dfn> of numbers. This will help you get rid of all the excess zeros that plague big and large numbers, as well as indicate the number of significant figures. For example, if you look in science books, you might read that the mass of the Earth is 5,974,200,000,000,000,000,000,000 kg. There are two things wrong with this number. First, the value itself is incorrect: it isn't 59742 followed by 20 zeros kilograms, right down to the last digit: that kind of accuracy just isn't possible in physics (with the possible exception of Quantum Mechanics, where theory can be accurate to up to a staggering 14 decimals. That's right, that ‘fuzzy’ stuff actually has the highest degree of accuracy of *all* fields of science). When it comes to planetary masses, the first 3 to 5 numbers may be accurate, the rest is usually junk. The second problem is more obvious: the number is just too damn long to write!

The scientific notation solves both problems. Multiplying with a power of 10 effectively moves the floating point around and thus can rid you of the zeros. The mass of the Earth can then be written concisely as 5.9742·10<sup>24</sup>, that is, 5.9742 times 10 to the power 24. You can also come across the even shorter notation of 5.9742e+24, where the “·10\^” is replaced by an ‘e’ for exponent. Don't misread it as a hexadecimal number. And yes, I am aware that this is a shorthand notation of a shorthand notation. What can I say, math people are lazy bastards. Additionally, this number also indicates that you have 5 significant digits, and any calculation you do afterwards needs to respect that.

Of course, this notation will work for any base number, just remember that conversion between bases require the whole number.

#### It ain't as hard as you think

The concepts laid out in this section may seem difficult, but I assure you they are actually quite easy to understand. All of this stuff is taught in elementary or high school; the only thing is that they only use the decimal system there. Like I said, the workings of the positional system is equivalent for all base numbers, the only difference is that you've had lots and lots of *practice* with the decimal system, and hardly any with the others. If you had memorised the multiplication tables in hex instead of in decimal, you'd have found the latter awkward to use.

## Of bits and bytes {#sec-bits}

Any self-respecting programmer knows that the workings of a computer are all about little switches that can be on or off. This means that computers are more suited to a binary (or maybe hex) representation than a decimal one. Each switch is called a <dfn>bit</dfn>; computer memory is basically a sea of millions upon millions of bits. To make things a little more manageable, bits are often grouped into <dfn>bytes</dfn>. 1 byte = 8 bits is the standard nowadays, but some older systems had 6-, 7-, or 9-bit bytes.

Since *everything* is just 1s and 0s, computers are the best example on the meaning of symbols: it's all about interpretation here. The bits can be used to mean anything: besides switches and numbers you can interpret them as letters, colors, sound, you name it. In this section, I will explain a few ways that you can interpret bits. I will often use a mixture of binary and hex, switching between them for convenience.

### Integer number representations {#ssec-bits-int}

An obvious use of bits would be numbers, especially integers. With 8 bits, you have 2<sup>8</sup>=256 different numbers running from 0 to 1111,1111<sub>two</sub> (FFh in hex and 255 decimal). That's not much, so there are also groupings of 16 bits (10000h or 65536 numbers) and 32 bits (10000:0000h or 4,294,967,296 numbers). In the late 2000s decade, PCs made the transition to 64 bits CPUs; I'm not even going to write down how much that is. The C types for these are `short` (16 bits), `int` or `long` (32 bits), and `long long` (64 bits). The size of an `int` or `long` is actually system dependent, but on a GBA, both are 32 bits.

#### Negative numbers {#bits-int-neg}

That you have *n* bits to represent a number does not necessarily mean that you have to use them for the range \[0, 2<sup>n</sup>−1\], that is, positive integers. What about negative numbers? Well, there are a number of ways you can represent negative numbers. A very simple way could be to use one of the bits as a <dfn>sign bit</dfn>: 0 for positive numbers and 1 for negative numbers. For example, binary 1000,0001 could be ‘−1’. Some systems use this, but the GBA doesn't, because there's a smarter way.

Let's bring out our odometers again. In an three-digit odometer, you could go from 0 to 999. Forget what a three-digit odometer says about the quality of the car, just focus on the numbers. At 999, *every* digit will roll over and you'll be back at 0 again. You could also argue that the number *before* 0 is 999. In other words, '999' would be the representation of −1. You could split the full one thousand range into one half for the first positive five hundred (0 to 499), and the other for the first negative five hundred (−500 to −1), as counting backward from 0, using the roll-over. This type of numbering is called be <dfn>ten's complement</dfn>. The table below shows how this works for 3 digits.

<div class="lblock">
<table id="tbl:10cmpl" class="table-data">
<caption align="bottom">
  <b>*@tbl:10cmpl</b>: ten's complement for 3 digits
</caption>
<tbody align="center">
<tr><th>Number</th>
  <td>-500</td> <td>-499</td> <td>-498</td> <td> ...</td>  <td>-2</td>   <td>-1</td>
  <td>0</td>    <td>1</td>    <td> ...</td> <td> 497</td>  <td> 498</td> <td> 499</td></tr>

<tr><th>Representation</th>
  <td> 500</td> <td> 501</td>  <td> 502</td> <td> ...</td> <td> 998</td> <td> 999</td>
  <td> 0</td>   <td> 1</td>    <td> ...</td> <td> 497</td> <td> 498</td> <td> 499</td></tr>
</tbody>
</table>
</div>

That's the practice, now the theory behind it. Negative numbers are deeply tied to subtraction; you could almost consider it part of their definition. Basically, for every number *x*, the following should be true:

<table id="eq:sum-xeqmx">
<tr>
  <td class="eqnrcell">({!@eq:sum-xeqmx})</td>
  <td class="eqcell">
0 = *x* + (−*x*)
  </td>
</tr>
</table>

This could be considered zeros' complement: the number (−*x*) is the number you need to add to *x* to get 0. In ten's complement, they need to add up to 10 or a power of 10. In our odometer, 1000 will have the same representation as 0, and counting back from one thousand will be the same as counting back from zero. However, you *must* know the number of digits beforehand; otherwise it won't work. The actual representation of -*x* using *m* digits, can be derived as follows:

<!--
\begin{matrix}
0 & = & x+(-x) \\
\cong & & \cong \\
10^m & = & x+(-x) \\
(10^m-1)-x+1 & = & -x
\end{matrix}
-->
<table id="eq:cmpl-def">
<tr>
  <td class="eqnrcell">(!@eq:cmpl-def)</td>
  <td class="eqcell">
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle displaystyle="true" scriptlevel="0">
    <mrow data-mjx-texclass="ORD">
      <mtable rowspacing=".5em" columnspacing="1em" displaystyle="true">
        <mtr>
          <mtd>
            <mtable columnspacing="1em" rowspacing="4pt">
              <mtr>
                <mtd>
                  <mn>0</mn>
                </mtd>
                <mtd>
                  <mo>=</mo>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>+</mo>
                  <mo stretchy="false">(</mo>
                  <mo>&#x2212;</mo>
                  <mi>x</mi>
                  <mo stretchy="false">)</mo>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mo>&#x2245;</mo>
                </mtd>
                <mtd></mtd>
                <mtd>
                  <mo>&#x2245;</mo>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <msup>
                    <mn>10</mn>
                    <mi>m</mi>
                  </msup>
                </mtd>
                <mtd>
                  <mo>=</mo>
                </mtd>
                <mtd>
                  <mi>x</mi>
                  <mo>+</mo>
                  <mo stretchy="false">(</mo>
                  <mo>&#x2212;</mo>
                  <mi>x</mi>
                  <mo stretchy="false">)</mo>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mo stretchy="false">(</mo>
                  <msup>
                    <mn>10</mn>
                    <mi>m</mi>
                  </msup>
                  <mo>&#x2212;</mo>
                  <mn>1</mn>
                  <mo stretchy="false">)</mo>
                  <mo>&#x2212;</mo>
                  <mi>x</mi>
                  <mo>+</mo>
                  <mn>1</mn>
                </mtd>
                <mtd>
                  <mo>=</mo>
                </mtd>
                <mtd>
                  <mo>&#x2212;</mo>
                  <mi>x</mi>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
        </mtr>
      </mtable>
    </mrow>
  </mstyle>
</math>
  </td>
</tr>
</table>

Don't panic, these equations aren't as nasty as they seem. Remember that for *m* digits, the highest number is 10<sup>m</sup>&minus;1. If *m* = 3, then that'd be 999 in decimal, 111 in binary or FFF in hex. This will allow you to do the subtraction by *x* without borrowing. There's more to 10's complement then a way to express negative numbers; it'll also turn subtraction into a form of addition: *subtraction* by *y* is equivalent to *addition* by its 10's complement. That feature was part of the system from the start, and the other schemes of negative number representations don't have that property. Checking this is left as an exercise for the reader.

The binary version of 10's complement is <dfn>two's complement</dfn>. Finding the two's complement of a number is actually easier than in other cases: the subtraction of 10<sup>m</sup>−1 by *x* is just the inversion of all the bits of *x*. Take 76, for example:

<table>
<tr>
  <td class="fill">&nbsp;</td>
  <td class="eqcell">
  <table class="eqtbl" cellpadding=2 cellspacing=0>
  <col align="right">
  <col align="center">
  <col align="left">
  <tr>
    <th>255:</th> <td>1111 1111</td> <td></td></tr>
  <tr>
    <th class="bdrB">76:</th>
	<td class="bdrB">0100 1100</td> 
	<td class="bdrB">&minus;</td></tr>
  <tr>
    <th>179:</th>
    <td>1011 0011</td></tr>
  </table></td></tr>
</table>

The 8bit −76 would be 179+1=180 (10110100<sub>two</sub>) and you will indeed see that 180+76 = 256 = 2<sup>8</sup>, exactly as it should be.

#### Signed is not unsigned {#bits-int-sign}

I've already mentioned this before, but it's important enough to state it again: when using 10's complement, you *must* know the number of digits ahead of time, otherwise you won't know what to subtract *x* from. Most of the time you can remain blissfully ignorant of this fact, but there are a few instances where it really does matter. In C or assembly programming, you have two types of integer numbers: <dfn>signed</dfn> and <dfn>unsigned</dfn>, and only the *signed* types are in two's complement. The difference manifests itself in the interpretation of the most significant bit: in unsigned numbers, it's just another bit. But in signed numbers, it acts as a sign-bit, and as such it needs to be preserved in certain operations as *type-casting* or *shifting*. For example, an 8-bit FF<sub>sixteen</sub> is a signed ‘−1’ or an unsigned ‘255’. When converting to 16 bits, the former should become FFFF<sub>sixteen</sub>, while the latter would remain 00FF<sub>sixteen</sub>. If you ever see stuff go completely bonkers when numbers become negative, this might be why.

Here are a few guidelines for choosing signed or unsigned types. Intrinsically signed types are numbers that have a physical counterpart: position, velocity, that kind of stuff. A key feature of these is that you're supposed to do arithmetic on them. Variables that act as switches are usually unsigned, the bitflags for enabling features on a GBA are primary examples. These usually use logical operations like masking and inverting (see the section on [bit operations](#sec-bitops)). Then there are quantities and counters. These can be either signed or unsigned, but consider starting with signed, then switch to unsigned if you really have to. Again, these are just recommendations, not commandments that will land you in eternal damnation if you break them.

:::note

Unsigned and signed types can behave differently under type casting, comparison and bit-operations. A byte *x* containing FFh could mean a signed −1 or an unsigned 255. In that case:

<div class="lblock">
<table class="table-data">
<tr><td>FFh</td>	<th>signed</th> 		<th>unsigned</th></tr>
<tr><th>comparison x&lt;0</th>
  <td>true</td> <td> false</td></tr>
<tr><th>conversion to 16 bit</th>
  <td>FFFFh (-1)</td> <td> 00FFh (255)</td></tr>
<tr><th>shift right by 1</th>
  <td>FFh (-1)</td> <td> 7Fh (127)</td></tr>
</table>
</div>

:::

### Characters {#ssec-bits-char}

No, I'm not talking about GBA-tiles, but the letter variety (this possible confusion is why I'm not fond of the name ‘character’ for tiles). For everyday purposes you would need 2×26 letters, 10 numerals, a bunch of punctuation signs and maybe a few extra things on the side: that's about 70 characters at least, so you'd need 7 bits to indicate them all (6 would only allow 2<sup>6</sup>=64 characters). Better make it 8 bits for possible future expansion, and because it's a nice round number. In binary that is. That's part of the reason why the byte is a handy grouping: one character per byte.

#### ASCII

Knowing which characters you need is only part of the story: you also need to assign them to certain numbers. The order of any alphabet is, again, just a convention (well, there are orders that are more logical than others, see Tolkien's *Tengwar*, “The Lord of the Rings”, Appendix E, but the Latin alphabet is completely random). One possible arrangement is to take a normal keyboard and work your way through the keys. Fortunately, this isn't the standard. The common code for character assignments is <dfn>ASCII</dfn>: *American Standard Code for Information Interchange*.

The lower 128 characters of ASCII are given below. The first 32 are control codes. Only a few of these are still of any importance: 08h (backspace, `\b`), 09h (tab, `\t`), 0Ah (Line Feed, `\n`) and 0Dh (Carriage Return, `\r`). If you have ever downloaded text files from Unix/Linux servers, you might have noticed that all the line breaks have been removed: this is because CP/M, MS-DOS, and Windows use CRLF (`\r\n`) as the line break, while Unix environments just use the line feed.

The real characters start at 20h, the space character. Note how the numeric, uppercase and lowercase characters are located sequentially and in a logical fashion. Numbers start at 30h, uppercase at 41h, lowercase at 61h. The alphabetical order of the letters makes for easy alphabetizing, although I should point out that the 32 difference between uppercase and lowercase may cause problems.

The ASCII set also has an upper 128 characters, but these can be different for different language settings. Normally, these will include accented characters that are frequent in non-English languages. In a DOS environment, they also contained a number of purely graphical characters for borders and the like. ASCII isn't the only character set available. Chinese and Japanese languages usually use the 16bit <dfn>Unicode</dfn>, as the 8bit ASCII simply isn't sufficient for thousands of characters. ASCII is basically a subset of Unicode.

The C type for the character is called <dfn>char</dfn>. A **char** is actually a *signed* 8bit integer. I mention this because I distinctly remember being sent on a long bughunt long ago because of this little fact. To be perfectly honest, I think that the default signing of the char-type is actually platform dependent, so consider yourself warned.

<div class="cblock">
<table id="tbl:ascii" class="table-data">
<caption align="bottom">
  <b>*@tbl:ascii</b>: ASCII 0-127
</caption>
<tr><td>
  <table class="border-none"><tr><th>dec</th> <th>hex</th> <th>Char</th></tr>
    <tr><td> 0</td> <td>00h</td> <th>NUL</th></tr>
    <tr><td> 1</td> <td>01h</td> <th></th></tr>
    <tr><td> 2</td> <td>02h</td> <th></th></tr>    <tr><td> 3</td> <td>03h</td> <th></th></tr>
    <tr><td> 4</td> <td>04h</td> <th></th></tr>    <tr><td> 5</td> <td>05h</td> <th></th></tr>
    <tr><td> 6</td> <td>06h</td> <th>ACK</th></tr>  <tr><td> 7</td> <td>07h</td> <th>BELL</th></tr>
    <tr><td> 8</td> <td>08h</td> <th>BS</th></tr>   <tr><td> 9</td> <td>09h</td> <th>HT</th></tr>
    <tr><td>10</td> <td>0Ah</td> <th>LF</th></tr>
    <tr><td>11</td> <td>0Bh</td> <th></th></tr>
    <tr><td>12</td> <td>0Ch</td> <th>FF</th></tr>   <tr><td>13</td> <td>0Dh</td> <th>CR</th></tr>
    <tr><td>14</td> <td>0Eh</td> <th></th></tr>    <tr><td>15</td> <td>0Fh</td> <th></th></tr>
    <tr><td>16</td> <td>10h</td> <th></th></tr>    <tr><td>17</td> <td>11h</td> <th></th></tr>
    <tr><td>18</td> <td>12h</td> <th></th></tr>    <tr><td>19</td> <td>13h</td> <th></th></tr>
    <tr><td>20</td> <td>14h</td> <th></th></tr>    <tr><td>21</td> <td>15h</td> <th></th></tr>
    <tr><td>22</td> <td>16h</td> <th></th></tr>    <tr><td>23</td> <td>17h</td> <th></th></tr>
    <tr><td>24</td> <td>18h</td> <th></th></tr>    <tr><td>25</td> <td>19h</td> <th></th></tr>
    <tr><td>26</td> <td>1Ah</td> <th>^Z</th></tr>   <tr><td>27</td> <td>1Bh</td> <th>ESC</th></tr>
    <tr><td>28</td> <td>1Ch</td> <th></th></tr>    <tr><td>29</td> <td>1Dh</td> <th></th></tr>
    <tr><td>30</td> <td>1Eh</td> <th></th></tr>    <tr><td>31</td> <td>1Fh</td> <th></th></tr>
  </table></td>
<td>
  <table class="border-none"><tr><th>dec</th> <th>hex</th> <th>Char</th></tr>
    <tr><td>32</td> <td>20h</td> <th>sp</th></tr>   <tr><td>33</td> <td>21h</td> <th>!</th></tr>
    <tr><td>34</td> <td>22h</td> <th>"</th></tr>    <tr><td>35</td> <td>23h</td> <th>#</th></tr>
    <tr><td>36</td> <td>24h</td> <th>$</th></tr>    <tr><td>37</td> <td>25h</td> <th>%</th></tr>
    <tr><td>38</td> <td>26h</td> <th>&amp;</th></tr><tr><td>39</td> <td>27h</td> <th>'</th></tr>
    <tr><td>40</td> <td>28h</td> <th>(</th></tr>    <tr><td>41</td> <td>29h</td> <th>)</th></tr>
    <tr><td>42</td> <td>2Ah</td> <th>*</th></tr>    <tr><td>43</td> <td>2Bh</td> <th>+</th></tr>
    <tr><td>44</td> <td>2Ch</td> <th>,</th></tr>    <tr><td>45</td> <td>2Dh</td> <th>-</th></tr>
    <tr><td>46</td> <td>2Eh</td> <th>.</th></tr>    <tr><td>47</td> <td>2Fh</td> <th>/</th></tr>
    <tr><td>48</td> <td>30h</td> <th>0</th></tr>    <tr><td>49</td> <td>31h</td> <th>1</th></tr>
    <tr><td>50</td> <td>32h</td> <th>2</th></tr>    <tr><td>51</td> <td>33h</td> <th>3</th></tr>
    <tr><td>52</td> <td>34h</td> <th>4</th></tr>    <tr><td>53</td> <td>35h</td> <th>5</th></tr>
    <tr><td>54</td> <td>36h</td> <th>6</th></tr>    <tr><td>55</td> <td>37h</td> <th>7</th></tr>
    <tr><td>56</td> <td>38h</td> <th>8</th></tr>    <tr><td>57</td> <td>39h</td> <th>9</th></tr>
    <tr><td>58</td> <td>3Ah</td> <th>:</th></tr>    <tr><td>59</td> <td>3Bh</td> <th>;</th></tr>
    <tr><td>60</td> <td>3Ch</td> <th>&lt;</th></tr> <tr><td>61</td> <td>3Dh</td> <th>=</th></tr>
    <tr><td>62</td> <td>3Eh</td> <th>&gt;</th></tr> <tr><td>63</td> <td>3Fh</td> <th>?</th></tr>
  </table></td>
<td>
  <table class="border-none"><tr><th>dec</th> <th>hex</th> <th>Char</th></tr>
    <tr><td>64</td> <td>40h</td> <th>@</th></tr>    <tr><td>65</td> <td>41h</td> <th>A</th></tr>
    <tr><td>66</td> <td>42h</td> <th>B</th></tr>    <tr><td>67</td> <td>43h</td> <th>C</th></tr>
    <tr><td>68</td> <td>44h</td> <th>D</th></tr>    <tr><td>69</td> <td>45h</td> <th>E</th></tr>
    <tr><td>70</td> <td>46h</td> <th>F</th></tr>    <tr><td>71</td> <td>47h</td> <th>G</th></tr>
    <tr><td>72</td> <td>48h</td> <th>H</th></tr>    <tr><td>73</td> <td>49h</td> <th>I</th></tr>
    <tr><td>74</td> <td>4Ah</td> <th>J</th></tr>    <tr><td>75</td> <td>4Bh</td> <th>K</th></tr>
    <tr><td>76</td> <td>4Ch</td> <th>L</th></tr>    <tr><td>77</td> <td>4Dh</td> <th>M</th></tr>
    <tr><td>78</td> <td>4Eh</td> <th>N</th></tr>    <tr><td>79</td> <td>4Fh</td> <th>O</th></tr>
    <tr><td>80</td> <td>50h</td> <th>P</th></tr>    <tr><td>81</td> <td>51h</td> <th>Q</th></tr>
    <tr><td>82</td> <td>52h</td> <th>R</th></tr>    <tr><td>83</td> <td>53h</td> <th>S</th></tr>
    <tr><td>84</td> <td>54h</td> <th>T</th></tr>    <tr><td>85</td> <td>55h</td> <th>U</th></tr>
    <tr><td>86</td> <td>56h</td> <th>V</th></tr>    <tr><td>87</td> <td>57h</td> <th>W</th></tr>
    <tr><td>88</td> <td>58h</td> <th>X</th></tr>    <tr><td>89</td> <td>59h</td> <th>Y</th></tr>
    <tr><td>90</td> <td>5Ah</td> <th>Z</th></tr>    <tr><td>91</td> <td>5Bh</td> <th>[</th></tr>
    <tr><td>92</td> <td>5Ch</td> <th>\</th></tr>    <tr><td>93</td> <td>5Dh</td> <th>]</th></tr>
    <tr><td>94</td> <td>5Eh</td> <th>^</th></tr>    <tr><td>95</td> <td>5Fh</td> <th>_</th></tr>
  </table></td>
<td>
  <table class="border-none"><tr><th>dec</th> <th>hex</th> <th>Char</th></tr>
    <tr><td>96</td> <td>60h</td> <th>`</th></tr>    <tr><td>97</td> <td>61h</td> <th>a</th></tr>
    <tr><td>98</td> <td>62h</td> <th>b</th></tr>    <tr><td>99</td> <td>63h</td> <th>c</th></tr>
    <tr><td>100</td> <td>64h</td> <th>d</th></tr>    <tr><td>101</td> <td>65h</td> <th>e</th></tr>
    <tr><td>102</td> <td>66h</td> <th>f</th></tr>    <tr><td>103</td> <td>67h</td> <th>g</th></tr>
    <tr><td>104</td> <td>68h</td> <th>h</th></tr>    <tr><td>105</td> <td>69h</td> <th>i</th></tr>
    <tr><td>106</td> <td>6Ah</td> <th>j</th></tr>    <tr><td>107</td> <td>6Bh</td> <th>k</th></tr>
    <tr><td>108</td> <td>6Ch</td> <th>l</th></tr>    <tr><td>109</td> <td>6Dh</td> <th>m</th></tr>
    <tr><td>110</td> <td>6Eh</td> <th>n</th></tr>    <tr><td>111</td> <td>6Fh</td> <th>o</th></tr>
    <tr><td>112</td> <td>70h</td> <th>p</th></tr>    <tr><td>113</td> <td>71h</td> <th>q</th></tr>
    <tr><td>114</td> <td>72h</td> <th>r</th></tr>    <tr><td>115</td> <td>73h</td> <th>s</th></tr>
    <tr><td>116</td> <td>74h</td> <th>t</th></tr>    <tr><td>117</td> <td>75h</td> <th>u</th></tr>
    <tr><td>118</td> <td>76h</td> <th>v</th></tr>    <tr><td>119</td> <td>77h</td> <th>w</th></tr>
    <tr><td>120</td> <td>78h</td> <th>x</th></tr>    <tr><td>121</td> <td>79h</td> <th>y</th></tr>
    <tr><td>122</td> <td>7Ah</td> <th>z</th></tr>    <tr><td>123</td> <td>7Bh</td> <th>{</th></tr>
    <tr><td>124</td> <td>7Ch</td> <th>|</th></tr>    <tr><td>125</td> <td>7Dh</td> <th>}</th></tr>
    <tr><td>126</td> <td>7Eh</td> <th>~</th></tr>    <tr><td>127</td> <td>7Fh</td> <th>DEL</th></tr>
  </table></td></tr>
</table>
</div>

### IEEE(k)! Floating points {#ssec-bits-float}

The last of the most common types is the floating point. Having, say, 32bits for a number is nice and all, but it still means you are limited to around 4 billion characters. This may seem like a big number, but we've already seen numbers that are much bigger. The floating-point types provide a solution, using the scientific notation in binary. I already described [floating point](#num-float) numbers (even in binary), as well as the [scientific notation](#num-sci), so I won't repeat how they work.

Describing floating-point numbers on a computer is done according to the <dfn>IEEE/ANSI</dfn> standard (Institute of Electrical and Electronic Engineers / American National Standards Institute). The floating-point format consists of 3 parts, a sign bit *s*, an exponent *e* and a fractional part *f*. The following table and equation is the formatting and meaning of a normal, 32bit float

<div class="reg">
<table class="table-reg" id="tbl-float-fmt"
  border=1 frame=void cellpadding=4 cellspacing=0>
<caption class="reg">
  IEEE format for 32bit float
</caption>
<tr class="bits">
	<td>1F</td><td>1E 1D 1C 1B 1A 19 18 17</td>
	<td>16 15 14 13 12 11 10 F E D C B A 9 8 7 6 5 4 3 2 1 0</td></tr>
<tr class="bf">
  <td class="rclr2">s</td>
  <td class="rclr1">e</td>
  <td class="rclr0">f</td></tr>
</table>
<br>

<table class="table-reg-vert">
  <col class="bits" width=40>
  <col class="bf" width="8%">
  <col class="def">
<tr align="left"><th>bits</th><th>name</th><th>&nbsp;</th><th>description</th></tr>
<tbody valign="top">
<tr class="bg0">	
  <td>00-16</td><td class="rclr0">f</td>
  <td>&nbsp;</td>
  <td><b>Fractional</b> part (23 bits)</td></tr>
<tr class="bg1">	
  <td>17-1E</td><td class="rclr1">e</td>
  <td>&nbsp;</td>
  <td><b>Exponent</b> (8 bits)</td></tr>
<tr class="bg0">	
  <td>1F</td><td class="rclr2">s</td>
  <td>&nbsp;</td>
  <td><b>Sign</b> bit.</td></tr>
</tbody>
</table>
</div>

<!--
x=(-1)^s \cdot 1.f \cdot 2^{e-127}
-->
<table id="eq:float">
<tr>
  <td class="eqnrcell">(!@eq:float)</td>
  <td class="eqcell">
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle displaystyle="true" scriptlevel="0">
    <mrow data-mjx-texclass="ORD">
      <mtable rowspacing=".5em" columnspacing="1em" displaystyle="true">
        <mtr>
          <mtd>
            <mi>x</mi>
            <mo>=</mo>
            <mo stretchy="false">(</mo>
            <mo>&#x2212;</mo>
            <mn>1</mn>
            <msup>
              <mo stretchy="false">)</mo>
              <mi>s</mi>
            </msup>
            <mo>&#x22C5;</mo>
            <mn>1.</mn>
            <mi>f</mi>
            <mo>&#x22C5;</mo>
            <msup>
              <mn>2</mn>
              <mrow data-mjx-texclass="ORD">
                <mi>e</mi>
                <mo>&#x2212;</mo>
                <mn>127</mn>
              </mrow>
            </msup>
          </mtd>
        </mtr>
      </mtable>
    </mrow>
  </mstyle>
</math>
  </td>
</tr>
</table>

Note that unlike signed integers, there *is* a real sign bit this time. Furthermore, the number always starts with 1, and the fractional part *f* really is the fractional part of the number. This makes sense, because sense, since if it weren't, you can always move the point around until you get a single 1 before the point. The exponent is subtracted by 127 to allow for negative powers (similar, but not exactly like you'd get in a 2s' complement number). Two examples:

<div class="lblock">
<table class="table-data">
<tr align="center"><th>x</th> <th>s</th> <th> e</th> <th> f</th></tr>
<tr><th>1.0</th>  <td>0</td> <td>01111111</td> <td> 000 0000 0000 0000 0000 0000</td></tr>
<tr><th>&minus;1.0</th> <td>1</td> <td>01111111</td> <td> 000 0000 0000 0000 0000 0000</td></tr>
</table>
</div>

Eq 4 will hold for the usual causes, but there are a few exceptions to this rule.

-   If **e = f = 0**, then *x* = 0. Note that the sign-bit can still be set to indicate a left-limit to zero.
-   If **e = 0** and **f ≠ 0**, then the number is too small to be normalized, *x* = (−1)<sup>s</sup> × 0.*f* × 2<sup>−127</sup>
-   If **e = 255** and **f = 0**, then the *x* = +∞ or *x*= −∞
-   If **e = 255** and **f ≠ 0**, then *x* = NaN, or *Not a Number*. √−1 would be NaN, for example.

The 32bit **float** has a 23bit fractional part, meaning 24 bits of precision. Each 10 bits mean roughly one decimal, so that 24 bits give around 7 decimals of precision, which may or may not be enough for your purposes. If you need more, there are also the 8 byte **double** and and 10 byte **long double** types, which have more exponent and fractional bits.



As you can probably tell, the floating-point format isn't nearly as easy to understand as an integer. Both arithmetic and int-float conversion is tricky. This isn't just for us humans, but computers can have a hard time with them too. PCs usually have a separate floating-point unit (FPU) for just these numbers. The GBA, however, does not. As such, the use of floating-point numbers is *strongly* discouraged on this system. So does that mean that, if we want to use fractions and decimals and such, we're screwed? No, the solution to this particular problem is called fixed-point math, and I'll explain that [here](fixed.html).

### AAaagghhh! The endians are coming! {#ssec-bits-endian}

There is one convention I have completely overlooked throughout this chapter: <dfn>endianness</dfn>. This is about the reading order numbers, bits and bytes. I have always just assumed that in a number, the *left*most digit is the most significant number, that is, the highest power of *N*. So 1025 is read as one thousand twenty-five. That's <dfn>big-endian</dfn>, so named because the big-end (the highest power) goes first. There is also <dfn>little-endian</dfn>, in which the little-end (lowest power) goes first. In that case, 1025 would be read as five thousand two hundred and one. Once again, it's a trivial convention, but it matters greatly which one you use. Both have their merits: speech is usually big-endian and our number system reflects that (except in a few countries which place the ones before the tens (five and twenty), which can be quite confusing). Arithmetic, however, usually starts at the little-end, as do URLs.

Computer endianness plays a part in two areas: bit-order in a byte and byte-order in a multi-byte type such as an int. Since the byte is usually the smallest chunk you can handle, the bit-order is usually of little concern. As a simple example, look at the int 0x11223344. This will be stored differently on different systems, see the table below. Try to think of what would happen if you save this in a file and then transfer that to a computer with a different endian-scheme.

<div class="lblock">
<table id="tbl:endian" class="table-data" width=30%>
<caption align="bottom">
  <b>*@tbl:endian</b>: storing 0x11223344
</caption>
<col span=5 align="center">
<tr><th>memory</th> <th> 00</th> <th> 01</th> <th> 02</th> <th> 03</th></tr>
<tr><th>big</th>    <td> 11</td> <td> 22</td> <td> 33</td> <td> 44</td></tr>
<tr><th>little</th> <td> 44</td> <td> 33</td> <td> 22</td> <td> 11</td></tr>
</table>
</div>

So what should we use then? Well, that's just it: there is no real answer. A benefit of big-endian is that if we see a memory dump, the numbers will be in the human reading-order. On the little-endian side, lower powers are in lower memory, which makes more sense mathematically. Additionally, when you have a 16bit integer *x* = 0x0012, when you cast its address to a 8bit pointer, the value will be preserved which, personally, I think is a good thing.

```c
  u8 *pc;
  short i= 0x0012;
  pc= (u8*)&i;
  // little endian: *pc = 0x12, fine
  //    big endian: *pc = 0x00, whups
```

There is actually one place where you can see the bits-in-byte order: bitmaps. In particular, bitmaps with a bit depth less than 8. A byte in a 4bpp bitmap will represent two pixels. In a BMP, the high-nybbles are the even pixels and low-nybbles the odd ones. GBA graphics work exactly the other way around. One could say that BMP bits are big-endian and GBA bits are little-endian (*bytes*, however, are little-endian on both PCs and GBA). Another endianness-related thing about bitmaps is the color order, RGB (red-green-blue), or BGR (blue-green-red). There are so many pitfalls here that I don't even want to get into this.

Interestingly, there's one other field where endianness mucks things up: dates. In Europe we use a little-endian scheme: day-month-year. China, Japan, and the ISO 8601 standard use big-endian dates: year-month-day. And then there's the American English scheme, which just had to make things difficult for themselves by using a month-day-year scheme. This could be called middle endian, I suppose.

In the end it's not a matter of which is ‘better’, but rather of which system you're working on. PCs and the GBA are little-endian; I hear that PowerPC Macs and a lot of other RISC chips are big-endian (but I may be wrong here). Don't get dragged into any [holy wars](https://www.rfc-editor.org/ien/ien137.txt) over this, just be aware that the different schemes exist and be careful when porting code.

## Bit operations {#sec-bitops}

As the name implies, bit operations (bit-ops) work at the individual bit level and are therefore the lowest operations you can think of. Most Real World applications have little need for bit-fiddling and therefore use bit-ops sparingly, if at all. A good number of programming languages don't even have them. Assembly and C (and Java) belong to the ones that do, but if you look at course books, bit operations are usually moved to the back pages (yes, I am aware that I'm doing this too, but remember that Tonc isn't meant as a general programming tutorial; you should know this stuff already. Most of it, anyway). As GBA programming is done very close to the hardware, with effects taking place depending on whether individual bits are set (1) or clear (0), a good understanding of bit operations is *essential*!

The basic list of bit-ops is: OR, AND, NOT, XOR, shift left/right, rotate left/right. That's 8 operations, though someone proficient with Occam's Razor could cut this list down to 5, perhaps even four items. Of these, only OR, AND and XOR are ‘true’ bit operations: they can be used to change the value of a single bit. The rest change all the bits of a variable.

### True bitwise bit operations {#ssec-bitops-true}

There are 3 bitwise operators: OR ( (inclusive or, symbol ‘|’), AND (symbol ‘\&’) and XOR (exclusive or, symbol ‘\^’) ). These are binary operators, as in ‘taking two arguments as their inputs’. They're called <dfn>bitwise</dfn> operators because that the *n*th bit of the result is only affected by the *n*th bits of the operands. AND and OR work pretty much as their logical counterparts (&& and \|\|). In *c*=*a*&*b*, a bit in *c* will be `1` only if that bit is `1` in both *a* *and* *b*. For OR, the *a*-bit *or* *b*-bit (or both) must be `1`. XOR doesn't have a logical counterpart, but it is more closely linked to the Real Word definition of ‘or’: XOR is `1` if *either* the *a*-bit *or* the *b*-bit is `1` (but not both).

There is a fourth operation that is often included in this group, namely NOT (ones' complement, symbol ‘\~’). NOT is a unary operator, and inverts all bits of the operand, which is basically XORring with −1 (which is all `1`s in binary). The bitwise NOT is similar to the logical not (‘!’). There is an important difference between the logical operations (‘&&’, ‘\|\|’ and ‘!’) and their bitwise counterparts (‘&’, ‘\|’ , ‘\~’), try not to confuse them.

What these four operations do is usually written down in truth tables, which list all possible input combinations and their results. Note that the truth tables look at each bit individually, not the variable as a whole, even though the operators themselves always act on variables. Table 8 shows examples of these operators on bytes 0Fh and 35h.

<div class="lblock">
<table id="tbl:bitops-truth">
<caption align="bottom">
  <b>*@tbl:bitops-truth</b>: bit operations
</caption>
  <tr valign="top"><td>
    <table class="table-data rules-groups">
    <colgroup align="center"></colgroup>
    <colgroup align="center"></colgroup>
    <colgroup align="center"></colgroup>
    <colgroup align="center"></colgroup>
    <thead>
      <tr><th>a b</th> <th> a&amp;b</th> <th> a|b</th> <th> a^b</th></tr></thead>
    <tbody>
      <tr><td>0 0</td> <td> 0</td> <td> 0</td> <td> 0</td></tr>
      <tr><td>0 1</td> <td> 0</td> <td> 1</td> <td> 1</td></tr>
      <tr><td>1 0</td> <td> 0</td> <td> 1</td> <td> 1</td></tr>
      <tr><td>1 1</td> <td> 1</td> <td> 1</td> <td> 0</td></tr></tbody>
    </table></td>
  <td width=32></td>
  <td>
    <table class="table-data rules-groups">
    <colgroup align="center"></colgroup>
    <colgroup align="center"></colgroup>
    <thead>
	  <tr><th> a</th> <th> ~a</th></tr></thead>
    <tbody>
      <tr><td> 0</td> <td> 1</td></tr>
      <tr><td> 1</td> <td> 0</td></tr></tbody>
    </table></td></tr>
</table> <!-- /frame -->
</div>

<div class="lblock">

<!-- frame for masked results -->
<table id="tbl:bitops-eg">
<caption>
  <b>{*@tbl:bitops-eg}a</b>: bit-ops examples
</caption>
  <col span=4 width=144>
  <tr valign="bottom"><td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <tr><th align="center" colspan=3>AND</th></tr>
    <tr>
	  <th><code>0Fh</code></th>
	  <td><code>0000<font color=blue><b>1111</b></font></code></td></tr>
    <tr>
	  <th class="bdrB"><code>35h</code>&nbsp;</th>
	  <td class="bdrB"><code>00110101</code>&nbsp;</td>
	  <td class="bdrB"> &amp;</td></tr>
    <tr>
	  <th><code>05h</code></th>
	  <td><code><font color=red><b>0000</b></font>0101</code></td></tr>
  </table></td>
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <tr><th align="center" colspan=3>OR</th></tr>
    <tr>
	  <th><code>0Fh</code></th>
	  <td><code>0000<font color=blue><b>1111</b></font></code></td></tr>
    <tr>
	  <th class="bdrB"><code>35h</code>&nbsp;</th>
	  <td class="bdrB"><code>00110101</code>&nbsp;</td>
	  <td class="bdrB"> |</td></tr>
    <tr>
	  <th><code>3Fh</code></th>
	  <td><code>0011<font color=red><b>1111</b></font></code></td></tr>
  </table></td>
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <tr><th align="center" colspan=3>XOR</th></tr>
    <tr>
	  <th><code>0Fh</code></th>
	  <td><code>0000<font color=blue><b>1111</b></font></code></td></tr>
    <tr>
	  <th class="bdrB"><code>35h</code>&nbsp;</th>
	  <td class="bdrB"><code>00110101</code>&nbsp;</td>
	  <td class="bdrB"> ^</td></tr>
    <tr>
	  <th><code>3Ah</code></th>
	  <td><code>0011<font color=red><b>1010</b></font></code></td></tr>
  </table></td>
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <tr><th align="center" colspan=3>NOT</th></tr>
    <tr><td>&nbsp;</td></tr>
    <tr>
	  <th class="bdrB"><code>0Fh</code>&nbsp;</th>
	  <td class="bdrB"><code>00001111</code>&nbsp;</td>
	  <td class="bdrB"> ~</td></tr>
    <tr>
	  <th><code>F0h</code></th>
	  <td><code><font color=red><b>11110000</b></font></code></td></tr>
  </table></td></tr>
</table>  <!-- /frame for masked results -->
</div>

I hope you've noticed that some of the bits were colored. Yes, there was a point to this. Knowing what the bit-ops do is one thing; knowing how to *use* them is another. A bit is a binary switch, and there are four things you can do to a switch: leave it alone, flip it, turn it on, and turn it off. In other words, you can:

-   **keep** the current state,
-   **toggle** it (0→1, 1→0),
-   **set** it (*x*→1), and
-   **clear** it (*x*→0)

If you look at the truth tables and the examples, you may already see how this can work. OR, AND, XOR are binary operators, and you can think of the two operands as a source variable *s* and a <dfn>mask</dfn> variable *m* which tells you which of the bits are affected. In table 8a I used *s*=35h and *m*=0Fh; the mask consists of the set bits (in blue), the red bits were the ones that were affected. If you examine the table, you'll see that an OR sets bits, a XOR toggles it and an AND keeps bits (i.e., clears the unmasked bits). To clear the masked bits, you'd need to invert the mask first, so that would be an *s* AND NOT *m* operation. Note that the first three are commutative ( *s* OP *m* = *m* OP *s* ), but the last one isn't. This masking interpretation of the bit operations is very useful, since you'll often be using them to change the bits of certain registers in just this way, using C's assignment operators like '\|='.

<div class="lblock">

<!-- frame for masked results -->
<table>
<caption align="bottom">
  <b>{*@tbl:bitops-eg}b</b>: bit-ops examples encore,
  using source <i>s</i>=35h and mask <i>m</i>=0Fh
</caption>
<col span=4 width=144>
<tr valign="bottom">
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <caption><b>AND (keep bits)</b><br> <i>s &amp; m</i></caption>
    <tr>
	  <th><code>35h</code>&nbsp;</th>
	  <td><code>00110101</code>&nbsp;</td></tr>
    <tr>
	  <th class="bdrB"><code>0Fh</code></th>
	  <td class="bdrB"><code>0000<font color=blue><b>1111</b></font></code></td>
	  <td class="bdrB"> &amp;</td></tr>
    <tr>
	  <th><code>05h</code></th>
	  <td><code><font color=red><b>0000</b></font>0101</code></td></tr>
  </table></td>
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <caption><b>OR (set bits)</b> <br> <i>s | m</i></caption>
    <tr>
	  <th><code>35h</code>&nbsp;</th>
	  <td><code>00110101</code>&nbsp;</td></tr>
    <tr>
	  <th class="bdrB"><code>0Fh</code></th>
	  <td class="bdrB"><code>0000<font color=blue><b>1111</b></font></code></td>
	  <td class="bdrB"> |</td></tr>
    <tr>
	  <th><code>3Fh</code></th>
	  <td><code>0011<font color=red><b>1111</b></font></code></td></tr>
  </table></td>
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <caption><b>XOR (flip bits)</b> <br> <i>s ^ m</i></caption>
    <tr>
	  <th><code>35h</code>&nbsp;</th>
	  <td><code>00110101</code>&nbsp;</td></tr>
    <tr>
	  <th class="bdrB"><code>0Fh</code></th>
	  <td class="bdrB"><code>0000<font color=blue><b>1111</b></font></code></td>
	  <td class="bdrB"> ^</td></tr>
    <tr>
	  <th><code>3Ah</code></th>
	  <td><code>0011<font color=red><b>1010</b></font></code></td></tr>
  </table></td>
  <td>
  <table class="eqtbl" cellpadding=2 cellspacing=0>
    <caption><b>AND NOT (clear bits)</b> <br> <i>s &amp;~ m</i></caption>
    <tr>
	  <th><code>&nbsp;35h</code>&nbsp;</th>
	  <td><code>00110101</code>&nbsp;</td></tr>
    <tr>
	  <th class="bdrB"><code>~0Fh</code></th>
	  <td class="bdrB"><code>1111<font color=blue><b>0000</b></font></code></td>
	  <td class="bdrB"> &amp;</td></tr>
    <tr>
	  <th><code>&nbsp;30h</code></th>
	  <td><code>0011<font color=red><b>0000</b></font></code></td></tr>
  </table></td></tr>
</table>  <!-- /frame for masked results -->
</div>

### Non-bitwise bit operations {#ssec-bitops-false}

And then there are the shift and rotate operations. In contrast to the earlier operations, these act on a variable as a whole. Each variable is a string of bits and with the shift and rotate operations you can move the bits around. Both have left and right variants and are binary operations, the first operand is the source number, and the second is the amount of bits to move. I'll refer to shift left/right as SHL and SHR and rotate left/right as ROL and ROR for now. These sound like assembly instructions, but they're not. At least, not ARM assembly. Shift left/right have C operators ‘\<\<’ and ‘\>\>’, but there are no C operators for a bit-rotate, although you can construct the effect using shifts. As said, shift and rotate move bits around a variable, in pretty much the way you'd expect:

<div class="lblock">
<table id="tbl:shift" class="table-data rules-groups">
<caption align="bottom"><b>*@tbl:shift</b>: shift / rotate operations on
  byte 35h (<code>00110101</code>)</caption>
<colgroup></colgroup>
<colgroup></colgroup>
<colgroup></colgroup>
<colgroup></colgroup>
<thead>
<tr align="center">
  <th>name</th> <th> symbol</th> <th>example</th> <th> result</th></tr></thead>
<tbody>
<tr>
  <th>shift left</th> <td> SL, &lt;&lt;</td>
  <td> <code>00<font color=red><b>110101</b></font></code> &lt;&lt; 2</td>
  <td> <code><font color=red><b>110101</b></font>00</code>, D4h</td></tr>
<tr>
  <th>shift right</th> <td> SR, &gt;&gt;</td>
  <td> <code>00<font color=red><b>110101</b></font></code> &gt;&gt; 2</td>
  <td> <code>0000<font color=red><b>1101</b></font></code>, 0Dh</td></tr>
<tr>
  <th>rotate left</th> <td> ROL</td>
  <td> <code>00<font color=blue><b>110101</b></font></code> ROL 3</td>
  <td> <code><font color=blue><b>10101</b></font>00<font
    color=blue><b>1</b></font></code>, A9h</td></tr>
<tr>
  <th>rotate right</th> <td> ROR</td>
  <td> <code>00<font color=blue><b>110101</b></font></code> ROR 3</td>
  <td> <code><font color=blue><b>101</b></font>00<font
    color=blue><b>110</b></font></code>, A6h</td></tr></tbody>
</table>
</div>

Shifting has two uses. First of all, you can easily find the *n* bit, or the *n*th power of 2 by using `1<<`*n*. Speaking of powers, shifting basically comes down to adding zeros or removing bits, which is essentially multiplying or dividing by 10. Binary 10, that is. So you could use shifting to quickly multiply or divide by 2. The latter is especially useful, since division is very, very costly on a GBA, while shifting is a one-cycle operation. I can't really thing of a use for rotation right now but I'm sure they're there.

OK, that's what they do in theory. In *practice*, however, there's a lot more to it. One thing that is immediately obvious is that the size of the variable is important. A rotate on an 8bit variable will be very different then a rotate on a 16bit one. There is also the possibility of including the carry bit in the rotation, but that doesn't really matter for the moment because bit rotation is purely an assembly matter, and that's beyond the scope of this page.

What does matter is a few nasty things about shifting. Shift-left isn't much of a problem, unless you shift by more than the amount of bits of the variable. Shift-right, however, has one particular nasty issue for negative numbers. For example, an 8bit −2 is represented in twos' complement by `FEh`. If you shift-right by one, you'd get `7Fh`, which is 128, and not −2/2 = −1. The problem here is that the first bit acts as a sign bit, and should have special significance. When shifting- right, the sign-bit needs to be preserved and extended to the other bits, this will ensure that the result is both negative and represents a division by a power of two. There are actually two right-shift instructions, the *arithmetic* and the *logical* shift right (ASR and LSR); the former extends the sign bit, the latter doesn't. In C, the [signing](numbers.html#bits-int-sign) of the variable type determines which of these instructions is used.

Take the interesting case of the 8bits 80h, which is both the unsigned 128 as the signed −128. A right-shift by 3 should result in 16 and −16, respectively. This would be 10h for the unsigned and F0h for the signed case, and lo and behold, that is exactly what you'd get by sign-bit extension or not.

<div class="lblock">
<table id="tbl:sign" class="table-data">
<caption align="bottom">
  <b>*@tbl:sign</b>: signed and unsigned <code>80h&gt;&gt;3</code>
</caption>
<col span=3 align="center">
<tr><th>type <b>char</b></th><th> unsigned</th> <th> signed</th></tr>
<tr>
  <td><code><font color=blue><b>1</b></font>000 0000</code></td>
  <td>&nbsp;128</td> <td> &minus;128</td></tr>
<tr>
  <td><code>80h&gt;&gt;3</code></td>
  <td> <code>000<font color=red><b>1</b></font> 0000</code></td>
  <td> <code><font color=red><b>1111</b></font> 0000</code></td></tr>
<tr>
  <td>&nbsp;</td><td> 16</td> <td> &minus;16</td></tr>
</table>
</div>

I know this seems like such a small and trivial issue, and indeed, it usually is. But when it isn't, you could be looking at a long bughunt. This isn't limited to just shifting, by the way, *all* bit operations can suffer from this problem.

### Arithmetic with bit operations {#ssec-bitops-arith}

The shift operators can be used to divide and multiply by powers of two. The other bit-ops also have arithmetic interpretations.

For example, a modulo of a power of two basically cuts away the upper bits, which can be done with an AND operation: *x*%2<sup>n</sup> = *x* AND 2<sup>n</sup>−1. For example, *x*%8 = *x*&7.

An OR operation can be used as an addition, but *only* if the affected bits were 0 to start with. F0h \| 01h = F1h, which is the same as F0h+01h. However, F0h \| 11h = F1h too, but F0h+11h is actually 101h. Be careful with this one, and make note of it when you see it in other people's code.

Thanks to [two's''s complement](#bits-int-neg), we can use XOR as a subtraction: (2<sup>n</sup>−1)−*x* = (2<sup>n</sup>−1) XOR *x*. This can be used to reverse the traversal order of loops, for example, which can be useful when you want collision detection with flipped tiles. Yes, it's a bit of a hack, but so what?

```c
int ii, mask;

for(ii=0; ii<8; ii++)
{
    // array direction based on mask
    // mask=0 -> 0,1,2,3,4,5,6,7
    // mask=7 -> 7,6,5,4,3,2,1,0
    ... array[ii^mask] ...
}
```

OR and XOR are only very rarely used in their arithmetic form, but the shifts and AND can be seen with some regularity. This is especially true on a system with no hardware division (like the GBA), in which case division and modulo are expensive operations. That is why powers of two are preferred for sizes and such, the faster bit operations can then be used instead. Fortunately, the compiler is smart enough to optimize, say, division by 8 to a right-shift by 3, so you don't have to write down the bit-op version yourself if you don't want to. Mind you, this will only work if a) the second operand is a constant and b) that constant is a power of two.

<div class="lblock">
<table id="tbl:bitops-arith" class="table-data rules-groups">
<caption align="bottom">
  <b>*@tbl:bitops-arith</b> Arithmetic bit-ops summary
</caption>
<colgroup valign="bottom"></colgroup>
<colgroup align="center" valign="bottom"></colgroup>
<colgroup align="center" valign="bottom"></colgroup>
<thead>
<tr>
  <th>bit-op</th> <th>arithmetic function</th> <th>example</th></tr></thead>
<tbody>
<tr>
  <td>SHL</td>
  <td><i>x</i>&lt;&lt;<i>n</i> 
    = <i>x</i> * 2<sup><i>n</i></sup></td>
  <td><i>x</i>&lt;&lt;3 = <i>x</i> * 8</td></tr>
<tr>
  <td>SHR</td>
  <td><i>x</i>&gt;&gt;<i>n</i> 
    = <i>x</i> / 2<sup><i>n</i></sup></td>
  <td><i>x</i>&gt;&gt;3 = <i>x</i> / 8</td></tr>
<tr>
  <td>AND</td>
  <td><i>x</i>&amp;(2<sup><i>n</i></sup>&minus;1) 
    = <i>x</i> % 2<sup><i>n</i></sup></td>
  <td><i>x</i>&amp;7 = <i>x</i> % 8</td></tr></tbody>
</table>
</div>

And now for my final trick of the day, let's take a closer look at the most basic of arithmetic operations, addition. The addition of 2 bits to be precise, and the truthtable of that can be found in table 12 below. If you've paid attention so far (well done! I didn't think anyone would make it this far <kbd>:P</kbd>), there should be something familiar about the two columns that make up the result. The right column is just *a* XOR *b* and the left column is *a* AND *b*. This means that you can create a 1-bit adder with just an AND and a XOR port, electric components that can be found in any Radio Shack, or its local equivalent. String 8 of these together for an 8-bit adder, and you'll have yourself the foundation of an 8bit computer, cool huh?

<div class="lblock">
<table id="tbl:adder" class="table-data rules-groups" width=20%>
<caption align="bottom">
  <b>*@tbl:adder</b>: 1&minus;bit adder
</caption>
<colgroup align="center"></colgroup>
<colgroup align="center"></colgroup>
<colgroup align="center"></colgroup>
<thead>
  <tr><th>a b</th> <th> a+b</th></tr></thead>
<tbody>
  <tr><td>0 0</td> <td> 00</td></tr>
  <tr><td>0 1</td> <td> 01</td></tr>
  <tr><td>1 0</td> <td> 01</td></tr>
  <tr><td>1 1</td> <td> 10</td></tr></tbody>
</table>
</div>

### Beware of bit operations {#ssec-bitops-caveat}

There are two things you should *always* remember when you're using bit operations. I've already mentioned the first, that they can mess with the sign of the variables. This is only relevant for signed integers, though.

The second problem is concerns the level of precedence of the bit operations. Except for NOT (`~`), the precedence is very low; lower than addition, for example, and even lower than conditional operators in some cases. Your C manual should have a precedence list, so I'll refer you to that for details. In the mean time, be prepared to drown your code in parentheses over this.
