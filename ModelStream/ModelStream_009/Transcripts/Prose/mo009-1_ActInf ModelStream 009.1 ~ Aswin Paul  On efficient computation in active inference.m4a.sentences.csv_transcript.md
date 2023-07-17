
00:07 _Daniel:_
Hello and welcome, everyone.
It's July 15, 2023.
We're here in active inference model stream number 9.1 with Aswin Paul.
Today we're going to have a presentation and a discussion on efficient computation in active inference.
So if you're watching along live, please feel free to add comments or questions in the chat.
Otherwise, Aswin, thanks so much for joining today.
Really looking forward to your talk.

00:38 _Aswin:_
Thank you, Daniel.
Thank you so much.
So, as mentioned today, I'm here to talk about efficient computation and active inference.
And yeah, let's get started.
So we are all familiar with this idea of the free energy principle, which is also known as active inference, right?
So the central concept is that an agent minimizes entropy of its observation to maintain homeostasis or survive in its environment.
And here the entropy is defined in the information theoretic sense, right?
So if an observation is highly probabilistic, that is less entropic or less surprising because it was high probability and we were expecting it, that's the idea, then that's the base that we build this framework of active inference on.
And this idea of Marco blanket, it gives us a systematic way of surprising or systematic way of separating an agent from its environment and model purposeful behavior.
Right?
So let's focus on this idea of minimizing entropy.
So how does an agent minimize entropy or know which observation is highly probabilistic and vice versa?
So that is by maintaining a generative model.
And the generative model is basically a toy model of the environment which the agent builds in its brain and that is built using only the observation that it gets from the environment.
So it has no access to the real states or the hidden states of the environment.
It's building the toy model.
And given this toy model, it has scope or ability to compute the probability of an observation and hence try to minimize the entropy.
Right?
So that's the idea.
But it has a problem of cursive dimensionality.
Like, given a generative model, it may not be possible always to calculate or marginalize the probability of observations out of it because the state space can quickly become intractable.
But the idea is that you define an upper bound on the surprise using Jensen's inequality.
And you may also define a new term called Q, which is the hidden belief or the belief about the hidden states.
And this Q is going to be the focus of decision making, right?
So if you have a noisy queue and you have no idea what's in the environment, then you can't make or hope to make decisions to control that environment.
And it is this belief about the hidden states that you use and that becomes useful to take decisions.
And this whole quantity is of course called the free energy.
And the variational free energy F can be interpreted in multiple ways.
So the first or the most common is the machine learning way of how it is trying to minimize the complexity of the model at the same time trying to maximize the accuracy of it.
So that's the machine learning interpretation of minimizing various free energy.
You may also try to interpret free energy in the physics term where you at the same time try to minimize the energy of your model, but at the same time trying to maximize the entropy.
But the focus of today or decision making is always on this belief that you have after you do the perception in active inference.
So how do you do vanilla decision making?
Or what is the most discussed idea of decision making in classical active inference?
So, if you are in an environment and if you're an agent who's trying to make decisions, then you have a space of available actions, right?
So in this toy model, you have three available actions run, jump or stay.
And given these actions, you can hope to define a policy pi, small pi, which is a sequence of actions in time and capital T is the time horizon of planning.
Or that's the length of your policy.
And you have a policy space with many such policies, small pi.
So given this bigger small C space, you can attempt to evaluate the expected free energy based on the beliefs that you accumulated.
So here you are not minimizing anything.
You already have a belief from variation free energy and you are just calculating or evaluating the expected free energy corresponding to many small policies that you can define.
And after you evaluate it for all policies, then you know which is the optimal policy to take.
And that's the classical active inference idea of decision making, right?
And this expected free energy is really useful in the sense that it is goal directed.
So the risk term is goal directed and then you have this expected ambiguity term that forces you to explore as well.
But there is a problem that this policy space can quickly turn interactable and that has always stayed as a bottleneck in scaling active inference to commonly seen environments.
But let's see how it becomes quickly intractable.
So how many policies can be defined, say, for a time horizon of 15, right?
So if you are playing, say, supermago, you might want to plan at least say, ten times steps ahead.
So the first policy could be the same action run, stacked for 15 timesteps and you can basically define several combinations of such actions.
And the policy space is simply intractable.
It becomes too huge for you to evaluate the expected free energy for all such policies.
And in a stochastic problem setting where the environment itself is noisy, you don't really have a method to choose a subset of this policy space and do classical active inference.
And this is clearly a computational intractable problem.
And that's why in literature we always see small grids or small environments when you discuss decision making in active inference.
But recently, a new idea was proposed, which is called the sophisticated inference.
And in sophisticated inference, it is not really the policy space.
You are actually real time trying to think what to do.
So if you have a belief, then you are trying to evaluate the actions based on that.
So here we don't have a sequence of policies or things that becomes intractable.
Here we are doing basically tree search in the sense that you are trying to evaluate expected free energy of this joint distribution of actions and observations and to evaluate the expected free energy at some time small T, you will also need the expected free energy at the next time step.
And to evaluate that, you will need the expected free energy of time T plus two.
And this basically becomes a tree search that rolls out in time and it's a recursive relation.
And here it's fundamentally different from the policy space that we saw in the last slide, right?
And is it computationally better in the sense that if you have to plan, say, ten times steps ahead?
Comprehensively?
In classical active inference, we saw that the policy spaces, the cardinality of the action space raised to t, so that is the computational bottleneck.
If you have to consider all possibilities.
But in sophisticated inference, it's even worse, because you are considering combination of state and actions.
So it is computationally worse in fact.
But a solution was proposed in the sophisticated inference paper that we can do pruning of this research, that we can avoid some states and actions when you do this research and that becomes computationally very tractable.
So let's see how pruning works in sophisticated inference.
So this grid was discussed in the original sophisticated inference paper and say, for this grid, given that you have this kind of prior preference distribution, so this white square, which is the gold state, is the most preferred state.
And you have a uniformly decreasing preference for states that is far away from that goal state, then basically if you observe yourself at some observation at Time T, then basically what you're doing is you're considering the consequence of available actions from that observations.
And basically you can use the projection of your belief and set a threshold for those beliefs to kind of maybe ignore some actions and ignore some observations.
And what you will find is that it's no longer a tree search, it's a subset of tree search and it's computationally way efficient than doing the whole tree search, right?
So here you have avoided a lot of combinations and this becomes a computationally tractable problem.
This is because you have decided to avoid some actions and observations.
So you are essentially compromising on that possibilities which might give you a higher reward or which might be more optimal than the consequence of this partial research.
But this works.
So this simulation was presented in the paper and it works.
The agent kind of learns to do what needs to be done if it plans in this forward direction of planning in a pruned way.
And basically you can computationally show that even for a small search threshold, you can drastically decrease the computational complexity.
So if you decide to do the whole research with the planning depth, the computational time is exponential and quickly you can't do much about it.
But if you decide a search threshold which is even very small, you can see that this problem becomes computationally attractable.
And this demo on sophisticated inferences available in my version of PMDP and it's going to be integrated to the original PMDP soon.
But the key point is that the pruning of the tree search requires us a well informed prior preference like this in the sense that here the agent is aware of how desirable are neighboring states, it not only knows about the final goal state, it also knows about its neighboring state.
And given such a prior preference, we can see that for a planning depth of three, the agent is getting stuck basically in this local maxima of prior preference.
But with sufficient planning depth it is able to overcome this barrier and reach the goal state in in this great problem.
And the question is that what if the agent only knows this final state?
It has no other knowledge about what to do.
And in this case, what does the agent do?
So this is the problem that we are trying to address and in the absence of a meaningful trip reference like this, the agent has basically no way of reaching the goal state other than by random exploration.
It has no way of planning because it cannot do planning eight times steps ahead, because it's computationally intractable.
If it chooses to do the full tree search, right?
For a grid like this, what do you do if you get a sparse trip reference which is not well informed and as highlighted in the previous slide, your research is now blind, you have no way of pruning the tree search, and you have to do the full tree search in this scenario.
So, as you might have thought, there are two solutions to this.
Either you have to find out a way to do the full depth planning with this past prior preference or you have to learn a meaningful prior preference which will enable you to do this pruned research.
So we are going to discuss these two solutions in this presentation for a given scenario like this.
So, the first solution to do full research is basically using dynamic programming.
And dynamic programming is a well known idea in operation research and industrial engineering and many branches of engineering.
And the basic idea is that you solve the subparts of a bigger problem first and then later try to integrate the solutions of these sub problems to do optimal decision making.
So in this scenario, imagine that you're trying to plan for the last action.
So earlier we started from the first action, we started from the present and tried to predict what is happening in the future.
So your direction of planning was basically forward in time.
But imagine that you are trying to plan only for the last time step where you are just near the goal state and right going to that goal state.
Right.
So you are trying to make a decision for that last time step, which is capital T minus one, and your projections to the next time step or the last goal state can be done because you have access to this model of the world using this transient dynamics or the B matrix in active inference.
So for this single time step, which is a sub problem, you are actually evaluating a table of expected free energy that tells you if you are in, say, this observation, what is to be done, which is for the last time step.
And basically you can do this in state space or observation space.
So this can be done using the A matrix and B matrix together, where you can do planning either way.
Right.
So the question is that if you know what to do in the last time steps, that you might be thinking, how do I know that I'm in the last time step?
It is all about imagining.

