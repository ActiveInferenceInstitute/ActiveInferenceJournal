00:01 _Daniel:_
And now welcome Aswin how are you doing?

00:07 _Aswin Paul:_
Hi, Daniel.
I'm good.

00:09 _Daniel:_
Hanging out, looking forward.

00:12 _Aswin:_
Can you hear me properly?

00:14 _Daniel:_
Yeah, sounds good.
And yes, looking forward to your workshop on sophisticated inference in pymdp.
So it can be up to 90 minutes or it's totally okay if it's less and we can take a short break, but please take it away and just let me know however I can help.

00:34 _Aswin:_
Great.
Thank you so much.
Maybe I'll share my screen and start.
So, regarding the structure of what we are doing here, I'm assuming that people who see this later might want to try it hands on along with the tutorial or something.
So that's the structure I kept in mind.
And so I'll go slow.
Please bear with me.
So welcome all of you to this session on sophisticated inference in pymdp.
So here we are going to attempt to model some sophisticated inference simulations, especially the one in the original paper using the pymdp module and how it is not part of pymdp right now.
But we are on the process of adding sophisticated inference to the pymtp module.
And I'm going to mainly talk about the code that I have developed to kind of add that functionality.
Right.
So I'm Ashwin Paul.
I am finally a PhD candidate at Monash University.
And mostly I work with active inference models and try to understand how to use them as an explainable model to basically understand emergence of intelligent behavior.
Right, so let's dive into the material right away.
So to give an intro of free energy principle, I'm sure all of you right now have an understanding of what it is.
But the central idea is that an agent is always trying to minimize the entropy of its observations, right?
So if an observation is having really low probability in your mind and that happens, then you are probably surprised and vice versa, right?
And the entropy here is defined as the information theoretic entropy, where if you have a low probability, then automatically this is a high surprise or a high entropic observation.
And as we all know, active inference also gives us a methodology to define what we call an agent environment loop.
And this lets us define what is the agent that we are looking at and what is the behavior of the agent given the environment around it and so on.
Right?
So you're also familiar with the idea of Marco Blanket.
And this is important because we always have to remember, I mean, have to remember the difference between the generative process and the generative model, which is quite a famous point of confusion in active inference literature and for the people who try to understand it in the beginning.
Right?
So the central question is that how does an agent minimize entropy?
Because how does an agent know which observation is low or high probabilistic?
Right?
So that is by maintaining a generative model.
And the generative model will tell you which is a high probabilistic observation and which is a low probabilistic observation.
So the idea is that all the agent has access to is an observation that is coming from a generative process which the agent cannot directly observe.
And an intelligent agent will try to build up a generative model in its mind, which is a model of the hidden states and the observation it has access to.
And it can hope to kind of compute probabilities using this generative model, right?
But there is a problem that in general it is an intractable problem to kind of marginalize the probability of observations from the generative model.
And that is why we have to define an upper bound on the surprise that the agent is trying to minimize.
And there comes the idea of free energy, right?
So this upper bound the agent is supposedly minimizing is the free energy.
And that's why it is the free energy principle.
And here we have a new term called capital QS, which can be interpreted as the belief that the agent is maintaining about the hidden state in its generative model.
And this quantity is the free energy.
And traditionally we see this variational free energy being interpreted as in mostly the machine learning way where it is a balance between complexity and accuracy of the model.
So when minimizing the free energy, the agent is trying to come up with a single model but at the same time an accurate model because here it's a minus sign with accuracy, right?
It can also be interpreted in the physics way where the agent is always trying to minimize the energy of the model but at the same time maximizing the entropy of the model which goes in conjunction with the maximum entropy principle and so on from the classic literature.
So, given that this idea of a generative model is so important in a software point of view, that's the first thing that you might want to do, right, to define a generative model for the agent which is informed or not informed depending upon the experiment that you're trying to model.
So in classical active inference, usually decision making is defined in terms of policies.
So, for example, if you are an agent in this environment so in the Mario game, Mario is the agent and everything else is the environment.
And Mario has three available actions run, jump or stay in this environment.
And the classic definition of policy is that it is a sequence of actions in time.
So if you have a time horizon of capital T, then a policy is nothing but a series of actions you might take.
So run, run, jump and so on in time.
So this is the SuperScript is the action.
So here it is jump, run and so on.
And the subscript is the time.
And then what you can have is a policy space, which is a collection of many such policies, small pi.
And what you essentially do to take decisions in active inference is compute, not optimize.
Compute the expected free energy of every policy in your policy space.
And basically, that can be interpreted as a balance between risk and ambiguity.
So when you compute this expected free energy, what you're trying to do is minimizing the risk.
That is, how different is your belief about the observation from your prior preferences?
Capital C.
So this is also part of the generative model when you're trying to model control and at the same time you are trying to minimize the ambiguity when you are choosing a policy that has the minimum expected free energy, right?
But this formulation has a problem that a policy space quickly becomes intractable, that there can be an enormous number of small pies or policies in your policy space and sitting and computing the expected free energy for all such policies even for a small time horizon, is not possible.
But this is the classical structure that has been implemented in Pymdp nonetheless, where we have different modules in Pymdp that is meant to be implementing different aspects of behavior.
So for example, for inference or perception we have belief propagation, fixed point iteration, marginal message passing and all that implemented in the inference module.
In the control module we have different methods to evaluate expected free energy for policies, one depending upon the expected utility, the other one depending upon the classic method that I just explained.
Then we have module for learning.
So we learn the parameters in the form DP like capital A, capital B, so likelihood transition dynamics and so on.
And then we have algorithms for implementing all this in the algorithms module.
And then the most powerful thing in Pymdp right now is the agent class where it is easy for you to kind of define the agent environment loop and we are trying to build up.
So today I'm going to talk about an agent class that implements sophisticated inference rather than the classical active inference that we just saw.
So, as I mentioned, how many valid policies can be defined, say for a time horizon of 15 in classical active inference?
Right?
So the first policy of course, is a series of first action that is jumped, then you can have the last action changed and you already can see that there can be n number of combinations.
And for this simple case, the policy space is as big as ten to the power 13.
And in a stochastic problem setting there is no way to kind of come up with a small subset of this policy space so that you can tackle this problem of computational complexity.
And yeah, as I mentioned, in a stochastic problem setting it is an intractable size policy space.
There comes the idea of sophisticated inference where we are thinking about taking decisions in a different way, right?
So rather than thinking about sequence of actions in time, we can directly think of what to do when we see something depending upon our beliefs about the current state and beliefs about the future, right?
So if I see myself in a current situation, what should I do?
And that's more like a straightforward thinking of how to take actions.
And here the expected free energy.
The structure of the expected free energy is the same but we are not evaluating expected free energy of policies, but expected free energy of observation action combinations.
So if I see something and if I do this, what's the expected free energy?
And that's what I'm trying to minimize.
That's what I'm trying to optimize in this setting, right?
So here again, we have the risk term where we are trying to minimize the deviation between the belief and the prior preferences.
We also have the ambiguity term and this together makes up the expected free energy of this time point at time T.
But we also have an expectation about what's the expected free energy in the next time step.
And to evaluate the expected free energy of next time step, you will have to again compute this equation with OT plus two.
And for that you will have to again compute this equation with OT plus three and so on.
And this automatically becomes a tree search because of the recursive way this equation is defined and it comes with its own problems, but there are clever ways to get around them and we are going to discuss that in the code today.
So, given the structure of sophisticated inference here, as I mentioned, the research replace the policy space that we saw for the traditional active inference we are used to.
So in this workshop, what I am focusing on is how to kind of define a generative model and given an environment.
So for example, this is the grid that is simulated in the original paper and we are going to talk about how to build up a generative model for this grid that can be used in the sophisticated inference in the PMDP module.
So basically, what I'm trying to talk about is that the environment will have a step function that takes an action from the agent in Pymdp, and the agent will get an observation out of that action and we'll talk about this particular function, agent step and agent steps.
Step will take up an observation and try to come up with an action for the next time.
Step right.
And this creates a loop and cleverly designing this loop will let you see emergence of purposeful behavior in the sophisticated inference setting.
So for example, in this particular grid with sufficient planning horizon, you will be able to see that the agent is capable of navigating in this grid and so on.
So this is the example that I'm going to focus on in this talk today.
Excuse me, I want to right away jump in to the code.
So we have the Pymdp home, which I'm hoping you are familiar with.
So we have this GitHub repository where we have the pymdp module and inside pymdp module we have several parts for it.
So here we have the agent in the original Pymdp module that implements the so called classical active inference.
We have several environments and we have help of functions like learning inference, maths and so on.
So this is the module of Pimedp.
But in the parent folder we also have examples where there is tutorials about how to use the agent class, how to kind of deal with the environments and so on.
So if you look at the pull requests so we are right now trying to merge sophisticated inference into the original Pymdp module.
And today I'm going to talk about the code in this pull request.
So if you want to try this hands on, you might want to go to this page where this pull request is there and it has the same structure of Pymdp.
It's basically designed using Pymdp.
And here what we have additionally is an agent si which is a sophisticated inference agent which does everything and also planning and decision making in the sophisticated inference way.
And in the parent folder there is also an example folder for sophisticated inference demo.
And what I am going to do today is to walk you through this tutorial of sophisticated inference.
And on the way, I'm going to discuss and at points where I reference the helper codes, I'm going to go to that code and try to explain what's actually happening and how we complete that agent environment loop where we can see that purposeful behavior.
Right?
Yeah.
So that's the Pymdp home.
Then I also talked about the pull request.
So let's right away go into the jupyter notebook.
So this is my local copy of this repository, so it's easier for me to run it and show it in my personal computer.
So this is the parent folder with Pymdp and examples and inside examples I have a demo folder for sophisticated inference and this is the notebook I'm talking about.
Right?
So here in this example, what we are trying to do is deal with this particular grid world task from the original sophisticated inference paper and make this agent or enable this agent to navigate to this red dot, which is supposedly the goal state in this particular task given a prior preference like this, right?
So this prior preference is quite informative in the sense that we right away can see that this is the most preferred state, the white color and the surrounding states are kind of less preferred, but more preferred than the faraway ones.
Right?
So this is the grid world task that we are trying to use.
So the first cell is importing all the necessary libraries and some useful libraries like NumPy and Matplotlib.
And the most important one is Pymdp.
So I'm actually now calling the local copy of my Pymdp with the sophisticated inference implementation, not the original one, which is not merged yet.
And the first thing I want to talk about is the environment itself, right?
So the environment step part where if I get some action, how does the environment work?
And for that, inside this folder I have a file which is Grid environment Si PY and this is basically an environment class.
So don't worry about how this environment is actually implemented.
The only thing to worry about is this function that we are going to use which is environment step.
So this function will take an action into it and depending upon the current state of the environment, it will calculate what is the most probable next state given this action from the agent.
So that's the idea.
And then it will also calculate a reward of some negligible negative value if it is not the Gold State, and if it is the Gold State, it will give a reward of ten.
And that's how the environment is.
Designed and it will update the current state to the new state.
And basically what it will return is a new state, depending upon your action, the reward for that action and whether it is an end of the episode and so on.
So this implementation is the standard OpenAI environment implementation and this is the environment step function, right?
So in this grid, for example, if I am right now in this state and if I take an action up, so I have four available actions north, South, east and west.
So if I go on north, then the environment step will make sure that I am in the state that is above the state.
And if I go east or west, then I'll stay here.
Or south.
I'll stay here.
So that's the idea.
And there is an episode length limit that is eight here, that means that I am restricting the length of every episode to be eight, which is the ideal length of reaching this goal state just to avoid confusion.
So in this environment, after eight actions, the environment will terminate.
And if you have to kind of reach this goal state in the optimal time point so that's the idea how the environment is implemented.
Okay, I hope that is clear.
And there are many helpful functions in this environment, like rendering the environment, rendering a prior preference matrix in this environment.
So if you design a prior preference, this environment can show that in a pictorial way how your prior preference is that you will see in the notebook below.
So now it's time that we define a generative model for the sophisticated inference agent, right?
Before that, let's define the structure of the generative model that we want the agent to have in its mind, which is tailor made for this particular environment, right?
So here in this particular grid world task, we have 25 valid states starting from this state.
All this black states in this path are valid states.
So there are 25 valid states.
Then there are four available actions for the agent, north, Southeast and west.
So this is part of our generative model.
This is also in alignment with the reality of the grid.
But this is about what the agent has in its mind, right?
And then the observation is just the state space.
The problem is fully observable, so there is no ambiguity there.
Then we define basically the number of states.
Then we define basically the number of states, which is a list of your state space, number of factors, which is now one because you only have one hidden state factor here.
Then number of controls, which is going to be four.
That's four available actions and your observation space like that.
So this is the structure of your generative model.
And let's look at the structure of the parameters now inside a POMDP.
So the first one is the likelihood function which is often denoted by capital A.
And here it is a function of how many observational modalities I have and how many state modalities I have.
Right?
If I run this cell, yeah, I have to run the parent cell to make sure everything works.
So I have rendered the environment the structure of the generative model.
And here I have the capital A matrix which has a structure 25 25.
That means that I have 25 states and 25 observations.
And here, because it's fully observable, I am initializing it as an identity matrix of size 25.
So that's my likelihood matrix that I'm initializing for this particular grid world task.
Then the second element is the transition matrix.
So please note that I'm using all the existing Pymdp functionalities to define a random A matrix and then using an identity matrix on top of that.
So, yeah, I'm not doing anything new.
Here it is the existing Pymdp functionality.
Then what I can do now is define the B matrix, which is also called transition matrix.
So the transition matrix encodes transitions like where I'm going to end up in the future if I start from a particular state and take an action.
So that's the idea where it depends upon the number of states, which is the hidden state modality and number of controls.
So it has the structure of state action state where if I take an action from a particular state where I'm going to end up.
So that is also a future state, right.
So I'm going to initialize it as the true environment state.
So now this is part of the environment that I've built.
It will give out the B matrix.
It might be worth it to look at the structure of this B matrix.
So here we have 25, 25 four.
So that means that if I take an action from a particular state where I'm going to enter and we have the true transition dynamics for this particular grid by design.
So there is a function called get true B and that will give us the true b of the system which the agent can use.
Okay?
So ideally we would want the agent to learn this, but for the purpose of this demo we are assuming that the agent already knows the structure.
And then comes the prior preference, which is interesting here in the sense that it is defined as how closer you are to the gold state.
So if you are at the gold state, then clearly that is the most sought out state.
You prefer that the most.
And how do you prefer the neighboring states, right?
So that is dependent upon the square root of the distance or basically the distance from that particular gold state.
So you define a grid which is eight cross eight, the same size as this particular grid world task.
And then we have a method to kind of add values which is the preference you have for every state.
And if you render the particular C matrix you can see the structure which is the same where this gold state is more preferred and the surrounding states less preferred and so on.
So now we have the C matrix also defined in the classic PMDP way.
And then I initialize that C matrix as the C matrix we evaluated in the previous cell which is small C, this particular C matrix.
Okay?
And then lastly, for the generative model we have capital D which is your prior overhead and states.
And for that I'm using a uniform object array.
So that means that I don't have a prior of where I am starting.
So let me run the pending cells.
So here the D matrix is a uniform distribution over hidden states.
I don't know where I'm going to start the simulations and so on.
So this is the basic structure of the generative model.
And then we have the agent class which I want to discuss separately, like the environment, right?
So given these environment parameters, how would you expect the agent class to work?
So where is the agent class?
Inside this folder structure?
Inside the Pymdp module folder we have an agent Si PY which is basically a class again and similar to the environment class here.
Also we have a step function where this will take an observation to the function and also a flag whether or not to learn the environment, which is optional.
So if you disable it, it won't learn the generative model.
If you enable it, it will update the parameters of the generative model.
And what basically it does is it will return an action which is to be taken at this point of time and the environment can basically use that action, right?
So in this file we have the agent class which I will explain in detail.
So I am basically importing that agent class in this cell and then we are going to try and reproduce this behavioral result from the original sophisticated inference paper.
Okay?
And for that.
So what we expect is that given this prior preference structure, there are local maximas in this prior preference structure.
So if you start from this particular point, if you do not plan deep enough, what you will end up is in one of these local maximas where you don't see that there is a highly preferred observation, say four steps down the line.
So if you are in this particular state, what you will see is this local maxima and you will go and sit there because the neighboring states are less preferred and this state which is more preferred is not accessible because of the wall or the wall structure.
So you have to take a turn and pass through less preferred states and you need deep planning in order to enable the agent to do that.
The agent should be able to kind of simulate four time steps ahead in time to see that there is this highly rewarding observation coming to kind of do that actions.
So that's the point that we are trying to see in this particular demo.
So for a low planning depth it will basically get stuck in one of the local maximas but with sufficient planning depth it will navigate to the gold state.
So that's what we are trying to see, right?
So we have different planning horizons and what we are basically doing is give the agent a generative model which we right now defined the A matrix, B matrix, C matrix B matrix.
Then we have the planning horizon of capital N.
So here I am, iterating over planning depth.
So N will be one, three and four for the loop.
Then we have action precision, which is often denoted by alpha in active inference literature.
So that determines which action is to be taken.
So a highly precise action precision means that it will stick to the action with the lowest expected free energy.
But a lower action precision is kind of probabilistic where it will also consider other actions.
Then we have a planning precision which is part of the planning function we'll discuss, which is often denoted in the literature as gamma.
Then we also have a search threshold which is extremely important for sophisticated inference because as we saw, sophisticated inference is a tree search and tree search is bad in the sense that it can have a lot of computations.
But you have to define a threshold to kind of ignore many possibilities to make it work.
And that's the idea that we will also discuss.
So just a preview before we go to the agent class.
What we are trying to do is in a loop we are going to call the agent step and environment step in series.
So the agent will see an observation, it will take an action, that action will go into the environment, the environment will give it back new observations and this loop continues.
And we want to see over time how this loop evolves into a purposeful behavior and if the agent at all is capable for that.
So before I reveal the results, let's discuss the agent class.
So in order to give an action, when an observation is given, the agent should have the planning and so on, right?
So here is the agent, the sophisticated inference agent, where we are actually using the existing Pymdp agent for some functionalities.
So in Pymdp we already have really well written functions for perception and learning.
So the only thing we want to kind of replace is how the agent is doing planning and how the agent is taking decisions over policies, right?
So here we are using that parent agent class.
So from Pymdp agent we are importing that agent class which is sitting next to the Si agent that we are discussing now.
And basically we are taking in the generative model structure from the main program for this class to work which is C and D and all the precisions and threshold parameter I mentioned, then it is kind of normalizing the prior preference that we mentioned in the main program.
So here if I look at how C is, the structure of C is defined in terms of numbers and the prior preference is often interpreted or it should be a probabilistic distribution for the computations to work, right?
So we are going to normalize it as a probabilistic distribution rather than having numbers that don't add up to one.
So that's what's happening here.
We are using Softmax to do that.
Then what we are doing is we are initializing the existing PMDP agent with these generative model parameters and what we are intending to do is write a planning function for a given planning horizon and a given threshold for trees.
Okay, so there are three functions in this agent class.
One is a helper function for planning which we will discuss now.
Then there is a planning function itself which is going to do planning using tree search.
And then because it is a recursive tree search, we are going to need an additional function that implements that recursive evaluation where we are going to call this function called forward search inside the function itself.
So we are calling this function inside this function.
So that is to calculate expected free energy for the next step and it will call it again for the next step till our planning horizon.
So that's the idea of recursive looping and finally it will return the expected free energy for all actions given an observations and then we just implement the step function where it is written sequentially what to do given an observation.
So going back to the demo here we have this first idea where you get an observation and it gives out an action.
So let's go to the agent step function and imagine what happens.
So if it is time t equal to zero or in the beginning of the experiment, what it is ideally.
Supposed to do in the first place is infer that state using its observation.
So what we are giving it is an observation and using the modules for inference, it's going to come up with a belief QS, which is a belief about states.
Okay, so self dot QS is the belief inside the agent and once it has a belief about where it is right now, it can implement plan research which is do planning for this particular belief of hidden state right now.
And once it has done planning, it can take decision using the sample action function in Pymdp and basically return that action.
And for every other time steps, the sequence remains the same.
But it is also learning about the structure if you enable learning in your agent class.
So that's the step function.
But in order to do planning, what it does is it kind of reorganizes the generative model structure for any number of hidden state modalities and any number of observation modalities.
So to discuss how melting works, I would like to talk about the new A matrices and B matrices it evaluates for implementing that planning and let's understand that.
So let's go back to the original hidden state factors.
So here we only have one hidden state factor.
So that's why it is B zero, right?
And B one does not exist because we only have one hidden state factor.
But imagine that if I have two hidden state factors with the same size maybe.
So here it could be a location and maybe something else inside the agent's mind.
And we should also have controls for these two hidden state factors.
Just like so there should be control for every hidden state factor if you're familiar with active inference idea and then maybe the observation space is also directly observing these two hidden state factors.
Okay, so this is a new Generative Model structure with multiple hidden states and multiple observation modalities.
And right away you can see that the dimensionalities of your parameters change.
You have 25 observations coming from 25 times 25 hidden states.
And if you look at the structure of the first observation modality, it's the same.
But what we want is a new matrix where it's going to be 25 with not two hidden states but just one hidden state.
It's only a reorganization of the generative model, but computations essentially remains the same.
So that's what this helper function is trying to do, which will make things easier for us when we have multiple hidden state modalities.
So if you have multiple hidden state modalities, we are going to compute how many total states you have, which is the multiplication of number of hidden states in each modality.
Okay?
So if you have 25 hidden states in one modality and 25 hidden states in the other modality, you're going to have 625 total number of states.
And if you have four actions each in each modalities, then you have total of 16 actions which is nothing but the combination of these four actions each in the modalities.
So you're going to have four times 416 actions if you have two modalities.
And it's basically going to build a generative model that has the same model parameters but just with a different dimension structure so that it's easier for us to calculate the expected.
So now we have a new A and new B and a new belief which is nothing but tensor products of existing parameters and beliefs.
It's nothing but a new big matrix and nothing else.
Okay?
It's not a change, it's just a transformation of structure.
And given this A, B and Q, we are going to predict what's going to happen in the future and evaluate the expected free energies for them.
So in order to do planning, so that's the second function.
What we are going to do is first call the first function which will do the melting for us and set up the generative model in good dimensions, easy to compute.
Then we have the expected free energy itself for all the actions and then we have the probability that depends upon this expected free energy for these actions.
So why is it just the actions and not the observations?
Because here we are going to evaluate expected free energy of actions for the given observations, right?
So let me go back to the slides and discuss this pictorially to make things easier.
So here we have the grid and we have the prior footprints.
And what we are trying to implement is that if you observe some observation at time T, then you're going to consider the consequences of your actions given that observation, because you can predict what's going to happen.
Because in your generative model you have the transition dynamics that will tell you, given this state, if I take this action, where I'm going to end up, right?
So that's basically predicting what's going to happen in the future and you're right now considering the consequence of available actions in your arsenal.
And then if you take an action, then you can predict what's going to happen in the next time step as a new observation, right?
So you have a probability distribution that tells you that say this observation is the most likely and the other observations are not really likely.
Then what you will do is you do this again, you consider the consequence of doing your actions from that particular observation and this goes on in your planning depth, right?
So this can be thought of as maybe you want to go to the gym.
Then you are going to consider all the consequences.
What will happen if I wear my shoes, if I don't wear my shoes, if I go in my car, if I don't go in my car, then you realize that, okay, I have to wear my shoes.
Then you consider the consequence that I'm now ready to go to the gym and me going to the gym will end up me being in the gym.
So that's the idea.
You consider the consequence of where you are right now and you can go as much as you want, right.
You can predict.
So in a game of chess, you might be in a particular state.
You consider your consequences, you see the future, you consider consequences from that future, and you can go as deep as you want depending upon your computational abilities.
Right.
So that's what you're trying to implement in this agent class where we are considering consequences?
Yeah.
So for every modality we are going to consider the expected free energy for actions.
And this will basically call the next function, which is forward search.
So forward search is implementing the thing that I just mentioned, considering consequences.
And in forward search, what you are basically doing is for every action.
So in line 149, I have a loop that goes over every action.
Then I'm going to consider the posterior or the consequences of all those actions.
I use my transition probabilities to evaluate that consequences.
Then I'm going to predict the observations, because my prior preferences are defined in terms of observations.
I'm going to predict my observations and then evaluate the expected free energy, which is the sum of risk and ambiguity.
Okay?
I hope that makes sense.
Like here, you have considered the consequence, which is consequence of future, which is post or posterior.
And you're basically evaluating how good that posterior is depending upon your expected free energy.
And that becomes the expected free energy for that particular action.
And you do this for all the actions.
Okay.
And why this is powerful?
It is because you can go as deep as you want.
So here in the next step, you go to this loop where you will check if I am crossing my deep planning or the depth of planning.
And then you are doing basically the same.
Given that posterior, what is the consequence of the actions of that particular posterior.
So here for considering that we are again calling the parent function.
So the same function, forward search, to consider consequences of those combinations and it will basically come back and add up to your expected free energy.
So what happens over this sequence is that you consider some or all future consequences and then all that values will trickle up your tree.
And that sum of the expected free energy will tell you which action is good or which action is bad, which you can take to kind of see your preferred observations.
So that's the idea of implementing tree search.
And I will also talk about the importance of this threshold here, which makes this algorithm possible.
So without this threshold, this algorithm will not work.
I will explicitly talk about why that is the case.
And then once you evaluate the expected free energy for all available actions, given the present state, you can basically compute what you call the action distribution.
That is how probable is my action or how I should take my action.
And we also have this action precision parameter alpha.
So if alpha is very high then it basically is a highly skewed distribution where you will always choose the action that minimizes expected free energy.
If alpha is really low then it's going to be a more sparse or spread out distribution.
And then you can use this action distribution to sample actions in the agent environment loop.
We just finished doing planning and computing that action distribution.
Then using that action distribution, you can sample an action from your policy space.
So let's look at the policy space in this generative model.
So I'm switching back to the original generative model with one hidden state factor and let's do planning and maybe initialize this agent.
I just want to initialize this agent to see the policy space, not run the loop.
So I initialize this agent, say for planning depth of one.
And if I look at agent policies, I can see that I have basically four available actions which is north, south, east and west.
And if I have an action distribution, it will tell me how probable is to take that action.
So if I look at agent UPI, okay, so this is not defined because I have not done planning, but I can do planning and then it will be defined.
Yeah, so I implemented planning with research and then now I have an action distribution.
So for this particular scenario, I am going to take my third action the most which is zero point 99.
Basically that's the probability which is north, south and east in this particular case.
I just wanted to kind of familiarize you with the matrices, but we are now going to see the agent environment loop in action.
Now you can sample an action from the sample action function and then implement learning which is using the standard Pymdp way where I will update my transition dynamics and likelihood dynamics depending upon what I see and what's my belief and so on.
So my emphasis is on the decision making part.
So once you sample an action, then that action basically goes back to the environment.
Okay, so now let us implement this for a planning depth of one and see how the agent behaves.
So here if it is a planning depth of one, then that means that the agent is only considering the consequence of one time step ahead, just seeing the immediate future for doing planning, right?
So I'm giving the planning depth of one.
I'm resetting the environment where the agent is going to start from that initial start state, and in the loop, it's going to get that observation, take that action, give back an action, and we will look at the action probabilities.
And also we will give that action back to the environment, get back the observation, and this loop continues till the episode is terminated.
And I have set the episode length to be eight, just to see the outcome of eight action.
So when we run this loop, these matrices are nothing but the action distributions of how likely each action is to be taken.
And this is where the agent end up in the last time step.
Okay?
So let's maybe kind of also enable this environment render that will show us where the agent is at every time step.
So initially the agent was at this location and we have an action distribution of this here.
So north, south, east and west.
So the agent knows that it should go north.
Why?
Because if I look at the prior preference, this state is more preferred than this state.
Right?
So the agent successfully calculated the expected free energy and inferred that, okay, I should go to this state and not stay in this state.
And because it has the generative model of transitions available, it can infer that I should take an action north to go to this state.
So that's good.
And the agent goes to north.
And at this particular state, the agent infers that it should go to north southeast.
So it will take an action east and it will go here.
And at this point of time, I want your attention where the action distribution is equally probable for north and east.
Why is that?
Because the agent is only looking at the immediate future.
Right.
So let's go back to the prior preference where the agent is right now here, or is it here?
Yeah, it is right now here in this particular state.
And if the agent is considering immediate consequences of just one action, then these two states are equally good for it to be in the next state.
So there is no distinction between these two states if it is only looking at the immediate future.
So that means that the expected free energygies will conclude that I should go to north or east.
It doesn't matter if I'm looking at just one time step ahead.
Okay?
That's the idea.
And out of probability it is going here.
It took the action east and from this state, when it's doing inference, it's inferring that this state is better and basically it's ending up in this local maxima state, which is this particular state where the neighboring states are less preferred.
And this is Wall and you can't go there because it is forbidden for the agent by structure.
So it's basically going to sit there forever where it only sees that local maximum of prior preference.
And let's look at what might happen if you have higher planning depth.
So if I go to the planning depth of three, then that means that the agent is actually reaching the goal state at the last time step.
But still in the third time point, it had two probabilistic actions, north and east.
So here from this particular state, out of probability, it took the action north but it can all equally take the action east and end up in this local maxima.
So let's run again and probably it will end up in this local maxima, okay?
And only for the planning depth of four, which is sufficient enough, which is necessary for this particular grid, the agent is fully sure of what to do.
So at every time point it is fully sure of what to do, that it has to go north, then east, north, north, north, east, east and south and reach this particular goal state.
So only for time step or planning depth n equal to four, it can successfully navigate this grid with 100% certainty.
So that's the idea.
That's the implementation that I hope you got.
So there is also this idea of action precision.
So here it's a high action precision.
That is why it is taking the actions.
That is from the probability.
If it is a low action precision like one, then the good actions are more probable.
But that doesn't mean that it will be taken right here by luck, it is taking the right actions and reaching the state.
But here probabilities are most passed.
But you will also see like exploration behavior in more number of trials if you control this action precision.
So I set it to a high value to make sure that the agent reaches the goal for this particular problem.
But it's worth playing and it's important, right?
Okay, yeah.
So for different planning depths like one, three and four in this problem, this is the behavior that you expect.
For lower planning depths, which is not sufficient, the agent ends up in local maximas or local minimas of expected free energy or local maximas of prior preference.
But with sufficient planning depth, it's able to navigate and reach the goal.
So that brings us to the last point in this tutorial where why is it important to have a threshold in evaluating sophisticated inference?
So by threshold, what we mean is that we can ignore future possibilities in two levels, right?
You can ignore not likely actions or not likely observations in this research.
But if you consider the consequences of all actions and observations, that means that you'll have to consider four consequences in the first place.
Then you will have to consider four times the action states in the next time step for the next time step.
Then all of that multiplied with the number of actions and this tree search becomes intractable and you'll explode.
And it's even worse than the classical active inference policy space problem.
But by defining a threshold of even a small value, we'll ignore possibilities.
So where is that implemented?
In the forward search algorithm, we are considering actions with only action probabilities greater than the particular threshold.
Here I am defining it as one by 16.
Also in the parent paper, it's one by 16 the action probability.
Okay?
So if it is zero, then that means that it will consider all the consequences of future and that's intractable.
So you can ignore actions which is not probable, and also ignore states which is less likely, or only consider states that has probability greater than this particular threshold value, and that significantly reduces the computational complexity, where you will only consider combinations that are probable in the future.
Tree and that lets you go deeper in your planning horizon.
That's an important point here.
And if you compare the time that takes for deeper planning for a search threshold of zero, so a search threshold of zero means that you will consider all consequences.
And the more deep you plan, the more time it takes.
And if you see to consider only the first future or the immediate future, it takes 0.1 second.
For considering three possibilities into the future, it takes 3 seconds, and for four it takes 300 seconds.
And you can see that the computational time is exponentially growing.
But if you have a very small search threshold, you have that computational time that makes sense for implementation in real world, right?
So here for N equal to four, that is four times steps into the future, it's only taking 0.1 second.
And that's okay.
I can still do simulations with this complexity, but there is no way I can talk about how less the computational complexity is.
It truly depends on the nature of your prior preferences and environment in action.
But this search threshold actually works in real life, and we just saw that in our simulations, right?
For N equal to four, it took only like 0.3 seconds in our simulations.
But if you set the search threshold as zero, it already is 300 seconds for doing full depth planning.
And if I set a planning depth of five, then it will basically run forever maybe, and I will not be able to do simulation.
So that's the idea of search threshold.
So actually, that's it.
I wanted to explain the Agent class, the environment class, and the particular demo and yeah, maybe it's a good time for questions if anybody was listening.
And I hope people get to play with this code and look at the tutorial and implement this and build generative models like this.
So this particular example is how do you build a generative model for this grid world task and see how the Agent is able to take meaningful actions?
But here we gave it that true structure of the environment in the B matrix and A matrix and so on.
But you can also play around with learning in the sense that while defining the Agent step, you can add a flag that says learning equal to true.
And if you start with an uninformed AB and so on, you can experiment on how the Agent is learning that environment.
Here you can look at the B matrix in the beginning, you can look at the B matrix after, say, ten trials and see how the learning is taking place here.
It doesn't matter because the agent knows the structure and it won't learn much.
But if it starts from an unknown structure, then there is scope of learning also to be implemented.
And it's already implemented because we are using existing Pymdp functionalities for learning A and B and it's already part of the step function.
So I hope step function is clear, which is the only thing you need to know if you're trying to implement sophisticated inference and just the names of these matrices if you want to probe them and look at them.
And yeah, I hope the session was useful.
So I thank my collaborators and Connor, who maintains Pimdp, and also Brendan who runs the Pimdp Fellowship, which I was part of, and that's where I worked on implementing sophisticated inference in Pimdp and it will be part of the original Pymdp module soon.
And I hope people can start using this module to simulate sophisticated inference experiments and this basically becomes useful.
So maybe it's a good time to discuss questions or clarifications on the code or maybe it's a good time to take a break, as Daniel was.

