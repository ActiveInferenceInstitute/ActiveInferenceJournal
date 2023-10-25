
00:01 _Daniel:_
[[start:1210][end:2000]] All right.

00:08 [[start:8080][end:9740]] Greetings, Takuya.

00:10 _Takuya:_
[[start:10640][end:11390]] Hi.

00:14 _Daniel:_
[[start:14000][end:20860]] You can mute the live stream or turn off the other live stream, but yeah, thank you for joining.

00:22 _Takuya:_
[[start:22080][end:26220]] Yes, thank you for inviting thank you for it.
[[start:26290][end:28150]] Yeah, it.

00:30 _Daniel:_
[[start:30440][end:42760]] Well, we have a little bit 35 or 38 minutes, so it would be awesome to have your presentation.

00:45 _Takuya:_
[[start:45500][end:46250]] Great.
[[start:46620][end:59630]] So the moment well, can you see my.

01:01 _Daniel:_
[[start:61760][end:63420]] I saw PowerPoint.

01:06 _Takuya:_
[[start:66880][end:67630]] Okay.

01:09 [[start:69840][end:71870]] Can you see my screen?

01:12 _Daniel:_
[[start:72320][end:73070]] Perfect.

01:14 _Takuya:_
[[start:74240][end:74990]] Okay.
[[start:76480][end:78300]] So shall we start?

01:18 _Daniel:_
[[start:78450][end:78908]] Yes.

01:18 [[start:78994][end:79870]] Thank you.

01:21 _Takuya:_
[[start:81620][end:82368]] Then.
[[start:82534][end:88476]] Thank you for organizing this wonderful symposium.
[[start:88588][end:107792]] Today I'd like to talk about relationship between canonical neural network and active inference and possible extension for modeling social and shared intelligence using canonical neural network.
[[start:107936][end:109670]] So let's start.

01:56 [[start:116250][end:132874]] As you know, the free energy principle is proposed by Karl Friston that states that perception, learning and action of all biological organisms are determined to minimize variational free energy as a tractable proxy for surprise minimization.
[[start:133002][end:143040]] And by this process organism can perform parational BJ inference or external mineral state.

02:23 [[start:143650][end:152494]] And this can't even just show one example typical set up under the free energy principle active inference.
[[start:152622][end:163030]] Here there is a hidden state in the external world and only a part of this state can be observable.
[[start:163370][end:187690]] For our agent, this doc and this transformation is done by genetic model parameterized by theta and to infer the hidden state, agent need to reconstruct the copy of the external state called posterior relief.

03:07 [[start:187770][end:193440]] And this optimization is done by minimizing variational free energy.
[[start:194450][end:204580]] And parameter is also optimized by minimizing free energy to obtain an apt generative model to represent this relationship.

03:25 [[start:205030][end:213042]] An interesting aspect of the free energy principle active inference is its application to the optimization of action.
[[start:213186][end:237150]] Here our agent have some preference prior c and to obtain this observation in the future, agent may select the action that minimize the expected free energy in the future to obtain the most predictable outcome.
[[start:237810][end:246206]] And finally, by selecting actions that minimize the expect frequency, it can obtain the feed.

04:06 [[start:246398][end:250206]] So, this is a typical setup under active inference.
[[start:250238][end:256258]] But question is what is the neural neurosurge that can implement this process?
[[start:256344][end:264306]] So that is our interest and to address this issue we propose theory as follows.
[[start:264418][end:284874]] Here we consider that external world is parameterized characterized by a set of the variables like this here, this is a posterior expectation and the S indicates the hidden state in the external world.

04:44 [[start:284992][end:298046]] Delta indicate the action of the agent or decision and the theta indicate a parameter and lambda is a hyperparameter.

04:58 [[start:298238][end:310546]] So those set of parameters or variables characterize a generative model and free energy variational.
[[start:310578][end:323930]] Free energy is defined as a function of the sequence of observation and external state and its minimization indicates the variational Bayesian inference.
[[start:325470][end:336778]] Similarly, we consider a dynamics of neural network and we consider that dynamics is characterized by a set of those variables.
[[start:336874][end:359266]] Here x indicates the neuroactivity firing rate at middle raya neurons and y indicate neuroactivity of output raya neurons and W here is a synaptic weight and phi is any other free parameter that characterize neural network.

05:59 [[start:359458][end:367894]] And we consider that neural network dynamics is characterized by minimization of some cost function l.