15:09 _Daniel:_
Sorry, last thing we heard for a second was it's all about imagining.

15:15 _Aswin:_
Yeah.

15:16 _Daniel:_
So just pick up from there.
It's all about imagining.

15:19 _Aswin:_
Okay, so there was a connection issue.

15:22 _Daniel:_
Yeah, just for a few seconds.
It's all good then now.

15:25 _Aswin:_
Oh, sorry about that.
So what I'm trying to say is that you are trying to imagine what you will do if you are in time capital T minus one, which is the last time step for your planning horizon.
And if you are in that time step, what do I do?
So this table represents all such scenarios that if I am, say, at observation three, at time T minus one, what do I do?
And this quantity here, I'm only considering the risk term or the purposeful term, and this term represents that policy.
And what if I do this backwards till time T minus one?
So if I know what to do at time capital T minus one, then this table can inform what to do at capital T minus two.
So rather than planning forward in time, what I'm doing is basically stacking many tables together just by fixing a capital T of planning.
And given that I have all such stacked tables, then basically what I can do is use them to take decisions forward in time.
And what we have observed is that this idea works, that I can calculate the expected free energy backwards step by step, considering them as sub problems.
And the fundamental difference is that in sophisticated inference to calculate the expected free energy at time small T, you don't know what is the expected free energy at time T plus one.
So this becomes a research so that you have to calculate this first and to calculate for T plus one you need t plus two and so on.
But here because you're calculating it backwards in time.
You already know what is the expected free energy for T plus one.
And it's basically the same equation.
It's just that you're doing it backwards in time and pictorially in sophisticated inference.
You are trying to do a tree search.
But in the dynamic programming algorithm, you are doing your planning backwards, using tables.
And given your planning horizon is sufficient enough for a problem, what we have seen is that the agent will be able to take optimal actions forward in time.
So in the paper we are also proposing one algorithm for sequential palm DPS using this backward planning in time and we were able to scale up simulations for grid spaces which was previously intractable without neural networks.
So that was the first solution.
So the second solution is that so in the first solution it was fixed that you only get a sparse prior preference, you don't get any other information, you only get your information about the final goal state and all you get is the model of the environment which you learn and you basically have to take decisions.
But the second solution of course is that if you're allowed, you can attempt to learn a pride preference which is meaningful like the one we saw in the previous slides, which has the information about the other states also.
But how do you learn it?
Right?
So there is a seminal work from optimal control literature that talks about efficient computation of optimal actions and in that work there is a quantity similar to our prior preference which is called the Desirability function.
So for example, in this grid world here darker colors are more preferred.
So if this crosses your final gold state, what the agent in this paper is trying to do or the said learning method in this paper is trying to do, is learn this Desirability function as optimally as possible.
And what has been shown in this paper is that if you try to learn the Desirability function using a particular learning rule, it is computationally far more efficient than even Q learning which is a well known reinforcement learning algorithm.
So Q learning is a well known computationally optimal algorithm but in this paper that particular learning rule for learning this kind of a Desirability function is way faster and this approximate error represents how different it is from the optimal Desirability function.
So this Desirability function is nothing but our prior preference and as mentioned learning set is borders of magnitude efficient than learning the Q function in Q learning.
So this is the particular learning rule depending upon the reward that it gets from the environment and in this particular grid world environment we are only giving it reward at the last step which is similar to the sparse parent preference, the agent basically gets no reward until it reaches that final goal state.
And with this learning rule which has a parameter ETA that controls how fast or slow this learning happens.
So basically we tried to study the effect of this learning parameter ETA, but what we observed is that it's very robust, it can learn the prior preference reliably even with variable values of this learning parameter.
And what we see is that the agent is able to learn a meaningful prior preference over time very fast and using such a meaningful prior preference, then the agent don't have to plan a lot, it can manage optimal behavior or purposeful behavior with very low time horizons of planning.
And given these two solutions, we could scale up active inference algorithm for decision making and talking about the computational efficiency, we saw that the dynamic programming method could plan 30 timesteps into the future with only say a computational complexity of thousand when compared to say ten to the power 68 for sophisticated inference.
And the second method which learns the prior preference which we call active inference and it only needs to plan one time step ahead, so it is way more computationally efficient in that sense, but it has to learn.
So in the Dpsv method we are not learning, we are using the sparse sprite preference and doing the whole depth of planning and in the other method we are letting the agent learn this prior preference but then we can save planning a lot because it knows a lot of what to do in time, right?
So graphically we can see that the Dpfe method is really computationally efficient and when plotted against time in the AI t equal to one method, it is basically computationally way cheaper.
So it scales very fascinatingly well with higher and higher complexity of the environment.
So we tested these methods in very huge state spaces like say 900 states compared to state spaces which has dimension of say five or ten in the usually seen active inference literature.
So I want to kind of emphasize that we are not using any neural networks here, we are using explainable active inference agents doing all necessary matrix multiplication so that we have access and explainability to every computation that is taking place in these algorithms.
And when tested on these grids first, we validated this on a smaller grid with hundred states.
And we observed is that when compared to benchmark reinforcement learning algorithms like Q learning and Dynaq, dynaq is a model based reinforcement learning algorithm.
And we compared our newly proposed agents, which is Dpfe and AIF, and we saw really good performance and AIF agent is slightly worse.
And that's because it's only planning one time step ahead, right?
But the Dpfe agent who does full time planning, it's performing as good as benchmark reinforcement learning algorithms.
And we tested it with bigger and bigger grids.
And when we introduced Stochasticity in the goal state, in the sense that when the agent had to navigate to Stochastic goal state.
So we changed the goal states at every ten episodes.
And what we observed is that the Dynaq took more time than our Dpfe agent to kind of recover and do well.
So Dpfe agent in this Stochastic environment performed really well, even better than the Dynaq agent, and we could also see that the AIF agent is recovering faster but not as good as the other agents.
So basically that was the result in the paper and the methods.
So, yeah, thank you for listening, and I'm open for discussions.

