---
title:  'Physics as Information Processing - Lecture 4, "Communicating Observers"'
author:
- 'Chris Fields (Allen Discovery Center at Tufts University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-4812-0744)'
- 'Ander Aguirre (Ohio State University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-6337-8292)'
- 'Daniel Friedman (Active Inference Institute; University of California, Davis) [![Orcid](images/orcid.png)](https://orcid.org/0000-0001-6232-9096)'
date: "2023-08-10 Version 1.0"
...

# Lecture 4, "Communicating Observers"

00:07 _Daniel:_
[[start:7390][end:9306]] Hello and welcome, everyone.
[[start:9488][end:10422]] This is Physics
[[start:10486][end:14806]] as Information Processing, Session 4, on Communicating Observers.
[[start:14918][end:17740]] It's the 10th of August, 2023.
[[start:18110][end:20390]] Chris, looking forward to this lecture!

00:20 [[start:20470][end:21580]] Off to you.

00:23 _Chris:_
[[start:23470][end:26810]] Thank you, Daniel, and welcome to this session.
[[start:27310][end:30734]] As Daniel said, this is about communicating observers.
[[start:30862][end:35540]] And fasten your seatbelts because we have a lot to cover in the next hour.

[[start:36870][end:39170]] So just to do a quick review.

00:39 [[start:39320][end:55850]] We've been talking about quantum information theory and we've been talking about it in the simplest possible setting of two systems, Alice and Bob, that exchange information through their mutual boundary.
[[start:56350][end:60118]] And we've assumed that everything is finite dimensional.
[[start:60214][end:65130]] So we don't need to worry about infinite energy transfer across this boundary.
[[start:65790][end:72682]] And of course, we assume conservation of energy, so there are no sources or sinks in either of the systems, Alice and Bob.
[[start:72746][end:87250]] And we emphasize that this way of depicting things as topological; we're not assuming any background geometry, no sort of spatial embedding, which is going to become very important in this session.

01:29 [[start:89750][end:102706]] In the last session, we talked about how the boundary, which I'll always call "B," can be thought of as a channel that comprises N qubits that are independent.
[[start:102818][end:113450]] And Alice and Bob each can prepare and measure those qubits, and they can always choose independently their reference frames for doing so.
[[start:113520][end:121070]] So how they define up and down when they're measuring a spin with effectively a Z-spin operator to interact with these qubits.
[[start:125810][end:130690]] We talked a little bit about the free energy principle and its quantum formulation.

02:11 [[start:131510][end:143250]] And the principle basically says that interacting systems will behave in a way that aligns their reference frames, and that they therefore asymptotically approach entanglement.
[[start:143410][end:147906]] So the FEP is a classical limit of the principle of unitarity.
[[start:148098][end:161100]] And that's one reason for studying quantum information - to learn more about the FEP and so to learn more about active inference, and what the theory of active inference says about agents.

02:42 [[start:162990][end:172880]] And last time, we talked a lot about the constraints that are imposed by a limited free energy supply on any agent.
[[start:174050][end:191626]] Recall that we talked about the fact that in the absence of sources of free energy within an agent - so, as long as you conserve energy globally, that the free energy that each agent uses has to come from its environment.

03:11 [[start:191758][end:193590]] That's clearly true for us.
[[start:193660][end:199510]] We have to consume oxygen and eat food and things like that to keep running as systems.
[[start:200490][end:216970]] And we discussed a little bit this theorem [[see slide "Free energy constraints induce compartmentalization"]], that if two reference frames or quantum processes, Q1 and Q2 don't commute, they have to be implemented by compartments that communicate classically.
[[start:217050][end:219520]] And we'll use this extensively today.
[[start:220450][end:233970]] But the bottom line, last time, was that physics alone gives us compartmentalization in systems whenever the systems are complex enough to have multiple kinds of measurements that they can't deploy simultaneously.

03:56 [[start:236390][end:254470]] So where we're going: Today, we're going to start from this place we left off last time, of the possibility of agents that are compartmentalized into compartments that have to communicate classically.
[[start:255070][end:270830]] So we're going to talk about agents that can be compartmentalized into multiple subagents that share an environment, the environment consisting of Bob, and how those agents talk about that shared environment.
[[start:271490][end:274000]] So the motivation for this is simple.
[[start:274450][end:278250]] It's that what we do all the time is a group activity.
[[start:278330][end:283470]] And what we're doing right now is a group activity that involves sharing an environment such as what's shown on this screen, and talking about it.
[[start:287430][end:296886]] And the whole post-session discussion process will be another example of just that sort of thing.

04:57 [[start:297068][end:313130]] So to talk about science at all, or to talk about any kind of social relation or to talk about anything other than solipsism, we have to be able to talk about how multiple agents communicate about some shared environment.
[[start:313630][end:318000]] And so that's what we're going to develop a formal way of talking about.

05:19 [[start:318690][end:323920]] And there are two things to notice right off the top about this.

05:24 [[start:324610][end:331310]] One is that the way we've defined interactions at boundaries, they're effectively instantaneous.
[[start:331470][end:337758]] So each agent, remember, interacts with its boundary with some set of operators.
[[start:337854][end:345326]] And what those operators do is effectively measure each operator--effectively measure the spin of a qubit.
[[start:345518][end:347940]] So this is a very fast process.

05:50 [[start:350390][end:370762]] The other thing that we then need to notice is that if we have two agents and they're communicating with each other classically, then they're going to be using degrees of freedom of their shared environment in order to communicate.

06:10 [[start:370906][end:373278]] And that's exactly what we're doing right now,
[[start:373364][end:379718]] for example. We're using degrees of freedom of the internet to communicate.
[[start:379914][end:391140]] I'm using degrees of freedom of the local atmosphere to talk to my microphone and I'm using degrees of freedom of the local photon field to see my screen.
[[start:392090][end:403122]] So all communication between agents, and certainly all classical communication between agents, uses degrees of freedom of the environment.

06:43 [[start:403186][end:410090]] And the environment, remember, is the other system, Bob, that's on the other side of that shared boundary.
[[start:410750][end:420698]] So we're going to be interested in how components of Alice use Bob as a communication channel - and in fact, as multiple communication channels.
[[start:420874][end:429558]] And I just wanted to quote my colleague and friend, Mike Levin, in his statement that "all intelligence is composite."
[[start:429754][end:449270]] All of us, all organisms, even single cells, are composite systems that comprise many many different agents that are able to make different kinds of measurements and execute different kinds of actions, and so have to communicate classically.

07:30 [[start:450010][end:458780]] So we're talking about all of life here, as well as all of social systems and ecosystems and such things as that.