1:00:27 _Daniel:_
Thank you.
That was awesome.
Well, I have a few different questions and I'll read a few from the live chat.
So I'll first just go to the live chat and then ask those and then ask some other questions.
So Dave asks, how do you think about the neural implementation of recursion?
Brains don't seem to implement computer hardware style recursion deeper than a stack depth of one.
Aside from heavily over learned tasks, we can confine ourselves to asking about recursion for the purposes of exploring temporally deep state spaces, searching forward in time.
So how do we reconcile this really beautiful and elegant and computationally efficient full depth tree search with the biological basis of multiscale planning?

1:01:21 _Aswin:_
Yeah, so I'm not an expert in neural computation, but the answer to that would be basically you're doing only one computation at a time, right?
And all you need is some memory to store your beliefs and use those beliefs to kind of do the same computation again.
So we are not talking about this hardcore recursive implementation.
We are only doing local computations at a time.
And just because of the structure of the generative model and because we have memory, this can be done.
And I don't see why brain can't do it, even though individual neurons might not be able to do it.
The brain has memory.
The brain has the ability to store memory and the ability to dream, the ability to simulate.
It knows the consequences of actions.
And you do this on a daily basis where you plan your future and decide what to do.
Right?
So on a single neuron level, I'm not really sure of how to answer that question, but I don't really see why the brain can't do it as an organism.
Cool.