24:32 _Daniel:_
All right.
Awesome.
Wow.
Very cool.

24:38 _Aswin:_
Thank you.

24:39 _Daniel:_
Okay, well, just as we start the discussion, if anyone wants to add anything first, just how did you come to work on this project?
Were you studying active inference and you came to this question as being interesting, or were you working on the planning and came to active inference as a method?

25:02 _Aswin:_
Yeah, so little bit background about myself.
So I studied physics both in my undergrad and postgrad, and towards the end of my post graduation, I got interested in things like game theory and reinforcement learning, and I joined for a joint PhD with Professor Adela and Professor Manoj.
And so Professor Manoj is a control theory person, and Adela is a neuroscientist.
And in the beginning of my PhD, I started reading active inference literature, and I wanted to implement that in problems.
And I was always fascinated with explainable active inference about this idea of expected free energy, trying to minimize risk as well as expected ambiguity.
Just so not just making the agents work, but also being able to tell how they work is what fascinated me in active inference.
And initially, I tried to implement them, and there is a conference paper which we published in which we compared it for a similar grid world task.
And then I faced this problem of scaling active inference, and then I started working on sophisticated inference.
Yeah, so basically these methods came out of the need that I wanted to scale the map up.
And I always had was skeptical in using deep active inference because I didn't want to use neural networks to do planning, because deep reinforcement learning in itself is a huge field.
And if you're about just scaling active inference, then maybe just do deep reinforcement learning.
That's what I thought.
Yeah.
So that's basically the background, and that's how it came about.

