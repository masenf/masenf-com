---
title: "cad/cam/cnc: competing in skillsUSA"
author: masen
layout: post
tags: knowledge lengthy technical popular
redirect_from:
  - /blog/cad-cam-cnc--competing-in-skillsusa.html
  - /blog/2
---

As a sophomore in high school, I unwittingly took Stuart Smith\'s CAM
class and learned some CAD, CAM, and CNC milling on ProLight and Haas
Mills. In fact, I came to learn that my high school just happened to
have one of the best CNC labs in the entire country. I went on to take
2nd Place in the Washington state Automated Manufacturing contest in
2007, 1st Place in 2008 and 2009. And 3rd place in the entire Nation in
2008! Who knew? My specialty on the three person Automated Manufacturing
team was the CAD designer. The contest is designed to simulate a job
process in industry. Each team is given a set of incomplete and possibly
inaccurate \"engineering\" drawings and required to make an industry
standard set of dimensioned CAD prints, as well as rapidly prototype the
part using a CNC mill. Below you will find some of the drawings that
we\'ve had to make over the years at various contests and some files
that seem for some reason to be very hard to track down.

[Intelitek ProLight post for MastercamX2](http://emastercam.com/posts/edu_x2.php)

[Intelitek ProLight post for MastercamX](http://emastercam.com/posts/edu_x.php)

Alternate links: [\[x2-alt\]]({{ "assets/downloads/files/cnc/light-mcamx2.zip" | relative_url }}) [\[x-alt\]]({{ "assets/downloads/files/cnc/light-mcamx.zip" | relative_url }})

These posts are basically *required *to use MasterCam at the national
competition. They allow posting clean code to the provided machines.
Just a word of caution though, when you load up programs posted by these
definitions in **CNCBase** the new CNC control software, you MUST put a
percent-sign (%) as the first line of the program to make the arcs work
correctly (CTRL+L to unlock the code). Other than that you\'re golden.

Most of these files require [Rhinoceros 4.0](http://www.rhino3d.com/) to
open, some are in IGS format.

Nationals 2009:
---------------

TDN: <http://tdn.com/business/local/article_0f65fab8-c76e-5da5-906a-73feeb251703.html> [(local
copy)]({{ "assets/downloads/files/cnc/2009-tdn-article.txt" | relative_url }})

-   [Gear Box Cover CAD.3dm -
    504kb]({{ "assets/downloads/files/cnc/2009/Gear%20Box%20Cover%20CAD.3dm" | relative_url }})
-   [Gear Box Cover Curves Only.3dm -
    49kb]({{ "assets/downloads/files/cnc/2009/Gear%20Box%20Cover%20Curves%20Only.3dm" | relative_url }})
-   [Gear Box Cover Curves Only.IGS -
    25kb]({{ "assets/downloads/files/cnc/2009/Gear%20Box%20Cover%20Curves%20Only.igs" | relative_url }})
-   [Gear Box Housing CAD.3dm -
    181kb]({{ "assets/downloads/files/cnc/2009/Gear%20Box%20Housing%20CAD.3dm" | relative_url }})
-   [Gear Box Housing Curves Only.3dm -
    61kb]({{ "assets/downloads/files/cnc/2009/Gear%20Box%20Housing%20Curves%20Only.3dm" | relative_url }})
-   [Output Shaft CAD.3dm -
    131kb]({{ "assets/downloads/files/cnc/2009/Output%20Shaft%20CAD.3dm" | relative_url }})
-   [Output Shaft Curves Only.3dm -
    31kb]({{ "assets/downloads/files/cnc/2009/Output%20Shaft%20Curves%20Only.3dm" | relative_url }})
-   [Output Shaft Curves Only.IGS -
    9kb]({{ "assets/downloads/files/cnc/2009/Output%20Shaft%20Curves%20Only.igs" | relative_url }})
-   [Planet Gear CAD.3dm -
    141kb]({{ "assets/downloads/files/cnc/2009/Planet%20Gear%20CAD.3dm" | relative_url }})
-   [Planet Gear Curves Only.3dm -
    40kb]({{ "assets/downloads/files/cnc/2009/Planet%20Gear%20Curves%20Only.3dm" | relative_url }})
-   [Planet Gear Curves Only.IGS -
    33kb]({{ "assets/downloads/files/cnc/2009/Planet%20Gear%20Curves%20Only.igs" | relative_url }})

Nationals 2008:
---------------

The goal of this project (and trust me, I wish I had the original
documentation too) was to create a mold that could be utilized to create
the part that they gave us a drawing of. In this case it was a mold that
could create 4 small motor housings. We created a three piece mold which
accomplished this goal. The assembly drawing shows what it would look
like all put together

TDN: <http://tdn.com/business/local/article_38cea3a9-a81f-50de-9fbf-9418daea7661.html> [(local
copy)]({{ "assets/downloads/files/cnc/2008-tdn-article.txt" | relative_url }})

-   [Assembly.3dm -
    1.84mb]({{ "assets/downloads/files/cnc/2008/Assembly.3dm" | relative_url }})
