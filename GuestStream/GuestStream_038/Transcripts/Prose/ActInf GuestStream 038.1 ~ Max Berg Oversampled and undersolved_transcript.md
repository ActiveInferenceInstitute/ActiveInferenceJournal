
00:06 _Daniel:_

Hello and welcome.
It's March 9, 2023.
We're in ActInf GuestStream number 38.1 here with Max Berg.
Thank you, Max, for joining.
This is going to be great.

00:19 Really looking forward to your presentation and discussion.
So appreciation again for joining and looking forward to what you'll share with us today.

00:29 _Max:_

Yes, thank you, Daniel, for having me. As I was introduced,
my name is Max Berg.
I come from the University of Marburg and I'm a clinical psychologist.

00:41 I want to do a little bit of impression management first.
So Marburg is next to Frankfurt, in case you don't know.
It's a small or medium city in Germany.
And regarding me, I'm interested in the intersection of clinical psychology, neuroscience and philosophy.
That doesn't mean that I'm an expert in all of these fields.

01:02 Of course, I have a lot of knowledge in clinical psychology, I would say, and the rest is more of my hobbies.
And so it's important that you keep in mind to expect a clinical perspective today.
I'm not an expert on Bayesian mathematics or anything like that.
I know a little bit about it and I've read books about it and try to keep myself updated.
But it's not my expertise.

01:27 My expertise is clinical psychology.
And what I want to present today is like a paper about depressive rumination.
But we will see that it's not important that it's depressive rumination.
And rumination is a much broader construct here and we want to rephrase, like depressive rumination from active inference lab perspective.
And this is what we want to talk about today.

02:03 I want to start with a little quote.
And it's romantic is the coin of my realm.
Interiority breeds interiority.
And we will see that this might be literary true.
And this is why I think it's a good quote to start with.

02:19 So what is rumination?
It is defined by the APA as obsessional thinking involving excessive repetitive thoughts or themes that interfere with other forms of mental activity.
It is a common feature of OCD and generalized anxiety disorder.
I actually don't know why these two disorders were chosen first, but well, here we go.
I just quoted them here.

02:45 I would add a major depression to the list, and at least in my mind, major depression is the prototype disorder for rumination.
But sure, OCD and generalized anxiety disorder also has a lot of rumination going on.
And here you can see a first really important point, namely that Rumination is a transdiagnostic marker.
Right.
It's important for multiple psychiatric conditions.

03:15 And yeah, as such, it's an important transdiagnostic risk factor and it can predict, actually depression scores and subsequent measurement time points.
And this is what makes it interesting.
There was like a grant, a small grant proposal by, I believe, the Wellcome Trust in the UK where they gave grants for writing systematic reviews about transdiagnostic topics in mental health.
And unsurprisingly rumination is one of the topics where they gave or where they wanted to have systematic reviews for which they can see that it's an important topic where people really believe that it has some utility, clinical utility.
And unfortunately it is also the case that it's associated with worse treatment response for psychotherapy and also for medication treatment.

04:21 Yeah, and let's make it more complicated, shall we?
The rumination is sometimes used interchangeably with the concept of repetitive negative thinking.
And sometimes repetitive negative thinking means rumination and various varying.
But we will use the definition of rumination in its broader sense today.
So when I talk about rumination I also mean varying some of the time.

04:50 I just wanted to make this clear at the beginning so I use it in the older broader sense.
So to say yes.
So why would we need a new concept for rumination?
Well, reinforcement learning, I would say reinforce struggles to explain the constant continuation of ruminative thinking.
To make it short, why should you continue with doing something that is not giving you like pleasure or any good feelings in the short or the long run?

05:29 Why is something continued despite not promoting action and also leading to depressed mood?
This is a question at hand.
It's not an easy question to answer, I would say.
And this is why we would say that we have to not only take exploitation learning into account but also take exploration learning or surprise reducing learning or free energy minimization into account, however you want to call it.
The important part is you have to take into account that not all learning is done in the sense of like reinforcement learning but there's also learning that we do to know more about the world.

06:15 And if this goes wrong, rumination can occur and this is how we want to rephrase it today.
Yes.
So this is the roadmap for today.
We want to reconceptualize Rumination as an extreme case of failed mental problem solving.
We want to present a model of Rumination using active inference terminology.

06:35 So this will be a conceptual model.
We don't have the mathematics to back it up at the moment.
I will talk about this limitation at the end again and we will also discuss neurobiological correlates shortly to then continue to point towards treatment implications of the model.
So the next part is like I want to talk a little bit about problem solving and mental problem solving.
And I've had a classic quote by Richard Dawkins that I really find interesting in this context.

07:10 It says survival machines that can simulate the future are one step ahead of survival machines who can only learn on the basis of overt trial and error.
The trouble with over trial is that it takes time and energy.
The trouble with overt error is that it's often fatal.
Simulation is both safer and faster.
And I think this is really interesting and we can talk about also like this evolutionary perspective later.

07:40 I have really broke it down into simple terms first, okay, so when I want to solve problems using my mind, what do I need to do?
Well, at first, I need to think about what to do next, what do I want to think about, so to say.
And we have called this step candidate sampling.
So it's meter policy, basically.
So what do I even want to think about before thinking about what are important tasks of today, for example?

08:11 And then the next step is policy evaluation.
Or if I think about that, what are the expected results?
If I tell them about this concept, will they understand my talk today, for example?
And then let's say, yes, I hope that this is the case.
Then we have to do another step and do the actual problem solving.

08:34 Okay, now I'm convinced that this might be the right way, but how to do it, how to actually solve the problems, which are the steps necessary?
And these three steps we will consider over and over again today.
And whereas in the paper, neat little example that happens to me a lot.
That's one of the reasons I recharge it today.
Imagine you lost your key.

09:04 And now what we typically do is at first we check the usual places, oh, have I put it there?
No, have maybe put it there.
And after a while, if this doesn't work, my policy changes typically.
And I think, okay, where did I see my key the last time that I saw it?
And trace it back, and maybe this works and I find my key back.

09:31 And a few days after, I have the same problem again because I already lost my key again.
And what I may do after a few instances of this behavior is like, okay, I need to change something fundamentally in order to get my key back faster.
And so in Beijing, learning terms at the beginning, my expected prediction error minimization is just search the usual places.
It might work.
Okay, after a while, the mental policy, okay, why do I keep losing the key?

10:10 And how do I solve this problem?
Might lead to a higher expected free energy minimization or prediction error reducing properties.
And this is why I switched the policy, right after a while.
So this meter policy step decides how to go or how to go about a given problem, in this case, how to find my key.
Good.