07:40 [[start:460270][end:470490]] So the first thing I want to do today is simplify the notation so that we don't have to draw quite such complicated diagrams.
[[start:470650][end:474618]] So the picture on the left here [[see slide "First, simplify the graphic notation..."]] is a picture from the last session.
[[start:474794][end:490900]] It shows the structure of a very simple agent that makes some measurements using a reference frame called "E," and then writes some results of those measurements to memory using a reference frame called Y.
[[start:491450][end:500662]] And those two processes are connected by an internal clock that ticks between the input process and the output process.
[[start:500796][end:508490]] And the clock tick corresponds to the expenditure of free energy to write information irreversibly on the boundary.

08:28 [[start:508830][end:515478]] So the memories are actually written on the boundary because that's where classical information lives in this theory.

08:35 [[start:515654][end:530930]] So you can think of this whole process from E through the clock and back to Y as a single quantum process, or as a quantum computation, that maps some sector E of the boundary to some sector Y of the boundary.
[[start:531590][end:544150]] And so we can represent it in this much simpler way that's over on the right side as some process Q that maps some sector on the boundary to some other sector on the boundary.
[[start:544650][end:551030]] And formally, that process can be thought of as a topological quantum field theory.

09:11 [[start:551530][end:553446]] Topological here is important.
[[start:553548][end:561660]] It's not geometric, it doesn't assume an embedding in space and this will become critically important later on.
[[start:562030][end:573790]] And the operation of that TQFT [Topological Quantum Field Theory] requires a clock tick or it incorporates a tick of this internal clock.
[[start:574370][end:592530]] And we can do this because we were able to prove--James Glazebrook and Antonino Marciano and I [(2022) Sequential measurements, topological quantum field theories, and topological quantum neural networks]--were able to prove last year that we can always represent a quantum reference frame as a topological quantum field theory.

09:52 [[start:592690][end:599526]] And this just illustrates the two kinds of transformations between quantum reference frames that are important. [[See slide "This reflect a general result: QRFs are TQFTs"]]
[[start:599628][end:622730]] We can take one and divide it into two pieces that commute. Or we can take a two-part reference frame and we can swap in another part that doesn't commute with the part that we've swapped it in for, but that does commute with the remainder of the reference frame.

10:22 [[start:622810][end:637394]] So here "R" is the reference component of some object identification system; and we can swap in some different way of looking at the object once we've identified it.
[[start:637432][end:661690]] So, for example, if the object that we're identifying is a box that can measure both Z spin and X spin, then P and Q can be the Z-spin and X-spin settings on that box that allow us to effectively rotate the filter from this way to that way, so that we measure vertical spin versus horizontal spin.

11:02 [[start:662110][end:663562]] And that's really it.
[[start:663616][end:669194]] I mean, those are the ways that one can transform quantum reference frames.
[[start:669322][end:687810]] Of course, we could do arbitrarily many compositions of this kind of transformation to do something very complicated, but they map very simply to TQFTs with the structure. And you can construct categories out of this and find a functor that's well defined that maps one category to another.

11:27 [[start:687880][end:698390]] So it's an example of a nice use of categorical techniques for solving a problem that looks difficult but in fact it's very straightforward.
[[start:699370][end:728350]] So using this simplified notation, it becomes very easy to see that if we have two systems, Alice and Bob on opposite sides of this boundary and we perfectly align their quantum reference frames, which is what the FEP says they will tend to do, then they become entangled.

12:08 [[start:728790][end:739940]] And you can see that they're entangled by seeing that once the reference frames are perfectly aligned, they jointly implement one quantum process.
[[start:741610][end:746630]] And jointly implementing one quantum process just means you're entangled.
[[start:747290][end:753640]] The two sides no longer have conditionally independent states.

12:34 [[start:754190][end:763930]] If one quantum process, which is time reversible, information preserving, is implemented jointly by the two systems.
[[start:764510][end:786158]] So a lot of things like this become very simple when we think of these processes as just quantum computations going on inside some system, implemented by some system, and how those processes relate across some boundary.
[[start:786334][end:792680]] So that's what we're going to do for studying communication today.

13:14 [[start:794410][end:812454]] Another thing to recall from a couple of sessions ago, or last session, [[Clarify! - ed.]] is that if two reference frames, Q1 and Q2, commute, we can always join them together to form a single reference frame.
[[start:812502][end:818560]] And this is just a graphical depiction in this simpler language of how that works.

13:39 [[start:819250][end:826862]] And topologically, there's no distinction between the left side and the right side.
[[start:826916][end:834210]] What I've done is just squeeze the top two green circles together and the bottom two green circles together into one circle.
[[start:834790][end:840594]] And that just makes a simple process connecting the top one to the bottom one.
[[start:840792][end:856170]] So what we're going to be interested in, is situations where this doesn't happen, where Alice consists of two components that execute reference frames that don't commute.

14:16 [[start:856750][end:862822]] And so the two components _are_ conditionally independent.

14:22 [[start:862886][end:866410]] They _do_ each have free choice of reference frame.
[[start:867090][end:870074]] And so they have to communicate classically.
[[start:870202][end:877070]] They don't share a single quantum process, so they're not entangled.
[[start:878130][end:908006]] And before we go ahead to do that, I just wanted to remind you of some of the no-go theorems that follow from this situation depicted on the right, where we have a single agent executing a single reference frame, a single process, a single kind of measurement, any set of commuting measurements that can be combined into one measurement.
[[start:908198][end:910666]] And here are some things Alice can't do.

15:10 [[start:910768][end:913450]] And we've talked about some of these previously.
[[start:913870][end:916490]] So this is basically a reminder.

15:17 [[start:917090][end:927626]] But Alice can't, using just one measurement, measure the entanglement entropy across her own boundary.
[[start:927818][end:931442]] So Alice can't know that she has an independent state.
[[start:931576][end:935598]] She can't know that she's _not_ entangled with Bob.

15:35 [[start:935774][end:942360]] And that's a useful thing to think about philosophically as it applies to you and me.
[[start:942810][end:946360]] We can't actually know that we have independent states.![image](https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/assets/30888152/e202d421-db89-4b87-abd6-588203f0a920)

15:47 [[start:947690][end:957530]] Alice can't measure her own entanglement entropy, so she can't know whether she has components that have to communicate classically.

15:59 [[start:959630][end:968430]] She can't measure _Bob's_ entanglement entropy, so she can't know whether Bob has compartments that have to communicate classically.
[[start:968850][end:978670]] And if you think in terms of perception theory, this says Alice can't know whether Bob consists of separate objects that behave classically.
[[start:981190][end:993190]] Their behavior can look classical to her, but she's not able to determine that their behavior _is_ classical, because she can't measure Bob's entanglement entropy.

16:34 [[start:994410][end:1014540]] She can't measure the dimension of her own boundary. And recall from a couple of times ago that the boundary includes some sector that supplies free energy that Alice can't extract information from for further processing, she can only extract free energy from.
[[start:1014990][end:1023360]] So she can't measure the dimension of that sector, and so she can't measure the dimension of the whole boundary itself.
[[start:1023970][end:1027646]] And this, of course, means that she can't measure her own dimension either.

