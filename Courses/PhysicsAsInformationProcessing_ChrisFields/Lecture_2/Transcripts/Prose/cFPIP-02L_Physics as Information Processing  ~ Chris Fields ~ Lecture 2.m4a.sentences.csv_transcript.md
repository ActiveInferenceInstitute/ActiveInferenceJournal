
00:07 _Daniel:_
[[start:7800][end:8870]] Hello, everyone.
[[start:9320][end:12148]] It's June 15th, 2023.
[[start:12314][end:19280]] We are here in lecture two of Chris Field's course: Physics as Information Processing.
[[start:19360][end:19700]] So,

00:19 [[start:19770][end:21040]] Thank you, Chris.
[[start:21200][end:23460]] Looking forward to the lecture.

00:25 _Chris:_
[[start:25240][end:26660]] Thank you, Daniel.
[[start:27160][end:29380]] And, yes, welcome to this session.
[[start:29840][end:30492]] How?

00:30 [[start:30626][end:34300]] This section is titled "Why Quantum Physics?".
[[start:35440][end:54560]] And, if you will recall, from the first session, we reviewed the History of Physics and some of the History of Mathematics and Computer Science, from the end of the 19th century through to the beginning of the 21st century.
[[start:55400][end:90808]] And, we discussed the slow development from classical thermodynamics of Quantum Information Theory and specifically we characterized Quantum Information Theory as a new kind of physics that describes systems that are exchanging finite amounts of discretely encoded information across some intervening boundary.

01:30 [[start:90984][end:112928]] And so we use this very conventional graphical notation of two agents or physical systems, Alice and Bob (A and B), that are exchanging energy and information across some boundary.
[[start:113104][end:120680]] And I always use a blue ellipse like this to indicate the boundary that separates Alice from Bob.

02:01 [[start:121500][end:128884]] And this new approach to physics is entirely topological.
[[start:129012][end:130840]] It's not geometric.
[[start:131360][end:140620]] So, it doesn't assume a particular background spacetime. So, it doesn't assume that Alice and Bob are spatially separated.
[[start:141920][end:159844]] And, so, this makes it a very different kind of theory from Classical Information Theory in that the channel that separates Alice from Bob, this boundary, is a boundary in state space.

02:40 [[start:160042][end:164612]] It's not a boundary in some geometric embedding space.

02:44 [[start:164666][end:173880]] And, in particular, it's not a boundary or a channel that's embedded in a three-dimensional space that separates Alice from Bob.
[[start:175500][end:194770]] So, that's what we talked about last time. And today, what I want to discuss is how Quantum Theory in particular makes this idea of physics as a theory of communication simple and obvious.
[[start:196260][end:211590]] And, Quantum Theory, of course, has a terrible reputation of being abstruse and mathematically incredibly complicated and counterintuitive and difficult to understand.
[[start:212520][end:224490]] And, this is one quotation among many from leading physicists pointing out that quantum mechanics is just difficult.

03:45 [[start:225900][end:239580]] And, as you probably know, there's an entire philosophical industry of interpretations of Quantum Theory that try to make sense of its ontology.

04:02 [[start:242900][end:248720]] And so, what I don't want to do today is try to introduce quantum mechanics.
[[start:250340][end:253730]] We're not doing any of this.
[[start:254740][end:264660]] Some of you will recognize this as the table of contents, the first part of the table of contents of the famous textbook by Landau and Lifshitz.
[[start:265080][end:266004]] How that?
[[start:266042][end:275930]] If you've studied Quantum Theory in undergraduate or graduate school, you've probably dealt with a textbook structured much like this one.

04:36 [[start:276300][end:294530]] And, you've probably been introduced to quantum mechanics as it was traditionally conceived: as essentially a mechanical theory, a theory of motion, with wave functions and particle representations, and on, and on, and on.

04:54 [[start:294980][end:297264]] So, we're not going to try to do that
[[start:297382][end:318810]] (this). What we're going to do instead is take a completely information theoretical approach, and we're going to characterize information transfer in a quantum theoretical way without any assumptions about mechanics or spacetime or any of that.
[[start:319500][end:323770]] So, instead of this, we're going to ask a simple question.
[[start:325580][end:331788]] By a simple question, I mean a question with just a "yes-no" answer or a binary answer.

05:31 [[start:331874][end:336670]] So, let's use "up or down" as our example question.
[[start:338160][end:341070]] And, to ask this question, we need three things:
[[start:342340][end:343932]] First, we need an action.
[[start:343996][end:346290]] We need a way of asking it.
[[start:347860][end:351730]] For example, making a sound or writing something down.

05:53 [[start:353860][end:359030]] Second, we need a thing that we can ask the question of.

06:00 [[start:360040][end:373930]] We need an environment or a friend or the rest of the world or an experimental apparatus or some system or other that we're going to act on to ask this question.
[[start:375100][end:381100]] And, the third thing that we need to ask this question is a shared language.
[[start:381520][end:389100]] And, it's the shared language that's often neglected in models based on physics.
[[start:390880][end:396300]] And, I think the importance of the shared language became clear in Classical Information Theory.

06:36 [[start:396460][end:400572]] And, it's become clear again, of course, in Quantum Information Theory.
[[start:400716][end:404080]] But this has only happened over the last few decades.
[[start:404840][end:418664]] So, what I want to do today is to construct in a step-by-step fashion a formal representation of these three things that we need to ask a simple question.
[[start:418862][end:424628]] And, what we'll find is that that formal representation is, in fact, Quantum Theory.

07:04 [[start:424724][end:435436]] So, it's the Quantum Theory that provides us with a formal representation of asking these simple binary questions.

