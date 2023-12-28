---
title:  'Physics as Information Processing - Discussion 4, "Communicating Observers"'
author:
- 'Ander Aguirre (Ohio State University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-6337-8292)'
- 'Daniel Friedman (Active Inference Institute; University of California, Davis) [![Orcid](images/orcid.png)](https://orcid.org/0000-0001-6232-9096)'
- 'Chris Fields (Allen Discovery Center at Tufts University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-4812-0744)'
- 'Haris Neophytou (Interfusion Services / UpCycleClub) [![Orcid](images/orcid.png)](https://orcid.org/0009-0003-0921-737X)'
- 'Dean Rickles (Professional Initiatives Programming, Active Inference Institute) [![Orcid](images/orcid.png)](https://orcid.org/0000-0003-2213-0773)'
date: "2023-08-26 Version 1.0"
...

## Discussion 4, "Communicating Observers"

00:08 _Daniel:_
[[start:8730][end:9390]] All right.
[[start:9540][end:11070]] Hello and welcome everyone.
[[start:11220][end:20570]] It is Saturday, August 26, 2023 and we're here in “Physics as information processing,” in the fourth discussion.
[[start:20730][end:21470]] Thank you everybody.
[[start:21540][end:23550]] Who's joining live or watching.
[[start:23620][end:25266]] Live or watching in replay.
[[start:25418][end:28530]] This should be a really fun discussion as usual.
[[start:28690][end:43290]] So we're going to have Ander provide some slides and some initial clarifying questions for Chris and then we're going to open it up for our guests to ask some questions and check in a live chat, see what people are talking about.
[[start:43360][end:47050]] So Ander, to you for some slides and overview.

00:48 _Ander:_
[[start:48030][end:48394]] Okay.
[[start:48432][end:49222]] Thank you, Daniel.
[[start:49286][end:57614]] So last time we were starting to talk about multi-agent communication and LOCC protocols and all of that.
[[start:57732][end:64430]] So let's quickly go through the slides and sort of try to recall the main concepts.
[[start:66630][end:71170]] I guess just to go back to session 3 for a second.
[[start:71320][end:81350]] One takeaway was that when you have noncommunicative sectors in a boundary, that's necessarily going to require classical communication between them.
[[start:81500][end:90170]] So that is more or less the whole point of today, how noncommunicative sectors have to communicate classically.
[[start:96110][end:108474]] Another introduction in this last lecture was this new graphical notation, TQFT, if you wish to call it that way for any of these clock ticks.

01:48 [[start:108522][end:134470]] Okay, so let's recall the whole process of measuring a sector environment and writing it into a memory environment can be simplified to this sort of tick that connects two portions of the boundary. Everything we talk about LOCC protocols will be written in this graphical notation.
[[start:137550][end:142300]] So let's keep going a little bit.
[[start:143790][end:149562]] This slide is on the paper on sequential measurements from 2022 [(2022) Sequential Measurements, Topological Quantum Field theories, and Topological Quantum Neural networks. Fields C, Glazebrook JW and Marcianò A].
[[start:149696][end:156858]] These are basically the formal mapping between QRFs and topological quantum field theories.
[[start:156954][end:157214]] Okay.
[[start:157252][end:162714]] So we're more used to the picture here on the left hand side of this slide, right with the QRF sectors.
[[start:162762][end:167490]] But pictorically speaking, this is at least how they map.

02:49 [[start:169110][end:169714]] Okay?
[[start:169832][end:178418]] And then from then we started talking about entanglement and classical communications using this notation.
[[start:178514][end:182120]] And this is probably where my questions to Chris will start.
[[start:182650][end:193770]] So in section 3, we saw this idea of the FEP asymptotically being the principle of unitarity, a.k.a, driving the system, the joint system, Alice and Bob to entanglement, which in this graphical notation, amounts to them sort of completing a cycle here where the QRFs are perfectly aligned, so that the S sector of one becomes the memory sector of the other and viceversa. I actually at this point already, I have a question for Chris. I have it written down.

03:50 [[start:230330][end:230886]] Yes.
[[start:230988][end:232790]] Two things here, Chris.
[[start:233530][end:246826]] Number 1 - in the LOCC protocol picture we distinguish between a quantum channel and a classical channel.
[[start:247008][end:257962]] And if I understood that part correctly, we said that passage of time or expenditure of energy, free energy, only corresponds to the classical tick.
[[start:258106][end:270738]] So in this quantum entanglement picture where you don't quite have that, is it fair to say that there's no such thing as a classical tick no passage of time, no expenditure of free energy.
[[start:270904][end:282582]] Is this a degenerate picture of the LOCC protocol where the sectors were aligned the right way and boom, you got rid of that classical thing and that's it.
[[start:282636][end:295020]] And secondly, I guess, what does it mean for these two parts, quote unquote from the paper, to implement a joint quantum process?

04:59 _Chris:_
[[start:299860][end:311860]] So, yeah, this is not a LOCC protocol, clearly, because there is no classical communication.
[[start:312280][end:321012]] And in fact, Alice is not divided into multiple compartments here. Alice is just implementing this single quantum process, Q.
[[start:329360][end:376308]] And because these QRFs are perfectly aligned, we can think of...remember from probably the 2nd session, the picture that you were very interested in, the Wick rotation reversing time between Alice and Bob.

06:16 [[start:376484][end:388860]] So Alice's clock in fact ticks in the opposite direction from Bob's clock because both of their internal clocks are counting incoming bits, not outgoing bits.
[[start:390640][end:398930]] In this, in the right side of this picture, there is no overall time.
[[start:399620][end:410980]] You can think of Alice's clock ticking forward one unit and then Bob's clock ticking backward one unit.
[[start:411720][end:422388]] So that the information flow is completely time symmetric between Alice and Bob.
[[start:422564][end:431550]] So we can think of both of these processes, Q and Q prime, as bi-directional in time.
[[start:432480][end:435710]] That's what it means to have a pure unitary process.