06:08 [[start:368012][end:385470]] This is a function of the O and Phi internal state of neural network and its minimization indicates the generation of neural network dynamics including both activity and plasticity.
[[start:385810][end:392378]] And our theory indicates equivalence between those two functions.
[[start:392554][end:403710]] Meaning that for any neural network that minimize some cost function error, there is a generative model that satisfy if we call error.
[[start:403870][end:418418]] Which means that the recapturation of external dynamics is an inherent feature of any neural system that follow such dynamics.
[[start:418594][end:423910]] So this is an interesting prediction but too abstract.

07:04 [[start:424730][end:434430]] So I would like to introduce some analytically tractable example to understand this relationship formally.
[[start:435250][end:439626]] So first we consider a very simple architecture.
[[start:439818][end:445710]] This is represented by POMDP without any state transition.
[[start:445790][end:457958]] So hidden state s is simply generated by priya distribution D and it is a binary state.
[[start:458124][end:492542]] But we consider a vector of binary state, so it is a factory of structure and observation is also a binary vector and the transformation from S to O is characterized by categorical distribution using likelihood of matrix A and variational Bayesian inference indicates the inversion of this generative process like this.

08:12 [[start:492676][end:505620]] So by solving the appropriate frequency functional we obtain those posterior brief that is optimal in the Bayesian sense.
[[start:506890][end:522134]] On the other hand, for neural network we consider such structure here upper part indicates the generation of signal in the external world and the neural network comprises only single layer.
[[start:522262][end:534478]] Here activity of output layer are generated by weighted sum of sensory input O weighted by synaptic matrix W.
[[start:534644][end:540590]] And we then characterize this neural network in the next slide.
[[start:541010][end:564406]] So to model neural network or neuron, we start from considering hodgeken hacksray equation which comprises four differential equation and this is a very complicated non linear equation although it is barely possible.

09:24 [[start:564508][end:568818]] So we consider some reduction of these equations.
[[start:568994][end:598462]] So a typical reduction method is like this for example, m here is much faster than other variables so this can be repressed with its fixed point or it is known that h and minus one sorry, it is known that h and one minus SN have similar dynamics.
[[start:598526][end:612214]] So we can consider a new effective variable U to characterize those two variables and then we obtain 2D hoskin hacks ray equation like this.
[[start:612332][end:637998]] So this is a famous cross of neural network model which includes the well known Fitzfuel Nagamo model or other continuous neural network model and we modify those model to derive canonical neural model.

10:38 [[start:638164][end:643630]] So this is a definition of canonical neural network model.

10:43 [[start:643780][end:657102]] Here leak current is characterized by imbass sigmoid function instead of cubic function which is adopted in the Fitzfuel Nagmo model.
[[start:657256][end:689200]] And we also consider connection synaptic connection and this part indicates synaptic input from sensory layer through weight matrices and 1 may consider that W one indicate excitatory synapse and W zero indicate inhibitory synapse and the threshold are adaptive thresholds that are function of W one and W zero.
[[start:689810][end:703380]] Interestingly, when we consider a fixed point of this differential equation we obtain well known red coding model with the Sigmoidal activation function.

11:45 [[start:705190][end:729850]] Which means that we can say that in some sense this canonical neural network network model is approximation of Hodgkin hatt's ray equation and its approximation level is, in some sense between the realistic model and the most simplified red coding model.
[[start:730000][end:745300]] So we basically consider this type of neural network model and in the next slide we consider what is the plausible cost function for this neural network model.

12:25 [[start:745670][end:782730]] So again we write the same equation for canonical neural network model which represents the activity of neurons vector of neurons and we consider cost function for this differential equation which can be obtained by simply calculating the integral of right hand side of this equation and get this type of cost function for neural network.

13:02 [[start:782890][end:794350]] This is biologically plausible cost function in the sense that its derivative derived neural network activity which has a certain biological plausibility.
[[start:794870][end:812760]] Moreover, if we consider derivative of this cost function with respect to synaptic weight W, we obtain a conventional synaptic plasticity rule which follows Hebian law.
[[start:814410][end:836030]] On the other hand, for Bayesian inference we first define generality model like the previous slide and we then derive variational free energy for given genetic model.
[[start:836100][end:852340]] So this variation of free energy is derived from the Pom DP model in the previous slide and its minimization indicates the Beijing inference and running.

