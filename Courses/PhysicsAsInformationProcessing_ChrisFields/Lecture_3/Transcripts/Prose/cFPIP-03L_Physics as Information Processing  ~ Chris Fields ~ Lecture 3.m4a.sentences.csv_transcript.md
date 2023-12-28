---
title:  'Physics as Information Processing - Lecture 3, "Quantum Reference Frames"'
author:
- 'Chris Fields (Allen Discovery Center at Tufts University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-4812-0744)'
- 'Ander Aguirre (Ohio State University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-6337-8292)'
- 'Daniel Friedman (Active Inference Institute; University of California, Davis) [![Orcid](images/orcid.png)](https://orcid.org/0000-0001-6232-9096)'
date: "2023-07-13 Version 1.0"
...

## Lecture 3, "Quantum Reference Frames"

00:06 _Daniel:_
[[start:6930][end:8462]] Hello and welcome everyone.
[[start:8596][end:11230]] It's July 13, 2023.
[[start:11380][end:17818]] We're here in physics as information processing with the third lecture by Chris Fields.
[[start:17914][end:31474]] So please check out the course website, Coda Document, where you can submit questions, check out the recordings and descriptions of all sessions, and register if you want to participate in one of the discussion sections.

00:31 [[start:31602][end:34600]] So thank you again, Chris, to you.

00:36 _Chris:_
[[start:36410][end:44330]] Thank you and welcome to Physics as Information Processing, session Three, which is about quantum reference frames.
[[start:45470][end:67490]] So in this course, we've talked about quantum information theory, which we characterized as a general theory that describes the exchange of information, exchange of finite information between two finite agents that are separated by some boundary.
[[start:67830][end:77330]] And we emphasize that this is a topological theory, not a geometric theory, so it makes no assumptions about an embedding spacetime.
[[start:79050][end:110830]] And last time we showed how to characterize this boundary of script B as an array of N, some finite N quantum bits or qubits, and how to characterize the interaction of the agents A and B with the boundary as an alternating cycle of preparing and measuring the qubits in this array.

01:51 [[start:111410][end:120130]] And we showed that their interaction could be represented as a sum of operators, each of which act on just one of the qubits.
[[start:121350][end:136038]] And we also talked about the need for each of the agents A and B to choose a reference frame for their interaction with the qubits that defined which way was up.
[[start:136204][end:162590]] So what the orientations of the qubits meant and emphasized that the two observers A and B could choose different reference frames, so different ways of measuring and preparing their qubits that use different meanings for the idea of up for each qubit.
[[start:163570][end:179490]] And we ended the last session with a pointer forward toward the quantum formulation of the free energy principle, which can be stated as the claim that interacting systems behave in a way that aligns their reference frames.

03:00 [[start:180490][end:199014]] And pointed out at that time that what this means is that the two agents A and B approach entanglement asymptotically, and that therefore the FEP is a classical limit of the principle of unitarity, which is the core principle of quantum theory.

03:19 [[start:199062][end:202540]] So we'll see in this session why this is true.
[[start:204130][end:221330]] So what we'll talk about today is what reference frames are in general, how they make observations and actions meaningful, so how they give physics a semantics, and then we'll talk about the free energy principle.

03:43 [[start:223510][end:225650]] So what is a reference frame?
[[start:226550][end:241160]] The idea that physics involves reference frames goes back at least to Galileo, but was probably familiar well before that, just not formalized in the way that Galileo formalized it.

04:02 [[start:242270][end:247050]] So the key idea can be thought of in terms of motion.
[[start:247550][end:259738]] And you're all familiar, for example, with riding a bicycle or driving a car and seeing the world as if it's passing by you at some velocity, with some velocity.
[[start:259914][end:264830]] And of course, with respect to the world you're passing by it with some velocity.

04:25 [[start:265810][end:280802]] And this idea that velocity is not absolute but that's relative to some observer who measures it in some reference frame is the foundation for theories of relativity.
[[start:280866][end:298410]] So Galileo developed his theory of relativity which basically was just a way of converting from classical velocities measured by one observer to classical velocities measured by another observer that was moving with respect to the first one.
[[start:298560][end:317490]] And this provided the foundation for Einstein's theories of relativity which modified Galileo's by adding the concept that the observers have to exchange information and can only exchange it at the speed of light which is finite.

05:19 [[start:319990][end:324660]] So this idea in physics has a long history.
[[start:325110][end:332040]] Of course, the core idea is that measurements are always with respect to something or other.
[[start:332490][end:338870]] And the something or other is a reference frame and different agents can choose different reference frames.
[[start:339290][end:341494]] And this idea is very old.
[[start:341612][end:350170]] Here we have a picture of Anubis choosing a feather as the reference frame with which to measure the heart of the pharaoh.

05:50 [[start:350590][end:354906]] So this goes back to well before the common era.
[[start:354938][end:357950]] This is about 2000 BCE.
[[start:358370][end:387750]] So this is a very old idea that's been elaborated over the centuries as science has developed and in the 90s a fairly big change in how this idea was thought about occurred. In classical physics reference frames were always thought of as mathematical abstractions and an observer and a reference frame were more or less identified by Galileo...

06:28 [[start:388250][end:403210]] ...and that identification is carried forward into Einstein who thinks about observers, for example, sitting on photons and observers in spaceships and observers riding on railroad trains and this sort of thing...
[[start:403280][end:408720]] ...and always that just means, think of a reference frame that's doing something or other.

06:49 [[start:409570][end:433350]] So a reference frame in classical physics is essentially just a coordinate system and these abstract coordinate systems can be employed in thought experiments and so they are a way to illustrate classical intuitions about motion.
[[start:434490][end:447002]] And in the 90s, as quantum information theory developed it was realized that a reference frame actually consists of a physical object.
[[start:447136][end:454250]] I mean, even in the picture from the Egyptian tomb the reference frame is a physical feather.