26:48 _Daniel:_
All right, I'll go first to a question in the live chat, and we'll just probably discuss various aspects because there was a lot in your presentation.
So ML.
Don writes, I wonder, when it comes to computing the expected free energy over a time horizon, what kind of mean field approximation was used to factorize Q of S?

27:13 _Aswin:_
Sure.
So I assume that the question is about the expected free energy in Dpfe, and to calculate this, basically.
So in my simulations, I use belief propagation for this belief cube and you can also use variation message passing or marginal message passing.
That's not a problem.
Once you have this belief queue, what do you do?
Right?
Yeah.
So when I say you imagine Q for a time, then what I use mostly is one hot vector.
So to take decisions, you use the belief that you get out of your perception step in active inference.
But for imagining, these are hard tables where they are one hot vector.
So given, say, in your generative model has ten states.
The queues that you use are precise queues for planning.
But for decision making you use the imprecise mean field approximation queue that you get from the perception step.
So I don't know if that answers the question, but maybe I also need to think about more about the approximation that may be there in steps.

28:50 _Daniel:_
Cool.
Yeah, they can write more if they want.
Let's talk a little bit more generally about preference learning.
So in the context of the active inference generative model, we have a mediating between observations and hidden states and learning makes a lot of sense.
It's about learning the mapping between observations and hidden states of the world.
And then we have B learning, learning the consequences of action and how things change through time.
And preference learning is learning on C.
And you've highlighted that this is a very interesting variable to learn.
And I'm curious, how do we learn to learn the right thing?
How do we know that we're learning in adaptive preference?
And then how does that preference learning reduce cognitive overhead or computational complexity?