-   [Bottom.3dm -
    265kb]({{ "assets/downloads/files/cnc/2008/Bottom.3dm" | relative_url }})
-   [Dimensions.3dm -
    227kb]({{ "assets/downloads/files/cnc/2008/Dimensions.3dm" | relative_url }})
-   [Middle-layout.3dm -
    153kb]({{ "assets/downloads/files/cnc/2008/Middle-layout.3dm" | relative_url }})
-   [middle.3dm -
    102kb]({{ "assets/downloads/files/cnc/2008/middle.3dm" | relative_url }})
-   [Motor Housing.3dm -
    154kb]({{ "assets/downloads/files/cnc/2008/Motor%20Housing.3dm" | relative_url }})
-   [motor housing - curves.3dm -
    29kb]({{ "assets/downloads/files/cnc/2008/motor%20housing%20-%20curves.3dm" | relative_url }})
-   [top-layout.3dm -
    150kb]({{ "assets/downloads/files/cnc/2008/top-layout.3dm" | relative_url }})
-   [top-layout-B.3dm -
    342kb]({{ "assets/downloads/files/cnc/2008/top-layout-B.3dm" | relative_url }})
-   [top.3dm -
    832kb]({{ "assets/downloads/files/cnc/2008/top.3dm" | relative_url }})

Tips for Competing at the National Level:
-----------------------------------------

1.  READ READ READ all of the provided material. While you are doing
    this, take a pen or pencil and underline all important details
    including the company they say you work for, your customer, any
    missing dimensions from the drawing, what to turn in, etc. They will
    use this documentation to try and throw you for a loop, so pay
    attention, it is purposely tricky, but at the same time very
    straight forward
2.  Time counts, but so does accuracy. According to a Judge I talked to
    at the 2009 contest, the first person to turn in a part gets 100
    extra points, then each person after that will receive about four
    less points. For example, 2nd turn in gets \~96, 3rd turn in gets
    \~92, etc. So don\'t race to get first, because surface finish and
    accuracy are worth 150 themselves I believe.
3.  Don\'t run the machine slow. 50\"/min is a pretty good bet. My first
    year at nationals, we wanted a clean finish and were over confident
    so we ran at 20ipm the entire time and didn\'t get done, don\'t let
    this happen to you
4.  The contest isn\'t all about the parts. The first part is worth
    about 1/3 of the total, the CAD drawings are worth about 1/3, and
    the Change Order/Revision is worth about 1/3 itself. So my advice
    here is *get to the change order.* If your parts aren\'t perfect,
    you may be able to make up for it by simply turning them in and
    getting the change order and allowing yourself enough time to get it
    done. 
5.  Don\'t forget you can get extra stock. If you mess up real bad,
    don\'t be shy, run up to the judges table and get another piece of
    stock and start over. One team in 2008 did this probably six times
    if I recall correctly. Now, they didn\'t win, but at least they
    weren\'t totally SOL.
6.  Don\'t believe everything you hear. Not all of the \"officials\"
    know every contest regulation. If someone answers a question for you
    and you\'re still not sure, ask the main guy, or resort to reading
    the book. I\'ve heard of a team losing a medal due to misinformation
    provided by a judge, and there\'s not much you can do about it after
    all is said and done.
7.  If you\'ve never used a real ProLight mill before, you\'re at a
    severe disadvantage. They zero parts completely different than a
    Haas or Fanuc style mill and they are just a tad quirky. Your best
    bet is to find someone with one in a shop near by and ask if you can
    use it. You definitely want some hands on experience before the
    practice day or you\'ll be struggling.
8.  Manual Facing vs. Machine facing. It\'s your choice, but doing it
    manually is easier
9.  Wear the right stuff. This has happened to me two years in a row
    now. Wear work boots and the designated contest attire (more
    information can be found at the [SkillsUSA
    website](http://www.skillsusa.org/)). On that note, remember to
    always wear your safety glasses when machines are running as any
    deemed \"safety violation\" costs you 50 points
10. Come prepared with your title block already mostly done and your
    dimensioning properties and scale already set up in a template. This
    will save you valuable time during the contest and as far as I know
    isn\'t against the rules. Keep in mind the CAD drawings are to be
    industry standard for *technical drawings.* You may have to look up
    what that means if you are unsure. At the debrief in 2009 they
    mentioned specifically that some default settings in CAD packages
    produced dimensions that were NOT in the correct style, so check
    these.
11. Your pieces will fit together. If they are not dimensioned in the
    engineering drawings remember, offsetting the line for your holes
    that fit together .005\" is a very good idea. It\'s not much, in
    fact, barely even noticeable, but it has cost my school\'s team the
    gold medal in 2006.
12. Prepare your resumes in advance. You will turn in a resume. In 2009
    Skills was trying to switch over to an all digital resume collection
    system which I guess failed. Unfortunately, we didn\'t bring paper
    copies like they advised and were forced to print them on the
    plotter on 11\"x17\" paper, and they didn\'t look good. (Printing at
    the hotel was about \$10 0.o)
