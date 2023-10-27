
00:07 _Daniel:_
[[start:7500][end:9096]] Hello and welcome, everyone.
[[start:9198][end:10200]] Welcome back.
[[start:10350][end:22010]] This is the second interval of the third applied active inference symposium at the active inference institute on August 22, 2023.
[[start:23100][end:35628]] This is going to be another packed and exciting interval, and we're kicking it off with Jean Francois Cloutier, a Collective of theorizers First Steps.

00:35 [[start:35724][end:40572]] So, JF, thank you for joining and to you for this presentation.
[[start:40716][end:48116]] And if anybody has questions for this presentation or any of the others, please just put it in the live chat and I'll do it.
[[start:48138][end:48628]] I can.
[[start:48714][end:49536]] So thanks, JF.

00:49 [[start:49568][end:50310]] To you.

00:54 _JF:_
[[start:54900][end:56560]] Thank you, Daniel.
[[start:57800][end:65300]] I'm a software engineer at a company called Smart Rent, where I write software for smart home systems.
[[start:66120][end:73530]] I also work on a research project at the Active Inference Institute called the Robotics and Embodied Project.
[[start:74620][end:80650]] My current focus is unsupervised learning in active inference agents.
[[start:81840][end:100930]] In my presentation today, which is titled A Collective of theorizers First Steps, I'll first start with a brief recap of the project, then dive into recent progress, and then I'll conclude with what I see as the next steps of the project.

01:43 [[start:103780][end:111300]] Well, since 2017, I've been experimenting with Lego robots and models of cognition.
[[start:111880][end:121690]] I do this for my own education, because, like I think most of us, I understand something better when I build it.

02:02 [[start:122460][end:126776]] What you see here is my latest robot model.
[[start:126958][end:128276]] It's a rover.
[[start:128468][end:134780]] It has a whole bunch of sensors and a number of effectors actuators.

02:15 [[start:135360][end:142860]] As a matter of fact, those sensors and actuators can be understood as forming the marker blanket of my robot.

02:26 [[start:146330][end:156310]] Last year, I presented at the symposium about the history of the project, its then status, and its ambitions.
[[start:156730][end:164470]] I presented a cognitive model that implemented predictive processing from an active inference perspective.
[[start:164630][end:170006]] So there were generative models, there was predictions, there was prediction errors.
[[start:170198][end:187374]] And these generative models animated the robots so that they would roam, avoid obstacles, observe their companion, and also, in a very simplistic way, build a theory of mind of the other robot.

03:07 [[start:187502][end:207734]] They could from observations infer that the other robot had detected food, food being presented here as a sheet of paper on the floor, and then would kind of try to track the other robot to also get to the food and fun stuff like this.

03:27 [[start:207932][end:214006]] The implementation combined multi processing and functional computing.
[[start:214038][end:218250]] There was nothing probabilistic in the implementation.

03:40 [[start:220830][end:223114]] I thought maybe we'd see them in action.
[[start:223162][end:224574]] That's what's presented last year.
[[start:224612][end:232698]] But just to get a sense of what they do, I have two robots here, one named Karl and Andy.
[[start:232794][end:236290]] I named them before I knew I was going to present at the conference.
[[start:237350][end:243090]] So they benefited from a number of training sessions.

04:03 [[start:243510][end:253000]] They learned how to find which policies would achieve their goals better than others.

04:13 [[start:253370][end:256150]] And one here on the left.
[[start:256300][end:288850]] Found the food rather right away but got closer to the pedestal where the beacon is that simulates the scent of food feared was getting into a collision and then backs off in a hurry as we'll see the other robot observes all this, sees the robot backing off as being in a panic and decides to share this emotion and backs up as well.
[[start:289000][end:291540]] So fun stuff.

04:58 [[start:298180][end:306390]] From the beginning I've implemented different cognition models but they all have in common the fact that they implement a society of mind.
[[start:307160][end:308852]] So what is a society of mind?
[[start:308906][end:327710]] A society of mind is a concept by which the mind is not a monolithic structure but a composition of simple actors, independent actors that interact with each other in simple ways.

05:28 [[start:328480][end:334764]] That view of the mind was put forth by Marvin Minsky 50 years ago.
[[start:334802][end:336320]] So this is not recent.

05:40 [[start:340290][end:349434]] Again, what I presented last year was a society of mind containing a hierarchy of, I call them cognition actors.
[[start:349562][end:359682]] Each cognition actor is an independent process, each one has a scope, a level of abstraction as well.
[[start:359736][end:381322]] So for example, you would have a cognition actor that's concerned with the location of food and it would have beliefs and perceptions about food location and these would feed into a higher level cognition actor, let's say food approach which is concerned about getting closer to the food and so forth and so on.
[[start:381376][end:385642]] These cognition actors communicate again in simple ways.
[[start:385696][end:398138]] This is the society of mind and they communicate by emitting predictions, predictions about the beliefs of other cognition actors and they communicate by emitting prediction errors.

06:38 [[start:398234][end:422194]] When predictions made about their beliefs by others are inaccurate that leads to connection actors processing these prediction errors and combining them with their own predictions to create an updated set of perceptions that are synthesized into beliefs.
[[start:422242][end:431770]] And these beliefs lead to actions in order to eliminate negative beliefs or validate positive beliefs.
[[start:432270][end:441390]] Now it's from the interactions of all these kung fu actors that seemingly purposeful behaviors emerge.
[[start:442130][end:446190]] So that was successful but learning was very limited.
[[start:447170][end:465430]] This hierarchy of cognition actors was given, was predefined and the only learning that a robot would do was to discover which action policies tended to be more effective.

07:49 [[start:469950][end:475900]] So clearly my robots are not monolithic active inference agents.
[[start:477630][end:483978]] So the question is why would I use a society of mind architecture?
[[start:484154][end:494210]] Well, because I subscribe to the notion that all intelligence is collective intelligence.
[[start:495190][end:506854]] This paper makes the argument quite cogently and I'm going to cite a number of papers which were important to the evolution of my thinking.
[[start:506972][end:508280]] This is one of them.