07:35 [[start:455490][end:462554]] And that means that the reference frame itself is described by quantum theory.
[[start:462602][end:464560]] It's some quantum system.

07:45 [[start:465810][end:486950]] And if you think about reference frames that are familiar for example, meter sticks for measuring distance or clocks for measuring time or gyroscopes or batteries or even the Earth's gravitational fields which typically defines up for us; those are all physical objects that can be described by quantum theory.
[[start:487770][end:500490]] Well, this was an important insight because it led to the realization that reference frames as quantum systems are unique.
[[start:501550][end:505200]] And uniqueness in quantum theory is very strong.
[[start:506610][end:514080]] There's the no-cloning theorem which states that you can't reproduce, exactly reproduce, any unknown quantum state.

08:35 [[start:515730][end:523074]] And that applies to reference frames because they encode what Bartlett et al.

08:43 [[start:523112][end:533270]] ...in that paper called nonfungible information which just means information that can't be completely represented in any finite bit string.
[[start:534010][end:538520]] So unless you know the state of a reference frame, you can't clone it.
[[start:539290][end:555946]] Since these reference frames encode more than any bit string's worth of information in their quantum phases, they're unique and their states are unknown.
[[start:556138][end:567726]] And the consequence of this is that if Alice wants Bob to use her reference frame to make a measurement, she can't just send him a description.
[[start:567918][end:571410]] She has to actually send the reference frame.

09:32 [[start:572390][end:591350]] And this has an important consequence for physics because it makes all replicate measurements approximate because observers obviously aren't using exactly the same physical objects as their reference frames.

09:51 [[start:591790][end:605630]] But there's a deeper implication of this, which is that Alice's ultimate rock bottom reference frame is actually implemented by her body, by her brain.
[[start:606690][end:618426]] And using any external reference frame requires having this internal reference frame that makes the external reference frame meaningful and usable.
[[start:618538][end:623902]] So, for example, this thing is a piece of a meter stick, a third of a meter stick.
[[start:624046][end:630790]] But for me to use it to make measurements, I have to actually have some concept of distance.

10:31 [[start:631130][end:635400]] And that concept of distance is implemented by my nervous system.
[[start:636170][end:641990]] And that implementation is my reference frame for length.
[[start:642830][end:648598]] And it's what gives meaning to any external measurement of length.
[[start:648774][end:659600]] It's what makes my measurements of length actionable by me using my effectors or action capabilities, whatever they are.

11:00 [[start:660210][end:667730]] So my internal reference frames are what make information I get from the world actionable.

11:08 [[start:668230][end:675694]] And in Bateson's sense of differences that make a difference, actionability is the core of semantics.
[[start:675822][end:679720]] Something is meaningful if I can do something about it.
[[start:680090][end:693990]] So this idea that we all contain embodied reference frames gives physics a semantics by giving observers a semantics.
[[start:694150][end:695580]] And this is new.
[[start:696590][end:706030]] This is an idea that never really appeared in physics before that measurements automatically had to have some kind of semantics.

11:46 [[start:706610][end:711550]] But reference frames give semantics to measurements.

11:53 [[start:713730][end:717410]] So here's an example of an embodied reference frame.
[[start:717990][end:723266]] This is the reference frame that bacteria use for chemotaxis, i.

12:03 [[start:723288][end:723522]] e,
[[start:723576][end:733830]] ...to move toward molecules in the environment that they like, like sugars and to move away from molecules that they don't like, like acids.
[[start:734250][end:739142]] And it's been worked out in great detail over decades of experimental work.

12:19 [[start:739196][end:741190]] And this is a rough schematic.
[[start:742350][end:745130]] The reference frame has three parts.
[[start:746590][end:753530]] There's the measurement part, which is conveniently located in the front of the bacterium.
[[start:754050][end:757950]] And it consists of a bunch of receptors that probe the environment.
[[start:758450][end:764346]] And they can bind molecules, which are called ligands, out in the environment.

12:44 [[start:764538][end:770250]] And when they bind them, they send a signal into the back of the bacterium.
[[start:770330][end:783830]] And it turns out that there's a little miniature reference frame attached directly to these ligands which is this R and B system which control the ligands--not the ligands--the receptor sensitivity.

13:04 [[start:784890][end:800170]] Then the back of the reference frame is the action component and it consists of a set of molecules that control a motor--a molecular motor--that drives the flagella on the bacteria.
[[start:800830][end:807390]] And the flagellum allows it to swim forwards or turn in some other direction.
[[start:808050][end:816640]] And depending on how it spins, the creature either goes in the direction of something it likes or it stops and turns around.

13:37 [[start:817430][end:832760]] And the stuff in the middle is a little molecular feedback loop that represents the amount of ligand in the environment that the bacterium expects to see.
[[start:833130][end:842410]] So this is the middle of the reference frame and it defines the default value for what the bacterium is observing in its environment.
[[start:843150][end:859760]] And if you're thinking in terms of the free energy principle or Bayesian inference, then you'll immediately see the concentration of this molecule is encoding a prior probability, the bacterium's prior probability for what its environment is like.

14:20 [[start:860450][end:871300]] And the zero point, the default value of that encoding, is the ligand concentration in which the bacterium does nothing.
[[start:872310][end:890710]] So a QRF in general can be characterized as an expected value, which is here the concentration of this molecule pY phosphorylated plus a bunch of computation, which is all the rest of the things in this diagram.