07:15 [[start:435618][end:441950]] And of course, if you can ask a binary question, you can ask any finite number of binary questions.
[[start:442420][end:455670]] So, you can construct an arbitrarily complex, finite decision tree that ends up formulating an arbitrarily complex but still finite question.
[[start:456040][end:462870]] So, this really is a general model of communicative interactions between agents.

07:45 [[start:465240][end:472104]] So, let's go about this. And, talk first about the action of asking you a question.
[[start:472222][end:488030]] And, so, the first thing I want you to do is actually say out loud "up or down?". Actually, ask a question, and then note two things about what just happened.

08:09 [[start:489440][end:493856]] The first thing to note is that it took some time to do that.
[[start:494038][end:503970]] That action actually required a finite amount of time, a couple of seconds, not very long, but it's not zero.
[[start:504740][end:507590]] It always takes time to ask a question.

08:28 [[start:508440][end:514870]] And the second thing to note is that it took energy to actually say "up or down".
[[start:515400][end:520650]] It requires a little bit of exertion to ask a question.
[[start:521660][end:526920]] So, let's put those two together and define a word.
[[start:526990][end:533596]] We're going to define the word "action" to mean some energy that's been spent in some time.
[[start:533778][end:544944]] So, asking a question is an action and it qualifies as an action because it requires spending some energy in some finite amount of time.

09:05 [[start:545142][end:549170]] And, so, we can write this as: action equals energy times time.

09:09 [[start:549540][end:553730]] Or I'll sometimes use the abbreviation E times T.

09:16 [[start:556100][end:571736]] And, action is always required when there's some inter-action or two-way-action between systems.
[[start:571848][end:583330]] So, whenever we talk about physical interaction, we're always talking about two systems doing something to each other that requires both energy and time.
[[start:584980][end:588220]] So, let's define another concept.
[[start:588300][end:595750]] A concept of a minimum action needed to ask a question, and, specifically, a question with a binary answer.
[[start:597000][end:601696]] And, we'll just pick a symbol to stand for that minimum action. STOPPED HERE

10:01 [[start:601888][end:605590]] And the symbol we'll use because it's conventional is h.
[[start:606200][end:629260]] And it turns out that this h is planck's constant, the number that planck came up with when he was trying to solve the black body problem back in 1900 that we talked about last time and recall, that was the problem of characterizing, the spectrum of radiation emitted by some physical system.

10:29 [[start:629330][end:630430]] That was hot.
[[start:630800][end:633920]] How much energy comes out as a function of temperature.
[[start:634660][end:642304]] And if you assume that the spectrum of energy coming out is continuous, you get predictions that are wrong.

10:42 [[start:642502][end:658824]] And Planck got predictions that were correct by assuming that that spectrum was discrete and that this h represented the minimum amount of energy that could be emitted in a particular time.
[[start:658942][end:663400]] So it represented the minimum energy times time or action.
[[start:663980][end:666490]] So let's look at an example of that.
[[start:667500][end:669976]] And here's an example that may be familiar.
[[start:670088][end:673310]] It's the example of your own visual system.

11:14 [[start:674640][end:695750]] So in the retinal, the cells of your retinas, there are many, many molecules that are rodoxins of one variety or other that respond to different wavelengths of visible light, and they have some efficiency for capturing light.

11:36 [[start:696280][end:703430]] And let's just assume that they're optimally efficient, that they're as efficient as they could possibly be.
[[start:704200][end:727372]] And that means that they require the minimum amount of energy to change shape, which is what they do when they're impacted by Light to capture the energy and hence the information that's available in the Light and the minimum energy to do anything that records one bit of information.
[[start:727506][end:728796]] So yes or no?
[[start:728898][end:732112]] Up or down is 0.7.

12:12 [[start:732166][end:739760]] So log two of Boltzman's constant times the temperature.
[[start:741060][end:744370]] And again, we saw this last time.
[[start:745080][end:760340]] This is from roughly 1875 and was then built into classical information theory by Shannon and then by Landauer in the mid 20th century.

12:40 [[start:760680][end:769720]] So what we're doing is assuming that since rudopsin is optimally efficient, all it requires is this amount of energy to change shape.
[[start:770300][end:775944]] And it's known experimentally, that rhodopsin takes about 200 femtoseconds to change shape.

12:55 [[start:775992][end:779436]] So that's 200 times ten to the -15.
[[start:779538][end:780392]] Seconds.
[[start:780536][end:784320]] So it's a very very fast reaction, chemical reaction.
[[start:785140][end:807910]] So we can just calculate what the action is and at 37 degrees centigrade so human body temperature KT is about 4.3 times ten to the -21 Joule and Joule is just a standard unit of energy and so we can multiply everything together.
[[start:809800][end:811992]] KT times zero seven times.

13:32 [[start:812046][end:825260]] This response time of 200 femtoseconds multiplied together gives you an action of about six times ten to the -34 joule seconds.

13:45 [[start:825840][end:836604]] And if you're familiar with quantum mechanics, you'll instantly recognize that number because it's very close to the value of Planck's Constant, which is 6.6 times.
[[start:836642][end:837792]] Ten to the -34.
[[start:837846][end:838780]] Joule seconds.
[[start:838860][end:842720]] So this says that Rhodopsin is very near to optimal.

14:05 [[start:845480][end:850736]] The best it would be able to do would be Planck's constant.
[[start:850848][end:854180]] That's the minimum action that can be undertaken.
[[start:855720][end:859290]] So Rodobson is clearly doing very well.
[[start:860220][end:868840]] It can't be as efficient as we're assuming it to be, but it's pretty efficient.
[[start:869180][end:877868]] So this number Planck's constant is and this idea of a minimum action is not something we just pulled out of the air.

