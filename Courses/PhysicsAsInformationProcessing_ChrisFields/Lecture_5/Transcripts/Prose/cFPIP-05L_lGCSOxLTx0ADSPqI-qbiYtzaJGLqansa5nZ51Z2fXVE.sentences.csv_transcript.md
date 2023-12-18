
00:06 _Daniel:_
[[start:6720][end:8348]] Hello and welcome, everyone.
[[start:8514][end:15624]] It is September 14th, 2023, and we are in the course: Physics as information processing.
[[start:15752][end:17150]] It's lecture 5.
[[start:18080][end:20904]] Looking forward to this lecture and then a little conversation.

00:20 [[start:20952][end:21884]] Chris, off to you.
[[start:21922][end:22670]] Thank you.

00:24 _Chris:_
[[start:24800][end:25596]] Okay.
[[start:25778][end:27100]] Thank you, Daniel.
[[start:27840][end:32340]] And, welcome to session 5 of Physics of information processing.
[[start:33400][end:46680]] And, today we're going to talk about Spacetime, and particularly about the idea that Spacetime is emergent from information processing.
[[start:47340][end:54940]] And, this has now become a very mainstream idea in the quantum information and quantum gravity communities.

00:57 [[start:57360][end:65580]] And there are still, of course, some people holding out for the idea that Spacetime is fundamental.
[[start:66260][end:93000]] But I would say that, at least in these communities, I expect it's become now the dominant idea that Spacetime is not fundamental, that Spacetime is not part of the basic ontology of reality or something like that, and that instead, Spacetime is a construct.

01:33 [[start:93660][end:98570]] So, that's what today's Session is going to be about.
[[start:99740][end:123360]] So, for those of you who are just joining or who would like a little review, we started this course talking about Quantum Information Theory and the idea that Quantum Information Theory is actually a new science about systems that communicate across a boundary.
[[start:123700][end:137632]] And, the systems are always called Alice and Bob for kind of historical reasons. And, we emphasized that this new science is topological.

02:17 [[start:137696][end:140752]] It's about connectivity between systems.
[[start:140816][end:142596]] It's not geometric.
[[start:142788][end:146436]] So, it doesn't assume a Spacetime embedding.
[[start:146628][end:152100]] So, it leaves open the possibility that Spacetime is actually a construct.
[[start:152180][end:155150]] It doesn't assume Spacetime up front.

02:36 [[start:156560][end:179824]] And, in the 2nd Session of the course, I think, we talked about how this boundary could always be represented as an array of qubits, and that what the systems on each side of the boundary do to communicate is prepare and then measure the states of these qubits.
[[start:179872][end:191440]] So, they communicate by exchanging classical information via a quantum channel.
[[start:192390][end:206630]] And, this introduces a particular kind of quantum noise whenever they don't share the reference frames that they use to prepare the bits and measure the bits.
[[start:206970][end:217646]] So, it's not necessarily a perfect communication channel from a classical fidelity point of view, but all of the noise is quantum noise.

03:37 [[start:217698][end:225100]] It's not classical, and it always derives from differences in the reference frames that are used by the two agents.

03:46 [[start:226830][end:236480]] We reformulated the Free Energy Principle in this setting, and the Free Energy Principle turned out to be very simple.
[[start:237010][end:245170]] It turns out to be a classical limit of the Principle of Unitarity, which is just the principle that information is conserved.
[[start:245750][end:258290]] And, we saw that the approach to perfect alignment between the two agents, or perfect prediction on the part of the two agents, becomes more challenging.
[[start:258370][end:261590]] Not surprisingly, as system complexity increases.
[[start:262330][end:269180]] So, the more complex the communication, the harder it is to predict, as one would expect.

04:30 [[start:270910][end:282240]] In the last Session, we talked about how constraints on thermodynamic free energy induce compartmentalization in agents.

04:43 [[start:283250][end:299810]] So, whenever agents interact with their environments in fairly complex ways, then they end up being compartmentalized into compartments that have to communicate classically.
[[start:300310][end:304986]] And, this is solely a result of Quantum Information Theory.
[[start:305038][end:314562]] You don't have to assume any biology to get this compartmentalization, but clearly, this is something that we see in biological systems.
[[start:314626][end:330250]] Not only do we see compartments, we also see hierarchical control, which is likewise a sort of automatic outcome of the theory for complex systems.

05:30 [[start:330850][end:349620]] And finally, last time, we talked a little bit about how these compartments communicate and introduced the idea of communication protocols that involve local operations on a shared quantum resource of some kind and classical communication.
[[start:352014][end:366754]] We talked to fair amount about how classical communication is a little bit problematic to define in Quantum Theory, because, of course, you're introducing classicality.
[[start:366802][end:372730]] And so, you have to make some very specific assumptions about what's classical.
[[start:373470][end:386270]] And, we'll see later on today what the key assumption that gives you classicality is, as we talk about Spacetime.

06:27 [[start:387730][end:395220]] But before I go into the topic of Spacetime, I want to spend a little time.
[[start:397110][end:399300]] Okay, sorry.
[[start:399750][end:400962]] This is where we're going.
[[start:401016][end:406360]] We're talking about Spacetime, and we'll talk about applications to biology next time.
[[start:407050][end:413030]] But before we get going on this, I want to spend a little bit of time talking about the explanation.

06:53 [[start:413930][end:427100]] And, this is motivated by a question that came up, a very long question that touched on many different topics that came up in the interactive Q&A last time.
[[start:428990][end:450450]] And, a fair amount of that question had to do with, directly or indirectly, the question of what scale-free explanation looks like and how it compares to scientific explanation in general, most of which is reductive.
[[start:451590][end:469514]] So, I want to make a short detour into the question of how reductionist theories, which all of you are probably very familiar with, relate to scale-free theories, and particularly the Free Energy Principle is a scale-free theory.

07:53 [[start:473070][end:484240]] So, it's a theory that's unlike most of the theories that most of you probably learned about in college.

