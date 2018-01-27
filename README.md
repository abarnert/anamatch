# anamatch
A simple program to find anagrams of a set of letters matching a pattern.

This was designed for a friend who wanted to cheat on WordCross and
couldn't find an online anagrammer that did the trick. It turns out that
half the time, the words you can't find in WordCross are non-words like
"flaen" that won't be in any dictionary, so it's not all that useful,
but for a similar but better game it could be more helpful.

It might have some use cases for cheating at games like Scrabble.

# Requirements/Installation

There's no `setup.py`.

Probably requires Python 3.3 (although making it work in 2.7 wouldn't be
too hard), and the shebang line expects it to be named `python3`. Works 
with at least CPython and PyPy.

Depends on your OS's wordlist in `/usr/share/dict/words`. If you don't
have one there (e.g., you're on Windows), or you want to use a wordlist
that better matches the one used by the game you're cheating on, you'll
need to edit the script. If you have no idea where to get a wordlist,
[SCOWL](http://wordlist.aspell.net/) is a good place to start.

The check is case-insensitive, so it will come up with matches like
"bible" even though the BSD wordlist only has "Bible".

If you want to install the script, just do something like:

    $ install -m755 anamatch.py ~/bin/anamatch

# Examples

For a quick use, you can pass the pattern to fit (with dots or underscores 
for empty spaces) and the unforced letters.

So, if you're playing WordCross, with letters `ayibbhd`, and you're stuck
on a 3-letter word ending in `d`:

    $ anamatch ..d ayibbh
    add aid bad bid dad did had yad yid

Or, if you're playing Scrabble, and your hand is `ayibbhd`, and you want
a list of all valid two-letter words you can make (although that's valid
according to your system words, not the Scrabble Dictionary, which makes
it less useful...):

    $ anamatch .. ayibbhd
    ab ad ah ai ay ba by da di ha hi hy id ya

If you need to use the same letters over and over, run interactively:

    $ anamatch
    Letters: ayibbhd
    Pattern: ..d
    add aid bad bid dad did had yad yid
    Pattern: ...d
    dyad ibad
    Pattern: b..y
    baby
    Pattern: 
    Letters: 

# Library use

If you wanted to build a web interface or something, the `ana` function
that generates and filters permutations is reusable. So `import anamatch`
and you can do the same thing the `__main__` bit does:

    with open('/usr/share/dict/words') as f:
        words = {line.strip().lower() for line in f}
    answers = words.intersection(ana(pattern, leftovers))

If you want to iterate the matches instead of building a set, keep in
mind that `itertools.permutations` doesn't care about element equality, 
so `ayibbhd` will iterate over `baby` twice (once with the two `b`s in 
the same order as in the letter set, once with them in the reverse order).

# Implementation

The code just iterates all possible permutations of the letters, filters
out the ones that don't match the pattern, then filters out the ones that
aren't in the wordlist, then sorts and prints the results. This could be 
done more efficiently (but don't worry about memory--we're generating the 
permutations on the fly), but since it takes a fraction of a second for 
any reasonable game you'd want to cheat on, who cares? (If you care, 
running on PyPy is faster than CPython in interactive mode, although a 
lot slower in CLI mode, but that doesn't change the fact that we're
rebuilding all permutations for each pattern.)