1:02:40 _Daniel:_
Okay, to the code.
I guess I have a few questions.
Can we go back to the maze?
And of course, if anyone else has questions in the live chat, just go for it.
So in the maze, how does the moves that are possible, how is that reflected?
What stage is it updated, for example, that it initially knows that it can only go up and then it can only go right or down?
Where is that reflected with the updating of kind of that relational aspect of affordances?
What is even possible to do?
And then how does it evaluate in a deep tree search?
Does it need to know what things could or couldn't happen in the future?

1:03:39 _Aswin:_
So, if I understand the questions correctly, there is an important distinction between the generative process and the generative model, right?
So in the grid world, which is the generative process, we have implemented all of that manually, where we have this transition dynamics that already knows what will happen if you take an action from a state.
So it's like an environment that knows how to work.
So it's like a reality where there are consequences of actions and it's already there.
But this information is available to the agent to be part of its generative model.
And in the generative model, what it basically does is use that transition dynamics, which is given or learned to simulate what might happen in the future.
Okay?
So once I have that transition dynamics, if I go to the where's the if I go to the tree search, what it is essentially doing is evaluating the posterior given a particular state and an action J.
So from my generative model, I know that if I start from this state and if I take this action, I go to this posterior and I consider all the consequences.
And if in the generative model, it is unlikely that if I go east, I don't go there and so on, it's automatically reflected in the expected free energy.
So I hope that answers the question.
So here, if I set the action precision to be high and also enable the so initially I am in this particular state, and with respect to the expected free energy, what I'm doing is I'm using my generative model to predict what will happen if I take four actions.
And my predictions will say that if I take North, I will go here.
And if I take all the other actions, I'll stay here.
And because in my prior preference, north is more preferred, I can infer that north is the action I should go for.
So that's the idea.
So here, the grid structure is given to the agent.
And it might be a little confusing, but the agent can also learn this grid structure and this will work.
So once I know the grid structure as an agent, I can simulate the future and consider the consequences of action, right?
So that's what's happening.
And once I am in this state, I will consider the consequence of all four actions, and I will infer that, okay, going east is better because that will take me to this state.
So there is always a difference between or you should keep in mind how generative model and generative process are two different things, and what the agent knows might not be the reality or might be the reality, depending upon what you give it.
Makes sense.
Cool.