10:35 This is really important.
We cannot search the intractably large probability distribution for this step.
It's not possible to remember all instances where I lost my key and to compare, like, promising strategies based on the whole distribution.
I'm not able to do this.

10:56 No machine, no living being.
We have to find fitting samples, so to say.
And fitting means it's usually based on heuristics.
What did I do the last time when the key was gone?
How can I find it?

11:12 This will become important later, because these Heuristics can run into problems.
They help us, like, make computationally intractable problems solvable.
But these heuristics have also their downsides as we want to discuss.
Okay, then, step two.
Now, policies are then selected if they provide a trade off between pragmatic and epistemic value and pragmatic is okay, I have a good chance of finding my key back to stay on the example.

11:49 And epistemic is I learn also something about finding keys or understand the world better.
And this is also important.
Whenever I choose a specific policy, high opportunity costs may arise.
What I mean with that is when I pursue a searching process, for example, for finding my key, I cannot continue preparing my talk or something like that.
So every decision I make has necessary costs because I cannot pursue other goals at the same time and this is also becoming going to become important.

12:32 So in order to be chosen by an organism, each chosen policy has to outweigh the resulting opportunity cost.
Otherwise it's not adaptive, right?
Okay.
And now the last step, the mental problem solving.
Good.

12:52 I now decided for one strategy of finding my key and now I have to actually pull it off.
So where to search, what to do next, which sequences of movements do I have to perform and how to go about it best and typically in different strands of literature, not just an active inference.
I need to perform something that is called research.
You know this from chess playing typically or from chess computers.
They do it a lot better than we do, but they look okay.

13:27 If I do this move and he does this move, then I can do this move and in all moves that follow it, I have a good position.
And it's again not possible to search the whole tree because the more branches, the more branches are daughter branches of these branches again.
So the tree grows exponentially.
So I need to have a strategy of not searching through all the branches.
It's called a pruning strategy.

14:03 In the case of Bayesian learning, it's often occam's window, meaning that branches are not searched through if they don't promise a prediction error minimization that is sufficient to pursue searching them.
This can also lead into problems because if a branch at first doesn't provide enough prediction error and minimization, it will not be searched through despite the fact that it could have some prediction error minimization further down the road, so to say.
But we have to prune again because it's not possible to search the whole distribution.
Okay, so with these three steps in mind, we can have the following model.
So we have the candidate sampling how to go about the loss key, so to say, policy evaluation.

14:57 If I do the strategy, do I have a good chance of finding the key and learning something about the world and mental problem, how to actually pull this strategy off.
And I want to say one really important thing and this is an increase in mental problem solving is a normal process in a lot of situations, right?
So for example, if I lose a person, that is really important for me, it's normal that my general model decreases.
Like a lot of my strategies for getting social supports don't work anymore because the person is gone.
And so in invasion terminology, prediction errors increase after such an event and this is a normal process.

15:46 And if, like, my general model declines, this was linked in the active inference literature to bad mood or to feelings of sadness, for example.
And in such cases, typically you think more about fundamental things in your life, everybody knows it and has experienced it.
If you don't feel well, you tend to think more and to try to get into a better situation again and hopefully what happens then is okay.
For example, I lost someone, my social support system is breaking together or breaking apart, falling apart.
So after a while, I search for people that I like and that can form a new bond with.

16:42 And hopefully, after a while, my prediction errors become smaller again.
But therefore, I need to take action.
I need to think about what to do with my lies, how to get to know new people in this example, to reduce my prediction errors in this case, regarding social support.
And then I have to pull it up, I have to go to certain places to meet people and hopefully after a while of sadness and difficult times, my general model fit increases again.

17:22 But this is not always the case, as we now want to discuss next.
So I have yet another quote.
You will get to use two quotes today, sorry.
The next quote is about rumination and it says shut up, she tells her monkey mind please shut up, you picker of knits, presser of bruises, counter of losses, fear of failures, collector of grievances, future and past and now we want to discuss what happens when this doesn't work.
So it can happen that despite trying, agents and organisms don't find good approximations for important problems in their life, right?

18:03 And if this is the case, the prediction errors regarding these problems stay high because surprising doesn't get resolved.
And despite trying, the organism tries over and over again.
Prediction errors say hi, surprising doesn't get resolved and the prediction error doesn't reduce again and the problem stays.
And what we now want to do is discuss reasons for why this happens in depressive rumination.
And at first we have to say okay, typical rumination problems have high complexity with uncertainties at many hierarchical levels.

18:45 If you think about problems, for example, like why is the world such a cruel place?
For example, this could be a nice rumination problem.
You would have to gather a lot of evidence from different strains.
It's really hard to actually disprove such a claim or to prove such a claim or even to say what it means.
And this is why there might be no efficient solution for such a question.

19:15 It's not like navigating a maze or something like that, but it's much more complicated.
And in addition, sometimes like we human beings have very high precision demands for solutions.
For example, after I may have survived a traumatic event, I might be really reluctant to go to similar looking places again.
And I have to be really sure that the new place where I don't want to go is really different from the place where something bad happened to me.
And if I'm not sure and sure means really sure, high precision, I won't go there.

20:01 And these complexity demands can also make an efficient approximation to a problem improbable.
And this might be one reason why problem solving isn't functioning in the case of Depressive Rumination.
Another reason might be over pruning and missing action policies.
So as I said beforehand, like pruning in order to action properly, or let's say this way, pruning is a good strategy when the parts of the surge tree that I remove, so to say, don't yield.
Like at the beginning, small losses and at the end large gains.

20:53 Because if it's like that, the tree branch might be pruned away despite actually helping the organism to reduce surprisal.
But the organism will never find out because it gets pruned away.
And the next thing is also, action policies can only be thought through if an agent knows about them.
We know about a lot of depression patients with a lot of childhood adversities that actually don't know a lot of strategies for navigating social environments.
It's not their fault, it's a consequence of childhood adversities.

21:31 But nevertheless, this is a problem.
If I don't know the solution for a social problem, I cannot approximate a solution because action policies are missing.

21:44 And the next problem might be that after many failed attempts of problem solving, I might not even have a reason to engage in deeper instrumental learning.
What I mean with that?
I go back one slide.
After a while I have an idea.
Okay, why is my life becoming so shitty?

22:09 It is because I don't engage with other people anymore.
I just lie in my bed and feel sad.
Okay?
And now normally there would be a step where I think about how to engage with other people again.
But if I have, for example, missing action policies, really bad mood and not a lot of strategies, I might think this through shortly and think, well, I can try, but they won't like me anyway.