29:50 _Aswin:_
Yeah, great.
So if you are trying to learn a prior preference, then that assumes that there is something to chase or there is something to maximize, like a reward.
So in a reinforcement learning setting, there is clear reward that's coming from the environment that you're trying to maximize.
And say for this grid, you get that reward only in the last step.
That's what makes this problem hard.
So if you are getting rewards at every time step, then basically you know what to do that I just have to pursue that reward at every time step.
Right?
But here you might have to take say, 15 time steps ahead to get that one reward and that basically is hard to do.
So here, because I'm trying to learn a prior preference, there should be a reward structure that exists in the environment.
If the environment doesn't care about what I do or if I can't define what is good or bad, then there is no meaning in learning the prior preference.
Right?
So here the reward is what controls the learning of this prior preference.
And the good thing is that even if only I get the reward at the last time step, I have my B matrix and I have experience of transitioning from different states, which I reached this final goal state.
And this algorithm that we are using, or the learning rule that we are using, is precisely learning a similar thing in optimal control.
That paper I introduced which is called the desirability function.
And given that you have this desirability function so imagine that maybe I'm starting from this state, then I just have to look at my nearest neighbors to take a decision.
If the state at state below the state is more preferred, then I only have to plan one times ahead and that's the optimal decision I have to take.
So learning this prior preference reduces the cognitive load in the sense that I'm only now looking at nearest neighbors, I don't have to plan all the way up to this final goal state.
And I will learn this as efficiently as possible because one, it is a guaranteed algorithm, we tested its robustness and it is also informed by the reward that I get from the environment.
If there is some way to kind of define what is preferred then you are guaranteed to learn a pride preference that's meaningful by this algorithm.

32:28 _Daniel:_
So if only nearest neighbors and one time step inference is being used, then what prevents this kind of preference learning agent from being stuck in a local optima?

32:43 _Aswin:_
Yeah, so there won't be local optimas here.
That's the point.
Why would there be a local optima if I am learning it using rewards?
Yeah.
So if there is local optima, then it will be getting stuck in the local optima.
But there won't be one if you're learning us this way because you're learning it from your own experience and how you got the reward at time sometime.
And what we observed is that it's very gradual and there is no glitches or local optimus when you learn such a practical.

33:23 _Daniel:_
So it's kind of backfilling a preference so that there can be a smooth path to the distal goal.

33:36 _Aswin:_
Yes.
So the animation kind of makes it look like a backfilling but you're actually learning it from your experience forward in time.
Right.
So I observed a reward when I transition from this state to this state.
So this must be good.
Then in the next time step I say, okay, this state is responsible for taking me there.
So this might be good also, but not as good as the other one.
So it looks like it's learning backwards, but it's actually learning from the real t to T plus one experience.

34:13 _Daniel:_
Okay.

34:15 _Aswin:_
So in that way you can't have local maximas because this is the learning rule that does that.
I don't know how to answer it more systematically.

34:28 _Daniel:_
Yeah.
What real world situations or what real life situations do you kind of see this kind of preference learning happening in?

34:39 _Aswin:_
Yeah, great question.
So, so there is one paper that came out from our lab where neurons are laying learning the game of poem.
So it's a paper is called Dish Brain and the device is called Dish.
Brain.
And what they have accomplished is that they managed to culture neurons on a silicon chip and they gave it a good feedback signal when it successfully tackled the ball or played the game well and gave it a shock when it made mistakes.
And what we saw is that in the paper, what we see is that it learns to play the game over time.
Right.
And in such a scenario, imagine that if I encounter, say, a positive thing in the world, then I might associate what is good with the states I observed in the past and so on.
Right.
So I learned step by step what is good or bad, and that's a reasonable hypothesis to make.
So if I want to say, get fitter, then I might associate going to gym as a good thing.
Then I might also associate walking to the gym as a good thing.
Then I might associate, say, wearing my shoes as a good thing.
So learning prior preference that way makes sense, I would say.
But yeah, this is a computational solution to the problem of cursive dimensionality.
But testing this on the real world is definitely what we should do.
And yeah, I also look forward to doing that.

