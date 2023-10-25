
00:02 _Daniel:_
[[start:2010][end:2800]] All right.

00:04 [[start:4930][end:11754]] And on to the last session of the first interval.
[[start:11882][end:13310]] Greetings, Nynke!

00:19 [[start:19860][end:20960]] Greetings.

00:21 _Nynke:_
[[start:21380][end:21888]] Hello.
[[start:21974][end:22944]] Good morning.

00:23 _Daniel:_
[[start:23142][end:24770]] Yes, good morning.
[[start:26580][end:27890]] How goes it?

00:29 _Nynke:_
[[start:29380][end:31370]] Yeah, I'm doing fine, thanks.

00:33 _Daniel:_
[[start:33260][end:36730]] Would you like to present and then we'll discuss?

00:38 _Nynke:_
[[start:38220][end:40184]] Yes, that sounds like a good idea.
[[start:40382][end:41130]] Great.

00:43 [[start:43200][end:44350]] Let's see.

00:46 [[start:46400][end:58212]] Just going to share my screenplay.
[[start:58356][end:59050]] Yes.

01:05 [[start:65600][end:67260]] Can you see the presentation?

01:08 _Daniel:_
[[start:68720][end:69710]] Not yet.

01:10 _Nynke:_
[[start:70240][end:71084]] Okay.
[[start:71282][end:72780]] See flex.

01:15 _Daniel:_
[[start:75120][end:75628]] Yes.
[[start:75714][end:76670]] Looks perfect.

01:17 _Nynke:_
[[start:77520][end:78690]] Okay, great.

01:21 [[start:81460][end:81920]] Yeah.
[[start:81990][end:82976]] Should I just start?

01:23 _Daniel:_
[[start:83078][end:88780]] Yeah, go for as long as you want, and then anyone can ask questions in the live chat, and I'll write down some things, too.
[[start:88870][end:89460]] Thank you.

01:29 _Nynke:_
[[start:89530][end:90550]] Okay, great.

01:31 [[start:91800][end:92260]] Yeah.
[[start:92330][end:100084]] So my presentation today will be on advances in machine theory of mind and theory of mind.
[[start:100122][end:108244]] Sophistication I'm currently a student at the University of Amsterdam and finishing my master's thesis on this topic.
[[start:108292][end:122830]] And I'll be giving a broad overview of current machine theory of mind and an idea or concept for an active inference approach based on previous work related to active inference theory of mind.
[[start:124160][end:131340]] So to start okay, sorry.

02:13 [[start:133330][end:142180]] So for a global overview, we'll start with giving a short basic definition of what theory of mind is and how it's been used.
[[start:142870][end:156790]] Then I'll give you a global overview of current approaches to designing machine theory of mind, including evasion approaches, approaches using Biphysical models, et cetera.

02:37 [[start:157370][end:166230]] Then I'll zoom into active inference models of theory of mind and social intelligence and collective intelligence more broadly.
[[start:167370][end:170258]] And I'll get into the issue of theory of mind.
[[start:170284][end:186480]] Sophistication, which is basically the depth of recursivity of beliefs that you can have about another person's mental states and their thoughts or beliefs or goals about you.

03:07 [[start:187970][end:193250]] And then we'll get into the issue of how to implement recursive beliefs.
[[start:193750][end:201170]] And as an example, we'll discuss Bayesian theory of mind with K levels of depth.
[[start:201670][end:216902]] And then we'll get into the more specific paradigm that I'm using right now to build a theory of mind model, which is based on a very simple model of the matching panning paradigm.
[[start:217046][end:227770]] So we'll talk a little bit about that, and then we'll get into the model itself and current ideas for implementing theory of mind sophistication using active inference.

03:48 [[start:228770][end:232800]] So first of all, what is theory of mind?

03:53 [[start:233170][end:245060]] Theory of mind has been introduced by the very famous paper by Primac and Woodcherf in 1978, I think it was called does the Chimpanzee Have a Theory of Mind?
[[start:245750][end:256550]] And they define theory of mind as the ability to impute mental states to himself and others as a system of inferences.
[[start:257770][end:274410]] And they say system of inferences of this kind is properly viewed as a theory, first, because such states are not directly observable, and second, because the system can be used to make predictions specifically about the behavior of other organisms.
[[start:274990][end:277878]] And I think there's already a lot in this definition.
[[start:277974][end:302130]] And a lot of authors looking at theory of mind right now still use the same view of theory of mind as a theory, a structured theory of different kinds of mental states such as goals, beliefs and desires that facilitate the prediction of observable behavior in other agents such as facial expressions, movement or speech.