08:30 [[start:510810][end:515898]] This paper sees intelligence as a process, not a property.
[[start:515984][end:523850]] It's a process enacted by the interacting parts as opposed to again, a property of individuals.
[[start:524750][end:540374]] So society of mind is basically that it's actually a number of interacting processes that together from which emerge apparently intelligent behaviors.

09:00 [[start:540522][end:549410]] Now my own personal current definition of intelligence is self sustaining, inactive sense making.
[[start:549560][end:564920]] Sense making is really important by autonomous agent system in a dissipative and dynamic environment and this guides all the work I do in this project.

09:27 [[start:567230][end:584080]] Now, if you want a description, a detailed description of where my project stood a year ago, there's a paper that was published that I published on Xenodo, which you can look up.

09:47 [[start:587380][end:599044]] Now, over the last year, I wanted to move away from a pre built a given society of mind and toward a learned society of mind.
[[start:599082][end:610680]] I wanted to see if I could program an autonomous robot to evolve its society of mind through its interactions with its environment.

10:11 [[start:611580][end:622990]] Now, one might think that programming autonomy is an oxymoron would be a good point, but I don't think it is.
[[start:624400][end:654820]] If if the program I write and install my robot imparts constitutive autonomy, which is enable the robot to constitute its own identity, and if it imparts adaptivity, which enable the robot to modify itself from its interactions with the environment, then I think that the robot will be truly autonomous.
[[start:655820][end:664820]] Now, for autonomy to exist inherently in the robot, something in the robot must be at stake.

11:04 [[start:664980][end:670924]] And in this case, it's the survival of the robot society of mind.
[[start:671042][end:677880]] Now, the physical structure of the robot is not at stake.

11:17 [[start:677960][end:682028]] Its survival is not at stake, unless, of course, it falls off a shelf.
[[start:682204][end:699350]] But as I intend to have my robot develop its society of mind from experiences, I also expect that if it fails, that this society of mine will perish in its attempt to grow and sustain itself.
[[start:700040][end:710410]] So that's what's at stake going forward in this project is the survival of the robot society of mind.

11:51 [[start:711260][end:715000]] This survival would be an expression of being.
[[start:715070][end:723020]] By doing, the robot will need to act and interact in its environment in order to survive.
[[start:723360][end:730620]] Now, whatever sense it's going to make of its environment will then be grounded in this survival imperative.
[[start:730960][end:735950]] In essence, the robot society of mine will have skin in the game.
[[start:736560][end:741164]] If this weren't the case, then sense making would actually reside somewhere else.

12:21 [[start:741202][end:746864]] It would reside in in the mind of the programmer, in my mind as I observe the robots.
[[start:746912][end:753670]] But I would like the sense making to be grounded in the survival of the robot's mind itself.
[[start:754780][end:756010]] So that's key.
[[start:757500][end:763288]] Now, what do I mean by an evolving and growing society of mind?
[[start:763374][end:781920]] So instead of the given society of mind, which I showed earlier, I want the cognition actors to be created to connect with each other dynamically through interactions with the environment.

13:03 [[start:783060][end:790764]] So I want an active, self organizing, self optimizing collective of cognition actors.
[[start:790812][end:792076]] Now, is this feasible?
[[start:792188][end:793510]] Well, that's a big question.

13:15 [[start:795880][end:806084]] In trying to answer this question, I'll be also answering questions like what must be given a priori and what can be discovered?

13:26 [[start:806212][end:808920]] Well, I already have elements of an answer.
[[start:808990][end:821004]] I know that the sensors and the effectors and the primitive cognition actors that wrap them will be given.
[[start:821122][end:823708]] This will be like what you're born with, basically.
[[start:823874][end:835836]] And there might be a metacognition actor which role will be to oversee and guide the evolution of all other cognition actors.

13:55 [[start:835868][end:838160]] But that's my hypothesis.

14:00 [[start:840580][end:847376]] I can imagine a test environment for my robot that will test its ability to survive.
[[start:847488][end:859860]] I can imagine, for example, that as the robot moves around or computes, it uses a limited store of energy it's stimulated.
[[start:860200][end:865892]] And that store of energy is replenished when the robot consumes food.
[[start:865946][end:872780]] And that would be by being on top of pieces of paper, colored pieces of paper on the floor.

14:34 [[start:874000][end:877928]] And I'm going to make sure that it needs two sources of food in order to survive.

14:38 [[start:878024][end:881552]] That would be represented by a yellow paper and a green paper, for example.
[[start:881686][end:889312]] So that to prevent the robot from just simply finding one source of food and just stationing itself over it.
[[start:889446][end:892728]] So the environment will also contain obstacles.
[[start:892844][end:908292]] So the robot will need to learn how to navigate, avoid obstacles, locate different sources of food, get to them, and make sure that it alternate between various sources of food in order to survive.
[[start:908356][end:917530]] And the society of mind that will evolve, will hopefully evolve to successfully do this.

15:17 [[start:917840][end:926904]] Else if it doesn't, then it will shrink as resources disappear and essentially die.
[[start:927032][end:931520]] So that's what it's at stake for this robot.

15:33 [[start:933620][end:946980]] Now, this effort employs a number of frameworks, and by framework, I mean a useful system of concept and constraints that guide the implementation.

15:47 [[start:947560][end:953220]] Well, there's obviously the free energy principle and the Active inference framework.

15:55 [[start:955800][end:962740]] However, I see this, the Acactive Inference, as an as if framework.
[[start:962900][end:973740]] It describes the what what must be achieved in this case, reduction of the agents, variational, free energy.
[[start:973890][end:979368]] But it doesn't guide me as to the implementation, how to build the robot.
[[start:979464][end:983196]] For this, I need as is frameworks.
[[start:983388][end:993510]] And I'll be using two frameworks, one which I've been using since the beginning of the project, which is the Actor model.

16:34 [[start:994200][end:1010680]] The Actor model views computation as a diversity of processes, processes that are independent, have their own private internal state, and who communicate with one another strictly through messages.

16:51 [[start:1011900][end:1023788]] Yesterday in Enterprise One, Keith Duggar presented on the Actor model and made the case that we should use the actor model to implement active inference agents.
[[start:1023954][end:1026350]] Well, I wholeheartedly agree with them.
[[start:1026800][end:1035824]] The other framework that I'm going to be using is a special case of symbolic AI called the App Perception Engine.
[[start:1035942][end:1042560]] And much of the presentation will be about the App Perception Engine and its implementation.