22:39 So instead of deep mental problem solving, I jump back to step one, which is why do I have so many problems with other people?
And there you can see illuminated circle is forming and no deeper engagement is possible anymore.
And if this happens, my prediction errors stay large and more candidate sampling occurs.
Okay, I cannot solve this by meeting other people, but maybe I can do it on my own.
No I feel so sad and lonely.

23:16 You see where this is going.
I do not engage anymore in deeper problem solving, but instead thinking through a lot of policy candidates and none of them is like giving me confidence that I can solve my problems.
So I stay at the same meter policy selection step, so to say.
And in consequence I have less instrumental thinking and less instrumental learning.

23:46 And this also has consequences.
For example, the pragmatic value of policies are estimated to be low due to low model fit.
And this even becomes worse over time.
So if I think I cannot do it, I will not train it.
If I do not train it, I become even worse at doing it.

24:09 And so it becomes more and more improbable that I try because my action policies become more and more under trained.
And this is another really important problem.

24:29 And the next problem is the opportunity cost because I ruminate a lot.
So now we are at a meter level, I don't do much else and because I don't do much else, my model fit further declines.
And yes, the rest we talked about on the last slide.
So Ruminated states may be learned as the agent's default response for, quoteunquote, dealing with problems after a while.
And now we have a wishes cycle here.

25:05 And the next thing that I want to discuss is how neurobiology might play a role here.
And I have had a little joke of Phil Colette ripped off for my slides here and quotation by Karl Friston that says an agent does not have a model of its world, it is a model.
In other words, the form, structure and states of our embodied brains do not contain a model of the sensoriums.
They are that model.
And on the right you can see like a Yale School of Management guy that actually really embodies this principle as he's clearly showing on his backpack.

25:49 Okay, jokes aside, what was supposed to be said?
The Default Mode network is going to be important for our discussion here.
The Default Mode network is a largescale network with mediofrontal, temporal and pariatal regions in the brain.
It's important for introspection, selfreferential thinking and autobiographical recall.
So in short, it's important for everything mental, problem solving and Rumination related or a lot of these things.

26:18 And this is why it's unsurprisingly going to play a role here.
And to be more precise, the frontal courtesies seem to be the main driver of memory recall in the Default Mode network.
So if the Default Mode network tries now I'm intermorphalizing it to recall a memory.
So where do I find the key?
For example, it uses the frontal regions to be the main driver of this process.

26:54 And it is the case that meter studies found a stronger coupling and a hyperactivation in Default Mode network structures to be correlated with Ruminations.
And there are actually two meter analysis that found this and it is also suggested that a coupling with sub Lagrangian cortex might contribute to the negatively agent nature of rumination MdD.
So we know, okay, Dmn is important for problem solving and for rumination and it's also found meta analytically that it indeed plays a role for rumination or at least it's correlated.
And in addition, meter studies also found evidence for a reduced frontier periodic control network within network connectivity in major depression.
And this is also interesting because as we discussed, our idea is basically that rumination means I get stuck in abstract thinking and don't use my instrumental learning capabilities as much.

28:06 And so it makes sense that in MdD we find reduced control network or front of periodical control network activity.
Note by the way that this part of the evidence line is more indirect than the part before, right, I don't want to gloss over this.
So while we have here a direct correlation with Rumination, in the case of the default mode network here it's more Mvd in general.
This is why we also wrote it much more careful in the paper because it's a more indirect line and I don't want to gloss over that.
And it is further more known that a connection between control networks and default mode networks seem to be reduced.

28:51 And interestingly these two networks have to connect in order to solve complicated problems.
They actually study about that and these studies suggest that if the problem gets harder for an individual, it uses more of the default mode network to do the meter thinking and then the control networks to do the problem solving and the interplay between the two is really important.
Okay, so in conclusion, what we think could be the case is that the default network is hyperactive and hyper connected.
Because it does policy candidate over sampling that we talked about before and the reduced mental problem solving.
Or instrumental learning due to the policy over sampling is reflected by the reduced resting state activation and the hyperconnectivity of the control networks and also of integration hubs like the insula.

29:58 Okay, then a short citation, it will be the last one and it's existentialist model and it says simply existence precedes essence.
And it wants us to say okay, in the first instance we are beings that get thrown into the world, but we have to do something with our lives in order to flourish and give ourselves reasons to live and to succeed.
And I want to talk a little bit about how can we get out of ruminative loops and what might be old idea and new dean.
At first I want to say there's good evidence for the effectiveness of existing psychotherapeutic treatment regarding depression in general and it's also regarding rumination.
So we also have like meta analysis specifically analyzing rumination.

30:56 However, we have substantial non responder rates for psychotherapy and also for current medication approaches.
We have a high chance for relapse after depression is gone, it will oftentimes reoccur in the life of patients, unfortunately.
And we also have substantial therapy dropouts so patients actually leaving therapy.
So it's really easy to say that psychological and pharmacological treatment needs improvement.
So they are effective but they don't help everyone and there's a lot of room for improvement here.

31:37 And there are multiple ideas that we briefly discussed in the paper and the first is like a simple idea but could be quite effective and has also meta analytical evidence that it helps.
And this is like reduce memory interference and rumination by physical exercise in the everyday lives of patients.
So doing more like especially endurance exercises actually helps reducing rumination even when compared to active treatment like CBT.
So maybe depressing patients don't only need therapy to be paid for but also to have a personal trainer that might be paid for.
And I only say this half jokingly, this could improve the life of a lot of people.

32:21 And another idea is more medical stylocybin or ketomine was shown in studies to increase the sampling entropy of the brain and this could also be an interesting prospect because we've learned that the samples are getting repeated over and over again.
But if we could have an idea for how to increase the variance of samples drawn then probability that one sample is actually a good idea for thinking through increases.
However, I have to say cautionary notes, especially with psychedelic drugs because it is a promising pharmacological avenue probably, but at the moment we have really small sample sizes.
It's hard to blind for these drugs between groups.
I mean, you know, when you are tripping it's quite easy to know.

33:20 So this makes RCTs difficult and we know from a lot of questionable research practices from this line of research, unfortunately.
I don't want to say that everybody in these fields are doing bad science, it's not what I want to say but I know from a few cases where preregistered protocols don't fit the results that were presented and stuff like this.
And if you combine all this it's actually quite hard to say whether these work really well.
So what we would need is really larger study, not these small brain imaging studies with 20 subjects, more like 200 subjects would be a beginning and we need the researchers to actually stick to predefined interpretations of their results so we can learn about more about this problem promising avenue.
Okay, and more ideas would be to change therapy a little bit and concrete idea is we could actually add problem complexity estimations into therapy.