36:25 _Daniel:_
Okay, let me try to run a real world situation by you and see if this connects.
So we're rewarded by turning in an essay that gets a high grade.
And so there's many steps between starting the idea of the essay and seeing that preferred sparse outcome, which is the grade, and we do all kinds of things, and then we learn, okay, well, this one where I did get a good grade, it was well formatted.
And then now you sort of expand the umbrella of your preference out, and then you go, well, what brought me to getting it well formatted?
Well, I did it on time.
And then you kind of work all the way to the ideation phase so that in the future you can do one step inference exactly.
And just take it step by step as a skill, instead of needing to do a 15 time step inference over all the possible tree structures.
So you've kind of used your embodied learnings to simplify the structure of the problem.

37:40 _Aswin:_
Exactly, yeah.

37:43 _Daniel:_
And can we look at the computational complexities again of all them?

37:51 _Aswin:_
So here, CIF stands for the classical active inference.
And to do the full horizon of planning, it's around ten to the Power 18.
So this is for this particular grid example with hundred states and four available actions.
So this is for a special case, and I just wanted to put numbers to put things in perspective.
So for this particular example, if you are trying to do it with the policy space thing, you will have to do ten to the Power 18 computations for one step of planning or in one instance, in sophisticated inference, it's even worse because the state space also matters.
And that won't work.
So this third line was supposed to kind of show that even for a time horizon of two, it's really hard to do sophisticated inference if you have to do the full planning.
But with dynamic programming, when you're planning backwards, you can attempt to do the full horizon of planning and that's only 1000 computations.
But with learning prior preference, it's even low when you do it just one time step ahead.

39:04 _Daniel:_
Wow, this is quite stark.
And in the branching time active inference work.
In a previous model stream, we also saw some computational complexity estimates.
But I think these are really clear.
First thing it made me think of is no one said sophistication was cheap.
I mean, it's astronomical how costly it is for maybe even only at two or three or four or five potentially starting to get up to so it's increasing the complexity of planning radically.
So it's very interesting pedagogically as we think about like, as we imagine active inference, intelligence architectures, but this makes it pretty clear that it's not something that you can just enumerate over.
And so I think it's very creative and important what you've done by connecting this to principled methods of computational complexity reduction rather than potentially effective but ad hoc methods of complexity reduction, like neural networks, which might work when they work, but then once those start to get bloated, now you have no principles and no efficacy.

40:40 _Aswin:_
Exactly, yeah.
And sophisticated inference, I must note, that has its own benefits when compared to dynamic programming, in the sense that when you're planning forward, you are taking into consideration all the possibilities.
Right.
But when you're planning backwards, say, for example, like queue based exploration, like if you have to go somewhere, get a queue and then navigate to the goal state, then planning backwards might not work.
So this was one feedback I got when I discussed the work with some people.
So that's a thing to note about dynamic programming.
But the other place where you learn prior preference, I believe it's not a problem, but yeah, dynamic programming is computationally cheap, but it also come with its own limitations, I must note.

41:26 _Daniel:_
There, just to restate, that in dynamic programming, with a bellman optimality, we're solving backwards.
And so it's kind of like the checkmate is what we want and so now we're working backwards to the present, but we end up not exploring counterfactual endpoints.
We don't work back to the present to endpoints that we're not interested in.

41:53 _Aswin:_
Exactly.

41:53 _Daniel:_
So that's why it's so ruthless.
But on the other hand, it's a much more constrained search.

42:03 _Aswin:_
Yes.
So what I'm thinking about these cases that we should also consider combinations of these two where I can afford to kind of ignore such counterfactual things.
There I can do dynamic programming and maybe I can do as two steps of planning.
So if it's a queue based exploration, say reaching Q is one task and from Q to the reward is the other task.
So I can separate these two and use dynamic programming for them and that's computationally cheaper, but also kind of preserves this idea of having to do it.
Yeah, but these are all future things I am thinking about.
Cool.

42:48 _Daniel:_
I'll ask another question from the chat Alex wrote.
Do you have ideas or developments on nested models where different scales could have different one time step ahead and speed of execution?
So how does this model play out in nested models?
And how do we think about this forwards and backwards in time in the speed of execution and nested models?

43:19 _Aswin:_
Okay, so I might need a little more context here.
Like when you say nested models, do you mean hierarchical models?

43:27 _Daniel:_
Yeah.