05:04 [[start:304230][end:328330]] And I find it very interesting how much this aligns with maybe a predictive processing view of social cognition, but also how weird it is that this theory, theory of theory of mind is still so widespread in the theory of mind literature, modeling literature.
[[start:328690][end:338960]] So there's been some discussion on whether you can properly regard theory of mind as a theory and if so, what kind of theory it is.
[[start:339330][end:348130]] So within the philosophy of mind, there's been basically two mainstreams or main perspectives on theory of mind.
[[start:348200][end:358090]] According to the classic theory, theory of Tom, theory of mind is a causal theory of how these internal mental states generate other agents'behaviors.
[[start:358190][end:361560]] So it's the same kind of view that we just saw.

06:02 [[start:362890][end:380400]] And then the opposite side is called simulation theory of theory of mind, which posits that we use the same kind of cognitive and neurological resources for understanding and predicting other agents as those that we use for understanding the self.

06:20 [[start:380770][end:383882]] And simulation theory can also take on different forms.
[[start:384026][end:386334]] The sun is coming up next to them.
[[start:386372][end:390320]] So that's why I'm based in light at the moment.
[[start:391170][end:394034]] But basically there are lots of versions of this.

06:34 [[start:394072][end:398980]] Some posit that we use the same kind of action prediction mechanisms for ourselves as for others.
[[start:399670][end:414194]] And there is this new version of simulation theory that Gordon proposes in 2021 which very broadly says that we have the same kind of theory for other agents for ourselves.
[[start:414242][end:424490]] So there's this general theory for what it means to be an agent that is refined at different stages to facilitate context sensitive predictions in social interactions.

07:08 [[start:428030][end:436670]] So this is also interesting to look at when you model theory of mind, what you think theory of mind is and how it is specifically implemented.
[[start:437250][end:443018]] So why would we be interested in creating computational models of theory of mind?

07:23 [[start:443204][end:449138]] So I think there are three important reasons why this is very relevant at the moment.
[[start:449224][end:454130]] First of all, there is a technical reason or the reason of technological advancement.
[[start:454810][end:466230]] There's been some proposals that argue for the development of artificial social intelligence.

07:46 [[start:466830][end:469420]] Oh wait, yes.
[[start:469870][end:489550]] So the technical reason for developing computational models of theory of mind is to improve artificial social intelligence, especially as we start to live in a world in which research on human AI interaction becomes more relevant.
[[start:490930][end:511670]] And that's been this paper Bob Williams, for example, that's argued that improving artificial social intelligence is needed for successful AI human cooperation and it could improve communication, trust and maybe also value alignment.

08:33 [[start:513050][end:516126]] By utilizing theory of mind for value alignment.
[[start:516178][end:532160]] For example, there is a very strong foundational reason to study social cognition generally and the evolution of social cognition through in silica hypothesis testing and clarifying the conceptual boundaries of theory of mind.

08:53 [[start:533890][end:550850]] One great example for this is research by Devane ETL, which used a computational model of recursive theory of mind compared to alternative models to study different cognitive strategies in non human primates.
[[start:551910][end:562870]] And they find no evidence for the hypothesis that theory of mind sophistication involved with an increase in herd size, but they do find a correlation with, for example, neocortex ratio.
[[start:564010][end:571130]] So in this way, theory of mind models can give us some insight into the evolution of social cognition.
[[start:571950][end:595490]] On the clinical side, theory of mind models can be used to understand relevant social variations in clinical populations, for example, through computational phenotyping and diagnostics and by studying social behavior in groups that have some difficulty with social interactions.

09:56 [[start:596630][end:610470]] And groups that show some kind of variation in social cognition, such as people with autism spectrum, people in the autistic spectrum, people with ADHD or schizophrenia.

10:10 [[start:610970][end:620474]] So I hope that with some of these reasons, I convinced you that modeling theory of mind is very relevant at the moment.
[[start:620672][end:623260]] And there have been a lot of people already on this.
[[start:624270][end:639870]] And I've created this very global overview of some approaches that are representative or some models that are representative of their more general approaches.
[[start:641590][end:658390]] There's this brain Tom model which aims to basically build up clear mind abilities and abilities facilitating social interaction from the bottom up using Biphysical models of neural firings.

10:59 [[start:659850][end:662450]] That's why I've placed it on the dynamic scale.