14:51 [[start:891950][end:897130]] So this is a very simple QRF that's embodied by a bacteria.
[[start:897470][end:908670]] Here's a more complicated QRF that's embodied by eukaryotic cells, or more complicated cells like our cells.
[[start:909170][end:917070]] And this is the reference frame that makes decisions about whether cells are going to divide.
[[start:918150][end:932790]] So on the top you see the cell's membrane, and there are all sorts of receptors sticking out of it that detect hormones and neurotransmitters and growth factors and this, that, and the other thing, many of which are produced by other cells.

15:33 [[start:933610][end:955710]] And those receptors communicate via a lot of chemistry with the nucleus, which is contained in another membrane and so serves as, in a sense, the outside upon which the reference frame is acting.

15:56 [[start:956130][end:963770]] And what this reference frame does is control the transcription of large numbers of molecules from DNA.
[[start:963850][end:967586]] So it basically controls what proteins the cell is making.
[[start:967768][end:974530]] And those proteins end up doing something like restructuring the cytoplasm and actually driving cell division.
[[start:975190][end:987030]] And the stuff in the middle of this reference frame, which I've labeled the integrative center, are three molecules called RAF, mech and ERC.
[[start:987450][end:993450]] And they're connected by positive bi-directional feedback loops.

16:33 [[start:993950][end:1004300]] And they basically negotiate the default value of the environment at which the cell does nothing.
[[start:1005330][end:1014970]] So they're the middle of the reference frame that represents the cell's expectation values about what's going on in its environment.
[[start:1015130][end:1020754]] So you can imagine now what reference frames encoded by our nervous system look like.
[[start:1020792][end:1035350]] They're extremely complicated and exist at multiple scales, from the scale of molecules in cells to the scale of large scale connections between parts of our brains.

17:17 [[start:1037370][end:1039960]] So how do we represent all this stuff?
[[start:1041050][end:1047020]] There are many ways to do this, but this is a particularly simple way.
[[start:1048350][end:1068370]] It assumes that whatever's in the middle, which is here called C prime, is the most general thing that the inputs can give information to and the most general thing that can give information to the outputs.

17:49 [[start:1069030][end:1086070]] And most general here has a category-theoretic definition so it can be stated in a way that's equivalent across many different specific mathematical forms.
[[start:1086570][end:1095158]] But if you're familiar with neural networks, this will look to you a lot like the skeleton of a variational autoencoder.

18:15 [[start:1095334][end:1097660]] And that's basically what it is.
[[start:1098910][end:1121620]] And I don't want to deal with this formalism except to say that it exists and is very convenient, except to say that we can attach this kind of formal diagram as a representation of a QRF to our representation of the boundary between two interacting agents.
[[start:1122550][end:1134070]] And we can use these formal structures to drive the measurement operators that actually implement physical changes on this boundary.

18:55 [[start:1135530][end:1146646]] And I'll represent this whole business with just a triangle labeled Q for some QRF that's attached to the boundary.
[[start:1146838][end:1160830]] And we can use this simple notation then to investigate what sorts of structures one gets when one starts to think about systems as implementing specific QRFs.

19:22 [[start:1162290][end:1169970]] And here's the structure of the minimal system that we can really think of as an interesting observer.
[[start:1170870][end:1201078]] And this is a system that has some QRF that I've called E that looks at its environment, the part of its environment that it can actually observe and act on, and it defines a sector of the boundary which mathematically is just the image of this QRF-E that the system can manipulate.

20:01 [[start:1201174][end:1208560]] So this is the part of the environment or the part of the boundary that the system actually sees and can do something about.
[[start:1209890][end:1227380]] And for this observer to be interesting, it needs to be able to detect the difference between what it sees now and what it saw just then so that it can decide whether to take some action or other.
[[start:1227750][end:1236802]] So it needs a memory and that requires another QRF that has some allocated piece of the boundary. Recall...

20:36 [[start:1236866][end:1244570]] ...the boundary is where classical information gets written in this purely quantum theoretic formalism.
[[start:1245870][end:1250620]] So it needs a memory sector that that QRF can act on.
[[start:1251470][end:1266000]] And then in order to do this computation and specifically in order to write information to the boundary--in order to actually flip bits on the boundary--it needs free energy.

21:06 [[start:1266630][end:1279890]] So the rest of its boundary gets devoted to extracting free energy from the environment and exhausting free energy, waste heat, in other words, into the environment.
[[start:1280050][end:1284600]] And so it has this nice little thermodynamic cycle that drives everything else.

21:25 [[start:1285770][end:1304800]] And finally, in order to tell now from just a second ago the information in memory, it needs a clock that marks the information in memory as not current, so as past information.
[[start:1305730][end:1318900]] And if it can store multiple memory records, it needs to be able to count and say this piece of remembered information is actually more recent than that piece over there.
[[start:1319510][end:1327490]] So it has to implement a little internal clock, and that clock is its internal time QRF.

22:07 [[start:1327830][end:1331058]] And we've seen that QRFs act on boundaries.
[[start:1331154][end:1335320]] This clock acts on a boundary, but it doesn't act on B.

22:15 [[start:1335690][end:1353050]] It acts on an internal boundary that's essentially the boundary between it the clock and the points at the ends of these QRFs that actually encode information that's either read from the environment or written to the environment.
[[start:1354050][end:1372130]] So already this minimal observer has a little bit of hierarchical structure, which is that its clock has to, in some sense, be higher up in the hierarchy than the parts, the QRFs that interact directly with the environment.
[[start:1373590][end:1384950]] So if you have a structure like this, you face a metabolic trade off for a fixed amount of energy that you can extract from the environment.
[[start:1385290][end:1393740]] You can allocate it either into learning more about the environment or remembering more about what you learned before.

