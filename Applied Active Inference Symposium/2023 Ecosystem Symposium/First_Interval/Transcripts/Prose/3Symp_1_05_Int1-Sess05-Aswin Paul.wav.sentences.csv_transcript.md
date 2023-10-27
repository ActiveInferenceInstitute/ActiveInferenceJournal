
00:01 _Daniel:_
[[start:1970][end:7006]] And now welcome aswin how are you doing?

00:07 _Aswin:_
[[start:7188][end:7914]] Hi, Daniel.
[[start:7962][end:8720]] I'm good.

00:09 _Daniel:_
[[start:9810][end:12766]] Hanging out, looking forward.

00:12 _Aswin:_
[[start:12788][end:13946]] Can you hear me properly?

00:14 _Daniel:_
[[start:14058][end:15502]] Yeah, sounds good.
[[start:15556][end:22090]] And yes, looking forward to your workshop on sophisticated inference in pymdp.
[[start:22250][end:34200]] So it can be up to 90 minutes or it's totally okay if it's less and we can take a short break, but please take it away and just let me know however I can help.

00:34 _Aswin:_
[[start:34570][end:35366]] Great.

00:35 [[start:35548][end:36760]] Thank you so much.
[[start:37710][end:39980]] Maybe I'll share my screen and start.
[[start:40510][end:52734]] So, regarding the structure of what we are doing here, I'm assuming that people who see this later might want to try it hands on along with the tutorial or something.
[[start:52772][end:54800]] So that's the structure I kept in mind.
[[start:55170][end:57178]] And so I'll go slow.

00:57 [[start:57354][end:58894]] Please bear with me.
[[start:59092][end:63854]] So welcome all of you to this session on sophisticated inference in pymdp.
[[start:63902][end:76286]] So here we are going to attempt to model some sophisticated inference simulations, especially the one in the original paper using the pymdp module and how it is not part of pymdp right now.
[[start:76328][end:81010]] But we are on the process of adding sophisticated inference to the pymtp module.
[[start:81170][end:88662]] And I'm going to mainly talk about the code that I have developed to kind of add that functionality.

01:28 [[start:88726][end:88954]] Right.
[[start:88992][end:90854]] So I'm Ashwin Paul.
[[start:90902][end:95302]] I am finally a PhD candidate at Monash University.

01:35 [[start:95446][end:108218]] And mostly I work with active inference models and try to understand how to use them as an explainable model to basically understand emergence of intelligent behavior.
[[start:108314][end:113374]] Right, so let's dive into the material right away.

01:53 [[start:113572][end:120626]] So to give an intro of free energy principle, I'm sure all of you right now have an understanding of what it is.
[[start:120728][end:128534]] But the central idea is that an agent is always trying to minimize the entropy of its observations, right?
[[start:128572][end:138410]] So if an observation is having really low probability in your mind and that happens, then you are probably surprised and vice versa, right?
[[start:138480][end:150598]] And the entropy here is defined as the information theoretic entropy, where if you have a low probability, then automatically this is a high surprise or a high entropic observation.
[[start:150774][end:158986]] And as we all know, active inference also gives us a methodology to define what we call an agent environment loop.

02:39 [[start:159098][end:170210]] And this lets us define what is the agent that we are looking at and what is the behavior of the agent given the environment around it and so on.
[[start:170280][end:170562]] Right?
[[start:170616][end:173614]] So you're also familiar with the idea of Marco Blanket.
[[start:173662][end:191414]] And this is important because we always have to remember, I mean, have to remember the difference between the generative process and the generative model, which is quite a famous point of confusion in active inference literature and for the people who try to understand it in the beginning.
[[start:191542][end:192220]] Right?

03:12 [[start:192590][end:196582]] So the central question is that how does an agent minimize entropy?
[[start:196646][end:201994]] Because how does an agent know which observation is low or high probabilistic?
[[start:202042][end:202494]] Right?
[[start:202612][end:204798]] So that is by maintaining a generative model.
[[start:204884][end:212458]] And the generative model will tell you which is a high probabilistic observation and which is a low probabilistic observation.

03:32 [[start:212554][end:221982]] So the idea is that all the agent has access to is an observation that is coming from a generative process which the agent cannot directly observe.

03:42 [[start:222126][end:233094]] And an intelligent agent will try to build up a generative model in its mind, which is a model of the hidden states and the observation it has access to.
[[start:233212][end:238246]] And it can hope to kind of compute probabilities using this generative model, right?
[[start:238268][end:246858]] But there is a problem that in general it is an intractable problem to kind of marginalize the probability of observations from the generative model.
[[start:246944][end:252774]] And that is why we have to define an upper bound on the surprise that the agent is trying to minimize.

04:12 [[start:252822][end:255054]] And there comes the idea of free energy, right?
[[start:255092][end:259870]] So this upper bound the agent is supposedly minimizing is the free energy.
[[start:259940][end:262154]] And that's why it is the free energy principle.
[[start:262282][end:272386]] And here we have a new term called capital QS, which can be interpreted as the belief that the agent is maintaining about the hidden state in its generative model.
[[start:272568][end:274930]] And this quantity is the free energy.

04:35 [[start:275000][end:286390]] And traditionally we see this variational free energy being interpreted as in mostly the machine learning way where it is a balance between complexity and accuracy of the model.

04:46 [[start:286540][end:296074]] So when minimizing the free energy, the agent is trying to come up with a single model but at the same time an accurate model because here it's a minus sign with accuracy, right?
[[start:296112][end:313962]] It can also be interpreted in the physics way where the agent is always trying to minimize the energy of the model but at the same time maximizing the entropy of the model which goes in conjunction with the maximum entropy principle and so on from the classic literature.
[[start:314106][end:332486]] So, given that this idea of a generative model is so important in a software point of view, that's the first thing that you might want to do, right, to define a generative model for the agent which is informed or not informed depending upon the experiment that you're trying to model.
[[start:332588][end:338342]] So in classical active inference, usually decision making is defined in terms of policies.

05:38 [[start:338406][end:347654]] So, for example, if you are an agent in this environment so in the Mario game, Mario is the agent and everything else is the environment.

05:47 [[start:347782][end:355994]] And Mario has three available actions run, jump or stay in this environment.
[[start:356042][end:361454]] And the classic definition of policy is that it is a sequence of actions in time.
[[start:361572][end:368194]] So if you have a time horizon of capital T, then a policy is nothing but a series of actions you might take.
[[start:368232][end:371490]] So run, run, jump and so on in time.

06:11 [[start:371560][end:375278]] So this is the SuperScript is the action.
[[start:375454][end:377814]] So here it is jump, run and so on.
[[start:377852][end:379734]] And the subscript is the time.
[[start:379932][end:388598]] And then what you can have is a policy space, which is a collection of many such policies, small pi.
[[start:388694][end:395142]] And what you essentially do to take decisions in active inference is compute, not optimize.

06:35 [[start:395206][end:400830]] Compute the expected free energy of every policy in your policy space.
[[start:400980][end:407150]] And basically, that can be interpreted as a balance between risk and ambiguity.

06:50 [[start:410770][end:417570]] So when you compute this expected free energy, what you're trying to do is minimizing the risk.
[[start:417990][end:424942]] That is, how different is your belief about the observation from your prior preferences?
[[start:425086][end:426066]] Capital C.
[[start:426168][end:437302]] So this is also part of the generative model when you're trying to model control and at the same time you are trying to minimize the ambiguity when you are choosing a policy that has the minimum expected free energy, right?
[[start:437356][end:455920]] But this formulation has a problem that a policy space quickly becomes intractable, that there can be an enormous number of small pies or policies in your policy space and sitting and computing the expected free energy for all such policies even for a small time horizon, is not possible.

07:36 [[start:456370][end:472366]] But this is the classical structure that has been implemented in Pymdp nonetheless, where we have different modules in Pymdp that is meant to be implementing different aspects of behavior.

07:52 [[start:472478][end:485394]] So for example, for inference or perception we have belief propagation, fixed point iteration, marginal message passing and all that implemented in the inference module.
[[start:485522][end:501542]] In the control module we have different methods to evaluate expected free energy for policies, one depending upon the expected utility, the other one depending upon the classic method that I just explained.
[[start:501686][end:503790]] Then we have module for learning.
[[start:503860][end:510734]] So we learn the parameters in the form DP like capital A, capital B, so likelihood transition dynamics and so on.

08:30 [[start:510772][end:517534]] And then we have algorithms for implementing all this in the algorithms module.
[[start:517662][end:530406]] And then the most powerful thing in Pymdp right now is the agent class where it is easy for you to kind of define the agent environment loop and we are trying to build up.
[[start:530508][end:539500]] So today I'm going to talk about an agent class that implements sophisticated inference rather than the classical active inference that we just saw.

09:00 [[start:540110][end:548374]] So, as I mentioned, how many valid policies can be defined, say for a time horizon of 15 in classical active inference?
[[start:548422][end:549018]] Right?