14:38 [[start:878034][end:880216]] It's something that one can observe.
[[start:880328][end:888290]] When you're looking at what real biological systems in particular do and other physical systems do.

14:49 [[start:889860][end:897380]] So let's think about the second component of this project of asking a question.
[[start:897450][end:899830]] And that's the thing to be asked.
[[start:900840][end:903348]] And we want to ask a very simple question.

15:03 [[start:903434][end:906870]] We want to have a theory of asking very simple questions.
[[start:907340][end:915290]] So let's define the simplest thing that we can ask a binary question to.
[[start:915660][end:923484]] And let's say this is the thing that we can ask a binary question of using just this minimum action h.
[[start:923682][end:930030]] So we're going to ask for the minimal thing that it's possible physically to ask a question of.
[[start:930560][end:934160]] And this thing needs a name, so let's call it a qubit.

15:34 [[start:934740][end:938210]] And that word is a contraction of Quantum bit.
[[start:939300][end:940832]] And we can draw it like this.
[[start:940886][end:943104]] A little sphere with an arrow through it.
[[start:943222][end:945380]] That's called a block sphere.
[[start:946040][end:947504]] And we use a symbol.

15:47 [[start:947552][end:948244]] Q.
[[start:948442][end:957556]] And that notation with the bar and the angle bracket is called a bra notation.

15:57 [[start:957668][end:960228]] And it originates with Durac.
[[start:960404][end:972350]] So it's a traditional way of writing inner products, actually, in quantum theory to indicate the state of Q.
[[start:973360][end:980556]] So this thing called a qubit only responds to binary questions.

16:20 [[start:980738][end:983776]] So it clearly can have only two states.
[[start:983878][end:987410]] The state that answers yes and the state that answers no.
[[start:987860][end:989440]] And conventionally.
[[start:989780][end:993344]] We draw the arrow going up if the answer is yes.
[[start:993382][end:996308]] And the arrow going down if the answer is no.

16:36 [[start:996474][end:1003350]] And so those are the two states that the qubit can be in when it's answered a question.
[[start:1004520][end:1011480]] So now let's draw a picture for the act of asking a question of q in the state.
[[start:1011550][end:1011832]] Q.
[[start:1011886][end:1013530]] And let's draw it like this.
[[start:1015180][end:1021596]] This curvy arrow is the action of asking the question and getting the answer back.

17:01 [[start:1021778][end:1025740]] And we're asking it of this minimum system, the qubit.
[[start:1026240][end:1038080]] And let's call this entire act of h and write h acting on Q by this expression HQ.
[[start:1038660][end:1048660]] So again, we're developing the notation of quantum theory, which all of you who know the theory already will find familiar.

17:30 [[start:1050680][end:1058360]] So the third thing that we have to build into this picture and into the theory is the shared language.
[[start:1059740][end:1068810]] So we have to know what we mean by up or down if we're going to ask the question up or down?
[[start:1070000][end:1080110]] And we have to have some representation of what it means for the qubit to distinguish up or down.
[[start:1080560][end:1094560]] So let's say that to us, up and down mean this little diagram with an arrow that's labeled up on one end and down on the other end.

18:14 [[start:1094710][end:1100048]] So we're defining up and down in a very simple way as just opposites.

18:20 [[start:1100144][end:1103888]] We don't know anything else about them except that they're opposites.
[[start:1104064][end:1107412]] So this is a stripped down one bit question.
[[start:1107546][end:1110296]] We could have called them one and minus one.
[[start:1110478][end:1112312]] We could have called them A and B.
[[start:1112366][end:1113930]] We could have called them anything.

18:34 [[start:1114860][end:1120460]] We're just indicating that up and down are two opposing concepts.
[[start:1121200][end:1133760]] And so this object that we've used to make this definition of the relationship between our two words up and down is called a reference frame.
[[start:1135220][end:1143120]] It's a physical object that encodes a concept or a meaning.
[[start:1144120][end:1165160]] And if you think about using language, using English, for example, you can understand me speaking in English because your brain has the right sorts of neural circuits to allow you to understand English and produce English using your hand in your mouth.

19:25 [[start:1165820][end:1174616]] And those neural circuits are reference frames in your brain for understanding and producing English.

19:34 [[start:1174728][end:1178270]] And they encode the relationships between different words.
[[start:1179600][end:1183040]] So you all know about Chat GPT.
[[start:1183540][end:1201940]] You can think of all of the weights on all of the ten to the 19th or however many parameters there are in GPT four as a reference frame that describes the relationships between words and phrases in English and many other languages.
[[start:1202280][end:1214452]] So this idea of a reference frame is an instance of Landauer's principle, which is often summarized as saying that information is physical.
[[start:1214596][end:1228700]] What that means is that information always has to have some encoding and that encoding, that object can always be thought of as a reference frame.

20:29 [[start:1229840][end:1231950]] So let's put all this stuff together.

20:34 [[start:1234100][end:1240208]] What we have now is a reference frame that defines the difference between up and down.
[[start:1240374][end:1251110]] We have an action that we've labeled H, and the action acts on this object, the qubit, which is in some state.
[[start:1252520][end:1256900]] And what we've drawn here now is an experiment.
[[start:1257660][end:1268324]] And you can think of the incoming part of the arrow that goes from the reference frame to the qubit as a preparation of the qubit.
[[start:1268452][end:1280590]] So you can think of it as I'm doing something to the qubit to put it in a particular state like up, because that's the state I want it to be in.

21:21 [[start:1281680][end:1290930]] And I can think of this returning part of the arrow as a measurement of the state that the qubit is actually in.