23:16 [[start:1396510][end:1402170]] So any system has to make this decision about how they're going to use energy.
[[start:1402240][end:1405758]] Are they going to devote it to learning more or remembering more.
[[start:1405924][end:1409050]] And your laptop makes that decision.
[[start:1409210][end:1411390]] Memory is cheap for your laptop.
[[start:1412050][end:1413770]] Your brain makes that decision.

23:33 [[start:1413850][end:1416390]] Memory is much more expensive for your brain.
[[start:1416570][end:1419102]] And all cells have to make that decision.
[[start:1419246][end:1426142]] And the universal solution to this trade off is coarse graining memory...
[[start:1426286][end:1426882]] ...i.e.,
[[start:1426936][end:1430878]] ...remembering things in less detail than you saw them in the beginning.

23:51 [[start:1431054][end:1432710]] Ander, you have a comment?

23:53 _Ander:_
[[start:1433530][end:1434278]] Yes.
[[start:1434444][end:1437074]] I wanted to ask a question now before it gets too late.
[[start:1437122][end:1452630]] So two or three slides ago, when we were looking at the diagram of the co-cone diagrams, I was wondering if the classifiers identified with measurement and preparation...
[[start:1452710][end:1466602]] ...those correspond to sensory and action degrees of freedom in the earlier picture with the bacteria and the classifier in the middle in that picture, would it correspond to the default chemical concentration?

24:26 _Chris:_
[[start:1466746][end:1468480]] That yes, exactly.

24:29 _Ander:_
[[start:1469010][end:1470586]] Okay, perfect.

24:30 _Chris:_
[[start:1470708][end:1471380]] Yeah.

24:34 [[start:1474150][end:1478770]] That crossing point in the middle is specifically where the default is encoded.
[[start:1479930][end:1482360]] Thank you for pointing that out.

24:45 [[start:1485230][end:1491020]] Okay, so let's follow the consequences of this metabolic issue.

24:53 [[start:1493150][end:1508586]] If you have a system that's a little bit smarter than our minimal system that can actually detect and measure the states of objects, it has to do even more work because it has to encode even more QRFs.
[[start:1508778][end:1514686]] So think of measuring the state of some object like a volt meter in a laboratory.
[[start:1514878][end:1522710]] If I tell you to go into the lab and tell me what the voltmeter is reading, then the first thing you have to do is find the voltmeter.
[[start:1523050][end:1532170]] And your process of finding the voltmeter is independent of your process of reading what it's actually saying on its dial.

25:33 [[start:1533150][end:1545840]] So in order to measure the state of an object, you have to have two QRFs one that lets you find the object, and then the other that lets you measure the state of interest of the object.

25:46 [[start:1546370][end:1562820]] And we call these the R sector for reference that lets you find the object and the P sector for pointer because old instruments used to have pointers on dials that read analog numbers.

26:06 [[start:1566830][end:1596898]] But what thinking about object identification tells you is that every object that you can identify leads to having to sector both the informative part of your boundary and the memory part of your boundary into two new sectors one to store information about object identification and one to store information about the states of those objects.

26:37 [[start:1597074][end:1600310]] So this requires much more metabolism.
[[start:1601210][end:1605234]] And again, the solution is coarse grained.
[[start:1605362][end:1610970]] Typically, what we coarse grain is our memory of the object that we've identified.
[[start:1612750][end:1616250]] So what does this do to systems?

26:59 [[start:1619070][end:1628240]] Because making measurements costs energy and recording memories costs energy...
[[start:1629330][end:1635586]] ...we have to make decisions about what QRFs to use at what time.
[[start:1635688][end:1645250]] Given our finite energy budgets, we can't look at the world with all of our measurement capabilities at the same time because it's too expensive.
[[start:1646410][end:1675546]] And now we see the effect of a theorem in quantum information theory which is that if two QRFs can't be deployed simultaneously for whatever reason that corresponds to them not commuting as operators and if they don't commute as operators, they have to be implemented by compartments that are separable.

27:55 [[start:1675658][end:1678990]] So compartments that only communicate classically.

28:00 [[start:1680690][end:1702098]] The consequence of this theorem is that as soon as one has too many sensory and motor capabilities to run all at the same time, given your energy budget you end up being compartmentalized into compartments that only communicate classically.
[[start:1702194][end:1718250]] So you end up looking like this diagram where there are a bunch of components that do sensory motor loops or memory, one or the other and they can only communicate classically.
[[start:1718670][end:1731280]] And they're controlled by some sort of attention system that selects which ones to activate depending on the amount of free energy that's available.
[[start:1732390][end:1738500]] And clearly, this clock function becomes part of this control system.

28:59 [[start:1739350][end:1765980]] So, the physics alone of any system that's acting as, that executes a fairly complicated interaction with its environment gives us this hierarchical compartmentalized structure without having to add any biological or cognitive science type assumptions at all.

29:27 [[start:1767710][end:1770300]] So we can go in three directions from this.
[[start:1771390][end:1775150]] We can go deeper into the biology which we're going to do in October.
[[start:1775490][end:1787220]] We can go deeper into the physics which we're going to do in August and September and we can go deeper into this issue of alignment which is what we're going to do today.
[[start:1788630][end:1790430]] So there are four possibilities.
[[start:1790590][end:1800870]] If you think about two agents that have QRFs that are interacting across this boundary and the first one is trivial.