17:24 [[start:1044840][end:1061880]] So here's where we are is the project is located at the intersection of Active Inference as a domain, the Wet and Society of Mind as an architecture, and symbolic AI as a form of computing.
[[start:1062460][end:1066280]] So that's where the project is, at this intersection.

17:49 [[start:1069040][end:1070204]] So where to begin?
[[start:1070322][end:1077916]] So I want to dive into a more extensive form of learning.

17:58 [[start:1078018][end:1083660]] And the first step, logically, is to learn how to predict.
[[start:1083820][end:1091756]] So I want to enable a single cognition actor.
[[start:1091868][end:1099792]] We'll start with a single cognition actor to learn how to make sense of its local environment, its so called unvelt.

18:19 [[start:1099936][end:1109684]] And making sense implies, at a minimum, to be able to predict incoming sensations.
[[start:1109732][end:1112040]] So it needs to learn to predict.

18:36 [[start:1116650][end:1120966]] So what will be given to a cognition actor?
[[start:1120998][end:1131100]] Well, there will be a history of sensations broken into discrete units of time.
[[start:1131550][end:1138320]] So time n minus three and N minus two, n minus one time n, which is the present moment.

19:00 [[start:1140450][end:1143150]] So these would be remembered observations.
[[start:1144210][end:1157140]] And then what we want to get out of this is the ability to predict the next incoming set of sensations at time t equals n plus one, n plus two.
[[start:1157530][end:1169430]] And for this, to be able to predict future observations, we need some kind of predictor function that is learned from the remembered observation.
[[start:1170350][end:1175306]] Now, this predictive capability can be built in two very general ways.
[[start:1175488][end:1188506]] One is from statistics, so doing pattern analysis and being able to predict what's most probable, which is the standard current machine learning approach.

19:48 [[start:1188698][end:1212120]] Or we could predict from an understanding of the observations by developing a causal model of what produced these sensations, and from this understanding, predict what rationally should be observed next.

20:16 [[start:1216070][end:1219620]] So this is all about sense making.
[[start:1219990][end:1223110]] And now what is sense making?
[[start:1223180][end:1225000]] How do I understand sense making?

20:27 [[start:1227210][end:1232694]] Well, to rationally predict incoming sensory inputs, one must make sense of them.
[[start:1232732][end:1234760]] That's what making sense means to me.
[[start:1235150][end:1242154]] And to make sense of sensory inputs means to derive meaningful experiences from them.
[[start:1242192][end:1246346]] It's not just data, it's not just pieces of data.
[[start:1246528][end:1248666]] There must be meaningful experiences.

20:48 [[start:1248858][end:1258862]] And by experience, I mean a conceptualization of the sensations and a unification of them in time and space.
[[start:1258996][end:1270110]] So making sense of these inputs will mean to produce meaningful experiences that are conceptualizations and unifications of the sensations.
[[start:1270270][end:1276840]] Now, an experience is meaningful if it is underwritten by a causal model.

21:17 [[start:1277450][end:1290330]] So the experience is perceived as the consequences of a latent generative model, generative process that we have modeled.
[[start:1291070][end:1294218]] And I want meaning to be inherent to the agent.

21:34 [[start:1294384][end:1303630]] And that only happens if the agent is truly autonomous and if this meaning is grounded in the survival imperative, as discussed earlier.

21:46 [[start:1306210][end:1308494]] So how does experiencing work?
[[start:1308692][end:1311540]] How can that be put into computer code?
[[start:1312150][end:1317090]] Surprisingly for this, we refer to the philosophy of Emmanuel Kant.
[[start:1317510][end:1326360]] Emmanuel Kant took a reverse engineering approach, asking himself what must entities do to achieve experience?
[[start:1327930][end:1337286]] This is akin to the free energy principles high Road, which can be paraphrased as what must organisms do to maintain their existence?

22:17 [[start:1337398][end:1355150]] So Emmanuel Kong tried to reverse engineer cognition, asking himself what's the minimal cognitive apparatus needed by an entity to have experiences?

22:35 [[start:1355970][end:1361666]] And that he documented in his critique of pure reason.
[[start:1361848][end:1364130]] Just a little parenthesis.
[[start:1365270][end:1370580]] The meaning of the title Critique of Pure Reason is not what I thought it was.
[[start:1371270][end:1375442]] It actually translates more closely to the case for April.

22:55 [[start:1375506][end:1383074]] Cognition critique is a legal term is where you make your case and pure reason we translate nowadays.
[[start:1383122][end:1384710]] April cognition.
[[start:1385070][end:1406030]] So his work wanted to establish what must happen to create an experience that's coherent, that is unified in time and space, and to reverse engineer cognition as a system that is both complete and essential, that is minimal.

23:31 [[start:1411100][end:1427148]] Okay, so I'm going to try to give you the postage stamp version of Emmanuel Kant's theory focusing on the Synthetic Unity of Apperception.

23:47 [[start:1427324][end:1432050]] Well, first of all, there's the real world, which is outside of our direct experience.
[[start:1432740][end:1433884]] It's the pneumonia.
[[start:1433932][end:1446016]] It's forever hidden from us as an as is reality, but it impinges on our sensorium.
[[start:1446048][end:1462570]] And then so we have a number of intuitions, sight, sound, touch, smell that are initially separate, and then we need to network them, connect them both in time and in space.

24:23 [[start:1463200][end:1468750]] In space is sound.
[[start:1469520][end:1479970]] And the sight describing a single thing is one thing behind or inside another.
[[start:1481300][end:1486370]] And in time, is this happening before, after something else?
[[start:1487220][end:1504330]] And then at a higher level, meaning is given to these networked, intuitions, sensations via concepts and judgments, rules which are generalizations as to what can and cannot be.

25:05 [[start:1505980][end:1508090]] And this is what we experience.

25:12 [[start:1512720][end:1522690]] Now, it turns out that synthetic Unity of Apperception is a blueprint for automating sense making.