17:08 [[start:1027748][end:1036382]] And of course, she can't measure Bob's dimension, because the only information she can get about Bob is the classical information that's encoded on this boundary.
[[start:1036446][end:1041220]] She can't reach past the boundary to see how large a system Bob is.

17:21 [[start:1041850][end:1057350]] And that's clearly connected to this first point, that she can't measure the entanglement entropy across Bob, because the entanglement entropy can only be small if her dimension and Bob's dimension are both much larger than the dimension of the boundary.
[[start:1057430][end:1059740]] So that's a condition she can't check.

17:41 [[start:1061310][end:1066330]] So all of these kind of no-go theorems lead off in interesting directions.
[[start:1066690][end:1088610]] And the only one that we're really going to be interested in here is the third one, the one about measuring Bob's entanglement entropy, because we want to talk specifically about how multiple agents, so _multiple_ components of Alice, can access information about Bob's entanglement entropy.

18:13 [[start:1093050][end:1101290]] Okay, so recall from the end of the last session that the last thing we talked about was classical communication.

18:21 [[start:1101950][end:1111920]] And we talked about the fact that classical communication involves assumptions and pitfalls and that we have to be very careful whenever we talk about it.
[[start:1112450][end:1117178]] And what we're going to do today is standard practice in physics.
[[start:1117274][end:1127390]] We're simply going to _stipulate_ that these components, A1 and A2, the separable components of Alice, communicate classically.
[[start:1127470][end:1129202]] And so we're going to draw it like this. [[See slide "Recall from July session:"]]

18:49 [[start:1129256][end:1135330]] We're going to draw a classical channel between them, and that classical channel passes through Bob.
[[start:1135410][end:1149610]] It uses degrees of freedom of the ambient photon field or the ambient atmosphere or pieces of paper or email or something like that, that's out there in the environment, to exchange classical messages.
[[start:1150510][end:1154394]] And there are a couple of things to note here - I haven't even written down here.
[[start:1154432][end:1159322]] We're assuming that A1 and A2 share some **language** for this classical communication.
[[start:1159386][end:1162320]] That's a big assumption, as we talked about last time.

19:23 [[start:1163810][end:1168398]] But I will note explicitly that classical communication takes time.
[[start:1168564][end:1171554]] That's what defines classicality here.
[[start:1171592][end:1176180]] It's causal, so it can't work faster than the speed of light.

19:37 [[start:1177030][end:1179150]] This is a topological theory.
[[start:1179230][end:1181102]] We don't have any embedding geometry.
[[start:1181166][end:1191240]] So we can't, at this point, talk about light, which is a relationship between space and time, because we've got time, we've got clocks, but we don't have any space.

19:51 [[start:1191930][end:1201900]] But we _can_ say that whatever passes through this classical channel requires at least one clock tick on Bob's side.
[[start:1202590][end:1206330]] So it's a process that Bob has to execute.
[[start:1206930][end:1210158]] And executing that process takes time.
[[start:1210244][end:1216318]] So getting the signal from me to you on the internet takes some time so the environment's clock has to tick during that.

20:21 [[start:1221110][end:1241686]] And all of these assumptions bundled together turn out to be a fairly serious set of assumptions. And they involve assumptions about fine tuning, about the universe being just right. And they should make us nervous! And I just want to leave it at that.
[[start:1241868][end:1247142]] We always assume, with complete aplomb, that agents can communicate classically. But it's not a straightforward assumption--and it's worth... Any of you who are looking for interesting research projects, can look into the nature of classical communication.
[[start:1258506][end:1266846]] It's full of hidden assumptions and surprises and things that aren't at all straightforward, even though they look like they ought to be.

21:07 [[start:1267028][end:1268590]] So there's a challenge.
[[start:1269890][end:1271374]] So why do we assume this?
[[start:1271412][end:1273758]] Why do we assume classical communication?
[[start:1273934][end:1278930]] We do it because we _have to_ if we're going to talk about detecting entanglement.
[[start:1280070][end:1287666]] And most of you probably know the history of the notion of entanglement.

21:27 [[start:1287778][end:1296314]] It was first noticed by [Albert] Einstein, [Boris] Podolski, and [Nathan] Rosen--ever after called EPR [Einstein-Podolsky-Rosen]--in 1935.
[[start:1296512][end:1309390]] And they wrote a paper which is infamous, and called the EPR paper, in which they argued that the phenomenon of entanglement made no sense and couldn't possibly be physical.
[[start:1310050][end:1320100]] And since quantum theory included this notion of entanglement, it couldn't possibly be a complete theory of what's going on in the world.

21:59 [[start:1320710][end:1331570]] And [Erwin] Schroedinger replied the same year with a very detailed paper where he introduces, among other things, "Schroedinger's cat" as a paradox.
[[start:1332170][end:1338498]] And he explains very clearly what entanglement is, and why entanglement follows from quantum theory.
[[start:1338674][end:1347322]] And he uses that discussion to argue that the classical notion of a physical state is not actually applicable to the world as it is, so he answers the EPR paper very directly.

22:32 [[start:1352270][end:1373810]] And this discussion is currently mostly known as the Bohr-Einstein debate because of course [Niels] Bohr already in 1928 had said, in print, that the classical notion of causality in space and time simply doesn't apply anymore.
[[start:1374470][end:1377646]] And Einstein objected to that vigorously.

22:57 [[start:1377838][end:1385090]] But that was 1935. And it was almost 50 years later that entanglement was first observed in the laboratory.
[[start:1385170][end:1398060]] Here, the 1982 picture is a picture of the interior of Alain Aspect's laboratory when he performed the first entanglement experiment for which he finally won the Nobel Prize last year [2022].
[[start:1399790][end:1409310]] And these days this kind of experiment is done all over the world and is even done with satellite-borne sources.

23:32 [[start:1412710][end:1428440]] Resource[?] is the key to quantum-secured communication--as we'll discuss--in quantum cryptography and quantum banking and the quantum internet, all this other stuff that you may have heard of.

23:49 [[start:1429450][end:1440570]] So before talking more about these experiments, I just want to provide a definition of entanglement.
[[start:1442350][end:1446278]] "Entangled" simply means "not separable."
[[start:1446374][end:1447850]] That's the definition.
[[start:1448270][end:1459220]] So a state, a joint state "ab" is entangled if and only if it does not factor into two separable states.
[[start:1460310][end:1461426]] And that's it.
[[start:1461528][end:1462930]] That's the definition.

24:23 [[start:1463830][end:1484540]] And the literature, and especially the popular literature, is absolutely rife with hype and various kinds of mysterification of entanglement and authors trying to convince you that entanglement is this amazing kind of woo-woo thing.
[[start:1485310][end:1500670]] And whenever you run across that, go back to the definition. Entanglement simply means this simple mathematical condition of non-separability or a state that isn't factorizable.
[[start:1501170][end:1506346]] And that means that the state does not display classical conditional independence.