30:01 [[start:1801450][end:1814934]] If the B agent, the agent on the right side, doesn't actually employ any QRFs if it just interacts with the boundary thermally, then there is no alignment.
[[start:1814982][end:1820380]] You're in a trivial situation where A can measure something about B, but not in return.
[[start:1822370][end:1839860]] If the B agent deploys a QRF that's much broader in scope than the A agent what we show here in panel B, then the A agent can learn something about the B agent but misses most of what the B agent is doing.
[[start:1841750][end:1850962]] In panel C, we have agents with QRFs of the same size on the boundary, but they're not lined up correctly.
[[start:1851026][end:1854440]] So each one misses part of what the other is doing.

30:55 [[start:1855210][end:1863162]] And finally, indeed, we have the optimal situation where they have QRFs of the same size and they're actually lined up.

31:03 [[start:1863296][end:1868890]] So each sees what the other is doing, at least on this sector of the boundary.
[[start:1869230][end:1881370]] And since the agents have to allocate some of the boundary to free energy supply and can't look at that part, then they can't tell what's happening across their entire boundaries.
[[start:1881450][end:1887730]] They can only tell what's happening in this sector where they can actually deploy a QRF.
[[start:1888790][end:1899160]] But let's now look at this interesting situation, situation D, where the QRFs are aligned between A and B.

31:40 [[start:1900890][end:1904600]] As I said, that's the optimal channel for A and B.
[[start:1905770][end:1935506]] And if we think about this, we can write the variational free energy or the uncertainty or the prediction error for A for the QRF X as the action that it sees, i.e., B's action, the difference between that and what it expects B to do.

32:15 [[start:1935688][end:1938930]] So what it can predict about B's action.
[[start:1939350][end:1971920]] And this is just the notion of free energy from the free energy principle, except translated into this situation where we have two QRFs and A can measure what B has done, but it can also use its QRF to predict, because it's predicting the very state that it's going to observe next of the same sector that B is using.
[[start:1973410][end:1991140]] Now, if we look at this diagram, we can see easily that the way to minimize the variational free energy and therefore maximize predictive capability is for these two QRFs to actually be the same.

33:12 [[start:1992150][end:2008700]] So if A is doing the same thing to the boundary that B is, A can predict B's next action perfectly because B is going to do whatever A is doing.

33:31 [[start:2011310][end:2029070]] So what the free energy principle tells us in this case is that A and B, as they minimize their variational free energies, will approach having identical QRFs.
[[start:2030210][end:2040210]] Well, again, we have a theorem that tells us that if these QRFs are shared, A and B are not separable but entangled.
[[start:2041110][end:2047190]] And this is also fairly easy to see because it depends on this notion of nonfungibility.
[[start:2048570][end:2055480]] If XA and XB both encode nonfungible information, which is quantum systems, they do...
[[start:2056730][end:2066540]] ..their states aren't clonable, so they can't be copies of each other because one can't clone an unknown system.

34:27 [[start:2067630][end:2072430]] So they can only be identical if they're actually identical systems.

34:32 [[start:2072930][end:2084850]] This is exactly the same point made earlier about Alice having to actually send her QRF to Bob if she wants Bob to use her QRF.
[[start:2086550][end:2094050]] So minimizing VFE for quantum systems is becoming entangled.
[[start:2095050][end:2103538]] So the classical free energy principle, which tells us to minimize VFE actually drives quantum systems toward entanglement.
[[start:2103714][end:2115450]] And that's why it's a special case of the principle of unitarity which just says that any isolated joint system is going to asymptotically approach entanglement.

35:17 [[start:2117150][end:2127360]] So this raises an obvious question, which is why all of us aren't entangled with our environments all the time and entangled with each other?
[[start:2128530][end:2135170]] And the answer is that entanglement is really hard for complex systems.

35:35 [[start:2135990][end:2144500]] And this illustrates the sense in which the FEP is moving systems in two different directions at once.
[[start:2145370][end:2154790]] The FEP is driving systems to maintain their separability but it's also driving systems toward entanglement.
[[start:2155450][end:2163690]] And as the system becomes more and more complex the difference between those two outcomes becomes larger and larger.

36:04 [[start:2164350][end:2177390]] So recall from last time that the condition for separability is that the two systems have dimensions that are much larger than the dimension of their boundary.
[[start:2178370][end:2186770]] And this is the condition that allows them to have internal states, to have them have states that aren't located on their boundaries.
[[start:2187350][end:2193540]] And clearly, to formulate the free energy principle you have to have internal states.
[[start:2194810][end:2205510]] So if you do a complex QRF that's in a lot of computation then you need a lot of internal degrees of freedom to implement that computation.

36:45 [[start:2205850][end:2208362]] So you need a lot of internal state.

36:48 [[start:2208496][end:2211130]] So you have to have large dimensions.
[[start:2212030][end:2216090]] So complexity favors separability.
[[start:2216430][end:2221710]] As a system becomes more complex, it has to have more internal states.
[[start:2221860][end:2226720]] So it has to be, in a sense, more separable from whatever it's interacting with.
[[start:2227730][end:2230110]] Now, think about this classically.

37:10 [[start:2230850][end:2255350]] If you have a complex system that's doing a lot of computation then it requires a lot of free energy and it has to dissipate a lot of entropy in the form of heat, typically, but something, some form of energy transfer that its environment is going to see as noise, as not informative.
[[start:2256650][end:2263340]] So a complex system is working very hard to predict its environment's next state.
[[start:2264110][end:2269286]] But by working very hard it's dumping a lot of entropy into its environment.

37:49 [[start:2269478][end:2276730]] And putting in that extra entropy makes the environment's behavior even harder to predict.
[[start:2276890][end:2286690]] So the more you work at predicting what the environment is going to do the more you yourself make the environment's behavior less predictable.