08:05 [[start:485090][end:500994]] So, we're all familiar with reductionist theories and the reductionist idea of scientific explanation, which is really an outcome of the Philosophy of Science in the 1920s and 1930s.
[[start:501032][end:510280]] People like Rudolph Carnap were among the first to actually make precise what this idea of reductive explanation is.
[[start:511050][end:531920]] But the basic idea is that the laws or the dynamics or the formalism that describes the behavior at some microscale, the behavior of little things actually explains the behavior of big things.
[[start:532610][end:541680]] So, the basic reductionist idea is that what the little things are doing is what's important.

09:02 [[start:542710][end:551422]] And, what big things are doing are either emergent phenomena, or they're just epiphenomena.

09:11 [[start:551566][end:553890]] They're essentially just appearances.
[[start:555050][end:558898]] And, this defines a fundamental scale.
[[start:559074][end:574998]] So, the real assumption in any reductionist theory is that there's some fundamental scale at which the "real dynamics" takes place and everything else is just an appearance, or it's some sort of emergent phenomenon.
[[start:575174][end:584874]] And, I try to be very careful when I use the word "emergence" because it's one of the most ambiguous words in the Philosophy of Science.

09:44 [[start:584922][end:587680]] And people use it to mean all sorts of different things.

09:50 [[start:590050][end:599380]] But whenever you say "emergent", it always sort of implies the idea that it's emergent from something.
[[start:600310][end:617350]] And, so the idea of emergence is essentially a reductionist idea because it at least implicitly assumes that there's some microscale from which the macroscale is emergent.

10:18 [[start:618430][end:630460]] And so, the discussions of emergent phenomena are often very consistent with reductionism, even if they claim not to be.
[[start:631570][end:638670]] And, we're all taught that science is reductionist.
[[start:639250][end:644930]] And, there are certainly people who publicly claim that science is reductionist.

10:45 [[start:645750][end:650340]] Richard Dawkins is certainly a shining example of this.
[[start:651430][end:679740]] But I suspect that a lot of scientists just kind of play lip service to reductionism without really believing in it, because they don't really believe that the macroscopic phenomena that they are studying, life, for example, is completely determined by what's going on at the microscale, or what's going on at the microscale, plus some stochastic noise or something like that.

11:20 [[start:680450][end:686910]] So, I want to explicitly contrast this with a scale-free theory.
[[start:687730][end:696050]] In a scale-free theory is not simply a holistic theory, it's much more precise.
[[start:696390][end:709590]] In a scale-free theory, little things and big things obey the same laws, or they have the same dynamics, or they're described by the same formalism.

11:50 [[start:710330][end:715110]] So it's not that the macro scale is emergent from the microscale.
[[start:715770][end:720410]] The macro scale and the microscale actually obey the same laws.
[[start:721470][end:730250]] And, the relationship between macro and micro is probably best stated as one of implementation.

12:12 [[start:732350][end:740480]] Macro scale things have microscale components, and those microscale components are doing something or other.

12:20 [[start:740930][end:749410]] And, whatever they're doing implements the macroscale system and its behavior.
[[start:750950][end:761960]] But this implementation is not an explanation, or at least it's not an explanation all by itself.
[[start:762730][end:766866]] And the bumper sticker version of scale-free theories is just as above, so below. Whatever laws you have at the macro scale, are the ones, the same ones you have at the microscale, and vice versa.

12:54 [[start:774838][end:777498]] So, scale-free theories, in a sense, are simple.
[[start:777584][end:781470]] It's the same theory at every level of description.
[[start:783330][end:791520]] So, what is this idea of scale, and how does it relate to what we've talked about in this course?
[[start:792450][end:799090]] Well, what we've talked about in this course all has to do with what an agent can observe on its boundary.
[[start:799590][end:810360]] So, scale has to do with how information is encoded on the boundary, and we can describe that scale in many different ways.

13:31 [[start:811770][end:821340]] Here's a commonplace way to describe it in Physics by a relationship between energy and distance, or size.
[[start:822590][end:828250]] And, you've probably all heard of the Planck scale.
[[start:828910][end:833840]] The Planck scale is the smallest scale at which current Physics makes any sense.

13:56 [[start:836930][end:847650]] And, in energetic terms, it's defined by energies on the order of 10 to the 19th GEV, which is gigaelectronvolt.

14:09 [[start:849750][end:858738]] The LHC (the Large Hadron Collider) in Switzerland gets to about 10 to the 4th GEV.
[[start:858834][end:863190]] So many, many orders of magnitude less than the Planck scale.
[[start:863930][end:870170]] So the Planck scale is extremely energetic compared to what we can probe experimentally.
[[start:871710][end:884110]] The Planck scale energy of 10 to the 9th GEV corresponds to a distance of about 10 to the -35 meters, which is incredibly tiny.

14:45 [[start:885410][end:890970]] An intermediate scale on this diagram is about the scale of a nucleon.

14:51 [[start:891050][end:901410]] So, for example, a proton or a neutron, they have a rest mass of about 1 GEV and a size of about 1 femtometer.
[[start:901830][end:906550]] So, this intermediate scale is roughly the scale of nucleon Physics.
[[start:907930][end:927066]] And, then if you go to our scale, the scale of things that are about a meter in size, human beings, tables, and chairs, lots of animals, the things we're most familiar with, that corresponds to an incredibly tiny energy 10 to the -5 electron volts, which is about the energy of a photon of radio... radiation. And, a meter is about the wavelength of long wave Radio.
[[start:941970][end:951966]] So, if you think about visible light, it has a wavelength of about 10 to the -5 meters, an energy of about an electron volt.

15:52 [[start:952078][end:967670]] So, it's not surprising that visible light feels energetic to us because it's orders of magnitude above our natural scale of energy of this sort of thermal environment in which we exist.
[[start:968990][end:984640]] So, it's the encoding scale and the boundary that is going to relate theories of things that we see to each other.
[[start:985490][end:988874]] And, this ends up giving a kind of complicated picture.
[[start:988922][end:994770]] If you think of Alice interacting with Bob and measuring things on the boundary...

16:39 [[start:999890][end:1001790]] Sorry, I'm a little bit ahead of myself.
[[start:1001940][end:1004954]] I just wanted to show you a picture of a Reductive Theory.
[[start:1005002][end:1005994]] This is the Big Bang.
[[start:1006042][end:1007700]] You're all familiar with this.
[[start:1008070][end:1017220]] Something happens at the Planck scale, and the entire universe results from it by just a scale change.