07:18 _Ander:_
[[start:438320][end:439784]] So no time asymmetry.
[[start:439832][end:440760]] That's what it is.

07:20 _Chris:_
[[start:440850][end:441152]] Right.
[[start:441206][end:444108]] So there is no time asymmetry in this picture.
[[start:444284][end:450300]] And when you introduce classical communication, of course you have to have a time asymmetry.

07:30 _Ander:_
[[start:450460][end:450880]] Right.

07:30 _Chris:_
[[start:450950][end:457700]] Because you have this, I mean, classicality is defined by this notion of irreversibility.

07:38 _Ander:_
[[start:458440][end:459060]] I see.

07:39 _Chris:_
[[start:459130][end:462656]] Which is just the same as time asymmetry.
[[start:462848][end:465976]] And it's the irreversibility that burns energy.
[[start:466078][end:496970]] So there has to be energy flow between Alice and Bob to drive what is from a global point of view and only an apparent asymmetry, but from the point of view of Alice 1 and Alice 2 as components of Alice, they're the ones who see the asymmetry.

08:21 _Ander:_
[[start:501390][end:516026]] So I guess just to tie back to the question of the Wick rotation, once this joint process is implemented, naively, one can say, is this cycle going clockwise or counterclockwise?
[[start:516058][end:525700]] And is that going to define on, originally--whenever these guys ended up being lined up, where the Wick sign was coming from?

08:51 _Chris:_
[[start:531770][end:532520]] Yes.
[[start:533530][end:539190]] Whenever Alice sees information flowing in, Bob sees information flowing out.
[[start:539260][end:544810]] So their Wick rotations are going in opposite directions.

09:06 _Ander:_
[[start:546110][end:546860]] Okay.
[[start:548990][end:551020]] Yeah, very good.

09:12 _Chris:_
[[start:552830][end:585590]] The other thing to think of in this picture--it's impossible to draw all of these simultaneously--is that if you think of the FEP as fully aligning Alice and Bob, then not only do these processes perfectly couple, but the area that's green in this right hand side kind of expands to fill the whole boundary.
[[start:586250][end:599480]] So that in the complete limit of Alice being able to perfectly predict Bob and vice versa, then the whole boundary is green.
[[start:600490][end:611870]] So there's no this distinction between the S sector, and the Y sector disappears.

10:12 _Ander:_
[[start:612930][end:615294]] Yes, that makes sense, actually.
[[start:615412][end:631138]] And just to conclude with this slide, back in the session 2, we saw something about agents requiring a free choice of reference frame for their QRFs, which amounts to being able to choose how to measure a spin.
[[start:631234][end:632806]] Right, right.
[[start:632908][end:642150]] So is part of this entanglement picture; do they just have to align the sectors, or also the way they are measuring a spin on those sectors?

10:43 _Chris:_
[[start:643790][end:648598]] Yes, they have to align the way they're measuring the spin in those sectors.
[[start:648774][end:662990]] It's that lack of--remember the point that free choice of local reference frame is required for separability.
[[start:663890][end:677300]] So as the systems become fully entangled, then their local reference frames for each qubit become the same.
[[start:678230][end:680500]] Become necessarily the same.

11:25 _Ander:_
[[start:685170][end:686078]] Thank you.
[[start:686244][end:686622]] Okay.
[[start:686676][end:688880]] And then let's continue a little bit.
[[start:689250][end:695250]] So in this talk, we're mainly interested on QRFs that do not commute.
[[start:695990][end:706754]] Now, maybe, Chris, you can tie this back to what you were saying earlier about if you're perfectly entangled, then the sector is going to grow.
[[start:706792][end:708166]] Does it have anything to do with this?
[[start:708188][end:717720]] So if Q1 and Q2 here do commute, then how do you reduce this to the picture on the right hand side?
[[start:718490][end:725130]] At the first glance, it looks like the picture on the left hand side encompasses more sectors of the boundary.

12:07 _Chris:_
[[start:727390][end:728090]] Yeah.
[[start:728240][end:776710]] The point here is just that if we go back to the notation where what we're representing by this simplified notation is a collection of Cone-Cocone diagrams, and if these reference frames commute, then one can take these two diagrams and find a...think of it in the information inflow direction...there will always be a common Cone-Cocone over the two sets of input classifiers if the two QRFs commute.

13:16 [[start:796070][end:819534]] So what that means is that I go from a diagram with two sets of classifiers, each going up to some apex, to a diagram with the merged set of classifiers going up to some farther up the hierarchy apex because they commute.
[[start:819602][end:828570]] I can find that sort of yet more abstract Cone-Cocone that covers all of the classifiers in both QRFs.
[[start:830270][end:839034]] So that just collapses these pairs of green segments down to one green segment.
[[start:839082][end:840830]] And I've drawn it the same size.
[[start:840900][end:845154]] I mean, it would make more sense graphically, I suppose, to draw it.

14:05 _Ander:_
[[start:845272][end:845842]] Right.

14:05 _Chris:_
[[start:845976][end:850740]] Each one is twice as big or twice the area.
[[start:851270][end:865800]] But keeping to this kind of very topological representation where the area isn't actually meaningful, it is convenient to draw it this way.

14:26 _Ander:_
[[start:866330][end:866982]] Right.
[[start:867116][end:872810]] So in short, the fact that they commute means that you will have that higher apex anyway, so you can bypass that first nesting.

14:35 _Chris:_
[[start:875830][end:876202]] Right.

14:36 _Ander:_
[[start:876256][end:879530]] But it comes to the number of degrees of freedom at the boundary.
[[start:879950][end:881098]] They're still the same.
[[start:881184][end:884170]] And in terms of area right, okay.

14:44 _Chris:_
[[start:884240][end:884630]] Yeah.
[[start:884720][end:891600]] We're not getting rid of any of the degrees of freedom of the boundary that these QRFs are looking at.