1:06:46 _Daniel:_
So if you were going to go about making a new situation that you wanted to do generative modeling for, do you tend to start from an existing working Pi MDP notebook and start modifying state spaces, or do you draw it out on a canvas?
How would you recommend somebody other than replicating what is shown here?
Let's just say we're interested in something that's not exactly just a maze.
What do we do to get our head around how we should proceed?

1:07:24 _Aswin:_
Yeah, good question.
So if you are trying to simulate, say, a new environment, you have the heavy lifting to do, which is to define the generative model for the agent.
You can either define a very sparse generative model, which the agent can learn, but you have to define the structure.
That structure should be there, and only using that structure, the agent can learn the generative model.
So here you can make use of this cell of code to understand how I define the structure of the grid.
Okay, so I am defining a structure for the agent for it to make use of.
I'm saying that there are 25 valid states and there are four available actions.
And this is the standard way of defining the state space in Pymdp.
And you also have to define the central parameters ABC and D for the agent simulations.
So here I am defining A using my state space and observation space.
But this step of giving it or telling it that it's an identity matrix is my decision choice in my modeling.
I don't have to do this for simulations.
I can see if the agent is learning it from a random A matrix or when it starts from a random A matrix.
And similarly for this B matrix, this structure is defined.
And there are functions like this which can give you a random B matrix.
But this is a modeling choice where if I want to give it the grid structure or not give it the grid structure, I can start from a random B matrix, let the agent learn, and look at that learned B metric.
Just for the purpose of the demo.
I gave it the grid structure to enable it to take the actions.
But it's not a mandatory thing.
So this notebook is useful in the sense that you know what to do, but definitely you should play around with steps that may not be mandatory.
Right, so if I give a prior preference for this state to be the maximum, then you can see behavior that.
The agent will try and go there.
Right.
So this prior preference is defined in conjunction that this is the goal state, but this may not be the goal state.
And in a different ask, what prior preference means is different according to the environment.
Right.
So that's also there and your prior.
So once you define that generative model, which you have to do, you can't run from it, then everything is kind of automated.
The agent only have to use the agent step, give it the observation from the environment.
The agent knows how to take actions, and then everything that happens inside the agent, you don't really have to worry.
So this structure, I'm sure, will be useful for your particular task that you are trying to model in your hmm.