11:02 [[start:662530][end:683470]] So I've tried to align these modeling approaches along the axes of how they treat time, how broad their description is from the individual level to maybe describing more broader social and cultural processes and along the level of description from the molecular biophysical to the behavioral.
[[start:684450][end:703890]] And one thing you can see is that there is a lot of work based on invasion inference and active inference that moves along that has relevant ties to the molecular and neurobiological level but moves along the lines of making behavioral and cognitive predictions.
[[start:705050][end:716040]] And there are very little models that really also formalize the concrete implementation of theory of mind.
[[start:716990][end:733366]] And there is also, I think, this need for connecting this dynamic implementational level to individual level social cognition and putting that in the context of social interaction more generally.

12:13 [[start:733558][end:748594]] So some of the representational approaches that I selected are the TOMNET, which basically uses neural network embeddings to train reinforcement learning agents.

12:28 [[start:748792][end:764562]] We have Ktom, which is a Bayesian recursive model which I'll come back to later, some or theory of mind with self other modeling uses multiagent reinforcement learning with goal inference.
[[start:764706][end:778540]] And we have the more theoretical active inference model of implicit cultural learning called thinking through other minds, which could be seen as an alternative or a redefinition of theory of mind.

13:01 [[start:781250][end:793300]] Okay, so to sum up, we have this stream of biophysical models, most notably Brain Tom, which was developed by Zhao et al.

13:13 [[start:793990][end:821290]] And its strengths are its neurobiological plausibility at making dynamic predictions about neural activation in populations that are associated with theory of mind abilities and its weaknesses is that it's quite computational and costly and it's probably difficult to implement in an interactional setting.

13:43 [[start:823550][end:839550]] There are some deep learning models such as Tomnets by Rabinovitz and Self other modeling which I just mentioned that are also quite neurobiologically plausible and also make some dynamic predictions.
[[start:840210][end:874618]] But there is this strong danger of shortcuts, which has been addressed in deep learning models, that the task might not be solved by learning the relevant ability of being able to infer another agent's goals or beliefs, but just by learning simple lower level associations between, for example, the perspective or how another agent stands and where, for example, a food reward would be.

14:34 [[start:874704][end:888270]] So there are a lot of ways to solve the task and there's this finding that deep learning models sometimes use these kinds of shortcuts so that's something that's needed to be addressed.
[[start:889570][end:905222]] Then there are some Bayesian belief based models such as K Tom for Recursive theory of Mind and Beijing Tom which was originally developed by Baker et al.
[[start:905276][end:929600]] In 2011 and its strengths are that it's quite efficient, it's very easy to interpret and its weaknesses are that the road to the implementational level is longer and it requires many priors and there's this question about whether it's scalable because of the prior specifications that you have to give.

15:32 [[start:932450][end:944100]] Okay, so as one of the I think the interesting newer developments on a theory of mind wait, yes.

15:46 [[start:946630][end:959878]] Is Hierarchical active Inference for collaborative agents which has been recently published and Haika is based on the Asian theory of mine by Baker et al.
[[start:960044][end:983790]] But it adds this formalization of belief resonance which is the incorporation of beliefs about another's intentions with top down predictions and this influence of these other agents beliefs are modulated by susceptibility parameter which controls this influence.
[[start:985170][end:996340]] And what I find I think it's important to note here that they use an approach based on active inference but they don't use the free energy principle for example.
[[start:997510][end:1002702]] So they do couple perception and action but just in a different way using a karma filter.
[[start:1002766][end:1014150]] So the way they formalize this is slightly different but I think the overall structure can still be informing or inspiring for active inference methods.

16:55 [[start:1015950][end:1034720]] So what is interesting about their simulation results is that they show that agent that there is some emergent collaboration on tasks for low values of the susceptibility parameter without any explicit planning or communication needed.
[[start:1035250][end:1055750]] And this means that they improve upon the original Bayesian model, which explored different sort of overall plans for all of the agents, which means that an agent employing Bayesian Tom would need to reason about the roles of all of the other agents, which was very costly.
[[start:1056170][end:1065640]] And the authors wanted to improve on that to model maybe on the fly coordination, which is more spontaneous and takes less time.
[[start:1066650][end:1073980]] And they also show that incorporating belief resonance has a very positive effect in scenarios in which there's unbalanced information.
[[start:1074750][end:1084720]] They did this simulation, the overcooked domain in which agents have to collaborate on different cooking tasks and the goal is basically the order, the cooking order.

18:05 [[start:1085170][end:1089920]] And then the intention would be any kind of action that has to do with completing the order.
[[start:1090930][end:1103650]] And they show that incorporating the leaf resonance seems to be especially useful in situations with unbalanced information which, for example, one agent knows the order and the other doesn't.
[[start:1104170][end:1120650]] And these agents develop some kind of leader follower dynamic in which one is more susceptible to the other agent's intentions and one agent attends more to the evidence from the environment.
[[start:1121390][end:1133870]] And this also aligns with what we know about your mind mainly being employed in situations in which there is some asymmetry in what the agents know about the environment.
[[start:1134210][end:1137230]] So I thought that was very insightful.