14:53 _Ander:_
[[start:893170][end:894750]] Yeah, very good.
[[start:894820][end:898706]] So the next slide I found a very interesting one.
[[start:898728][end:912070]] So these are no-go theorems things that Alice and Bob cannot do, and it's mainly having to do about measuring their own entanglement entropy and counting degrees of freedom.
[[start:913850][end:922554]] I guess this has a very holographic feel to it, and also maybe even a bit of a Godel theorem feel to it.
[[start:922592][end:925420]] So I don't know if Chris wants to comment on that.

15:27 _Chris:_
[[start:927950][end:951250]] Well, I'll just say that I think this does have a kind of Godel undecidability feel to it, in that there are a large number of questions that Alice can't answer, which certainly suggests a formulation in terms of incompleteness.
[[start:952310][end:968150]] And the connection to Godel's theorem is actually something that Jim Glazebrook and I are currently working on, and hopefully we'll be able to make that connection more precise.
[[start:968730][end:990090]] But the point of these statements is just to emphasize that a single observer that's uncompartmentalized cannot determine anything about the entanglement entropy of the environment.

16:30 [[start:990250][end:999214]] And this is just the result that to measure entanglement, you have to employ a LOCC protocol, so you have to have classical communication.
[[start:1002710][end:1028700]] And this raises a fundamental issue in the theory in that classical communication is an exchange of information that cannot be represented as a single quantum process.
[[start:1029390][end:1051570]] Hence, you have language like the collapse of the wave function, or these various other decoherence, etcetera, etcetera, these various ways of trying to capture this idea that something different and irreversible is happening as soon as you talk about classical communication.

17:32 [[start:1052950][end:1065030]] So the point is, for Alice to measure anything about the entanglement entropy of Bob, she has to be sectored.
[[start:1066250][end:1074122]] So her entanglement entropy has to decrease, but she can't know that.
[[start:1074256][end:1080700]] She can't actually know that she has sectored compartments when we think of Alice as an entire system.
[[start:1081470][end:1094030]] So from now on, we're going to be talking about the very limited points of view of particular observers.
[[start:1094870][end:1099218]] And to talk about that.
[[start:1099384][end:1121414]] I think it's very important to keep these various limitations in mind, because there's a real distinction between what we can say effectively from this kind of God's eye point of view that we're adopting as theorists, where we say Alice has sectors that are communicating classicall,y and what Alice's system can do from her point of view, or her sectors can do from their points of view.
[[start:1144004][end:1150420]] And this is a distinction that's often ignored, but it's important to keep it in mind.

19:17 _Daniel:_
[[start:1157190][end:1157940]] Awesome.
[[start:1158310][end:1161330]] Thanks for this line, Ander.

19:21 _Ander:_
[[start:1161690][end:1162198]] Yeah.
[[start:1162284][end:1164280]] So should we continue?
[[start:1165130][end:1188350]] Yeah, then I guess we get to the proper material of the last lecture, which is what happens when you have sectors that are commutative, such as two portions of Alice involved that have to communicate classically.
[[start:1189010][end:1191950]] This is what requires the classical communication tick.
[[start:1195330][end:1196400]] Let me see.
[[start:1197910][end:1211074]] So would it be fair to say, Chris, this--only such a classical channel,such as the one shown in this slide,requires free energy.
[[start:1211272][end:1212178]] Is that right?
[[start:1212264][end:1215750]] Because there's some writing into a memory involved in here...compared to the earlier slide where we had that closed loop in the entangled picture, there was no expenditure of energy, is that correct?
20:27 _Chris:_
[[start:1227390][end:1239040]] The example to keep in mind here is exactly the process that we're executing right now.
[[start:1241570][end:1249730]] Alice has two components, and we are currently in the position of those components.
[[start:1250470][end:1260870]] And we're communicating classically with each other by employing a channel that's part of our shared environment.
[[start:1261690][end:1268390]] So we are acting irreversibly on our shared environment.
[[start:1269770][end:1279020]] And it's that irreversible action on the environment that has the free energy cost for each of us.
[[start:1281070][end:1293520]] We actually have to make noise to communicate, and our laptops are actually consuming power.

21:34 [[start:1294130][end:1296118]] All of this is classical.
[[start:1296314][end:1302850]] It's this irreversibility that defines classicality.

21:45 _Ander:_
[[start:1305496][end:1312194]] Right. And to continue with this question, I guess it will come, I'm sure in later slides, but the other side of this LOCC protocol is the quantum channel.
[[start:1315452][end:1334810]] And my question to you, Chris, is just like there is an expenditure of time and energy involved in this classical channel, is the quantum channel basically the opposite of that, meaning its action is instantaneous entanglement, presumably, and also, again, back to that loop picture of entangled cycle, is there just no passage of time, no expenditure of energy?
[[start:1344690][end:1346740]] Does any of that make sense?

22:28 _Chris:_
[[start:1348150][end:1348610]] Yeah,and I think it's worth actually going to the next slide here where we complete the loop and add the quantum channel.

22:39 _Ander:_
[[start:1359450][end:1360662]] Is it this one?

22:40 _Chris:_
[[start:1360796][end:1361480]] Yeah.
[[start:1364090][end:1394030]] I think to understand what's going on here, I think it's very useful to think of it in terms of a Bell EPR experiment, right, where Bob, in this case, the shared environment includes the source that's creating the entangled pair, which A1 and A2 observe simultaneously.
[[start:1394930][end:1403502]] They interact simultaneously with their two detectors, which are interacting with the entangled pair.
[[start:1403566][end:1414760]] So you can think of their two detectors are entangled, and it's only later that they exchange this classical information.
[[start:1415690][end:1452450]] And in a Bell EPR experiment, the elapsed time between the source emitting the entangled pair, and the entangled pair interacting with the detectors deployed by A1 and A2 is designed as part of the experimental protocol to be less than the time that it is required for A1 and A2 to communicate classically.