25:06 [[start:1506538][end:1509074]] So classically, that's the way to think about it; it's a failure of conditional independence.
[[start:1512230][end:1519650]] And it's ubiquitous in quantum theory, even though it wasn't actually observed for almost 50 years after it was predicted.
[[start:1521130][end:1524182]] So here's what all these experiments look like. [[See slide "Bell/EPR experiment (lab frame)"]]
[[start:1524236][end:1535406]] They're called "Bell/EPR experiments," after John Bell, who derived the statistical criterion for detecting entanglement; and EPR, Einstein, Podolski, and Rosen, who did this as a thought experiment and said, if this occurs in the theory, it can't possibly be real.
[[start:1544400][end:1545900]] And of course it is real.
[[start:1546270][end:1549390]] It's now amply demonstrated by experimentation.

25:50 [[start:1550050][end:1551022]] Here's how they work.
[[start:1551076][end:1552190]] There's a source.
[[start:1552930][end:1557562]] The source produces a state that is entangled.
[[start:1557706][end:1562050]] And I've written the typical... what's called a "Bell state."
[[start:1562200][end:1567906]] It's "up" plus-or-minus "down," divided by the square root of two just to normalize it.
[[start:1568088][end:1573350]] But up plus-or-minus down is clearly not the same as up times down.
[[start:1573420][end:1575720]] So this is not a separable state.

26:16 [[start:1576570][end:1586886]] And this state propagates outward in space and time to two observers who have independent laboratories, for example on different continents.
[[start:1586998][end:1602830]] In that space-based experiment that I showed you the picture of from the cover of Science a few years ago (2017, I think), the two observers have freedom to choose their own reference frame, their own Z axis for measuring spin.
[[start:1603170][end:1607550]] They do a spin measurement, and they do this over and over and over again.
[[start:1607620][end:1617598]] They accumulate statistics and they exchange their results so that they can analyze the joint statistics of their experiment.
[[start:1617774][end:1623938]] And they check to see whether that joint statistics is consistent with classical probability theory.
[[start:1624114][end:1634090]] And if it isn't, to a statistically significant level, then they've been able to detect entanglement.

27:14 [[start:1634910][end:1640086]] Now, notice that this process _requires_ classical communication.
[[start:1640278][end:1653550]] They have to make their independent measurements in their own laboratories, and then they have to exchange results, or one of them has to send results to the other one, or they both have to send their results to some third party.
[[start:1653890][end:1658962]] But in all of these cases, they're exchanging some classical data.
[[start:1659096][end:1669730]] And so we have the assumption that whoever gets that classical data knows the language it was recorded in and so can do a joint analysis.

27:50 [[start:1670410][end:1677062]] So I'll just show you another picture of this experiment that's in a standard space-time diagram here. [[See slide "How Bell/EPR works"]]
[[start:1677116][end:1679830]] Time is vertical, space is horizontal.
[[start:1681930][end:1684970]] The two observers are labeled Alice and Bob.
[[start:1686190][end:1691622]] They share a quantum channel that goes, from Alice, to the source, to Bob.
[[start:1691686][end:1693340]] That's the entangled state.
[[start:1694190][end:1696082]] They do some processing.

28:16 [[start:1696246][end:1701194]] And then one of them, here Bob, sends the results to Alice.
[[start:1701322][end:1703658]] And that's a classical communication.
[[start:1703754][end:1707600]] It takes time, and it traverses space.
[[start:1708470][end:1710910]] So this step is classical.
[[start:1711070][end:1719250]] So this is why we have to assume classical communication to talk about detecting or using entanglement.

28:40 [[start:1720470][end:1723640]] So now I want to represent this in a different way.
[[start:1725770][end:1728226]] Using our little picture earlier, we're going to think of Alice, again, as two components, A1 and A2.
[[start:1733070][end:1736890]] They're separable, so they have to communicate classically.
[[start:1737230][end:1743866]] They have a classical channel that goes through Bob, and they also now share some _quantum_ channel.
[[start:1743968][end:1746060]] They share an entangled state.

29:06 [[start:1746670][end:1749642]] And the entangled state, of course, is produced by _Bob._
[[start:1749706][end:1752030]] The _source_ is part of Bob.
[[start:1752450][end:1763060]] And their detectors, if you want to think about it that way, are located on this boundary B, or their interface with the source is on this boundary B.
[[start:1763830][end:1774760]] And each of them executes a process that accumulates data from the quantum channel and communicates it to the other observer via the classical channel.

29:36 [[start:1776010][end:1779842]] Now, this picture illustrates what's called a **LOCC protocol.**
[[start:1779986][end:1784250]] **LOCC** means "local operations and classical communication."
[[start:1784830][end:1789766]] So A1 and A2 are each operating locally on their boundary.
[[start:1789878][end:1800938]] They're making measurements locally on their boundary, and they're communicating via actions locally on their boundary and observations locally on their boundary.

30:01 [[start:1801034][end:1806526]] So, for example, I'm communicating with my computer here.
[[start:1806628][end:1808958]] We can consider it my boundary.
[[start:1809134][end:1823094]] And stuff is happening in the environment that's implemented by the Internet, and you're receiving those communications locally on your boundary, on your laptop or whatever it is you're using.
[[start:1823292][end:1826360]] So that's what local operations means.

30:26 [[start:1826890][end:1831890]] And these protocols specifically involve classical communication.
[[start:1831970][end:1834774]] And so they're able to detect entanglement.
[[start:1834902][end:1839370]] And a Bell/EPR experiment is just an example of a LOCC protocol.

30:40 [[start:1840670][end:1845974]] The observers exchange information about how they're going to do their experiments.
[[start:1846022][end:1848202]] They're both going to measure Z spin.
[[start:1848346][end:1855070]] They're going to use independently chosen reference frames, and they're going to look at the output from some agreed upon source.
[[start:1855970][end:1858480]] So that's all classically set up.
[[start:1858870][end:1864270]] Then they actually make their observations, and then they classically communicate their results.
[[start:1864350][end:1867620]] So classical communication, front and back. 

31:08 [[start:1868950][end:1877510]] LOCC protocols are not limited to this sort of Bell/EPR sort of setting.
[[start:1877930][end:1882630]] We can also represent a _scattering_ experiment as a LOCC protocol.
[[start:1884030][end:1889718]] So here's a representation of scattering as a LOCC protocol.
[[start:1889814][end:1900494]] And you can see all I've done is cut that previous boundary at the division between A1 and A2.
[[start:1900692][end:1914290]] And I've then _extended_ it in some external time, the time that is counted by Bob's clock, not by Alice's clock.
[[start:1914950][end:1917250]] That's what's meant by external.