09:09 [[start:549184][end:562362]] So the first policy of course, is a series of first action that is jumped, then you can have the last action changed and you already can see that there can be n number of combinations.
[[start:562426][end:567726]] And for this simple case, the policy space is as big as ten to the power 13.
[[start:567838][end:578470]] And in a stochastic problem setting there is no way to kind of come up with a small subset of this policy space so that you can tackle this problem of computational complexity.
[[start:578970][end:584600]] And yeah, as I mentioned, in a stochastic problem setting it is an intractable size policy space.
[[start:585050][end:592794]] There comes the idea of sophisticated inference where we are thinking about taking decisions in a different way, right?

09:52 [[start:592832][end:603214]] So rather than thinking about sequence of actions in time, we can directly think of what to do when we see something depending upon our beliefs about the current state and beliefs about the future, right?

10:03 [[start:603252][end:606334]] So if I see myself in a current situation, what should I do?
[[start:606452][end:611802]] And that's more like a straightforward thinking of how to take actions.
[[start:611946][end:614322]] And here the expected free energy.
[[start:614456][end:626434]] The structure of the expected free energy is the same but we are not evaluating expected free energy of policies, but expected free energy of observation action combinations.

10:26 [[start:626562][end:630070]] So if I see something and if I do this, what's the expected free energy?
[[start:630140][end:632338]] And that's what I'm trying to minimize.
[[start:632514][end:638374]] That's what I'm trying to optimize in this setting, right?
[[start:638412][end:645622]] So here again, we have the risk term where we are trying to minimize the deviation between the belief and the prior preferences.
[[start:645766][end:654542]] We also have the ambiguity term and this together makes up the expected free energy of this time point at time T.

10:54 [[start:654676][end:659662]] But we also have an expectation about what's the expected free energy in the next time step.
[[start:659716][end:667442]] And to evaluate the expected free energy of next time step, you will have to again compute this equation with OT plus two.

11:07 [[start:667576][end:672514]] And for that you will have to again compute this equation with OT plus three and so on.
[[start:672552][end:687270]] And this automatically becomes a tree search because of the recursive way this equation is defined and it comes with its own problems, but there are clever ways to get around them and we are going to discuss that in the code today.
[[start:687420][end:698410]] So, given the structure of sophisticated inference here, as I mentioned, the research replace the policy space that we saw for the traditional active inference we are used to.

11:38 [[start:698560][end:709786]] So in this workshop, what I am focusing on is how to kind of define a generative model and given an environment.
[[start:709898][end:725670]] So for example, this is the grid that is simulated in the original paper and we are going to talk about how to build up a generative model for this grid that can be used in the sophisticated inference in the PMDP module.
[[start:727370][end:745622]] So basically, what I'm trying to talk about is that the environment will have a step function that takes an action from the agent in Pymdp, and the agent will get an observation out of that action and we'll talk about this particular function, agent step and agent steps.

12:25 [[start:745766][end:750414]] Step will take up an observation and try to come up with an action for the next time.
[[start:750452][end:750894]] Step right.

12:30 [[start:750932][end:762298]] And this creates a loop and cleverly designing this loop will let you see emergence of purposeful behavior in the sophisticated inference setting.
[[start:762394][end:770354]] So for example, in this particular grid with sufficient planning horizon, you will be able to see that the agent is capable of navigating in this grid and so on.
[[start:770392][end:775860]] So this is the example that I'm going to focus on in this talk today.

12:59 [[start:779370][end:788510]] Excuse me, I want to right away jump in to the code.
[[start:789600][end:797264]] So we have the Pymdp home, which I'm hoping you are familiar with.
[[start:797382][end:809284]] So we have this GitHub repository where we have the pymdp module and inside pymdp module we have several parts for it.

13:29 [[start:809322][end:815980]] So here we have the agent in the original Pymdp module that implements the so called classical active inference.
[[start:816080][end:822888]] We have several environments and we have help of functions like learning inference, maths and so on.

13:42 [[start:822974][end:825764]] So this is the module of Pimedp.
[[start:825892][end:838444]] But in the parent folder we also have examples where there is tutorials about how to use the agent class, how to kind of deal with the environments and so on.
[[start:838482][end:848156]] So if you look at the pull requests so we are right now trying to merge sophisticated inference into the original Pymdp module.
[[start:848268][end:851132]] And today I'm going to talk about the code in this pull request.
[[start:851196][end:864800]] So if you want to try this hands on, you might want to go to this page where this pull request is there and it has the same structure of Pymdp.

14:24 [[start:864880][end:867748]] It's basically designed using Pymdp.
[[start:867844][end:879752]] And here what we have additionally is an agent si which is a sophisticated inference agent which does everything and also planning and decision making in the sophisticated inference way.

14:39 [[start:879886][end:885692]] And in the parent folder there is also an example folder for sophisticated inference demo.
[[start:885826][end:891540]] And what I am going to do today is to walk you through this tutorial of sophisticated inference.
[[start:891640][end:909136]] And on the way, I'm going to discuss and at points where I reference the helper codes, I'm going to go to that code and try to explain what's actually happening and how we complete that agent environment loop where we can see that purposeful behavior.

15:09 [[start:909248][end:909910]] Right?
[[start:911800][end:912164]] Yeah.
[[start:912202][end:914116]] So that's the Pymdp home.
[[start:914218][end:917040]] Then I also talked about the pull request.
[[start:917120][end:920500]] So let's right away go into the jupyter notebook.

15:20 [[start:920580][end:928440]] So this is my local copy of this repository, so it's easier for me to run it and show it in my personal computer.
[[start:928590][end:938508]] So this is the parent folder with Pymdp and examples and inside examples I have a demo folder for sophisticated inference and this is the notebook I'm talking about.
[[start:938594][end:938844]] Right?
[[start:938882][end:961236]] So here in this example, what we are trying to do is deal with this particular grid world task from the original sophisticated inference paper and make this agent or enable this agent to navigate to this red dot, which is supposedly the goal state in this particular task given a prior preference like this, right?

16:01 [[start:961258][end:975112]] So this prior preference is quite informative in the sense that we right away can see that this is the most preferred state, the white color and the surrounding states are kind of less preferred, but more preferred than the faraway ones.

16:15 [[start:975166][end:975384]] Right?
[[start:975422][end:978796]] So this is the grid world task that we are trying to use.
[[start:978978][end:989896]] So the first cell is importing all the necessary libraries and some useful libraries like NumPy and Matplotlib.
[[start:990088][end:992412]] And the most important one is Pymdp.
[[start:992476][end:1002112]] So I'm actually now calling the local copy of my Pymdp with the sophisticated inference implementation, not the original one, which is not merged yet.

16:42 [[start:1002246][end:1006292]] And the first thing I want to talk about is the environment itself, right?
[[start:1006346][end:1012388]] So the environment step part where if I get some action, how does the environment work?
[[start:1012554][end:1024104]] And for that, inside this folder I have a file which is Grid environment Si PY and this is basically an environment class.

17:04 [[start:1024222][end:1028096]] So don't worry about how this environment is actually implemented.
[[start:1028228][end:1037660]] The only thing to worry about is this function that we are going to use which is environment step.

17:17 [[start:1037810][end:1050000]] So this function will take an action into it and depending upon the current state of the environment, it will calculate what is the most probable next state given this action from the agent.
[[start:1050150][end:1051392]] So that's the idea.
[[start:1051526][end:1063652]] And then it will also calculate a reward of some negligible negative value if it is not the Gold State, and if it is the Gold State, it will give a reward of ten.
[[start:1063706][end:1065124]] And that's how the environment is.
[[start:1065162][end:1068900]] Designed and it will update the current state to the new state.

17:48 [[start:1068970][end:1078148]] And basically what it will return is a new state, depending upon your action, the reward for that action and whether it is an end of the episode and so on.
[[start:1078174][end:1085996]] So this implementation is the standard OpenAI environment implementation and this is the environment step function, right?

18:06 [[start:1086018][end:1097724]] So in this grid, for example, if I am right now in this state and if I take an action up, so I have four available actions north, South, east and west.
[[start:1097772][end:1105252]] So if I go on north, then the environment step will make sure that I am in the state that is above the state.
[[start:1105306][end:1107972]] And if I go east or west, then I'll stay here.

18:28 [[start:1108026][end:1108544]] Or south.
[[start:1108592][end:1109332]] I'll stay here.
[[start:1109386][end:1111270]] So that's the idea.
[[start:1112440][end:1126916]] And there is an episode length limit that is eight here, that means that I am restricting the length of every episode to be eight, which is the ideal length of reaching this goal state just to avoid confusion.
[[start:1127028][end:1131208]] So in this environment, after eight actions, the environment will terminate.

18:51 [[start:1131384][end:1139500]] And if you have to kind of reach this goal state in the optimal time point so that's the idea how the environment is implemented.
[[start:1140160][end:1143120]] Okay, I hope that is clear.
[[start:1143190][end:1153756]] And there are many helpful functions in this environment, like rendering the environment, rendering a prior preference matrix in this environment.

19:13 [[start:1153788][end:1163110]] So if you design a prior preference, this environment can show that in a pictorial way how your prior preference is that you will see in the notebook below.
[[start:1163960][end:1169610]] So now it's time that we define a generative model for the sophisticated inference agent, right?