1:10:31 _Daniel:_
Yes, very interesting.
And how would you contrast that or point to any similarities or differences with how this would be pursued outside of active inference?
Like if somebody were just going to use another kind of deep policy agent in the maze example, what parts of the process would be familiar and what parts would be like a lot of work that wasn't expected or skipping through parts that were a lot of work otherwise.

1:11:00 _Aswin:_
Yeah.
So the general structure is very familiar to somebody who does things like this in reinforcement learning.
So the idea that it's an agent step and environment step, so this is the standard OpenAI gym way of writing an environment and a standard OpenAI way of writing an agent.
Okay?
So if you have a Q learning agent who does the same trying to navigate, then the way you have to define the queue matrix is the heavy lifting there.
It's just a state action mapping.
And in contrast to that, in active inference, you have to come up with a generative model that you want to see.
So in active inference, generative model is the central thing.
Right.
Without a generative model, there is no meaning of purposeful behavior in active inference.
So the only unfamiliar part for a person who is coming from, say, a field like reinforcement learning is the structure of the generating model.
But there is no way, other than getting used to it, where it's the palm DP structure which dominates.
But if you're doing deep active inference, all of this is going to be neural networks and palm DPS are also not active inference things.
Right.
It's an industrial engineering thing.
So palm DPS must also be familiar for people who are coming from the computer science background, just the idea that what really happens in the agent is the active inference part where we have expected free energy s and variation of free energy energies.
And if you want to learn about that, then you have to go to the agents and see how it works.
Look at the matrices numerically, see what's happening.
But in a level where you want to get started, I don't see any problem.
All of this is standard frameworks like palmdps and OpenAI gym environments, agent environment loop.
All this is very deeply discussed in computer science.
It's not cool.