31:57 [[start:1917910][end:1923718]] And I've relabeled Alice2 as Alice1 at a later time.
[[start:1923804][end:1936300]] So now what Alice is doing is communicating with her past self, or A1 is communicating with her future self, and they're each doing something different.
[[start:1937470][end:1944490]] A1 is executing a procedure that in the laboratory we call "state preparation."
[[start:1945470][end:1953450]] She's preparing a state that we'll call "in", which is just the initial state of some scattering experiment.

32:33 [[start:1953530][end:1965220]] So, for example, at the LHC [Large Hadron Collider], "in" is some state of two protons that are whirling around the ring at the LHC at close to the speed of light.
[[start:1966790][end:1975494]] And Alice then, later on, at t plus delta t, is doing a different kind of quantum process.
[[start:1975612][end:1986730]] She's analyzing the data coming out of something like the ATLAS detector, which is a multiparticle counter that's located at the LHC.
[[start:1987550][end:1997120]] So they share a quantum channel, which is the scattering channel that takes the incoming state and produces the outgoing state.

33:18 [[start:1997810][end:2017006]] And recall from the very first session, as [Richard] Feynman told us, to understand this transition from "in" to "out", we have to integrate over all possible paths that are consistent with conservation of spin helicity - basically, momentum plus spin--all the different spins that are relevant in a high energy physics experiment, including things like lepton number, which is basically a spin.

33:52 [[start:2032490][end:2033858]] Now, how do we know?
[[start:2033964][end:2036330]] How do we know what we have to conserve?
[[start:2036750][end:2048442]] We know what we have to conserve because Alice is doing the experiment has a classical memory that allows her to remember what she prepared.
[[start:2048586][end:2064770]] She can remember that what she did back in the past was set two protons counterrotating in the LHC, and they had certain energies, and so they had certain momenta, and they were protons, so they had certain spin variables.
[[start:2065510][end:2071670]] All of that has to be remembered to make any sense of the output of the detectors and so to actually come up with a measured state that _makes sense._
[[start:2080410][end:2087078]] And very often this memory channel is neglected by physicists.

34:47 [[start:2087174][end:2089980]] And I'm going to pause here and let Ander ask a question.

34:52 _Ander:_
[[start:2092110][end:2093078]] Thank you, Chris.
[[start:2093174][end:2102682]] So does this imply that every time you have a LOCC channel, the quantum part is a scattering picture, like a unitary evolution?
[[start:2102746][end:2109970]] Even in the earlier EPR picture, is that quantum channel portion always a unitary evolution scattering picture?
[[start:2110310][end:2111300]] Thank you.

35:14 _Chris:_
[[start:2114310][end:2127510]] Yes. For essentially the reason that defined a classical channel, you're always assuming you have something that's protected from decoherence by the environment.
[[start:2128250][end:2140730]] So, yeah. If you're doing an EPR experiment, you have to assume that you don't have any environmental decoherence between the source and the detectors.
[[start:2141630][end:2166740]] And similarly, when you're doing a scattering experiment, you have to make the assumption that the environment is not reaching in there and messing with the outgoing state that you're going to see, or reaching in and messing with the incoming state and changing it in some way that reprepares it in a way that you don't know, that you have no knowledge of.
[[start:2167190][end:2175640]] So, yes, you're making a fairly strong anti-decoherence assumption in any of these settings when you're talking about having a quantum channel.

36:18 [[start:2178090][end:2179720]] Does that answer the question?

36:20 _Ander:_
[[start:2180650][end:2181014]] Yes.
[[start:2181052][end:2181734]] Thank you.

36:21 _Chris:_
[[start:2181852][end:2182920]] Okay, great.

36:23 [[start:2183530][end:2198650]] So we can think of LOCC, we can think of scattering as LOCC. And I just wanted to now emphasize that effectively what LOCC is implementing is two parallel memories.
[[start:2202746][end:2209330]] A _classical_ memory, which, as we said in the case of scattering, is memory for preparation.
[[start:2209910][end:2219940]] In the EPR case, it's memory for preparation for what the experimental setup is, for what the instructions for doing the experiment are.

37:00 [[start:2220890][end:2227058]] And we also have a _quantum_ channel, which is effectively _another memory._
[[start:2227234][end:2230280]] It's something that's extended through time.
[[start:2230970][end:2237190]] And again, it's implemented by the environment, implemented by Bob, and it involves Bob's clock ticking.
[[start:2239550][end:2248110]] So whenever we have two memories in parallel, we can construct an **error correcting code.**

37:28 [[start:2248180][end:2251760]] So think of a simple classical error correcting code.
[[start:2252610][end:2258026]] For example, the use of parity bits in exchanging digital data.
[[start:2258148][end:2277190]] So if I send you a bit string classically, and I send it to you two or three times, so there's some redundancy in my signal, and I send you a parity bit, I say, okay, add up your bit string, and the result should be one.

37:57 [[start:2277340][end:2279160]] It's one on my side.
[[start:2279850][end:2283830]] If you add it up and you get zero, there's an error someplace.
[[start:2284270][end:2286806]] You can use that parity bit to detect errors.
[[start:2286838][end:2300666]] So you can throw out the bit strings that you receive that have parity of zero and say, oh, the environment interfered somehow with the signal, or some eavesdropper interfered with the signal,
[[start:2300698][end:2302462]] it made a mistake, or something like that.

38:22 [[start:2302516][end:2309294]] So this corresponds to environmental decoherence not being a good assumption.
[[start:2309422][end:2314180]] Even though it's classical, environmental interference is not a good assumption in this case.

38:35 [[start:2315510][end:2319666]] So a quantum error correcting code is basically the same idea.
[[start:2319768][end:2333690]] I use some feature of the fact that I have two different memories and that I'm encoding something in time.
[[start:2333840][end:2344940]] I'm encoding multiple replicates of something in time to provide a way of checking to make sure that I'm sending the correct message.

39:06 [[start:2346610][end:2361650]] So I can, for example, consider the message to be my classical memory, and consider the quantum process as a process that _tests_ that memory.
[[start:2362230][end:2367300]] So I remember that I need to do experiment X, and I will get result Y.
[[start:2367830][end:2374440]] I actually _do_ experiment X on this quantum channel and see if I get result Y.
[[start:2376010][end:2379320]] And if I don't get result Y, then something's wrong.
[[start:2380570][end:2389450]] Either I can't trust the quantum channel, or I've remembered my preparation conditions incorrectly.
[[start:2389790][end:2394220]] So I'm using one memory to check the accuracy of the other.

39:54 [[start:2394830][end:2411378]] And {this} using something about the environment, some channel in the environment, to check memory, is absolutely ubiquitous, and we use it all the time.
[[start:2411464][end:2421910]] So, for example, look around your room, and your room (hopefully) looks more or less the same now that it did at the start of this session.
[[start:2423050][end:2425830]] And that's very reassuring.
[[start:2426730][end:2434570]] It reassures you that something's not happening in the environment that's dangerous and disturbing.