38:07 [[start:2287110][end:2292670]] And this is the paradox of the FEP, which is not really a paradox.
[[start:2292750][end:2294980]] It's just what the physics does.
[[start:2296650][end:2325310]] So we can think of the FEP by driving systems to increase their distinctness from their environments or to self evidence, as Karl Friston calls it, as driving this increased complexity that both makes predictions better and makes predictions harder by transferring entropy into the environment.
[[start:2326050][end:2337086]] So what this tells us is that the FEP by itself will drive the development of systems with larger and larger complexity.

38:57 [[start:2337278][end:2345830]] And this clearly has enormous implications for evolutionary theory which we'll talk about in October.

39:08 [[start:2348170][end:2351554]] But I want to emphasize here that this is just the physics.
[[start:2351682][end:2357510]] It's just what the FEP does when it's forced to maintain a boundary.

39:20 [[start:2360270][end:2371710]] And before stopping here, I want to consider one aspect of this in particular, which is language.
[[start:2372210][end:2382800]] For example, human language, but any kind of language connecting any systems that are communicating with QRFs that are fairly close.
[[start:2383430][end:2389650]] And language is a complex QRF that we basically share.
[[start:2389800][end:2397670]] Otherwise, things like this interaction would be impossible, but we also remain distinct systems.

39:58 [[start:2398090][end:2401862]] So the question arises, how do we manage to do this?

40:01 [[start:2401996][end:2409530]] How do we manage to largely share a QRF while escaping, becoming entangled?
[[start:2410750][end:2424458]] And this is a question that's largely been ignored in physics because physicists have tended to ignore language and just assume that observers can communicate classically.
[[start:2424554][end:2440180]] So, for example, in talking about a Bell/PR experiment, which is a canonical experiment for measuring entanglement, the observers have to be able to share their results, or they can't observe entanglement, right?
[[start:2441110][end:2454898]] The observed result is a bunch of observational statistics that violate Bell's inequality, and those statistics can only be computed given the results that both of the observers obtain.
[[start:2454994][end:2459290]] So the observers have to share language to encode these results.

41:00 [[start:2460430][end:2464410]] So how come the observers aren't entangled?
[[start:2465310][end:2467850]] How come they are still separable?
[[start:2469310][end:2476026]] What we end up appealing to is some sort of common cause in the past to explain why they share a language.
[[start:2476218][end:2481760]] They both learned it from their culture, so their culture is some sort of common cause.
[[start:2482630][end:2486610]] But all such assumptions are fine tuning assumptions.

41:27 [[start:2487110][end:2504120]] So they all have basically the status of the value of something like the fine structure constant, without which we wouldn't have atoms and so we wouldn't have us.
[[start:2504970][end:2513210]] This value has to be within very small limits of the value we actually observe.
[[start:2513550][end:2517206]] And that's a case of fine tuning.
[[start:2517318][end:2521950]] The universe seems fine tuned in a way that allows us to exist.

42:02 [[start:2522450][end:2528560]] And if it wasn't fine tuned in that way, we wouldn't exist, and so we wouldn't observe anything.

42:09 [[start:2529170][end:2532218]] But fine tuning assumptions are a problem.
[[start:2532404][end:2535220]] They're a pointer to something we don't understand.
[[start:2536310][end:2546070]] And so I just want to leave you with the point that we have to be very careful when talking about interacting observers.
[[start:2546810][end:2569740]] So in talking about two components of some system that jointly interact with some environment but also communicate classically, and if you think back a few slides, that's exactly the structure that we've shown that the physics forces any complicated system to have.
[[start:2570610][end:2587970]] So next time, what we're going to focus on is this very question of how we describe observers that are both interacting with the quantum system and communicating classically in some language.

43:08 [[start:2588950][end:2591970]] So that session will be in August.
[[start:2592550][end:2604680]] At the end of this month, there's a discussion of this session with Ander, and I encourage you all to use the interactive Q and A to ask questions.
[[start:2605130][end:2610620]] You've been asking very good questions that I hope I've been managing to answer.
[[start:2611550][end:2613418]] So thank you very much.
[[start:2613504][end:2614422]] And Daniel.

43:34 [[start:2614486][end:2615500]] Over to you.
[[start:2617150][end:2617562]] Cool.
[[start:2617616][end:2617882]] Well.

43:37 _Daniel:_
[[start:2617936][end:2630720]] We have a few minutes for some questions maybe and or if you want to bring up any questions first, then go for it.

43:53 _Ander:_
[[start:2633330][end:2642718]] I was curious if you could say any words on the slide where you had all the possible alignments of QRFs and what you meant more by interacting thermally.
[[start:2642814][end:2649350]] So when you have a trivial agent on one side, what exactly does it mean to say that you're interacting thermally?

44:14 _Chris:_
[[start:2654080][end:2677830]] If you think about a system that is only interacting thermally with its environment, you end up thinking classically about, for example, an ideal gas that's in some sort of container and some of the molecules are very near the surface and their motions depend on the motions of all the other molecules that are inside.
[[start:2678600][end:2694040]] So there's a set of internal states that interact randomly with the external states that are near the boundary and so those external states interact randomly with the boundary.
[[start:2694700][end:2708750]] But notice in thinking in this way, you've imposed a spacetime embedding, so you've actually used space as a way of separating the internal states from the boundary states.
[[start:2710500][end:2729700]] And a system that if you drop this assumption of a spatial boundary, then a system that's only interacting thermally with its environment is going to look like a system that doesn't have any real internal states.

45:29 [[start:2729850][end:2733030]] It's going to look like a system that just has boundary states.