34:33 What I mean with this is like ask patients, okay, how much time you spend ruminating, what typically are the results of these processes, what are the costs of these processes.
So we could try to make the costs of the process more explicit to the patient and to give them a grasp on how much opportunity cost they invoke on themselves by the process.
It's not typically done at the moment but it could be an idea for improving CBT and what is also important this is done in CBT, what I now tell by the way, but it's really important to keep it in mind.
We learned that a good problem solving requires an intricate interplay between the false mode network and brains control networks.
So it's actually important to have optimal difficulties for behavioral tasks given to patients.

35:30 If it's too difficult, they will not do it and if it's too easy, they will not learn anything from that nor epistemic value is mindful to say.
And both options are not good for reducing rumination.
And there's actually another experimental treatment that shows some success, and it's called emotional flanker tasks.
And in these tasks, like, patients learn how to shift their attention away from bad emotions.
And this could also help stop the ruminative process, because we learn that, depending on your mood, you will have different heuristics in your brain about what you think about next.

36:12 And in the case of bad moods, you don't have the best heuristics.
So this is another idea for better treatment.
Yes.
Now I want to talk about a few limitations and then we can enter the discussion.
So one limitation is clearly that the model only discusses typical depression where behavior breaks down.

36:33 However, there are cases of agitated depression where behavioral output actually increases or to make it more abstract, depression is a really heterogeneous subject and also Rumination is really heterogeneous.
So we don't have a model actually at the moment that considers all individual trajectories.
So this is only a general scheme, so to say, but it will not fit every individual.
And the next thing is we describe plausible ways for Rumination development but we do not know whether these pathways play a cause or role in MdD development.
I said briefly that when I have Rumination at time point T, I will have more depression at time point T plus one.

37:24 But we do not know whether this is a causal factor but or only a coincidence in time, you know what I mean?
So this is also an unsolved problem at the moment and the last problem which is also important for active inference lab nursing in the community is it's not a mathematical model, it's a conceptual model that we did and so the next step would be to make a mathematical model out of it.
For example, like partially observable Markov decision process or something like this in order to be able to simulate it and to check whether the behavior that we set it would come out, actually come out.
So this is another major limitation of the paper.
Yes, I will skip over that.

38:12 I guess we talked about this enough.
So what I want to talk about shortly before entering the discussion with other projects that we want to do next with respect to active inference and what we actually have done and now under review at.
Psychological medicine is applying the active inference framework to heterogeneous social experiences and behavior.
And this is actually done in a mathematical precise way.
So there we have a hierarchical pond or partially observable Markov decision process model, and we use it for trying to explain, like, social withdrawal or other social problems in depression.

38:57 So it's a little bit rumination adjacent and it's more mathematicized.
A preprint is available, but it's not yet through the revision process.
And what we also want to do is like, simulate distorted social functioning and mental disorders and also to compare these simulations, or computer simulations based on active inference to empirical data, because this is also what we found in the literature to be missing.
We have the simulation studies, right, where we have like these simple games where active inference computer agents play like a trust game or something like that, or where you simulate hallucinations and psychosis.
And these are really good studies, don't get me wrong.

39:43 But what is missing, in our view, is a little bit combining these computer simulations with the behavior of human being to compare them within one and the same design.
And this is what we aim to do.
But it's an ambitious project and we are not finished, so this will take more work.
And another project that we actually will finish this year and we have done the literature screening is we have prepared like a systematic review of all active inference literature that is of interest for psychological treatment.
And this will hopefully at least be a preprint this year.

40:25 So thank you.
These are my coworkers in different projects to drop a few names.
On the left is Matthias Feldman, then Lucas Kirchner and Tobias Coupon.
These are the guys that I wrote the rumination paper with.
Then there's an Elena Ecker.

40:40 She's from theoretical cognitive science groups, and she does a lot of the computer models for our new projects.
So we need actually scientists that are better at programming than I am.
And she is doing a lot of the work here.
And then there's Philip Hatzok and Burgut Kleim.
And with those two people, I also collaborated on a predictive processing model of PTSD, which was also published in Neuroscience and Behavior Reviews at 2020.

41:17 Yeah.
So with that, I would like to thank you for listening and yeah, we can discuss a few questions if you want now.

41:28 _Daniel:_

Awesome.

41:33 _Max:_

Thank you.

41:36 _Daniel:_

Okay.
All right, well, thanks for the great presentation.
Looking forward to the discussion.
So, just to sort of begin, how did predictive processing and active become integrated with your and your colleagues research direction?

41:56 Were you looking for integrative frameworks and came across this area, or did this motivate you to study and enter into the clinical space?

42:08 _Max:_

It's a mixture of two things, I would say.
One is like observations in patients.
Maybe start with that.
So my friend Tobias Cooper got me interested in this stuff.
And he had a patient and this patient really had to struggle with social phobia.

42:31 And what was interesting about him that he was discarding information that would challenge his worldview to say right.
So whenever somebody said that he actually liked him, this one said, oh, no.
He just pretends to say this because he wants to be a nice guy.
But in reality, nobody likes me.
And this is what got us interesting, interested in this line of thinking about information seeking.

43:00 For example, how do organisms seek information to run their lives?
But also how do organisms discard information and stay in a depressed or in an anxious state?
And this is, I guess, one of the reasons why we started to get interested in active inference.
And another reason comes from my love or love from a lot of my colleagues for simple explanations.
And I don't dean simple as mathematically simple because I don't get most of the math, to be honest, fully.

43:40 But simple in the sense of we can have only a few axioms and explain sentient behavior with it, we can computer simulate behavior in it and it actually produces interesting behavior patterns that we know from the literature.
And this is the other reason why we got into it.

43:59 _Daniel:_

Awesome.
So many directions and ways to go.
But one excerpt from the paper that jumped out at me was the line between adaptive problem solving and self perpetuating maladaptive ruminating.

44:17 So how do we know that line and how does that play out when you're in the clinical context?
Like what is the appropriate amount of thinking or overthinking?
How do we really find that line and come to know it?

44:37 _Max:_

Well, there's a short answer that is we don't know.
So it's hard to say, to be honest, where the line is because in principle, maybe you find a good solution if you ruminate just 2 hours more, right?