1:13:10 _Daniel:_
So what other motifs or cognitive phenomena are you excited or how do you see the Pi MDP development trajectory continuing after your sophisticated inference gets pulled in?

1:13:27 _Aswin:_
Yeah, so the Pimdp had the original functionality and the functionality to implement or simulate general active inference agents with the policy space and so on.
And that enabled a lot of people in the community who are not familiar with complicated coding and so on, who people who do psychology, psychiatry, and all the things.
Right.
So whoever want to come up and try implement active inference, pymdp enabled that.
And I am hoping that this module will enable people who want to try out sophisticated inference experiments in their particular domain.
So if you spend some time and get familiarized yourself with the structure of how Pymdp works, then everything else is just writing a jupyter notebook with minimal code, right, to simulate this.
So if you have a particular task in your domain, I don't see a problem for a beginner to kind of try and code it.
And what I'm very excited to see is people using this module for variety of experiments, just like how people started using Pymdp and sophisticated inference is taking off.
And it's now widely talked about how it is the way of doing active inference.
And I'm really hoping that people in various domains start using this module and see their experiments, and I look forward for the feedback.
Yeah, so what Pimdp did two years ago, I'm hoping this module will do to people who are trying to model active inference in the soap state.

1:15:14 _Daniel:_
So you mentioned the OpenAI gym and the standardized format, and what benchmarks do you use or what kind of test suites are you comparing, and how do we really know when we've made a generative model that really exceeds or excels in a way that other techniques are just not doing?

