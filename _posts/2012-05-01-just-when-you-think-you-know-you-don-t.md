---
title: just when you think you know, you don't
author: masen
layout: post
tags: lengthy technical programming
redirect_from:
  - /blog/just-when-you-think-you-know-you-don-t.html
  - /blog/10
---

<span class="image right" style="width: 180px">
![I dont always test my code but when I do its on the production
server]({{ "assets/img/blog/i_dont_always_test.jpg" | relative_url }})</span>
As the natural-born overachieving perfection-seeking pragmatist that I am,
I often find myself exceeding the specifications on my Computer Science
assignments. Generally, I find them to be either too simple, or not
interesting; and in an effort to \'get the education my parents paid
for\' I make my own rules.

Unfortunately, in UNIX software development, part of the specification
is to explicitly NOT stray from the specification...and the assignments
are too easy. How could I remain an overachieving bastard while not
sacrificing my turn-in grades by modifying the assignment?

100% code coverage? That may just be crazy enough to enlighten me. I\'ve
been reading/hearing about TDD (test driven development) and the
benefits of testing discrete pieces of code for expected
behavior.  It\'s fun and since I started, I\'ve caught about 3 or 4 bugs
which previously slipped through my professor\'s grading
script. There\'s plenty of material on it around the internet, and
that\'s not what this entry is quite about.

The ongoing assignment for the quarter is to implement our own basic
mini shell, msh. Part of the current assignment this week is to
implement shell scripting. Ahh, I can\'t wait to test this, I
thought...

The mini shell is written in C, however I\'m using Python\'s subprocess
and unittest modules for running \'External\' tests: I Popen my shell
and send data to it. For the scripting test, I open a file,
\_\_test\_script.msh; write the contents of the test script (stored
as literal strings in the python code); and then execute the shell with
\_\_test\_script.msh as the argument. Straightforward right:

```
    class TestMshExternal(unittest.TestCase):
        def setUp(self):
            self.EXE = ["./msh"]
        def executeLine(self,inp,env,EXE=None):
            if EXE is None:
                EXE = self.EXE
            msh = Popen(EXE,stdin=PIPE, stdout=PIPE, stderr=PIPE, env=env)
            raw_output, raw_err = msh.communicate(inp)
            return (raw_output, raw_err, msh.returncode)
        def test_a4_execute_script(self):
            f = open("__test_script.msh","w")
            f.write("""
                   echo showshift is named $0
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
                   echo Argument 2 is $2.
                   echo Argument 3 is $3.
                   echo Argument 4 is $4.
                   shift 3
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
                   echo Argument 2 is $2.
                   echo Argument 3 is $3.
                   echo Argument 4 is $4.
                   unshift 1
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.                                                                                                                                                
                   unshift
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
            """)

            args1 = ["./msh","__test_script.msh","a","b"]
            result = self.executeLine("", None, args1)

            # make assertions about the result
```

So I run it and...no output. The result tuple, which should return the
strings from the stdout and stderr buffers as well as the return code,
contained empty strings. I looked at the script file:

```
    furerm@CF416-11:~/code/csci352/work/msh$ cat __test_script.msh

                   echo showshift is named $0
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
                   echo Argument 2 is $2.
                   echo Argument 3 is $3.
                   echo Argument 4 is $4.
                   shift 3
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
                   echo Argument 2 is $2.
                   echo Argument 3 is $3.
                   echo Argument 4 is $4.
                   unshift 1
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
                   unshift
                   echo Number of arguments is $#.
                   echo Argument 1 is $1.
```

Everything looks good... I separated out the Popen code from the main
test script and ran it in iPython: the result came back just as
expected! I tried it again as part of the test script: Nothing. I run it
from the shell, works as expected. At this point, I\'ve brought in
some cronies to help me debug this overachieving mess to no avail.
Searching on the internet turns up nothing and my pragmatic side starts
to take over: \"Dude, you\'ve been working on this unnecessary thing
(which technically works) for over 2.5 hours now, it\'s not worth your
time!\" You\'re right, self, so I tabled the script and finished the
actual assignment.

After completion, I was still unsettled that my test script was borked.
Determined to solve the problem for my own sanity, I decided to start
dismantling this part of the test case piece by piece. (My previous
solution strategy was to make a conjecture, try it, repeat). I moved all
the shell spawning Popen stuff into the test function itself to isolate
it and began simplifying the script. The next thing I removed was the
actual writing of the \_\_test\_script.msh file (it already existed on
the filesystem anyway). As I selected the last line in Vim Visual Line
mode I had the realization of my ignorance...

### I never closed the file 0.o

The script interpreter stops execution on EOF...and it never found one.
All in all, I had sunk about 4 or 5 hours into such folly which needs
only a two line fix. (I likely made this error because of my overuse of
contextmanagers =\])

```
    furerm@CF416-11:~/code/csci352/work/msh$ diff test.py test_fix.py
    232,233c232,233
    <         f = open("__test_script.msh","w")
    <         f.write("""
    ---
    >         with open("__test_script.msh","w") as f:
    >             f.write("""
```

I feel like I speak out about this sort of ignorant debugging frequently
in the form of advice: \"Read what the code is doing, not what it
\*should\* be doing\". In all the tinkering, I had erroneously
**assumed** that years of programming experiencing would compel someone
to close an open file after writing it, or at least before executing it
with an external child process...eeps.

Just when you *think* you *know* how to program, you don\'t... It\'s as
true in programming as it is in life: when you assume, you make an
**ass**-(out of)-**u**-(and)-**me**.

Here\'s to learning from it.
----------------------------