43:28 _Aswin:_
So maybe something like there is an observation.
I get on a fast pace and I do some inference on that, but then I use this inference to kind of do and basically this inference becomes the observation for the next state.
That's what nested models mean, right?
Yes.
So I might have to actually think about that in terms of a task and then think about it.
But honestly, I haven't thought how this might work in that context, but say, for a task.
So in terms of navigation, if you think about it, you can think about, say, rooms environment.
So that's one of the examples I can think about where you can apply this.
So imagine maybe you have a collection of rooms and as an agent, you have to first figure out which room to go and then you have to navigate inside that room.
And basically you can do inference in two stages or decision making in two stages.
And you will have to separate your decisions in those stages inside the room.
You can do, say, dynamic programming to navigate your optimal path, but you will always have to kind of have two stages of decision making and maybe different methods work better at different stages.
But this would be better, this discussion would be better to better in a well thought out task, I would say.
I don't have an answer that might be fitting for everything.

45:18 _Daniel:_
But yeah, we've seen almost exactly that kind of hierarchical simultaneous localization and mapping slam in a robotics case.
There have been active inference models on that.
Would it be possible to sort of do one of these methods at one level of the nested model and then have another computational method applied to another?
Or if you wanted the advantages of one in one place, can you mix and match with these different methods even within one simulation?

46:00 _Aswin:_
Yeah, I definitely think that's possible, but we'll have to maybe try.
So all my methods are one stage.
It's not a hierarchical model, but I strongly believe that it would also work in an estate model where you can have two methods of decision making working together in, say, for a room example.
I just mentioned.
Cool.

46:27 _Daniel:_
Could you go to the slide on Z learning?

46:32 _Aswin:_
Yeah.

46:35 _Daniel:_
Cool.
Yeah.
So I noticed here and in the great paper that you had several totorov citations.
Yes.
And this introduction of the Z learning is a novelty with respect to the active inference field.
So could you explain a little more what is the Z and what is it that enables such a rapid improvement in the Z with respect to the Q?

47:07 _Aswin:_
Yeah.
Okay.
So to give some context about this paper, it talks about a linear method of decision making in a particular class of MDP.
So given that you are having a markout decision process where your actions can be based on states and not actions.
So when you think about actions in a, say in, for example, a grid world task, you think about left right and north south right?
So if I take a north, then that has a consequence on state space.
But in this paper, they're introducing a class of MDP where decision is itself in terms of states.
So if I am, say, in state s one, my decision will be depending upon the other states.
So my decision will be based on the other states I want to be in the next time step.
So it's a redefinition of decision making in terms of the state space rather than decisions being something else like left right and down up.
So given that such an MDP exists where I can take decisions in terms of states, they have showed that computationally you can take decisions in linear complexity, however big the problem is.
So for that to enable decision making in terms of states, you should have a sense of what is good and bad for the states.
So in this grid word example, you have a desirability function which is C.
So C is the desirability function which talks about how desirable is this tip?
And if I have a C function, then what they have showed is that I can take decisions with linear computational complexity for this particular class of MDP.
So if my MDP allows me to take decisions in terms of states, it's only linear complexity for that thing.
So this graph is basically comparing how you can learn desirability better or faster, right?
So Q learning, if you're familiar with Q learning, it's basically a table based method where you have desirability of actions given a state.
So given a state, you know what to do.
That's basically the Q matrix.
But in terms of C or the C learning method, it's only about states.
You're only learning how desirable a state is.
There is no concept of action states.
And this is exactly what our prior preference is in active inference, where it is a distribution that quantifies how desirable or non desirable states are.
So given that they have shown that you can learn the C matrix faster and that's optimal and it's way faster than even Q learning, then I thought, okay, why not try to learn C the same way as C is learned in this paper and using this.
So there is a similar learning rule for learning C, which is called set learning in that paper.
And when I attempted to learn C, what I've seen is that it learns really fast a useful prior preference that lets me take decisions or let the active inference agent take decisions only by say, one time step of planning.
So basically that's a story.
This idea of C being easily learnable is in that paper, the Tarot paper.

