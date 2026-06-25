---
original_url: https://nick-black.com/dankwiki/index.php/Fast_UNIX_Servers
fetched_date: 2026-05-09
---

Fast UNIX Servers - dankwiki, the wiki of nick black
Check out my first novel,
midnight's simulacra
!
Fast UNIX Servers
From dankwiki
Jump to navigation
Jump to search
"I love the smell of 10GbE in the morning. Smells like...victory." - W. Richard Stevens, "Secret Teachings of the UNIX Environment"
Dan Kegel's classic site "
The C10K Problem
" (still updated from time to time) put a Promethean order to the arcana of years, with Jeff Darcy's "
High-Performance Server Architecture
" adding to our understanding. I'm collecting here some followup material to these excellent works (and of course the books of W. Richard Stevens, whose torch we merely carry). Some of these techniques have found, or will find, their way into
libtorque
, my multithreaded event unification library (and master's thesis).
FIXME
as of 2019, I need update this with information on
DPDK
,
io_uring
, and
eBPF
/
XDP
at a minimum.
Contents
1
Central Design Principles
2
Queueing Theory
3
Event Cores
3.1
Edge and Level Triggering
4
A Garden of Interfaces
5
The Full Monty: A Theory of UNIX Servers
6
DoS Prevention or, Maximizing Useful Service
7
The Little Things
7.1
Hardware Esoterica
7.2
Operating System Esoterica
7.3
Tuning for the Network
7.4
Power Consumption
8
See Also
Central Design Principles
Varghese's
Network Algorithmics: An Interdisciplinary Approach to Designing Fast Networked Devices
is in a league of its own in this regard.
Principle 1:
Exploit all cycles/bandwidth.
Avoid blocking I/O and unnecessary evictions of cache, but prefetch into cache where appropriate (this applies to page caches just as much as processor caches or any other layer of the
memory hierarchy
). Be prepared to exploit multiple processing elements. Properly align data and avoid cache-aliasing effects. Use jumbo frames in appropriate scenarios and proactively warn on network degradation (e.g., half-duplex Ethernet due to failed link negotiation).
Principle 2:
Don't duplicate work.
Avoid unnecessary copies, context switches, system calls and signals. Use double-buffering or ringbuffers, and calls like
Linux's
splice(2)
.
Principle 3:
Measure, measure, and measure again, preferably automatically.
Hardware, software and networks will all surprise you. Become friends with your hardware's
performance counters
and tools like
eBPF
, dtrace, ktrace, etc. Build explicit support for performance analysis into the application, especially domain-specific statistics.
"I thought of another moral, more down to earth and concrete, and I believe that every militant chemist can confirm it: that one must distrust the almost-the-same (sodium is almost the same as potassium, but with sodium nothing would have happened), the practically identical, the approximate, all surrogates, and all patchwork. The differences can be small, but they can lead to radically different consequences, like a railroad's switch points: the chemist's trade consists in good part of being aware of these differences, knowing them close up and foreseeing their effects. And not only the chemist's trade." - Primo Levi,
The Periodic Table
Queueing Theory
"
Introduction to Queueing
"
Little's Law
(L = λW)
Leonard Kleinrock's peerless
Queueing Systems
(Volume 1:
Theory
, Volume 2:
Computer Applications
)
Event Cores
as of Linux 5,
io_uring
is the only game in town on Linux
epoll
on
Linux
,
/dev/poll
on Solaris,
kqueue
on
FreeBSD
I/O Completion Ports
on Win32,
Event Completion Framework
on Solaris 10, POSIX.1b asynchronous I/O
liboop
,
libev
and
libevent
Ulrich Drepper's "
The Need for Aynchronous, ZeroCopy Network I/O
"
If nothing else, Drepper's plans tend to
become sudden and crushing realities
in the
glibc
world
In a
flywheel design
, maximizing topological locality of the event set becomes the hinge on which manycore efficiency turns
FIXME defend
this is a hypothesis and an active
research area
of mine
Edge and Level Triggering
Historic interfaces like POSIX.1g/POSIX.1-2001's
select(2)
and POSIX.1-2001's
poll(2)
were level-triggered
Asynchronous I/O
is pretty much by definition edge-triggered.
epoll
(via
EPOLLET
) and
kqueue
(via
EV_CLEAR
) provide edge-triggered semantics
see the
mteventqueue
document from libtorque's documentation
:
<include src="
https://raw.github.com/dankamongmen/libtorque/master/doc/mteventqueues
" />
A Garden of Interfaces
We all know doddering old
read(2)
and
write(2)
(which can't, by the way, be portably used with shared memory). But what about...
readv(2)
,
writev(2)
(
FreeBSD
's
sendfile(2)
has a
struct iov
handily attached, perfect for eg the
Chunked
transfer-encoding)
splice(2)
,
vmsplice(2)
and
tee(2)
on
Linux
since version 2.6.17
(When the first page of results for your interface centers largely on exploits, might it be time to reconsider your design assumptions?)
sendfile(2)
(with charmingly different interfaces on FreeBSD and Linux)
On Linux since 2.6.2x (
FIXME get a link
),
sendfile(2)
is implemented in terms of
splice(2)
aio_
and friends for aysnchronous i/o
mmap(2)
and an entire associated bag of tricks (
FIXME detail
)
most uses of
mincore(2)
and
madvise(2)
are questionable at best and useless at likely.
FIXME defend
broad use of
mlock(2)
as a performance hack is not even really questionable, just a bad idea
FIXME defend
use of
large pages
is highly recommended for any large, non-sparse maps
FIXME explain
mremap(2)
and
remap_file_pages(2)
on
Linux
can be used effectively at times
There's nothing wrong with
MAP_FIXED
so long as you've already allocated the region before (see caveats...)
"The linux mremap() is an idiotic system call.  Just unmap the file and re-mmap it. There are a thousand ways to do it, which is why linux's mremap() syscall is stupid." -
Matthew Dillon
"I claim that Mach people (and apparently FreeBSD) are incompetent idiots. Playing games with VM is bad. memory copies are _also_ bad, but quite frankly, memory copies often have _less_ downside than VM games, and bigger caches will only continue to drive that point home." -
Linus Torvalds
User-space networking stacks: The Return of Mach!
Linux has long had zero-copy
PF_PACKET
RX; get ready for
zero-copy TX
(using the same
PACKET_MMAP
interface
)
I'm actively using
PACKET_TX_RING
in
Omphalos
as of June 2011; it works magnificently.
"Zero-copy" gets banded about a good bit; be sure you're aware of hardware limitations (see FreeBSD's
zero_copy(9)
, for instance)
Linux 5 introduced
io_uring
and really locked down and expanded
eBPF
The Full Monty: A Theory of UNIX Servers
We must mix and match:
Many event sources, of multiple types and possibly various triggering mechanisms (edge- vs level-triggered):
Socket descriptors, pipes
File descriptors referring to actual files (these usually have different blocking semantics)
Signals, perhaps being used for asynchronous I/O with descriptors (
signalfd(2)
on Linux unifies these with socket descriptors;
kqueue
supports
EVFILT_SIGNAL
events)
Timers (
timerfd(2)
on Linux unifies these with socket descriptors;
kqueue
supports
EVFILT_TIMER
events)
Condition variables
and/or
mutexes
becoming available
Filesystem events (
inotify(7)
on Linux,
EVFILT_VNODE
with
kqueue
)
Networking events (
netlink(7)
(PF_NETLINK) sockets on Linux,
EVFILT_NETDEV
with
kqueue
)
One or more event notifiers (
epoll
or
kqueue
fd)
One or more event vectors, into which notifiers dump events
kqueue
supports vectorized registration of event changes, generalizing the issue
Threads -- one event notifier per? one shared event notifier with one event vector per? one shared event notifier feeding one shared event vector? work-stealing/handoff?
It is doubtful (but not, AFAIK, proven impossible) that one scheduling/sharing solution is optimal for all workloads
The
Flash web server
dynamically spawns and culls helper threads for high-latency I/O operations
The contest is between the costs of demultiplexing asynchronous event notifications vs managing threads
My opinion: if fast async notifications can be distributed across threads, one thread per processing element always suffices
Other opinions exist
, centered around communication bottlenecks
"Thread scheduling provides a facility for juggling between clients without further programming; if it is too expensive, the application may benefit from
doing the juggling itself
. Effectively, the application must implement its own internal scheduler that juggles the state of each client." - George Varghese,
Network Algorithmics
DoS Prevention or, Maximizing Useful Service
TCP SYN -- to
Syncookie
or nay? The "half-open session" isn't nearly as meaningful or important a concept on modern networking stacks as it was in 2000.
Long-fat-pipe options, fewer MSS values, etc...but recent work (in Linux, at least) has improved them (my gut feeling: nay)
Various attacks like
slowloris
,
TCPPersist
as written up in Phrack 0x0d-0x42-0x09,
Outpost24
etc...
What are the winning feedbacks?
fractals and queueing theory, oh my!
fixme detail
The Little Things
Hardware Esoterica
Direct Cache Access
must be supported by NICs, northbridge chipset, OS and microarchitecture
IOMMU
/ I/OAT
Checksum offloading / TSO /
LRO
/ Frame descriptors
Use
ethtool
on Linux to configure NICs (try
ethtool -g, -k and -c
)
PCI
shared bus/bus-mastering, PCIe slots/lanes (channel grouping), PCI-X, MSI
"Many times, but not every time, a network frontend processor is likely to be an overly complex solution to the wrong part of the problem. It is possibly an expedient short-term measure (and there's certainly a place in the world for those), but as a long-term architectural approach, the commoditization of processor cores makes specialized hardware very difficult to justify." - Mike O'Dell, "
Network Front-end Processors, Yet Again
"
What about robustness in the face of hardware failure? Actual hardware interfaces (
MCE
,
IPMI
, CPU and memory blacklisting) ought mainly be the domain of the operating system, but the effects will be felt by the application. If a processing unit is removed, are compute-bound threads pruned?
Operating System Esoterica
The Linux networking stack is a boss hawg and a half. Check out the
Linux Advanced Routing and Traffic Control
(LARTC) HOWTO for details
ad nauseam
See my
TCP
page -- auto-tuning is pretty much to be assumed (and best not subverted) in recent Linux/FreeBSD
When extending
MAP_NOSYNC
maps on FreeBSD, be sure to
write(2)
in zeros, rather than merely
ftruncating
(see the
man page's warning
)
Linux enforces a systemwide limit on LVMAs (maps):
/proc/sys/vm/max_map_count
Tuning for the Network
All hosts ought employ the RFC 1323 options (see
Syncookies
regarding contraindications there)
Avoid fragmentation: datagram services (UDP, DCCP) ought ensure they're not exceeding PMTUs
LAN services ought consider jumbo frames.
There is little point in setting IPv4 TOS bits (RFC 791, RFC 1349); they've been superseded as DiffServ/ECN (RFC 3168)
IPv6 does away with this entire concept, using flow labels and letting the router decide
Power Consumption
Less power consumed means reduced operating cost and less waste heat, prolonging component life.
Using on-demand CPU throttling (
ACPI
P-states, voltage reduction) is a no-brainer, but requires dynamic control to be effective.
Be sure it's enabled in your OS and your BIOS; more info
here
Sleep states (architectural changes) are useful outside environments pairing low-latency requirements with sporadic traffic
Even aggressive power-saving
ACPI
C-states
wake up in usec
Don't wake up disks when it's not necessary; try using tmpfs or async for transient logging, and don't log MARK entries
If your app doesn't use disk directly, consider PXE booting and network-based logging
Avoid periodic taskmastering and timers where available, using event-driven notification (more effective anyway!)
Use as
few processing elements as completely as possible
, so that CPUs and caches can be powered down
This also applies, of course, to machines in a cluster
See Also
"mteventqueues"
by Your Humble Wikist, and likewise
libtorque
"Scaling Linux Services Before Accepting Connections"
by Theo Julienne, 2020-07-03
"Poll vs Epoll, Once Again"
by Jacques Mattheij, 2010-08-04
"Poll, Epoll, Science, and Superpoll"
by Zed Shaw
"Buffered Async I/O"
on Jens Axboe's livejournal (
axboe
)
"Asynchronous I/O on linux OR: welcome to hell"
by Devin McCall
"Linux: epoll performance and gotchas"
on Gerard Toonstra's
blog
"epoll, threading"
on
lkml
, 2007-05-26
"sendfile(): fairly sexy (nothing to do with ECN)"
on
lkml
, 2001-01-27
"rfc: threaded epoll_wait thundering herd"
on
lkml
, 2007-05-04
"epoll: fix for epoll_wait sometimes returning"
on
lkml
, 2009-02-24
">10% performance degradation since 2.6.18"
on
lkml
, 2009-06-02
"
rps: Receive packet steering
" on linux-network, 2009-11-11
"sharing memory map between processes (same parent)"
on comp.unix.programmer
Stuart Cheshire's
"Laws of Networkdynamics"
and
"It's the Latency, Stupid"
"some mmap observations compared to Linux 2.6/OpenBSD"
on freebsd-hackers
"mremap help? or no support for FreeBSD?"
on freebsd-hackers
"mmap() sendfile()"
on freebsd-hackers
"
Implementation of mmap() on FreeBSD
" on freebsd-hackers (1999-06-26)
"
read vs mmap (or io vs page faults)
" on freebsd-questions (2004-06-20)
"Edge-triggered interfaces are too difficult?"
on LWN, 2003-05-16
"Toward a kernel events interface"
on LWN, 2006-08-01
"The Return of Kevent?"
on LWN, 2007-05-10
LWN's
2003-03-05 article
on
remap_file_pages(2)
"epoll ready set loops diet"
on LWN, 2007-02-28
"
Linux and TCP Offload Engines
" on LWN, 2005-08-22
"
Interrupt Mitigation in the Block Layer
" on LWN, 2009-08-10
"
JLS2009: Generic receive offload
" on LWN, 2009-10-27
"Edge- vs Level-Triggered Events"
on Pierre Phaneuf's livejournal (
pphaneuf
)
"Linux Event Handling"
on Ulrich Drepper's livejournal (
udrepper
) (2006-10-31)
"
glibc 2.10 news
" on Ulrich Drepper's livejournal (
udrepper
) (2009-04-17)
"edge-triggered vs level-triggered epoll in kernel 2.6"
on comp.unix.programmer, 2004-12-01
Ian Barile's 2004-02 Dr. Dobb's Journal article, "
I/O Multiplexing & Scalable Socket Servers
"
2006-04-21 KernelTrap article
"Linux: vmsplice() versus COW"
covers lively debate of
vmsplice(2)
vs FreeBSD's ZERO_COPY_SOCKET
"
Implementation and Analysis of Large Receive Offload in a Virtualized System
", 2008 paper by Takayuki Hatori and Hitoshi Oi
"
Large Receive Offload implementation in Neterion 10GbE Ethernet driver
" from proceedings of the 2005 OLS
"Using epoll() For Asynchronous Network Programming"
"
Lazy Asynchronous I/O for Event-Driven Servers
", 2004 USENIX paper by Khaled Elmeleegy, Anupam Chanda, and Alan L. Cox (
pdf
)
"
The context-switch overhead inflicted by hardware interrupts (and the enigma of do-nothing loops)
", 2007 Experimental Computer Science, Dan Tsafrir
"
Patches and Documents related to Page Fault Performance in the Linux Kernel
" at SGI
PipesFS
at Vrije Universiteit Amsterdam
Retrieved from "
https://nick-black.com/dankwiki/index.php?title=Fast_UNIX_Servers&oldid=10058
"
navigation menu
Personal tools
log in
Namespaces
page
Discussion
English
Views
Read
view source
View history
More
Search
recent changes
all pages
Tools
what links here
related changes
special pages
printable version
permanent link
page information
modified on 22 May 2023 at 20:49.
copyright © 2008–2026 nick black. all rights worth shit.
privacy policy
about dankwiki
disclaimers
mobile view