19:01 [[start:1141090][end:1152260]] Okay, so I'm going to go into some active inference approaches that I think are relevant for developing active inference theory of mind.

19:12 [[start:1152630][end:1166742]] First of all, there's this very broad proposal on inculturation and non development thinking for other minds, a variational approach to cognition and culture, which we'll go into a little bit.
[[start:1166876][end:1175610]] We'll go into Castle and HAF's paper on ideas for spreading a free energy proposal for cumulative cultural dynamics.
[[start:1176510][end:1178658]] We'll go into Kaufman et al's.
[[start:1178694][end:1186990]] Model on collective intelligence and finally also the proposal by Mutusis et al.

19:47 [[start:1187060][end:1190080]] On Beijing inferences about the self and others.

19:53 [[start:1193100][end:1207900]] Okay, so first of all, I am starting with beta inference about the self and others because it gives a very sort of broad introduction to, I think, predictive social cognition.
[[start:1208320][end:1234340]] And that's also why I've added this figure on the right that is from the Tam Thoughts and paper in 2018, which explores the predictive social brain and what kind of features seem to be relevant for categorizing and understanding others behaviors.

20:36 [[start:1236920][end:1254644]] Some figure on the right, you see that there is this space, this trade space, which is ordered by power, sociality and balance, and that constraints the state space which seems to be ordered by rationality, social impact and balance.
[[start:1254772][end:1261340]] Of course, these are just correlations, but these futures seem to be most predictive of what they're seeing in the brain.
[[start:1262560][end:1276480]] And you can see that there is this sort of basically a very strong top down constraint of the possibility space in which you interpret other people's actions.
[[start:1277060][end:1289252]] And you can also see that based on another agent's actions, you learn something about where they fall within that space in a given context and also where they fall in that trade space.
[[start:1289306][end:1300104]] What kind of so at the same time, you might have already have some priorities on what kind of a person this is, but you're also learning about it.

21:40 [[start:1300302][end:1308472]] You might also have some priors on how someone behaves when they're mad, for example, or when they're sociable versus unsociable.
[[start:1308616][end:1311384]] And all these kinds of priors informative priors.
[[start:1311432][end:1321440]] They inform your predictions in the context, and they make this task much more manageable of predicting other people's behaviors on the fly.
[[start:1322740][end:1343130]] And I think that links very well back to Mutuses proposal, which is basically that inferences about the self and others at different timescales facilitates interpersonal minimization of surprise and thereby optimal social decision making.

22:26 [[start:1346460][end:1363260]] And these self and other representations that facilitate personal minimization of surprise could be seen as representations that inform our inferences and predictions on the fly.

22:46 [[start:1366720][end:1384064]] I think it's also important to mention that one of the main key points of their paper is that self representation, so beliefs about how beliefs about the self can facilitate interpersonal minimization of surprise.
[[start:1384112][end:1399080]] So even what I think about me and how I represent that, while communicating, will facilitate the other person's optimal decision making at that moment, maybe by providing the right kind of information that they need to optimize.
[[start:1400140][end:1409032]] Okay, so to the next two interesting papers, ideas Worth spreading and an active inference model of collective intelligence.
[[start:1409176][end:1417580]] So the key idea, I think, for both of these papers is the emergence of group behaviors from local interactions.
[[start:1417920][end:1427840]] For Caston Hess, this is the global group behaviors cultural transmission or transmission of beliefs and norms.

23:48 [[start:1428180][end:1434980]] And they describe this process as the mutual achievement of actively inferring agents through communication.
[[start:1435400][end:1442128]] And theory of mind is one of the many mechanisms that facilitate this process of achievement.
[[start:1442304][end:1443590]] So that's the link.
[[start:1444040][end:1458680]] And they show that the spread of certain kinds of beliefs through a group can be modeled just by making agents interact in diadic groups and stimuli.
[[start:1459100][end:1460116]] Kaufman et al.

24:20 [[start:1460158][end:1486230]] Show that you can create a system of free energy minimizing agents with some minimal properties of social intelligence, such as the ability to assess how self similar another agent is to themselves, the ability to infer another agent's intentions, and the ability to align their goals to another agent, more or less.
[[start:1486760][end:1498520]] And they show that if you put all of these agents together in those diets, they don't only minimize free energy on the dietic scale, but they also minimize free energy as a collective.