21:31 [[start:1291460][end:1302930]] So if the qubit is actually in this state with the arrow pointing up, then I'm going to get back the answer up when I act on the qubit to measure its state.
[[start:1304420][end:1328556]] So now we can recognize this action, H as the Hamiltonian operator in quantum theory, which always takes some time, which we represent by an interval DT, to act on some state, and in particular this binary state, Q.
[[start:1328738][end:1335360]] So this whole picture depicts the action of a very simple Hamiltonian operator.

22:17 [[start:1337380][end:1346070]] And again, I want to emphasize that we've just defined the qubit as the simplest thing that we can ask a binary question of.

22:28 [[start:1348920][end:1351110]] So how does this H work?

22:32 [[start:1352840][end:1361450]] We can use H to prepare this qubit in one of two states, which we're going to label one and minus one.
[[start:1362140][end:1375292]] The state one corresponds to the up direction, and the state minus one corresponds to the down direction, and doing this to Q.
[[start:1375426][end:1382288]] So preparing Q in one of these two states takes energy, and we know how much.
[[start:1382454][end:1394556]] Boltzman told us back in 1875 that the minimum energy to reduce the entropy of the universe by one bit is log two of KT.

23:14 [[start:1394748][end:1398720]] We saw that earlier when we were thinking about Rhodobson.
[[start:1399240][end:1409864]] So we can say that acting with H always requires some number times KT, where that number is bigger than the log of two.
[[start:1409982][end:1431612]] Remember, the log of two is just in there to get units of bits of binary questions, as opposed to units of nats, which are questions that have e answers, where E is the exponential base, the natural exponential base.

23:51 [[start:1431746][end:1437010]] But we want to use units of bits, so we have to always have this factor of log two.
[[start:1438500][end:1442480]] So this lets us write H in a particular way.

24:02 [[start:1442550][end:1452900]] We can take out this energetic term that Boltzman tells us we have to include beta times KT.
[[start:1454040][end:1462868]] And what's left over is, in a sense, the pure representation of the action, stripping out the energy requirement.
[[start:1463044][end:1472380]] And we're going to call that M, because M is the standard symbol to use in quantum theory for a measurement operator.
[[start:1473520][end:1476552]] And M is now dimensionless.
[[start:1476696][end:1487712]] H has units of energy, KT is an energy, and M has no units at all.

24:47 [[start:1487846][end:1490290]] So it's H without the energy.
[[start:1491300][end:1505220]] So now we can ask, what is this operator M that we've defined as the simplest possible action on a qubit, but abstracting away the amount of energy that we have to use to act on the qubit.

25:06 [[start:1506200][end:1512490]] Well, what M does is just encode a bit or decode a bit.
[[start:1513740][end:1520760]] So we can use this operator M to say, I want Q to have the value one.
[[start:1520910][end:1530030]] I want it to be up, so I can sort of reach out with my operator M and grab Q and turn it so that its arrow is pointing up.

25:31 [[start:1531600][end:1534332]] And that's the operation.
[[start:1534396][end:1536284]] That's called preparation in physics.
[[start:1536332][end:1539644]] It's what it means to prepare an experimental apparatus.
[[start:1539692][end:1548070]] For example, you actually grab hold of the apparatus, and you twist some knobs and flick some switches to prepare it to be in some state.
[[start:1549320][end:1554160]] And you can use M to measure a state that isn't known.

25:54 [[start:1554320][end:1565290]] So I can use M to grab a hold of Q and look at it and determine whether it's in state one or minus one.
[[start:1566140][end:1574940]] And I can represent these as just a cycle that starts with measuring and then prepares, or that starts with preparing and then measuring.

26:15 [[start:1575840][end:1589052]] And if I represent it that way, what I see is M having a value which is either the value I want to encode or the value that I have measured.
[[start:1589196][end:1603510]] And Q and M acts on that value and Q to produce a particular state of Q, to put Q in a particular state, or to realize that Q is in that state.
[[start:1604840][end:1613000]] And so M is actually an identity acting on some value and Q.

26:53 [[start:1613150][end:1624664]] So it maps one in Q to one in Q, and it maps minus one in Q to minus one in Q if you do the whole cycle of preparation and then measurement.
[[start:1624792][end:1625852]] And that makes sense.
[[start:1625906][end:1639024]] It's actually an axiom in some formulations of quantum theory that if I measure the state of some object, what I'm doing is also preparing it in that state.

27:19 [[start:1639142][end:1643010]] So if I immediately measure it again, I'll see the same value.
[[start:1644580][end:1646512]] And that makes sense physically.

27:26 [[start:1646576][end:1655540]] If I put my coffee cup on the table and then I look for it, it's likely going to be on the table unless something else intervenes.
[[start:1656200][end:1657464]] Well, what does this mean?
[[start:1657502][end:1660280]] It means that we can do a little bit of algebra.

27:42 [[start:1662860][end:1680670]] It means that we can write this original expression of acting on Q with our Hamiltonian in this somewhat more explicit form of using the energy beta KT and our operator M on Q.
[[start:1681540][end:1687890]] And what I get out of that is the energy beta KT multiplied by Q.

28:10 [[start:1690020][end:1693360]] So HQ equals EQ.
[[start:1694200][end:1696180]] That's the Schrodinger equation.
[[start:1696520][end:1700016]] So that's one of the central equations of quantum theory.

28:20 [[start:1700208][end:1707450]] What it says is that this operator, H, is the total energy operator on a system.
[[start:1707980][end:1712344]] Its eigenvalues are the total energies of the system.