25:25 [[start:1525540][end:1534980]] It's kind of interesting, I think, that 18th century philosophy would be relevant to 21st century technology development.
[[start:1535480][end:1549290]] And this is what happened and was published by Richard Evans and all in the paper Making Sense of Sensory Input, where they developed the App Perception Engine.
[[start:1549740][end:1570656]] They took synthetic Unity of Apperception as software requirements and successfully implemented them into a piece of software, the App Perception Engine, and applied it to a number of exercises where they got a very good result.

26:10 [[start:1570838][end:1575360]] So the App Session Engine is in an instance of machine learning.
[[start:1575430][end:1586820]] It's unsupervised machine learning, and it operates on very small data sets and generates human readable generative models.

26:27 [[start:1587480][end:1592810]] When I read the paper, I realized, well, that's exactly what my robot needed.
[[start:1594700][end:1597848]] So what does an app perception engine do?
[[start:1598014][end:1615632]] Well, given a sequence of observed states, it finds a generative model that can recreate past states but most importantly, predict future states.
[[start:1615686][end:1624160]] And the state is defined as a set of simultaneous observations, sensations, intuitions.

27:07 [[start:1627740][end:1636264]] So an apperception engine searches for a causal theory that can recreate observations.

27:16 [[start:1636392][end:1642380]] I say searches because this causal theory is not determined by the observations.
[[start:1643380][end:1644512]] It has to be found.
[[start:1644566][end:1645980]] It has to be discovered.
[[start:1646140][end:1664390]] But once it is found, then it can be validated against the observations and see if it can recreate them and augment them into the future as well as into the past.

27:47 [[start:1667100][end:1669880]] So what is a causal theory?
[[start:1670780][end:1676920]] A causal theory is a logic program that has a number of components.

27:59 [[start:1679180][end:1686828]] In the causal theory, there will be the objects and the predicates from the observed relations.
[[start:1686914][end:1697356]] So from the observations, we can extract what objects were observed and what properties of these objects were observed and maybe what relationships these objects were observed.

28:17 [[start:1697548][end:1698720]] That's the start.
[[start:1698870][end:1702908]] Then we have latent object types, objects and predicates.
[[start:1703004][end:1717940]] So we may want to imagine causal theory, imagines hidden objects, maybe hidden types of objects and maybe hidden properties and relationships between objects, latent meaning unobserved.

28:38 [[start:1718020][end:1733608]] And given both the observed and unobserved objects and predicates, it derives rules, first of all constraints on those predicates, what's permissible.
[[start:1733704][end:1743712]] So for example, being in front of A cannot be in front of B and at the same time behind B.
[[start:1743766][end:1747632]] So an object cannot be in front of another and behind it.
[[start:1747686][end:1759316]] So there are constraints on predicates and then there are rules that apply to any simultaneous sets of observations, what they must conform to.

29:19 [[start:1759418][end:1771240]] Then there are rules that given a state, will infer the next state and then maybe some initial state from which we can run the causal theory.

29:33 [[start:1773020][end:1776520]] So what makes a causal theory unified?
[[start:1777180][end:1781000]] Well, first of all it needs to be unified in order to make sense of the observation.
[[start:1781680][end:1783640]] There are various dimensions.
[[start:1783720][end:1789704]] So if a causal theory involves a number of objects, all these objects must be directly or indirectly related.
[[start:1789752][end:1796080]] There's no object that just floats in space totally independent of the other objects, so they must all be related.

29:56 [[start:1796980][end:1799360]] So they're spatially unified.
[[start:1799780][end:1820760]] All predicates that make up the causal theory, like on, off, behind, in front, they must be constrained so that, for example, in front cannot be at the same time as behind or that a light cannot be both turned on and turned off.

30:20 [[start:1820830][end:1828360]] So there's some restrictions on the predicates and that creates conceptual unity.
[[start:1828780][end:1839900]] And then there's static unity where all simultaneous relations must satisfy the static rules, and temporal unity, where all the states must be sequenced by causal rules.
[[start:1840320][end:1841820]] We'll see examples.

30:43 [[start:1843700][end:1852108]] So let's start with an example here of a set of observations.
[[start:1852204][end:1862436]] What we are observing are two lights and the lights can either be at any discrete moment in time, either on or off.
[[start:1862618][end:1871130]] So here we have a sequence of observations and one moment in time.
[[start:1871900][end:1874730]] The first light was off and the second light was on.
[[start:1875180][end:1884780]] Then the first light was on, the second light was off, then both were on, et cetera.

31:25 [[start:1885600][end:1891816]] And I put the gray bars there to show that maybe the observations are incomplete.
[[start:1891848][end:1899760]] So at one stage we can only see the second light or there may be other lights or other objects that we do not see, but that's what we observe.

31:42 [[start:1902870][end:1927322]] So you feed these observations in discrete time into the apperception engine and the perception engine searches for a causal theory that when applied to an initial condition, let's say that light A is off and light B is on.
[[start:1927456][end:1932350]] It will create a trace of recreated observations.
[[start:1932770][end:1940538]] That cover is a superset, matches the initial observations.
[[start:1940634][end:1945140]] And if this happens, then our causal theory is a good one.

32:25 [[start:1945910][end:1956100]] Now, the causal theory may infer the existence of hidden objects, hidden relations, and whatnot it may actually need to.

32:38 [[start:1958330][end:1966822]] So here's an example of a causal theory that is generated by my own implementation of the App perception engine.
[[start:1966956][end:1986400]] Because I re implemented the App perception engine as described in the paper by Richard Evans and all, and I ran it on the set of observations about lights on two lights, one on, one off at any point in time.
[[start:1987490][end:1989918]] And it came up with it found a result.
[[start:1990084][end:1993098]] It found the result in 64 seconds.
[[start:1993274][end:1994980]] It was a perfect match.

33:15 [[start:1995430][end:2008200]] And it actually invented a relationship, which it called thread One, which we can let's imagine that it actually means connects to.

33:29 [[start:2009130][end:2012950]] And it found a static rule and a causal rule.
[[start:2013290][end:2017894]] It said that a light is on at any moment in time.
[[start:2017932][end:2022460]] A light is on if a light that connects to it is off.
[[start:2022990][end:2035280]] And it found a causal rule that said a light turns off if it connects to another light that was also off.

