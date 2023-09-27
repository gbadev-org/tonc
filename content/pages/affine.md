Title: The Affine Transformation Matrix
Date: 2003-09-01
Modified: 2023-09-06
Authors: Cearn

# 10. The Affine Transformation Matrix (a.k.a. **P**)

[TOC]

## About this page

As you probably know, the GBA is capable of applying geometric transformations like rotating and/or scaling to sprites and backgrounds. To set them apart from the regular items, the transformable ones are generally referred to as Rot/Scale sprites and backgrounds. The transformations are described by four parameters, `pa`, `pb`, `pc` and `pd`. The locations and exact names differ for sprites and backgrounds but that doesn't matter for now.

There are two ways of interpreting these numbers. The first is to think of each of them as individual offsets to the sprite and background data. This is how the reference documents like [GBATek](http://nocash.emubase.de/gbatek.htm){target="_blank"} and [CowBite Spec](http://www.cs.rit.edu/~tjh8300/CowBite/CowBiteSpec.htm){target="_blank"} describe them. The other way is to see them as the elements of a 2x2 matrix which I will refer to as **P**. This is how pretty much all tutorials describe them. These tutorials also give the following matrix for rotation and scaling:

<math id="eq:incorrect_transform_matrix" class="block">
    <mo>(</mo>
    <mi>{!@eq:incorrect_transform_matrix}</mi>
    <mo>)</mo>
    <mspace width="30px" />
    <mi>𝗣</mi>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><msub><mi>p</mi><mi>a</mi></msub></mtd>
                <mtd><msub><mi>p</mi><mi>b</mi></msub></mtd>
            </mtr>
            <mtr>
                <mtd><msub><mi>p</mi><mi>c</mi></msub></mtd>
                <mtd><msub><mi>p</mi><mi>d</mi></msub></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><msub><mi>s</mi><mi>x</mi></msub><mi>cos</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
                <mtd><msub><mi>s</mi><mi>y</mi></msub><mi>sin</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
            </mtr>
            <mtr>
                <mtd><mo>-</mo><msub><mi>s</mi><mi>x</mi></msub><mi>sin</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
                <mtd><msub><mi>s</mi><mi>y</mi></msub><mi>cos</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
</math>

Now, this is indeed a rotation and scale matrix. Unfortunately, it's also the <span class="rem">wrong one</span>! Or at least, it probably does not do what you'd expect. For example, consider the case with a scaling of <math><msub><mi>s</mi><mi>x</mi></msub></math> = 1.5, <math><msub><mi>s</mi><mi>y</mi></msub></math> = 1.0 and a rotation of α= 45. You'd probably expect something like {@fig:rotatescale}a, but what you'd actually get is {@fig:rotatescale}b. The sprite has rotated, but in the wrong direction, it has shrunk rather than expanded and there's an extra shear as well. Of course, you can always say that you meant for this to happen, but that's probably not quite true.

<div style="display: flex; margin: 20px" markdown>
<div class="cpt" style="width:160px;" markdown>
![](img/affine/metr_rs_good.png){#fig:rotatescale}
**{*@fig:rotatescale}a**: when you say ‘rotate and scale’, you probably expect this…
</div>
<div class="cpt" style="width:160px" markdown>
![](img/affine/metr_rs_bad.png){#fig:rotatescale}
**{*@fig:rotatescale}b**: but with **P** from {@eq:incorrect_transform_matrix}, this is what you get.
</div>
</div>

Unfortunately, there is a lot of incorrect or misleading information on the transformation matrix around; the matrix of eq 10.1 is just one aspect of it. This actually starts with the moniker “Rot/Scale”, which does not fit with what actually occurs, continues with the fact that the terms used are never properly defined and that most people often just copy-paste from others without even considering checking whether the information is correct or not. The irony is that the principle reference document, GBATek, gives the correct descriptions of each of the elements, but somehow it got lost in the translation to matrix form in the tutorials.

In this chapter, I'll provide the **correct** interpretation of the **P**-matrix; how the GBA uses it and how to construct one yourself. To do this, though, I'm going into full math-mode. If you don't know your way around vector and matrix calculations you may have some difficulties understanding the finer points of the text. There is an appendix on [linear algebra](matrix.html) for some pointers on this subject.

This is going to be a purely theoretical page: you will find nothing that relates directly to sprites or backgrounds here; that's what the next two sections are for. Once again, we will be assisted by the lovely metroid (keep in cold storage for safe use). Please mind the direction of the y-axis and the angles, and do *not* leave without reading the [finishing up](#sec-finish) paragraph. This contains several key implementation details that will be ignored in the text preceding it, because they will only get in the way at that point.

<div class="note">
<div class="nhcare">
Be wary of documents covering affine parameters
</div>

It's true. Pretty much every document I've seen that deals with this subject is problematic in some way. A lot of them give the wrong rotate-scale matrix (namely, the one in {@eq:incorrect_transform_matrix}), or misname and/or misrepresent the matrix and its elements.
</div>

## Texture mapping and affine transformations.

### General 2D texture mapping

What the GBA does to get sprites and tiled backgrounds on screen is very much like texture mapping. So forget about the GBA right now and look at how texture mapping is done. In {@fig:rotatescale}a, we see a metroid texture. For convenience I am using the standard Cartesian 2D coordinate system (y-axis points up) and have normalised the texture, which means that the right and top side of the texture correspond precisely with the unit-vectors <math><msub><mi>e</mi><mi>x</mi></msub></math> and <math><msub><mi>s</mi><mi>y</mi></msub></math> (which are of length 1). The texture mapping brings **p** (in texture space) to a point **q** (in screen space). The actual mapping is done by a 2×2 matrix **A**:

<math class="block">
    <mi>𝗾</mi>
    <mo>=</mo>
    <mi>𝗔</mi>
    <mo>&middot;</mo>
    <mi>𝗽</mi>
</math>

So how do you find **A**? Well, that's actually not that hard. The matrix is formed by lining up the transformed base vectors, which are **u** and **v** (this works in any number of dimensions, btw), so that gives us:

<math id="eq:correct_transform_matrix" class="block">
    <mi>𝗔</mi>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><msub><mi>u</mi><mi>x</mi></msub></mtd>
                <mtd><msub><mi>v</mi><mi>x</mi></msub></mtd>
            </mtr>
            <mtr>
                <mtd><msub><mi>u</mi><mi>x</mi></msub></mtd>
                <mtd><msub><mi>v</mi><mi>y</mi></msub></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
</math>

<div style="display: flex; align-items: center" markdown>
<div class="cpt" style="width:128px;" markdown>
![A metroid texture...](img/affine/metr_tex.png){#fig:metroid_texture}a
**{*@fig:metroid_texture}a**: a texture.
</div>

<span style="font-size: 3em; display: inline-flex; flex-direction: column; padding: 10px" markdown>**A** →</span>

<div class="cpt" style="width:128px;" markdown>
![ ... mapped](img/affine/metr_texmapA.png){#fig:metroid_texture}b
**{*@fig:metroid_texture}b**: a texture mapped
</div>
</div>
A forward texture mapping via affine matrix **A**.

### Affine transformations

The transformations you can do with a 2D matrix are called <dfn>[affine](http://en.wikipedia.org/wiki/Affine){target="_blank"}</dfn> transformations. The technical definition of an affine transformation is one that preserves parallel lines, which basically means that you can write them as matrix transformations, or that a rectangle will become a parallelogram under an affine transformation (see {@eq:transformation_matrix_and_inverse}).

Affine transformations include rotation and scaling, but *also* shearing. This is why I object to the name “Rot/Scale”: that term only refers to a special case, not the general transformation. It is akin to calling colors shades of red: yes, reds are colors too, but not all colors are reds, and to call them that would give a distorted view of the subject.

As I said, there are three basic 2d transformations, though you can always describe one of these in terms of the other two. The transformations are: rotation (**R**), scaling (**S**) and shear (**H**). {*@tbl:transformation_matrices_and_their_inverses} shows what each of the transformations does to the regular metroid sprite. The black axes are the normal base vectors (note that *y* points down!), the blue axes are the transformed base vectors and the cyan variables are the arguments of the transformation. Also given are the matrix and inverse matrix of each transformation. Why? You'll see.

  
<math id="eq:transformation_matrix_and_inverse" class="block">
    <mo>(</mo>
    <mi>{!@eq:transformation_matrix_and_inverse}</mi>
    <mo>)</mo>
    <mspace width="30px" />
    <mi>𝗔</mi>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><mi>a</mi></mtd>
                <mtd><mi>b</mi></mtd>
            </mtr>
            <mtr>
                <mtd><mi>c</mi></mtd>
                <mtd><mi>d</mi></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
    <mspace width="30px"/>
    <msup>
        <mi>𝗔</mi>
        <mn>-1</mn>
    </msup>
    <mo>≡</mo>
    <mfrac>
        <mn>1</mn>
        <mrow>
            <mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi>
        <mrow>
    </mfrac>
        <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><mi>d</mi></mtd>
                <mtd><mo>-</mo><mi>b</mi></mtd>
            </mtr>
            <mtr>
                <mtd><mo>-</mo><mi>c</mi></mtd>
                <mtd><mi>a</mi></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
</math>

{*@tbl:transformation_matrices_and_their_inverses}: transformation matrices and their inverses.
<table id="tbl:transformation_matrices_and_their_inverses">
    <thead>
        <tr>
            <th>Identity</th>
            <th>Rotation</th>
            <th>Scaling</th>
            <th>Shear</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td markdown><img alt="Normal metroid" src="img/affine/metr_id.png" /></td>
            <td markdown><img alt="Rotated metroid" src="img/affine/metr_rot.png" /></td>
            <td markdown><img alt="Scaled metroid" src="img/affine/metr_scale.png" /></td>
            <td markdown><img alt="Sheared metroid" src="img/affine/metr_shear.png" /></td>
        </tr>
        <tr>
            <td>
                <math>
                    <mi>𝗜</mi>
                    <mo>=</mo>
                    <mrow>
                        <mo>[</mo>
                        <mtable>
                            <mtr>
                                <mtd><mn>1</mn></mtd>
                                <mtd><mn>0</mn></mtd>
                            </mtr>
                            <mtr>
                                <mtd><mn>0</mn></mtd>
                                <mtd><mn>1</mn></mtd>
                            </mtr>
                        </mtable>
                        <mo>]</mo>
                    </mrow>
                </math>
            </td>
            <td>
                <math>
                    <mi>𝗥</mi>
                    <mo>(</mo>
                    <mn>&theta;</mn>
                    <mo>)</mo>
                    <mo>=</mo>
                    <mrow>
                        <mo>[</mo>
                        <mtable>
                            <mtr>
                                <mtd><mi>cos</mi><mo>(</mo><mn>&theta;</mn><mo>)</mo></mtd>
                                <mtd><mo>-</mo><mi>sin</mi><mo>(</mo><mn>&theta;</mn><mo>)</mo></mtd>
                            </mtr>
                            <mtr>
                                <mtd><mi>sin</mi><mo>(</mo><mn>&theta;</mn><mo>)</mo></mtd>
                                <mtd><mi>cos</mi><mo>(</mo><mn>&theta;</mn><mo>)</mo></mtd>
                            </mtr>
                        </mtable>
                        <mo>]</mo>
                    </mrow>
                </math>
            </td>
            <td>
                <math>
                    <mi>𝗦</mi>
                    <mo>(</mo>
                    <msub><mi>s</mi><mi>x</mi></msub>
                    <mo>,</mo>
                    <msub><mi>s</mi><mi>y</mi></msub>
                    <mo>)</mo>
                    <mo>=</mo>
                    <mrow>
                        <mo>[</mo>
                        <mtable>
                            <mtr>
                                <mtd><msub><mi>s</mi><mi>x</mi></msub></mtd>
                                <mtd><mn>0</mn></mtd>
                            </mtr>
                            <mtr>
                                <mtd><mn>0</mn></mtd>
                                <mtd><msub><mi>s</mi><mi>y</mi></msub></mtd>
                            </mtr>
                        </mtable>
                        <mo>]</mo>
                    </mrow>
                </math>
            </td>
            <td>
                <math>
                    <mi>𝗛</mi>
                    <mo>(</mo>
                    <msub><mi>h</mi><mi>x</mi></msub>
                    <mo>,</mo>
                    <msub><mi>h</mi><mi>y</mi></msub>
                    <mo>)</mo>
                    <mo>=</mo>
                    <mrow>
                        <mo>[</mo>
                        <mtable>
                            <mtr>
                                <mtd><mn>1</mn></mtd>
                                <mtd><msub><mi>h</mi><mi>x</mi></msub></mtd>
                            </mtr>
                            <mtr>
                                <mtd><msub><mi>h</mi><mi>y</mi></msub></mtd>
                                <mtd><mn>1</mn></mtd>
                            </mtr>
                        </mtable>
                        <mo>]</mo>
                    </mrow>
                </math>
            </td>
        </tr>
        <tr>
            <td>
                <math>
                    <msup><mi>𝗜</mi><mn>-1</mn></msup>
                    <mo>=</mo>
                    <mi>𝗜</mi>
                </math>
            </td>
            <td>
                <math>
                    <msup><mi>𝗥</mi><mn>-1</mn></msup><mo>(</mo><mn>&theta;</mn><mo>)</mo>
                    <mo>=</mo>
                    <mi>𝗥</mi><mo>(</mo><mn>-&theta;</mn><mo>)</mo>
                </math>
            </td>
            <td>
                <math>
                    <msup><mi>𝗦</mi><mn>-1</mn></msup>
                    <mo>(</mo>
                    <msub><mi>s</mi><mi>x</mi></msub>
                    <mo>,</mo>
                    <msub><mi>s</mi><mi>y</mi></msub>
                    <mo>)</mo>
                    <mo>=</mo>
                    <mi>𝗦</mi>
                    <mo>(</mo>
                    <mfrac><mn>1</mn><msub><mi>s</mi><mi>x</mi></msub></mfrac>
                    <mo>,</mo>
                    <mfrac><mn>1</mn><msub><mi>s</mi><mi>y</mi></msub></mfrac>
                    <mo>)</mo>
                </math>
            </td>
            <td>
                <math>
                    <msup><mi>𝗛</mi><mn>-1</mn></msup>
                    <mo>(</mo>
                    <msub><mi>h</mi><mi>x</mi></msub>
                    <mo>,</mo>
                    <msub><mi>h</mi><mi>y</mi></msub>
                    <mo>)</mo>
                    <mo>=</mo>
                    <mfrac>
                        <mrow>
                            <mi>𝗛</mi>
                            <mo>(</mo>
                            <mn>-</mn><msub><mi>h</mi><mi>x</mi></msub>
                            <mo>,</mo>
                            <mn>-</mn><msub><mi>h</mi><mi>y</mi></msub>
                            <mo>)</mo>
                        </mrow>
                        <mrow>
                            <mn>1</mn>
                            <mo>-</mo>
                            <msub><mi>h</mi><mi>x</mi></msub>
                            <msub><mi>h</mi><mi>y</mi></msub>
                        </mrow>
                    </mfrac>
                </math>
            </td>
        </tr>
    </tbody>
</table>

We can now use these definitions to find the correct matrix for enlargements by <math><msub><mi>s</mi><mi>x</mi></msub></math> and <math><msub><mi>s</mi><mi>y</mi></msub></math>, followed by a **counter-clockwise** rotation by α (=−θ), by matrix multiplication.

<math id="eq:inverse_transform" class="block">
    <mo>(</mo>
    <mi>{!@eq:inverse_transform}</mi>
    <mo>)</mo>
    <mspace width="30px" />
    <mi>𝗔</mi>
    <mo>=</mo>
    <mi>𝗥</mi><mo>(</mo><mn>-&alpha;</mn><mo>)</mo>
    <mo>&middot;</mo>
    <mi>𝗦</mi><mo>(</mo><msub><mi>s</mi><mi>x</mi></msub><mo>,</mo><msub><mi>s</mi><mi>y</mi></msub><mo>)</mo>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><msub><mi>s</mi><mi>x</mi></msub><mi>cos</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
                <mtd><msub><mi>s</mi><mi>y</mi></msub><mi>sin</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
            </mtr>
            <mtr>
                <mtd><mo>-</mo><msub><mi>s</mi><mi>x</mi></msub><mi>sin</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
                <mtd><msub><mi>s</mi><mi>y</mi></msub><mi>cos</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
</math>

… ermm, wait a sec … I'm having this strange sense of déja-vu here …

<div class="note" markdown>
<div class="nh" markdown>
Clockwise vs counterclockwise
</div>

It's a minor issue, but I have to mention it. If the definition of **R** uses a clockwise rotation, why am I suddenly using a counter-clockwise one? Well, traditionally **R** is given as that particular matrix, in which the angle runs from the x-axis towards the y-axis. Because *y* is downward, this comes down to clockwise. However, the affine routines in BIOS use a counter-clockwise rotation, and I thought it'd be a good idea to use that as a guideline for my functions.
</div>

<div class="note" markdown>
<div class="nh" markdown>
Nomenclature: Affine vs Rot/Scale
</div>

The matrix **P** is not a rotation matrix, not a scaling matrix, but a general affine transformation matrix. Rotation and scaling may be what the matrix is mostly used for, but that does not mean they're the only things possible, as the term ‘Rot/Scale’ would imply.

To set them apart from regular backgrounds and sprites, I suppose ‘Rotation’ or ‘Rot/Scale’ are suitable enough, just not entirely accurate. However, calling the **P**-matrix by those names is simply wrong.
</div>

## “Many of the truths we cling to depend greatly upon our own point of view.”

<div class="cpt_fr" style="width:160px" markdown>
![Human view](img/affine/metr_texmapA.png){#fig:human_pov}  
**{*@fig:human_pov}**: Mapping process as seen by humans. **u** and **v** are the columns of **A** (in screen space).
</div>

As you must have noticed, {@eq:inverse_transform} is identical to {@eq:incorrect_transform_matrix}, which I said was incorrect. So what gives? Well, if you enter this matrix into the `pa-pd` elements you do indeed get something different than what you'd expect. Only now I've proven what you were supposed to expect in the first place (namely a scaling by <math><msub><mi>s</mi><mi>x</mi></msub></math> and <math><msub><mi>s</mi><mi>y</mi></msub></math>, followed by a counter-clockwise rotation by α). The *real* question is of course, why doesn't this work? To answer this I will present two different approaches to the 2D mapping process.

### Human point of view

“Hello, I am Cearn's brain. I grok geometry and can do matrix- transformations in my head. Well, his head actually. When it comes to texture mapping I see the original map (in texture space) and then visualize the transformation. I look at the original map and look at where the map's pixels end up on screen. The transformation matrix for this is **A**, which ties texel **p** to screen pixel **q** via **q**= **A · p**. The columns of **A** are simply the transformed unit matrices. Easy as π.”

### Computer point of view

<div class="cpt_fr" style="width:160px" markdown>
![puter view](img/affine/metr_texmapB.png){#fig:comp_pov}  
**{*@fig:comp_pov}**: Mapping process as seen by computers. **u** and **v** (in texture space) are the columns of **B** and are mapped to the principle axes in screen space.
</div>

“Hello, I am Cearn's GBA. I'm a lean, mean gaming machine that fits in your pocket, and I can push pixels like no one else. Except perhaps my owner's GeForce 4 Ti4200, the bloody show-off. Anyway, one of the things I do is texture mapping. And not just ordinary texture-mapping, I can do cool stuff like rotation and scaling as well. What I do is fill pixels, all I need to know is for you to tell me where I should get the pixel's color from. In other words, to fill screen pixel **q**, I need a matrix **B** that gives me the proper texel **p** via **p = B · q**. I'll happily use any matrix you give me; I have complete confidence in your ability to supply me with the matrix for the transformation you require.”

### Resolution

I hope you spotted the crucial difference between the two points of view. **A** maps *from* texture space *to* screen space, while **B** does the exact opposite (i.e., <math><mi>𝗕</mi><mo>=</mo><msup><mi>𝗔</mi><mn>-1</mn></msup></math>). I think you know which one you should give the GBA by now. That's right: **P = B**, not **A**. This one bit of information is the crucial piece of the affine matrix puzzle.

So now you can figure out **P**'s elements in two ways. You can stick to the human POV and invert the matrix at the end. That's why I gave you the inverses of the affine transformations as well. You could also try to see things in the GBA's way and get the right matrix directly. Tonc's main affine functions (`tonc_video.h`, `tonc_obj_affine.c` and `tonc_bg_affine.c`) do things the GBA way, setting **P** directly; but inverted functions are also available using an "`_inv`" affix. Mind you, these are a little slower. Except for when scaling is involved; then it's a *lot* slower.

In case you're curious, the proper matrix for scale by (<math><msub><mi>s</mi><mi>x</mi></msub></math>, <math><msub><mi>s</mi><mi>y</mi></msub></math>) and counter-clockwise rotation by α is:

<math class="block">
    <mi>𝗔</mi>
    <mo>=</mo>
    <mi>𝗥</mi><mo>(</mo><mn>-&alpha;</mn><mo>)</mo>
    <mo>&middot;</mo>
    <mi>𝗦</mi><mo>(</mo><msub><mi>s</mi><mi>x</mi></msub><mo>,</mo><msub><mi>s</mi><mi>y</mi></msub><mo>)</mo>
</math>

<math class="block">
    <mtable>
        <mtr>
            <mtd>
                <mi>𝗣</mi>
            </mtd>
            <mtd columnalign="left">
                <mo>=</mo>
                <msup><mi>𝗔</mi><mn>-1</mn></msup>
            </mtd>
        </mtr>
        <mtr>
            <mtd />
            <mtd columnalign="left">
                <mo>=</mo>
                <mo>(</mo>
                <mi>𝗥</mi><mo>(</mo><mn>-&alpha;</mn><mo>)</mo>
                <mo>&middot;</mo>
                <mi>𝗦</mi><mo>(</mo><msub><mi>s</mi><mi>x</mi></msub><mo>,</mo><msub><mi>s</mi><mi>y</mi></msub><mo>)</mo>
                <msup><mo>)</mo><mn>-1</mn></msup>
            </mtd>
        </mtr>
        <mtr>
            <mtd />
            <mtd columnalign="left">
                <mo>=</mo>
                <msup><mi>𝗦</mi><mn>-1</mn></msup><mo>(</mo><msub><mi>s</mi><mi>x</mi></msub><mo>,</mo><msub><mi>s</mi><mi>y</mi></msub><mo>)</mo>
                <mo>&middot;</mo>
                <msup><mi>𝗥</mi><mn>-1</mn></msup><mo>(</mo><mn>-&alpha;</mn><mo>)</mo>
            </mtd>
        </mtr>
    </mtable>
</math>

Using the inverse matrices given earlier, we find

<math id="eq:correct_matrix" class="block">
    <mo>(</mo>
    <mi>{!@eq:correct_matrix}</mi>
    <mo>)</mo>
    <mspace width="30px" />
    <mi>𝗣</mi>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><msub><mi>p</mi><mi>a</mi></msub></mtd>
                <mtd><msub><mi>p</mi><mi>b</mi></msub></mtd>
            </mtr>
            <mtr>
                <mtd><msub><mi>p</mi><mi>c</mi></msub></mtd>
                <mtd><msub><mi>p</mi><mi>d</mi></msub></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
    <mo>=</mo>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd>
                    <mfrac>
                        <mrow><mi>cos</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mrow>
                        <msub><mi>s</mi><mi>x</mi></msub>
                    </mfrac>
                </mtd>
                <mtd>
                    <mfrac>
                        <mrow><mn>-</mn><mi>sin</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mrow>
                        <msub><mi>s</mi><mi>x</mi></msub>
                    </mfrac>
                </mtd>
            </mtr>
            <mtr>
                <mtd>
                    <mfrac>
                        <mrow><mi>sin</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mrow>
                        <msub><mi>s</mi><mi>y</mi></msub>
                    </mfrac>
                </mtd>
                <mtd>
                    <mfrac>
                        <mrow><mi>cos</mi><mo>(</mo><mn>&alpha;</mn><mo>)</mo></mrow>
                        <msub><mi>s</mi><mi>y</mi></msub>
                    </mfrac>
                </mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
    </mrow>
</math>

<div class="note" markdown>
Just to make it perfectly clear:

The affine matrix **P** maps from screen space *to* texture space, not the other way around!

In other words:  

&nbsp;<math><msub><mi>p</mi><mi>a</mi></msub></math>: texture *x*-increment / pixel

&nbsp;<math><msub><mi>p</mi><mi>b</mi></msub></math>: texture *x*-increment / scanline

&nbsp;<math><msub><mi>p</mi><mi>c</mi></msub></math>: texture *y*-increment / pixel

&nbsp;<math><msub><mi>p</mi><mi>d</mi></msub></math>: texture *y*-increment / scanline
</div>

## Finishing up {#sec-finish}

Knowing what the **P**-matrix is used for is one thing, knowing how to use them properly is another. There are three additional points you need to remember when you're going to deal with affine objects/backgrounds and the affine matrices.

1.  Datatypes
2.  Luts
3.  Initialisation

### Data types of affine elements

Affine transformations are part of mathematics and, generally speaking, math numbers will be real numbers. That is to say, floating point numbers. However, if you were to use floating points for the **P** elements, you'd be in for two rude surprises.

The first one is that the matrix elements are not floats, but integers. The reason behind this is that <ack>the GBA has no floating point unit!</ack> All floating-point operations have to be done in software and without an FPU, that's going to be pretty slow. Much slower than integer math, at any rate. Now, when you think about this, it does create some problems with precision and all that. For example, the (co)sine and functions have a range between −1 and 1, a range which isn't exactly large when it comes to integers. However, the range would be much greater if one didn't count in units of 1, but in fractions, say in units of 1/256. The \[−1, +1\] range then becomes \[−256, +256\],

This strategy of representing real numbers with scaled integers is known as <dfn>fixed point arithmetic</dfn>, which you can read more about in [this appendix](fixed.html) and on [wikipedia](http://en.wikipedia.org/wiki/Fixed-point_arithmetic){target="_blank"}. The GBA makes use of fixed point for its affine parameters, but you can use it for other things as well. The **P**-matrix elements are 8.8 fixed point numbers, meaning a halfword with 8 integer bits and 8 fractional bits. To set a matrix to identity (1s on the diagonals, 0s elsewhere), you wouldn't use this:

```c
    // Floating point == Bad!!
    pa= pd= 1.0;
    pb= pc= 0.0;
```

but this:

```c
    // .8 Fixed-point == Good
    pa= pd= 1<<8;
    pb= pc= 0;
```

In a fixed point system with *Q* fractional bits, ‘1’ (‘one’) is represented by 2^Q^ or 1\<\<*Q*, because simply that's how fractions work.

Now, fixed point numbers are still just integers, but there are different types of integers, and it is important to use the right ones. 8.8f are 16bit variables, so the logical choice there is `short`. However, this should be a *signed* short: `s16`, not `u16`. Sometimes is doesn't matter, but if you want to do any arithmetic with them they'd better be signed. Remember that internally the CPU works in words, which are 32bit, and the 16bit variable will be converted to that. You really want, say, a 16bit "−1" (`0xFFFF`) to turn into a 32bit "−1" (`0xFFFFFFFF`), and not "65535" (`0x0000FFFF`), which is what happens if you use unsigned shorts. Also, when doing fixed point math, it is recommended to use signed ints (the 32bit kind) for them, anything else will slow you down and you might get overflow problems as well.

  

<div class="note" markdown>
<div class="nhgood" markdown>
Use 32-bit signed ints for affine temporaries
</div>

Of course you should use 32bit variables for everything anyway (unless you actually *want* your code to bloat and slow down). If you use 16bit variables (`short` or `s16`), not only will your code be slower because of all the extra instructions that are added to keep the variables 16bit, but overflow problems can occur much sooner.

Only in the final step to hardware should you go to 8.8 format. Before that, use the larger types for both speed and accuracy.
</div>

### LUTs {#sec-luts}

So fixed point math is used because floating point math is just to slow for efficient use. That's all fine and good for your own math, but what about mathematical functions like sin() and cos()? Those are still floating point internally (even worse, *`double`s*!), so those are going to be ridiculously slow.

Rather than using the functions directly, we'll use a time-honored tradition to weasel our way out of using costly math functions: we're going to build a <dfn>look-up table</dfn> (LUT) containing the sine and cosine values. There are a number of ways to do this. If you want an easy strategy, you can just declare two arrays of 360 8.8f numbers and fill them at initialization of your program. However, this is a poor way of doing things, for reasons explained in the [section on LUTs](fixed.html#sec-lut) in the appendix.

Tonclib has a single sine lut which can be used for both sine and cosine values. The lut is called `sin_lut`, a `const short` array of 512 4.12f entries (12 fractional bits), created by my [excellut](http://www.coranac.com/projects/#excellut){target="_blank"} lut creator. In `tonc_math.h` you can find two inline functions that retrieve sine and cosine values:

```c
//! Look-up a sine and cosine values
/*! \param theta Angle in [0,FFFFh] range
*   \return .12f sine value
*/

INLINE s32 lu_sin(uint theta)
{   return sin_lut[(theta>>7)&0x1FF];           }

INLINE s32 lu_cos(uint theta)
{   return sin_lut[((theta>>7)+128)&0x1FF];     }
```

Now, note the angle range: 0-10000h. Remember you don't *have* to use 360 degrees for a circle; in fact, on computers it's better to divide the circle in a power of two instead. In this case, the angle is in 2^16^ parts for compatibility with BIOS functions, which is brought down to a 512 range inside the look-up functions.

### Initialization

When flagging a background or object as affine, you *must* enter at least some values into `pa-pd`. Remember that these are zeroed out by default. A zero-offset means it'll use the first pixel for the whole thing. If you get a single-colored background or sprite, this is probably why. To avoid this, set **P** to the identity matrix or any other non-zero matrix.

## Tonc's affine functions

Tonclib contains a number of functions for manipulating the affine parameters of objects and backgrounds, as used by the `OBJ_AFFINE` and `BG_AFFINE` structs. Because the affine matrix is stored differently in both structs you can't set them with the same function, but the functionality is the same. In {@tbl:affine_functions} you can find the basic formats and descriptions; just replace *foo* with `obj_aff` or `bg_aff` and *FOO* with `OBJ` or `BG` for objects and backgrounds, respectively. The functions themselves can be found in `tonc_obj_affine.c` for objects, `tonc_bg_affine.c` for backgrounds, and inlines for both in `tonc_video.h` … somewhere.

<table class="cblock" id="tbl:affine_functions">
    <thead>
        <tr>
            <th>Function</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>void foo_copy(FOO_AFFINE *dst, const FOO_AFFINE *src, uint count);</td>
            <td>Copy affine parameters</td>
        </tr>
        <tr>
            <td>void foo_identity(FOO_AFFINE *oaff);</td>
            <td><math><mi>P</mi><mo>=</mo><mi>I</mi></td>
        </tr>
        <tr>
            <td>void foo_postmul(FOO_AFFINE *dst, const FOO_AFFINE *src);</td>
            <td>Post-multiply: <math><mi>D</mi><mo>=</mo><mi>D</mi><mo>&middot;</mo><mi>S</mi></math></td>
        </tr>
        <tr>
            <td>void foo_premul(FOO_AFFINE *dst, const FOO_AFFINE *src);</td>
            <td>Pre-multiply: <math><mi>D</mi><mo>=</mo><mi>S</mi><mo>&middot;</mo><mi>D</mi></math></td>
        </tr>
        <tr>
            <td>void foo_rotate(FOO_AFFINE *aff, u16 alpha);</td>
            <td>Rotate counter-clockwise by α·π/8000h.</td>
        </tr>
        <tr>
            <td>void foo_rotscale(FOO_AFFINE *aff, FIXED sx, FIXED sy, u16 alpha);</td>
            <td>Scale by <math><mfrac><mn>1</mn><msub><mi>s</mi><mi>x</mi></msub></mfrac></math> and <math><mfrac><mn>1</mn><msub><mi>s</mi><mi>y</mi></msub></mfrac></math>, then rotate counter-clockwise by α·π/8000h.</td>
        </tr>
        <tr>
            <td>void foo_rotscale2(FOO_AFFINE *aff, const AFF_SRC *as);</td>
            <td>As foo_rotscale(), but input stored in an AFF_SRC struct.</td>
        </tr>
        <tr>
            <td>void foo_scale(FOO_AFFINE *aff, FIXED sx, FIXED sy);</td>
            <td>Scale by <math><mfrac><mn>1</mn><msub><mi>s</mi><mi>x</mi></msub></mfrac></math> and <math><mfrac><mn>1</mn><msub><mi>s</mi><mi>y</mi></msub></mfrac></math></td>
        </tr>
        <tr>
            <td>void foo_set(FOO_AFFINE *aff, FIXED pa, FIXED pb, FIXED pc, FIXED pd);</td>
            <td>Set P's elements</td>
        </tr>
        <tr>
            <td>void foo_shearx(FOO_AFFINE *aff, FIXED hx);</td>
            <td>Shear top-side right by <math><msub><mi>h</mi><mi>x</mi></msub></math></td>
        </tr>
        <tr>
            <td>void foo_sheary(FOO_AFFINE *aff, FIXED hy);</td>
            <td>Shear left-side down by <math><msub><mi>h</mi><mi>y</mi></msub></math></td>
        </tr>
    </tbody>
</table>
**{*@tbl:affine_functions}**: affine functions

### Sample rot/scale function

My code for a object version of the scale-then-rotate function (à la {@eq:transformation_matrix}) is given below. Note that it is from the computer's point of view, so that `sx` and `sy` scale down. Also, the alpha `alpha` uses 10000h/circle (i.e., the unit of α is π/8000h = 0.096 mrad, or 180/8000h = 0.0055°) and the sine lut is in .12f format, which is why the shifts by 12 are required. The background version is identical, except in name and type. If this were C++, templates would have been mighty useful here.

```c
void obj_aff_rotscale(OBJ_AFFINE *oaff, int sx, int sy, u16 alpha)
{
    int ss= lu_sin(alpha), cc= lu_cos(alpha);

    oaff->pa= cc*sx>>12;    oaff->pb=-ss*sx>>12;
    oaff->pc= ss*sy>>12;    oaff->pd= cc*sy>>12;
}
```

With the information in this chapter, you know most of what you need to know about affine matrices, starting with why they should be referred to *affine* matrices, rather than merely rotation or rot/scale or the other names you might see elsewhere. You should now know what the thing actually does, and how you can set up a matrix for the effects you want. You should also know a little bit about fixed point numbers and luts (for more, look in the [appendices](fixed.html)) and why they're Good Things; if it hadn't been clear before, you should be aware that the choice of the data types you use actually *matters*, and you should not just use the first thing that comes along.

What has not been discussed here is how you actually set-up objects and backgrounds to use affine transformation, which is what the next two chapters are for. For more on affine transformations, try searching for ‘linear algebra’