24:59 [[start:1499500][end:1515580]] And thereby, this is a very simple model of how adaptive behaviors, group adaptive group behaviors, could emerge from agents with very simple social abilities.

25:30 [[start:1530020][end:1557240]] Okay, so now we get to thinking through other minds, which is not technically a proposal for theory of mind, but it's a proposal for how social cognition shapes inculturation more generally and what kind of abilities agents need to facilitate this kind of normation.

25:59 [[start:1559340][end:1572060]] And I think it's a very interesting proposal because I think it highlights an important function of social behavior more generally.

26:12 [[start:1572720][end:1581680]] And you could even see it as a way to redefine theory of mind as more of an interactional concept than as an individual level cognitive ability.
[[start:1583220][end:1596260]] So, according to this proposal, thinking through other minds is a property of multiple interacting minimizing agents and a process by which agents infer other agents expectations.
[[start:1596840][end:1613160]] And based on this, the authors propose a definition of enculturation as a process of learning social expectations through the selective patterning of attention that guides agents towards relevant affordances within their social and cultural niche.
[[start:1614460][end:1621532]] I'm not sure if you're all familiar with the concept of affordances but it was quite hyped up a couple of years ago.

27:01 [[start:1621586][end:1633272]] In general it is defined as relational construct denoting possibilities for action offered by an environment that are code determined also by an agent's interest, goals and abilities.

27:13 [[start:1633416][end:1647140]] So I think that the standard example for this is when you are thirsty, a glass of water might appear as an affordance or you might not consciously or might also tend to it otherwise.
[[start:1647960][end:1653540]] And cultural affordances in this sense are epistemic affordances.
[[start:1654360][end:1663160]] So affordances that give you some epistemic value that have come to stand out as reliable and relevant based on a history of culture information they encode.
[[start:1663580][end:1668300]] And good examples for this are different kinds of signs of traffic signs.

27:48 [[start:1668720][end:1683520]] We learn what they mean from a young age and we sort of inherited the symbolism of the traffic signs and they guide our intention towards points in traffic and they regulate our behaviors.

28:05 [[start:1685940][end:1705248]] So when you look at the complete proposal, it sketches how the regulation of social behavior depends on the learning of shared norms and expectations and also how this connects to utilizing cultural affordances and thinking through other minds.

28:25 [[start:1705424][end:1717070]] As this profits interactional processing, in which agents learn to infer each other's expectations to optimize collective behavior and decision making.
[[start:1718480][end:1726524]] Okay, so from these interesting active inference and broader proposals of fear of mind we get to the issue of form.
[[start:1726562][end:1730544]] Sophistication in active inference so what is fear of mind?
[[start:1730582][end:1739312]] Sophistication a short recap it's the depth of reclusivity that can be utilized for fear of mind of the form.

28:59 [[start:1739366][end:1765640]] I think that they think that I think, and it has been found that agents generally use a reclusivity of between zero and four and that humans, humans ability for recursive belief reasoning is generally limiting but in principle, formally this could go on forever.

29:27 [[start:1767120][end:1780430]] And one way to implement this kind of sort of arbitrarily recursive belief inference is proposed by Vada et al.
[[start:1781200][end:1796148]] Uses a Bayesian model of sophisticated theory of minds with Ktom agents and provides simulations in which K tom agents play against agents that are just one level of recursivity under them.
[[start:1796234][end:1802352]] And this model has been used for a lot of interesting simulation experiments.
[[start:1802416][end:1803190]] For example.

30:04 [[start:1804380][end:1830690]] Devane Et Al Showed that in a trade based analysis but with agents having a fixed depth of theory of mind reclusivity there is a specific distribution of agents with level one tom and level two tom that could provide an evolutionary advantage compared to populations with larger proportions of serotonin three tom agents.

30:31 [[start:1831140][end:1843220]] So they look at the adaptive properties of systems with different kinds of ratios of theory of my sophistication.
[[start:1844600][end:1857184]] And in another experiment, which is a state based analysis for Joe et al.
[[start:1857242][end:1874380]] Showed that if you use computational phenotyping on autistic individuals, this shows reduced sensitivity to task framing and strategy switching within the game that they'll be using and theoretical line sophistication.

31:16 [[start:1876640][end:1883100]] So these are just some interesting applications for theoretical mind sophistication.
[[start:1883760][end:1898416]] And the promise of modeling theoretical mind sophistication would be that you could investigate how people flexibly switch between different social strategies while solving a social task.

31:38 [[start:1898608][end:1909172]] And one of them would be to increase the depth of fear of my sophistication or decrease it depending also on what you think about the other agent's.
[[start:1909236][end:1910360]] Sophistication.