19:31 [[start:1171180][end:1183164]] Before that, let's define the structure of the generative model that we want the agent to have in its mind, which is tailor made for this particular environment, right?
[[start:1183282][end:1191648]] So here in this particular grid world task, we have 25 valid states starting from this state.
[[start:1191734][end:1196352]] All this black states in this path are valid states.
[[start:1196406][end:1198384]] So there are 25 valid states.
[[start:1198582][end:1203756]] Then there are four available actions for the agent, north, Southeast and west.

20:03 [[start:1203868][end:1205940]] So this is part of our generative model.
[[start:1206090][end:1211328]] This is also in alignment with the reality of the grid.
[[start:1211504][end:1214772]] But this is about what the agent has in its mind, right?

20:14 [[start:1214906][end:1219210]] And then the observation is just the state space.
[[start:1220780][end:1224490]] The problem is fully observable, so there is no ambiguity there.

20:24 [[start:1224860][end:1228330]] Then we define basically the number of states.

20:34 [[start:1234170][end:1245466]] Then we define basically the number of states, which is a list of your state space, number of factors, which is now one because you only have one hidden state factor here.
[[start:1245568][end:1248620]] Then number of controls, which is going to be four.
[[start:1249150][end:1253562]] That's four available actions and your observation space like that.
[[start:1253616][end:1256062]] So this is the structure of your generative model.
[[start:1256196][end:1262378]] And let's look at the structure of the parameters now inside a POMDP.

21:02 [[start:1262474][end:1270846]] So the first one is the likelihood function which is often denoted by capital A.
[[start:1270948][end:1276594]] And here it is a function of how many observational modalities I have and how many state modalities I have.

21:16 [[start:1276632][end:1277122]] Right?
[[start:1277256][end:1284840]] If I run this cell, yeah, I have to run the parent cell to make sure everything works.
[[start:1285450][end:1290246]] So I have rendered the environment the structure of the generative model.

21:30 [[start:1290348][end:1295802]] And here I have the capital A matrix which has a structure 25 25.
[[start:1295856][end:1298870]] That means that I have 25 states and 25 observations.
[[start:1299030][end:1305790]] And here, because it's fully observable, I am initializing it as an identity matrix of size 25.
[[start:1305860][end:1313978]] So that's my likelihood matrix that I'm initializing for this particular grid world task.
[[start:1314154][end:1317630]] Then the second element is the transition matrix.

21:58 [[start:1318130][end:1329650]] So please note that I'm using all the existing Pymdp functionalities to define a random A matrix and then using an identity matrix on top of that.
[[start:1329800][end:1332914]] So, yeah, I'm not doing anything new.
[[start:1332952][end:1336690]] Here it is the existing Pymdp functionality.

22:16 [[start:1336850][end:1342786]] Then what I can do now is define the B matrix, which is also called transition matrix.
[[start:1342898][end:1351334]] So the transition matrix encodes transitions like where I'm going to end up in the future if I start from a particular state and take an action.

22:31 [[start:1351462][end:1358822]] So that's the idea where it depends upon the number of states, which is the hidden state modality and number of controls.
[[start:1358886][end:1365806]] So it has the structure of state action state where if I take an action from a particular state where I'm going to end up.
[[start:1365828][end:1368078]] So that is also a future state, right.
[[start:1368244][end:1374082]] So I'm going to initialize it as the true environment state.
[[start:1374136][end:1376482]] So now this is part of the environment that I've built.

22:56 [[start:1376536][end:1378530]] It will give out the B matrix.
[[start:1379190][end:1382950]] It might be worth it to look at the structure of this B matrix.

23:05 [[start:1385370][end:1388390]] So here we have 25, 25 four.
[[start:1388460][end:1400602]] So that means that if I take an action from a particular state where I'm going to enter and we have the true transition dynamics for this particular grid by design.

23:20 [[start:1400736][end:1408062]] So there is a function called get true B and that will give us the true b of the system which the agent can use.
[[start:1408196][end:1408542]] Okay?
[[start:1408596][end:1417150]] So ideally we would want the agent to learn this, but for the purpose of this demo we are assuming that the agent already knows the structure.

23:37 [[start:1417890][end:1428978]] And then comes the prior preference, which is interesting here in the sense that it is defined as how closer you are to the gold state.
[[start:1429064][end:1434198]] So if you are at the gold state, then clearly that is the most sought out state.
[[start:1434284][end:1436006]] You prefer that the most.
[[start:1436188][end:1439606]] And how do you prefer the neighboring states, right?
[[start:1439628][end:1447626]] So that is dependent upon the square root of the distance or basically the distance from that particular gold state.

24:07 [[start:1447808][end:1456258]] So you define a grid which is eight cross eight, the same size as this particular grid world task.
[[start:1456454][end:1465230]] And then we have a method to kind of add values which is the preference you have for every state.

24:25 [[start:1465380][end:1477458]] And if you render the particular C matrix you can see the structure which is the same where this gold state is more preferred and the surrounding states less preferred and so on.
[[start:1477624][end:1482440]] So now we have the C matrix also defined in the classic PMDP way.
[[start:1483290][end:1492722]] And then I initialize that C matrix as the C matrix we evaluated in the previous cell which is small C, this particular C matrix.

24:52 [[start:1492786][end:1493446]] Okay?
[[start:1493628][end:1499930]] And then lastly, for the generative model we have capital D which is your prior overhead and states.
[[start:1500000][end:1502918]] And for that I'm using a uniform object array.
[[start:1503014][end:1506702]] So that means that I don't have a prior of where I am starting.
[[start:1506836][end:1510350]] So let me run the pending cells.

25:12 [[start:1512530][end:1516622]] So here the D matrix is a uniform distribution over hidden states.
[[start:1516676][end:1519346]] I don't know where I'm going to start the simulations and so on.
[[start:1519368][end:1522898]] So this is the basic structure of the generative model.
[[start:1523064][end:1530574]] And then we have the agent class which I want to discuss separately, like the environment, right?

25:30 [[start:1530632][end:1536550]] So given these environment parameters, how would you expect the agent class to work?

25:36 [[start:1536700][end:1538662]] So where is the agent class?
[[start:1538796][end:1540790]] Inside this folder structure?
[[start:1541850][end:1555274]] Inside the Pymdp module folder we have an agent Si PY which is basically a class again and similar to the environment class here.
[[start:1555312][end:1568938]] Also we have a step function where this will take an observation to the function and also a flag whether or not to learn the environment, which is optional.
[[start:1569114][end:1572898]] So if you disable it, it won't learn the generative model.

26:12 [[start:1572984][end:1576850]] If you enable it, it will update the parameters of the generative model.
[[start:1577000][end:1586294]] And what basically it does is it will return an action which is to be taken at this point of time and the environment can basically use that action, right?
[[start:1586332][end:1590520]] So in this file we have the agent class which I will explain in detail.

26:31 [[start:1591850][end:1605420]] So I am basically importing that agent class in this cell and then we are going to try and reproduce this behavioral result from the original sophisticated inference paper.
[[start:1605810][end:1606560]] Okay?

26:47 [[start:1607010][end:1608720]] And for that.
[[start:1609490][end:1617034]] So what we expect is that given this prior preference structure, there are local maximas in this prior preference structure.
[[start:1617082][end:1631362]] So if you start from this particular point, if you do not plan deep enough, what you will end up is in one of these local maximas where you don't see that there is a highly preferred observation, say four steps down the line.
[[start:1631496][end:1646434]] So if you are in this particular state, what you will see is this local maxima and you will go and sit there because the neighboring states are less preferred and this state which is more preferred is not accessible because of the wall or the wall structure.
[[start:1646562][end:1654458]] So you have to take a turn and pass through less preferred states and you need deep planning in order to enable the agent to do that.

27:34 [[start:1654544][end:1666954]] The agent should be able to kind of simulate four time steps ahead in time to see that there is this highly rewarding observation coming to kind of do that actions.
[[start:1667082][end:1671794]] So that's the point that we are trying to see in this particular demo.
[[start:1671912][end:1682982]] So for a low planning depth it will basically get stuck in one of the local maximas but with sufficient planning depth it will navigate to the gold state.
[[start:1683036][end:1685142]] So that's what we are trying to see, right?
[[start:1685276][end:1699094]] So we have different planning horizons and what we are basically doing is give the agent a generative model which we right now defined the A matrix, B matrix, C matrix B matrix.

28:19 [[start:1699222][end:1702026]] Then we have the planning horizon of capital N.
[[start:1702128][end:1705238]] So here I am, iterating over planning depth.
[[start:1705334][end:1708410]] So N will be one, three and four for the loop.
[[start:1708570][end:1713722]] Then we have action precision, which is often denoted by alpha in active inference literature.
[[start:1713786][end:1716894]] So that determines which action is to be taken.

28:37 [[start:1717012][end:1725394]] So a highly precise action precision means that it will stick to the action with the lowest expected free energy.
[[start:1725592][end:1731374]] But a lower action precision is kind of probabilistic where it will also consider other actions.
[[start:1731502][end:1738658]] Then we have a planning precision which is part of the planning function we'll discuss, which is often denoted in the literature as gamma.
[[start:1738754][end:1753734]] Then we also have a search threshold which is extremely important for sophisticated inference because as we saw, sophisticated inference is a tree search and tree search is bad in the sense that it can have a lot of computations.
[[start:1753862][end:1759310]] But you have to define a threshold to kind of ignore many possibilities to make it work.