14:12 [[start:852870][end:866262]] So we found formal correspondences between component of those two cost functions like this.
[[start:866396][end:895662]] So this broke vector formally correspond to this Brock vector that represent a posterior expectation and this logarithm correspond to this logarithm and actually this a matrix can be represented as the broke matrix like this and its dot product correspond to this computation.
[[start:895806][end:905730]] And finally, this phi naturally correspond to this log d logo state prior.
[[start:906310][end:927080]] Which means that because the cost function are same, its derivative provides its derivative provides sorry.

15:27 [[start:927790][end:936640]] Because the cost function are formally equivalent, its derivative sorry.

15:37 [[start:937010][end:943440]] It's a result of derivative also corresponding each other.
[[start:944550][end:954590]] Which means that for any neural activity equation in this form, there is a corresponding Bayesian inference equation.
[[start:954670][end:969618]] This is an equation that compute the posterior belief of the hidden state and this synaptic practice equation formally correspond to learning or parameter of genetic model.
[[start:969804][end:1000210]] And moreover, by establishing this relationship we can consider the reverse engineering of the generality model from empirical data here this schematic summarize our approach to reverse engineer generative model and we first record the neural activity and assign the canonical neural network to explain this obtained data.

16:40 [[start:1000360][end:1006650]] And by computing the integral we obtained a cost function for this canonical network.

16:46 [[start:1006830][end:1022054]] And by the mathematical equivalence we established, we can automatically identify genetic model and variational free energy that correspond to this neural network architecture.
[[start:1022182][end:1032458]] So interestingly, this is a Bayesian agent which is a kind of artificial intelligence.
[[start:1032554][end:1039198]] But importantly, this artificial intelligence is formally derived from empirical data.
[[start:1039284][end:1074780]] So we can say that this agent is biomimetic artificial intelligence that follow the free energy principle and then its derivative with respect to parameter posterior derived synaptic plastic algorithms that follow the free energy minimization and its time integral can predict the running process of original neural network data.

17:55 [[start:1075390][end:1096866]] Which means that if the frequency principle is correct, then this prediction should work, should work and should be able to predict the result of this neural neta without referencing to the data itself.

18:17 [[start:1097048][end:1143002]] So our strategy is in summary, our strategy is that we reconstruct generative model only from the initial data, like initial data before running and then predict the running process or running curve that this neural system should follow by using the frequency principle and compare or examine whether this prediction is correct by comparing actual data after running and the prediction by the free energy principle.

19:03 [[start:1143146][end:1152850]] And if this prediction is correct, then it indicates the predictive validity of the free energy principle under setup considered.
[[start:1154230][end:1159330]] So we apply this strategy to the in vitro neural network.
[[start:1159410][end:1170142]] So here, this in vitro neural network are stimulated using the POMDP generative process defined in the previous slide.
[[start:1170226][end:1184890]] So there are two hidden sources that are binary signals and they are mixed to generate 32 sensory stimuli.

19:44 [[start:1184970][end:1187630]] Those are also binary.
[[start:1188450][end:1205726]] And this is an overview of experiment by stimulating in vitro neurons they generate spiking response and those rhyme indicate a high density spiking response.

20:05 [[start:1205918][end:1234186]] So we observed that in some neuron the response specificity is so we found that for some neuron response was high to source one signal compared to source two signal.
[[start:1234378][end:1277866]] And if we see the transition of those neurons, we found that although we removed the offset at the first session to set those activities zero, but we see that those neuron self organized to respond high when source one is one, but those neurons response low level when the source one is zero.

21:18 [[start:1278048][end:1297714]] So which means that those neurons activity, those neurons response was consistent with our theoretical prediction that neuroactivity cell organized to encode the posterior expectation of healing state.

21:37 [[start:1297832][end:1306740]] And we also found that some other group of neuron responds preferentially to source two but not to source one.
[[start:1308090][end:1345540]] So then we ask okay, then we found that posterior expectation is encoded by neuroactivity and the next question is about other neuronal substrate and we then ask if the prior brief about hidden state is effectively equal to the firing threshold of neural activity model, neural network model.

22:26 [[start:1346230][end:1351810]] So if the theory is correct, this correspondence should exist.
[[start:1352390][end:1370838]] To check this, we first simulated a Bayern agent and when we varied the PRI of the Bayesian agent, the inference was attenuated as I expected.
[[start:1371014][end:1382714]] And we found that when we buried the excitatory level of in vitro neural network by using the pharmacological manipulation.