40:35 [[start:2435150][end:2447870]] And if you couldn't do that, if your environment was constantly changing and there was no familiarity about the environment, you wouldn't be able to check your memory.
[[start:2448450][end:2449406]] You wouldn't be able to check your sanity.
[[start:2451410][end:2460494]] So even though we don't _think_ about our local environments as effectively an error correcting code, that's exactly how we use it.
[[start:2460532][end:2470180]] We use **stigmergic memory,** or memory out there in the environment, as a way of checking our own memories and assuring that our memory is okay.

41:13 [[start:2473180][end:2476650]] So I talked a little bit about **quantum security.**
[[start:2477420][end:2481064]] Here's how quantum security system works again.
[[start:2481102][end:2482520]] It's a LOCC protocol.
[[start:2483660][end:2498720]] We have some classical signal that can be thought of as a code or a key or a one-time pad, for example, that encodes a way of doing experiments.
[[start:2499380][end:2507890]] And once that's been exchanged, assuming it's secure, then we can use the quantum channel to communicate information.

41:48 [[start:2508500][end:2514308]] And the classical channel has told us what we have to _do_ with that quantum channel.
[[start:2514394][end:2521184]] We have to make certain kinds of measurements at, say, particular clock times as measured.
[[start:2521312][end:2529000]] And we'll get information sent from the past, from the sender.
[[start:2530060][end:2550130]] And the classical channel protects the quantum channel from adversarial agents, because anything that an adversarial agent does to the quantum channel, if some agent tries to eavesdrop, for example, on the quantum channel, they'll disrupt the quantum channel and the results of our measurement will not be what's expected given the protocol that we have run.

42:39 [[start:2559574][end:2571380]] So quantum communication is secured by the fact that interfering with some entangled state actually destroys the state - so it's detectable.
[[start:2572040][end:2580360]] We can always know if someone is trying to disrupt our communications, which isn't true if we just have two classical channels.
[[start:2581020][end:2584468]] Charlie can always intercept a message and then recreate it, and that's not possible with the quantum channel.

43:10 [[start:2590720][end:2600130]] So let's refold this diagram so that we've taken the external time back out of it.
[[start:2601300][end:2609712]] And we have this picture where the two components of Alice are just interacting via their shared boundary with their environment, Bob. And now we can see that the source of redundancy is not _time;_ it's the boundary itself.

43:39 [[start:2619320][end:2634940]] Just sharing the boundary allows Alice's components, A1 and A2, to put copies of the same information on different places on the boundary.
[[start:2635520][end:2640510]] So the boundary now becomes a resource for redundant storage of information.
[[start:2641360][end:2666740]] So Alice 1 and Alice 2 can use different parts of the boundary to check what other parts of the boundary say, to check the information that's encoded on other parts of the boundary. So they can define an error correcting code on the boundary itself using this LOCC protocol.

44:29 [[start:2669320][end:2710710]] So I just want to leave you with this idea: that using classical and quantum channels together allows us to define error correcting codes on boundaries that we share as separate agents, and leave you to think about what shared measurements, what shared quantum reference frames, let us as agents see the same things.

45:13 [[start:2713560][end:2718580]] And this is what we'll talk about next time. In September
[[start:2719400][end:2741980]] we'll talk specifically about how _space_ provides us with an error correcting code, and try to understand why space is treated as emergent from something else, basically from communication in most of quantum gravity.
[[start:2742400][end:2744270]] So thank you very much.
[[start:2744880][end:2752716]] I encourage you to use the interactive Q&A and to attend the discussion sessions, and we'll see you in September.
[[start:2752908][end:2753890]] Thank you.

45:57 _Daniel:_
[[start:2757940][end:2758690]] Awesome.
[[start:2760120][end:2763780]] Chris, thank you for the lecture.
[[start:2764280][end:2768950]] Ander, do you have any remarks or questions?

46:10 _Ander:_
[[start:2770040][end:2771750]] Not right now, thank you.

46:13 _Daniel:_
[[start:2773320][end:2778116]] I'll just ask a few quick questions. And if anyone has one, quickly, in the live chat!

46:18 [[start:2778228][end:2789224]] So, you mentioned the tick of the clock. And in Active Inference, we often hold up side by side both the discrete time models and the continuous time models.
[[start:2789272][end:2796460]] So do clocks have to tick discretely? Or, how do we think about continuous time modeling?

46:39 _Chris:_
[[start:2799700][end:2801036]] In this quantum setting they do have to tick discretely, because one has to be able to distinguish Alice's preparation of the qubits on her boundary from Bob's measurements of the qubits on the boundary.
[[start:2817640][end:2827130]] And this process can be extremely fast with respect to any kind of sense of macroscopic time.

47:09 [[start:2829260][end:2836060]] Your eyes are responding to photons in, I think it's hundreds of femtoseconds.
[[start:2837440][end:2853760]] So the discrete transitions that are effectively time measurements for you are, at that very fast molecular timescale, much, much faster than our typical clocks.
[[start:2855300][end:2865860]] Now, when we try to do very fast timing, we're constructing a faster clock than that, but it's a clock that we can only observe indirectly.

47:50 _Daniel:_
[[start:2870640][end:2871292]] Awesome.
[[start:2871426][end:2871916]] Okay.
[[start:2872018][end:2892390]] Now, this one maybe connects a little bit to application, but: With all the developments happening in theory, some of which you're reviewing here and also in practice with quantum computation, and then keeping in mind this distinction... {Sorry, I've lost you.} {Back?}