50:52 _Daniel:_
Okay, let me try to restate that since I think it's a very interesting augmentation of active inference.
So we're going to be learning C for all the reasons we discussed earlier.
We're going to learn C analogously to how Todorov presented Z learning.
And in the Z learning, instead of learning, for example, updated posterior probabilities on actions and then using actions to navigate amongst states that emit observations, we're going to kind of bake the action into the states.
So that really we're learning transitions amongst states directly.
And to connect this to the free energy principle and how it is playing out with active inference here, C is not just our desirability function, that's one way of thinking about it.
That's why we call it preference.
But also C is our expectation.
And so that is what allows us to, on one hand use the language familiar to reward and preference learning.
Like the agent is ending up where it likes to be, but also the expectation based definition of C.
These are the same thing allows us to talk about that as a path of least action or as the most likely outcome or the least surprising outcome.
And because we've defined it what we want as the least surprising outcome, then we can use variational free energy to bound surprise, whereas you can't use simply a variational method to bound or even necessarily approximate reward itself.
But if you say I prefer what I expect and what I expect reduces my surprise and I'm going to bounce surprise, then you get both that sort of behavioral reward seeking couched in a surprise bounding surprise minimizing physics framework.

53:27 _Aswin:_
Yeah, that's a beautiful way of saying it.
Yeah.
Thank you.

53:31 _Daniel:_
Well, what are your next exciting steps or directions or what ways do you want to take this work?

53:40 _Aswin:_
Yeah, great.
So if you are talking about only this work, what I want to do next is think about queue based exploration tasks.
First of all, address the limitations of dynamic programming.
So if you have, say, a queue to explore in this grid first and that's more optimal, I want to see how the expected ambiguity term in the expected free energy is useful and should be made use in the dynamic programming strictly in that sense.
But more generally, I'm also looking at other ways of making decisions in active instance.
Like there are works from professor Isamura from CBS Reckon, he talks about how neural networks are doing active inference and basically decision making there is really more efficient in the sense that it's like Q learning.
So there he's making clever use of the variation free energy to learn good state action mappings and it's a very drastic change to what we are used to in terms of expected free energy.
So there is no concept of expected free energy in that work.
It's all about learning what is good and bad directly from variation of free energy.
So I find that also fascinating.
I want to kind of explore that more and see how decision making in this way is better or worse or should be thought about.
Should we even reconsider ways of decision making?
Because active inference only talks about variation of free energy and that's the central tenet.
Everything else is your interpretation of that.
Right, that's another direction I want to work.

55:35 _Daniel:_
Interesting way to say it.
Definitely the variational free energy, which is a functional of our variational distribution Q and the data y, the variational free energy is kind of like the real time homeostasis, like how are things making sense given what I believe and the incoming data.
And then to extend that kind of a sense making framework into decision making, we've seen a lot of different methods.
Expected free energy is a common one, but for example, there's been free energy of the expected future and there's other constructions that have different methods.
And then you pointed also to Professor Samura's work with the sort of relationship between the variational free energy on the base graph and the loss function in a neural network and all those relationships.
That's very exciting work too, I guess kind of in closing, just as a last question or thought, you're coming close to the end of your PhD.
So just in the time that you've been a PhD student, how have you seen active inference develop or what feels different to you today near the end than when you were fresh eyed and excited several years ago?

57:21 _Aswin:_
Yeah, that's a really great question and I am also very excited of how the field has evolved.
And frankly, I started from this reinforcement learning background and the physics background, and when I started reading, it was only, say, one or two papers and I did not quite understand much of it.
It was only when I started implementing it using Carl's MATLAB scripts, I kind of understood, okay, this makes sense and I like it.
But within, say, one or two years, I saw a lot of papers coming in from different directions and people also starting to use neural networks and all this scaling up came.
And at some point I also questioned the need of active inference because if you have deep reinforcement learning, which can do many things, and why deep active inference?
And that's the reason why I did not get into that.
But I still find it fascinating.
I want to kind of understand deep, active inference more than what I know now, but I've seen the field growing, like anything in two or three years, and many cohorts of people starting to work.
And in no time, it was a seriously taken field other than a field with, say, two papers with nobody actually knowing what it is.
So it's really exciting.
Yeah.
So I really look forward how the field evolves in time and also what I can do after my PhD and so on.

58:52 _Daniel:_
Cool.
Forward in time, backward in time, what we prefer, what we expect.

58:58 _Aswin:_
Yes.

59:02 _Daniel:_
Any other comments or anything else you want to add?

59:07 _Aswin:_
Yeah, so please let me know what you think about the paper and what you think about these ideas.
Feel free to let me know.
I really look forward to the feedback and yeah.
Thanks so much for this opportunity, Daniel, and thank you for your time.

59:23 _Daniel:_
It was amazing.
I hope people check out the paper and get in touch and replicate the code and take it their own direction.
Thank you.
See you next time.

59:34 _Aswin:_
See you next time.
Thank you so much.

59:36 _Daniel:_
Bye.

59:36 _Aswin:_
Have a good day.
Bye.