29:19 [[start:1759380][end:1761920]] And that's the idea that we will also discuss.
[[start:1762610][end:1768510]] So just a preview before we go to the agent class.
[[start:1768660][end:1777486]] What we are trying to do is in a loop we are going to call the agent step and environment step in series.

29:37 [[start:1777598][end:1788418]] So the agent will see an observation, it will take an action, that action will go into the environment, the environment will give it back new observations and this loop continues.
[[start:1788514][end:1798442]] And we want to see over time how this loop evolves into a purposeful behavior and if the agent at all is capable for that.

29:58 [[start:1798496][end:1803498]] So before I reveal the results, let's discuss the agent class.
[[start:1803664][end:1812382]] So in order to give an action, when an observation is given, the agent should have the planning and so on, right?
[[start:1812516][end:1823966]] So here is the agent, the sophisticated inference agent, where we are actually using the existing Pymdp agent for some functionalities.
[[start:1824078][end:1833782]] So in Pymdp we already have really well written functions for perception and learning.
[[start:1833916][end:1842690]] So the only thing we want to kind of replace is how the agent is doing planning and how the agent is taking decisions over policies, right?

30:42 [[start:1842860][end:1849930]] So here we are using that parent agent class.
[[start:1850080][end:1860960]] So from Pymdp agent we are importing that agent class which is sitting next to the Si agent that we are discussing now.
[[start:1861810][end:1883526]] And basically we are taking in the generative model structure from the main program for this class to work which is C and D and all the precisions and threshold parameter I mentioned, then it is kind of normalizing the prior preference that we mentioned in the main program.
[[start:1883708][end:1899754]] So here if I look at how C is, the structure of C is defined in terms of numbers and the prior preference is often interpreted or it should be a probabilistic distribution for the computations to work, right?
[[start:1899792][end:1909902]] So we are going to normalize it as a probabilistic distribution rather than having numbers that don't add up to one.

31:50 [[start:1910036][end:1911454]] So that's what's happening here.
[[start:1911492][end:1913742]] We are using Softmax to do that.
[[start:1913876][end:1932378]] Then what we are doing is we are initializing the existing PMDP agent with these generative model parameters and what we are intending to do is write a planning function for a given planning horizon and a given threshold for trees.
[[start:1932574][end:1937080]] Okay, so there are three functions in this agent class.
[[start:1937690][end:1941190]] One is a helper function for planning which we will discuss now.

32:21 [[start:1941340][end:1947354]] Then there is a planning function itself which is going to do planning using tree search.
[[start:1947552][end:1962830]] And then because it is a recursive tree search, we are going to need an additional function that implements that recursive evaluation where we are going to call this function called forward search inside the function itself.
[[start:1962980][end:1966142]] So we are calling this function inside this function.
[[start:1966276][end:1973646]] So that is to calculate expected free energy for the next step and it will call it again for the next step till our planning horizon.

32:53 [[start:1973678][end:1990390]] So that's the idea of recursive looping and finally it will return the expected free energy for all actions given an observations and then we just implement the step function where it is written sequentially what to do given an observation.

33:12 [[start:1992330][end:2007050]] So going back to the demo here we have this first idea where you get an observation and it gives out an action.
[[start:2007130][end:2011934]] So let's go to the agent step function and imagine what happens.
[[start:2012132][end:2019934]] So if it is time t equal to zero or in the beginning of the experiment, what it is ideally.
[[start:2019982][end:2024526]] Supposed to do in the first place is infer that state using its observation.
[[start:2024638][end:2037638]] So what we are giving it is an observation and using the modules for inference, it's going to come up with a belief QS, which is a belief about states.

33:57 [[start:2037804][end:2054474]] Okay, so self dot QS is the belief inside the agent and once it has a belief about where it is right now, it can implement plan research which is do planning for this particular belief of hidden state right now.
[[start:2054592][end:2064590]] And once it has done planning, it can take decision using the sample action function in Pymdp and basically return that action.
[[start:2065410][end:2069362]] And for every other time steps, the sequence remains the same.
[[start:2069496][end:2075620]] But it is also learning about the structure if you enable learning in your agent class.
[[start:2076470][end:2078900]] So that's the step function.

34:39 [[start:2079590][end:2091986]] But in order to do planning, what it does is it kind of reorganizes the generative model structure for any number of hidden state modalities and any number of observation modalities.
[[start:2092178][end:2106560]] So to discuss how melting works, I would like to talk about the new A matrices and B matrices it evaluates for implementing that planning and let's understand that.

35:07 [[start:2107650][end:2113274]] So let's go back to the original hidden state factors.
[[start:2113402][end:2116266]] So here we only have one hidden state factor.
[[start:2116458][end:2118622]] So that's why it is B zero, right?

35:18 [[start:2118676][end:2124238]] And B one does not exist because we only have one hidden state factor.
[[start:2124334][end:2130020]] But imagine that if I have two hidden state factors with the same size maybe.
[[start:2130730][end:2137320]] So here it could be a location and maybe something else inside the agent's mind.
[[start:2137850][end:2142306]] And we should also have controls for these two hidden state factors.
[[start:2142418][end:2161390]] Just like so there should be control for every hidden state factor if you're familiar with active inference idea and then maybe the observation space is also directly observing these two hidden state factors.

36:01 [[start:2161810][end:2168862]] Okay, so this is a new Generative Model structure with multiple hidden states and multiple observation modalities.

36:09 [[start:2169006][end:2174114]] And right away you can see that the dimensionalities of your parameters change.
[[start:2174232][end:2182178]] You have 25 observations coming from 25 times 25 hidden states.
[[start:2182344][end:2186550]] And if you look at the structure of the first observation modality, it's the same.
[[start:2186700][end:2195594]] But what we want is a new matrix where it's going to be 25 with not two hidden states but just one hidden state.

36:35 [[start:2195632][end:2204060]] It's only a reorganization of the generative model, but computations essentially remains the same.
[[start:2204910][end:2215498]] So that's what this helper function is trying to do, which will make things easier for us when we have multiple hidden state modalities.
[[start:2215674][end:2228718]] So if you have multiple hidden state modalities, we are going to compute how many total states you have, which is the multiplication of number of hidden states in each modality.
[[start:2228814][end:2229074]] Okay?

37:09 [[start:2229112][end:2238120]] So if you have 25 hidden states in one modality and 25 hidden states in the other modality, you're going to have 625 total number of states.

37:18 [[start:2238570][end:2250622]] And if you have four actions each in each modalities, then you have total of 16 actions which is nothing but the combination of these four actions each in the modalities.
[[start:2250706][end:2255014]] So you're going to have four times 416 actions if you have two modalities.
[[start:2255142][end:2269810]] And it's basically going to build a generative model that has the same model parameters but just with a different dimension structure so that it's easier for us to calculate the expected.
[[start:2270150][end:2281586]] So now we have a new A and new B and a new belief which is nothing but tensor products of existing parameters and beliefs.
[[start:2281698][end:2286470]] It's nothing but a new big matrix and nothing else.

38:06 [[start:2286540][end:2287160]] Okay?
[[start:2288250][end:2291570]] It's not a change, it's just a transformation of structure.

38:11 [[start:2291730][end:2302346]] And given this A, B and Q, we are going to predict what's going to happen in the future and evaluate the expected free energies for them.
[[start:2302448][end:2306986]] So in order to do planning, so that's the second function.
[[start:2307088][end:2317910]] What we are going to do is first call the first function which will do the melting for us and set up the generative model in good dimensions, easy to compute.

38:38 [[start:2318010][end:2330110]] Then we have the expected free energy itself for all the actions and then we have the probability that depends upon this expected free energy for these actions.
[[start:2330190][end:2333122]] So why is it just the actions and not the observations?
[[start:2333266][end:2341606]] Because here we are going to evaluate expected free energy of actions for the given observations, right?
[[start:2341628][end:2351286]] So let me go back to the slides and discuss this pictorially to make things easier.
[[start:2351398][end:2354870]] So here we have the grid and we have the prior footprints.

39:14 [[start:2354950][end:2369854]] And what we are trying to implement is that if you observe some observation at time T, then you're going to consider the consequences of your actions given that observation, because you can predict what's going to happen.
[[start:2369892][end:2378226]] Because in your generative model you have the transition dynamics that will tell you, given this state, if I take this action, where I'm going to end up, right?
[[start:2378248][end:2389154]] So that's basically predicting what's going to happen in the future and you're right now considering the consequence of available actions in your arsenal.
[[start:2389282][end:2397130]] And then if you take an action, then you can predict what's going to happen in the next time step as a new observation, right?
[[start:2397280][end:2406406]] So you have a probability distribution that tells you that say this observation is the most likely and the other observations are not really likely.

40:06 [[start:2406598][end:2417022]] Then what you will do is you do this again, you consider the consequence of doing your actions from that particular observation and this goes on in your planning depth, right?