33:55 [[start:2035970][end:2041230]] So that's how the lights change over time, the status of on and off.
[[start:2041380][end:2056500]] And it came up with initial conditions that said that, well, A connects to, first of all, that there's an object one, a light called object one that we don't see, but is there, we imagine is there, that A connects to it.
[[start:2056890][end:2061800]] The light object one connects to B, and the light B connects to object one.
[[start:2062410][end:2065190]] So that's the causal rule that it discovered.

34:27 [[start:2067770][end:2072170]] Now, if we run this causal rule, we produce a trace.

34:33 [[start:2073070][end:2076982]] And as you can see, the trace matches the observation.
[[start:2077126][end:2079354]] It adds a new object.
[[start:2079552][end:2086910]] So the coverage being excellent, being perfect in this case, and our causal theory is a good one.
[[start:2086980][end:2088560]] It's actually a perfect one.

34:49 [[start:2089570][end:2091760]] It's not necessarily the only one, though.

34:54 [[start:2094230][end:2097646]] So is this causal theory unified?
[[start:2097838][end:2100050]] So going back to Dr.
[[start:2100120][end:2114710]] Kant's requirement of synthetic unity, of Apperception, not every causal theory will do, though it may predict correctly, it may not be meaningful unless it is unified.

35:17 [[start:2117560][end:2121844]] Well, we saw the four dimensions of unification.
[[start:2121892][end:2124484]] Is it spatially unified?
[[start:2124612][end:2131530]] Well, all our objects are connected directly or indirectly to each other.
[[start:2132480][end:2133630]] That's good.

35:34 [[start:2134720][end:2136940]] So we have spatial unification.

35:37 [[start:2137440][end:2139144]] Do we have conceptual unification?
[[start:2139192][end:2141192]] So we have this new predicate.
[[start:2141336][end:2142940]] We have two predicates, right?
[[start:2143090][end:2151584]] Pred One, which we translate to, connects to, and then the predicate that says whether the light is on or off.
[[start:2151782][end:2159908]] Well, we have a constraint that says that a light can only be connected to one other light.

35:59 [[start:2159994][end:2169840]] So pred one has a constraint on it that says it's exclusive.
[[start:2170000][end:2175572]] So an object cannot pred one to two objects cannot connect to two objects.
[[start:2175636][end:2179332]] That's a constraint that was discovered and part of the causal theory.
[[start:2179476][end:2192172]] And also implicitly, the on relation of the predicate has the value on or off, and it cannot be both at the same time.
[[start:2192226][end:2195180]] So it's conceptually unified.

36:35 [[start:2195700][end:2197680]] Is it statically unified?
[[start:2198020][end:2201292]] Are the static rules obeyed.
[[start:2201436][end:2212324]] Well, for example, the static rule would say that given that B connects to A, if B is off, then A must be on.
[[start:2212362][end:2217540]] So if you look at any place where B is off, a is going to be on.
[[start:2217610][end:2223716]] And you could do that for every other light and relationships between lights.

37:03 [[start:2223748][end:2226404]] So they all obey the static rule.
[[start:2226532][end:2236668]] And the causal rule says, for example, here, that if B connects to A, then if A was off, then B must turn off.
[[start:2236754][end:2241790]] So if you look at B, let's say B was off.

37:25 [[start:2245680][end:2259716]] Yeah, I'm sorry, if B connects to A, and yes, and if A was off, B must be off.

37:39 [[start:2259818][end:2264020]] So if A was off, B becomes off the next step.
[[start:2264090][end:2266310]] So that's correct as well.
[[start:2267240][end:2272730]] So statistically we are true, and temporarily we are true.
[[start:2273500][end:2275060]] We are unified.

37:55 [[start:2275220][end:2279480]] And of course, that we get a thumbs up from Dr.
[[start:2279550][end:2283928]] Kant, our causal theory is unified.
[[start:2284104][end:2289580]] Thus it makes sense of the observations of the sensory inputs.
[[start:2291120][end:2299308]] Now, it's no accident that Kant would be would figure in an active inference project.
[[start:2299474][end:2310980]] There is a link between active inference and Kant, and it runs through the celebrated 19th century German engineer Herman von Hemholz.

38:31 [[start:2311320][end:2319536]] He was a disciple of Kant and he developed the theory of visual perception that operationalized Kant's epistemology.
[[start:2319648][end:2322520]] And in fact, it anticipates predictive processing.

38:42 [[start:2322860][end:2329284]] In 1995, Peter Day and Jeff Hinton developed the Helmholtz machine.
[[start:2329332][end:2331000]] Name is in his hunter.
[[start:2332220][end:2338732]] It is a type of artificial neural network that's trained to create a generative model from an original set of data.

38:58 [[start:2338786][end:2341950]] And it can account for the hidden structure of the data.
[[start:2343040][end:2351410]] So as you see, there's a link which is discussed and elaborated in this paper, which is very interesting paper.
[[start:2352580][end:2356748]] All right, so close parentheses.
[[start:2356924][end:2361780]] So we've looked at the App Perception engine from the perspective of philosophy.
[[start:2362120][end:2366550]] So now let's look at it through the lens of machine learning.

39:29 [[start:2369660][end:2372136]] The observations constitute a training set.
[[start:2372238][end:2373850]] It's a very small one.
[[start:2374220][end:2380500]] And the Appetition engine is the learning algorithm.
[[start:2380660][end:2384140]] And what is learned, the output is a causal theory.

39:46 [[start:2386000][end:2397904]] So the learning process is unsupervised logical inferencing, and the output is a human readable logic program.

39:58 [[start:2398102][end:2423450]] So we see here that there's some profound differences with the more popular form of machine learning in that the training set is really small, that the product of the learning is actually a human readable artifact, in this case, a logic program.

40:25 [[start:2425500][end:2427770]] So this is the training set.
[[start:2429340][end:2447520]] As inputted lights led, a turned off at time one, b turned on at time one, a turned on at time two, b turned off at time two, et cetera, et cetera.

40:47 [[start:2447940][end:2462992]] So that's the training set and you feed this into the perception engine's algorithm and out comes a causal theory.
[[start:2463136][end:2468676]] So in a little bit more details what the algorithm is and does.
[[start:2468858][end:2477684]] First, it extracts the observed object extent objects, the object types and predicates from the observations.