45:33 [[start:2733660][end:2738200]] And so a pure thermal interaction is going to start to look like entanglement.
[[start:2739180][end:2747384]] So we're actually only really interested in systems that aren't interacting only purely thermally with their environments.
[[start:2747512][end:2756860]] We're interested in systems that have enough internal structure that they're using that thermal energy to do something internally.
[[start:2757440][end:2777510]] So to give their internal dynamics some particular shape, so that their internal dynamics is actually circling around some well-defined attractor that requires some energy to maintain itself.

46:20 _Ander:_
[[start:2780200][end:2782244]] Yeah, I'm continuing with that question.
[[start:2782442][end:2799420]] I saw in the paper free energy principle for Quantum Systems that if you're in that situation when both keras are nontrivial, but perhaps B's is larger than A's, A's perceives non-local hidden variables.
[[start:2799760][end:2808220]] So I wonder if there is a way to relate those by taking a limit of making A small and recover the thermal interaction.
[[start:2808580][end:2815264]] Presumably if you let A become small, you should recover that thermal interaction, so to speak.
[[start:2815302][end:2815890]] Right?

46:56 _Chris:_
[[start:2816820][end:2819984]] Yeah, that's a very interesting comment actually.
[[start:2820102][end:2838016]] So if you're a system and all of your environments variables are effectively hidden to you, then you can't do any information processing because you don't have any access to any of your system, your environments' variables.
[[start:2838208][end:2841172]] So yeah, your interaction can only be thermal.
[[start:2841236][end:2842490]] I think that's correct.
[[start:2844460][end:2845450]] Thank you.

47:32 _Ander:_
[[start:2852460][end:2857310]] Since we're in this, in this topic and we don't have to context switch in that way.
[[start:2857920][end:2860016]] On the other hand, you have noise, right?
[[start:2860118][end:2865250]] In one of those other situations, I can't recall which one.
[[start:2866340][end:2868448]] I guess in the reversed one, right.
[[start:2868614][end:2878880]] When A's QRF is larger than that of B, so it encompasses more of the boundary degrees of freedom, those that are not overlapping A perceives as noises.

47:59 [[start:2879040][end:2879604]] That's correct.
[[start:2879642][end:2880230]] Right?

48:01 _Chris:_
[[start:2881320][end:2881780]] Yeah.
[[start:2881850][end:2889412]] A will be looking at B's thermal sector, B's free energy sector.
[[start:2889556][end:2890200]] Right.

48:10 [[start:2890350][end:2903340]] So A may be interpreting, in a sense, what it's doing as informative, and A may even be seeing what B is doing as informative.

48:26 [[start:2906800][end:2923890]] So noise for B may be signal for A, depending on how a's QRF is structured, but A is seeing more information than B is trying to send it.
[[start:2925860][end:2930390]] So it's essentially the reverse of the hidden variable case.
[[start:2931400][end:2942410]] There are variables in the other system that aren't telling you anything about what the other system is actually doing.

49:06 _Daniel:_
[[start:2946070][end:2955122]] That's very interesting in terms of reading too much or too little between the lines, connecting too many dots or connecting not enough dots.
[[start:2955266][end:2965098]] But these challenges where noise for one quantum cognitive agent might be signal for another and vice versa, those are the challenges that we want to address...
[[start:2965184][end:2977950]] ...because to have a physics that doesn't recognize those situations is kind of taking the view from nowhere or not really addressing the complexity of a cognitive engagement.

49:39 _Chris:_
[[start:2979890][end:2987330]] Yeah, it's describing interactions between, effectively, systems that don't share the same language.

49:50 _Daniel:_
[[start:2990390][end:2993300]] I have a question about the free energy principle here.
[[start:2994630][end:3002790]] Only in the last several years has the quantum free energy principle relationship come into light.
[[start:3002940][end:3011130]] So maybe could you just share a little bit about what incremental or quantum advances enabled that to happen?
[[start:3011280][end:3030400]] Or what degrees of freedom were pre-existing or added to enable work arising from perception and action in neural systems to also so naturally enter this context with the quantum information?

50:32 _Chris:_
[[start:3032450][end:3047620]] Well, I think, at least from a historical point of view, that connection was made based on the analogy between a Markov blanket and a Holographic screen.
[[start:3048570][end:3061420]] So these are structures developed in different parts of physics that essentially serve the same function of limiting the information that one system can have about another system.
[[start:3063230][end:3086930]] So it's that functional analogy between a Markov blanket defined classically and a Holographic screen defined in quantum theory that made it seem obvious that we could translate the free energy principle into a quantum theoretic principle.

51:35 _Daniel:_
[[start:3095350][end:3095954]] Yes.
[[start:3096072][end:3124650]] In live stream 40, we talked a lot about this, but I think that remains one of the most remarkable advances inside or outside the free energy principle literature based upon this functional acknowledgment of boundaries and the conditions that they entail, which, again, are the challenges that we want to address lest we ignore boundaries.

52:04 _Chris:_
[[start:3124990][end:3125642]] Right
[[start:3125776][end:3126774]] Yeah, precisely.
[[start:3126822][end:3131630]] I mean, the free energy principle is all about what happens when you have a boundary.

52:17 _Daniel:_
[[start:3137410][end:3139230]] The waste heat.

52:21 [[start:3141270][end:3148210]] Is this the actual thermal exhaust from our CPU?
[[start:3148710][end:3162338]] Or how can we think about the heat being released topologically rather than geometrically, like the location where it's released?
[[start:3162434][end:3171740]] What does it mean to consider physical processes topologically that we might otherwise just use a geometric way of thinking about?

52:53 _Chris:_
[[start:3173870][end:3194530]] Well, you basically put your finger on it and that you're not worried about the spatial difference between the geometric spatial difference between where one kind of information flows through the boundary and where another kind of information flows through the boundary.
[[start:3195590][end:3199460]] And you can think about this in Markov blanket terms.
[[start:3201030][end:3203730]] And the Markov blanket is just a network.
[[start:3204650][end:3215830]] And some of the causal arrows flowing through that blanket network are effectively transmitting noise.

