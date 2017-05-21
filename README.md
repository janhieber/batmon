# Monitor laptop battery state

Batmon is a daemon that monitors the state
of laptop batteries.  
I have written this because
most available tools can't handle multiple batteries.

Also this does not have a GUI, so is pefect for
tiling WMs.

## It does two things
Calculate the battery life over all
available batteries and make it available
via a state file (I use it for i3blocks/i3bar).

Hibernate/suspend the machine when estimated
battery life falls under a limit.

## Why another app
Both things need an accumulated time calculated
for both batteries. Most tools calculate
battery life separate for each battery, this
is bullshit and not useful.

The other thing is, I don't want fancy apps with GUI
and tray icon. I want a background daemon that can
handle the low battery action and share the estimated
battery life with apps like i3bar/i3blocks.

## Notes
Currently, I use a polkit rule to get permission to
suspend or hibernate. This is bad and should work with
group permissions or something else...

Do not mistake this with http://www.nongnu.org/gap/batmon/index.html.
These are different projects with different purpose.