16:57 [[start:1017670][end:1020626]] So this is a Reductive Theory.
[[start:1020818][end:1023830]] A scale-free theory is much more complicated.
[[start:1024650][end:1027720]] So here's what a scale-free theory looks like.
[[start:1029050][end:1037962]] Alice interacts with Bob, and she's looking at her boundary, and her boundary states, the boundary states she sees could be encoded at different scales.

17:23 [[start:1043070][end:1048080]] So, there may be a small-scale scale1 and a bigger scale scale2.
[[start:1049330][end:1059200]] And, what Alice is looking for is some sort of theory that relates the first scale, the microscale, to the macro scale.

17:42 [[start:1062930][end:1069540]] So, it's not that the microscale came first like it did in the Big Bang, and the macro scale came later.

17:51 [[start:1071770][end:1075430]] These are encodings that can be happening simultaneously.
[[start:1076090][end:1083494]] And the theoretical task is to find theories that relate between these scales.

18:03 [[start:1083542][end:1091020]] And these are implementation theories, or you might call them embedding theories from one scale into another.
[[start:1092110][end:1099982]] And what we want as a consistency criterion is for these theories to be constant in time.
[[start:1100036][end:1102400]] So as Bob evolves in time and what Alice sees are these encodings on her boundary.
[[start:1107918][end:1117220]] She wants the relationship between encodings at different scales to stay constant, because if it doesn't, she'll never be able to figure anything out.
[[start:1118870][end:1125960]] She'll just have this chaotic relationship between things happening at different scales, and nothing will make sense.
[[start:1127690][end:1133130]] So, you have this complicated picture in scale-free theories.
[[start:1133470][end:1154510]] And, if you look at this and it seems vaguely familiar, or even vaguely... even very familiar then it should, because this is exactly the kind of explanatory structure or semantic structure that you have in Computer Science.

19:16 [[start:1156050][end:1170390]] If you're studying the behavior of a computer, which is just some piece of hardware, some physical system, then you can describe what that piece of hardware is doing at different scales.
[[start:1170970][end:1187878]] And, in fact, what we call "the hardware level of description" when we talk about our laptops, for example, is typically the level of description of circuits and transistors inside microprocessors.
[[start:1187974][end:1190010]] We think of that as "the hardware level".
[[start:1190160][end:1208020]] But of course, that's just a description, too, that's layered on top of lots of much smaller scale dynamics, all the way down to the scale of atoms and eventually nuclei and elementary particles and all that other stuff.
[[start:1208710][end:1217250]] So, there's some quantum stuff that's going on that we describe as having a classical hardware level of bit exchange.

20:18 [[start:1218550][end:1223320]] And then, we describe the behavior of programs on top of that.
[[start:1224650][end:1240134]] So, what we want, what makes a computer useful is that we can assign semantics to programs, and we can talk about semantic relationships between programs.
[[start:1240182][end:1258900]] For example, the relationship between the internet protocol stuff that Zoom is doing and what you actually see on your user interface and hear on your user interface. That needs to stay fixed over time or Zoom becomes incomprehensible and not programmable and, in fact, not even well defined as an algorithmic system.
[[start:1268470][end:1277080]] And, the same is true for the relationship between the operating system and the hardware description, or between the operating system and Zoom as a program.

21:17 [[start:1277850][end:1284666]] So, Computer Science works in exactly this scale-free way.

21:24 [[start:1284848][end:1291462]] And so, in a sense, the scale-free explanation is very familiar.
[[start:1291526][end:1296618]] It's exactly the kind of explanation that we have in Computer Science.
[[start:1296794][end:1310850]] And, that's why I referred to the relationship between scales as one of implementation because that's a term that we're familiar with from thinking about computers implementing programs.
[[start:1311910][end:1314046]] So, what are these theories?

21:54 [[start:1314238][end:1339210]] If we think in biological terms, we can think of pathways being embedded in a cell, or cells being embedded in tissues, all the way up to niches of various kinds, which may be social niches being embedded in ecosystems, and ecosystems being embedded in the biosphere.
[[start:1339550][end:1348670]] And so, we have all of these essentially semantic theories that talk about how one scale embeds in another scale.

22:29 [[start:1349650][end:1376310]] And, if we have these sorts of scale transitions, we can think of representing the relationship between transitions at different scales in terms of the activity of some kind of renormalization group, which is transforming entities and processes at one scale into entities and processes at another scale.
[[start:1377210][end:1403470]] And I think in Biology, we can at least put forward the hypothesis that in all the way from pathways embedding in cells to ecosystems embedding in the biosphere, we could put forward the hypothesis, at least, that the renormalization group flow across all of these scales is trivial.
[[start:1404290][end:1428146]] That is that the embedding theories all have the same formal structure, that the structure that describes how pathways embed into cells is the same structure that describes how ecosystems embed into the biosphere.

23:48 [[start:1428338][end:1431080]] Now, I certainly can't prove that.
[[start:1432670][end:1434650]] I believe that it's likely.
[[start:1435550][end:1439370]] So, I think it's an interesting hypothesis to investigate.
[[start:1440190][end:1450240]] And, this is a hypothesis that I want to leave you with as a result of this class is something to think about.
[[start:1451650][end:1461940]] To what extent, in thinking about biological systems or even social systems, are the embedding theories the same?

24:23 [[start:1463830][end:1496378]] So, in thinking this way, that the physics of the situation has the same formal structure as Computer Science has in terms of explanation, we're of course, faced with a problem, which is that we're not just reconstructing physics, we're talking about the physics of interacting observers.

24:56 [[start:1496474][end:1498830]] We're talking about the physics of communication.
[[start:1499570][end:1503710]] So, we're modeling how we do physics.
[[start:1504770][end:1507970]] And, that makes our theory self-referential.
[[start:1508870][end:1521320]] And so, we have to face the music from Gödel's theorem, which tells us essentially that powerful self-referential theories can't be both consistent and complete.