44:51 You never know.
But we have an answer in the clinical field in practice and it's like a pragmaticist answer and it only goes okay, if you suffer a lot and don't get your everyday life sorted out, then it becomes a problem and we have like measures for that.
So you can assess the global functioning level of a person and say can he continue to work, has he friends, has he or she free time activity that actually fulfill her?
And this way you can at least say, okay, has this person a good level of functioning?
And if not, does rumination impair this level of functioning?

45:38 And yeah, this is a really pragmatic answer, sorry for that, but this is how we do it in clinical practice.

45:47 _Daniel:_

Totally makes sense also in that kind of clinical area.
So I was curious, other than rumination, what other trans diagnostic risk factors?
What are some examples of those risk factors and how might they be linked together in a kind of holistic understanding?
Or what is the active and non active way of thinking about the causes and consequences of these trans diagnostic risk factors.

46:20 _Max:_

One that jumps to mind is emotion regulation that comes up over and over again.
So this is a risk factor also for depression.
It's a risk factor for borderline personality disorder but it's also a risk factor for violence.
So a lot of things are connected to poor emotion regulation and I have to think shortly to get an active inference answer out of that.
There's actually a paper, a new one by my colleague Philip Hatzok about like a predictive processing model of borderline personality disorder where he describes in more detail.

47:00 So he is the expert there but maybe we can just look it up before I make stuff up that it's not.
Can I just search it shortly and give us an answer?

47:13 _Daniel:_

Sure.
This is internet extended cognitive rumination yes.

47:22 _Max:_

Because I don't feel confident enough to talk about stuff that was not my main area of research.

47:36 _Daniel:_

Extended rumination you could make a script or a computer program.
That just iterates.
And whether it experiences that in an anxious way kind of a second question but at least from that functional side it's as if ruminating yes.

48:04 _Max:_

So I have the paper here.
Do you see it now?

48:07 _Daniel:_

Yes.
Thank you.

48:08 _Max:_

Yeah.
So let's see here.
They actually have a model of active inference terms.

48:15 So let's see where it starts.

48:25 And it's actually not so simple.

48:31 Okay, so what they want to explain is basically how childhood male treatment leads to borderline personality disorder.
And this is important for my transdiagnostic marker of reduced emotion regulation because bad emotion regulation is the symptom of borderline personality disorder and what they say is, okay, let's see that.
We have two relevant factors here, strong negative belief about the self and others.
It's also typically known for borderline personality disorder.
So we have high precision to active inference lab terms here to my prior belief that other people are bad and I am also like a loser that cannot do anything right in his or her life.

49:29 And this needs of course if the precision of the prior is really high, new information doesn't matter.
And so we have a persistence of effects of hostility because if the others are all bad, well, I can be hostile towards them of fear and of sadness.
And in addition to that, also contributing to the temporal fluctuations because we know that borderline is characterized by sometimes like I really like my therapist as a borderline patients and after a while I really hate him and not a lot in between.
And this may come about due to like a high uncertainty of beliefs about consequences of action.
So here about policies.

50:16 So here my standard deviation is really broad and due to that belief updating regarding policies gets passed.
And this is why I show instability while at the same time also showing persistence.
And I show persistence of my worldview but instability of my behavior.
And this is how they try to explain borderline personality disorder in active inference terminology.
But this is only me giving it a try.

50:49 I only read the paper once, but this might be one way how to characterize like, symptoms of emotion regulation problems in a conceptual model using Bayesian terminology.

51:07 _Daniel:_

Awesome.
And also in this paper and in yours, it's on the roadmap towards formalization.
Not like that's the only endpoint, but going from the empirical evidence and the ways of thinking and knowing in the clinician's office through the integrative frameworks to the pros and to the graphics that connect different nodes and edges.
This figure and the ones that you drew, they're not exactly a Bayes graph, so it's not exactly ready to be entered into a computer program.

51:41 But it's also not far from a Bayes graph.
You have variables that could basically be variables in a Bayes graph.
And so it moves along and brings collaborators and so on, as in a kind of methodologically plural way.
There can be development on multiple fronts and integrate the neuroimaging and the predispositions and then the treatment modalities in a way that's not just like following the causal chain of the ideology, but rather approaching it almost like in.
A reverse problem solving way, starting with the clinician's awareness and view and first seeking to integrate and improve the sense making of the clinician even without a formal model.

52:40 _Max:_

Yeah, I would totally agree with that.
Not much I can say about it.
I think it's totally right what you said.
There maybe one thing in clinical experience, at least in psychology, I don't dare to speak of other fields, but their backward translation is really important.
So this is what you described, right?

53:00 So going back from the clinical phenomenon to more precise view, for example, in formal modeling and typically problems got tackled the other way around.
And this oftentimes doesn't work as well as backwards translation because typically problems got thought through by basic scientists that are really good at doing this formal modeling but don't model necessarily the right parameters from our view at least, because they lack the clinical experience.
And so both parties working together is really important.
Like guys like us bring in the important parameters, or at least where we think they could be important from clinical practice and the more mathematically inclined can model them.
And so there could be a fruitful collaboration between so start with backward translation, then do forward translation, then do another loop of backward translation.

54:06 And I guess this is a fruitful way of advancing psychiatry and psychology.

54:13 _Daniel:_

Wow.
So, a related question.
To what extent, either today or in the future do you think patients would be clued in to some of this lexicon and ontology?
For example, is it enough to just say, hey, here's the new recommendation, here's the new exercise plan?

54:40 Or is it explicitly oriented around communicating within these ways of talking about belief, uncertainty, information and so on?

54:52 _Max:_

I think it can be done with patients, and it should be done to a certain extent.
I think it's not plausible to teach them all the math and stuff like this will not be possible for at least a lot of them, for sure.
If you have a mathematics professor patience, it would be easy for him or her, but in most cases, no, not that.
But you could talk about precision, you could talk about surprising, you could talk about hierarchical learning, and I guess it's important to do this.

55:26 You could simplify models into like, vicious circles.
One could easily draw a simple vicious circle with the help of our remnant model and teach them or the patients a few Bayesian adjacent words, at least, to better understand their condition.
And I think this is important because psycho education actually is proven to help, right?
The more you know about the condition, the higher your chances of getting better are in a lot of cases.
And so I guess, yes, you could teach them at least base rules and a few simple things, not doing a lot of math, but like, drawing a few graphs and try to teach them the basics would be a good idea because I guess everybody can get what precise information is and what belief updating, how it functions.

56:30 In principle, this is teachable to most of us.

56:34 _Daniel:_

Yeah, one example that from the talk you mentioned, like, with the loss of an important person in our life, our social or our emotional support policies are going to have to be updated.
If there was some source we went to for information and that source no longer became available, we would have to change our epistemic foraging.
And of course, this exists in the social space.
And so when life changes, when our generative model or when our generative process, our niche changes, we should expect the unexpected.

