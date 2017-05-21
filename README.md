# Monitor laptop battery state

Batmon is a tool that monitors the power state
of laptop batteries.  
I have written this because
most available tools can't handle multiple batteries.

# It does two things
Calculate the estimated runtime over all
available batteries and make it available
via a state file (I use it for i3blocks/i3bar).

Hibernate/suspend the machine when estimated
battery runtime is too low.

# Why another app
Both things need an accumulated runtime calculated
with both batteries. Most tools only calculate the
runtime of the battery currently in use and dismiss
the other one (I have a Thinkpad T440s).

The other thing is, I don't want fancy apps with GUI
and tray icon. I want a background daemon that can
handle the low battery action and share the erstimated
battery runtime with things like i3bar/i3blocks.

# Notes
Currently, I use a polkit rule to get permission to
suspend or hibernate. This is bad and should work with
group permissions or something else...

Do not mistake this with http://www.nongnu.org/gap/batmon/index.html.
These are different projects with different purpose.