25:21 [[start:1521850][end:1526690]] And, by powerful I just mean powerful enough to express arithmetic, so, not terribly powerful.
[[start:1529770][end:1535100]] So, this becomes an issue that we have to live with.

25:37 [[start:1537630][end:1554478]] We will always be faced with this issue of having to construct meta-theories which tell us how our lower-level theories work, but we never get to the end of that process.
[[start:1554644][end:1566820]] We never can get to theories that are both consistent and complete, because our tower of theories becomes progressively, actually more powerful as it goes up.

26:08 [[start:1568150][end:1590860]] So Gödel, in a sense, poses a problem, but in another sense just tells us what life is like as a scientist, that you can't have everything all the time doing science, but we probably all already knew that.
[[start:1591310][end:1613700]] So, let's now talk about space, end of digression, and see how these ideas apply to a system or a tower of systems that can construct a spatial embedding in its world, in its observed world.
[[start:1614390][end:1626760]] So, let's start out thinking about a system that can see its environment, but what it sees is a completely uniform environment where nothing is happening.

27:08 [[start:1628730][end:1639180]] So, if you have a uniform environment where nothing is happening, you can't distinguish one part of the environment from another.
[[start:1640910][end:1642860]] You have no sense of space.
[[start:1644530][end:1662402]] So, what I want to do is build up from scratch what's needed to have a sense of space, and then we'll talk a little bit about what organisms are doing.
[[start:1662456][end:1685820]] And I think a very interesting question is, if you look at phylogeny, at what points in phylogeny, what lineages in phylogeny actually need to have a sense of space, and what do they have to have in terms of computational power to have that sense of space?
[[start:1687070][end:1692140]] So, if you just have a uniform environment, you don't have a sense of space.

28:13 [[start:1693950][end:1705550]] But the first thing we can do with an environment is to divide it up into some number of parts that are somehow distinguishable.
[[start:1706710][end:1711810]] So suppose we can segment the environment into two different parts.
[[start:1712470][end:1714066]] And if you think about E.Coli, for example, E.Coli has a bunch of sensors on the front and a bunch of effectors on the back. So, it can sense much more about the front part of the environment than the back part of the environment.

28:49 [[start:1729850][end:1731206]] So, already with E.Coli, you have this kind of segmentation of the environment into parts, but so far, nothing is happening in this environment.
[[start:1741046][end:1744090]] We just have segments that can be distinguished.
[[start:1745810][end:1754670]] So, let's consider an environment like this, that has distinguishable segments.

29:17 [[start:1757270][end:1764020]] What one next wants to know about these segments is whether they're next to each other.
[[start:1765190][end:1778040]] And, if we just have a bunch of segments, we just have a set, and a set doesn't have any order or any relationship information.
[[start:1779530][end:1788570]] So, I've drawn this environment as a rectangle of rectangles, but that's just a representation.

29:51 [[start:1791470][end:1798830]] And, it looks like there are relationships between these rectangles, but if they're just a set, then there are no relationships.
[[start:1799330][end:1803790]] If we want to add relationships, then we have to add them explicitly.
[[start:1804690][end:1834250]] So, let's add some connections between these different segments of the environment to turn that set into a graph that says explicitly, for example, that the light green segment is attached to the light blue segment, and it's also attached to the dark green segment, and the dark blue segment is attached to the light blue segment and attached to the dark green segment.

30:34 [[start:1834670][end:1839722]] So, now we have something that's much more mathematically complicated than a set.
[[start:1839776][end:1842842]] We have a graph that has some connection information.

30:42 [[start:1842976][end:1845070]] So, we have a connection topology.
[[start:1846850][end:1850110]] Now, adding this topology does something very important.
[[start:1850180][end:1855870]] It breaks the exchange symmetry that is there if you just have a set.
[[start:1856020][end:1871110]] So if we just have a set, it doesn't make any difference if I exchange, for example, the positions of the upper right light blue segment with the upper left light green segment.
[[start:1871610][end:1876120]] But if we have this connection topology, then it does make a difference.

31:16 [[start:1876810][end:1888330]] Right, I've twisted the graph around, and if I have to break connections to exchange things, then I've actually changed the topology.
[[start:1889550][end:1900990]] So, adding a topology, adding connections, can disrupt a symmetry that's there if there is no topology.

31:42 [[start:1902930][end:1910100]] So, now let's think about, now we have the structure that's required to think about something happening.
[[start:1911430][end:1923974]] So, suppose that at some time, as measured in the bit counter time reference frame of the observing system, something happens.
[[start:1924092][end:1927190]] So, a dot appears in the light green segment.

32:08 [[start:1928570][end:1933814]] And, we can express this actually in the notation of quantum field theory.
[[start:1933862][end:1947200]] We can think of the light green segment as a field and the dot appearing is the occurrence of an excitation in that field.
[[start:1948210][end:1959570]] And so, we can write this notation that says that the green field was excited to produce a dot which is up arrow green dot.

32:42 [[start:1962150][end:1976040]] And, sometime after that it may turn out that the dot disappears in the green field and some sort of dot appears down in the dark blue field.

32:56 [[start:1976890][end:1985450]] And again, we can write this in this kind of creation and destruction operator notation that one has in quantum field theory.
[[start:1986190][end:1994090]] And so, this says that the green field is no longer excited, but now the dark blue field is excited.
[[start:1995090][end:2000270]] So, this doesn't imply anything about these excitations being the same.
[[start:2000340][end:2002320]] In fact, they're completely different.

33:23 [[start:2003010][end:2007860]] One is an excitation of the green field and one is an excitation of the blue field.
[[start:2008230][end:2011650]] But at least now something is happening in the environment.
[[start:2012150][end:2022882]] So, we can think about what does it take for an observer to notice that something is happening in its environment?
[[start:2022946][end:2042890]] It has to be able to detect a change occurring in some segment of its environment, and that change can involve something happening or something stopping happening in that segment of its environment.

34:03 [[start:2043390][end:2049680]] But it doesn't yet have to have any idea of what an object is.