28:32 [[start:1712542][end:1723576]] And we can now see where that energy is coming from in this very, very simple, stripped down kind of representation of an action.
[[start:1723768][end:1732930]] The energy is the thermodynamic energy that has to be spent to determine one binary outcome up or down.
[[start:1734900][end:1746500]] Now, if you're familiar with quantum mechanics, you will have seen exponentiated operators like the next line here of algebra.
[[start:1748120][end:1762420]] This operator P, which is time dependent and which is the exponential of H multiplied by it over H bar, is called the propagator.

29:22 [[start:1762500][end:1770190]] It's the unitary operator in quantum theory, the operator that conserves probability or conserves information.

29:32 [[start:1772080][end:1785730]] And so, using the representation of H as beta KT, we can see that this operator P is just E to the minus beta M.
[[start:1787460][end:1803540]] If we recall the WIC rotation from the first session, this strange equivalence of it over H bar with one over KT that wasn't discovered until 50 years after the invention of quantum theory.
[[start:1805000][end:1809960]] And it's still a very debated thing.
[[start:1810030][end:1813850]] I mean, people worry about what this equation really means.
[[start:1814540][end:1836690]] But one thing that it means in this setting where H has this particularly simple form is that the propagator is now just the exponential of a number multiplied by this very simple strip down operator that encodes a bit or decodes a bit.

30:38 [[start:1838020][end:1842480]] But we know something about the exponential propagator just by looking at its form.
[[start:1842630][end:1848740]] If you're again familiar with these sorts of exponential operators, you know that they're wave equations.
[[start:1849720][end:1854608]] And we can make sense of that using the diagram up above.
[[start:1854784][end:1859160]] What M is doing is just performing a cycle.
[[start:1860220][end:1867850]] It's just mapping one and Q back to itself, or minus one and Q back to itself.

31:08 [[start:1868620][end:1884290]] So we can think of M as just taking this object and flipping it back around until it gets itself again.
[[start:1885860][end:1894608]] And that kind of cycle can always be turned into a wave equation and e to the I over H bar times.
[[start:1894694][end:1903524]] HT is a canonical form of a wave equation, where the horizontal axis here on the wave is time.

31:43 [[start:1903722][end:1917370]] Or if you look at the little cycle that I've drawn as a circle with an arrow, it's the time of the thing spinning around like this, which is exactly the same thing as a wave traveling through time.
[[start:1918540][end:1921070]] So that tells us something very important.

32:02 [[start:1922240][end:1929340]] It tells us that this equivalent expression, e to the minus beta M, is also a wave equation.
[[start:1929920][end:1937170]] So it tells us that this operator M has built into it some sense of time.

32:19 [[start:1939540][end:1943760]] It's the sense of time of this prepare measure cycle.
[[start:1944820][end:1948112]] And that's implicit in m right.
[[start:1948166][end:1958170]] We've used the WIC rotation to get rid of what I'll end up calling the external time t, the objective time T.
[[start:1959340][end:1971420]] And we'll see in July where this internal time comes from in terms of the WIC rotation.

32:52 [[start:1972160][end:1977948]] But we can say now that it's an agent specific time.

32:58 [[start:1978114][end:1992770]] It's an internal time reference frame that's built into our idea of this system, Alice, that can act on the world, and it represents the time that's required to ask this question.

33:14 _Ander:_
[[start:1994280][end:1997716]] Okay, can I ask a question at this point?

33:17 _Chris:_
[[start:1997898][end:1998630]] Yes.

33:19 _Ander:_
[[start:1999240][end:2004260]] So on this slide with the operator M, I'm curious.
[[start:2004600][end:2011240]] How can the agent deploy in the operator M tell the difference or break the symmetry between preparation and measurement?

33:32 [[start:2012060][end:2015000]] Or are they just completely dual pictures?

33:36 _Chris:_
[[start:2016060][end:2017572]] Yeah, they're completely dual.
[[start:2017636][end:2021720]] So the agent never breaks the symmetry.
[[start:2021800][end:2027340]] The agent can't actually distinguish the act of preparing from the act of measuring.
[[start:2028640][end:2032988]] Every preparation is a measurement, and every measurement is a preparation.

33:53 _Ander:_
[[start:2033164][end:2033890]] Right.

33:54 _Chris:_
[[start:2034340][end:2046310]] That's, in fact, what this axiom of unitarity measuring a state leaves the particle in the measured state means.

34:06 _Ander:_
[[start:2046760][end:2047510]] Right.

34:09 _Chris:_
[[start:2049800][end:2052180]] So, yeah, mathematically, they're duals.

34:13 _Ander:_
[[start:2053320][end:2054230]] Thank you.

34:17 _Chris:_
[[start:2057420][end:2064360]] Okay, so let's now use this theory that we've developed to describe the interaction between Alice and Bob.
[[start:2064940][end:2079150]] And let's think of a situation in which Alice prepares a qubit that Bob then measures, and then Bob prepares the very same qubit, and then Alice measures it.
[[start:2079680][end:2090720]] So Alice acts with her Hamiltonian operator, which we'll label Ha, and Bob acts with his Hamiltonian operator that we label HB.
[[start:2092020][end:2097030]] And let's say that Alice prepares the qubit as in state up.
[[start:2097800][end:2104870]] And Bob can then measure the qubit in state up and say, oh, the qubit is now up.

35:05 [[start:2105720][end:2117368]] And if Bob then prepares the qubit in state down, alice can measure the qubit in state down and say, oh, the qubit switched from the up that I prepared to down.

35:17 [[start:2117454][end:2119950]] So Bob must have prepared it as down.
[[start:2120880][end:2122590]] So what's happened here?
[[start:2123920][end:2128700]] Alice and Bob have actually shared a bit flip.
[[start:2130480][end:2137650]] Alice said up and Bob said, down, and Alice heard him say down.