41:17 [[start:2477812][end:2481896]] So we have on, we have object A, object B.
[[start:2481998][end:2483692]] We have led as an object type.
[[start:2483746][end:2489020]] So that's all part of the observations and that becomes part of the extent vocabulary.
[[start:2489440][end:2503516]] Then the application engine imagines unobserved objects, types and predicates for the relationships and properties, and that becomes a latent vocabulary.
[[start:2503548][end:2506380]] So there's a step of imagination.

41:46 [[start:2506540][end:2530760]] Then, using the combined vocabulary, both the extent and latent vocabulary combined, it looks for a unified causal theory, a set of constraints, rules and initial conditions that obey the constraints of synthetic unity of apperception.

42:12 [[start:2532220][end:2539980]] Once it has this causal theory and with initial conditions, it applies the causal theory to these conditions and produces a trace.
[[start:2540640][end:2546990]] It recreates observations if you want and augments them and extends them into the future.
[[start:2547680][end:2555952]] Now it looks at this trace and compares it with the initial observations for coverage and decides if this is a good causal theory or not.
[[start:2556086][end:2564784]] Then it also looks at the causal theory complexity, how many rules, how complex are the rules, et cetera, and measures for complexity.

42:44 [[start:2564832][end:2578596]] So if we have a choice between two causal theories of equivalent coverage, the App Perception Engine will select the least complex one using Occam's Razor.
[[start:2578788][end:2587420]] Now, if you look at this algorithm, you'll see that the boxes in green are not deterministic.
[[start:2587840][end:2589308]] This is where search happens.
[[start:2589394][end:2591976]] We can posit different kinds of objects.
[[start:2592088][end:2594888]] We can find different kinds of rules.

43:14 [[start:2594984][end:2598110]] So this is where search happens.
[[start:2599360][end:2604252]] Now, app perception is implemented using logic inference.
[[start:2604396][end:2608896]] Actually, it uses three forms of logic inference.
[[start:2609008][end:2617648]] There's the one that we're more familiar with, which is deduction, where given rules and causes, we infer the effects.
[[start:2617824][end:2619600]] Then there's induction.

43:39 [[start:2619680][end:2622324]] Where given causes and effect, we look for the rules.
[[start:2622372][end:2624728]] This is what science does, right?
[[start:2624814][end:2629108]] Looking for rules that would account for effects given the causes.
[[start:2629284][end:2636520]] Then there's abduction, where given the rules and given what we observe the effects, we're looking for the causes.
[[start:2636600][end:2642220]] In this case, we're looking for the latent objects, the latent relationships between these objects.

44:02 [[start:2642800][end:2654690]] And then you can combine both abduction and induction, where you're given effects, essentially observations, and you're looking for both causes and rules, which is what the App Perception Engine does.

44:15 [[start:2655300][end:2661524]] And this is where in the algorithm, these kinds of inferences are at play.
[[start:2661722][end:2671956]] So positing latent objects, that's a form of abduction, imagining causes, finding the rules, well, that's clearly a form of induction.
[[start:2672148][end:2682916]] And then applying the rules of a causal theory to some initial conditions to create a trace, well, that's deduction.
[[start:2683028][end:2690072]] We have the causes, the initial conditions, we have the rules, causal theory, and then we produce a trace, the effects.

44:50 [[start:2690136][end:2691544]] So that's deduction.
[[start:2691592][end:2697260]] So the App Perception Engine uses all forms of logical inference.
[[start:2698800][end:2707688]] Now, just a reminder that the output of the App Perception Engine, that is what is learned is actually human readable.
[[start:2707884][end:2720904]] You may want to compare that to a large array of floating points produced by traditional, the more popular form.

45:20 [[start:2720942][end:2722548]] Of machine learning nowadays.

45:22 [[start:2722644][end:2726392]] So here, this is what's actually produced by the app reception engine.
[[start:2726446][end:2735060]] As it runs on a set of observations, it produces a logic program that is human readable.
[[start:2735220][end:2741404]] When you look at it, the only thing you need to kind of guess is what is meant by pred one.
[[start:2741442][end:2752480]] And if you think, well, maybe it means connects to maybe the lights are connected underneath a board out of sight of the observer.

45:54 [[start:2754580][end:2757668]] But finding a unified causal theory is hard.
[[start:2757754][end:2762436]] So we have to guess what the latent objects and predicates are.
[[start:2762618][end:2767968]] What are the hidden lights, what are the hidden relationships between lights?
[[start:2768064][end:2777160]] And we have to discover what constraints might apply on the predicates and what are the initial conditions from which we want to recreate a trace.
[[start:2777660][end:2782240]] What are the static rules that apply to simultaneous observations?

46:22 [[start:2782340][end:2792030]] And then what are the causal rules that given observations at time T will predict observations at time T plus one?
[[start:2792480][end:2793550]] This is hard.
[[start:2794080][end:2798384]] As a matter of fact, it's non polynomially hard.
[[start:2798582][end:2808080]] The search space grows exponentially with the size of the input, which is the size of the extent and latent vocabulary.
[[start:2809240][end:2816660]] So just like in chess, you can't predict to the end the consequence of a move because of common turbo explosion.

46:57 [[start:2817000][end:2826970]] With the app perception engine, you cannot systematically traverse the entire space of possible causal theories to find a good one because it's impossibly large.

47:09 [[start:2829740][end:2836140]] So the job of the apperception engine is to find a causal theory in a ridiculously large haystack.
[[start:2837520][end:2838830]] How to do this?
[[start:2839600][end:2856000]] In my implementation, I follow the recommendations and I follow also the implementation in Richard Evans'paper by breaking the search space into chunks.

47:36 [[start:2856500][end:2864020]] First there's a region and the region says so how many latent object types, objects and predicates will we allow?
[[start:2864090][end:2873364]] So what is the limit of imagination of the cognition actors that is trying to apperceive a causal theory?

47:53 [[start:2873492][end:2875428]] What are the limits of its imagination?
[[start:2875524][end:2891432]] And within that region of bounded imagination, we carve it into templates where we say, okay, we're going to use these latent objects types, these latent objects.
[[start:2891576][end:2896000]] And so basically, what vocabulary, specific vocabulary we're going to be using?
[[start:2896150][end:2897392]] We're going to use object one.
[[start:2897446][end:2907884]] We're going to use object pred one on top of the observed on predicate and observed A and B lights.