34:10 [[start:2050690][end:2071310]] But we can add that if the system has a memory, we can have the system connect these events happening in different parts of its environment.
[[start:2072070][end:2082610]] So, if the system has a memory that has some number of steps, I'll say n steps, but here it could even just be 2 steps.

34:44 [[start:2084890][end:2103526]] It can see transitions between these two different states, where there's a dot in the green field and then a dot in the dark blue field, and then a dot in the green field, and then a dot in the dark blue field, and then a dot in the green field, etc.

35:03 [[start:2103718][end:2112080]] So, I've expressed this in this sort of field theory notation over on the right side.
[[start:2112690][end:2115418]] And, what this is is a flip-flop.
[[start:2115594][end:2118430]] It's an observed periodic behavior.
[[start:2119410][end:2124610]] So, this is the basic idea behind a clock.

35:24 [[start:2124950][end:2138914]] So, any observer that can see this number of time steps internally can interpret what's going on in its external environment as a clock ticking.
[[start:2141690][end:2143910]] It can see some periodicity.
[[start:2145130][end:2155782]] So, as long as you can have memory and the ability to detect change, you can see periodic behavior in the environment.
[[start:2155926][end:2159470]] So, you can see the environment acting like a clock.

36:01 [[start:2161970][end:2168110]] So, let's think a bit about what this does and does not require.

36:08 [[start:2168450][end:2177802]] So, seeing a clock in the environment requires having distinguishable, non-exchangeable sectors of the environment.
[[start:2177866][end:2183390]] So, you have to have this connection topology that breaks the exchange symmetry.
[[start:2183770][end:2189154]] It requires having these sectors implement some sort of flip-flop.
[[start:2189282][end:2202890]] So, something periodic happening, and you have to have enough memory to see that periodicity, but it doesn't require any sense of object identity.

36:43 [[start:2203870][end:2213600]] So, the excitation in the green part and the excitation in the blue part can still just be field excitations of the green part and the blue part.

36:56 [[start:2216770][end:2219742]] There's nothing that says that those have to be the same thing.
[[start:2219796][end:2223860]] They just have to appear and disappear in some periodic way.
[[start:2224790][end:2228580]] And, having a clock doesn't require a metric space.

37:08 [[start:2228950][end:2233730]] You don't need to have any sense of distance defined by the environment.
[[start:2234410][end:2239750]] You just have to have this segmentation that is not rearrangeable.

37:20 [[start:2240250][end:2247340]] So, this tells us something extremely important, which is that time is more fundamental than space.
[[start:2248030][end:2256570]] Time in the exterior environment is much simpler and easier to observe than space in the exterior environment.
[[start:2256910][end:2274130]] So, if we're thinking biologically about phylogeny, we might expect to see organisms that can detect periodic behavior in the external environment long before they can detect spatial organization in the exterior environment.
[[start:2274470][end:2282530]] And, we know that organisms, even down to microbial mats, can respond to the diurnal cycle.
[[start:2283370][end:2302540]] So, we know that organisms, in a sense, can detect environmental clocks, even organisms that we have no reason to believe, divide the environment up into spaces or the sort of space that we're used to, like a Euclidean space.

38:23 [[start:2303950][end:2310590]] So, adding space to this idea of time in the environment.

38:33 [[start:2313090][end:2333890]] So, the next step is to be able to see motion. And, being able to see one thing move from one segment of the environment to another segment, as opposed to something happening in one segment, and then something happening in another segment.
[[start:2334730][end:2351338]] One has to have this idea of object persistence, that there's a thing that has an identity, and its identity doesn't change over time, and it doesn't change when you move it someplace else.
[[start:2351424][end:2356460]] When it appears someplace else in the environment, it's the same object.
[[start:2358370][end:2370190]] So, this is an idea that psychologists call "object persistence", and it's an idea that physicists call "translational invariance".

39:30 [[start:2370950][end:2375314]] Translational invariance means two things.

39:35 [[start:2375512][end:2382098]] It means that if I have an object and I move it to a different location, I don't change the object.
[[start:2382264][end:2386166]] It's the same object that I move from here to there.
[[start:2386348][end:2389080]] So, the location doesn't change the object.
[[start:2390010][end:2392854]] And, it also means the reverse of that.
[[start:2393052][end:2396310]] It means that the object doesn't change the location.

39:59 [[start:2399310][end:2404730]] My container remains invariant even though I move the object around in it.
[[start:2404880][end:2412990]] So these are kind of the two phases of translational invariance, and they're the two faces of object persistence.
[[start:2414690][end:2424100]] As the object moves through time, its identity remains fixed, and it doesn't change the time that it's moving through.
[[start:2424790][end:2432610]] So, if I'm measuring its motion with a clock, moving the object doesn't change the clock.

40:34 [[start:2434090][end:2437590]] These are clearly very classical ideas.

40:39 [[start:2439210][end:2443750]] And, we talked about earlier classical communication.
[[start:2445450][end:2468880]] And, when we talked about classical communication in, for example, the context of a Bell EPR experiment, we talked about the observers being able to write down some data on a piece of paper or on a disk drive or something and hand those data to someone else.
[[start:2469330][end:2471774]] So, this is translational invariance.
[[start:2471822][end:2476130]] The data can't change when Alice gives it to Bob.
[[start:2476550][end:2480020]] Otherwise, there isn't classical communication taking place.

41:20 [[start:2480950][end:2485494]] And of course, there's an up to noise built into here, right?
[[start:2485532][end:2491654]] The piece of paper might get wet and the ink might run a little bit, but it's still the same message.
[[start:2491772][end:2495430]] There's still some identity being assumed.

41:36 [[start:2496110][end:2501670]] So, object persistence is not an idea we get from Quantum Theory.
[[start:2501750][end:2505850]] It's an idea that we impose on top of Quantum Theory.

41:46 [[start:2506270][end:2510190]] And, it's this idea that's intrinsically classical.
[[start:2511090][end:2516170]] So, we're looking right here at the quantum to classical transition.
[[start:2516250][end:2517360]] This is it.
[[start:2518370][end:2522334]] This is what gets added to Quantum Theory to get classical physics.
[[start:2522382][end:2524850]] It's this idea of object persistence.