23:02 [[start:1382842][end:1403220]] We also found that the attenuation of inference which is consistent with our theoretical prediction that firing threshold encode prior belief or the hidden state.
[[start:1404710][end:1430700]] And next we consider whether the scientific plasticity followed the free energy principle by asking whether free energy principle can predict the qualitative self organization of a subsequent neural data.

23:52 [[start:1432130][end:1443022]] So here we model neural network like this, there are two ensemble neurons that encode source one and source two.
[[start:1443156][end:1469160]] And we first compute the effective synaptic weight of those networks using a conventional connection strength estimation approach and plot those synaptic weights on the landscape of theoretically computed free energy.

24:31 [[start:1471690][end:1493040]] So this is a trajectory of empirically estimated synaptic weights effective sign optic connectivity and as predicted, those changes reduce the free energy.

24:54 [[start:1494710][end:1506638]] And here we computed this theoretically predicted free energy landscape only using the past ten sessions data.
[[start:1506824][end:1518550]] So that this indicates that indicates some prediction of the self organization.
[[start:1519310][end:1530806]] And for more explicit prediction, we then simulated neuroactivity and plasticity using green as a principle.
[[start:1530998][end:1544138]] Here the brighter color indicates the prediction of data without reference to activity data.

25:44 [[start:1544324][end:1550850]] So those lines exactly follow this free energy gradient.
[[start:1551750][end:1567990]] And we found that this predicted trajectory is tightly correlated with this empirically estimated effective synaptic weights.

26:08 [[start:1568490][end:1572300]] And LR rate is like this.
[[start:1572670][end:1590350]] So it indicates that frequency principle can quantitatively predict the circumstance in this setup, so it indicates some predictive validity of the free energy principle under this setup.
[[start:1590690][end:1600542]] And then we also consider the modeling of the neuromodulation using active inference.

26:40 [[start:1600606][end:1612534]] It is well known that synaptic process is modified by various factors like Dopamine, northern adrenaline, acetylcholine, serotonin, so on.
[[start:1612732][end:1644950]] And one interesting property of those moderation is that even though Dopamine was added after associative plasticity was established, it can change the result of plasticity in a post hoc or restorespective manner, so it implies some association to the reward and past decisions.

27:25 [[start:1645050][end:1649198]] So we model this process using canonical neural network.
[[start:1649374][end:1671414]] So here we model the post hoc modulation of HEBM plasticity using this type of plasticity equation and we also consider the recurrent neural network structure and output layer for this network.
[[start:1671542][end:1681778]] And we consider that modulation occur at this connectivity layer.

28:01 [[start:1681974][end:1713560]] And then we found cost function that can derive those differential equations and then found corresponding variational free energy and genetic model which means that this sort of neural network activity including moderation of sinus plasticity exactly follow the free energy principle under some type of homodp generative model.

28:34 [[start:1714090][end:1733610]] And by using this, we show that this biologically plausible neural network model with moderation of heavy and plasticity can solve some sort of delayed reward task like maze task.
[[start:1734530][end:1743770]] And then finally we would like to discuss a possible extension to this framework to the modeling social intelligence.
[[start:1743930][end:1760242]] So, to infer our con specifics, we need to select an appropriate generality model for our partners, depending on our partners.
[[start:1760306][end:1782970]] So this can be done by Beijing model selection scheme and we previously proposed a model that can predict the multiple biosomes using one big genetic model that comprises multiple genetic models.

29:43 [[start:1783130][end:1794378]] And this movie shows prediction of prediction of songs.
[[start:1794554][end:1808338]] So like this, this model nicely identified which genetic model is the best to explain a given sensory input.
[[start:1808434][end:1824730]] And this process indicates and the model can correctly infer the appropriate model and then imitate the song by its own action.
[[start:1825550][end:1844326]] So, although in the previous work we didn't discuss a detailed neural neural substrate for this mixture generative model, we now be able to consider the corresponding circuit architecture.

30:44 [[start:1844458][end:1857650]] For example, if we consider the moderation of neural module by neuromodulator like Dopamine, it act as an attentional filter.

30:57 [[start:1857810][end:1870118]] And this attentional filter can be explained by three factor Hebian running rule introduced in the previous slide.
[[start:1870214][end:1882450]] So again, this modulation works as the post hoc moderation plasticity.
[[start:1882550][end:1897358]] And this modulation can optimize each model to represent one generative model, one generate one song in a mutually independent manner.
[[start:1897454][end:1906990]] So, through this process, it is possible to learn multiple generative model in a vertically plausible manner.

