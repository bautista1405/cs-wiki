---
original_url: https://nick-black.com/dankwiki/index.php/UNIX_Weapons_School
fetched_date: 2026-05-09
---

UNIX Weapons School - dankwiki, the wiki of nick black
Check out my first novel,
midnight's simulacra
!
UNIX Weapons School
From dankwiki
Jump to navigation
Jump to search
Lecture slides are available
here
. These slides are very much a work in progress; LaTeX source is available on
GitHub
.
Accept the challenges so that you can feel the exhilaration of victory.
-- George S. Patton
On March 3, 1969, the United States Navy established an elite school for the top one percent of its pilots. Its purpose was to teach the lost art of aerial combat and to ensure that the handful of students who graduated were the best fighter pilots in the world. They succeeded. Today, the Navy calls it Fighter Weapons School. The flyers call it: TOP GUN.
UNIX Weapons School is an intense elective practicum.
Its goal is to train formidably competent systems programmers.
update from 2021: this class would now absolutely go into
io_uring
and
eBPF
. also SSDs and the resultant changes to the I/O paradigm. there would probably be some talk of Spectre/Meltdown in conjunction with the architecture lecture, also BIG.little and core scheduling. probably a bit more coverage of
ARM
details, though i'll not yet yeet the x86 stuff. the "future of systems programming section" would be updated. a bit more talk about distributed systems, probably, and i'd discard the current material about machine learning. other than that, this still pretty much stands.
Contents
1
Lectures thus far
1.1
2013-05-14 Greetings and Salutations
1.2
2013-05-16 Computer Architecture
1.3
2013-05-21 The x86
1.4
2013-05-23 UNIX Development
1.5
2013-08-01 FINAL EXAM SUMMER 2013
2
Cheating
3
Motivation
4
Grading
5
Week 1: C/C++ development in the x86 UNIX environment
6
Week 2: Systems methods for efficient use of memory and buses
7
Week 3: Algorithmic methods for efficient use of CPU and memory
7.1
Algorithms for event systems
8
Week 4: Compilers and their limitations
9
Week 5
9.1
Allotrios
9.2
Parallelism I: Hardware Parallelism
10
Week 6: Parallelism II: Software Parallelism
11
Week 7: Effective use of intranets and the Internet
12
Week 8: Heterogeneity
12.1
Hardware
12.2
Software
13
Week 9: The future of systems programming
14
Thanks
Lectures thus far
2013-05-14 Greetings and Salutations
"
Intro + official junk
"
Motivation
Class policies
Self-assessment
"
Big-O Ain't What it Used to Be
"
Review of asymptotic complexity
Case study: The impact of hardware upon matrix multiplication
2013-05-16 Computer Architecture
"
Your Friend the Computer
"
CMOS power equations and pipelining
Superscaler and out-of-order
Delays in dynamically pipelined processors
2013-05-21 The x86
"
The x86 is dead. Long live the x86!
"
Guided tour of the x86's history
Core frontend + backend
x86+SSE+VEX instruction set
2013-05-23 UNIX Development
"
Not Sucking in the UNIX Environment
"
Shell
C development: Autotools, gcc, binutils
C++ development: CMake, g++/clang
Debugging: gdb, valgrind, strace, ltrace
2013-08-01 FINAL EXAM SUMMER 2013
UWC Summer 2013 Final Exam
Cheating
If you feel predisposed to cheating,
I urge you to drop the class
. I will seek out cheating via comparison of compiled object code, statistical analysis of unit test results, and other methods. If you cheat in my class, I will use any influence I have to see you removed from my Institute and blacklisted from my industry. I will haunt you, yelling obscenities and bizarre threats for your life's pitiful remainder. My children will target your children for beatings, for unto seventy times seven generations.
Motivation
"The TOPGUN course is designed to train already experienced Navy and Marine Corps aircrews at the graduate level in all aspects of strike-fighter aircraft employment, including tactics, hardware, techniques and the current world threat for air-to-air and air-to-ground missions. The course includes eighty hours of lectures and twenty-five flights that pit students against TOPGUN instructors. When a pilot or WSO completes the TOPGUN course he/she will return as a Training Officer carrying the latest tactical doctrine back to their operational squadron, or go directly to an FRS squadron to teach new aircrews."
Without systems programmers, hardware sits silent, stillborn. Without systems programmers, application designers shout mutely into a void.
The reconfigurability of software combined with the system bounding of hardware allows the systems programmer the broadest space with which to innovate. Unfortunately, most of these possible innovations are just bugs, or (within the innermost ring) superbugs. When that signed vs unsigned comparison means the wrong hard drive sector is selected, it can ruin your whole day. Systems programming unites the most fundamental realms of our science:
programming language theory
,
compiler design
,
architecture
, and algorithms come together in practical application. These theories are complex enough to demand classes of their own. Here, we will integrate these prerequisite theories to deliver efficient, robust systems software solutions. Furthermore, you'll become acquainted with the gritty details of cutting-edge technique.
Grading
"Classes typically lose around 70–80% of their trainees, either due to DORs (Drop-on-Requests) or injuries sustained during training, but it is not always easy to predict which of the trainees will DOR. SEAL instructors say that in every class, approximately 10 percent of the students simply do not have the physical ability to complete the training. Another 10–15 percent will definitely make it through unless they sustain a serious physical injury. The other 75–80 percent is 'up for grabs' depending on their motivation."
-- Basic Underwater Demolition/SEAL training, as described in Dick Crouch's
The Warrior Elite: The Forging of SEAL Class 228
(2001)
"Qui si convien lasciare ogne sospetto; ogne viltà convien che qui sia morta."
-- Dante Alighieri,
The Inferno
, Canto III, 14-15
Because I am hard, you will not like me. But the more you hate me, the more you will learn.
Each project will be evaluated for both correctness (in terms of unit tests passed) and performance (on several reference platforms). Performance of incorrect code is, of course, moot. I will make each project public two weeks prior to its due date, and provide a set of basic unit tests and a web-accessible oracular reference implementation (you can submit inputs and receive outputs). For details of grading, see the first week's slides. I am using a scheme designed to maximize competition and conflict between class members, which I hope will reduce cheating, lead to great personal exertions, and possibly get a chair thrown.
Week 1: C/C++ development in the x86 UNIX environment
SHELL LIFE aka Things I Hope You Already Know
Job control
GNU readline
SSH tricks
effective use of interactive shells
shell scripting idioms.
rant: code is data and data is code so keep your home directory in source control
HOW COAL BECOMES CAT PICTURES aka Attack of the clone()s
UEFI. UNIX boot sequence.
Everything you wanted to know about /dev and /sys and /proc but never found out.
Where a process comes from, what composes it while alive, and where it goes when it dies.
lsof, netstat, memstat, etc
C/C++ UNIX DEVELOPMENT aka Onward Christian Soldiers
Highlights of
GCC
, G++, LLVM, Clang, ICC, and NVCC.
GNU Make
strace, ltrace, ptrace().
GDB tricks.
Profiling with perf.
UNIX resource management.
Linker tricks both stupid and less stupid.
The C and C++ machine models.
THE WORLD FATHER aka UNIX
The Linux virtual memory implementation on x86
The FreeBSD/Dragonfly virtual memory implementation
The Linux process schedulers
The Linux I/O schedulers
OUR EARTH MOTHERS aka C/C++
The system call interface.
Process-level memory management.
The C standard library.
Xmacros
/ The STL.
A glimpse of template metaprogramming
Week 2: Systems methods for efficient use of memory and buses
YOUR FRIEND THE COMPUTER aka Computer Architecture in Thirty Minutes.
Intel Core processors.
The memory hierarchy.
Branch prediction.
SIMD
.
Memory fences.
Transactional memory.
Predication.
DOUBLE-COPIED I/O aka Definitely More Copying Than Required.
C/C++ I/O using stdio.h and streams. Interactions of standard library buffering and I/O.
Semantics and side-effects of the I/O model.
popen() and the seven thousand ways it can be incorrectly used.
SINGLE-COPIED I/O aka Not Good Enough, Try Again.
UNIX I/O using bytestreams, datagrams, and sequenced packets.
The AF_UNIX namespace.
That mysterious EAGAIN.
ZERO-COPY I/O aka Now We're Getting Somewhere.
Mmap and shared memory.
TLB invalidation and IPIs
CLONE_VM and a glimpse of threads.
RDMA. The PCIe bus.
NEGATIVE-COPY I/O aka Oh Shit! There Go My Pages!
COW games.
sendfile() and TCP.
splice() your way to success.
MORE MEMORY aka When in Doubt, Blame Memory.
Interactions of disk, disk paging, memory paging, caching, registers, and multiprocessing.
Memory characteristics of long-lived programs.
Life in a post-paged world.
Computational memory.
NUMA and you.
Week 3: Algorithmic methods for efficient use of CPU and memory
IN THE GRIM FUTURE OF WEEK 3 THERE ARE NO AKAs, ONLY ALGORITHMS
Searching small spaces: Constant sorts (sorting networks). Dancing links. Timer wheels.
Searching large spaces: Trees. PATRICIA tries. Skip lists. Suffix trees. Automata search. Interval trees.
Searching by content: Hashes. Algorithmic complexity attacks. Universal hashes. Cuckoo hashing. Adaptive perfect hashes.
Searching huge spaces:
VLHU
. Enumeration by method of linear congruence and other space-filling parlor tricks.
Real-time machine learning: Support vector machines. Non-negative matrix factorization. Hierarchal hashing. Hidden Markov models.
Three impossible things before breakfast: Detecting an infinite loop, transforming an infinite list, and computing without executing.
Yes, You Really Have to Learn Fourier Transforms.
Algorithms for event systems
select(), poll(), interaction with signals
Linux's epoll, FreeBSD's kqueue. Level- vs edge-triggered events.
Algorithms for oneshot edge-triggered interfaces. Asynchronous I/O on POSIX systems.
Everything as events: timerfd, signalfd, V_NODE
Wrapping pthread events. Multithreaded event engines. Work queues, work stealing, tasklets.
Digression: Kernel threads and interrupt handlers
Robust systems and judicious fork()ing
libev, libevent, libtorque
Week 4:
Compilers
and their limitations
SSA and Basic Blocks, aka Planet of the Compilers
The Banerjee Test and the Polyhedral Model, aka Beneath the Planet of the Compilers
The limits of compiler-based optimization, aka Escape from the Planet of the Compilers
Inline assembly, aka Conquest of the Planet of the Compilers
PGO and Genetic-O aka Battle for the Planet of the Compilers
Week 5
Allotrios
Windows aka Unfathomably Wretched Function Naming: I/O Completion Ports. With Fibers come Heaps.
Libraries: objdump, nm, and how to design a shared library.
Internationalization. UTF8
Unpleasant Details of the UNIX Environment aka What Stevens Forgot to Tell You.
The OOM killer.
Atime.
Fragmentation, a spectre haunting your userspace.
Hardware failures.
Build systems aka They're All Shite
Parallelism I: Hardware Parallelism
Models of parallelism aka They're All Shite
Bit-level parallelism
Parallelism within a register
Parallelism among instructions
Parallelism among memory accesses
Week 6: Parallelism II: Software Parallelism
Parallelism among tasks
Algorithms simulating parallelism and nondeterminism.
POSIX threads
. Userspace threading. Coroutines.
Parallel languages and libraries. IPP and TBB.
Week 7: Effective use of intranets and the Internet
Sampling theory of Nyquist
Queueing theory of Kleinrock. The Linux packet queue disciplines.
The Internet backbone. Preserving service via anycast networking. Threats to the Internet. PMTUD / MSS black holes.
Bufferbloat. Perils of the end-user network. Hardware design of fast networking devices. The CODEL and CAKE queue disciplines.
IPv6. Algorithms for IPv6. Zeroconf. PXE. Ad-hoc and mesh networking. Algorithms for fragmentation and sequencing. Intranet threats.
Packet sockets
. Linux's netlink(7).
Local topology discovery
Week 8: Heterogeneity
Hardware
TCP offload engines
SolarFlare's OpenPacket
Microsoft AMP
NVIDIA's
CUDA
OpenCL
Software
System / guest emulation
Transmeta CMS (Code Morphing Software)
Popek and Goldberg virtualization requirements / KVM / Xen
Week 9: The future of systems programming
C++11
Amorphous computing
RAIN/RAIM, EMC-aware programming
COMA, ccNUMA, directories, SCI, SCA
Computational memory
Software-defined networking
MRAM / FeRam / PRAM / SONOS
Thanks
Bill Leahy, for causing GT to pick UWS up as a class, at a time when it was nothing more than a single-page PDF flyer.
David Kanter of
Real World Tech
for use of his superb processor diagrams, and his years of insightful writing besides.
Richard Bejtlich's and TaoSecurity's
TCP/IP Weapons School
from BlackHat 2007, for nomenclature.
...and through them, of course, to the United States Navy's
Fighter Weapons School
aka "Top Gun".
Retrieved from "
https://nick-black.com/dankwiki/index.php?title=UNIX_Weapons_School&oldid=10066
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
modified on 23 May 2023 at 06:20.
copyright © 2008–2026 nick black. all rights worth shit.
privacy policy
about dankwiki
disclaimers
mobile view