42:05 [[start:2525830][end:2539560]] Now, once we have object persistence, we can kind of go to town constructing space, and here's how we do it.

42:22 [[start:2542890][end:2565440]] We all learned about object persistence this way when we were six months old, doing motor babbling and observing our hands and feeling how our bodies worked and seeing objects that we could manipulate and that didn't change when we manipulated them.

42:46 [[start:2566450][end:2569658]] So, this is the birth of object persistence.
[[start:2569754][end:2575330]] This is the birth of classicality in human psychology.

42:59 [[start:2579350][end:2582546]] So, now let's start thinking about building a coordinate system.
[[start:2582648][end:2583842]] What's a coordinate system?
[[start:2583896][end:2589990]] A coordinate system is just a set of labels that are attached to these segments of the environment.
[[start:2590970][end:2594120]] And, to build a coordinate system, you have to have an origin.
[[start:2594970][end:2602060]] And, an origin means an object, something that's fixed, something that doesn't move around.

43:23 [[start:2603390][end:2609510]] And, so a coordinate system requires the ability to identify a stigmergic memory. It requires the ability to find something in the environment that has a meaning that stays constant over time.
[[start:2622550][end:2625474]] And, that's what a stigmergic memory is.
[[start:2625512][end:2633380]] It's something in the environment that provides us with a memory resource that we can count on being the same.

43:54 [[start:2634650][end:2665280]] And, it's having this fixed point that allows us to label these connected segments of the environment that contain objects that move and be able to say, okay, the object moved from this part of the environment to another part. And, I can give those parts labels with respect to this other part that doesn't move, this origin point.

44:26 [[start:2666290][end:2670910]] And, once I have this, I can construct other invariances.
[[start:2671490][end:2683170]] So, for example, I can consider an object that rotates around this origin without changing its identity. And that defines what's called rotational invariance.
[[start:2684410][end:2698006]] And, I can also talk about an object that gets bigger and smaller compared to this fixed point and that defines radial distance.

44:58 [[start:2698198][end:2724340]] And, if you think about the baby in the previous slide that's doing motor babbling, it sees things getting smaller as it moves them farther away. So, the visual system does this computation for us and constructs this radial coordinate for us with respect to our bodies, or specifically our heads, our eyes.
[[start:2726070][end:2744390]] So, in doing this very early motor activity, we're actually building the spatial coordinate system for our brains that's implemented by the hippocampus, the place cells in the hippocampus.

45:45 [[start:2745610][end:2758780]] And, if I have an origin point in the environment, I can also infer that I am moving, that I have changed my location with respect to that object.

45:59 [[start:2759730][end:2771162]] And, that's a considerably more complicated inference because you have to have a representation of the self of you to say "I moved".
[[start:2771306][end:2776562]] So, this is something that comes after you've developed this spatial coordinate system.
[[start:2776696][end:2785400]] You have to be able to locate, in a sense, metacognitively, a particular object that's you in that coordinate system.
[[start:2786730][end:2793638]] So, we're going to set that aside and now talk about adding some numbers, so, adding a metric. And, adding a metric requires another particular kind of object, which is a ruler, a particular fixed object that can be moved around and that has translational invariance, and rotational invariance up to some transformation, up to some tensor.

47:01 [[start:2821730][end:2825410]] And, in Euclidean space, that tensor is the identity.
[[start:2826070][end:2832530]] So, in Euclidean space, you have perfect translational and rotational invariance.
[[start:2833510][end:2844120]] As you get into general relativity, then the ruler can actually change its length as you rotate, or the ruler can change its length as it moves through space.
[[start:2844650][end:2855530]] So effectively, your spacetime can deform, the coordinates of your spacetime can deform, and that gives you the representation of mass, of course, in general relativity.

47:36 [[start:2856750][end:2868030]] So, we talked several sessions ago about quantum reference frames, and I used the example of rulers and clocks as quantum reference frames.
[[start:2868530][end:2887110]] So, now we see how to construct those from observations and symmetry breaking and object identity, all of which we need to define a quantum reference frame out in the environment, like a ruler.

48:07 [[start:2887930][end:2898678]] And, notice that we don't need any of that environmental stuff to define those QRFs within our own processing.
[[start:2898774][end:2907194]] And in fact, the ones that exist within us, we have no direct access to.
[[start:2907392][end:2919280]] We can look at someone else's brain and talk about their spatial representation system, but we can't look inside our own brains and talk about our spatial representation system.

48:41 [[start:2921090][end:2926820]] So, this is how we get a metric space from the ground up.
[[start:2927990][end:2950620]] And, we've talked about this from a very psychological or biological point of view: starting from sort of motor capabilities, motor babbling, for example, a measure of effort which gives you some sense of mass.

49:11 [[start:2951150][end:2957130]] So, if it's easy to move something, it's light, and if it's hard to move something, it's heavy.
[[start:2958270][end:2966510]] And, we understand that when we're six months old because we can measure how much force we're having to apply with our muscles.
[[start:2967090][end:2982370]] We have a reference internally for this force that we're applying, and we use that internal measurement to attribute this idea of mass to things in the environment.

49:42 [[start:2982950][end:2985490]] We have to have memory from manipulations.
[[start:2986090][end:2993830]] We have to be able to identify invariances that define object persistence.
[[start:2994330][end:3001580]] And we have to be able to build a ruler that we can move around and use to define a metric space.
[[start:3002670][end:3006460]] Now, this is very different from the way physicists approach this.
[[start:3007790][end:3012942]] If you look at the physics literature, people start with information transfer.

50:13 [[start:3013076][end:3017470]] They talk about entanglement as a basic resource.

50:19 [[start:3019490][end:3023822]] There's a lot of discussion of bulkboundary duality.
[[start:3023886][end:3040178]] And, the most well-known one is the duality between anti-de Sitter space, which is the sort of space you see inside a black hole, and conformal field theory, a quantum field theory on the boundary of the black hole.
[[start:3040274][end:3050330]] So, how things you can see, for example, going on, on the horizon of a black hole are dual to the geometry and the interior by this mathematical relationship. You can use that mathematical relationship to construct quantum error-correcting code by using the symmetries of the field theory as a resource for redundancy that allows you to represent the same thing in different places.