40:17 [[start:2417076][end:2420666]] So this can be thought of as maybe you want to go to the gym.
[[start:2420778][end:2424030]] Then you are going to consider all the consequences.
[[start:2424110][end:2433774]] What will happen if I wear my shoes, if I don't wear my shoes, if I go in my car, if I don't go in my car, then you realize that, okay, I have to wear my shoes.
[[start:2433902][end:2441842]] Then you consider the consequence that I'm now ready to go to the gym and me going to the gym will end up me being in the gym.

40:41 [[start:2441906][end:2443094]] So that's the idea.
[[start:2443212][end:2449322]] You consider the consequence of where you are right now and you can go as much as you want, right.
[[start:2449376][end:2450054]] You can predict.
[[start:2450102][end:2453114]] So in a game of chess, you might be in a particular state.
[[start:2453232][end:2466634]] You consider your consequences, you see the future, you consider consequences from that future, and you can go as deep as you want depending upon your computational abilities.

41:06 [[start:2466762][end:2467006]] Right.
[[start:2467028][end:2474690]] So that's what you're trying to implement in this agent class where we are considering consequences?

41:17 [[start:2477430][end:2478180]] Yeah.
[[start:2478790][end:2485030]] So for every modality we are going to consider the expected free energy for actions.
[[start:2485450][end:2490886]] And this will basically call the next function, which is forward search.
[[start:2490988][end:2497078]] So forward search is implementing the thing that I just mentioned, considering consequences.
[[start:2497254][end:2502150]] And in forward search, what you are basically doing is for every action.

41:42 [[start:2502310][end:2506750]] So in line 149, I have a loop that goes over every action.
[[start:2507090][end:2512282]] Then I'm going to consider the posterior or the consequences of all those actions.
[[start:2512426][end:2517390]] I use my transition probabilities to evaluate that consequences.
[[start:2517730][end:2524210]] Then I'm going to predict the observations, because my prior preferences are defined in terms of observations.
[[start:2524630][end:2533190]] I'm going to predict my observations and then evaluate the expected free energy, which is the sum of risk and ambiguity.

42:14 [[start:2534010][end:2534758]] Okay?
[[start:2534924][end:2536102]] I hope that makes sense.
[[start:2536156][end:2544910]] Like here, you have considered the consequence, which is consequence of future, which is post or posterior.

42:25 [[start:2545090][end:2550794]] And you're basically evaluating how good that posterior is depending upon your expected free energy.
[[start:2550912][end:2554454]] And that becomes the expected free energy for that particular action.

42:34 [[start:2554582][end:2556670]] And you do this for all the actions.
[[start:2557330][end:2558030]] Okay.
[[start:2558180][end:2560554]] And why this is powerful?
[[start:2560682][end:2563742]] It is because you can go as deep as you want.
[[start:2563876][end:2574574]] So here in the next step, you go to this loop where you will check if I am crossing my deep planning or the depth of planning.

42:54 [[start:2574702][end:2576578]] And then you are doing basically the same.
[[start:2576664][end:2582130]] Given that posterior, what is the consequence of the actions of that particular posterior.
[[start:2582210][end:2587078]] So here for considering that we are again calling the parent function.
[[start:2587244][end:2596330]] So the same function, forward search, to consider consequences of those combinations and it will basically come back and add up to your expected free energy.
[[start:2596480][end:2609482]] So what happens over this sequence is that you consider some or all future consequences and then all that values will trickle up your tree.

43:29 [[start:2609546][end:2619650]] And that sum of the expected free energy will tell you which action is good or which action is bad, which you can take to kind of see your preferred observations.
[[start:2620150][end:2623298]] So that's the idea of implementing tree search.
[[start:2623464][end:2632998]] And I will also talk about the importance of this threshold here, which makes this algorithm possible.
[[start:2633084][end:2636630]] So without this threshold, this algorithm will not work.
[[start:2636780][end:2640230]] I will explicitly talk about why that is the case.

44:00 [[start:2640380][end:2652646]] And then once you evaluate the expected free energy for all available actions, given the present state, you can basically compute what you call the action distribution.
[[start:2652838][end:2657550]] That is how probable is my action or how I should take my action.
[[start:2658850][end:2662298]] And we also have this action precision parameter alpha.
[[start:2662394][end:2671922]] So if alpha is very high then it basically is a highly skewed distribution where you will always choose the action that minimizes expected free energy.

44:32 [[start:2672056][end:2678542]] If alpha is really low then it's going to be a more sparse or spread out distribution.

44:38 [[start:2678686][end:2687938]] And then you can use this action distribution to sample actions in the agent environment loop.
[[start:2688034][end:2693106]] We just finished doing planning and computing that action distribution.
[[start:2693298][end:2698250]] Then using that action distribution, you can sample an action from your policy space.
[[start:2698400][end:2701580]] So let's look at the policy space in this generative model.
[[start:2702910][end:2717520]] So I'm switching back to the original generative model with one hidden state factor and let's do planning and maybe initialize this agent.

45:18 [[start:2718310][end:2723970]] I just want to initialize this agent to see the policy space, not run the loop.
[[start:2724390][end:2733288]] So I initialize this agent, say for planning depth of one.

45:33 [[start:2733454][end:2751808]] And if I look at agent policies, I can see that I have basically four available actions which is north, south, east and west.
[[start:2751904][end:2757552]] And if I have an action distribution, it will tell me how probable is to take that action.
[[start:2757616][end:2772780]] So if I look at agent UPI, okay, so this is not defined because I have not done planning, but I can do planning and then it will be defined.

46:18 [[start:2778580][end:2783776]] Yeah, so I implemented planning with research and then now I have an action distribution.
[[start:2783888][end:2790424]] So for this particular scenario, I am going to take my third action the most which is zero point 99.
[[start:2790462][end:2796184]] Basically that's the probability which is north, south and east in this particular case.

46:36 [[start:2796222][end:2806060]] I just wanted to kind of familiarize you with the matrices, but we are now going to see the agent environment loop in action.

46:48 [[start:2808880][end:2825424]] Now you can sample an action from the sample action function and then implement learning which is using the standard Pymdp way where I will update my transition dynamics and likelihood dynamics depending upon what I see and what's my belief and so on.
[[start:2825462][end:2829510]] So my emphasis is on the decision making part.

47:18 [[start:2838010][end:2844466]] So once you sample an action, then that action basically goes back to the environment.
[[start:2844578][end:2852490]] Okay, so now let us implement this for a planning depth of one and see how the agent behaves.
[[start:2852990][end:2864302]] So here if it is a planning depth of one, then that means that the agent is only considering the consequence of one time step ahead, just seeing the immediate future for doing planning, right?

47:44 [[start:2864436][end:2867120]] So I'm giving the planning depth of one.
[[start:2867730][end:2889150]] I'm resetting the environment where the agent is going to start from that initial start state, and in the loop, it's going to get that observation, take that action, give back an action, and we will look at the action probabilities.

48:09 [[start:2889490][end:2896490]] And also we will give that action back to the environment, get back the observation, and this loop continues till the episode is terminated.
[[start:2896570][end:2902110]] And I have set the episode length to be eight, just to see the outcome of eight action.
[[start:2902870][end:2912006]] So when we run this loop, these matrices are nothing but the action distributions of how likely each action is to be taken.
[[start:2912188][end:2915846]] And this is where the agent end up in the last time step.
[[start:2915948][end:2916502]] Okay?

48:36 [[start:2916636][end:2925100]] So let's maybe kind of also enable this environment render that will show us where the agent is at every time step.

48:45 [[start:2925870][end:2933098]] So initially the agent was at this location and we have an action distribution of this here.
[[start:2933184][end:2934934]] So north, south, east and west.
[[start:2934982][end:2937258]] So the agent knows that it should go north.
[[start:2937354][end:2937950]] Why?

48:58 [[start:2938100][end:2944414]] Because if I look at the prior preference, this state is more preferred than this state.
[[start:2944532][end:2944862]] Right?
[[start:2944916][end:2953714]] So the agent successfully calculated the expected free energy and inferred that, okay, I should go to this state and not stay in this state.
[[start:2953752][end:2962166]] And because it has the generative model of transitions available, it can infer that I should take an action north to go to this state.
[[start:2962348][end:2963686]] So that's good.

49:23 [[start:2963868][end:2965858]] And the agent goes to north.
[[start:2965954][end:2970530]] And at this particular state, the agent infers that it should go to north southeast.
[[start:2970610][end:2975274]] So it will take an action east and it will go here.
[[start:2975392][end:2983318]] And at this point of time, I want your attention where the action distribution is equally probable for north and east.
[[start:2983414][end:2984362]] Why is that?

49:44 [[start:2984496][end:2987166]] Because the agent is only looking at the immediate future.

49:47 [[start:2987268][end:2987582]] Right.
[[start:2987636][end:2996254]] So let's go back to the prior preference where the agent is right now here, or is it here?
[[start:2996292][end:2999714]] Yeah, it is right now here in this particular state.
[[start:2999832][end:3009538]] And if the agent is considering immediate consequences of just one action, then these two states are equally good for it to be in the next state.

50:09 [[start:3009624][end:3015014]] So there is no distinction between these two states if it is only looking at the immediate future.
[[start:3015132][end:3021026]] So that means that the expected free energygies will conclude that I should go to north or east.
[[start:3021058][end:3024538]] It doesn't matter if I'm looking at just one time step ahead.
[[start:3024704][end:3025418]] Okay?
[[start:3025584][end:3026860]] That's the idea.