24:13 [[start:1453670][end:1461800]] And notice that from the point of view of the entangled pair itself, no time has passed at all.
[[start:1462330][end:1463080]] Right?
[[start:1463850][end:1474010]] The entangled pair is, from a special relativity point of view, moving along a light-like trajectory, so there's no distance being traversed and no time is elapsing from the point of view of the entangled pair. There's only an elapsed time and a traverse distance in the coordinates of the observers.
[[start:1495330][end:1503490]] And it's those coordinates that define the parameters for the observers' eventual classical communication.
[[start:1506870][end:1520390]] So this is why I characterized the assumption of classical communication as a stipulation, and also why I characterized it as a fine-tuning assumption.

25:22 [[start:1522350][end:1548930]] We are assuming something very specific about this communication channel, and we're assuming that the part of Bob, the part of the shared environment that implements this classical communication channel, behaves differently from the rest of the shared environment.
[[start:1550470][end:1559350]] It behaves in a way that is classical, but the rest of the shared environment doesn't. Right. The rest of the world is described using quantum theory.
[[start:1564890][end:1579260]] So we're making this assumption that part of the shared environment is special, and the specialness is that it behaves in this classical way.

26:22 _Ander:_
[[start:1582270][end:1584666]] So let me finish with this slide, I suppose. So to go back to my earlier question about that entangled loop being, at least pictorically, appears like a degenerate version of this LOCC picture.
[[start:1597510][end:1616322]] If in this LOCC picture I have the quantum channel on the right, that hypothetical entanglement to complete the cycle on the left was only broken when A1 and A2 chose to write that into their memories at different sectors, right, and then that eventually necessitated the classical communication between them.
[[start:1621468][end:1622460]] Is that correct?

27:03 _Chris:_
[[start:1623630][end:1624380]] Yeah, you know, one could always take the point of view of, if you will, the observer whose outside the entire universe and just sees the entire universe evolving unitarily, and from that point of view, there's no such thing as classical communication.
[[start:1650230][end:1658370]] So the communication is classical only relative to this division between the observers.
[[start:1659610][end:1670310]] And that division between the observers corresponds to their measurement procedures not commuting.
[[start:1671230][end:1693390]] So it corresponds to what we think of classically as Alice acting on her half of the entangled state, determining what Bob will then see. All of that causal language is classical.

28:14 _Ander:_
[[start:1694050][end:1694800]] Right.
[[start:1698070][end:1700450]] We're like at 1130.
[[start:1700520][end:1712200]] So halfway, more or less, let's say a few words on the later slide, scattering is LOCC and all of that.
[[start:1714410][end:1724774]] I guess before we start talking about this, which will take us like five to ten minutes at most, could you say a few words again about the fine-tuning assumption?
[[start:1724822][end:1734010]] So I still can't quite understand what is meant here, that this whole classical communication stuff requires fine-tuning.

29:03 _Chris:_
[[start:1743020][end:1743720]] Okay.
[[start:1743870][end:1758140]] I think a way to think about it is to think about what it means to say that Alice and Bob are able to communicate classically.
[[start:1760960][end:1766068]] What we're saying is that Alice and Bob share some sort of language.
[[start:1766184][end:1773570]] So when they exchange their data, we can think of their data as written in some binary code in a data table, you know, Alice says, I set my instrument this way and I saw this spin.
[[start:1784820][end:1789596]] I then set my instrument this other way, and I made this observation.
[[start:1789788][end:1802360]] So Alice's data table, or A1's data table, is just a long table with two entries in each row.
[[start:1802940][end:1811180]] One entry is how the detector was adjusted, and the other entry is what the value of the spin was observed.

30:11 [[start:1811920][end:1814270]] And Bob's data table looks the same.
[[start:1814640][end:1822480]] And so they share this information, or they share it with some third party, they communicate it classically.
[[start:1823220][end:1826780]] And there are two aspects to that classical communication.
[[start:1826860][end:1841690]] One is that up to classical noise, their data tables don't change when they share them, so they really are irreversibly recorded.
[[start:1847980][end:1854860]] They're not evolving in time along with the rest of the universe.
[[start:1856720][end:1881540]] The other aspect is that we have to assume that Alice and Bob mean the same thing by their notations in these data tables so that they can actually compare them, so that they can actually do the statistics and see if they've violated Bell's inequality.

31:22 [[start:1882280][end:1909196]] So what that means is we have to assume that they actually share a definition of up, and that when they talk about changing the settings on their instruments, they're talking about changing those settings with respect to some shared definition of up, and you know, in a real experiment, that shared definition of up is provided by the Earth's gravitational field or something like that, Earth's magnetic field, some shared environmental variable.
[[start:1915940][end:1941540]] So now it seems like we have a situation in which Alice 1 and Alice 2 should be entangled because they share this reference frame that enables them to communicate classically, but they can't be entangled if they're going to communicate classically.

32:25 [[start:1945500][end:1956220]] So we make an assumption that, in just this case, they share a reference frame, but they're not entangled.
[[start:1957840][end:1962380]] They're able to communicate classically while sharing the reference frame.
[[start:1963040][end:1974450]] And we can sort of wave our hands and say they only share the reference frame up to some measurement resolution or something like that.
[[start:1975220][end:1993012]] But despite the hand waving, we're making a very specific assumption that violates the fact that reference frame sharing induces entanglement.
[[start:1993156][end:1995800]] So that's the fine-tuning assumption.
[[start:1996540][end:2008620]] We assume that the universe is such that in this very specific kind of case, we can have reference frame sharing without entanglement.

33:33 _Ander:_
[[start:2013200][end:2013950]] Cool.

33:35 _Daniel:_
[[start:2015760][end:2026370]] Let's keep it here and just open it up a little bit if Haris or Dean want to just give any thought or reflection on what we've gotten to so far.
[[start:2028440][end:2030870]] Haris, if you want to, please.