31:47 [[start:1907150][end:1919894]] So, in summary, we found that the dynamics of kinetic neural network that minimize a cost function can be read as minimization of variational free energy.

32:00 [[start:1920012][end:1927590]] It indicates free energy principle is an apt explanation for this type of neural network.
[[start:1927750][end:1950740]] And we also validate this prediction using some in vitro setup by showing that free energy principle can quantitatively predict the self organization of subsequent plasticity only using the initial data.
[[start:1951590][end:1968470]] And as the modeling, we can extend those canonical network modeling to the action generation as a planning via the delayed moderation of heavy emperor's DST.

32:49 [[start:1969130][end:1987610]] And finally, we discuss possibility to extend this canonical model to modeling the social or shared intelligence ah to interact with multiple partners.
[[start:1987770][end:1990510]] So, that's all of my talk.

33:10 [[start:1990580][end:1992510]] Thank you for listening.
[[start:1992930][end:1994474]] This is Acknowledgment.
[[start:1994602][end:2002814]] Our collaborator and fundings and our unit are now recruiting postdoc researchers.
[[start:2002862][end:2005220]] So if you're interested, please check.

33:28 _Daniel:_
[[start:2008120][end:2008916]] Awesome.
[[start:2009098][end:2011540]] Thank you for the presentation, Takuya.
[[start:2013160][end:2018004]] I'll just ask a few quick questions from the live chat and a few other things that come up.
[[start:2018042][end:2025400]] So Dave says Takuya used the phrase after plasticity was established.
[[start:2026220][end:2030948]] Was his group able to modify e g increase plasticity?

33:51 [[start:2031044][end:2035100]] Or is he saying merely that it was shown that there is plasticity?

33:59 _Takuya:_
[[start:2039600][end:2066656]] Yeah, I'm not sure if I understand correctly your question, but those groups show that Dopamine adding Dopamine after 2 seconds after the association occurred can change the magnitude of plasticity.
[[start:2066848][end:2082120]] So without how to say if Dopamine addition was before this association, then plasticity level is low.
[[start:2082270][end:2100800]] But after Dopamine addition after association can change this level can increase the plasticity like this or like this which indicates the post hook moderation.

35:03 [[start:2103140][end:2103648]] Cool.

35:03 _Daniel:_
[[start:2103734][end:2105650]] I think that answers it.
[[start:2107460][end:2111140]] Well, what are you excited for?
[[start:2111210][end:2122010]] Or what are your hopes or feelings on where the active inference ecosystem is at and where we're headed in the coming months and years?

35:26 _Takuya:_
[[start:2126790][end:2132770]] Sorry again chris, just what are you excited about?

35:32 _Daniel:_
[[start:2132840][end:2135314]] Other than your own research directions?
[[start:2135362][end:2138870]] What are you excited about in the active inference ecosystem?

35:40 _Takuya:_
[[start:2140410][end:2140918]] Yeah.
[[start:2141004][end:2159802]] So, of course, one direction is the modeling of social interaction, which is much rich architecture than the interaction between the static environment.

35:59 [[start:2159946][end:2167322]] So if both agents run with each other, then many interesting phenomena can be observed.
[[start:2167386][end:2181970]] So we are excited with modeling those phenomena using biologically plausible neural network model through this equivalence.

36:24 _Daniel:_
[[start:2184490][end:2185240]] Awesome.
[[start:2185930][end:2187910]] Any last comments?

36:33 [[start:2193130][end:2194886]] Any other comments that you want to make,
[[start:2194908][end:2195910]] Takuya?

36:43 [[start:2203600][end:2204350]] Awesome.
[[start:2205600][end:2207580]] Thanks again for the presentation.
[[start:2207920][end:2216736]] And people should check out Live Stream 51, where you and I talked a few other times and went into some of the details on that work.
[[start:2216918][end:2217744]] There's a lot there.
[[start:2217782][end:2218880]] It's really exciting.

37:01 _Takuya:_
[[start:2221620][end:2222610]] Thank you.

37:03 _Daniel:_
[[start:2223460][end:2225136]] All right, thank you.
[[start:2225318][end:2226690]] See you next time.

37:07 _Takuya:_
[[start:2227560][end:2228852]] See you next time.

37:08 _Daniel:_
[[start:2228986][end:2229780]] Bye.