50:27 [[start:3027790][end:3032380]] And out of probability it is going here.
[[start:3033150][end:3052154]] It took the action east and from this state, when it's doing inference, it's inferring that this state is better and basically it's ending up in this local maxima state, which is this particular state where the neighboring states are less preferred.

50:52 [[start:3052202][end:3058302]] And this is Wall and you can't go there because it is forbidden for the agent by structure.
[[start:3058366][end:3065338]] So it's basically going to sit there forever where it only sees that local maximum of prior preference.
[[start:3065534][end:3072526]] And let's look at what might happen if you have higher planning depth.

51:12 [[start:3072658][end:3083866]] So if I go to the planning depth of three, then that means that the agent is actually reaching the goal state at the last time step.
[[start:3084048][end:3093018]] But still in the third time point, it had two probabilistic actions, north and east.
[[start:3093114][end:3103678]] So here from this particular state, out of probability, it took the action north but it can all equally take the action east and end up in this local maxima.
[[start:3103694][end:3108626]] So let's run again and probably it will end up in this local maxima, okay?
[[start:3108808][end:3121590]] And only for the planning depth of four, which is sufficient enough, which is necessary for this particular grid, the agent is fully sure of what to do.

52:01 [[start:3121660][end:3133834]] So at every time point it is fully sure of what to do, that it has to go north, then east, north, north, north, east, east and south and reach this particular goal state.
[[start:3133952][end:3144906]] So only for time step or planning depth n equal to four, it can successfully navigate this grid with 100% certainty.
[[start:3145018][end:3146720]] So that's the idea.
[[start:3147250][end:3150786]] That's the implementation that I hope you got.
[[start:3150968][end:3153774]] So there is also this idea of action precision.

52:33 [[start:3153822][end:3155886]] So here it's a high action precision.
[[start:3155998][end:3158574]] That is why it is taking the actions.
[[start:3158622][end:3160690]] That is from the probability.
[[start:3160850][end:3169026]] If it is a low action precision like one, then the good actions are more probable.
[[start:3169218][end:3178442]] But that doesn't mean that it will be taken right here by luck, it is taking the right actions and reaching the state.

52:58 [[start:3178576][end:3180566]] But here probabilities are most passed.
[[start:3180598][end:3188794]] But you will also see like exploration behavior in more number of trials if you control this action precision.

53:08 [[start:3188842][end:3195230]] So I set it to a high value to make sure that the agent reaches the goal for this particular problem.
[[start:3195300][end:3199460]] But it's worth playing and it's important, right?
[[start:3200470][end:3203042]] Okay, yeah.

53:23 [[start:3203096][end:3210694]] So for different planning depths like one, three and four in this problem, this is the behavior that you expect.
[[start:3210892][end:3222846]] For lower planning depths, which is not sufficient, the agent ends up in local maximas or local minimas of expected free energy or local maximas of prior preference.
[[start:3222978][end:3227290]] But with sufficient planning depth, it's able to navigate and reach the goal.
[[start:3227950][end:3244922]] So that brings us to the last point in this tutorial where why is it important to have a threshold in evaluating sophisticated inference?
[[start:3245066][end:3252354]] So by threshold, what we mean is that we can ignore future possibilities in two levels, right?

54:12 [[start:3252392][end:3258370]] You can ignore not likely actions or not likely observations in this research.
[[start:3258520][end:3267542]] But if you consider the consequences of all actions and observations, that means that you'll have to consider four consequences in the first place.
[[start:3267676][end:3273730]] Then you will have to consider four times the action states in the next time step for the next time step.
[[start:3273820][end:3280294]] Then all of that multiplied with the number of actions and this tree search becomes intractable and you'll explode.
[[start:3280342][end:3285100]] And it's even worse than the classical active inference policy space problem.

54:45 [[start:3285410][end:3291630]] But by defining a threshold of even a small value, we'll ignore possibilities.
[[start:3291970][end:3294510]] So where is that implemented?
[[start:3295410][end:3305246]] In the forward search algorithm, we are considering actions with only action probabilities greater than the particular threshold.
[[start:3305438][end:3308030]] Here I am defining it as one by 16.
[[start:3308190][end:3314630]] Also in the parent paper, it's one by 16 the action probability.

55:16 [[start:3316170][end:3316920]] Okay?
[[start:3317290][end:3324686]] So if it is zero, then that means that it will consider all the consequences of future and that's intractable.
[[start:3324818][end:3346480]] So you can ignore actions which is not probable, and also ignore states which is less likely, or only consider states that has probability greater than this particular threshold value, and that significantly reduces the computational complexity, where you will only consider combinations that are probable in the future.
[[start:3347190][end:3352290]] Tree and that lets you go deeper in your planning horizon.
[[start:3352870][end:3354674]] That's an important point here.

55:54 [[start:3354792][end:3371618]] And if you compare the time that takes for deeper planning for a search threshold of zero, so a search threshold of zero means that you will consider all consequences.
[[start:3371794][end:3377498]] And the more deep you plan, the more time it takes.

56:17 [[start:3377584][end:3385450]] And if you see to consider only the first future or the immediate future, it takes 0.1 second.
[[start:3385790][end:3392474]] For considering three possibilities into the future, it takes 3 seconds, and for four it takes 300 seconds.
[[start:3392522][end:3396430]] And you can see that the computational time is exponentially growing.

56:37 [[start:3397190][end:3412694]] But if you have a very small search threshold, you have that computational time that makes sense for implementation in real world, right?
[[start:3412732][end:3420386]] So here for N equal to four, that is four times steps into the future, it's only taking 0.1 second.
[[start:3420418][end:3421302]] And that's okay.
[[start:3421436][end:3431722]] I can still do simulations with this complexity, but there is no way I can talk about how less the computational complexity is.
[[start:3431776][end:3436678]] It truly depends on the nature of your prior preferences and environment in action.

57:16 [[start:3436774][end:3443840]] But this search threshold actually works in real life, and we just saw that in our simulations, right?

57:24 [[start:3444210][end:3448350]] For N equal to four, it took only like 0.3 seconds in our simulations.
[[start:3448510][end:3456830]] But if you set the search threshold as zero, it already is 300 seconds for doing full depth planning.
[[start:3456910][end:3466470]] And if I set a planning depth of five, then it will basically run forever maybe, and I will not be able to do simulation.
[[start:3466810][end:3469750]] So that's the idea of search threshold.

57:50 [[start:3470810][end:3472940]] So actually, that's it.
[[start:3473790][end:3486762]] I wanted to explain the Agent class, the environment class, and the particular demo and yeah, maybe it's a good time for questions if anybody was listening.
[[start:3486906][end:3499138]] And I hope people get to play with this code and look at the tutorial and implement this and build generative models like this.
[[start:3499224][end:3509518]] So this particular example is how do you build a generative model for this grid world task and see how the Agent is able to take meaningful actions?

58:29 [[start:3509694][end:3516262]] But here we gave it that true structure of the environment in the B matrix and A matrix and so on.

58:36 [[start:3516396][end:3532700]] But you can also play around with learning in the sense that while defining the Agent step, you can add a flag that says learning equal to true.

58:54 [[start:3534750][end:3541962]] And if you start with an uninformed AB and so on, you can experiment on how the Agent is learning that environment.
[[start:3542026][end:3550530]] Here you can look at the B matrix in the beginning, you can look at the B matrix after, say, ten trials and see how the learning is taking place here.
[[start:3550600][end:3555058]] It doesn't matter because the agent knows the structure and it won't learn much.
[[start:3555144][end:3560914]] But if it starts from an unknown structure, then there is scope of learning also to be implemented.
[[start:3560962][end:3572646]] And it's already implemented because we are using existing Pymdp functionalities for learning A and B and it's already part of the step function.

59:32 [[start:3572828][end:3585260]] So I hope step function is clear, which is the only thing you need to know if you're trying to implement sophisticated inference and just the names of these matrices if you want to probe them and look at them.
[[start:3585630][end:3589482]] And yeah, I hope the session was useful.
[[start:3589626][end:3609362]] So I thank my collaborators and Connor, who maintains Pimdp, and also Brendan who runs the Pimdp Fellowship, which I was part of, and that's where I worked on implementing sophisticated inference in Pimdp and it will be part of the original Pymdp module soon.
[[start:3609496][end:3617378]] And I hope people can start using this module to simulate sophisticated inference experiments and this basically becomes useful.
[[start:3617554][end:3625240]] So maybe it's a good time to discuss questions or clarifications on the code or maybe it's a good time to take a break, as Daniel was.

1:00:27 _Daniel:_
[[start:3627870][end:3628570]] Thank you.
[[start:3628640][end:3629660]] That was awesome.
[[start:3630590][end:3636890]] Well, I have a few different questions and I'll read a few from the live chat.
[[start:3636970][end:3642750]] So I'll first just go to the live chat and then ask those and then ask some other questions.
[[start:3642820][end:3648814]] So Dave asks, how do you think about the neural implementation of recursion?