31:54 [[start:1914140][end:1921870]] So what I've been working on at the moment is an active inference model of social prediction during the Matching pennies game.

32:04 [[start:1924080][end:1933132]] The matching pennies game is a game farm economics with a very simple format.
[[start:1933196][end:1934076]] There are two rules.
[[start:1934108][end:1936044]] You have the guesser and the challenger.
[[start:1936172][end:1939744]] The challenger hides a penny in one of the two hands.
[[start:1939942][end:1948656]] The guesser needs to guess which hand, if the guesser is correct, they win, if the guesser is wrong, be challenger wins.

32:28 [[start:1948848][end:1952580]] This game has some logical equivalents.
[[start:1953800][end:1958964]] One version of the game makes both of the agents select heads or tails.

32:39 [[start:1959012][end:1964708]] So the challenger selects heads or tails and the getter guesses the tests or tails.
[[start:1964884][end:1967820]] But both have the same formal structure.
[[start:1968640][end:1977788]] And psychological experiments of subjects performing this task have shown that there is a strong social framing effect in the Matching Pennies game.

32:57 [[start:1977874][end:1988050]] So participants will behave and perform differently depending on whether they're seeing that they're playing against a human agent versus an AI for example.

33:10 [[start:1990980][end:2007876]] Additionally, a comparison of Ketone and other computational strategies that were fitted on experimental data of subjects playing the game revealed that participants seem to use fear of mind when playing the game.
[[start:2007978][end:2023180]] So there is a strong indication that theory of mind use does play a role in the Matching pennies game and that social framing will influence the social strategy that's being employed by the players.

33:45 [[start:2025440][end:2031744]] So this is the very simple zero sum architecture for the Matching pennies game.
[[start:2031942][end:2049510]] And I included beliefs about self choices as also kind of monetary self states beliefs about other agents choices on whether the agent thinks the opposing agent has hidden the penny left or right.
[[start:2050040][end:2053140]] And then the agent also tracks the war dates.
[[start:2055020][end:2072670]] Since the game in this setting is devised in a way in which the agents both make an observation simultaneously and then all of the observations are revealed, this set up made sense so just going to drink a little water.

34:38 [[start:2078260][end:2095108]] The outcome modalities or observations that the agents have are its own choice observations, the choice observations of the opposite agent and the reward observations and the possibility the action space is very limited.

34:55 [[start:2095284][end:2112750]] The seeker can choose to seek left or right and the hider which is the same as the challenger before, has the possibility of hiding penny left or right and the reward is uncontrollable since it depends on both agents choices at the same time.

35:16 [[start:2116240][end:2116556]] Yeah.
[[start:2116578][end:2129628]] So this is sort of a summary of the architecture that I just described and this is another visualization of this setup.
[[start:2129724][end:2141780]] And you can see here that if you look at the likelihoods the reward mapping for the seeker is just the opposite as for the hider.
[[start:2142920][end:2155160]] And I think that this simple setup is very suited for studying fear of mind in these kinds of simple competitive interactions.

35:57 [[start:2157600][end:2182772]] Okay, so if you wanted to study the use of theoretical bind sophistication in the matching penny scheme using active inference, I ran into a couple of challenges and one of them was how to steer the problem of recurring s.
[[start:2182906][end:2189110]] So how can we make a difference between the focal agent and the other agents?
[[start:2189960][end:2204504]] If we try to model the other agents within one agent, especially if you want to introduce or formalize desperate cave reclusivity, you can't just make one agent simulate the other agent simulating their self.
[[start:2204622][end:2221330]] There needs to be some kind of sort of structure that distinguishes the self inferential mechanism, a self learning mechanism from what the agent focal agent thinks the other agent is thinking and seeing and doing.

37:02 [[start:2222340][end:2229728]] And I think the gentleman with the bowler hat by firster in 2003 is a good example for this problem.

37:09 [[start:2229814][end:2244624]] So the basic setting is that our world is populated by beings like ourselves experiencing themselves as a subject, as the focal point of their world, with their own thoughts and feelings.
[[start:2244672][end:2248600]] And they all think that they're the one and only subject.

37:30 [[start:2250780][end:2252344]] But there can't all be.
[[start:2252382][end:2259100]] So there needs to be sort of either an outside focal point or one ultimate main subject.

37:41 [[start:2261600][end:2281890]] I think more practically, the questions that arise from this example are how do we distinguish between focal agents and simulated agents and how can we simulate other agents in a way that is computationally efficient and maybe uses the same kinds of resources that the agent already has?

