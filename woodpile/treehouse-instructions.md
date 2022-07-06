I've left R2C2--my autonomous tree chopping robot--to do his thing for awhile now,
and I think I *finally* have enough wood for the dream treehouse I've always wanted!
I've started writing up some schematics for a treehouse that should be *perfect* for the big oak tree in my backyard.
The measurements I came up with are already in my `treehouse-blueprint.py`.
(I didn't note it in the blueprint, but all the measurements are in feet.)
I'm absolutely positive they're perfect and won't need to be adjusted.

When it comes to the treehouse itself, it seems like simple will be best:
I'm thinking a real open concept--no interior walls, and no ceiling (so I can see the stars).
Just four walls around the exterior of the treehouse. Two of which don't need space for windows or anything.
However, I'd like the east- and west-facing walls to each have three rectangular spaces for windows of equal size
(so I can watch the sun rise and set, of course).
That means **six window spaces total, three on each of two walls.**

The floor of the treehouse complicates things a little bit. It'll need two holes in it:
a circular one that fits snugly against the tree trunk, and a **square** entry hole for me to climb up through.
(I'll have a rope ladder for climbing up into the tree house, so I don't need to take that into account,
just the hole itself I'd be clambering up through).
Thankfully this tree is *perfect* for this, in that its trunk is perfectly circular!
How often do you see that?!
Given that I've already determined the `tree_radius` in the `treehouse-blueprint.py`
calculating the space needed for the tree hole shouldn't be too bad.

**In summation, there's basically five rectangular surfaces to find dimensions for: four walls and a floor.**
**Three of these surfaces will have spaces cut out of them: two walls will have three rectangular windows each,**
**and the floor will have two holes--a circular one for the tree trunk and a square one for me to climb through.**

It definitely seems like the easiest way to go about this is to calculate each separate piece of the puzzle individually,
then incorporate it all together at the end.
Like, first go about finding the space needed for a window,
then calculate how much wood the wall will actually need with that amount of space missing.
That sort of thing.

Once I've got all the correct calculations in place, and have determined the *total square footage of required wood*,
running the `treehouse-blueprint.py` program will upload the schematic to R2B2, my autonomous building robot.
He'll get right to work and put together that treehouse in a jiffy! Can't wait to see the final product!

...Whenever I get around to finishing that `treehouse-blueprint.py`, that is.