35:38 [[start:2138100][end:2143890]] So they've shared this idea of change by interacting with each other.
[[start:2144680][end:2149510]] Now, this works as long as they mean the same thing by up and down.
[[start:2150040][end:2160730]] So we've implicitly assumed, in talking about them communicating, that they both have this reference frame that distinguishes up from down.
[[start:2162220][end:2170876]] And this is actually a completely general model of what I'll call a noiseless one qubit channel.
[[start:2171058][end:2172636]] Now, what does that mean?

36:12 [[start:2172818][end:2177692]] It's noiseless because there's nothing else in the picture, right?

36:17 [[start:2177746][end:2183112]] There's nothing in the picture that can jiggle the qubit when Alice and Bob aren't looking.
[[start:2183186][end:2190604]] Alice and Bob are the only systems we're talking about, and they share this qubit and there's nothing else in the picture.
[[start:2190652][end:2202944]] So there's no kind of third party or environment or heat bath or anything like that that's going to mess with the qubit and disrupt their interaction.
[[start:2203072][end:2215210]] So that's a noiseless channel and it's a one qubit channel because they just have one qubit that they're interacting with and they're alternately preparing and measuring its state.

36:56 [[start:2216620][end:2223100]] Now, clearly, if they can interact using one qubit, they can interact using any finite number of qubits.
[[start:2223760][end:2236240]] So here's a picture of an in qubit channel that Alice and Bob, which here I've labeled A and B because I took this figure from a paper, are sharing.
[[start:2236900][end:2245330]] And Alice and Bob both have N operators, one for each of the N qubits that they share.

37:25 [[start:2245700][end:2250192]] And they just do this prepared measurement cycle on all N qubits.
[[start:2250256][end:2264180]] So you can think of Alice preparing the N qubits, bob measuring the N qubits, and then Bob preparing and Alice measuring, and that allows them to exchange N bit messages.

37:44 [[start:2264340][end:2267048]] And we can make N as large as we want.
[[start:2267214][end:2272060]] And so they can exchange messages of arbitrary complexity.
[[start:2272640][end:2281580]] And if they share the meaning of up and down, then they can exchange these messages with no noise, so they can communicate.
[[start:2282260][end:2294050]] And we now have our theory of two communicating agents that are that are sharing arbitrary finite information.
[[start:2295240][end:2302550]] Now, I've labeled Q one through QN in this picture, a holographic screen.

38:23 [[start:2303080][end:2306150]] And in fact, that's exactly what it is.

38:27 [[start:2307900][end:2313000]] Recall from session one this slide illustrating the holographic principle.

38:36 [[start:2316540][end:2321470]] Shannon made this point that a bit of information is an answer to a yes no question.
[[start:2322320][end:2327916]] And so we can write down a number of possible states.
[[start:2328018][end:2330220]] We can write down an entropy.
[[start:2331940][end:2338844]] And the limiting case of that entropy is the entropy of a black hole.
[[start:2338972][end:2349300]] The densest possible encoding of information in space or on a boundary.

39:10 [[start:2350520][end:2360040]] And this holographic principle allows us to see any boundary, as we discuss in session one, as an encoding of bits.
[[start:2360700][end:2368010]] So the previous boundary of these in qubits, we can think of as a holographic screen.

39:28 [[start:2368960][end:2371310]] Now, why is that important?

39:34 [[start:2374640][end:2402608]] It's important because it allows us to use this idea of holography and this idea of a fixed encoding of a message or a fixed encoding of an observable entropy at some density that was developed in cosmology to talk about arbitrary quantum communication channels.
[[start:2402704][end:2414890]] So we can import a whole bunch of theory that was done someplace else into quantum information theory and see that it works perfectly because it describes exactly the same situation.
[[start:2416620][end:2418410]] Now, what does this tell us?
[[start:2419840][end:2431340]] Philosophically, it tells us that Alice and Bob can learn about each other at most N bits per communication cycle.

40:32 [[start:2432740][end:2443250]] So the maximal amount of information that they can get from an observation is the in bits that the other one wrote on the screen.

40:45 [[start:2445240][end:2464200]] So this tells us something very important, that when an agent is looking at their environment, which is this other agent, Bob, the amount of information that can be extracted from the environment is actually proportional to the size in bits of the boundary.
[[start:2465260][end:2470910]] And the holographic principle just makes that size finite in space.
[[start:2471440][end:2480190]] And I said early on that there's no embedding spacetime in this theory, that Alice and Bob are not thought of as separated in space.
[[start:2480960][end:2491360]] But as soon as we use the holographic principle, we can think of the boundary between them as having a spatial coordinate, even though they don't have a spatial coordinate.
[[start:2492100][end:2519880]] So we'll get back to this point in September when we talk about theories of emergent spacetime, but all of these theories of emergent spacetime come back to this idea that boundaries can have spatial extent, even though the systems that they separate don't have any natural spatial description or natural spatial degrees of freedom.

42:02 [[start:2522480][end:2528270]] Okay, so now let's recall another picture from session one.

42:10 [[start:2530640][end:2557370]] We talked a little bit about Feynman's theory of scattering and the origin of Feynman diagrams and the idea that if Alice prepares some system in some initial state and then measures the state later, if we want to calculate what the new state is.
[[start:2558140][end:2568760]] We have to take into account all of the possible paths that join the initial state that Alice prepared to the final state that Alice measured.
[[start:2570000][end:2572110]] So what does that mean?
[[start:2572560][end:2586770]] I mean, here effectively, if we think of suppose I'm Alice and the boundary is my screen, I'm talking to the screen, and then later on, I'm going to measure the screen.