1:15:43 _Aswin:_
Yeah, so if I may go to the OpenAI gym website, we have several experiments.
There the classical reinforcement learning examples like the lunar lander that you see in this screen right now.
So active inference from its inception has faced problems of scaling to tasks.
And that's in itself a field of research in active inference, scaling active inference.
And that's one of the reasons why deep active inference took over dealing with tasks like this.
So there are benchmarks even now where the sophisticated inference may not be able to deal with state spaces.
And personally, that's my research.
In my PhD.
I am actually looking at optimizing computations in sophisticated inference algorithms that lets you scale up to environments like that.
But to get started, you will have to kind of write code and see if it works for an environment, then look at if it's not working, then you have to look at methods to scale it up and so on.
So if I am talking about benchmarks, sophisticated inference is as good as any RL algorithms for this state space.
So for small problems, sophisticated inference will work and it's really good.
But for high dimensional problems like this, the classical implementation that I just showed might not work, but it's good enough for any decent experiment.
But if you want to scale up, then that's still open and it's a new field of research and what you do might become a next new important paper.
So that's all I can tell in that regard.
Cool.
You have to work and see what.

1:17:30 _Daniel:_
Measures do you think you'd be looking for, like computational resources or what are the measures that even make sense to juxtapose such different methods?

1:17:44 _Aswin:_
Yeah, so the OpenAI Gym was designed for that, to compare different algorithms.
So OpenAI Gym by definition is a collection of many environments.
So in my demo, I was talking about the grid environment.
Openiigm is nothing but a collection of many environments which will let you interact with those environments using the environment step function.
Yeah.
So here we have the environment step function that will let you interact with the lunar lander.
And that particular task will have matrixes that lets you judge how good or bad your algorithm is.
So in this lunar lander problem, how optimally can you land your rover between these two flags by spending minimizing the fuel and so on.
So those matrices are very tasks specific, and that's one direction you have to take.
You can take try and compete with RL algorithms in matrixes, but the right potential or the potential I see in sophisticated inference is modeling intelligent behavior, where in RL the focus is to get things done to make this work.
But it's not really explainable, especially deep RL and deep learning methods.
But in active inference, if you manage to scale it up, they are explainable and that will let you understand how intelligence emerges with time.
And I see that more interesting than competing with RL, because if your focus is getting things done, then maybe engineering is the right way and not active inference.
Awesome.

1:19:30 _Daniel:_
Any other comments or thoughts?
Aswin, do you have any other comments or thoughts?

1:19:45 _Aswin:_
No, I'm pretty happy.
I hope I was clear explaining the code.
Maybe it was too complicated or simple, depending upon your level, but I hope it is useful to at least one person who would start using this and write the code.
Thank you so much for your time.
Awesome.
And thank you for the opportunity.

1:20:05 _Daniel:_
Thank you for joining.
Till next time.
See you.

1:20:09 _Aswin:_
Thank you so much.
Bye.