53:39 [[start:3219290][end:3228374]] And you can think in the same way with respect to a holographic screen if you're doing a certain amount of information processing.
[[start:3228422][end:3240522]] And this brings up the whole issue of how efficient is a system in its information processing?

54:00 [[start:3240586][end:3243630]] How close is it to the Landauder limit,
[[start:3243710][end:3244340]] basically.

54:07 [[start:3247350][end:3262950]] Can it extract more energy from some bits than it has to use to modify the states of other bits?
[[start:3264090][end:3270060]] That's what this, if you will, metabolic question is all about.

54:32 [[start:3272190][end:3287150]] In the case of an organism, is it, can I get more energy from some of the chemistry that I have access to than I need to use to modify the chemistry that I need to modify?
[[start:3288290][end:3291622]] And if not, then life stops.
[[start:3291786][end:3293650]] Everything grinds to a halt.

55:00 _Daniel:_
[[start:3300810][end:3310066]] Now, can the heat exhaust informationally be useful for another agent somehow?
[[start:3310178][end:3316234]] I mean, can't we recover heat in a steam engine and use it to do useful work?
[[start:3316432][end:3321334]] Not to the point of a perpetual motion machine, but how can we recover exhaust?
[[start:3321462][end:3324640]] And then what does the perpetual motion machine look like?

55:27 _Chris:_
[[start:3327010][end:3340420]] Well, the environment is the system sitting over on the other side of the boundary that is absorbing whatever waste heat is generated by the system.
[[start:3341910][end:3345620]] Let's call it Alice that we're interested in.
[[start:3346310][end:3366780]] So that environment may be Alice, and Alice can't tell this, but it may be divided up into lots of different compartments, some of which are basically sucking in Alice's waste heat and doing something with it.
[[start:3368190][end:3386162]] So this is really a question about how is the environment structured and what operations does the environment execute with the input that it gets?
[[start:3386216][end:3388450]] How does it interpret that input?

56:32 _Daniel:_
[[start:3392200][end:3393430]] And what would.

56:35 _Chris:_
[[start:3395800][end:3413150]] This gets back to this question about how do we talk about multiple agents that are communicating with each other instead of talking about an environment that we don't characterize at all?

56:55 [[start:3415200][end:3427730]] How do we talk about an environment that includes some specified or preferred systems that are treated as or known to be other agents?

57:10 [[start:3430900][end:3434800]] Let me get back to your question about perpetual motion machine.
[[start:3435460][end:3448580]] Notice that in classical thermodynamics there's always the assumption that there's a big environment out there the rest of the universe or whatever, the whole environment that's not on Earth.
[[start:3449820][end:3463790]] That is an arbitrarily large source of, or it's not an arbitrarily large source of free energy, but it's a large source of free energy.

57:44 [[start:3464400][end:3470216]] And it's a large sink for entropy, a kind of arbitrarily large sink for entropy.
[[start:3470408][end:3489028]] So the second law of thermodynamics says the entropy of this entire system counting the whole surrounding environment doesn't decrease, so it can increase and still satisfy the second law.

58:09 [[start:3489114][end:3495750]] So this gives you the classical 19th century heat death of the Universe idea.
[[start:3497000][end:3517820]] And so your proposed machine is sitting somewhere embedded in this gigantic environment that can provide some finite amount of free energy but can exhaust effectively an arbitrary amount of entropy.
[[start:3519520][end:3535116]] So any machine has to dissipate entropy as it runs to fill up this kind of arbitrary sink of entropy that's the classical rest of the Universe.

58:55 [[start:3535228][end:3538180]] Now, compare that to the picture in quantum theory.
[[start:3538680][end:3543670]] The picture in quantum theory is the universe, by definition, is an isolated system.

59:04 [[start:3544600][end:3551480]] So its total information content doesn't change, right?
[[start:3551550][end:3552564]] It's evolving...
[[start:3552612][end:3560170]] ...unitarily, unitary operations preserve information, so they're just moving information around.

59:22 [[start:3562800][end:3578800]] So from the point of view of any local system, the local system is getting information from its environment, so it sees its environment losing information, so gaining entropy.

59:40 [[start:3580900][end:3592400]] What this tells us is that entropy is, in fact, not a globally definable quantity.
[[start:3592480][end:3598260]] Entropy is always defined relative to some observer, some division, some boundary.

1:00:00 [[start:3600140][end:3611850]] And this is another kind of big change in the last few decades and has led to, for example, entropic definitions of time.
[[start:3612400][end:3622590]] My local external time arrow is whatever direction I see entropy increasing the most.

1:00:29 [[start:3629210][end:3637110]] So, again, I would refer to people like Rovelli and Max Tegmark, who developed many of these ideas.

1:00:40 _Daniel:_
[[start:3640350][end:3641100]] Awesome.
[[start:3642430][end:3658222]] All right, thank you, Chris, and Ander, looking forward to seeing everyone's questions submitted and their preparation and participation and measurement in the discussion section.
[[start:3658366][end:3660162]] So thank you.
[[start:3660296][end:3661026]] Till next time.

1:01:01 _Chris:_
[[start:3661048][end:3661634]] All right.

1:01:01 [[start:3661752][end:3663102]] Thanks again, Daniel.
[[start:3663246][end:3663714]] Thank you.
[[start:3663752][end:3665938]] Ander, we'll see you later.

1:01:06 _Ander:_
[[start:3666104][end:3666930]] Bye.