43:07 [[start:2587380][end:2595510]] And between my preparation actions and my measurement actions, a bunch of stuff happens on the other side of the screen.

43:16 [[start:2596760][end:2605444]] And if I want to predict what's going to happen on the other side of the screen, I've got to take into account every possible thing.
[[start:2605482][end:2606630]] That could happen.
[[start:2608040][end:2613656]] And I have to give some weight to those possible things that could happen.
[[start:2613758][end:2625870]] And Quantum theory, in fact, tells you how to assign those weights to things that could happen in order to make a measurement, given some theory of the mechanism that makes things happen.
[[start:2627040][end:2632370]] But the fact that all of the paths have to be counted is what unitary evolution means.

43:53 [[start:2633060][end:2641570]] This evolution that preserves information that doesn't take any away, it doesn't add any, it just represents it in different ways.
[[start:2642100][end:2654470]] So if you look at this screen and imagine that Alice is interacting with her boundary and then she's interacting with her boundary again, it looks just like the previous screen.

44:14 [[start:2654840][end:2659800]] And the wavy red arrows are what's happening inside Bob.
[[start:2660540][end:2671630]] The wavy red arrows are a representation of what's going on inside Bob as he measures his side of the screen and then prepares his side of the screen.
[[start:2672320][end:2684370]] So what Feynman is representing here is just the action of the environment or the action of the system while Alice isn't looking.

44:44 [[start:2684980][end:2693040]] Between Alice's preparation stage and her measurement stage, while Bob is doing his measurement and preparation.
[[start:2693780][end:2696832]] So this diagram is actually completely symmetrical.
[[start:2696896][end:2704896]] We could have drawn an arrow where the wavy red things are and drawn wavy red things where we talked about Alice.
[[start:2705008][end:2708410]] And we'd have the same picture just from Bob's point of view.
[[start:2709260][end:2722830]] We can also think of this, of course, as Alice communicating with her future self by writing a memory record someplace in the world and then coming back and reading it.

45:23 [[start:2723680][end:2739650]] And if Alice writes a memory on the world and then comes back later on and reads it, she actually has to take into account some theory of all of the things the world might have done to her memory while she wasn't looking.
[[start:2741460][end:2746660]] So this picture of Feynman's actually tells us a lot about memory.
[[start:2747400][end:2762952]] And when we think about organisms running around in the world doing things like we do all the time, we tend to think of memories as things that are persistent and unchanging and all of that.
[[start:2763006][end:2764890]] But we know that that's not true.
[[start:2765340][end:2768730]] We know that memories degrade in various ways.

46:09 [[start:2769600][end:2781340]] We know that adversarial third parties can come and change what we've done so that they fool us into thinking that we've remembered something that we haven't.
[[start:2781700][end:2783600]] And so on and so forth.

46:24 [[start:2784260][end:2796740]] That whole picture of memory is actually encoded in this picture that Feynman drew in the late fifty S to represent scattering of particles.

46:40 [[start:2800680][end:2807030]] So what we've done here is started with this simple idea of asking questions.
[[start:2808060][end:2812164]] And we've actually constructed a fair amount of Quantum theory.
[[start:2812212][end:2816628]] We constructed the Schrodinger equation, we constructed the unitary propagator.
[[start:2816724][end:2824700]] We constructed the idea of a reference frame, which we'll talk about intensely next time in July.
[[start:2825760][end:2832370]] So we can sum this up by saying that Quantum theory simply is a theory of communicating agents.

47:13 [[start:2833300][end:2854704]] And that quantum mechanics, the theory that Feynman was complaining about in that earlier slide, that quantum mechanics generates this problem that seems intractable of how to understand measurement, because the theory is in fact about measurement.

47:34 [[start:2854832][end:2857690]] It's not about mechanical motion at all.
[[start:2858460][end:2862920]] So quantum theory actually tells us nothing about ontology.
[[start:2864300][end:2875912]] And this is why the interpretations of quantum theory, the many worlds interpretation, where you have all these branching universes and so forth, are not really science.
[[start:2875976][end:2877112]] They're philosophy.

47:57 [[start:2877176][end:2885788]] They're attempts to understand an ontology that's generated by a theory that doesn't talk about ontology.
[[start:2885884][end:2888850]] It talks about communication between agents.
[[start:2889780][end:2892528]] But we've left something very important out.
[[start:2892694][end:2900070]] We've left out a consideration of what happens when Alice and Bob don't mean the same thing by up and down.
[[start:2900760][end:2910136]] And we've left out the famous phenomenon of entanglement spooky action at a distance, as Einstein called it.

48:30 [[start:2910238][end:2914680]] And it turns out these things that we've left out are very, very closely related.

48:36 [[start:2916060][end:2919604]] And we're going to see why in July.
[[start:2919732][end:2922604]] But I'm going to give you a brief preview now.
[[start:2922802][end:2928284]] So what happens when Alice and Bob actually mean different things by up and down?
[[start:2928482][end:2931660]] What if their reference frames aren't aligned?

48:52 [[start:2932880][end:2937680]] Well, the first thing to note is that nothing in the theory says they have to be aligned.
[[start:2938180][end:2941490]] So we have to consider the possibility that they're not.
[[start:2942420][end:2949040]] And in fact, both Alice and Bob have to have what's called free choice of reference frame.
[[start:2949200][end:2957560]] When Alice prepares her instrument, she has to be able to prepare it any way she wants to in order to do an experiment.
[[start:2959020][end:2971710]] And when Bob makes up a sentence to tell Alice, he has to be able to choose any language he wants to use, he's a free agent in this way.

49:32 [[start:2972080][end:2975544]] And if they don't have that freedom, it turns out they're entangled.
[[start:2975672][end:2981900]] So reference frame, nonalignment and entanglement are very, very closely coupled.