57:12 It's a totally normal, surprising, but expected surprise event that opens up the discussion to like, there will be beliefs that will be changing, there will be new policies or policies that you didn't previously take.
Maybe now is the time to try them out.
And there's going to be volatility as you're learning the consequences of action.
So stick with it and try something three times before saying that it doesn't work.
Even without appeal to mathematics, that's very powerful.

57:49 And I think the way that somebody might say, well, in this double blind study, these two groups, this treatment that we're going to go with, it's been shown that in this context, these two groups, this group did better.
And no one says, well, slow down.
The Ttest used a lot of mathematics.
I'm not a statistics professor.
So people accept the epistemology of the group differential statistics and of diagnostic statistics, even though one could do 100 PhDs in theoretical statistics and in computational statistics.

58:28 And so it just speaks, I think, to the early stage when the field is even perceived as being math heavy because we're in such a methodological developmental stage.
But there will be layers and ways of working that will not mention any more technical detail than someone just saying the double blind study has provided evidence for X.

58:54 _Max:_

Yes, I can say two things about it.
The one thing is a philosophical thing Daniel Dennett talked about free floating rationales, right?
So a free floating rationale, in case you don't know, is like when lions go for givels.

59:11 It's an example that he likes to give.
The gazelles do these showboating types of jumps and the lions typically don't go after the gazelle that can show this behavior, but go after the injured ones that cannot do this anymore.
Right.
But we can be quite certain that neither the lion nor the gazelle knows what they are doing, but it works without knowledge.
And this is what he calls a free floating rationale.

59:39 There is a rationale behind the behavior of the lion, but he doesn't need to know it in order to take advantage of it.
And this is the case for science and this is also the case for patients.
You don't need to know every detail of a mathematical formalism in order to grasp some of the concepts and to advance your understanding of the world using these concepts.
But of course it helps, but for patients it's the same, and for us it's the same.
And I think free floating rationales are a really important concept to describe.

1:00:23 Why a lot of the times you don't need to know the exact formalisms.
And another idea that I want to give is more like science, of making niche constructions more applicable to the mainstream.
And this is well, at the beginning it's hard because you need to program every little bit yourself.
There are no toolboxes, nothing to help you.
Not really books, just a few experts.

1:00:54 But after a while books come out.
After a while you get toolboxes that actually simplify a lot of the process.
You don't need to write the helper functions yourself.
You can use the toolbox in a lot of cases and so after a while it becomes more widely applicable in science and maybe at someday, I don't know, Spss or something, one of these statistics software, maybe not SPF, has like a way to click through active inference algorithms.
That's it.

1:01:26 But then in principle everybody can use it.
Then you have new problems because people will use it without actually understanding it.
But I would predict that it gets simpler and simpler to use.
And I would say overall this is a good thing because this allows a lot more scientists to jump in on the endeavor.

1:01:49 _Daniel:_

Thanks.

1:01:50 Yeah.
Great points.
One of your quotes, the short one, was Existence precedes essence.
And it reminded me of a 2015 paper of Friston and mathis which is entitled I Am Therefore I Think.
And that of course is a little bit of an inversion on I think therefore I am, which puts rumination before the horse or the cart before the horse.

1:02:18 I'm not exactly sure, but I think therefore I am.
It actually puts thinking and ruminating first.
Whereas this existentialist quote that you provided concords well, with certain ways of thinking about reflexive systems in active inference.
So what did you mean with the introduction of that quote?
And how does that existentialist angle play out in the clinical setting?

1:02:54 _Max:_

Yeah, these are maybe two questions disguised as one.
I start with the existentialist worldview in clinical settings.
Well, I think it's important for clinical science and more so for clinical practice because we need to believe in a certain type of liberty in order to help patients.
If we believe everything is predetermined by, I don't know, brain chemistry, even if it's true, this will make changing your behavior hard because you can always say, well, I cannot change my behavior.
It's all in my, I don't know, genes or what type of biological reductionism you like.

1:03:41 So I guess we need these existentialist idea that you yourself are in control of your life in order to make therapy work.
Right?
So we need to at least have a compatible hard English word like this.
Even if determinism is true, we need to have it combined with some sort of liberty or belief in liberty.
And I guess this is where active inference jumps in, because active inference allows a formal description about self control.

1:04:18 And then we have a definition of acting in the world and learning new things that doesn't require, like, fairy tales.
And it's compatible with determinism.
And with this worldview, you have a worldview that on one hand is compatible with determinism and on the other hand allows for a concept like self control, agency policy, learning all the things.
And so it can also be used for psychotherapy.

1:05:00 _Daniel:_

Interesting.

1:05:03 _Max:_

I hope this answers the question, but this is what I can say.

1:05:07 _Daniel:_

Yeah, there's so much depth, obviously many threads and traditions in the clinical setting and that full stack from the manifest behavioral on through the cognitive and psychological, but verging or anchored in or descended from the metaphysical, that's a full spectrum area that seems like it must be navigated in the clinician's education.
But even in like the 1 hour that you're spending with somebody, I imagine that it could probably oscillate a lot in where you're focusing from.
Here's how to tie your shoe to here's why things matter.

1:06:02 Abstractly.

1:06:08 _Max:_

There's more philosophy, especially practical philosophy for therapy, than one would think because patients bring it up all the time.
Right?
I mean, one of the problems of depression is if it's going to be really severe, is this, for example, nihilism kicks in so nothing makes sense anymore.
And then, as you said, why should anything matter at all?
Then becomes an interesting question and a pressing question for them.

1:06:38 _Daniel:_

What's your go to response?
Why does anything matter?

1:06:43 _Max:_

It's a hard question I would try to get do you always thought that nothing matters?
What was different when something mattered for you?
How was your life then and what changed why you came to these conclusions now and how do you feel when you think about your old worldview versus new worldview?

1:07:10 So I would try to challenge their worldview by their own worldview a few years ago.
This is not always working because you have patients that have actually gone through a lot of difficult times in their lives but typically like their work view was not always depressed.

1:07:32 _Daniel:_

Yes, that seems to do multiple things.
By responding to a question with a question it puts an active posture back into the conversation.
So at the very least policies can be selected that aren't rumination and consequences could be learned.
Even if there's going to be a higher low precision on that learning at least it opens the door to movements.
Whereas just well person X said this or that, that response may land or inspire or not but it reifies the Pacification and therefore may not kind of like an inactive layer promote the movement.

1:08:30 _Max:_