33:51 _Haris:_
[[start:2031880][end:2032724]] Yes.
[[start:2032922][end:2034470]] Everything is very interesting.
[[start:2035880][end:2041270]] Basically, I was listening with great, let's say focus.
[[start:2041660][end:2049608]] It reminded me this, let's say, elaboration on the previous talk that Chris gave two weeks ago.
[[start:2049774][end:2054350]] It reminded me something that Michael Levin said some time ago.
[[start:2055600][end:2061630]] It is regarding this amazing ability of cognition to scale up.
[[start:2062000][end:2072556]] So it's not only this understanding, let's say, of the scattering of cognition, but also the scaling up of cognition.
[[start:2072748][end:2091424]] And when I tried to get inside in my head, actually, that as Chris said in one of his talks, that if a system is a tag wall, one cannot draw a meaningful boundary across it.
[[start:2091562][end:2104940]] So this fine-tuning, let's say elaboration that was made right now actually helps me understand that even better.

35:05 [[start:2105010][end:2109390]] So thank you, Chris, for that and thank you Ander for this elaboration.

35:14 _Chris:_
[[start:2114320][end:2114924]] Thank you.
[[start:2115570][end:2117040]] I'm glad that helped.
[[start:2119060][end:2141960]] Yeah, I think this is intimately related to the question of what cognition is since if we have a purely quantum system, there really is a deep sense in which nothing is happening because of the time symmetry.
[[start:2142620][end:2151000]] So to talk about cognition as something that actually occurs, we have to think of it classically.

35:55 _Haris:_
[[start:2155440][end:2156344]] Thank you.
[[start:2156482][end:2169860]] Also, if you allow me another comment on that, basically one of the comments posted during your last talk in the chat had to do with classical memories.
[[start:2170200][end:2177940]] And I was thinking about that and I came to the conclusion that classical memories presupposes a gestation period.
[[start:2178520][end:2183240]] And when I think about it, that actually makes sense.
[[start:2183390][end:2189812]] And it is true, let's say, for both physical and psychological reasons.
[[start:2189956][end:2202744]] So, for example, a hard disk needs to write data on its magnetic surface and a human brain needs to consolidate all those neural connections through synaptic plasticity.
[[start:2202792][end:2203580]] Let's say.
[[start:2203730][end:2227360]] However, when we start thinking about quantum information and quantum memories, let's say, we realize that such memories will be such quantum memories basically will be stored in qubits or in those entagled states that you describe.

37:07 [[start:2227520][end:2231540]] So they do not necessarily have the same limitations.
[[start:2231980][end:2250312]] And of course, quantum information theory suggests, as I understand it, that quantum memories can be created and accessed instantaneously without any form of gestation, let's say without any gestation period.
[[start:2250456][end:2268508]] And of course this goes back and it has the potential, as I see, to revolutionize computation in terms of quantum computation, but also, and most importantly, communication and quantum cryptography even.
[[start:2268694][end:2274550]] And this is something that I am truly interested in.
[[start:2275240][end:2279350]] So yeah, I just wanted to share also that.

38:03 _Chris:_
[[start:2283740][end:2286570]] Yeah, that's a very good point.
[[start:2288540][end:2314960]] And the flip side is the issue of stability which again gets to the notion of environmental decoherence which is just the process of observation of the quantum state by some environment or some observer, some component of its environment.
[[start:2316020][end:2330150]] And the reason this is a problem in practice is that we don't have complete control of all components of the environment, right?
[[start:2331580][end:2352780]] So we have to use things like liquid helium to try to keep the environment at bay to prevent decoherence because any other components of the environment interacting with our quantum memory will alter the state of the memory.

39:16 _Haris:_
[[start:2356660][end:2366160]] Yeah, that is a great answer and basically the reason why I typed that question regarding super selection rules, and namely me, I propose something called fuzzy super selection rules.
[[start:2376700][end:2403280]] Basically, as I understand it, those super selection rules, the classical ones, let's say they are based on symmetries or on all those conservation laws that actually limit the accessibility or our capacity to measure, let's say, certain quantum properties, let's say, maybe it's parity, maybe it's angular momentum, maybe it's even charge.
[[start:2403940][end:2426740]] But if we start thinking like these fuzzy super selection rules in an effort to relax these restrictions by allowing some degree of coherence or interference between the different super selected sectors, which can be quantified, let's say, by a parameter called fuzziness.

40:26 [[start:2426900][end:2446496]] I know that in other fields, like in my field, that is fuzzy cognitive mapping, the introduction of fuzziness, as it was propounded by Professor Lotfi Aliasker Zadeh, it actually helped a lot of our models to become more accurate, let's say.
[[start:2446598][end:2449484]] So this is what I am proposing.
[[start:2449532][end:2464672]] Maybe of course, I don't expect it to revolutionize quantum information, but maybe it can help us understand a bit better what is going on and the role of the coherence that comes out of the environment.
[[start:2464736][end:2474650]] So if we incorporate it as a parameter of fuzziness, a priority, then maybe we can understand what we are dealing with.

41:18 _Chris:_
[[start:2478510][end:2479260]] Yeah.
[[start:2481150][end:2487450]] I would refer you to the paper by Bartlett...there are two other co-authors--in 2007--a lovely review of quantum reference frames in Reviews of Modern Physics [2007, Reference frames, superselection rules, and quantum information, Bartlett SD, Rudolph T, Spekkens RW].
[[start:2500654][end:2512950]] And a point that they make, that I think is relevant here, is that a super selection rule can always be interpreted.
[[start:2514410][end:2515480]] Let me see...I'm not sure I'll be able to completely reproduce their argument, but they show that a super selection rule can always be interpreted as the absence of a reference frame or the lack of a reference frame.
[[start:2532750][end:2546270]] And one of the examples that they give is charge conservation--that we never see superpositions of different electric charges.

42:27 [[start:2547750][end:2555234]] And their point is--we never see this because we have no way of measuring it.
[[start:2555272][end:2569030]] We have no reference frame that we could use that would allow us to see a state of superposed charges.
[[start:2570490][end:2587150]] And effectively what they're saying is our reference frames are all made of matter that is composed of stuff that has well defined electric charges.
[[start:2587570][end:2592906]] So we can't see things that are superpositions of charge.
[[start:2593018][end:2598160]] And it's very difficult for us to see things that are superpositions of position.
[[start:2599910][end:2623658]] So this question of what is a super selection rule, why do we have these rules, at least in their reasoning, boils down to the question of why do we have some reference frames or some measurement capabilities and not others?