{48:17 _Chris:_
[[start:2897440][end:2898936]] I've lost you, Daniel.}

{48:19 _Daniel:_
[[start:2899048][end:2901388]] Okay, we'll wait till you're back.
[[start:2901554][end:2902460]] I can see you.}

{48:22 _Chris:_
[[start:2902530][end:2902908]] No.
[[start:2902994][end:2903724]] Okay.}

{48:23 [[start:2903922][end:2904364]] All right.
[[start:2904402][end:2905340]] Just repeat.}

48:26 _Daniel:_
{[[start:2906560][end:2906972]] Yeah.}
[[start:2907026][end:2937210]] So, given these rapid and ongoing developments in theory and practice related to quantum information science and quantum information security, how are people using this distinction of the classical stigmergic memory and then the quantum cognitive process to anticipate how to develop information systems that are reliable going forward?

49:01 _Chris:_
[[start:2941520][end:2954880]] I don't know of any instances in which thinking about quantum cognition has entered directly into any design of communication systems.
[[start:2955940][end:2961360]] The ability of humans to interact with these systems is just assumed.
[[start:2962500][end:2976928]] So it's just assumed that the user can interact with, say, a computer interface, which is the sort of interface that will be provided or is provided to any quantum computer.
[[start:2977114][end:2985770]] So if you think about a quantum computer, a practical quantum computer, it has classical interfaces, front and back.
[[start:2986700][end:2999196]] So in thinking about interacting with the computer, I'm giving it some classical problem statement, for example, and asking for some classical answer.

49:59 [[start:2999298][end:3003520]] And what it's going to give me is a probability distribution of classical answers.

50:04 [[start:3004500][end:3011520]] But I can, by running the calculation many times, make that probability distribution fairly tight.

50:16 [[start:3016130][end:3020340]] Yeah, I don't know of anyone talking about quantum BCIs [Brain-Computer Interfaces] at this point.
[[start:3021110][end:3022900]] It'd be an interesting question.

50:27 _Daniel:_
[[start:3027030][end:3036450]] Was it always understood, these sorts of blind spots and axioms associated with classical communication, was it developed as kind of like a proposal or like a special case and more unpacking was left for later?
[[start:3046928][end:3050730]] Or are these blind spots things that we're now coming into awareness of?
[[start:3050800][end:3054170]] Given what we're learning in the quantum information sciences?

50:55 _Chris:_
[[start:3055890][end:3058560]] I think we're learning how serious they are.

50:59 [[start:3059970][end:3064720]] But they were certainly recognized even by [Niels] Bohr in his 1928 paper [1928, The Quantum Postulate and the Recent Development of Atomic Theory, https://www.nature.com/articles/121580a0].
[[start:3065490][end:3070050]] And that's a very good paper, too.
[[start:3070200][end:3074194]] It's called the present state of quantum theory or something like that.
[[start:3074232][end:3079410]] And it's in Nature, and it's available on the web somewhere.
[[start:3081050][end:3082760]] I have a copy of it.

51:23 [[start:3083610][end:3098010]] But it was written, in a sense, as Bohr's summary of the 1927 Solvay Conference [Fifth Solvay Conference, Oct 24-29, 1927], which was the conference at which everyone doing quantum theory at that time got together to talk about their results.
[[start:3098990][end:3116566]] And in it, [Niels] Bohr essentially presents what came to be the Copenhagen interpretation, which I think is probably unfairly called an interpretation.

51:56 [[start:3116698][end:3122850]] It's sort of the Copenhagen pragmatic stance toward quantum theory.
[[start:3123670][end:3137320]] And essentially what Bohr says is that if we're going to do science, we have to assume that people can talk to each other.
[[start:3138650][end:3152010]] And if we're going to do science, we have to assume that there are instruments that we can manipulate and have reasonable confidence that we know what manipulation we've done.

52:32 [[start:3152080][end:3161200]] So if I turn a knob from one to two, I have to be reasonably confident that I'm making a particular change that I can understand.
[[start:3162690][end:3171170]] And we have to have reasonable confidence that different laboratories can replicate the same experiment.
[[start:3172390][end:3181560]] And if we think about any of those assumptions in purely quantum theoretic terms, then all sorts of questions are raised, right?

53:02 [[start:3182010][end:3184178]] Every quantum system is unique.
[[start:3184354][end:3188870]] We have the no-cloning theorem, so every scientific instrument is unique.

53:09 [[start:3189690][end:3194934]] So there's no such thing as exactly replicating an experiment.
[[start:3195062][end:3195740]] Right?
[[start:3196350][end:3202460]] That's a coarse-grained description of what I've done with a completely unique quantum system.
[[start:3202990][end:3207646]] And my brain, of course, is unique, and yours is too.
[[start:3207668][end:3209360]] And everyone else's is.

53:30 [[start:3210050][end:3217070]] So talking about us sharing a language is essentially a coarse-grained assumption.
[[start:3217910][end:3225710]] And what the Copenhagen stance is all about is coarse-graining yielding effective classicality.
[[start:3225870][end:3234840]] Or what that really means is coarse-graining yielding a description that we can use in the language that we understand?
[[start:3235770][end:3252250]] So these are very, very old issues that have been recognized for a long time, but I think in part because of the disaster of "shut up and calculate", they haven't really been talked about in the classroom.

54:14 _Daniel:_
[[start:3254990][end:3255546]] Awesome.
[[start:3255648][end:3258270]] I'll just read short questions from the chat.
[[start:3258930][end:3264190]] We can pass them to the discussion section, but there's a lot of great diverse questions.

54:24 _Chris:_
[[start:3264340][end:3267680]] So Alexi wrote, I think I've lost you again.
[[start:3268470][end:3270318]] The revenge of zoom.

54:30 _Daniel:_
[[start:3270494][end:3277570]] Well, we looked at the chart earlier where, like, Bob was talking to Alice, the unidirectional communication.

54:40 [[start:3280550][end:3281570]] Okay, okay.
[[start:3281720][end:3282978]] The unidirectional...
[[start:3283074][end:3285640]] The third party is recording it, I'm sure.
[[start:3286410][end:3298038]] Alexi wrote, regarding the environment being used for error correction, a symptom of derealization in psychological trauma breakdown, we don't recognize the environment around us and it's scary.

55:04 _Chris:_
[[start:3304350][end:3305340]] Makes sense.

55:05 _Daniel:_
[[start:3305810][end:3306750]] Makes sense.

55:06 _Chris:_
[[start:3306900][end:3307566]] All right.

55:07 _Daniel:_
[[start:3307668][end:3308778]] From Bala.
[[start:3308874][end:3309802]] Nice presentation.

55:09 [[start:3309866][end:3315994]] I heard Chris say entangled states are LOCC for a specific reference frame.
[[start:3316122][end:3321730]] Is this entanglement unitary or is it related to the numbers of degrees of freedom?

55:27 _Chris:_
[[start:3327320][end:3331270]] I think the quick answer would be both.
[[start:3332940][end:3339720]] If you have a complex system with many degrees of freedom, some can be entangled while others aren't.
[[start:3341500][end:3345500]] It depends on what parts of the state are separable.
[[start:3347040][end:3357500]] So again, entanglement is just a statement about components of a joint state that factor or don't.

55:59 [[start:3359700][end:3368000]] So you can have a joint state that looks separable along some dimensions, but... [inaudible] ...in other dimensions.
[[start:3368580][end:3377190]] The other big complication here is that whether a state looks entangled depends on the reference frames that you use to measure it with.
[[start:3378920][end:3388896]] And if you pick entangled reference frames, then what we ordinarily think of as separable entangled states become separable.

56:29 [[start:3389088][end:3391270]] So you can move entanglement around.

56:33 _Daniel:_
[[start:3393800][end:3394524]] Awesome.
[[start:3394682][end:3411360]] Okay, from Roland Rodriguez--is the discrete temporality only within the context of a given holographic screen interface, with time being bracketed otherwise beyond interface systems, is continuity or discretization kept agnostic?

56:54 _Chris:_
[[start:3414900][end:3419650]] I think if I understand the question correctly, it's yes.
[[start:3420840][end:3434280]] If I don't draw any boundaries, I just have the joint state, then the evolution is unitary and in a sense time plays no role.
[[start:3434940][end:3443720]] And if unitary evolution is perfectly time symmetric, so time actually drops out altogether.

57:25 [[start:3445840][end:3446204]] Awesome.
[[start:3446242][end:3448780]] So to talk about time, we have to draw boundaries.

57:29 _Daniel:_
[[start:3449280][end:3449740]] Awesome.
[[start:3449810][end:3452620]] Time must "have a stop", Huxley.
[[start:3453040][end:3466604]] And I'll ask one last question from the appropriately "monikered question quanderer"--all communication is abductive is a sentiment that I've been using to develop some arguments.

57:46 [[start:3466652][end:3468210]] Does that scan for you?
[[start:3469560][end:3474260]] How do we connect what we're discussing here with quantum to abductive logic?

57:57 _Chris:_
[[start:3477640][end:3482792]] Yeah, I could go along with that.
[[start:3482846][end:3484330]] I'd want a lot more detail.

58:06 [[start:3486860][end:3490564]] All communication is essentially analogical.
[[start:3490692][end:3491752]] I would agree with that.
[[start:3491806][end:3492410]] Yes.

58:13 _Daniel:_
[[start:3493900][end:3494840]] Andrew?

58:17 _Ander:_
[[start:3497440][end:3497852]] Yes.
[[start:3497906][end:3498670]] Thank you.
[[start:3499280][end:3503500]] So going back to the picture where the scattering picture.
[[start:3504320][end:3512716]] So we have so far, everything is topological, and certainly induces breaking the boundary in different sectors.
[[start:3512748][end:3516396]] I suppose it induces a topology on the boundary.

58:36 [[start:3516588][end:3521590]] Now, I had a couple of questions as for the geometry, and this might be getting ahead.

58:44 [[start:3524200][end:3529104]] Is it an emergent property of those channels between different boundary sectors?
[[start:3529232][end:3533850]] And if that's the case, then what does it mean to have a QRF or space?

58:57 _Chris:_
[[start:3537660][end:3548750]] Yeah, this is really the topic for September, but you do point out the fact that it's something of a chicken and egg situation.

59:11 [[start:3551040][end:3570980]] The way I think of it is, I suppose to choose the chicken side and think about what kind of reference frame does the agent have to implement to see space on their boundary.
[[start:3572040][end:3576468]] And the reason I think about it that way is that's a question I want to be able to ask about biological systems.
[[start:3579520][end:3584760]] And this actually gets into probably what won't be talked about until October.
[[start:3585420][end:3610560]] But I want to be able to ask essentially a phylogenetic question of what sorts of organisms, where in the lineage from LUCA, do we find systems that are able to assign spatial coordinates to their boundaries and what coordinates come first?

1:00:10 [[start:3610710][end:3647630]] And I suspect that sort of discrete location names with no metric come first that a system can talk about, for example, this part of their membrane versus that part of their membrane without even having any ability to say, how far apart they are and that some sort of metric representation of this angular space comes later and that a radial space comes even later than that.
[[start:3648080][end:3649928]] That's, at this point, speculation.
[[start:3650024][end:3662400]] But I think these are questions that we can end up asking given the right kind of formalism and the right understanding of what it means to be able to make a spatial measurement.

1:01:03 _Ander:_
[[start:3663220][end:3670452]] So the conjecture is that the metric would emerge from a discrete network metric of counting ticks sort of thing.

1:01:10 _Chris:_
[[start:3670506][end:3673236]] Yeah, I think that's correct.

1:01:13 [[start:3673338][end:3682396]] And the sort of symmetries of space that we see are very much tied up with object identity.
[[start:3682528][end:3696080]] So if we think about something like rotational symmetry let's see, I should stop screen sharing.

1:01:38 [[start:3698680][end:3707300]] So I've got this object, right, and I can do this, and I say, oh, space has this rotational symmetry.
[[start:3708040][end:3712744]] But for me to say that, I have to recognize that this is the same object, right?
[[start:3712862][end:3720010]] I have to implement object persistence, which we all learn to do when we're nine months old or something.
[[start:3720880][end:3742480]] But we tend to regard those as separate things as we learn object persistence, because space is rotationally symmetric, but we can view it the other way around, that space is rotationally symmetric for me because I implement these constraints that are called object persistence.

1:02:25 _Daniel:_
[[start:3745060][end:3761240]] Do you think we can understand phylogenetics as a whole, as a kind of scattering experiment, like the high energy LUCA event and then dissipating and propagating in a very tangled bank?

1:02:42 _Chris:_
[[start:3762780][end:3773388]] Well, I do want to be able to understand phylogeny in exactly the same terms as embryology, and Mike Levin and I have published papers about that.
[[start:3773474][end:3782030]] We should be able to view the lineage of LUCA in exactly the same way that we view the lineage of the zygote that produced us.

1:03:03 _Ander:_
[[start:3783220][end:3795330]] So that's why it's no coincidence that during pregnancy, the development of the embryo mirrors evolution in terms of the parts that are developed first.

1:03:16 _Chris:_
[[start:3796840][end:3810810]] Yeah, this is the old idea that phylogeny and ontogeny are related in some way, which, from an embryonic development point of view, they're certainly analogous in ways.

1:03:33 _Ander:_
[[start:3813340][end:3819700]] Sorry, if I may ask one last question--should be very quick--regarding the weak rotation.
[[start:3819780][end:3828590]] I'm still a bit unsure how it ties to this diagrammatic notation that we had with quantum channels on show so on.

1:03:51 [[start:3831760][end:3840240]] In the second session, we briefly talked about the weak rotation being a reversal in the direction of time.
[[start:3840310][end:3842960]] Is there any relation to today's session?

1:04:05 _Chris:_
[[start:3845880][end:3862388]] Yeah, whenever we think about the flow of time as driven by the input-output cycle, the input-output cycle for agents separated by a boundary, there's always a sign change.
[[start:3869182][end:3869560]] Right.
[[start:3869630][end:3872460]] My input is your output, and vice versa.
[[start:3873200][end:3899540]] So when we think about Bob's clock ticking, when Alice does something, his direction of time, in a sense, points with respect to the boundary opposite to hers, but that's only with respect to the boundary.

1:05:00 [[start:3900600][end:3905270]] He sees information flowing in, and she sees information flowing in.

1:05:07 [[start:3907160][end:3912980]] That's the only point being made here about the Wick rotation as an operation.

1:05:14 _Ander:_
[[start:3914600][end:3915590]] Thank you.

1:05:16 _Daniel:_
[[start:3916600][end:3917940]] Thank you, Chris.
[[start:3918520][end:3922668]] Very well appreciated by the viewers and by us.

1:05:22 [[start:3922754][end:3935112]] So we'll certainly look forward to reviewing the Q&A, and everybody is welcome and encouraged to join for the participatory discussion in about two weeks on Saturday.
[[start:3935256][end:3938270]] So till next time.

1:05:38 _Chris:_
[[start:3938880][end:3940300]] All right, thank you.
[[start:3940450][end:3940680]] Cheers.