38:07 [[start:2287120][end:2304736]] So I actually had a lab meeting at the Theoretical Neurobiology Lab a while ago and we were brainstorming about this issue and one of the ideas that came up was to use sophisticated inference for period mind.
[[start:2304918][end:2312870]] So in this case, an active inference formulation of belief recursivity could be used for modeling recursive period, line.

38:35 [[start:2315960][end:2343790]] Basically, serious planning using predictions about the other agents into account would consist of evaluating all the kinds of hypothetical scenarios, all kinds of counterfactuals on how your actions might influence their beliefs and their actions and so on and so on.
[[start:2345440][end:2347980]] So this would be one road to go into.

39:08 [[start:2348050][end:2353440]] But this would also mean that all these counterfeituals would need to be evaluated.
[[start:2353860][end:2367060]] So I was thinking is there a sort of more efficient way to sort of use these kinds of either internal simulations or kind of special evaluation?
[[start:2368680][end:2378276]] And the current approach I'm working on, which I'm also sort of still developing.

39:38 [[start:2378308][end:2388910]] So I'm very much open to feedback and comments on how this could work and possible alternative approaches at this point.
[[start:2389600][end:2398188]] But the general idea would be to create a partial internal simulation of the other agent's control mechanism.
[[start:2398364][end:2442750]] So taking the learning mechanism of an active inference agent as sort of the definition of what the focal agent is, that is the agent that perceives and learns and infers from the environment and what the agent does when predicting the observations of the other agent or the predicting the other agent's behavior is basically performing partial simulation about what it thinks the other agent preferences are and what it thinks that the other agent strategy is, which is encoded by the transition from state to state.

40:45 [[start:2445120][end:2459860]] And one of the potential ways in which you could include reclusivity in this way is that you pretend that you have control over the other agent's actions and you predict the other states.
[[start:2459930][end:2486300]] You predict self states, you evaluate the state action probabilities, choose the most valuable action based on that distribution, simulate the other states that come forth and simulate the self states that come forth.
[[start:2487040][end:2497730]] And then you have a new and then this can be used for the next round of action selection by the other model.
[[start:2498580][end:2512230]] So in this case, only the per preferences and the agent specific transition probabilities would be needed as sort of information on the other agent.

41:52 [[start:2512760][end:2525860]] And because you also want to include some kind of learning about the other agent strategies, one of the things you could implement would be learning also the Bay metrics.

42:06 [[start:2526380][end:2544220]] So having sort of the specific having the agents accumulate as evidence about these state transitions over time to also better predict the other agents potential actions.

42:26 [[start:2546420][end:2570032]] The basic principle would be to simulate control from the perspective of the other agents and the recusivity comes into play when you simulate the other when you've already simulated the others predicted actions and predicted other states and you've simulated your own actions as a consequence of those simulated actions.
[[start:2570176][end:2582010]] You can feed that back into the other model to predict what they would do if they thought that you were in the state that you were in.

43:03 [[start:2583100][end:2598850]] And I think that could be a way to develop repressivity in a way that does not need complete simulations of parallel agents within the same system.
[[start:2600340][end:2617540]] And of course there should be some kind of temporal discounting subparameter that discounts evidence based on the simulated planning horizon that is defined by the K number of steps.
[[start:2618600][end:2645260]] So yeah, this is sort of a conceptual outline of how you could implement because the fear of mind using active inference we haven't been able to perform simulations using this yet, but we're working on that and we're very much open to discussions on this and technical comments on how to improve on this outline.

44:06 [[start:2646640][end:2657536]] And one of sort of the open questions that we are still thinking about is how to make the agent effectively infer the depth of reclusivity of the other agent in.
[[start:2657558][end:2658480]] A setting.
[[start:2659080][end:2659492]] Yeah.
[[start:2659546][end:2670470]] Special thanks to Guillaume Dumas, who will also be there at a panel, I think, in session two, who's supervising me during this project.
[[start:2671080][end:2691420]] Thanks to the PPSP labor, I'm doing my internship to Rudy Said, who's also working on a related project, the Pi MDP team, for that great coding package that I'm using, and for Kofristen for his feedback and ideas on my previous presentations.

44:56 [[start:2696200][end:2697940]] Thank you very much for listening.
[[start:2699580][end:2700330]] Cool.

45:02 _Daniel:_
[[start:2702140][end:2703620]] Great presentation.
[[start:2703780][end:2712970]] Very comprehensive review of a lot of the different theory of mind options out there.
[[start:2714560][end:2719000]] Well, if anyone has questions, they can write it in live chat.

