![Chris Fields presents "Physics as Information Processing" at Active Inference Institute, 2023](../../Video/cFPIP-01L_00001.png)

00:05 _Daniel:_
[[start:5900][end:9460]] Hello and welcome, everyone, to the Active Inference Institute.
[[start:9620][end:16020]] This is Session 1 of the course "Physics as Information Processing" with Chris Fields.
[[start:16180][end:19316]] First we'll have Ander Aguirre and Chris Fields
[[start:19348][end:20232]] introduce themselves.

00:20 [[start:20366][end:23540]] And then we'll carry on with the first lecture,
[[start:23620][end:24152]] here.
[[start:24286][end:44084]] Check out the video description for a link to the [Course Overview website](https://coda.io/@active-inference-institute/fields-physics-2023), where you can ask questions that will be answered asynchronously; register to participate in the discussions, which happen about two weeks after each of the six lecture sessions; and just learn more about this area.
[[start:44202][end:49264]] So thank you both so much for joining into this adventure
[[start:49312][end:51140]] we are starting now.

00:51 [[start:51290][end:54328]] And first, please, Ander Aguirre, introduce yourself.
[[start:54414][end:57172]] And then Chris' introduction and lecture.
[[start:57236][end:58010]] Thank you.

00:59 _Ander:_
[[start:59820][end:60280]] Hello!
[[start:60350][end:62200]] So I'll be the course assistant.

01:03 [[start:63180][end:70270]] And I'm a postdoc in math, specializing in probability. And I have a deep interest in the physics of information.
[[start:70640][end:74140]] And I've been familiar with Chris's papers for a while.
[[start:74290][end:76190]] So, yeah, just here to learn myself!

01:19 _Chris:_
[[start:79460][end:80316]] Thank you, Ander.
[[start:80348][end:81840]] And thank you, Daniel.
[[start:82260][end:99300]] I'm Chris Fields. And I'll be presenting this course in six sessions, and Ander will be organizing discussion sessions after each of those.
[[start:99670][end:103380]] And all of this is explained on the course website.
[[start:104730][end:108040]] So let's start!

01:49 [[start:109210][end:126810]] This is a course on "Physics as Information Processing," and this first session will be a historical perspective on the idea that physics is, or is about, information processing.

![Wittgenstein, Landaur, Wheeler](../../Video/Slide2.PNG)
[[start:127310][end:138478]] And I'll just start with a few quotations that span the middle of the 20th century - from **[Ludwig] Wittgenstein** in the 1920s saying "The world is all that is the case,"
[[start:138564][end:143490]] so, defining the world in terms of facts, not objects;

02:24 [[start:144390][end:149410]] **[Rolf] Landauer** in the early '60s, proclaiming that "Information is Physical;"
[[start:150470][end:162102]] and then **John Archibald Wheeler**, who in many ways is the grandfather of this era recently, stating it is "It from Bit,"

02:42 [[start:162236][end:167850]] so things come from information, i.e. bitstrings.
[[start:168910][end:177180]] And if nothing else, this shows that formulations of this idea get pithier as the 20th century rolls on!

![Physics, Clausius to Friston](../../Video/Slide3.PNG)
[[start:178510][end:185390]] But the history goes back farther clearly than the 20th century.
[[start:185730][end:196354]] But I'm only going to really talk about a piece of it and the timeline that I'll actually discuss today,
[[start:196472][end:203090]] the most relevant history of this idea, goes back to the mid-19th Century.

03:24 [[start:204330][end:211750]] And the first specific thing I'll talk about is **[Rudolf] Clausius**'s definition of entropy.

03:32 [[start:212890][end:230750]] But with the beginning of the understanding of thermodynamics and the role of information in thermodynamics, you get this very interesting multidisciplinary progression of ideas that incorporates the beginning of quantum theory.

03:52 [[start:232850][end:252900]] And the beginning of **quantum theory** can kind of be dated to the first **Solvay conference** in 1928 [[the Fifth Solvay Conference on Physics in 1927]], and the famous debate between **[Nils] Bohr** and **[Albert] Einstein** over whether quantum theory is about knowledge, information - or objects, things.
[[start:254650][end:261186]] But it incorporates a lot of work in computer science and logic and mathematics.
[[start:261298][end:275062]] So, interestingly, computer science was born effectively in the mid-30s with the work of **[Alonzo] Church** and **[Alan] Turing**, which very rapidly converged with the work in physics.

04:35 [[start:275206][end:279530]] So today we'll be talking about both computer science and physics.
[[start:280850][end:286880]] And then in the second half of the 20th Century, this just exploded into a huge area.

04:48 [[start:288050][end:303010]] And in consequence of that mid-20th Century development, we're beginning to see a new idea about physics which is roughly encapsulated in quantum information theory.

![Physics is about information transfer across boundaries](../../Video/Slide4.PNG)
[[start:303350][end:305494]] And the new idea is this.
[[start:305692][end:317686]] It's that what physics is actually about is information transfer across boundaries and the information... We can represent
[[start:317718][end:319978]] the information transfer like this.
[[start:320144][end:323260]] And this is a convention I'll use.

05:24 [[start:324030][end:326970]] A boundary is always a blue ellipse.
[[start:328030][end:339360]] And the agents that are exchanging information across this boundary are conventionally called Alice and Bob, which is just a more polite way of saying A and B.

05:40 [[start:340530][end:349890]] And when you think about this picture, it becomes clear that what physics is really about is communication.
[[start:350950][end:365750]] And this is a wild redescription of the idea of what physics is, compared to the ideas of Newton or LaPlace or even the 19th century ideas.
[[start:366170][end:393810]] And it's very different from the idea that's been preserved in 20th Century physics in the lineage of Einstein and others who viewed **classical physics** as, in a sense, either as completely fundamental or as a fundamental adjunct to quantum theory.

06:34 [[start:394550][end:403090]] So this way of thinking about physics is a very deeply quantum-theoretic way of thinking about physics.

![Where we are going in this course](../../Video/Slide5.PNG)
06:43 [[start:403670][end:411702]] And where we're going in this course today is really "how did this all happen?"
[[start:411756][end:413400]] It's the origin story.
[[start:414650][end:435600]] And then in the next session, I want to discuss quantum information theory explicitly. And in particular, how quantum theory makes this conclusion that physics is about communication very simple and obvious, much more obvious than it is in classical physics where it takes *work* to formulate this idea.
[[start:436610][end:451060]] Then in the next session, we're going to talk about **semantics**, and how observations become meaningful to the agents who make them and hence how actions become meaningful to the agents who make them.

07:32 [[start:452230][end:465750]] Then in August, we'll talk about **communication theory** a little bit more explicitly, and talk about how agents employ multiple communication channels when they're communicating.

07:46 [[start:466410][end:475974]] And this is obvious when you think of people communicating: they not only talk to each other, they look at the same things, they point to things, et cetera.
[[start:476022][end:479950]] So this is what I mean by multiple communication channels.
[[start:480450][end:489210]] Then in September, we'll leverage that discussion to talk about how **spacetime** actually emerges from communication.
[[start:489290][end:493854]] And this is one of the most important aspects, I think, of quantum information theory.

08:13 [[start:493982][end:509960]] It provides us with a way of viewing spacetime as an emergent phenomenon, that communication is what is *fundamental* in some ontological sense; and the *box* in which it happens, spacetime, is not.
[[start:511050][end:523530]] So in the final session in October we'll talk about applications to biology via the **Free Energy Principle**, and future directions both in physics and biology and elsewhere.
[[start:524190][end:526294]] So it's going to be an interesting ride!

08:46 [[start:526422][end:541150]] I'm keeping formalism to a minimum, because we're directing this toward the *broad* array of people who are interested in **Active Inference** and who are involved with the Active Inference Institute.
[[start:541830][end:553250]] And I would ask you to hold questions (because we have a lot to get through in an hour) for the interactive discussion and for the discussion forum.

09:14 [[start:554810][end:562470]] So I hope I explain things well enough that all of the concepts will be understandable.
[[start:563450][end:570780]] If not, **Wikipedia** is actually a wonderful resource in this area for just definitions of terms.
[[start:571230][end:577894]] So if there's anything that... just a term that is a trip-up, try Wikipedia.
[[start:577942][end:581006]] It's probably a very good source for what these terms mean.

![Our story begins...](../../Video/Slide6.PNG)
[[start:581188][end:586990]] So let's start! Our story, as I said, begins in the 19th Century.

09:47 [[start:587410][end:596130]] And in the mid-19th Century, lots of physicists were devoting their efforts to figuring out how to make better steam engines.
[[start:596870][end:611282]] And one question that arises when you're trying to design a steam engine is "what happens *physically* when you add heat to a system at constant temperature?"
[[start:611346][end:615350]] So if you're building a steam engine, you've got a boiler, because you need to make steam.
[[start:615690][end:622330]] And as you turn up the heat to your boiler, you get more steam, but the temperature doesn't change.
[[start:622480][end:624250]] So this is a mystery.

10:25 [[start:625470][end:634670]] What is the heat actually *adding* to the boiler that is not increasing the temperature?
[[start:635810][end:644530]] And Clausius responded to this question in a way that's sort of typical for a physicist or a mathematician.
[[start:645430][end:652478]] Since he didn't know what the answer was, he just *invented a new name* for whatever it was, and gave it a formal definition.

10:52 [[start:652654][end:665270]] So he called it **entropy**, which is a made-up word that, if it was translated from the Greek, would roughly mean "transformation content," en-tropy.
[[start:666250][end:683360]] And he represented it by a simple equation that the change in this new concept, entropy, which is always called S, is just equal to the change in heat, Q, at constant temperature, T.

11:23 [[start:683730][end:700210]] So obviously, this equation just reformulates the question in declarative form, saying "whatever this stuff is, its changes in this stuff are just changes in heat at constant temperature."
[[start:700790][end:702580]] Well, heat is energy.
[[start:702950][end:716066]] And this wasn't completely recognized in the mid-19th Century. But the way you'll see this equation in a current textbook is "dS is the change in *energy* at constant temperature."

11:56 [[start:716258][end:724010]] So even more commonly, you would see it written as "the change in energy is equal to the temperature times the change in entropy."
[[start:724430][end:728950]] It's the most common sort of textbook way of seeing this.

12:09 [[start:729120][end:732010]] But the question, of course, is, "What *is* this quantity?
[[start:732090][end:733498]] What is this entropy?
[[start:733594][end:735440]] What does this concept *mean?*"

![But what *is* entropy?](../../Video/Slide7.PNG)
[[start:736450][end:753300]] And about 15 years after Clausius proposed it, **[Ludwig] Boltzmann** had the key insight, which is that "entropy is a measurement of *our uncertainty* about the **state** the system is in."
[[start:754490][end:773820]] And in particular, he again, of course, went to formalism, and said "the entropy, S, is equal to some constant times the number of states that the system can be in that look the same to us."

12:54 [[start:774750][end:782542]] And since that number of states is enormous, the way to make that manageable is to take the *log* of the number of states.

13:02 [[start:782676][end:785310]] The **natural log** is *ln.*
[[start:786050][end:790270]] And this constant k is called **Boltzmann's constant**.
[[start:791750][end:811080]] And Boltzmann was able to do this because he subscribed to a radical, very unpopular theory that material things, including gases like air, were made of atoms; and heat made the atoms move around.
[[start:811770][end:816646]] And as you increase the amount of heat, the atoms can move in many different ways.

13:36 [[start:816828][end:822010]] So the number of *states* that they can be in that look the same to us *increases.*
[[start:822350][end:823914]] And that's what entropy is.
[[start:823952][end:832622]] It's this increase in the number of states that the system can be in that all look the same to us with the measurements that we can make.
[[start:832676][end:837840]] And since they look the same to us, we're *uncertain* about exactly what state they're in.
[[start:839250][end:841870]] So entropy is a measure of uncertainty.

14:03 [[start:843190][end:846370]] This was really the beginning of modern physics,
[[start:847510][end:855014]] because what it says now is that "decreasing uncertainty requires energy."
[[start:855212][end:859480]] It links a measurement of uncertainty to a measurement of energy.
[[start:860490][end:871580]] And if you think about the **uncertainty principle** in quantum theory, the core idea of the uncertainty principle is "you can't *measure* a system without *disturbing* it."
[[start:872270][end:877914]] So to actually *act* on a system requires energy.

14:38 [[start:878032][end:880400]] And that's what you have to do to get information.
[[start:881330][end:885710]] So here's Boltzmann, basically inventing quantum theory.

![fast forward to 1900](../../Video/Slide8.PNG)
[[start:887490][end:892000]] So we're going to fast forward by another 15 years, to 1900.
[[start:892850][end:903540]] And in 1900, **[Max] Planck** solved this problem called the "black-body radiation problem," which was basically "how much heat does your hot boiler give off into the air?"

15:04 [[start:904490][end:918766]] And all of the measurements of the heat that hot boilers gave off to the air ran into problems in classical physics, and caused contradictions and quantities that went to infinity.

15:18 [[start:918818][end:920346]] And all of that was bad.
[[start:920528][end:927078]] So many people were trying to solve this problem. And Planck solved it by making a simple postulate.
[[start:927174][end:932570]] He said "the energy of the radiation is proportional to its frequency."
[[start:932650][end:935440]] So its *color* in the case of light.
[[start:935970][end:942154]] And if you go higher frequency, you end up in ultraviolet and X rays and gamma rays.

15:42 [[start:942202][end:946740]] If you go to lower frequency, you go into microwaves and radio and all of that.
[[start:947670][end:951182]] So this is a nice way of talking about radiation.
[[start:951326][end:953330]] And it turned out that this solved the problem!
[[start:953400][end:963590]] I mean, just assuming this simple proportionality relationship produced spectra for black-body radiation that worked, that matched what you saw experimentally.
[[start:964250][end:965958]] Well, this means something very important.

16:06 [[start:966044][end:972906]] It means because this number *h*, the proportionality constant called **Planck's constant**, is a *number,*
[[start:973008][end:974198]] it's finite,
[[start:974374][end:977930]] it means that energy comes in discrete units of *h*.
[[start:978080][end:984080]] You can have one *h* or two *h* or 10 million *h*, but you can't have half an *h* of energy.
[[start:985890][end:987290]] So it's quantized.

16:27 [[start:987450][end:991230]] And this is widely recognized as the birth of quantum theory.
[[start:991750][end:994580]] But of course, we should have known this already,
[[start:994950][end:997060]] if we just thought a little bit,
[[start:997430][end:997890]] right?
[[start:997960][end:1007110]] We know that changes of energy are proportional to changes in entropy by temperature.

16:47 [[start:1007610][end:1016120]] And we know that entropy is a measure of the number of states, and numbers of states are just numbers.
[[start:1016750][end:1028140]] You can have one state, two states, three states, 10 million states, 100 billion states, but they're all just a number - one, up.

17:09 [[start:1029310][end:1030486]] And it's not infinite.
[[start:1030518][end:1035360]] There's not an infinite number of states unless you have an infinite amount of energy, which you don't have.
[[start:1036050][end:1040910]] So we knew already that entropy could only take discrete values.

17:21 [[start:1041330][end:1048530]] And since energy and entropy are basically the same thing, we knew already that energy could only take discrete values.
[[start:1049110][end:1057030]] So we could have realized in 1900 that energy is quantized because the number of states is quantized.
[[start:1058410][end:1067446]] So it shouldn't have really been a mystery why energy was quantized, but it was a mystery, and it stayed a mystery, and it said, still a mystery.
[[start:1067478][end:1091870]] People still debate the meaning of quantum theory, but another thing we could have known in 1900 was something very important, and it's that this quantum of action, Planck's constant, which has units of action, which is energy times time, is intimately related to Boltzmann's constant.

18:13 [[start:1093510][end:1099970]] And Boltzmann's constant has units of energy over temperature.

18:21 [[start:1101910][end:1106020]] But this wasn't actually understood until the 1950s.
[[start:1106870][end:1109158]] No one really figured that this out.
[[start:1109244][end:1112214]] There was this relation until the 1950s.
[[start:1112412][end:1117290]] And when it was figured out, it was figured out by a guy named Jean Carlo Wick.
[[start:1117710][end:1129930]] And he introduced this notion of the Wick rotation by realizing that if you have an equation in classical physics, and in it, there's the term one over KT.

18:50 [[start:1130910][end:1135658]] You can always replace that one over KT with this other expression.
[[start:1135754][end:1137150]] It over h-bar.
[[start:1137220][end:1143250]] H-bar is just h divided by two pi, and you'll get an equation that's valid in quantum theory.
[[start:1143910][end:1147730]] And this is typically described in textbooks as a trick.
[[start:1148310][end:1154760]] And whenever something in physics is described as a trick, what that really means is it's something we don't understand.

19:16 [[start:1156650][end:1161030]] And lots of papers have been written about the meaning of the WIC rotation.
[[start:1162890][end:1169980]] But to start to understand the WIC rotation, I want to look at this equation a little bit.
[[start:1171790][end:1183134]] One over KT is one over in energy, and it over h-bar is one over in energy.
[[start:1183252][end:1197250]] Since h-bar is units of energy times time, we have time in this equation, and then we have this factor, I, which is typically thought of as just an imaginary number.
[[start:1197400][end:1199940]] So it's the square root of minus one.

20:00 [[start:1200550][end:1203358]] And what's this I doing in this equation?
[[start:1203454][end:1206454]] And in fact, you see factors of it over h-bar.
[[start:1206492][end:1211698]] If you're familiar with quantum theory everywhere in quantum theory.
[[start:1211874][end:1216040]] So what's the meaning of this imaginary number?

20:17 [[start:1217230][end:1234670]] And if you just think of it or of I as this arbitrary imaginary number that somehow renders the equation mysterious, then the whole of quantum theory is mysterious, but the Wick rotation is very mysterious.

20:35 [[start:1235250][end:1238990]] But what I is actually is an operator.
[[start:1239970][end:1246910]] And if you think of the real numbers as an axis, which is always drawn horizontally.
[[start:1246990][end:1248082]] So here it is.
[[start:1248216][end:1252482]] Here's zero, and the axis is pointing that way.
[[start:1252536][end:1256326]] I'm sorry, I can't get the camera really far enough away to see my arm here.

20:56 [[start:1256508][end:1258070]] So what is I?
[[start:1258220][end:1265190]] I is actually an operator that rotates the whole real axis by 90 degrees.
[[start:1265690][end:1272954]] So if you see a plot of complex numbers, then the real numbers go this way, and the, quote, imaginary numbers go that way.
[[start:1272992][end:1277638]] So what multiplying by I has done is rotate by 90 degrees.

21:17 [[start:1277814][end:1286400]] And of course, if you do I squared, you rotate twice by 90 degrees by arm would do this, but you end up pointing that way, and those are the negative numbers.

21:26 [[start:1286930][end:1297358]] So I is an operator that rotates something by 90 degrees, and if you rotate four times by 90 degrees, you're back to the identity.
[[start:1297534][end:1299780]] So I to the fourth is one.
[[start:1300950][end:1308950]] So this tells us something very interesting, which is that what the WIC rotation is really talking about is a rotation.
[[start:1309770][end:1312230]] It's a geometrical equation.
[[start:1313290][end:1322410]] And in July, we'll come back to this and really probe what this Wick rotation means physically.

22:04 [[start:1324990][end:1332640]] But as I said, this wasn't understood to the 1950s, and by the 1950s, a lot had happened.
[[start:1333010][end:1334954]] So quantum theory had been developed.
[[start:1335002][end:1336922]] Bohren Einstein had had their debate.
[[start:1336986][end:1338814]] Particle accelerators had been built.

22:18 [[start:1338852][end:1340574]] The atomic bomb had been built.

22:20 [[start:1340692][end:1349794]] Nuclear physics was well in its way, so an enormous amount of practical physics had been done.
[[start:1349912][end:1351966]] Quantum theory was highly developed.
[[start:1351998][end:1360310]] People were starting to think about quantum field theory before they made this simple realization that's formulated in the Wick rotation.
[[start:1360650][end:1363240]] So this is a harboring of things to come.
[[start:1363610][end:1372060]] But before we continue in physics, we need to backtrack in time a little bit and look at what the mathematicians were doing.

22:53 [[start:1373150][end:1385146]] So across the hall in the math department, one year after the Solve conference in 1929, kurt Godel proved his famous first incompleteness theorem.
[[start:1385338][end:1391280]] And the theorem states that no formal system that contains arithmetic can be both consistent and complete.
[[start:1392630][end:1405880]] And that means that either there are true statements that aren't provable in the formal system, or there are false statements that are provable, or, of course, both.

23:26 [[start:1406810][end:1411878]] And Godel's proof is actually extremely simple.
[[start:1411964][end:1428010]] Almost all of the work in the proof is setting up all of the notation and procedures and so forth to formulate within arithmetic the sentence, this sentence is not provable.

23:49 [[start:1429090][end:1436800]] And once you have that sentence formulated within arithmetic, then the conclusion of the proof is obvious.
[[start:1437250][end:1443890]] If you can prove the sentence, this sentence is not provable, then you've proved something that's false.
[[start:1444230][end:1450686]] And if you can't prove it, then there are sentences that you can't prove in arithmetic.
[[start:1450878][end:1473686]] So this was incredibly bad news for mathematicians who thought that finite discrete operations, which is what proofs are and also what computations are, can exhaustively enumerate the facts and this was the assumption behind Wittgenstein's claim that the world is all that is the case, the world is a collection of facts.

24:33 [[start:1473878][end:1483600]] And optimistically, he thought that first order logic would allow us to enumerate all those facts and we'd be done dreams of a final theory again.

24:45 [[start:1485970][end:1496690]] So Godel's Theorem means that no system with finite capabilities, no system that can just do finite discrete operations, can fully describe its environment.
[[start:1497110][end:1503810]] It will always be in an environment where there are true things that aren't provable or false things that are provable.
[[start:1504890][end:1512040]] But I think more relative to a discussion of agents is that it means that no agent can describe itself.
[[start:1512970][end:1528540]] Any agent's theory of itself will either contain true statements that it can't derive or false statements, or it will either miss true statements that it can't derive or wind up deriving things that are false about itself.
[[start:1529410][end:1532320]] Of course, we see this in psychology all the time.

25:33 [[start:1533410][end:1544190]] So an immediate consequence of Godel's Theorem was an intense investigation of what computation actually is, what it meant to talk about finite discrete operations.

25:44 [[start:1544850][end:1548782]] And two leaders of this were, of course, Church and Turing.
[[start:1548846][end:1560440]] And here's a picture of a Turing machine, which is just a little device with a couple of tapes and a tape reader and a simple logic unit that either writes a one or a zero if it sees a one or a zero.
[[start:1561450][end:1577530]] And they defined a computation as a process that can be implemented in finite time by such a machine or by Church's lambda calculus or by any of the now hundreds of other methods that are provably equivalent to a Turing machine.
[[start:1578030][end:1579820]] So what does this mean?

26:20 [[start:1580270][end:1589200]] It means that computation is a physical process that can be mechanized and it turns out, mechanized in any one of a huge array of ways.
[[start:1590050][end:1594846]] It means that many different implementations of any computation are possible.
[[start:1594948][end:1600530]] So I can do it on a Turing machine, I can do it on my laptop, I can do it on my head, et cetera.
[[start:1601270][end:1605554]] The most important things it means is that there are questions with no computable answer.

26:45 [[start:1605672][end:1608306]] This is the Revenge of Godel's theorem.

26:48 [[start:1608498][end:1613798]] And two of the most famous questions of this kind are given some arbitrary program.
[[start:1613884][end:1614882]] Will it halt?
[[start:1615026][end:1617578]] Will it get to an answer in finite time?
[[start:1617744][end:1622410]] And the answer to that question is this is undecidable.
[[start:1622750][end:1625260]] No procedure can figure this out.

27:06 [[start:1626270][end:1634670]] And the other undecidable question is, given some arbitrary program, what function does it compute?
[[start:1635090][end:1640730]] And you'd think that would be simple, that you can read a program and figure out what function it computes.
[[start:1640890][end:1643502]] But it turns out that is undecidable.
[[start:1643646][end:1647620]] That cannot be done by any finite process.
[[start:1649270][end:1659990]] So this was another body blow to the goal of understanding everything with finite discrete processes.

27:40 [[start:1660330][end:1663366]] But it also set the stage for something new.
[[start:1663548][end:1676380]] It set the stage for thinking about an agent who interacts with a computational process by giving it an input and then looking at its output sometime later.

27:58 [[start:1678110][end:1686590]] And this, of course, will look familiar because I've included the blue ellipse, which is the boundary, which these days we call a user interface.
[[start:1687490][end:1697700]] And the user interface just allows some finite action on the system and then the ability to observe some finite response by the system.
[[start:1698150][end:1707574]] So we can now ask what can Alice determine by acting in some finite way and then making some finite number of observations I.

28:27 [[start:1707612][end:1708200]] E.
[[start:1708650][end:1713880]] Receiving some finite number of outputs from the system that she's acting on.
[[start:1715850][end:1722326]] And the first 20 years of this produced a large number of answers, all of them negative.
[[start:1722518][end:1731070]] So to go back to Turing, he proved that Alice can't tell what's implementing the function that she sees being implemented.
[[start:1731970][end:1737002]] She can't tell whether a given input will lead to an output.

28:57 [[start:1737066][end:1738560]] That's the halting problem.

29:00 [[start:1740130][end:1745380]] Shannon showed that Alice can't tell what the inputs mean to the system.
[[start:1746390][end:1751330]] His whole theory of communication is completely independent of semantics.
[[start:1751910][end:1758470]] And his theory of communication actually accurately describes what Alice can observe.
[[start:1759930][end:1769130]] Rice is the one who proved that you can't determine what program is generating the outputs.

29:29 [[start:1769950][end:1780510]] And then Moore proved a very similar result in a completely different formal setting of general cybernetics that you can't tell what process is generating the outputs by finite observation.
[[start:1781570][end:1793950]] But what Alice can do is build a predictive model of what generates the output she sees in response to her inputs and test it by designing new inputs.
[[start:1794370][end:1800930]] And this is, of course, as Karl Popper told us, the process that we call science.

30:01 [[start:1801430][end:1807080]] So Alice can do science even though she can't answer any of these fundamental questions.

30:10 [[start:1810010][end:1824730]] Now, this, of course, has a huge technological consequence since this theory of computation tells us that processes are effectively virtual.
[[start:1826430][end:1831306]] We don't know what they are and we can't determine what they are except in theory.
[[start:1831418][end:1841600]] By making a theory technologically, it means we're free to use virtualization everywhere because we have to deal with it anyway.
[[start:1842470][end:1845758]] And this allows us to build multilevel architectures.
[[start:1845854][end:1855960]] It means that we can architect computers where no layer of the computation has any idea what's going on below or above it and doesn't need to.

30:57 [[start:1857290][end:1860520]] And that's what makes practical programming possible.
[[start:1861130][end:1878780]] So from these no go theorems that tell you what you can't do, you actually get an enormous boost into it and use to probe the world and develop theories and on and on and on.

31:20 [[start:1880290][end:1891680]] So in a sense, Godel birthed not only computer science, but practical computing by showing us that virtualization is just the way the world works.
[[start:1892150][end:1908230]] So now let's go back to physics where these ideas were replicated, basically reintroduced, reinvented by Feynman in developing his path integral formulation of quantum theory.
[[start:1908570][end:1921882]] And basically what Feyman realized was that in any physical process, the observer Alice prepares some state that she's interested in.

32:01 [[start:1921936][end:1924730]] She prepares some input to an experiment.
[[start:1925230][end:1932080]] Then she lets something happen, and then she sees what the result of the experiment is.
[[start:1932450][end:1936110]] And the canonical experiment in physics is scattering.
[[start:1936450][end:1944420]] You fire two protons at each other, and they intersect someplace, and stuff comes out, and you measure the stuff that comes out.

32:24 [[start:1944950][end:1952580]] And what you can measure is momentum and spin energy, things like that position.

32:33 [[start:1953510][end:1961762]] So these processes conserve the total values of the things you can measure.
[[start:1961826][end:1974940]] So in particular, they preserve momentum and angular momentum, and they preserve other things that are harder to measure and are only approximately conserved anyway, like Lepton number.
[[start:1975710][end:1996020]] But Feynman's contribution to this way of thinking about experiments was to say, look, if you want to understand the output, you have to sum over all of the possible processes that could have produced the output from the input, no matter how improbable they are.
[[start:1996790][end:2016370]] So the famous idea from Feynman diagrams is if you have an electron that's scattering off an atom, you measure the initial state of the electron that you've generated with an accelerator or something, and you measure the final state, which involves momentum and spin and so forth.

33:36 [[start:2016530][end:2035120]] And for all you knew, partway through the process, the electron disappeared, and an entire universe appeared and then annihilated with a copy of an entire anti universe, and the electron came back out.

33:55 [[start:2035730][end:2043570]] And you have to include processes like that if you really want to understand and correctly predict the outcomes of your measurements.
[[start:2044230][end:2056274]] And Murray Gelman lifted the bumper sticker slogan from Th White and the once and Future King everything not explicitly forbidden is mandatory.
[[start:2056322][end:2058520]] That sums up Feynman's idea.
[[start:2060090][end:2072490]] And this is called the totalitarian principle, since it's what's written in Th White's book on the kingdom of the ants, for which everything not explicitly forbidden is mandatory.
[[start:2073550][end:2080026]] So let's think about a real example that's a bit actually, it's the same as scattering.

34:40 [[start:2080058][end:2085470]] The ultimate scattering experiment in physics is a black hole.
[[start:2086610][end:2091840]] Stuff goes into the horizon, stars, whole galaxies, whatever.
[[start:2092710][end:2096322]] Something happens, and stuff comes out.
[[start:2096376][end:2110840]] And what comes out is Hawking radiation, and information is conserved if the information in the Hawking radiation is actually the same as the information in the stuff that went in.
[[start:2111770][end:2115650]] And conservation is not qualitative.

35:15 [[start:2115730][end:2116910]] It's quantitative.
[[start:2117010][end:2121130]] It's only the quantity of information that's supposed to be preserved.
[[start:2121790][end:2130270]] And you can ask, how much is the information that's being emitted by a black hole that's emitting Hawking radiation?
[[start:2130930][end:2137658]] And Beckenstein was the one who figured this out, using an incredibly simple argument.
[[start:2137834][end:2140160]] But I'll just give the answer here.

35:40 [[start:2140530][end:2162920]] The answer is that the total entropy of the black hole is its area divided by four, and the area in this equation has to be computed in Planck units, which are units where Planck's constant and the speed of light and boltzman's constant and other interesting things are all set equal to one.
[[start:2164170][end:2172810]] So one Planck area is the Planck length squared, which turns out to be about ten to the minus squared.
[[start:2173470][end:2178460]] So this is that black holes are the most entropic entities we know of.
[[start:2178930][end:2199730]] So a black hole about this big with a radius of about a meter has an entropy of about ten to the 70th, which is, of course, an astonishingly big number, and a black hole with the area of the sun.
[[start:2199880][end:2212440]] So a moderate sized cosmological black hole, a real thing that we can observe with a gravity wave telescope or something, has an entropy of about ten to the 79th.

36:52 [[start:2212810][end:2224300]] And really big black holes, which are bigger than the entire solar system, have entropies into the ten to the something.
[[start:2225070][end:2228650]] So these are enormously entropic entities.

37:10 [[start:2230930][end:2233998]] But Beckenstein didn't just tell us that.
[[start:2234084][end:2240830]] He told us something about the structure of the interface, the horizon of a black hole.
[[start:2241510][end:2243700]] And this is what he told us.

37:26 [[start:2246790][end:2256950]] You can compute entropy in bits just by using logs, base two instead of logs based e, natural logs.
[[start:2257370][end:2263560]] And that's just multiplying the natural log by about 1.4.
[[start:2264810][end:2272620]] So we can write the entropy of black hole, of black hole in units of bits, and it's about a over six.

37:53 [[start:2273630][end:2280270]] So what does this mean to say that we can think of the entropy in terms of bits?
[[start:2280610][end:2308690]] What it says is that we can think of the interface in terms of a bit array, and we can think of all of these bits as encoded on this interface at a density of one bit every roughly six plank lengths squared, six plank areas.

38:28 [[start:2308850][end:2312470]] So this is an incredibly dense encoding in a black hole.

38:34 [[start:2314650][end:2317014]] And it's an interesting idea about black holes.
[[start:2317062][end:2321498]] But what gets really interesting is what happens when you generalize it.
[[start:2321584][end:2327260]] And of course, physicists are prone to generalization, and that's what happened next.

38:50 [[start:2330110][end:2337150]] Gerard to Hooft, almost immediately thereafter, on the basis of Beckenstein's work, formulated the Holographic principle.

38:57 [[start:2337730][end:2346050]] And what the Holographic principle says is we can think of any system as approximately a black hole.
[[start:2346870][end:2350210]] And the only approximation is the encoding density.
[[start:2350950][end:2361042]] The boundary of any system encodes the information that we can get about the system at some density.
[[start:2361106][end:2366150]] And the density is less than the density for a black hole because we're not black holes.

39:27 [[start:2367370][end:2379130]] And this rules out a lot by limiting the amount of information that you can extract from a system to the amount of information that you can actually write on its boundary.
[[start:2379790][end:2385406]] And one of the things that it rules out is knowing the geometry on the inside of the system.
[[start:2385588][end:2402034]] And to Hoof put it this way, which I think is a brilliant thought experiment, he says, look, the metric inside this system can be so curved, effectively the space time inside the system can be so curved that you could stick an entire universe inside.

40:02 [[start:2402232][end:2409750]] And we never know because it wouldn't change the amount of entropy number of bits that are encoded on the boundary.
[[start:2410650][end:2413494]] So the inside geometry can be anything.

40:13 [[start:2413692][end:2415414]] And you can't find out by.
[[start:2415452][end:2417740]] Looking at the outside of the system.
[[start:2418990][end:2424010]] Now, the Holographic principle almost follows from classical physics.
[[start:2425630][end:2440670]] There's Euler's theorem, which tells you about one over R squared forces, and you can think of the force as penetrating the boundary at some density.
[[start:2441250][end:2451330]] And the difference between Euler's theorem and the Holographic principle is just that the density in classical physics can go to infinity.

40:51 [[start:2451990][end:2460466]] And in the Holographic principle, it can only go to this maximal density that's achieved by a black hole.
[[start:2460658][end:2461110]] Why?
[[start:2461180][end:2469100]] Because if you try to get any higher, more information, the information gets sucked into the black hole, and you can't get it out.

41:11 [[start:2471390][end:2484560]] So the Holographic principle becomes a guiding principle for thinking about any physical system and what it means to extract information from a physical system.
[[start:2485330][end:2488974]] And in fact, we'll talk about this next time.
[[start:2489172][end:2495060]] You can say exactly what the information encoded on the boundary of any system is.
[[start:2496790][end:2513106]] And what I'll go through next time is seeing that the information that's encoded on the boundary is a specification of the energy that's being exchanged by the interaction, which, of course, is linear in the number of bits.
[[start:2513138][end:2515830]] It's just counting the number of bits.

41:57 [[start:2517230][end:2517980]] Okay?
[[start:2518350][end:2539630]] So with the Holographic principle, we now have a complete new science about systems that are exchanging finite discrete information across a boundary by encoding that information on the boundary and then reading the information off the boundary.

42:20 [[start:2540370][end:2545650]] So here's a new way of thinking about physical interaction.
[[start:2545990][end:2558658]] Alice writes a message on her boundary with Bob, and Bob reads the message off the boundary and then writes his own new message, which Alice then reads.
[[start:2558834][end:2562280]] And of course, that's what's happening right now.

42:42 [[start:2562970][end:2570886]] I'm writing information by speaking on an interface, which is effectively the Internet.
[[start:2571078][end:2576250]] And you're reading that information off the Internet by listening to it.
[[start:2576400][end:2584030]] And when we get time for questions, you'll be writing information on the Internet, which I'll be reading.
[[start:2585250][end:2589658]] Now, the key thing about this new science is that it's topological.
[[start:2589754][end:2596942]] It's about connectivity across some communication channel, which we represent as a boundary.

43:17 [[start:2597086][end:2602930]] It's not geometric, so it doesn't assume anything about spacetime.

43:24 [[start:2604090][end:2613030]] So it allows us to build a model of space in particular as an emergent phenomenon.
[[start:2613370][end:2627100]] And it allows us to see time as not some absolute external abstraction, but something that the communicating agents measure for themselves.
[[start:2628430][end:2631920]] And so they each act in their own time.
[[start:2633090][end:2640906]] And we get a very natural measure of time in terms of how many bits I see coming across my boundary.

44:00 [[start:2640938][end:2651250]] And again, we'll talk about that in the next couple of sessions and then talk about it more thoroughly in September when we talk about emergent spacetime.
[[start:2652230][end:2664882]] So quantum information theory looks very different from the physics that came before, not because it's adopted a new formalism, the tools of quantum theory.

44:25 [[start:2665026][end:2681840]] It's because it's entirely changed the thinking about what physics is and what it's about and replace this idea of forces and balls banging into each other and all of that with the idea of communication between agents.
[[start:2682530][end:2687310]] And of course that's familiar from an active inference perspective.
[[start:2687890][end:2695710]] So we can now back up a little bit to see what they were doing in classical physics during this period.

44:55 [[start:2695790][end:2697682]] Well, let me go on a little bit.
[[start:2697736][end:2698340]] Sorry.

45:02 [[start:2702070][end:2714226]] This is just a slide quoting Wheeler, who of course is the most radical in terms of impitheist, in terms of formulating these ideas.
[[start:2714418][end:2718250]] But here's his characterization of this new physics.
[[start:2718830][end:2720490]] It's not reductive.
[[start:2721630][end:2723930]] All of the reasoning is circular.

45:25 [[start:2725230][end:2731630]] You don't have smaller things and then yet smaller things, and then yet smaller things forever.

45:33 [[start:2733090][end:2734510]] There are no laws.

45:36 [[start:2736690][end:2741070]] So what you see on the interface is a message.
[[start:2741220][end:2747090]] It's not something that's governed by laws since the beginning of the universe.
[[start:2747830][end:2749406]] There's no continuum.
[[start:2749518][end:2752050]] So there's nothing described by real numbers.
[[start:2752120][end:2753930]] It's all described by integers.

45:54 [[start:2754030][end:2756710]] Everything's done in finite dimensional spaces.
[[start:2757050][end:2762280]] And finally, and most importantly, there's no spacetime box in which things happen.
[[start:2762810][end:2766294]] So think of how radical this is means.
[[start:2766332][end:2773290]] There's no big bang, there's no big rip, there's no bouncing universe.
[[start:2773870][end:2779290]] All of those ideas are out the window because they're classical and they're about spacetime.

46:19 [[start:2779970][end:2787390]] And what the new physics wants to do is derive spacetime out of basically users experiences.

46:28 [[start:2788850][end:2796142]] So the agents here are all observer participants in Wheeler's language.
[[start:2796206][end:2804450]] But what that just means is agents that want to communicate and it's their communication that gives rise to physics.
[[start:2805850][end:2818810]] So now we'll go back to classical physics and what was happening, or one thing that was happening in classical physics at that time was a lot of thinking about stochastic causal networks.
[[start:2819630][end:2835130]] And Pearl realized that if you have any stochastic causal network that's unidirectional, then around any node, you can draw what he called a Markov blanket.

47:15 [[start:2835290][end:2857080]] And a Markov blanket is just the set of nodes in the network that absorb all outside causation and then transmit that causation into whatever node you're interested in and then absorb all causation coming from the node you're interested in and transmit it to the rest of the world.

47:37 [[start:2857770][end:2864642]] And so we can redraw that in Part B here, and it should look very familiar.
[[start:2864706][end:2869900]] A Markov blanket is just a classical physics way of talking about a Holographic screen.
[[start:2870670][end:2884874]] And the number of nodes in the Markov blanket, or in particular the number of degrees of freedom times the number of nodes, is just the number of bits that flow across that Markov blanket.
[[start:2884922][end:2889520]] So it's the entropy of the effective Holographic screen.

48:12 [[start:2892390][end:2898210]] All these ideas were reinvented more or less independently within classical physics.
[[start:2898950][end:2921960]] And it was from this classical physics background that Karl Freston came up with the idea that a Markov blanket defines a persistence, at least from an active inference institute point of view everyone is familiar with, because it's the foundation of the idea of active inference.

48:44 [[start:2924620][end:2936140]] Any system that persists through time does so by making sure that it doesn't dissolve into its environment.
[[start:2936560][end:2938284]] Well, what does that mean?
[[start:2938482][end:2947040]] It means it persists through time by maintaining the integrity of its Markov blanket or the integrity of its boundary.
[[start:2947620][end:2967380]] So this of course is just a tautology, but it's a very interesting and very productive tautology because it says that any system is using the information it gets on its boundary from its environment to build a model of how its environment behaves.
[[start:2967960][end:2975690]] And then it uses that model to act back on its environment to test and refine its model.

49:36 [[start:2976380][end:2980490]] And again, as Popper told us, this is just what science is.
[[start:2981120][end:2989470]] So what the free energy principle really tells us is that all systems are agents that are doing science all the time.

49:50 [[start:2990400][end:3011060]] So physics is effectively not just the study of communication, but it's the study of agents doing science with each other, pairs of agents who are trying to figure each other out by their communicative exchanges.
[[start:3012200][end:3043020]] So that's the history of how we got from 1930s sorry, 1850s thermodynamics to the free energy principle and how the free energy principle connects to these very deep and extremely radical, especially within context ideas in quantum theory and quantum cosmology and computer science.
[[start:3043540][end:3079560]] All of which tell us that the world we see is a projection that's being written on our boundaries by a process that we have no access to except the procedure of active inference or the procedure of science, which is to formulate predictive models and test them by doing things in the world and seeing how the world responds.

51:21 [[start:3081360][end:3085260]] So that's it for this session.
[[start:3087200][end:3097250]] The first discussion session which Andrew is going to lead will be the 3 June at this same time, I E 05:00 European time.
[[start:3098180][end:3102960]] And then my session number two will be in mid June.
[[start:3103700][end:3111910]] And if you look at the course website, there's this subsidiary website for interactive Q and A.
[[start:3112360][end:3132060]] And I invite everyone to post questions and discuss them and hope that we'll have an interesting exchange and that everyone will come to sort of an understanding of what was talked about today through discussion.

52:12 [[start:3132560][end:3140888]] And we'll be interested in being back in June to see how to formulate this in quantum theory.
[[start:3140984][end:3151424]] So thank you very much and thank you again, Daniel, for organizing this and hosting it and putting together all the technical things necessary to pull this off.

52:31 [[start:3151622][end:3153570]] I could never do that on my own.

52:35 _Daniel:_
[[start:3155140][end:3155744]] Thank you.
[[start:3155782][end:3158550]] We're really excited here.

52:39 [[start:3159560][end:3160816]] Any closing thoughts?
[[start:3160848][end:3165140]] Or andrew, I'd love to hear your reflection just briefly.
[[start:3166120][end:3172570]] How would you have told that history or how does that history reflect on the areas that you're familiar with?

52:54 _Ander:_
[[start:3174380][end:3176890]] Well, I don't think I have much to add.
[[start:3178860][end:3183176]] I've been mainly interested in the weak rotation part.

53:03 [[start:3183278][end:3187020]] I'm excited to hear more about that, Chris.
[[start:3188240][end:3192620]] But no, I found this to be a very nice summary.
[[start:3193040][end:3208710]] I'm less familiar with the staff on computation, formal computation, despite being a mathematician by training, it was a little more familiar with all the physics stuff, but yeah, I thought it was great.

53:29 _Chris:_
[[start:3209400][end:3210436]] Thank you.
[[start:3210618][end:3211508]] All right.

53:31 _Daniel:_
[[start:3211674][end:3212244]] Thank you.
[[start:3212282][end:3213396]] I will close it.
[[start:3213418][end:3216320]] So in about two weeks, we'll have the first discussion.
[[start:3216400][end:3218272]] Everyone's welcome to join.
[[start:3218416][end:3222996]] I will share with Honor and Chris the questions, and we can develop that.

53:43 [[start:3223018][end:3227584]] And we'll have that on the course, front end before the coming discussion.
[[start:3227712][end:3229344]] So thanks again, fellows.
[[start:3229392][end:3230500]] See you next time.

53:50 _Chris:_
[[start:3230650][end:3231540]] Bye.