48:28 [[start:2908012][end:2916688]] And we're going to set the maximum complexity on the rules and see if we can find causal theories that fit this template.

48:36 [[start:2916864][end:2930116]] So this is a carving up of the search space and having broken the search space into regions and templates, we have scopes in which to apply Heuristics.
[[start:2930228][end:2930936]] Now.
[[start:2931118][end:2932600]] Why heuristics?
[[start:2933120][end:2938172]] Because the systematic traversal cannot be done in reasonable time.

48:58 [[start:2938306][end:2944476]] There's just too many candidate causal theories to look at to find a good one.
[[start:2944578][end:2946320]] So we use Heuristics.
[[start:2948260][end:2954384]] We find ways of maybe getting to a good solution faster at the risk of missing it.
[[start:2954502][end:2961028]] But at least we'll have an answer or no answer in a reasonable amount of time.
[[start:2961114][end:2967396]] And there's a number of heuristics that I've implemented in my implementation of the app assetron engine.

49:27 [[start:2967578][end:2969040]] Well, there's time boxing.
[[start:2969120][end:2975240]] At some point, you'd spend no more than this amount of time looking into a region or into a template.
[[start:2976060][end:2977348]] There's multitasking.

49:37 [[start:2977444][end:2980724]] Well, the problem is actually, as they say, embarrassingly parallel.
[[start:2980852][end:2988830]] You can explore multiple regions and multiple templates in parallel and so make good use of a multicore computer.

49:49 [[start:2989680][end:2991612]] You want to make sure you don't repeat yourself.
[[start:2991666][end:2998080]] So you don't want to traverse the same region twice or look at the same causal theory twice.
[[start:2998500][end:3003520]] You want to satisfy maybe a good enough theory is just fine.
[[start:3003590][end:3006364]] We don't want to look for the perfect one necessarily.
[[start:3006412][end:3007730]] We may not have time.

50:08 [[start:3008740][end:3010044]] You want to fail early.
[[start:3010102][end:3021184]] If you're in a region where nothing good is found, you may want to leave it quite quickly at the risk of maybe not finding a good one that is just over the horizon.
[[start:3021232][end:3023220]] But you want to be impatient.
[[start:3023380][end:3024884]] You want to throw the dice.
[[start:3025012][end:3036350]] You may want to kind of mix it up so that every time you run the app Perception Engine on the same problem, you may find a different solution first.

50:37 [[start:3037840][end:3041372]] You want to go for the simpler solution first.
[[start:3041506][end:3044124]] You may not want to try everything, just sample some.
[[start:3044242][end:3052144]] You want to start with the easiest part of the search base first, be judicious and so forth and so on.
[[start:3052182][end:3054236]] And most importantly, be selective.
[[start:3054348][end:3061760]] So reject any causal theory that would fail the constraints of unity of apperception.

51:02 [[start:3062200][end:3071156]] With all these in place, my implementation of the app Perception Engine gives pretty good results.
[[start:3071268][end:3073080]] So here I did a run.
[[start:3073150][end:3074148]] This is not cherry picked.
[[start:3074164][end:3082244]] I decided to do one series of seven runs and collect the data and show it.
[[start:3082382][end:3093900]] And in this run, I set up the apparition engine to only accept a perfect causal theory, one that would produce a trace that totally covers the observation.

51:34 [[start:3094480][end:3097260]] And I did seven runs.
[[start:3097780][end:3100880]] The first one succeeded, found it in 4 seconds.

51:41 [[start:3101300][end:3103756]] The second one, it took 102 seconds.
[[start:3103788][end:3108672]] So there's some randomization in the order in which things have searched if luck is involved.
[[start:3108736][end:3113510]] As I said, the third one, 1 second, that was pretty cool.

51:55 [[start:3115400][end:3121784]] The fourth one, well, took 204 seconds, then 90, 612, 99.
[[start:3121822][end:3125496]] So quite a good distribution here.
[[start:3125678][end:3133960]] Now, I said, okay, I'm going to run the app Perception Engine again on the same training set that I showed earlier, those two lights.
[[start:3134120][end:3145076]] But this time I said, I'm going to accept the theory that has 85% or more coverage.
[[start:3145208][end:3153708]] So it recreates the observations well enough, but not perfectly.

52:33 [[start:3153884][end:3156524]] And I time boxed it to 30 seconds.
[[start:3156572][end:3158276]] So you have 30 seconds to find it.
[[start:3158298][end:3158870]] Go.
[[start:3159640][end:3167760]] The first run, it find a causal theory with 75% accuracy immediately.

52:47 [[start:3167920][end:3170292]] Then the same accuracy, same coverage.

52:50 [[start:3170356][end:3171316]] 10 seconds.
[[start:3171428][end:3172196]] 11 seconds.
[[start:3172228][end:3174708]] It hit 29 seconds.
[[start:3174884][end:3177336]] It found a perfect one.
[[start:3177518][end:3180904]] Then eleven, it found 87% coverage and stopped right there.

53:00 [[start:3180942][end:3181688]] That's good enough.
[[start:3181774][end:3189416]] 75 again, 100% is the first one it found above 85 in 18 seconds and 75% 0 second.
[[start:3189448][end:3193772]] So a good distribution again, so we're getting into reasonable times.
[[start:3193826][end:3196444]] We're not talking about hours here, we're talking about seconds.
[[start:3196572][end:3217536]] And I'm hoping to do further optimizations and bring it down to something even smaller so that a cognition actor can say, I want to make sense of these observations, query the apperception engine, and get an answer, a causal theory within maybe a couple of seconds.

53:37 [[start:3217568][end:3218630]] That's my hope.
[[start:3220440][end:3222356]] Now, something interesting here.
[[start:3222378][end:3231960]] It so happens that what makes it hard for the app perception engine to find a good causal theory is formally equivalent to what makes cognitive science as a whole hard.

53:52 [[start:3232030][end:3237020]] And this paper here makes the case and proves the case quite cogently.
[[start:3238640][end:3254372]] So cognizant science wants to find models, functions or algorithms that explain, account for situated behaviors.