49:44 [[start:2984420][end:2991120]] Now, misalignment of reference frames is what produces superpositions of outcomes.
[[start:2991940][end:3014776]] So if Alice makes her measurements with her up and down arrow arranged vertically, for example, but Bob prepares his qubit with his up and down arrow arranged at 90 degrees to Alice's, alice is not going to have any idea what Bob did.
[[start:3014958][end:3018820]] I mean, she can't see distinctions in the left right direction.
[[start:3018900][end:3022380]] She can only see distinctions in the up and down direction.
[[start:3022880][end:3025580]] So all she can do is flip a coin.

50:26 [[start:3026080][end:3036608]] If she wants to know what Bob prepared, it's 50% likely he prepared up for her what she calls one.
[[start:3036774][end:3041088]] And it's 50% likely that he prepared what's down for her.
[[start:3041174][end:3042370]] She can't tell.
[[start:3044040][end:3049744]] Now, if Bob's reference frame is pointing at about 45 degrees.

50:49 [[start:3049872][end:3057690]] So up for him means 45 degrees off of Alice's up, then she can sort of tell what he did.

50:58 [[start:3058300][end:3066010]] If he's pointing 45 degrees from up, then she's probably going to measure up.
[[start:3066460][end:3071230]] And if he's pointing 45 degrees from down, she's probably going to measure down.
[[start:3071600][end:3077420]] So her outcomes are 75% for one and 25% for minus one.
[[start:3077490][end:3081660]] If he prepares at this 45 degree angle.
[[start:3082260][end:3084624]] So we can write this in a particular way.

51:24 [[start:3084662][end:3106368]] We can say that the value that Alice gets acting with her M on a qubit that Bob prepared is some number times what she measures as up plus some other number plus times what she measures as minus one, where those numbers, the squares of those numbers, add to one.
[[start:3106554][end:3108344]] So why do they have to add to one?
[[start:3108462][end:3111720]] Well, they add to one because of the Pythagorean theorem.

51:54 [[start:3114300][end:3120540]] One is the distance, the total distance between the two outcomes.
[[start:3121360][end:3127740]] And A squared plus B squared are the other two sides of that triangle.
[[start:3128480][end:3146256]] So another way to think of it is that the metric distance in possibility space is one and A squared and B squared are just the Euclidean distance components.
[[start:3146288][end:3149936]] Again, Euclidean distance is based on the Pythagorean theorem.
[[start:3150128][end:3153060]] So this is the Born rule in quantum theory.

52:34 [[start:3154120][end:3162490]] It's the rule that tells us what happens when we're trying to measure a superposition and it tells us where these superpositions come from.
[[start:3164220][end:3170140]] We have a mismatch in reference frames between two agents that are communicating.

52:52 [[start:3172480][end:3189330]] So if we go back to the free energy principle, which is what this whole active inference class is about, and we formulate it in quantum theory, we get a very simple idea of what the free energy principle is.

53:09 [[start:3189940][end:3201910]] The FEP and quantum theory just says that interacting systems are going to behave in a way that aligns their reference frames and that makes their communication as good as it can be.
[[start:3203640][end:3217160]] But since aligning reference frames perfectly leads to entanglement, the free energy principle drives systems asymptotically toward entanglement.

53:39 [[start:3219360][end:3226540]] Well, the principle of unitarity says that all systems will approach entanglement asymptotically.
[[start:3226960][end:3232540]] So we can see the FEP is actually a classical statement of the principle of unitarity.
[[start:3233540][end:3249860]] And what we'll see in the next session is why this is the case, why active inference, when we think of it, quantum mechanically is a way of talking about the principle of unitarity, which is the deepest axiom of quantum theory.

54:10 [[start:3250840][end:3265320]] And we'll also see that this question of alignment becomes more and more complex as the complexity of the messages that the systems are trying to communicate to each other increases.
[[start:3266220][end:3270860]] And that message complexity correlates with system complexity.

54:31 [[start:3271440][end:3279950]] So that aligning complicated systems is very hard, although aligning very simple systems is fairly easy.
[[start:3280480][end:3293410]] And if you think about what's the simplest possible theory in science, it's particle physics, because you're dealing with these very simple things that interact in extremely simple ways.
[[start:3294120][end:3306752]] And the really difficult parts of science are things like sociology, where you're dealing with incredibly complicated systems like humans that interact in incredibly complicated ways.
[[start:3306906][end:3312250]] And all we have are very vague kind of folk theories of how that works.

55:13 [[start:3313180][end:3319370]] But we know from that example that aligning complex systems is extremely difficult.

55:21 [[start:3321580][end:3324030]] So humans don't get along very well.
[[start:3325600][end:3334610]] So the second session well, the second discussion section which Andrew will be leading is on Saturday, the 1 July, a couple of weeks from now.
[[start:3335540][end:3361780]] The third lecture session will be on July 13 and I hope you all will contribute to the interactive question and answer session on the web and show up for the discussion on Saturday, the 1 July and join us again in July for the discussion of quantum reference frames and reference frame alignment.
[[start:3361940][end:3363530]] So thank you very much.

56:08 _Daniel:_
[[start:3368970][end:3370470]] Thank you, Chris.

56:12 _Ander:_
[[start:3372170][end:3372790]] All right.

56:12 _Daniel:_
[[start:3372860][end:3374070]] Thank you all again.
[[start:3374140][end:3382002]] Please check out the course syllabus, ask questions through the site and see you at the discussion.
[[start:3382066][end:3383414]] See you next time.

56:23 [[start:3383612][end:3384262]] Thank you.
[[start:3384316][end:3384666]] Bye.