43:43 [[start:2623744][end:2632970]] What is it about us that limits in some fundamental way our ability to make measurements?
[[start:2634190][end:2663160]] And I suspect that when you talk about fuzziness, which is a sense of classical uncertainty, that you may be sort of pointing in that direction, but I think it would be worth looking at that paper, which is largely written in English, right?
[[start:2663690][end:2667590]] The formalism is kept in the background.
[[start:2669690][end:2671880]] So it's a very nice paper.

44:35 _Haris:_
[[start:2675150][end:2676140]] Thank you.

44:38 _Daniel:_
[[start:2678270][end:2679260]] Thank you.
[[start:2679870][end:2680502]] Ander, maybe mute a little bit.
[[start:2682160][end:2687520]] Dean on the mountaintop, what can you throw down on us?

44:51 _Dean:_
[[start:2691910][end:2695778]] I don't have anything super special throw down.
[[start:2695944][end:2709218]] I have a question, though, and because I am very comfortable in that fuzzy space, I kind of see relationships and their lack of definability as a feature.
[[start:2709314][end:2712040]] So here's kind of my question.
[[start:2713450][end:2717594]] So you talked about a minimum sort of two different memories to encode something in time.
[[start:2717632][end:2726122]] And I think it was one of the slides just after the one that's up here right now, which sounds to me like "somewhere" processing capacity.
[[start:2726186][end:2739234]] It sounds like we are kind of stepping back and trying to look at this instantaneous thing, from the relative position of even the things that are classical that can be seen as all quantum.
[[start:2739432][end:2743940]] So that when you mentioned that earlier, Chris, that helped me quite a bit.
[[start:2744950][end:2749182]] Which then manifests itself as a classical ability to process somewhere.
[[start:2749326][end:2754390]] I spent a lot of my career self-labeling as a wayfinder.

45:55 [[start:2755210][end:2758200]] So not capacity realization--relationship, just as a relationship.
[[start:2762524][end:2772746]] It means that wayfinding is not just an orienting or a processing, where I am and being gripped by sort of the thing that I'm enveloped by.
[[start:2772768][end:2779450]] It's also the channel, the screen, the bound, the divide, the gap, the unentangled potentiator.
[[start:2779610][end:2784960]] It's the thing upon which traction can exist as being a gripper as well.
[[start:2787810][end:2799758]] I was already hung up on I wanted to go back like Colombo in that old 70s TV show, and talk about Z spin because I think Z spin is an energy way of describing.
[[start:2799934][end:2815290]] But I honestly think when I went back and watched your presentation a couple of times, I'm starting to get a sense that Z spin is also relationship. It's that affordance that allows us to be able to see up and down.

46:55 [[start:2815440][end:2836798]] But I'm just curious, Chris, are we really talking about processing somewhere in the classical sense, but because we have these two ways of encoding different memories, we're also talking about, somewhere processing, just that state that allows for that.
[[start:2836894][end:2843460]] My question is that--what we're really getting, are we trying to open up that possibility?

47:28 _Chris:_
[[start:2848230][end:2853400]] Yeah, I think that's a nice way to think about it.
[[start:2856170][end:2871180]] I think we're trying to, at some deep level come up with a way of describing what it means to be an agent and I'll say in our case, a self-conscious agent with a sense of time that's embedded in an environment that we depend on to store memories for us.
[[start:2893030][end:2918250]] And what I mean by that is that we depend on the environment to change very slowly, at least from our point of view, so that we can keep some sense of our orientation within the environment.

48:39 [[start:2919310][end:2919770]] Right.
[[start:2919840][end:2934720]] We're using everything we see as a memory that allows us to keep ourselves fixed, which allows us to have a point of view.
[[start:2935990][end:2948500]] So we're using the entire visible environment as, if you will, a reference frame against which we can see small changes.
[[start:2949610][end:2964060]] But if the environment was constantly and rapidly changing, we wouldn't be able to do that and we wouldn't be able to use it as a memory and so we would have no point of view.
[[start:2965070][end:2978960]] So in a sense, I think what we're talking about here is the miracle of having a point of view that gives us a sense of time.

49:44 [[start:2984320][end:2985980]] That's very philosophical.

49:48 _Daniel:_
[[start:2988980][end:2989856]] It's amazing.
[[start:2989958][end:2997936]] And I wonder if along with the perspectival visual advancements which you and Shannon Dobson have explored in the math art settings, you're almost bringing that kind of a transformative re-understanding or re-quantum reference framing into a temporal setting where it's not just a static spatial parallax that we are aesthetically and formally re-understanding.
[[start:3023636][end:3048320]] But also a temporal one, which, in an agent environment system, necessitates these questions of communication, which, in the quantum information formalism, are approached topologically rather than geometrically, which is what we needed for the kind of vanishing point type math art in the spatial setting.

50:50 _Chris:_
[[start:3050900][end:3059908]] Well, I think they're approached geometrically eventually and that's really what the session in September will be about.
[[start:3060074][end:3084190]] It's how to start with this very topological picture where we're only talking about interactions in a sense, interactions in time, but outside of space and layer a spatial structure on top of that.
[[start:3085360][end:3115690]] And I think this is particularly interesting in this active inference context because it immediately raises biological questions about the ability of different organisms to layer space on their experience and hence locate themselves, if you will, within some sort of perceived world.

52:00 _Daniel:_
[[start:3120060][end:3120664]] Awesome.
[[start:3120782][end:3124170]] Dean and then back to Ander for the last minutes.
[[start:3129180][end:3130056]] Oh, wait, unmute.
[[start:3130088][end:3131710]] Dean and then please continue.