54:14 [[start:3254436][end:3272450]] So you feed into the cognitive science machine pairs of situations and behaviors, and you want to come out of it a model, an explanation, a function, or an algorithm that accounts for it.
[[start:3273220][end:3289840]] Well, the paper makes the case that if the explanation is to be bounded in size, then the problem is computable, but it's not tractable in the sense meaning that it's combinatorially explosive.
[[start:3289920][end:3302936]] But once you have a solution, it is computable and tractable to verify that the solution is good, that it accounts for the data that you're trying to understand.

55:03 [[start:3303118][end:3307850]] Well, this is equivalent, formally equivalent to what the app perception engine is doing.

55:11 [[start:3311200][end:3314300]] My implementation was done in prologue.
[[start:3314800][end:3316776]] I will not go into the details.
[[start:3316808][end:3318648]] It's about 1000 lines of prologue.
[[start:3318744][end:3328480]] I'll just say that prologue is a programming language that use deductive inference as its model of computation with backtracking.
[[start:3329460][end:3339430]] So essentially it searches for a solution and will backtrack if it took the wrong branch if you want.

55:40 [[start:3340280][end:3346570]] And we'll look for a different way of satisfying a line of the program.
[[start:3348220][end:3352170]] So let's just say that it makes traversing a search space.
[[start:3353340][end:3357316]] We get traversing a search brains for free when we program in prologue.
[[start:3357508][end:3360764]] I won't go into any more details, but you can see some prologue code here.
[[start:3360802][end:3371740]] And the fun thing is that a prologue program is akin to a logical description of the problem it's trying to solve.

56:12 [[start:3372340][end:3373890]] I think it's very cool.
[[start:3374420][end:3385344]] And prologue environment was augmented by something called constraint handling rules, which is an extension to prologue that adds abductive reasoning.
[[start:3385472][end:3401400]] So basically in the program, you can say, assume this is true until proven otherwise, and the CHR rules are there to verify if it can be proven otherwise.
[[start:3401980][end:3415080]] So, again, I'm not asking you to understand this code at all, but I want you to realize that this code is the code that actually executes a causal theory, both the static and causal rules to build traces.
[[start:3415240][end:3416540]] It is that small.

56:56 [[start:3416690][end:3417672]] It's very powerful.
[[start:3417736][end:3423564]] So combining prologue and CHR, I found extraordinarily powerful.
[[start:3423612][end:3425088]] I'm very excited about it.
[[start:3425174][end:3426400]] I'm a programmer.
[[start:3427300][end:3428480]] Next steps.

57:08 [[start:3428900][end:3449800]] Well, next steps, now that we've solved individual learning by cognitive actors, well, I want to move to beliefs from sensations and to policies to validate or eliminate beliefs.

57:31 [[start:3451820][end:3454932]] A lot of these beliefs actually fall out of our perception.
[[start:3454996][end:3459656]] Latent objects and latent relationships and properties can be considered as beliefs.
[[start:3459688][end:3465500]] Then there are other kinds of beliefs that can be obtained from what's been perceived.
[[start:3466800][end:3491984]] There will be introspective beliefs that communicate how the cognition actor is doing in terms of competence, predictionary rates, how well its apperception is doing, and whether it is engaging with other cognition actors.
[[start:3492032][end:3493140]] Is it relevant?

58:13 [[start:3493880][end:3498804]] I will have feelings which will provide normativity to these beliefs.
[[start:3498852][end:3530880]] So if feelings are signals of risk to homeostasis, loss of resources, physical damage, too many prediction errors so that's anger, pain, and fear and feelings will taint beliefs over time and tainted beliefs, good beliefs, bad beliefs will want to be eliminated or validated through policies that will be synthesized by the cognition actor.

58:51 [[start:3531460][end:3538180]] And each cognition actor will make available to others its API.
[[start:3539320][end:3542896]] What predictions can be made about the beliefs of this cognition actor?
[[start:3542928][end:3551880]] What actions are available to others to be asked of the cognition actor?

59:12 [[start:3552460][end:3577120]] And then as cognition actors connect to one another, as the conjunction actors form the umbelt of other cognition actors, then a conjunction actor will be able to predict the beliefs of others, will be able to compose policies made out of actions that are implemented by other cognition actors.
[[start:3577460][end:3586340]] And eventually, we'll have a society of mind, which is a bunch of intersecting boom belts.
[[start:3587480][end:3590870]] So that's it.

59:51 [[start:3591480][end:3599236]] So I see the society of mine is a complex system of collective theorizers.
[[start:3599428][end:3609790]] And I'm going to try going further with this project to answer the question if collective theorizers can self organize to actively sustain itself.

1:00:10 [[start:3610320][end:3620948]] So thank you to the Active Inference Institute for inviting me to present and for providing a home for this project and for the constant support and encouragement.
[[start:3621144][end:3623420]] I'll see you later on Discord.
[[start:3623580][end:3624450]] Thank you.

1:00:25 _Daniel:_
[[start:3625460][end:3626160]] Awesome.
[[start:3626310][end:3627756]] Thank you, JF.

1:00:27 [[start:3627948][end:3638112]] Just to conclude the session, I'll read two questions and let's maybe address them in an upcoming Robotics and embodied meeting.
[[start:3638176][end:3646944]] So if you're excited about this project, certainly we all are and about symbolic active inference, join the Discord and participate in the Robotics and Embodied.
[[start:3646992][end:3656080]] But I'll drop these two questions from David Williams in the Chat, who wrote, one, how important is conducting this work in real world versus simulation?
[[start:3656160][end:3663132]] And two, what tools or components are missing in the robotics toolkit to make this research easier and better?
[[start:3663266][end:3668172]] I know those are things that you have a lot of thoughts on, so I'll look forward to discussing with you more.

1:01:08 [[start:3668306][end:3669580]] Thank you, JF.

1:01:11 _JF:_
[[start:3671760][end:3672652]] Thank you.

1:01:12 _Daniel:_
[[start:3672786][end:3673580]] Peace.

1:01:15 _JF:_
[[start:3675920][end:3676910]] All right.

1:01:19 _Daniel:_
[[start:3679600][end:3680090]] See you.