Yeah, I just wanted to say awesome things the same and if you try something like person XY that says this is the reason why your life works, this will in most cases not work at all.
They will say something like but this person doesn't go through that many hardships that I did what is oftentimes true or something like that.
Right?
So often it's better if the ideas are sampled from their own generative models from a lost part of the distribution, so to say, and not from outside.
Typically you have to try to get them to think out of their own worldview and not of your work view or someone else's worldview with the seldom functions.

1:09:23 _Daniel:_

So another interesting area you mentioned the problem difficulty, complexity, time uncertainty estimations.
So kind of like a cognitive task analysis in the CBT setting where different tasks are estimated again along these axes of how challenging is that for you or how complex does that task seem to you, how does that really play out?
Because it really seems like something in the email inbox or in writing a paper with some improved signposting or learning even around which tasks are hard, which tasks are clear, which tasks are threatening our well being, those kinds of metadata on policy selection and being able to see that could help us select better policy and not to change our preferences.

1:10:36 Which is how sometimes behavior change is approached by changing what people are supposed to want, but by bringing this kind of cybernetic clarity around action selection to support people in different contexts, making the decisions that can then credibly be said to be more in alignment with what they do want.

1:11:04 _Max:_

Yeah, what is typically already been done is to let patients guess how high they would rate the probability of succeeding right.

1:11:16 So when we do this behavioral therapy, they are typically asked, okay, what do you think?
How probable is that?
You're going to go there until next week?
And it's a rule of thumb by clinicians that has no Bayesian science, but we say if it's 80% or higher probability, one should aim for it.
If it's lower, it's too difficult.

1:11:41 But if it's trivial, if it's 99.9% probability, it's also not worth typically pursuing, at least not always.
But I guess the problem with that is that I don't know a solution for this is my subjective probability, right.
How I think, how probable it is, I don't have a good grasp in all cases on how difficult it really is for me because there are all sorts of biases that would keep me from making such assumptions.
I don't have a solution for that.
But what would be good is to have more variables that we could estimate in order to actually have more information on how difficult a task is.

1:12:32 But for most cases we haven't.
And when we have them, we know that what patients think, how difficult it is and how difficult it really is hasn't the best correlation.
Sure, it's positively correlated, but how good I think my short term memory, for example, is and how good it really is is not the same.
And this is hard to solve problems for clinical science.
I have to think about it longer, but it would.

1:13:00 Giving patients tool to actually improve their probability estimates would be great.
But I guess it's also hard to do due to all these things that you said before.
Right.
If the problem is complex, multi layered, and has a lot of variation and good luck actually finding a way to estimating probabilities, but we could start for simple problems and maybe this helps patients, but I have to think about it more.
To be honest, it's not easy to find better solutions there.

1:13:37 _Daniel:_

Yeah.
Even just on paper or digitally journaling, but then eventually potentially integrating with the kinds of formal models we've been discussing, it can be really nice to know, hey, there's a lot of stuff that you said had a below 50 chance of happening and nine out of ten times you've done that.
So maybe next time you're in the zone of uncertainty, just go for it.

1:14:08 You tend to systematically overestimate your confidence in this or you overestimate how much other people will appreciate this kind of consequence.
And maybe writing three thank you notes a day would be a great use of 20 minutes.

1:14:28 _Max:_

Yeah, these are all really good ideas and this is also things that are done right.
What is missing, but what is doable in principle is tracking certain behavior.
Like an easy example would be aggressive behavior.

1:14:46 For example, counting how much verbal aggression was shown or physical aggression was shown over the days.
And then look what the expectation of the patient was.
And comparing those two and there you could do like patient belief updating in a simplified form.
Yeah, this would be a great idea.
It's always then possible I would say when the behavior is clear enough and easy enough to count right.

1:15:16 As soon as if it's getting more unclear this will not work but it could work for a lot of problem behaviors like self harm, aggression, lying in bed, like in depression, something like that.

1:15:36 _Daniel:_

So it makes me think about that contrast that you provided between reward oriented frameworks which struggle to describe rumination as it's not in the short or medium or long term necessarily oriented with rewards.
So the only explanation becomes well, something is off in the reward function which is kind of tautological.
And so that's a little bit of a local and a constrained explanation.
Whereas when we see policy selection external overt movement in the world as well as internal COVID policy selection like attention and mental action when we see those actions as being oriented around reduction of free energy which is bounding surprise and therefore, based upon what is likely, not what is necessarily the most rewarding.

1:16:35 It opens up that view to, again say, how many of this behavior do you expect to happen in the next week?
Yes, in a dream world we would aim for zero of event of this number.
We'll aim for you to be full time employed by next week.
That sounds awesome but what do we honestly expect in 12345 weeks?
And then we're going to actually be looking back in and then instead of maybe feeling like well you're going to leave the port and then you're going to have to sail across an ocean it can be more like there are checkpoints.

1:17:16 We're looking back at the buoys that we passed.
We have the next three buoys that we're looking towards.
We can do smaller corrections and there will be volatility so there's going to continue to be surprised.
We're not going to exactly hit every milestone per se but if we are on this trajectory we're going to be moving essentially as much as we possibly could in the right direction and spending less time just hypothesizing about like a total counterfactual world where the issue is already resolved.

1:17:51 _Max:_

Yes and this is a metaphor that is also used in therapy quite often, right.

1:17:56 The one of the mountain climber.
And the mountain climber typically needs a guide if he's a newbie.
And what psychotherapy can do is provide a good way over the mountain, so to say, provide a good place for resting, doing the next step, doing the next step, doing the next step.
And, yeah, this is really resonating with what you said.
Namely, we have to take a big problem and cut it into little problems that we can solve one after another, so it becomes plausible to actually solve it.

1:18:35 Yes, I would totally agree and emotional.

1:18:39 _Daniel:_

Flanker tasks, I'm not exactly sure what those would be.
But it just made me think of our policy selection throughout the day and all of the fires we have to put out or all of the bubbling soups that we have to tend to with thirst and rest and breathing and physical exercise and all of these different aspects to our cognitive and emotional well being.
It's like there's many things to attend to which is why our attention is so variable as a feature, it's not a bug.
So the fact that we have exactly pathological or not just neurodiverse states that involve a fixation of attention and also the inability to fixate attention, it just starts with our experience of the day and of our attention to our body and our surroundings and to the bigger questions that we know impinge on us.