52:13 _Dean:_
[[start:3133440][end:3134190]] Sorry.
[[start:3134640][end:3154790]] So, Chris, is it from the pure neophyte perspective that I have, is it OK to say that it's not just a flipping of position of words, that somewhere processing--that availability and processing somewhere in the classical sense of "where am I"...
[[start:3155160][end:3164630]] It's our ability to fuse those, as you mentioned, we can slow down, we can stabilize, we can see that relationship.
[[start:3165100][end:3175050]] Or is it about spin?

52:59 _Chris:_
[[start:3179230][end:3182140]] I think the former, right.
[[start:3182610][end:3190350]] Spin is a very convenient abstraction for talking about binary encoding.
[[start:3193840][end:3203324]] And we have this felt sense of spin, but its use in physics is very much an abstraction.
[[start:3203452][end:3207840]] I mean, the difference between a proton and neutron is a spin variable.

53:32 _Daniel:_
[[start:3212810][end:3213560]] Awesome.
[[start:3214170][end:3224360]] Ander you can in the last minutes take it where you need, also unmute and then continue.

53:46 _Ander:_
[[start:3226110][end:3227660]] Can you guys hear me now?
[[start:3228430][end:3232714]] So let's hope that I have time for Chris to address a couple of things.
[[start:3232832][end:3239690]] So just to conclude the slides and then hopefully we get to say a few words on quantum Darwinism.
[[start:3239850][end:3248640]] So towards the end, the slides appear to start pivoting towards the next subject, which is space and time.
[[start:3249030][end:3264870]] And here in particular, we see the earlier slide showcasing the LOCC protocol where you can notice that half of it has been cut and has been moved to the future.
[[start:3264940][end:3270840]] So here we don't have two sectors of Alice communicating, but rather Alice communicating with its future.
[[start:3271450][end:3274098]] Still, you have the classical and the quantum channel.
[[start:3274284][end:3289520]] Now, one question that I brought up, I remember and in the lecture, and maybe we can expand on a little more, was exactly what is the difference between this quantum and the classical channel part?

54:50 [[start:3290450][end:3295610]] Something I heard Chris say is that it is crucial for the quantum channel to be recohered.
[[start:3295690][end:3305060]] So this is going to be some sort of unitary scattering evolution that is completely independent of everything else going on.
[[start:3305750][end:3307938]] Is that correct, or should be in theory?

55:13 _Chris:_
[[start:3313120][end:3313870]] Yes.

55:15 _Ander:_
[[start:3315540][end:3324988]] And I suppose, just like earlier, the classical channel is the part that takes time and free energy expenditure.
[[start:3325164][end:3340490]] Now, my question to you, Chris, is not the channels in the middle, but the ticks on either side of the boundaries that have been broken down and separated in terms of an external time.
[[start:3341180][end:3344964]] What's up with those ticks from one sector to the other of the boundary?
[[start:3345092][end:3352984]] So in Q1, for example, the lower QRF sector, that amounts to a state that was prepared.
[[start:3353112][end:3357004]] The upper one was "I made a memory record of that state."
[[start:3357122][end:3358670]] That's what it is, right?

55:59 _Chris:_
[[start:3359680][end:3360430]] Yeah.

56:00 _Ander:_
[[start:3360800][end:3370610]] Okay, so in the lower sector, we both had a preparation and a measurement, and a measurement was recorded classically here.
[[start:3371540][end:3372850]] That's all there is.

56:14 _Chris:_
[[start:3374020][end:3374816]] Yeah.
[[start:3374998][end:3379750]] So preparation and measurement are effectively the same process.
[[start:3381960][end:3409890]] And you can think of, in A1 of (t) is what A1 is doing, which is--from an operational point of view--she's preparing an instrument and turning it on.
[[start:3410820][end:3443260]] She's creating an initial state, and she's simultaneously encoding a memory someplace in her head, or on a piece of paper of what those preparation conditions were, because it's only with respect to the memory of what the preparation conditions were that the later measurement is meaningful.

57:28 [[start:3448560][end:3451980]] Let's go back to just preparing a spin.
[[start:3454822][end:3468420]] At (t), she may set the angle of some polarization filter that defines a propagating beam of photons.
[[start:3469320][end:3475812]] And at t plus delta t, (t+dt), she measures something about what those photons are doing.
[[start:3475946][end:3487210]] But the measurement is only meaningful with respect to her memory of what the polarization setting that prepared the photons was.
[[start:3489260][end:3512720]] So effectively, what's going on in the quantum channel is an experiment, and it's the classical information that's preserved in this classical channel that makes the experiment meaningful or interpretable or informative.

58:33 _Ander:_
[[start:3513060][end:3514320]] Yeah, for sure.
[[start:3514470][end:3517904]] Yeah, that makes perfect sense in preparation of measurement.
[[start:3517952][end:3532630]] This ties back to an earlier question we had... both happen simultaneously at the same degree of freedom at the boundary, or do we have preparation at the lower bound measurement, at [inaudible]?

58:56 _Chris:_
[[start:3536140][end:3548424]] Yeah, one can think of that operator, mi...if you remember the decomposition of the Hamiltonian as preparing or measuring.
[[start:3548552][end:3553144]] It's just a matter of interpretation effectively.
[[start:3553192][end:3556050]] Is it acting to the left or acting to the right?

59:18 _Ander:_
[[start:3558260][end:3558912]] Yeah.
[[start:3559046][end:3559344]] Okay.
[[start:3559382][end:3559968]] Yeah.
[[start:3560134][end:3561072]] Makes perfect sense.
[[start:3561206][end:3572230]] And then before we get to quantum error correction as more of a spatial instead of a time thing, I wanted to ask about yet another question between this one.
[[start:3573400][end:3588170]] So the quantum channel does involve some sort of time evolutionary portion, that is, this portion that is evolving unitarily with no interference from the outside.
[[start:3589100][end:3603640]] However, as you said, for this experiment to make sense, you need to have a classical memory of how that experiment was prepared, so that means that classical guy on top is static.
[[start:3603720][end:3605470]] There's no time flow in it.