51:13 [[start:3073730][end:3081090]] And, as soon as you can do that, you can build up a network of elements that look basically like elements of a lattice.
[[start:3081750][end:3092840]] And, a lattice is a graph to which you can assign symmetric relationships, and you get a metric space.
[[start:3093850][end:3106730]] And in physics, typically, the goal is to get Einstein's equations out of this to start with some information-theoretic sorts of constructs and get the equations of general relativity.
[[start:3107630][end:3111534]] But what are the equations of general relativity?
[[start:3111572][end:3133330]] These are things that Einstein derived by doing fairly simple thought experiments, using the invariances of ordinary Euclidean space, combined with ideas from special relativity about the speed of light being constant.

52:14 [[start:3134230][end:3151980]] And, he added the Principle of Equivalence, which is the idea that essentially mass and acceleration are the same thing, or that gravity and acceleration are the same, that weight and acceleration are the same thing.
[[start:3153230][end:3181890]] So, it's at least reasonable to expect that this inferential process that's going on in theoretical physics is generating the same thing, although in a very formalized way that we can generate by thinking about how organisms deal with their environments.
[[start:3182950][end:3189800]] And so, I want to leave this with you as the second hypothesis here.

53:12 [[start:3192010][end:3201610]] The first one was the hypothesis about a trivial renormalization group flow across scales and biology.

53:22 [[start:3202830][end:3211920]] The second hypothesis is that these two approaches to emergent spacetime are actually giving us the same information.
[[start:3213410][end:3230450]] And, maybe starting out with the same information, in fact, that we may be able to think about these fundamental building blocks of information flow and entanglement in terms of the sorts of perceptual relationships that we've been talking about in this class.
[[start:3239290][end:3246520]] So there's our second hypothesis to think about going forward.

54:07 [[start:3247870][end:3267390]] And I just want to leave you with the idea that organisms at least manage this very interesting process that we can think of starting with the construct of memory.

54:28 [[start:3268770][end:3279730]] Organisms have memory at multiple scales, and it's memory that allows them to formulate the idea that there are objects.
[[start:3281030][end:3287670]] And, as soon as you have objects that persist, you have a source of redundancy.
[[start:3288330][end:3290550]] So, you can do error correction.
[[start:3291610][end:3303690]] And, if you can do error correction, if you can move the same thing from one place to another and have it encode the same information, then you can build spacetime.

55:05 [[start:3305150][end:3310810]] And, as soon as you have spacetime, you can use the spacetime as more memory.
[[start:3312130][end:3315514]] You can use the spacetime itself, as the error correcting code because spacetime has the nice ability to hold lots of copies of some informative structures.
[[start:3325466][end:3337058]] So, you can build libraries, or you can build computers, or you can build the internet, if you have spacetime, which gives you more memory, which gives you more object persistence, which gives you more error correction.

55:37 [[start:3337234][end:3339494]] And, the circle just spins around.
[[start:3339692][end:3344950]] So, organisms do this, and the question is, how does it get off the ground?
[[start:3345610][end:3364830]] And, next time, we can at least speculate about that kind of origin of life type of question in the context of the FEP and its realization in simple systems of communicating observers.
[[start:3365970][end:3372080]] So, as always, I encourage you to use the interactive Q&A.
[[start:3373110][end:3387000]] The 5th discussion session with Ander, who's unfortunately not here today, will be the last day of September, Saturday 5:00, as usual, 05:00 European time, 08:00 California time.

56:27 [[start:3387690][end:3392150]] And then, the last session of the class will be the 12th of October.
[[start:3392650][end:3399100]] So, thank you very much, and I look forward to your questions in the interactive Q&A.

56:44 _Daniel:_
[[start:3404990][end:3405740]] Awesome.

56:48 [[start:3408630][end:3409838]] Thank you, Chris.
[[start:3410014][end:3411700]] Can I ask some short questions?

56:52 _Chris:_
[[start:3412550][end:3413250]] Sure.

56:53 _Daniel:_
[[start:3413400][end:3414238]] All right.
[[start:3414424][end:3424200]] So, first Lana wrote: is the periodicity, the time lengths between and during the excitations built in?

57:04 [[start:3424570][end:3431340]] So this was when we had the four cells and there were the inklings of a clock coming into play.

57:16 _Chris:_
[[start:3436760][end:3459930]] I think the simplest answer is that if nothing else is happening in the environment except this periodic behavior, then it's not actually meaningful to talk yet about the time between the events.
[[start:3469680][end:3498000]] So, if I have a system that's quasiperiodic, for example, and nothing else is going on in my environment, then I can't distinguish that from a perfectly periodic system because I would have to have a perfectly periodic reference to know that the other system was aperiodic.

58:18 [[start:3498680][end:3516360]] And, if you think about the internal clock being driven by information flow into the system, then something has to be happening in the environment for information to be flowing into the system and being counted.
[[start:3517200][end:3527550]] So, again, as we talked about a few sessions ago, the internal memory only gets updated when something happens.
[[start:3529360][end:3533250]] So, internal and external get tied together.

58:55 [[start:3535540][end:3550500]] This is why we can use external clocks, but it's also why we depend on external clocks because our intuitive sense of time is very malleable.
[[start:3551880][end:3564570]] And so, we actually, as humans, use external clocks to correct for the malleability of our own intuitive sense of time.

59:26 _Daniel:_
[[start:3566780][end:3567396]] Wow.
[[start:3567518][end:3587760]] And there's probably a lot to be said for that procrustean nature of having the chronometer, the clock on the wall, and the tick, tick, tick as an evolutionarily novel ruler of time, playing a logistical role in time bound society.

59:50 _Chris:_
[[start:3590020][end:3596292]] Yeah, think of earlier clocks that earlier cultures have used and that animals use.
[[start:3596346][end:3608136]] I mean, we have the solar clock, the lunar clock, etc., and the orbit of Venus clock that was so important to the Mayans and so on.
[[start:3608318][end:3619740]] So there are lots of available clocks in the environment if you have the ability to notice them and enough memory to realize that they're clocks.