1:00:48 [[start:3648942][end:3654418]] Brains don't seem to implement computer hardware style recursion deeper than a stack depth of one.
[[start:3654504][end:3665190]] Aside from heavily over learned tasks, we can confine ourselves to asking about recursion for the purposes of exploring temporally deep state spaces, searching forward in time.
[[start:3665340][end:3680090]] So how do we reconcile this really beautiful and elegant and computationally efficient full depth tree search with the biological basis of multiscale planning?

1:01:21 _Aswin:_
[[start:3681070][end:3694142]] Yeah, so I'm not an expert in neural computation, but the answer to that would be basically you're doing only one computation at a time, right?
[[start:3694276][end:3704562]] And all you need is some memory to store your beliefs and use those beliefs to kind of do the same computation again.

1:01:44 [[start:3704696][end:3711906]] So we are not talking about this hardcore recursive implementation.
[[start:3712018][end:3714646]] We are only doing local computations at a time.
[[start:3714748][end:3723014]] And just because of the structure of the generative model and because we have memory, this can be done.
[[start:3723132][end:3729754]] And I don't see why brain can't do it, even though individual neurons might not be able to do it.
[[start:3729792][end:3731494]] The brain has memory.

1:02:11 [[start:3731622][end:3737226]] The brain has the ability to store memory and the ability to dream, the ability to simulate.
[[start:3737418][end:3739674]] It knows the consequences of actions.
[[start:3739802][end:3746286]] And you do this on a daily basis where you plan your future and decide what to do.

1:02:26 [[start:3746308][end:3746542]] Right?
[[start:3746596][end:3756050]] So on a single neuron level, I'm not really sure of how to answer that question, but I don't really see why the brain can't do it as an organism.

1:02:38 [[start:3758710][end:3759460]] Cool.

1:02:40 _Daniel:_
[[start:3760870][end:3762262]] Okay, to the code.
[[start:3762316][end:3764230]] I guess I have a few questions.
[[start:3764380][end:3766310]] Can we go back to the maze?

1:02:51 [[start:3771000][end:3775450]] And of course, if anyone else has questions in the live chat, just go for it.

1:02:57 [[start:3777500][end:3786596]] So in the maze, how does the moves that are possible, how is that reflected?
[[start:3786708][end:3795644]] What stage is it updated, for example, that it initially knows that it can only go up and then it can only go right or down?
[[start:3795842][end:3802684]] Where is that reflected with the updating of kind of that relational aspect of affordances?
[[start:3802732][end:3804530]] What is even possible to do?
[[start:3804900][end:3808530]] And then how does it evaluate in a deep tree search?

1:03:30 [[start:3810660][end:3816870]] Does it need to know what things could or couldn't happen in the future?

1:03:39 _Aswin:_
[[start:3819560][end:3829064]] So, if I understand the questions correctly, there is an important distinction between the generative process and the generative model, right?
[[start:3829182][end:3846620]] So in the grid world, which is the generative process, we have implemented all of that manually, where we have this transition dynamics that already knows what will happen if you take an action from a state.
[[start:3846770][end:3849950]] So it's like an environment that knows how to work.
[[start:3850320][end:3855376]] So it's like a reality where there are consequences of actions and it's already there.
[[start:3855558][end:3861808]] But this information is available to the agent to be part of its generative model.

1:04:21 [[start:3861974][end:3872164]] And in the generative model, what it basically does is use that transition dynamics, which is given or learned to simulate what might happen in the future.
[[start:3872362][end:3872916]] Okay?
[[start:3873018][end:3889530]] So once I have that transition dynamics, if I go to the where's the if I go to the tree search, what it is essentially doing is evaluating the posterior given a particular state and an action J.

1:04:49 [[start:3889920][end:3900404]] So from my generative model, I know that if I start from this state and if I take this action, I go to this posterior and I consider all the consequences.
[[start:3900552][end:3912610]] And if in the generative model, it is unlikely that if I go east, I don't go there and so on, it's automatically reflected in the expected free energy.

1:05:14 [[start:3914360][end:3916548]] So I hope that answers the question.
[[start:3916634][end:3943260]] So here, if I set the action precision to be high and also enable the so initially I am in this particular state, and with respect to the expected free energy, what I'm doing is I'm using my generative model to predict what will happen if I take four actions.
[[start:3943600][end:3947436]] And my predictions will say that if I take North, I will go here.
[[start:3947538][end:3950204]] And if I take all the other actions, I'll stay here.

1:05:50 [[start:3950322][end:3958640]] And because in my prior preference, north is more preferred, I can infer that north is the action I should go for.

1:05:58 [[start:3958790][end:3960130]] So that's the idea.
[[start:3960500][end:3963152]] So here, the grid structure is given to the agent.
[[start:3963206][end:3968164]] And it might be a little confusing, but the agent can also learn this grid structure and this will work.
[[start:3968282][end:3975684]] So once I know the grid structure as an agent, I can simulate the future and consider the consequences of action, right?
[[start:3975882][end:3977444]] So that's what's happening.

1:06:17 [[start:3977642][end:3987770]] And once I am in this state, I will consider the consequence of all four actions, and I will infer that, okay, going east is better because that will take me to this state.
[[start:3988300][end:4002130]] So there is always a difference between or you should keep in mind how generative model and generative process are two different things, and what the agent knows might not be the reality or might be the reality, depending upon what you give it.

1:06:44 [[start:4004260][end:4005344]] Makes sense.
[[start:4005542][end:4006290]] Cool.

1:06:46 _Daniel:_
[[start:4006660][end:4027380]] So if you were going to go about making a new situation that you wanted to do generative modeling for, do you tend to start from an existing working Pi MDP notebook and start modifying state spaces, or do you draw it out on a canvas?
[[start:4027540][end:4032408]] How would you recommend somebody other than replicating what is shown here?
[[start:4032494][end:4036180]] Let's just say we're interested in something that's not exactly just a maze.

1:07:16 [[start:4036340][end:4044220]] What do we do to get our head around how we should proceed?

1:07:24 _Aswin:_
[[start:4044880][end:4047180]] Yeah, good question.
[[start:4047250][end:4058210]] So if you are trying to simulate, say, a new environment, you have the heavy lifting to do, which is to define the generative model for the agent.
[[start:4058900][end:4065232]] You can either define a very sparse generative model, which the agent can learn, but you have to define the structure.
[[start:4065296][end:4071812]] That structure should be there, and only using that structure, the agent can learn the generative model.

1:07:51 [[start:4071866][end:4078680]] So here you can make use of this cell of code to understand how I define the structure of the grid.
[[start:4079020][end:4083672]] Okay, so I am defining a structure for the agent for it to make use of.
[[start:4083726][end:4088472]] I'm saying that there are 25 valid states and there are four available actions.
[[start:4088536][end:4094056]] And this is the standard way of defining the state space in Pymdp.
[[start:4094168][end:4101644]] And you also have to define the central parameters ABC and D for the agent simulations.

1:08:21 [[start:4101772][end:4107552]] So here I am defining A using my state space and observation space.

1:08:27 [[start:4107686][end:4115856]] But this step of giving it or telling it that it's an identity matrix is my decision choice in my modeling.
[[start:4115968][end:4119152]] I don't have to do this for simulations.
[[start:4119296][end:4126916]] I can see if the agent is learning it from a random A matrix or when it starts from a random A matrix.
[[start:4127108][end:4132932]] And similarly for this B matrix, this structure is defined.

1:08:52 [[start:4132996][end:4137428]] And there are functions like this which can give you a random B matrix.
[[start:4137524][end:4148760]] But this is a modeling choice where if I want to give it the grid structure or not give it the grid structure, I can start from a random B matrix, let the agent learn, and look at that learned B metric.
[[start:4148920][end:4150620]] Just for the purpose of the demo.
[[start:4150770][end:4154332]] I gave it the grid structure to enable it to take the actions.
[[start:4154476][end:4156624]] But it's not a mandatory thing.

1:09:16 [[start:4156662][end:4165208]] So this notebook is useful in the sense that you know what to do, but definitely you should play around with steps that may not be mandatory.
[[start:4165324][end:4172020]] Right, so if I give a prior preference for this state to be the maximum, then you can see behavior that.

1:09:32 [[start:4172090][end:4173652]] The agent will try and go there.
[[start:4173706][end:4173924]] Right.
[[start:4173962][end:4182456]] So this prior preference is defined in conjunction that this is the goal state, but this may not be the goal state.

1:09:42 [[start:4182558][end:4187800]] And in a different ask, what prior preference means is different according to the environment.
[[start:4188380][end:4189140]] Right.
[[start:4189310][end:4191304]] So that's also there and your prior.
[[start:4191352][end:4199668]] So once you define that generative model, which you have to do, you can't run from it, then everything is kind of automated.
[[start:4199784][end:4208876]] The agent only have to use the agent step, give it the observation from the environment.

1:10:08 [[start:4208988][end:4215140]] The agent knows how to take actions, and then everything that happens inside the agent, you don't really have to worry.

1:10:17 [[start:4217480][end:4228200]] So this structure, I'm sure, will be useful for your particular task that you are trying to model in your hmm.