1:00:07 _Chris:_
[[start:3607140][end:3617030]] Well, this actually gets back to the talk by [Leonard] Susskind that we were talking about before we started here, that you kindly referred me to.
[[start:3620360][end:3631800]] Part of this classical memory is memory for what counts as a classical clock.
[[start:3632620][end:3636516]] And we'll actually get to this again in the September session.
[[start:3636708][end:3662400]] But if you think again about doing an experiment in which a state is prepared and then it's measured, this quantum process is a process through time with respect to some classical clock that actually provides the time coordinate for the experiment.
[[start:3663700][end:3683620]] So this classical clock is some external reference frame that A1 here in this notation is using as part of her classical memory.

1:01:25 _Ander:_
[[start:3685480][end:3685904]] Right.

1:01:25 _Chris:_
[[start:3685962][end:3692090]] Again, it's a memory because it's something that's assumed not to change.
[[start:3695600][end:3710130]] This will be kind of the heart of the discussion in September that time and memory and object persistence are all different names for this same assumption that we make about the world.

1:01:57 _Daniel:_
[[start:3717160][end:3718420]] Thank you, Chris.

1:01:59 _Ander:_
[[start:3719000][end:3719796]] Thank you.

1:01:59 _Chris:_
[[start:3719898][end:3722310]] I am going to have to disappear.

1:02:03 _Daniel:_
[[start:3723480][end:3725110]] Only for now though.

1:02:05 _Chris:_
[[start:3725800][end:3727510]] Yeah, only for now.
[[start:3728220][end:3730760]] I will nonetheless persist someplace.

1:02:11 _Ander:_
[[start:3731820][end:3734660]] Thank you, Chris, so much, Chris.

1:02:14 _Chris:_
[[start:3734820][end:3736410]] Okay, awesome.
[[start:3737100][end:3737816]] See you.
[[start:3737918][end:3739050]] Thanks very much.

1:02:19 _Daniel:_
[[start:3739580][end:3740890]] Measure you later.
[[start:3745500][end:3761490]] Ander, if you wanted to drop any other cues or clues or bring us a little bit of a preparation for where we're going to be heading in lecture 5, that would be pretty cool.

1:02:43 _Ander:_
[[start:3763300][end:3763712]] Sure.
[[start:3763766][end:3768150]] So, I mean, I'm a little aware of what's coming in lecture 5.
[[start:3769560][end:3786244]] It's about space and time and how space may be, sorry, time may be a little more fundamental than space, for reasons that Chris will show...has a lot to do with the notion of how you define a clock, as in, we need to think hard about what are the bare minimum ingredients for you to talk about the existence of a clock.
[[start:3796888][end:3801528]] These are deep fundamental, almost philosophical questions that are overlooked.
[[start:3801704][end:3815004]] And the good news, and that's the [Leonard] Susskind talk that Chris and I were referring to, is that other people, especially in the high energy community, are also looking into these questions, which is very reassuring.
[[start:3815052][end:3830570]] So I'm talking at [Edward] Witten, [Leondard] Susskind, [Daniel] Harlow, etc. There is a recent talk on YouTube where they talk about what does it mean for something to be a clock; how long does a clock last?

1:03:50 [[start:3830940][end:3833770]] And then Chris will also talk about space.
[[start:3834300][end:3847324]] And the punchline of it will be that there's obviously a physics approach to emergent spacetime, which is very technical and so on.
[[start:3847522][end:3862600]] But from what I understood (I have yet to see the talk myself first), is that there is a parallel biological approach as to how we learn out spacetime.
[[start:3862760][end:3875712]] So from developmental psychology point of view infants, and I suppose all kinds of animals are not born fully equipped to perceive spacetime, hence, the necessity of things like play and so on.
[[start:3879294][end:3885784]] So they can find correlations between motor inputs and visual inputs, right?
[[start:3885902][end:3889880]] And eventually things like the mirror test, which is nontrivial.
[[start:3890620][end:3895070]] No human is born passing the mirror test already.

1:04:55 [[start:3895840][end:3899832]] So that implies that at least biologically, it is nontrivial.
[[start:3899896][end:3906632]] And it takes a few steps until you get to have that sort of spatial awareness.
[[start:3906776][end:3907470]] Right?
[[start:3907920][end:3913520]] Now, the interesting part, at least for me personally, is what the physics side of it is.
[[start:3913670][end:3924950]] And I'm no expert by any means, but I think the gist of it might have to do something with quantum error correction, [acronyms?] and so on.
[[start:3925720][end:3930170]] There was a bit of a teaser about quantum error correction here in these.
[[start:3931340][end:3933850]] Yeah, I mean, that's that's about all I can say.
[[start:3934460][end:3937130]] But very looking forward to the biology also.

1:05:37 _Daniel:_
[[start:3937900][end:3939304]] Yeah, cool.
[[start:3939502][end:3944670]] Haris any last thoughts or anything you want to point towards?

1:05:46 _Haris:_
[[start:3946000][end:3950028]] Basically, I would like to thank everyone for inviting me.
[[start:3950194][end:3956140]] I really enjoyed it the whole livestream.
[[start:3956740][end:3969670]] I hope we have made some progress and looking forward to the next live streams number 5 and number 5.
[[start:3970840][end:3973220]] So that's about it.
[[start:3973290][end:3974230]] Thank you, everyone.

1:06:14 _Daniel:_
[[start:3974760][end:3975750]] Thank you.
[[start:3976280][end:3977044]] Anything else, Ander?

1:06:17 _Ander:_
[[start:3977082][end:3979396]] That's it.

1:06:19 _Daniel:_
[[start:3979498][end:3979860]] Awesome.
[[start:3979930][end:3991468]] Well, I encourage everyone to go to the syllabus page, look ahead, look back, pregest, digest, regest, ask questions and let's make progress as you exhort, Haris.
[[start:3994552][end:3996956]] So, see you all.
[[start:3997058][end:3997850]] Till next time.