1:00:21 _Daniel:_
[[start:3621440][end:3622140]] Awesome.
[[start:3622290][end:3625192]] All right, here's a question from Upcycle Club.

1:00:25 [[start:3625256][end:3635040]] They wrote: how does representing the network structure and dynamics with quantum embeddings affect the semantic interpretation of the network?

1:00:42 _Chris:_
[[start:3642810][end:3648970]] The embedding theory is the simplest semantic interpretation of the network.
[[start:3650670][end:3651420]] So...

1:00:58 [[start:3658140][end:3665980]] And again, a good way to think of this is through the lens of Computer Science.
[[start:3667600][end:3680240]] As soon as you have a programming language that allows variable binding, then you've built a very simple kind of semantics into the language.

1:01:22 [[start:3682500][end:3705000]] If you have X as a variable and you have variable binding, then at different times in the execution of the program, X can have different causal consequences for downstream computation because it's been bound to a different value, so it has different semantics.

1:01:46 [[start:3706380][end:3713500]] So, the semantics of X, again, go back to Gregory Bateson.

1:01:55 [[start:3715920][end:3723420]] The basis of semantics is differences that make a difference, make a difference to behavior, make a difference to actionability.
[[start:3724820][end:3732610]] So, variable binding gives you differences that actually make a difference to what the program does.
[[start:3734580][end:3738310]] So, what is that?
[[start:3739240][end:3752440]] That is the semantics that's assigned by your embedding theory between what the programming language is doing and what the operating system is doing and so forth.
[[start:3753500][end:3782800]] And, I think it's no surprise that the semantics of programming languages end up being represented with these very general mathematical constructs like Category Theory, which are essentially tools for representing arbitrary relations between systems.

1:03:03 [[start:3783940][end:3786370]] And, that's what embedding theories are.
[[start:3787320][end:3792740]] They're theories that state relationships between systems.

1:03:16 _Daniel:_
[[start:3796080][end:3814660]] Awesome, and very provocative to explore on the biological and life and on the spacetime and matter sides, which are of course, seamlessly integrated through, if only our own experiences.

1:03:35 _Chris:_
[[start:3815800][end:3824992]] Yeah, this is another place where it's useful to go back to this difference between reductive theories and scale-free theories.
[[start:3825136][end:3833476]] Scale-free theories are all about semantics because they represent the existence of stuff happening at different scales.
[[start:3833508][end:3841820]] And so, they naturally raise the question of what are these relationships, what are these embedding theories?
[[start:3842720][end:3849550]] And, in reductive theories there's a very deep sense in which semantics doesn't matter.

1:04:12 [[start:3852580][end:3866530]] If you think that all that's going on that's important is the stuff that's going on at the Planck scale, then you don't need any semantics, right?

1:04:30 [[start:3870680][end:3887284]] You see this in the late 60s, early 70s, old-fashioned AI, where people talk about computation, is purely syntactic.

1:04:47 [[start:3887412][end:3889972]] And, this is a very reductionist view of computation.
[[start:3890036][end:3896300]] It leaves out the semantics, and without the semantics, the computation is useless.
[[start:3896720][end:3900350]] It doesn't tell us anything at all unless we can map it to something.
[[start:3902260][end:3921190]] So, we have this philosophy of science tradition that tells us that semantics is not important, and we end up with tools like the FEP that essentially tell us that semantics is all important.

1:05:23 [[start:3923720][end:3931976]] And, from a biological point of view, the most natural response is, of course, we knew that all the time.
[[start:3932078][end:3933720]] That's why we're doing biology.

1:05:36 [[start:3936140][end:3939630]] So all of this ties together.

1:05:40 _Daniel:_
[[start:3940480][end:3949068]] Would you say that FEP says semantics is important, and then what does it say about what semantics are important?
[[start:3949154][end:3952560]] Or is that entirely left up to the modeler?

1:05:56 _Chris:_
[[start:3956380][end:3963480]] Well, it tells you a lot about what's important for the system itself, right?
[[start:3963550][end:3972830]] The system itself is dealing with its environment and it's trying to increase its predictive power.
[[start:3973600][end:3981904]] So, it's building a theory of the environment, and that theory is intrinsically semantic, right?
[[start:3981942][end:3986800]] It's about the environment and it's actionable.
[[start:3988660][end:4007210]] The theory is meant to drive action on the environment that will either yield more information or get the environment to behave, to do what I'm predicting it's going to do.

1:06:48 [[start:4008780][end:4018060]] So, I think the FEP is intrinsically semantic in that sense, that it's about an agent modeling its environment.

1:06:59 _Daniel:_
[[start:4019040][end:4019596]] Yes.
[[start:4019698][end:4047492]] And about the semantics of action, as opposed to a partial or limited semantics of passive inference or semantics of abstraction, which kind of leaves the important link between the agent and the environment through sense-making and decision selection basically unaddressed because it's kind of Descartes in the thought experiment in the room.
[[start:4047626][end:4051830]] And here, when we actually engage with the boundary of the room, that's where we start.

1:07:32 _Chris:_
[[start:4052600][end:4054120]] Yeah, yeah.

1:07:34 [[start:4054190][end:4065700]] The FEP completely destroys this classical notion of the passive observer, as does Quantum Theory.
[[start:4065860][end:4068680]] There are no passive observers in quantum theory.
[[start:4069500][end:4078040]] So, this is a construct that we inherited from a classical worldview that is seriously misleading.

1:08:04 _Daniel:_
[[start:4084790][end:4087986]] A lot more to say, but that's a great place to end.
[[start:4088088][end:4089170]] Thank you, Chris.

1:08:09 _Chris:_
[[start:4089990][end:4090498]] OK.
[[start:4090584][end:4091566]] Thank you, Daniel.
[[start:4091678][end:4092914]] And thanks to you all.

1:08:13 [[start:4093032][end:4094740]] And ask questions.

1:08:15 _Daniel:_
[[start:4095110][end:4095874]] See you next time.

1:08:15 _Chris:_
[[start:4095912][end:4096222]] Cheers.
[[start:4096286][end:4097040]] We'll see you next time.