1:10:31 _Daniel:_
[[start:4231660][end:4233512]] Yes, very interesting.
[[start:4233646][end:4242232]] And how would you contrast that or point to any similarities or differences with how this would be pursued outside of active inference?
[[start:4242376][end:4259520]] Like if somebody were just going to use another kind of deep policy agent in the maze example, what parts of the process would be familiar and what parts would be like a lot of work that wasn't expected or skipping through parts that were a lot of work otherwise.

1:11:00 _Aswin:_
[[start:4260020][end:4260770]] Yeah.
[[start:4261700][end:4269076]] So the general structure is very familiar to somebody who does things like this in reinforcement learning.

1:11:09 [[start:4269178][end:4283544]] So the idea that it's an agent step and environment step, so this is the standard OpenAI gym way of writing an environment and a standard OpenAI way of writing an agent.
[[start:4283742][end:4284104]] Okay?
[[start:4284142][end:4294572]] So if you have a Q learning agent who does the same trying to navigate, then the way you have to define the queue matrix is the heavy lifting there.
[[start:4294626][end:4296632]] It's just a state action mapping.
[[start:4296776][end:4303072]] And in contrast to that, in active inference, you have to come up with a generative model that you want to see.

1:11:43 [[start:4303126][end:4306784]] So in active inference, generative model is the central thing.
[[start:4306822][end:4307410]] Right.
[[start:4307940][end:4314204]] Without a generative model, there is no meaning of purposeful behavior in active inference.
[[start:4314332][end:4323124]] So the only unfamiliar part for a person who is coming from, say, a field like reinforcement learning is the structure of the generating model.

1:12:03 [[start:4323242][end:4329796]] But there is no way, other than getting used to it, where it's the palm DP structure which dominates.

1:12:09 [[start:4329908][end:4338700]] But if you're doing deep active inference, all of this is going to be neural networks and palm DPS are also not active inference things.
[[start:4338770][end:4339052]] Right.
[[start:4339106][end:4341676]] It's an industrial engineering thing.
[[start:4341858][end:4356716]] So palm DPS must also be familiar for people who are coming from the computer science background, just the idea that what really happens in the agent is the active inference part where we have expected free energy s and variation of free energy energies.
[[start:4356828][end:4362172]] And if you want to learn about that, then you have to go to the agents and see how it works.

1:12:42 [[start:4362326][end:4365044]] Look at the matrices numerically, see what's happening.
[[start:4365162][end:4370228]] But in a level where you want to get started, I don't see any problem.
[[start:4370394][end:4379172]] All of this is standard frameworks like palmdps and OpenAI gym environments, agent environment loop.
[[start:4379236][end:4383444]] All this is very deeply discussed in computer science.

1:13:03 [[start:4383572][end:4388750]] It's not cool.

1:13:10 _Daniel:_
[[start:4390560][end:4407090]] So what other motifs or cognitive phenomena are you excited or how do you see the Pi MDP development trajectory continuing after your sophisticated inference gets pulled in?

1:13:27 _Aswin:_
[[start:4407540][end:4420404]] Yeah, so the Pimdp had the original functionality and the functionality to implement or simulate general active inference agents with the policy space and so on.
[[start:4420442][end:4437592]] And that enabled a lot of people in the community who are not familiar with complicated coding and so on, who people who do psychology, psychiatry, and all the things.
[[start:4437646][end:4437828]] Right.
[[start:4437854][end:4443932]] So whoever want to come up and try implement active inference, pymdp enabled that.

1:14:04 [[start:4444066][end:4452828]] And I am hoping that this module will enable people who want to try out sophisticated inference experiments in their particular domain.
[[start:4452924][end:4466756]] So if you spend some time and get familiarized yourself with the structure of how Pymdp works, then everything else is just writing a jupyter notebook with minimal code, right, to simulate this.
[[start:4466858][end:4475624]] So if you have a particular task in your domain, I don't see a problem for a beginner to kind of try and code it.

1:14:35 [[start:4475662][end:4487048]] And what I'm very excited to see is people using this module for variety of experiments, just like how people started using Pymdp and sophisticated inference is taking off.
[[start:4487214][end:4495992]] And it's now widely talked about how it is the way of doing active inference.

1:14:56 [[start:4496056][end:4504000]] And I'm really hoping that people in various domains start using this module and see their experiments, and I look forward for the feedback.
[[start:4504420][end:4513090]] Yeah, so what Pimdp did two years ago, I'm hoping this module will do to people who are trying to model active inference in the soap state.

1:15:14 _Daniel:_
[[start:4514840][end:4542910]] So you mentioned the OpenAI gym and the standardized format, and what benchmarks do you use or what kind of test suites are you comparing, and how do we really know when we've made a generative model that really exceeds or excels in a way that other techniques are just not doing?

1:15:43 _Aswin:_
[[start:4543520][end:4551276]] Yeah, so if I may go to the OpenAI gym website, we have several experiments.
[[start:4551308][end:4558768]] There the classical reinforcement learning examples like the lunar lander that you see in this screen right now.

1:15:58 [[start:4558854][end:4565680]] So active inference from its inception has faced problems of scaling to tasks.
[[start:4565760][end:4571296]] And that's in itself a field of research in active inference, scaling active inference.
[[start:4571328][end:4577256]] And that's one of the reasons why deep active inference took over dealing with tasks like this.
[[start:4577358][end:4584564]] So there are benchmarks even now where the sophisticated inference may not be able to deal with state spaces.
[[start:4584612][end:4586360]] And personally, that's my research.

1:16:26 [[start:4586510][end:4587408]] In my PhD.
[[start:4587444][end:4598524]] I am actually looking at optimizing computations in sophisticated inference algorithms that lets you scale up to environments like that.
[[start:4598642][end:4611344]] But to get started, you will have to kind of write code and see if it works for an environment, then look at if it's not working, then you have to look at methods to scale it up and so on.

1:16:51 [[start:4611382][end:4620708]] So if I am talking about benchmarks, sophisticated inference is as good as any RL algorithms for this state space.
[[start:4620874][end:4624932]] So for small problems, sophisticated inference will work and it's really good.

1:17:05 [[start:4625066][end:4635492]] But for high dimensional problems like this, the classical implementation that I just showed might not work, but it's good enough for any decent experiment.
[[start:4635556][end:4644284]] But if you want to scale up, then that's still open and it's a new field of research and what you do might become a next new important paper.
[[start:4644402][end:4647596]] So that's all I can tell in that regard.
[[start:4647778][end:4648268]] Cool.
[[start:4648354][end:4650544]] You have to work and see what.

1:17:30 _Daniel:_
[[start:4650582][end:4663380]] Measures do you think you'd be looking for, like computational resources or what are the measures that even make sense to juxtapose such different methods?

1:17:44 _Aswin:_
[[start:4664040][end:4672544]] Yeah, so the OpenAI Gym was designed for that, to compare different algorithms.
[[start:4672672][end:4677188]] So OpenAI Gym by definition is a collection of many environments.
[[start:4677284][end:4680308]] So in my demo, I was talking about the grid environment.
[[start:4680484][end:4690890]] Openiigm is nothing but a collection of many environments which will let you interact with those environments using the environment step function.

1:18:12 [[start:4692620][end:4693224]] Yeah.
[[start:4693342][end:4698424]] So here we have the environment step function that will let you interact with the lunar lander.
[[start:4698552][end:4706736]] And that particular task will have matrixes that lets you judge how good or bad your algorithm is.
[[start:4706838][end:4716484]] So in this lunar lander problem, how optimally can you land your rover between these two flags by spending minimizing the fuel and so on.
[[start:4716522][end:4723732]] So those matrices are very tasks specific, and that's one direction you have to take.

1:18:43 [[start:4723786][end:4741564]] You can take try and compete with RL algorithms in matrixes, but the right potential or the potential I see in sophisticated inference is modeling intelligent behavior, where in RL the focus is to get things done to make this work.

1:19:01 [[start:4741682][end:4746072]] But it's not really explainable, especially deep RL and deep learning methods.
[[start:4746136][end:4755392]] But in active inference, if you manage to scale it up, they are explainable and that will let you understand how intelligence emerges with time.
[[start:4755526][end:4767860]] And I see that more interesting than competing with RL, because if your focus is getting things done, then maybe engineering is the right way and not active inference.

1:19:29 [[start:4769880][end:4770532]] Awesome.

1:19:30 _Daniel:_
[[start:4770666][end:4773300]] Any other comments or thoughts?

1:19:42 [[start:4782070][end:4784710]] Aswin, do you have any other comments or thoughts?

1:19:45 _Aswin:_
[[start:4785290][end:4787494]] No, I'm pretty happy.
[[start:4787612][end:4790214]] I hope I was clear explaining the code.
[[start:4790252][end:4800246]] Maybe it was too complicated or simple, depending upon your level, but I hope it is useful to at least one person who would start using this and write the code.
[[start:4800428][end:4802022]] Thank you so much for your time.

1:20:02 [[start:4802156][end:4802550]] Awesome.
[[start:4802620][end:4803960]] And thank you for the opportunity.

1:20:05 _Daniel:_
[[start:4805450][end:4806634]] Thank you for joining.
[[start:4806682][end:4807550]] Till next time.
[[start:4807620][end:4808400]] See you.

1:20:09 _Aswin:_
[[start:4809010][end:4810046]] Thank you so much.
[[start:4810148][end:4810410]] Bye.