1:19:46 But also we can't necessarily have the geopolitics and the climate change solved just by thinking about it but we also don't want to neglect what are important issues and then seeing strategies and having the discussion about strategies and tactics in that attentional space instead of in the reward space.
Not to bash or anything like that, but that conversation is about well, what should we value more or less and then why are these values translating effectively or not into behavior?
Whereas the attention and surprise angle is like being more in the game and your local view instead of watching the game and just saying, well, I want this to be the outcome.

1:20:39 _Max:_

Exactly, yeah, I want to say a little bit about this attention focus and attention spreading that you mentioned.
I almost said it in the talk but I say it now.

1:20:52 Like for example, ADHD is not necessarily like disorder in the sense that it's a dysfunction, right?
So it can also be described or maybe better described as a neurodivergent property of some human beings so they shift attention more easily and this is depending on the environment, a good thing because if you stuck your attention at one place too much well, you might not notice what is going around in your surroundings.
So you have to be able to focus away from certain points of attention.
And you want to have, in a group, individuals that have really sticky attention so they can focus on a task really good.
But you also want to have the other ones that have really floating attention spans in order to see new opportunities or see danger.

1:21:49 And so I think this can be really easily explained by evolutionary theory, right?
So we have variance over the population and this variance is not a bug, it's a feature.
And on the more extreme ends of the variance you find phenotypes that are problematic from time to time but depending on the surroundings, always depending on the surroundings, right?
So on the one hand you might have something like OCD like behavior and on the other hand something like more ADHD like behavior and it can even jump between the two.
Interestingly, but this is not necessarily always bad.

1:22:36 It really depends on your environment.
And that humans differ with respect to this parameters is also not a bug, but a feature of evolution, I would say, and also a feature of our learning history.
Of course.

1:22:51 _Daniel:_

Totally agreed.
For individual and collective behavioral strategies, they're often discussed as if they were context independence when there are ant colony foraging strategies that work in the desert and they work not as well in the jungle.
So just like it is with our attention, there's attention surroundings that support this kind of work, but not that kind of work or well being.
So being able to talk about the generative model and the generative process and their engagements in a rich way, I guess it's what brings us together.
But it's also what feels like a powerful place to regather and remember a lot of the important qualitative threads and empirical threads in this important clinical area and also move forward in a way that's not just adding like another measurement onto the pile.

1:24:01 Because a lot of these models, as you continue to develop their formality and ambiguity to integrate data, they will provide a new view on previous findings and patterns that may have been taken in the Ttest reward learning world to be conclusive, or this or that will be shown to be just two darts thrown into a huge neurodiversity space.
And there might be other studies or sets of studies where what was treated as being all over the place are now perfectly in line and tell a really coherent story about, for example, how strong negative beliefs about the self and others or high uncertainty of beliefs about the consequences of action end up helping us just do what we do.

1:24:58 _Max:_

Yes, totally agree.
Maybe it's interesting there's even reconceptualization going on, like thinking about psychopathology in more like evolutionary terms, like Stefan Hoffman, for example, and Stephen Hayes.
Stephen Hayes is known as the founding father of Acts.

1:25:20 So acceptance and commitment based therapy.
And those two guys have a new therapy idea where we describe psychopathology on a pragmatic basis.
So we define psychopathology as behavior that doesn't fit any more the current circumstances.
So there you have the context and right.
And I think it's clever to do it more that way because, for example, PTSD like behavior, well, if you're a soldier in a really bad region of the world, this is not psychopathology.

1:25:56 This is allowing you to survive.
The problem is of PTSD, that the war comes home with you or dramatically bend comes home with you, and now your behavior doesn't fit the environment anymore.
Right.
And I think this is a neat way of describing a lot of psychopathology as maladaptive behavior in the evolutionary sense.
And typically it was adaptive in the past.

1:26:24 Like, also, what this, like, borderline personality disorder slide that I have on the screen right now is the same because it was adaptive in the past to behave like this in some circumstances, in a bare childhood, so to say, but it's not anymore, but it's continued despite being ineffective.
And I guess this is a good definition for a lot of psychopathology.
Not for all, I would say.
For example, there is really psychopathology where you have broken inference, so to say, and not just for example in psychosis.
In some cases I would say yes, you have more like brain pathology, you have more really broken inference, and the rules of active inference don't work anymore, so to say.

1:27:14 But I don't think that the rules.
Active inference lab don't work in rumination.
They work perfectly fine, but the organism has placed himself in a situation where they don't learn anything new by applying the same rules that everybody else applies.
So it's broken models, not broken inference.
And I guess this is true for a lot of psychopathology.

1:27:45 _Daniel:_

So what are your next moves with this line of research?
You mentioned some of the papers.
What would you like those papers to show?
Or who would you like them to speak to?
And show what?

1:28:02 _Max:_

Maybe I start with the literature review that we are planning.
I would like to get to know what the literature, so to say, says about active inference informed treatments.
This is what I would like to find out.
I don't have a lot of hypotheses.
I want to screen the literature and find out whether we can synthesize them into an active inference informed model of what is psychotherapy doing.

1:28:31 And I would like to speak this model to a clinical audience in the first place.
Again, so I want the clinical population to learn more about active inference.
I know that psychiatrists sometimes know about active inference literature, but psychologists, at least not clinical psychologists, typically don't know a lot about it.
And I would like to change this a little bit at least.
And afterwards the next logical step would be to implement some of the insight into actual therapy programs.

1:29:05 But this is something for more of the future.
But it would be interesting whether you can really have something like an active inference informed therapy, but now we are talking more like five to ten years.

1:29:17 _Daniel:_

Awesome.
Do you have any final thoughts or questions?
And then I will close with a short quote to fire back.

1:29:26 _Max:_

Yes, you are.
No, I don't have any final remarks or questions.
I would like to thank you for giving me the opportunity to speak and now I want to resolve my uncertainty regarding the quote.
Great.

1:29:40 _Daniel:_

The quote is from Henry David Thoreau and it's drawing a connection between the paths that we ruminate on, that we walk upon and travel upon, and then the paths in the mind.

1:29:54 So I thought it was Africa, so throw a rope.
I had not lived there a week before.
My feet wore a path from my door to the pond side and though it is five or six years since I trot it.
It is still quite distinct.
It is true, I fear, that others may have fallen into it and so helped to keep it open.

1:30:12 The surface of the earth is soft and impressive by the feet of men.
And so with the paths which the mind travels how worn and dusty then must be the highways of the world.
How deep the ruts of tradition and conformity.

1:30:28 _Max:_

Thank you.
Awesome.

1:30:31 And thank you for having me.

1:30:33 _Daniel:_

Till next time.
Thanks a lot.

1:30:35 _Max:_

See you.
Bye.