45:19 [[start:2719160][end:2720680]] What do you want to explore?
[[start:2720760][end:2724770]] Or can I ask a question or what would be fun for you?

45:28 _Nynke:_
[[start:2728740][end:2735040]] I'm blinded by the light at this point, so I can't easily read from my screen.
[[start:2735110][end:2741484]] So maybe it would be nice if you could read out the questions that are the live chat.
[[start:2741612][end:2741904]] Sure.

45:41 _Daniel:_
[[start:2741942][end:2743030]] Oh, yeah, sure.
[[start:2743640][end:2753288]] Well, first one part I found interesting, you mentioned that people play differently when they are playing a human or when they believe that they're playing a human.

45:53 [[start:2753454][end:2757240]] So what is that like?
[[start:2757390][end:2764350]] What is the difference in play when we believe that we're playing another person?

46:15 _Nynke:_
[[start:2775920][end:2808820]] If I look at the original paper, there is one study on this, and then they did the computational phenotyping study using Ktom and alternative strategies, and they showed that if you use the social framing condition, that subjects will more probably employ figure five strategies compared to other simple reward based strategies.
[[start:2809160][end:2814100]] So maybe those strategies could better be described using some kind of reward learning mechanism.

46:56 [[start:2816140][end:2822490]] What the difference in their overall sort of trajectory of choices is, I don't know.

47:05 _Daniel:_
[[start:2825740][end:2826116]] Yeah.
[[start:2826158][end:2831912]] A few themes then that you brought up that came up earlier in the session.
[[start:2831976][end:2839984]] So one was using Pymdp and sophisticated inference, which Aspen Paul gave a walkthrough on.
[[start:2840182][end:2862980]] And this question about recursivity and about the way in which you can on one hand talk about abstractly like K Recursivity, yet the biological system doesn't implement that kind of a logic.
[[start:2864360][end:2866328]] Could you maybe describe a little bit again?

47:46 [[start:2866414][end:2881150]] How does the structure that you laid out for the generative model capture some of those features of recursivity without falling into the trap of just theory of mind all the way down?

48:03 _Nynke:_
[[start:2883360][end:2883724]] Yes.
[[start:2883762][end:2904580]] So my general idea was to simulate the other agent's action prediction based on learning about the transition probabilities for what we think how the other agents face transition.
[[start:2905960][end:2920250]] And then if you've predicted what the other agent would do, you can use that as a prior for calculating action dependent expected states.
[[start:2921340][end:2928620]] And based on those evaluating those expected states, you simulate your own choice mechanism.
[[start:2930560][end:2940720]] And I think in principle, you could use this recursive simulation indefinitely.

49:02 [[start:2942820][end:2956450]] But also, it's also devised in a way that it uses the same kind of sort of just the architecture of the focal agent.

49:16 [[start:2956820][end:2976176]] So the other idea was to just use internal simulations all the way down and but that would be very cognitively implausible and yeah, I think it's a very good question, because why would you even need to formalize belief?
[[start:2976228][end:2977996]] reclusivity all the way down.
[[start:2978098][end:3000400]] If in end effect, people only use tom with a set sort of maximal depth and the fact that we use fear of mind with a maximum depth might also be sort of a hint that he might also use a different or what we do might also be described by a different strategy.

50:03 [[start:3003060][end:3006230]] So yeah, I'm not sure if that's an answer to your question.

50:08 _Daniel:_
[[start:3008440][end:3032344]] Yeah, well when I saw this and some of the other generative models you mentioned maybe here like you pretend like you can control the other person's mind and that's kind of the fundamental weaving of action into the inference challenge and then that uses expected free energy just like any other policy selection.
[[start:3032472][end:3053488]] So it's like pragmatic value would be bringing that controllable state your social partner's mind or beliefs bringing them into alignment with your preferences is pragmatic and then learning more about them is epistemic.
[[start:3053664][end:3069672]] And so then that might enable some theory of mind like behavior where it's like when you don't know enough to put the squeeze on then you have a kind of open ended learning and curiosity and question driven theory of mind.

51:09 [[start:3069806][end:3094640]] But then once one has enough to kind of exploit rather than explore then without necessarily even updating the model or engaging any deeper recursivity or strategic shifting you could get social behavior that's oriented towards control and pragmatic value rather than just like learning and questioning.

51:36 _Nynke:_
[[start:3096740][end:3098832]] Yeah, I think you're very right.
[[start:3098966][end:3120950]] The idea was also to enable the agent to maybe first use strategies that are more useful in gathering evidence about the kinds of strategies that the other agent is using before exploiting thing what you've learned about the other agent and.
