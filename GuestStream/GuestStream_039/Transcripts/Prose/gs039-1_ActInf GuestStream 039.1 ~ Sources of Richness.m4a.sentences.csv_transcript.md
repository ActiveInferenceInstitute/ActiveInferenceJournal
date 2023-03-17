00:07 _Daniel Friedman:_

Hello and welcome.
This is active guest stream number 39.1.
It's March 16, 2023.
We are here with Xu Ji, Eric Elmoznino, and Guillaume Dumas.
We're going to have a presentation followed by a discussion action.

00:26 So thank you all for joining and off to you for the presentation.

00:33 _Eric Elmoznino:_

All right, thanks.
Daniel?
Yeah.
I'm Eric.
I'm a PhD student in Yoshua Bengio's lab.

00:39 _Xu Ji:_

I'm Xu ['Shu'] Ji.
I'm a postdoc with Yoshua.

00:42 _Eric:_

Yeah.
And we're we're really excited to be here.
Thanks for the invite.

00:45 We're going to be talking about why we can't describe conscious experiences.
So this is going to be our take on a really long standing problem in the philosophy of mind.
But we're going to be looking at it through the lens of computational neuroscience and information theory.
So, yeah, hopefully it'll be fun for everyone.
It mixes a bunch of disciplines.

01:07 So I think the most salient way to illustrate the problem that we're going to be addressing is to ask you to try and think about how you would describe the experience of seeing the color red.
So probably the kind of stuff that's going in your head is things like, well, it's a bright, aggressive color symbolizes love, that sort of stuff.
And in a sense, this is a description.
It's effective.
I would be able to guess which color you were describing, but in another sense, it's really inadequate.

01:39 _Xu:_

Right?

01:39 _Eric:_

If I were blind, for instance, your description would be totally useless.
I would be no better in understanding what red looks like.
So there's this real sense in which conscious experiences are ineffable such that we can't describe them.
And this applies to percepts like red, but it also applies to experiences more broadly.

01:59 The experience of having a thought is just so ineffable, so hard to describe.
And really importantly, this doesn't happen with most of our knowledge.
I could describe most of what I know except for experiences.
They have this special place.
So it's a big topic in the philosophy of mind because it relates a lot to this thing called the hard problem of consciousness.

02:24 So basically all the hard problem is it's the problem of how and why physical processes give rise to conscious experiences in the first place.
So this is probably the oldest and most debated problem in the philosophy of mind.
And it's even led many to the conclusion that actually we're going to give up.
And consciousness can't be explained with physical theories at all, that it can't simply emerge from neuroscience computation or known physical laws.
So that's a bold statement, and I won't get into all the details about what makes the hard problem so salient, but just here's a few things.

03:03 So, first of all, we can logically conceive of what are called philosophical zombies.
Philosophical zombies very different from Hollywood zombies.
They're basically beings that are physically identical to us.
They behave exactly like us.
In fact, they even have the exact same neural activity that we do.

03:23 But they just aren't conscious.
So similarly, instead of these alternate agents being unconscious, we could also imagine them as just experiencing different things when they're in the same states.
So for instance, it's conceivable at least that in an alternate universe, the same exact brain mechanisms that produce an experience of red in this world would instead produce an experience of green in the other.
And that all experiences would kind of be like flipped in this way.
So intuitively we think that these two thought experiments aren't actually possible in our universe.

03:58 But even just their logical conceivability suggests some kind of explanatory gap where consciousness doesn't seem to neatly emerge from or be determined by physical state or function.
Another really prominent thought experiment is the knowledge argument.
And this is the main sort of problem that our work is going to address.
We're not going to address all facets of the hard problem of consciousness.
But this knowledge argument is one of the biggest arguments against physicalism.

04:27 So how the knowledge argument goes is it's another thought experiment.
It asks us to imagine Mary, who has grown up in a black and white room her whole life.
And despite this poverty and stimulus, she actually knows a lot.
In fact, we're going to assume that she knows all the physical facts about how color perception works.
So all the relevant physics, all the relevant neuroscience, et cetera.

04:53 And now we're going to ask, well, does she learn something new when she steps out of the room for the first time and actually experiences color?
And if we say that she does learn something new, which I think is the intuitive answer, there seems to be a problem.
We assumed that she knew all the relevant physical facts about color perception.
So doesn't this mean that what she learned had to be something that was nonphysical?
And if there was nothing more to color perception than physically embodied information and neural activity, then the experience is something describable that she presumably could have read about, understood, and would have already known?

05:35 So it feels like this thought experiment really pushes us against physicalism towards this idea that maybe conscious experience has something on top of just information content.
Now of course we don't want to reject physicalism.
It's been very fruitful for us in the history of science.
So we really do want to say that experience just consists of information that can be described.
So there has to be something wrong in this knowledge argument here.

06:04 And what we're going to do is we're going to bite the bullet and acknowledge that experiences actually are ineffable.
So maybe it is the case that experiences can be described in principle since they consist of nothing more than information, but maybe they can't be described in practice, or at least they can't be fully described in practice using something like language.
So then the challenge becomes explaining why experiences are ineffable under a physicalist framework.
And that's what our work is really going to be about.

06:38 _Xu:_

Okay, so the structure of the talk is going to be like this.

06:42 I'm going to summarize briefly why characterizing richness and ineffability is an interesting and important question.
Then Eric is going to talk about how there's a natural correspondence between ineffability and information loss which is going to let us link biologically plausible attractor models of working memory to ineffability, essentially because information loss is inherent in attractive dynamics.
Then I will talk about if you consider the ineffability of conscious experience to verbal report as just a special case of information loss between two specific points in the communication pipeline, then you can actually generalize the notion of ineffability more broadly by considering, for example, loss from sensory processing to conscious experience and even interpersonal information loss.
We're going to prove, using kilgomero of mutual information that your conscious experience being ineffable to another person implies high cognitive dissimilarity between the two of you under our model.

07:49 And finally we'll talk about whether an exact definition of conscious experience is required at least for characterizing the nature of ineffability and richness and also some open questions.

08:05 So yeah, why is richness and ineffability an important question?
There are sort of several reasons.
So first, as Eric said, understanding consciousness is not just of general interest.
It's a long standing central problem in philosophy of mind because it's not easy to reason about, which has led some dualists to believe that consciousness must be at least partly nonphysical in nature because they can't see how it could be explained by physical processes.
But it's also a topic that is of great interest in machine learning because if you assume that consciousness is essential to human cognition, then it follows that we won't be able to engineer machines that think like humans without incorporating consciousness.

09:02 We're actually going to argue in this talk that the confusing aspects of human consciousness, such as its ineffability can be understood with information theory, which, as you all know, is born from computer science.
We're going to use some primitives from information theory to shed light on why consciousness is ineffable and hopefully to dispel some of the mystery surrounding it.

09:31 _Eric:_

All right, so one of the main primitives over here that we're going to use is to talk about attractor dynamics in the brain and in conscious experience and how that results in ineffability.
So hopefully this sort of perspective is familiar to most people.
But we could talk about neural dynamics by saying the brain has a state at any particular time and we could denote this state using a vector.
So for instance, in this plot over here, maybe we could denote each axis in active states, each dimension using an individual neuron.
And maybe we denote the activity of each neuron using its average firing rate.

10:12 So any states at a particular time would be the firing rate of all the neurons across the brain.
Now, there's nothing special about neurons or firing rates.
If you think that things like the synapse strengths or the dendrite potentials or the astrocytes or whatever else is also important to the representation, you could include those in the state.
They're just additional axes.
The details aren't so important as long as we have some state that describes what the brain is doing at any particular time.

10:43 Now, of course, the brain is a dynamical system.
These states are changing.
So you can think of tracing out trajectories through state space as a function of time.
And the way that the state evolves will be determined just by the recurrent connections within the brain, as well as inputs coming from elsewhere.
Maybe we're just talking about the dynamics within a given brain region.

11:06 The inputs would be the other brain regions talking to it, as well as any sensory stimulus coming in.

11:15 Right?
So this dynamical systems perspective of the brain has been really instrumental in understanding the computations it performs.
And one of the primary methods for characterizing these computations is to look at what are called the state attractors of the system.
And for us as well, state attractors are going to be a really important part of our ineffability framework in a bit.
So basically what an Tractor state is, is it's a state where once the system reaches it, it's going to remain there at least until inputs come in and change the dynamics or noise, not just the state out of this attractor.

11:54 So you can see this thing clearly within the figure.
The X and y axis over here are like the state of the brain.
Again, maybe something like the average firing rates of the neurons.
These arrows are illustrating the dynamics of the brain.
So how the state will evolve given the brain's connectivity, given the synapses.

12:13 And you can see that there's some regions where all the arrows, all the dynamics kind of contract to a single point.
So that's called a fixed point.
If it's one dimensional, it's a kind of state attractor.
And because all the arrows point towards it, once you finally reach that state, you're not going to move out again until the dynamics change, because inputs came in or until noise nudges you out.
And you can see that each state attractor also is associated with this sort of attractive region, an attractor base in its cults, where once a trajectory is somewhere in that region, it will eventually converge to the attractor again in the absence of noise.

12:50 So these attractors are really common in the brain and also in artificial recurrent neural networks trained on tasks.
And a big computational benefit is that they provide a form of transient memory.
Once you're in the attractor, you remain there, that's where the memory comes in.
And because of this and other benefits, they're implicated in a wide variety of neural processes like working memory, long term memory, decision making and higher level cognition and we'll argue consciousness in general.
So they're all over the place in the brain.

13:25 An additional aspect of them that's interesting and it's going to be relevant for our talk, is that you can think of attractors as having a sort of dual discrete and continuous nature.
So what I mean by that is that the discrete aspects of an attractor is given by the fact that there's a finite number of them and that attractors are mutually exclusive, right?
You're in one or you're in another.
So this means that we could use discrete symbols to denote which attractor the system is in.
There's a finite number of them, you're either in one or another.

13:56 And this basically lets us identify or label the states using a discrete variable.
There's also a notion though, in which an attractor is just a continuous high dimensional vector in this really high dimensional state space of the brain, right?
Every attractor basically is just a vector in state space.
And that means that they're not arbitrarily discrete states, they have continuous representations.
We can say, for instance, that one attractor is more or less similar to another one depending on how close they are in state space.

14:28 And that gives a representation to the attractors that's the high dimensional sort of continuous part.
So just to recap, discrete part is you could identify which attractor you're in in the finite set of all possible attractors.
But you could also talk about an attractor through this continuous high dimensional vector that describes where the attractor is in the high dimensional state space of the brain.
And to wrap your head around this, there's a good analogy to word embeddings in NLP.
So in NLP each word has a discrete ID that's like the symbolic discrete part, but also each word is associated to a high dimensional vector that gives it a representation sort of the meaning of the word, where we could say that words are more or less similar to each other.

15:20 Okay, so we're going to use attractor dynamics quite a bit to explain a significant source of ineffability in conscious experience later.
But for that to be relevant, I first need to spend a bit of time to convince you that neural dynamics that produce conscious experience actually do have attractors.
And for this there's already a lot of work in the literature connecting attractors to conscious experience.
So this part is not something new from our work.
So for instance, one of the leading theories of consciousness, which is the global workspace theory, actually implicitly implies that attractor dynamics are kind of fundamental.

15:57 So what global workspace theory says is basically like across the brain in all the different regions, you have sort of sub process worker, workers basically, and these different distributed mechanisms, they can't speak to each other very easily.
They mainly communicate through this global workspace just kind of like a bottleneck.
Think of it like a blackboard that all the different processes across the brain could write to.
You could also think of it as like the ram of the brain, but basically it's collecting information from the different workers.
And one key aspect about the global workspace that's posited in the theory is that for content in the workspace to then be broadcast to the subprocesses, for instance, for us to be able to talk about what's in the workspace for it to be written to kind of speech regions.

16:52 The content of the workspace has to be amplified and sustained for a certain amount of time.
It has to be stable, basically.
And this is clearly where the attractors come in, right?
Attractors by definition are these states that are stable, these states that are sustained.
So basically what global workspace theory says is that the context of the global workspace that can be used by the rest of the brain are the attractor states.

17:18 And the relevance to consciousness in this theory is that it posits that the contents of this global workspace are the things that we're aware of, the things that we're able to report, the things basically that we're conscious of.
And then just kind of like terminologically.
Another term for this workspace is called working memory.
The idea there, it's a sort of like really short term memory in the sense that you could quickly act on the things that are in this global workspace or report on them.
They're accessible, basically.

17:53 Okay, so that's one very powerful argument for why attractors are relevant to consciousness.
There's a bunch of other related arguments.
For instance, just introspectively you could think of what experience is like is a sequence going from one thought to the next to the next.
We kind of have this like a sequence of discrete events.
And that clearly looks like a dynamical system, kind of jumping between attractor states and then experimentally.

18:22 There's also been work showing that in psychology experiments, when you sort of present a stimulus to a subject and you vary the amount of time that the stimulus is presented to kind of bring it below or above the conscious threshold.
Well, in the conditions where subjects report being aware of the stimulus, the main thing that's different is that the representation is really stable and robust and noise.
And those are also clearly properties of attractors.

18:50 _Xu:_

Okay?

18:50 _Eric:_

So again, I'll use those attractors to identify a source of ineffability in a little bit.

18:56 But first I need to also introduce how we're going to formalize the very notion of ineffability.
And for this we're going to use information theory part Shannon information theory.
I'll do that now and then she will talk a bit about Kamagrav complexity as another formalism.
But hopefully most people are familiar with this.
But one thing that we're going to be using is the entropy of a state.

19:23 So for instance, if you have the entropy of some random variable X, to make things concrete, maybe that random variable is conscious experience.
So the entropy of conscious experiences, that value would be high if the distribution over conscious experiences was kind of diffused.
Andy Clark so there's equal probability for all possible experiences, and entropy would be low if the distribution over conscious experiences was peaky.
So that's kind of like the green distribution in this image would have low entropy and the red distribution that's sort of flatter and more uncertainty would have higher entropy.
And basically what entropy is going to quantify in our framework is the richness of a variable, in particular the richness of conscious experiences.

20:12 Why this is a good measure of richness is because if conscious experiences could kind of take on many possible values with equal probability, they're very kind of diverse in that sense, well, then it's something that's rich.
Some other notions that are going to be important are mutual information.
So here that's denoted by I of x and Y.
And what that denotes is how much shared information there is between two random variables.
So again, to make things concrete, x we could take to be a conscious experience, whereas Y, maybe that's a description of the experience, maybe a verbal description.

20:51 So in this case, the mutual information will be really high if the verbal description uniquely determines the experience.
So basically, another way of saying that is knowing the verbal description.
We have no more uncertainty about what experience is going on.
They perfectly determine each other.
So that would maximize the mutual information.

21:09 And in contrast, if the message told you nothing about the conscious experience and you were just as unsure as when you didn't have the message, well, then the mutual information would be zero.
This is useful because we could use it to define a notion of ineffability.
So this conditional entropy that we've written h of X, given Y is equal basically to the richness of X.
So the entropy of a conscious, of conscious experiences minus the mutual information between conscious experiences and other variables like their descriptions, that's the mutual information.
What this captures basically is how much information is lost when going from an experience X to a description Y, right?

21:56 If all the information was lost, if Y doesn't tell you anything about X, the mutual information is zero, and H of X, well, the conditional entropy will be equal to the richness of X.
If Y perfectly determined X, well, then H of X and the mutual information cancel and the conditional entropy would be zero.
So what conditional entropy describes basically is how much information is lost when moving from X.
So like a conscious experience to Y, a description of it.
And that's, that's a perfect description of what ineffability is intuitively, right?

22:31 It's how much information is is lost when I try and describe something like an experience.
Okay, so I think we have most of the background out of the way, and now we're ready to describe one main source of ineffability that arises due to attractor dynamics.
So very quickly to describe some, some variables over here that we're going to be using throughout the presentation.
If you look at that top right diagram, we're going to have X, which is basically the trajectory of neural activity that's relevant for a conscious experience.
So for instance, in Global Workspace, x would be the trajectory of the working memory state.

23:10 We're going to assume that the trajectory of neural activity produces a conscious experience.
We're going to be calling that conscious experience S throughout.
But also the trajectory importantly is going to follow attractor dynamics so they converge to states such as so how does this result in ineffability?
Well, basically the idea is that whenever you have attractor dynamics, there's a to one mapping from trajectories to attractors and this induces information loss, right.
Just knowing the attractor, we're not able to kind of go the other way around and infer what the original trajectory was.

23:48 So this conditional entropy, this ineffability of X given A is going to be high, basically.
All right, why does this matter?
Who cares if there's information lost between the trajectory of working memory and the attractors that it converges to?
Well, important thing here again is that Global Workspace postulates that for working memory content to be accessible across the brain, it needs to be amplified and maintained over a sufficient duration, so thought to be around 100 milliseconds.
So this means that working memory is going through these trajectories X, but only A, only the attractor can be reported and only the attractor could broadly affect behavior.

24:29 Only it could be written to memory, only it could be broadcast to these other processes.
So that means that the contents of working memory, kind of these transient contents in the trajectory, X are inherently fleeting.
There's rich information that was encoded in the moment, in the moment of the trajectory, but that can't later be recalled or reported because only the attractors can be recalled or reported and kind of if we zoom out and go back to our philosophical notions of ineffability.
This also explains why it's difficult to sort of catch yourself in a thought.
Right.

25:04 Working memory encodes these rich and subtle thoughts through the trajectory, but we can never quite pinpoint or report in words what those thoughts consisted of.
Were they verbal?
Were they pre verbal?
Did they consist of visual imagery?
It's really hard to say exactly.

25:19 And the reasoning would be that, well, there's just a lot of information that's lost going from these trajectories to the attractors that again we could report on or that we could recall or they could just broadly affect behavior.
So that's one huge source of ineffability arising from attractor dynamics in working memory.

25:40 Now these attractor dynamics also give a lower bound for ineffability during verbal report.
So now at the top right, I've added another variable, M.
That's basically some verbal message that you could be using to describe your experience.
And M is a function of the attractors, right.
According to global workspace, only the attractors can be reported on or used across the brain.

26:05 So this means that basically, the ineffability of an experience given a verbal message has to be at least as great as the ineffability given an attractor, because M is a function of the attractor and you can't gain information when applying a function, you can only destroy it.
But we're actually going to argue that the ineffability is not just lower bounded by the ineffability of the attractor, it's actually, in practice, quite a bit greater than that.
And the reason is that M, this message, is a discrete variable, right?
It's language, whereas A, the attractor is this really high dimensional snapshot of some cortical states.
So because of the asymmetry between the richness of these variables, there has to be information loss.

26:52 And intuitively, what's going on here is that you can think of there as being a many to one mapping from attractors to messages as well.
So for instance, if I say that I saw fat cats, that paints a picture.
But it's also leaving out significant details about the original attractor, which presumably encoded things that you were aware of, like the cat's color, size, pose, the background, all these things that you were aware of and that were encoded in the attractor.
But you can't really put into a message without it being prohibitively large.
So again, the idea here is that the ineffability of experiences given messages higher than given attractors, because the message divides the space of attractors more coarsely, it's a simpler variable, it adds additional information loss.

27:44 So one problem is, if language is so coarse and simple, why can it describe experiences at all?

27:53 And the solution is that while attractors and the message kind of both share this discrete part, right?
So the message, because language is discrete, can be used to index or identify compositional attractors.
There's this comparable richness basically between the message and the discrete part of the attractor.
Which means that in practice, the richness of the experience h of S is typically much greater than the ineffability of the experience given the message.
So that explains why we still can communicate somewhat with language, even though it's this really low dimensional simple thing.

28:33 So, to recap quickly, what we have over here is the argument that the detractor dynamics are empirically ubiquitous in neural activity across brain regions.
They've been proposed as a computational model for working memory.
And prominent models contends that conscious experience is a projection of working memory states.
And one of our key contributions is to connect these theories to argue that attractor models, working memory offer an account for the ineffability of conscious experience, because attractor dynamics induce significant information loss.
That's the general argument.

29:09 There's one quick thing to add over here.
So I've been talking about working memory a lot less about conscious experience so far.
So let's link the two.
What's going on over here is that there's many ways to link conscious experience to X to working memory, basically.
And there's kind of two main options.

29:28 So one is we could say that the instantaneous state of working memory is always conscious.
So all the states in between attractors are also consciously experienced.
And how attractors would result in ineffability.
Here is that, again, what you're able to recall, what you're able to report is just the attractor, not the actual experiences in between attractors that you were having.
But there's another possibility, which is to say, well, maybe only the attractors themselves are experienced.

29:58 However, importantly, ineffability exists regardless in this case, right?
If only A is conscious, a can still encode the fact that there's information lost during processing.
And working memory during these trajectories.
Information loss is something that is computable.
It could be encoded along some dimensions in the attractor, for instance, which explains how we could be consciously aware that there's information lost during working memory processing.

30:24 Okay.

30:26 _Xu:_

Yeah.
So now I'm going to talk about generalizing ineffability.
Once you view ineffability as information lost from a source variable to a destination variable, then there are a myriad of different pathways that you can characterize, which we're going to split into two groups.
So pathways confined within an individual or intrapersonal communication, and pathways that extend between individuals or interpersonal communication.

30:54 So in the intracase, you've already seen conscious experience, the working memory trajectory, the attractive state, and the message.
But you can also consider D, which is the input data to the system, and V, which we use to denote the state of processes considered outside the delimitation of working memory.
And you can also consider the cognitive parameters of the individual being communicated to.
So we're going to work with Alice and Bob, and we're going to assume that Bob has a brain which is structurally identical to Alice's but has different parameters phi, tilde instead of phi.
And we're going to denote Bob's cognitive state using the tilde.

31:47 So empirical evidence from neuroscience suggests that the brain is hierarchical in nature, and there are many levels of organization, many instances of active dynamics across organizational levels and cortical regions.
So one example is the inferior temporal cortex is a sensory processing area that responds discriminatively to novel sensory stimuli, whereas the prefrontal cortex, or PFC, appears to be implicated in maintaining the attention modulated representations of working memory.
And to a first approximation, in this simple model, it's easy to obtain the result that richness of one process constrains the richness of another.
So here we have that richness of working memory trajectories.
Hx is upper bounded by the richness of its inputs.

32:45 And subsequently, we also have that the richness of conscious experience, HS is upper bounded by the richness of conscious experience and the richness of subprocess states.

33:01 Now we're going to zoom out and consider the interpersonal communication case.
Shannon entropy has some drawbacks when it comes to characterizing interpersonal ineffability.
A major one is that Shannon entropy.
Assumes you have access to Phi, Alice's cognitive parameters.
So note that H phi S given m, for example, is the descriptional complexity of S given not just A, but also phi.

33:36 And since we can't assume in the interpersonal case that Bob has access to Alice's brain parameters, we're going to rely on the Kulgamarov framework for information theory.
If you're unfamiliar with the kilgomera of complexity, the first thing to note is that conglomerate complexity, or Kx, is defined on instances X, hence the lowercase rather than variables, which are noted by capitals.
Kx is roughly defined as the length in bits Lz of the shortest binary program Z that prints x and Holtz.
So there's no explicit dependency on the probability distribution over X, unlike in Shannon information.
But we can introduce PX by taking an expectation over the cogomera of complexity of state to obtain the cogomerav version of Shannon entropy.

34:36 And likewise for ineffability, we characterized it before using conditional entropy.
In the Kogamara framework, expected k of x given y is sort of the analog to shadow unconditional entropy, and that represents the length of the shortest program that prints X, given that you know Y or that y is accessible to your program.
And it's approximately equivalent up to logarithmic terms to kx minus IX, where IX colon y is kilgomer of mutual information, which can be interpreted as the difference in program length for printing X depending on if you know Y or not.
Roughly speaking, there are a lot of similarities between Shannon information and Polgamorov information.

35:37 For example, mutual information in both cases is maximized if X is equal to y in the Shannon case, because that means Y uniquely determines X, and in the Kogamarov case, because it means that given Y, you don't require any extra bits to print X.

35:57 In fact, if you assume knowledge of the probability distribution P, then expected cogmera of complexity and Shannon entropy are equivalent up to some constant factor.
Because it turns out that the most efficient way to describe a state X on average, given that, you know, the distribution, is to encode X with a description of length minus log PX.
This.
But if you don't know the distribution which we want to make use of in the interpersonal case, because the parameters of the speaker's brain are not given, then the higher the descriptive complexity of that unknown distribution, then the higher the ceiling on active inference between expected cognitive complexity and Shannon entropy.
And in our case, we'd expect that to apply because the space of cognitive states is enormous, the probability distribution over those states is very complex, and the states themselves are in general complex to reconstruct being very high dimensional vectors.

37:07 The second advantage of Kogama of complexity, in addition to allowing us to explicitly avoid conditioning on the probability distribution, is that Shannon entropy is a measure of statistical determinability of states as opposed to difference in unique states.
So in Shannon information, entropy is fully determined by the probability distribution on states, and it's unrelated to the meaning or structure or content of the states.
Whereas cogmera of complexity is concerned with the difficulty of reconstructing states I e absolute difference, which corresponds more closely to the lay definition of ineffability.

38:00 Here are a number of results that we include in the paper.
So the first one is quite simple.
You can't increase cogmerate complexity by conditioning on more states, because the program can simply choose to ignore the input if it doesn't help to shorten the length of the program.
So we have trivially that KS given m, the complexity of conscious experience given the message is at least as great as KS given m and p phi.
But you would expect this gap to be quite significant because of the complexity of p phi.

38:44 In our case, and generally in non toy cases, the probability distribution itself provides a lot of information.
So it significantly reduces the descriptive complexity of S if you're able to condition on it.
This first result illustrates essentially the difference in ineffability from the tabular raza case on the left, where you don't condition on Alice's brain parameters phi, to the case where you can assume access to Alice's brain parameters, which is analogous to the Shannon entropy characterization that Eric was talking about.
But the quantity that we're more interested in is this expression in the green box.
So K s given M and P tilde phi, which is the expected ineffability well, in expectation of Alice's experience s given the message and Bob's brain parameters tilde phi, you can show that this quantity is upper bounded by an expression that scales with KP phi given tilde phi, which is a measure of the cognitive dissimilarity or the descriptive complexity of Alice's brain given Bob's brain.

40:22 So, in other words, if your experiences are ineffable to someone I e, the left hand term in the green box is high.
That implies that your brains are highly behaviorally dissimilar under our model.

40:43 So we can use this result to provide an account for what Mary learned when she stepped out of her black and white room.
And essentially what it's saying is that neurotypical Alice's experience of color is ineffable to Mary, which implies that they are cognitively dissimilar.
And cognitive dissimilarity is not the same as knowledge inadequacy, because knowing how the brain should respond to a particular stimulus is not the same as being able to execute that response when you're actually exposed to the stimulus.
So the cognitive dissimilarity principle is something that we generally believe intuitively, but it's also been studied in neuroscience.
So the ability for the neural activity of two brains to synchronize, which is to say, to behave in a mutually determined manner, appears to facilitate communication between individuals.

41:54 There's also a connection to theory of mind, which is the skill of being able to infer the thoughts of others.
So if Bob's cognitive functions, FX and FS, which produce his working memory trajectory and his conscious experience, are optimized for decoding Alice's message m into her conscious experience s, then ineffability is reduced.
If bob's conscious experience s tilde is conditioned on compared to m because it implies that part of the computation of reconstructing s is executed during inference of tilde s meaning that the smallest program from tilde s bob's conscious.
Experience and tilde phi Bob's cognitive parameters to s.
Alice's conscious experience would make use of tilde s to reduce the sort of residual work that needs to be the residual information that needs to be supplied in order to determine s, which would shorten the descriptive length of that program.

43:15 So, in other words, making progress at inferring the conscious experience of others in your own cognitive processing could literally be interpreted as reducing the ineffability of their conscious experience.

43:33 Quickly, we're going to touch on the grounding problem.
So, as Eric mentioned before, two individuals will generally understand the same word or sentence in different ways.
And our measure of ineffability does capture this dissonance for two reasons.
And first, measures of ineffability, such as we saw in the previous slide, they are bound by a ceiling that scales with cognitive dissimilarity or the cogmera of complexity of PFI given p, tilde Phi.
And phi includes all the parameters in Alice's computational graph, including those that parameterize functions defined on the input data D.

44:16 And likewise for Bob.
So that means that Alice's parameters, phi are grounded in a representation that is at least partly shared with Bob's tilde phi.
So if Bob's parameters implement a function that operates differently on input data compared to Alice, then they do not inform on each other to a great extent and the ceiling on ineffability is increased via this KP phi given p tilde, phi tan and secondly, conscious experience s is a function of phi.
It's computed using a function that depends on phi.
And likewise for Bob and phi contains Alice's long term knowledge.

45:11 Therefore, S is capable of containing information about the assumptions that Alice makes in the process of generating her conscious experience and that's included in the reconstruction target of KS, which is to say the description or complexity of her conscious experience.

45:39 So, our model offers an interpretation for the observations of Sperling, which were made in 1960 in this very famous experiment where he showed subjects a grid of characters briefly and then asked them to recall a specific row.
He observed that subjects were generally able to report the prompted row accurately, but not all the characters in the grid, despite being able to report that they had a conscious experience of they consciously apprehended all characters in the grid.
And our model offers an account for this this phenomenon in in the following way.
So upon being exposed to the grid of characters and being prompted to report the characters in a specific row, working memory contents represented by the attractive state A presumably contains the identities of those four characters in the prompted row as well as a summary over the grid.

46:57 For example, the approximate number of characters or their agreement and an estimate of the information lost by that summary.

47:07 Whilst information sufficient to discriminate all characters would exist at some point in the computational pipeline, but primarily in upstream sensory state V from which working memory trajectory X and working memory output A are computed.
Subsequently, since the active states A is directly accessible to verbal reporting processes, the characters of the prompted row, the grid details at summary level, and the presence of information loss would be directly reportable, whereas full grid details wouldn't.
And note that this explanation would hold irrespective of where the distinction between conscious and unconscious is drawn.
So whether X the working memory trajectory, which may contain sufficient information to discriminate all characters or not, whether X is considered conscious or not.

48:18 So, as this suggests, one of the points that we make is that at least when it comes to characterizing richness and ineffability, the exact definition of what constitutes conscious experience.
So the definition of FS phi in the computational pipeline is not that important.

48:46 We utilize this minimal computational model without relying on the implementation details in order to allow us to make general statements about richness ineffability.
And as Eric hinted before, you can account for the report of the report of ineffability from this computational assuming this computational graph, irrespective of how you define FS.
So if X is considered to be conscious, then the attracted dynamics bottleneck, the amount of information accessible to working memory output and verbal report.
But if X is not conscious, then information lost during processing can still be reported on.
It can still be approximately computed and reported on, leading us to report on ineffability.

49:46 So finally, some future directions for this work.
One of them is to link it to the neuroscience.
So, for example, to actually get some empirical estimates of the amount of information lost using neural correlates of working memory state, for example.
And also, I think for a deeper understanding of consciousness, you have to consider why it exists and not just how it manifests.
So this is something that we don't touch on on the paper.

50:30 But the use of information bottlenecks in machine learning would suggest that information loss actually has a purpose.
And specifically the purpose is generalization.
It improves the robustness of functions learned from data to noise, and it improves the ambiguity of functions to perform optimally on inputs that were not seen during training, which is what generalization is defined by.

51:12 And this is important because if we want to incorporate sort of observations about consciousness into our artificial models, what we really want to capture is the benefit that consciousness affords biological models.
And we might not need to transfer the actual form that it takes in human cognition and that's it.

51:51 _Daniel:_

Awesome.
Thank you for the presentation, Kiom.
It would be awesome if you could give some opening remarks and then we can have a discussion and hear any questions from the live chat.

52:07 _Guillaume Dumas:_

Sure.
Well, thanks again for the invitation to mind jazz on these beautiful topics.

52:14 So as opening questions and discourse, I would say, like a strong message here is that through the formalization that was just presented, we have an account that allowed to make the bridge between access consciousness and phenological consciousness.
Something that was described very well in the paper that was cited of the Nakash in Philosophical Transaction B, how you don't necessarily need something more than access consciousness to account for these phenomenal aspects, but it's also a lot of open questions.
Like typically we have seen how there is an information loss within brain and between brains, but we can also complexify the within brain message passage, for instance adding metacognition.

53:19 So at mida we are also working on addition of cognitive architecture on top of global neural workspace with typically attention schema theory for Michael Garciano.
And so there is again in these meta representational steps a lot of information as well.

53:38 And I think from an empirical point of view at both behavior and neurophysiological level, there is also a lot to unpack there on how our metacognitive representation of ourselves is also impoverished information from the real states that occur underlying and that connected well with the social dimension of consciousness.
And here we tapped a bit on that with the ineffability at the interpersonal level.
But in the case of the attention schema, there is a very interesting reversal from evolutionary standpoint of why the brain comes up to represent others at first and then we are recycling the neural mechanisms to predict others behavior on ourself.

54:40 And there is a kind of flipping of the traditional narrative in cognitive neuroscience with Graziano because the others come first in a way and self consciousness become a sort of side effect of having to have all the mechanisms to deal with others.
And here we don't talk too much about the representation of the self, but I think it's a very interesting path following this work.

55:11 Then there is also something that we didn't discuss too much, but we think about the trajectory to the attractor and how many trajectories can lead to one attractor.
But interestingly, from a sequence of attractor you can recover sort of a trajectory.
So like if I have point A and point B and point C, by having the sequence IBC, I will tend to have a trajectory that looks alike each time.
And so it's kind of heading towards like the dynamics also of social interaction and culture.
So typically cultural artifacts like music or movies are eliciting stuff from a subjective experience that seems like stronger than just words, I'm saying stronger than words, but even words are sequences.

56:09 So in a way there is maybe in the dynamics of communication a little bit of information that is retrieved by the interpolation of different discrete states of different attractors.
It's in the inequality that we saw.
The inequalities are there, but maybe we can play a bit with those phenomena to see to what extent we can retrieve more information by playing on those dynamical phenomena in communication and regarding communication.
So we talked about the grounding problem and how the message and the attractors are kind of aligned between people through a shared statistical environment.
And I think the Kolmogorov framework is interesting in the sense of a generative model of the world that you have to share with others.

57:16 In a sense, I'm working a lot on autism and I'm interested in neurodiversity.

57:24 The fact that you have this dissimilarity, the cognitive dissimilarity in the information loss, is also very interesting to interpret how diversity at the biological level can have an impact on how certain people would have more difficulty to communicate with others.
Specifically in a neurotypical world.
Like, we have a society that is very normative in design for neurotypical.
And so people who are more outside the norm and are more neurodiverse would then have more difficulty to align their genetic model and communicate with others.
That's also something that would be nice to discuss or to explore later.

58:11 And finally, so since we are on an active active inference Livestream, I would take the occasion to mention how it could connect with active inference.
We didn't really talk about the active inference formalism in the paper, but typically I'm coming back from a workshop on computational neurophenology where we used the previous work of Varela on neuroscience and phenology to try to have a generative passage between first person and third person experience.
And we discussed during the whole week how computational models can be a third constraint to stabilize this relationship between first and third person perspective on consciousness.
And I was among the rare people there not completely convinced by active inference.

59:12 And I was like trying to argue about the need for plurality at the formalism level, even from a theoretical perspective and for plurality in those domain, but at least from a formal point of view, to try to not bet all our eggs in the same basket, so to say.

59:35 And here it's a very nice example how even you can combine formalism that were mutually exclusive in the literature.
So for typically coming more from the embodied cognition and variables work, people with embodied cognition work tends to be more in dynamical system theory and very opposed to computationalism and information theory.
Here we show in this paper that information theory and dynamical system theory can totally work hand in hand.
So it doesn't mean that we need to commit to one or to have all formalism.
But to maintain this plurality, I think is very important from an epistemological standpoint and still the connection with active inference, that could be interesting.

1:00:21 And that's one of the things that I kept from last week workshop, is how from a social interaction point of view synchronization.
And I worked a lot on intervention synchronization and those phenomenal synchronization can be optimality for information transfer, as we see here.
But in the context of active inference, it's also the optimal minimizer of free energy because you have the two generative models that are perfectly aligned and so you don't have error in your prediction because the other person become a mirror of your own generative model.
So that may be also some bridges and predictions that can show that those different formattems are multiple way of looking at the same thing.

1:01:18 _Daniel:_

Thank you.
Awesome points.
So feel free to discuss if you have any responses and just take it from there.
Eric and shoe.
Or I can ask some questions or read some comments.

1:01:33 Do you have any comments on Guillum's thoughts?

1:01:39 _Xu:_

Yeah, I think we have some.
Do you have things to say?

1:01:42 _Eric:_

Go first.

1:01:44 _Xu:_

Yeah, that was a long list of comments.

1:01:51 I find your comments about the autism link really interesting because actually that's pretty much directly what the message of the result is, is that cognitive dissimilarity is associated with difficulty in communicating.
So yeah, actually the last thing that you said about how if the communicator and the listener's brains are synchronized or if they're equal, there's no prediction error, that's kind of the machine learning problem, actually, as a whole.
I don't know if this is a big thing, but the whole point of machine learning is to discover the true model that you're trying to learn so that you have no prediction error.

1:02:53 Right?

1:02:56 So, yeah, I dean, so I'm not an expert on active inference by any means.

1:03:09 But one thing that does make me a bit like apprehensive about it is that it's so concerned with prediction.

1:03:22 Generative models are about reconstruction and prediction, whereas cognition is about survival, and prediction is part of survival.
Obviously.
I mean, you need to be able to predict, I don't know, not crashing into a car or something so that you don't die, but it's just a part.

1:03:59 And more generally, the inference of cognitive states in the brain is not about discovery of truth in some sense, you know, it's not about coming up with with true model or explanation for some phenomenon.
It's about sort of optimizing for your fitness.
So, yeah, that's something that I don't quite understand, sort of what the active inference perspective on that would be.
I don't know if Daniel, you had some comments or not.

1:04:54 _Daniel:_

Okay, just jumping with active inference and then I'll give more comments in the chat.

1:04:59 But I think that's a great set of points.
So if I can make one point to Guillaumes first.
You spoke about in the presentation the generalized ineffability, and it reminded me of a few times in active inference where we're hearing about generalized synchrony, generalized, which means like, not necessarily lockstep or mirror, but mutually information encoding and not necessarily linearly correlate and synchronize, like the end state of the metronomes.
But there's like complex information transfer, especially in this multi scale setting, generalized synchrony, which is enabled by the generalized coordinates, which are the coordinates of motion of the path.
So these are kind of the summary statistics to describe the Taylor series expansion around that path or to better describe that path taken in some way.

1:05:55 And generalized homeostasis, which for certain environmental regularities it may be sufficient to be entirely retrodictive or there may be physical or cyberphysical constraints so that you'll have a system that is purely designed a different way.
So I wouldn't say any theory is necessarily too opinionated with respect to what you could describe.
And I think part of the reason to want such a descriptive approach, which is what I feel like you all did, by deciding to describe an analytics framework for ineffability rather than, for example, a mechanistic explanation, but describing some evidence.
All of that was just to say pluralism in what we're approaching that ineffable space from multiple compressions or bowls to even describe English words, scientific models.
And it reminds me of the recent discussions with Lance Acosta who described how other discrepancy measures other than free energy could be used and that free energy has been used in machine learning.

1:07:07 The variational auto encoders all kinds of Bayesian applications because it has a KL divergence and so it has some convenient variational optimization properties as a discrepancy measure, but it is not the only discrepancy measure.
And you mentioned two in your discussion, which were the Shannon syntactic sort of classical information content and then the Colemagorov, the program.
And so that is like another distance measure.
So in some ways these spaces can't or won't or don't even need to collapse below pluralism of at least several relatively stabilized kinds.
But I thought that was a very important point, Guillaume, about explanatory pluralism and how we can be excited about one area of science or one way of knowing and it's compatible with others ways of knowing because we have some of those properties of differences that were discussed.

1:08:16 So those are first thoughts before even any active technicality.

1:08:27 _Guillaume:_

Go for it.

1:08:28 _Eric:_

Sure.

1:08:29 _Xu:_

No, I just want to remark that KL is distance between two distributions.
Yeah, anyway.

1:08:42 _Guillaume:_

Yeah, I was just saying in the case of the autism, this typically show how also you don't necessarily need to go to the mechanistic neurobiology to have potential explanation.

1:09:00 And so in the case of Crabber for explaining the brain, there's a very nice definition, very nice mindscape of different kind of explanation and in the same way those different formalism can give different perspective on how to understand what's going on.
Autism has been very focused on the neurobiology at some point and the genetics, but maybe it's not at that level specifically that the functional understanding should occur.
I don't say it has a no causal relationship because it's highly genetically irritable and so on, but sometimes the functional understanding is not necessarily at the very lowest level of explanation.

1:10:00 _Daniel:_

So now, to kind of move to active imprints and really physics based approaches, the trajectory recovery is going to have some maximum information representation with the generalized coordinates of motion.
It's how paths are represented in many settings.
And so that path of least action, the Bayesian mechanics on that mindscape, whatever it is, empirically, it's like fitting a spline in that space or doing some other kind of modeling.
Whether it's SPM modeling or hyper scanning, there's some kind of generalized time series modeling between the present and artifacts, the past, the future, other entities.

1:10:56 _Guillaume:_

What do you mean, Daniel?
I didn't get it.

1:10:59 _Daniel:_

Just that that kind of trajectory recovery is what is being parameterized in physics of consciousness type models or physics of cognition.
Bayesian physics, anything where a probability distribution has a position, velocity, acceleration, and so on, it's being path inferred continuous time generative models, and there's discrete time generative models in activ and hybrid models, just like other Bayesian graphs.
So in the continuous time setting where there's a Taylor series expansion, that's trajectory recovery.

1:11:44 _Xu:_

Yeah, well, I think more generally, maybe the point is that you could use Bayesian learning variational inference to learn a generative model of these states that we're referring to.
Right.
If you had some kind of data set that actually represents a sample from, let's say, the True model, then you could use variational inference to approximate that model.

1:12:21 You don't have to, though.
I mean, there are many generative model techniques in machine learning that don't fall under variational inference.

1:12:33 _Daniel:_

I'll read a comment and a question.
So Yashua Bengio writes Guillaume Dumas idea about trajectories of consecutive attractors to recover information about likely trajectories that lead into each of these attractors that are normally lost in working memory is very cool.
And then shu.
Eric, any relation between what you talked about and the compositional properties of conscious thoughts?

1:13:00 _Eric:_

Yeah, I think so.

1:13:02 In terms of compositionality of conscious thoughts, I think what Yasha is referring to now is that our thoughts kind of compose concepts that we already have.
So it's something like a sentence.
If I think the fat cat, I'm composing these mental concepts of fat and cat, and that generates sort of a new experience.
So experiences are always generated from these building blocks.
And then, similarly, one thing that we didn't talk so much about is that conscious experiences, language and attractors, can also have this shared compositional structure.

1:13:39 So, like language, it's clear base based words combined to form new little phrases, new sentences that have novel meaning in a systematic way.
How this could happen with attractors is, well, kind of in the most basic case, different dimensions in this high dimensional state space might converge to different attractors.
And so now one attractor that's converged to is really a composition of attractors along different dimensions.
So this is a sense in which our experiences are compositional.
Our attractors that generate those experiences can have compositional structure.

1:14:18 And this could be a reason why language itself is compositional.
We're basically trying to come up with some way of describing or identifying compositions of attractors.

1:14:29 _Xu:_

I mean, I would add that compositionality is a mechanism for reducing descriptional complexity.

1:14:42 In fact, that's arguably the objective for the compositional nature of our thoughts and language features.
Like less time to describe, more robustness to noise.

1:15:00 Yeah, I mean, if you're trying to describe an instance of a state, obviously the descriptional complexity is much less if it's built up of concepts that you already know about.

1:15:15 _Eric:_

Yeah, just to bring this back to something I mentioned in the talk, I pointed out that attractors have this discrete structure.
There's a finite number of them, and we could assign labels to them.
But if these attractors are compositional, which would allow for a richer space, richer number of attractors, basically it's finite.
But the space of total attractors is exponentially large.
So we don't want a Lagrange that's assigning one unique word to every composition of attractors.

1:15:42 It would be an exponentially large language.
We want some kind of language that will minimize the description, like what Shu said, you could have a language that's compositional.

1:15:57 _Daniel:_

Yeah, I think that provides a really.

1:16:00 _Eric:_

I think you're muted Daniel.

1:16:03 _Daniel:_

Sorry.
It provides a very interesting and justifying rationale for using the description length as opposed to the Kale divergence, which is maybe in some telepathy enabled world or space.
The KL divergence does help you move quickly or on some defined manifold.

1:16:30 But in encoding decoding space and on the computers that we have, then writing shorter programs and or making smaller information, theoretic compressions becomes one of the imperatives to take the kind of empirical approach that you are describing.
Because though you've described mainly equations, these are all also computer packages that can be used to model different data sets.
So what kinds of data sets do you think this is most proximally applicable to?

1:17:24 _Eric:_

Yeah.
Are you saying like, what kind of data sets would kind of minimum description length computational models be most useful for.

1:17:34 _Daniel:_

Or just with the approaches and measures that you described today?
What kinds of data sets or behavioral and cognitive settings do you think that could be used as an empirical tool or measure for?
I think it'd be really interesting to hear about does the data already exist?

1:17:53 Is it some hypothetical measurement?
Are there ways to even reanalyze?
Yes.
Guillaume or anyone else?

1:18:03 _Guillaume:_

Yeah, I think on language already there is a lot of things that have been done on the number of bytes per second transferred, for instance, and I guess on large corpus of discussions or even in clinical settings.
For instance, I'm working on the clinical alliance between a patient and a clinician, for instance.
This formalism of ineffability and information loss would be interesting to apply to as even a form of biomarker.
I mean.
Even if at the language level, it's not bio.

1:18:48 And then you can also apply those information theoretic measurements to physiological data, movement, neural data.
So in my lab, we are recording multiple brains simultaneously.
We can totally try to empirically approach what we are describing this paper and show that, for instance, in certain population that are more challenged to communicate through neurodiversity.
So what we discussed earlier, we can apply the same type of measurements with information theory instead of just classical neuroimaging measurements.
So that would be, for instance, empirical way of dealing with that.

1:19:35 What I'm very interested in would be to make the relationship between the access consciousness and the V basically process and the information loss that you have in your working memory.
Right now, I feel that no imaging technology are not at that level of possibility.
But who knows?
Maybe we're going to have soon the ability to disentangle that kind of stuff.

1:20:05 _Xu:_

Oh, yes, the delimitation of what constitutes working memory in the brain.

1:20:16 I think that's not a settled question, right?
I mean, there are lots of different possible approaches.

1:20:31 _Eric:_

Yeah, I mean, it's totally up in the air.
Classically, in global workspace theory, they traditionally thought, okay, working memory is localized to prefrontal cortex.
Now, the new perspective that's emerging that maybe working memory is sort of distributed across the brain, we see kind of sustained attractor representations all over the place from this distributed working memory.
So all these different pieces, what constitutes x?
What constitutes that working memory trajectory?

1:21:02 And also what constitutes the experience?
What's the function that goes from x from working memory to an experience?
All that is up in the air.
When writing this paper, we had plenty of discussions about what is the trajectory?
The whole trajectory conscious is just the attractor conscious is there kind of a sense in which both these things are true.

1:21:22 So, like, Guillaume was talking about access versus phenomenal consciousness.
Access consciousness refers to what I'm able to report, whereas phenomenal consciousness kind of refers more to the standard definition of what is my experience like.
So our framework kind of illustrates that maybe we could unify these things where x the trajectory is some phenomenal, experience it's in the moment, whereas your tractor is really the only thing you're able to report, remember?
And you must still know that something is missing between what you're reporting and what you were actually experiencing throughout.

1:22:05 _Xu:_

Yeah, in terms of our model, it's pretty clear, but I think actually grounding it in empirical data sets is a challenging question.
The other thing is that colgomer of complexity is more of a theoretical measure.
So that that's actually, I think, the reason why Shannon information is much more ubiquitous, for example, in machine learning, because basically, given a generative model, you can approximate it, for example, just using Monte Carlo estimation.
But Kogamov complexity yeah, it would be much more of an approximation with a much greater error.

1:23:06 I think if you attempted to approximate that.

1:23:13 So I guess that would be a potential concern.

1:23:15 _Eric:_

Yeah.
One advantage of it, if you could measure the Call Margaret complexity is it would allow you to kind of measure the ineffability of an experience on an individual case.
So, for instance, one thing we spoke about with theory of mind was that this complexity of the experience, given the message, we would think it would be much higher than an experience given Bob's experience given the listener's experience.
Because the listener's brain is doing a lot of the work of decoding the message into a similar sort of experience.

1:23:47 So it'd be useful if you could see something like are there certain types of experiences where the message is wildly insufficient?
The comagraph complexity of the experience given the message is massive.
But actually people do a really good job inferring the experience and maybe it would be different in a case of, like, autism.
Maybe there's some sorts of experiences that they simply can't reconstruct.
So I think there's some value in trying to create measures of Kalmakov complexity to kind of handle these individual cases.

1:24:17 The issue is it's not really computable.
You can't search through the space of all possible programs.
But maybe there are kind of ways to get around this.
For instance, you could sort of parameterize a program with, I don't know, a neural network.
Let's say you have a neural network going from message to some brain scan for an experience and then maybe the size of that neural network or the complexity of the network could be sort of a surrogate for the complexity of the program.

1:24:45 The shortest program.

1:24:47 _Xu:_

Yeah.

1:24:49 _Guillaume:_

That'S a cool idea.

1:24:52 _Daniel:_

That is really cool.
It reminds me of using adversarial neural networks which don't have as strong analytical guarantees as, for example, cryptography.

1:25:07 But then they kind of converge in being able to protect or change or modify information in certain ways.
But you aren't getting the same bounds or guarantees on the formality.
And that's kind of like the discrete continuous dialectic.
And so it's important to embody even that pluralism with respect to state spaces because if the formalisms in any of these domains, the formalism for discrete continuous, they're not always aligned.
And those are definitely the areas that can be studied.

1:25:45 But for the space of empirical models that we're talking about as part of even then methodological pluralism and science.
But if we're talking about statistical models, we want to be able to intake the data at some point.
So it has to have certain properties which are even looser than the math.
And there's probably a lot that could fit in this.
And I think it'll be interesting.

1:26:11 Like when you have a hyper scanning experiment, how do you include the environment or how do you deal with different number of sensors or different types of sensors, different kinds of action, and report that people might encode their symbols through all kinds of accessibility and interface types which I think returns to Guillaume's point.
So yes, please.

1:26:44 _Guillaume:_

Actually that also reminds me that there is also a nice empirical playground associated with what we discussed is how we can maximize from an environmental perspective instead of the biological perspective this information transfer.
So I'm working for instance with Michael Lipsheet which is part of Earliest as well from anthropological standpoint, humans came out with rituals or cultural practice to maximize the alignments of people and those things also are very important in our society or to reach consensus and collaborate and so on.
And I guess this can also of issue would be very important, I mean when we have to converge on optimal collective dynamics.

1:27:45 Here we are talking with Alice and Bob in a diadic scale but a nice follow up also on this work will be at the group level, how you optimize consensus and collaboration on group scales strictly for taxing climate change or social inequality and very challenging topics of society.

1:28:09 _Xu:_

Yeah, so actually that touches on a well, possibly weakness of the simple model that we use which is that we don't incorporate any feedback loops.
So we have this very simple unidirectional model which I think has advantages as well because it sort of shows basic principles in a relatively easy to understand way.
But you're right in that realistically there's always feedback not just at the interpersonal level but obviously within the brain working memory is top down attention actually.
So that's something that we didn't address.

1:29:04 _Eric:_

Yeah, it would be really interesting to sort of unify our work with the field of pragmatics which is exactly about this.
It's like given many back and forth steps in dialogue, how do people come to a consensus?
And this could also kind of involve the active inference framework where as a listener I'm going to ask questions that are going to try and reduce my uncertainty about the speaker's state as much as possible.

1:29:32 _Daniel:_

Awesome, thank you for these comments.
So in my experience, computer scientists and those who have empirical data measurement experience, they know that you can have different kinds of behavioral measurements or just columns in a database.
You could have heart rate and you can have video data and you kind of have this like open ended it doesn't need to be just a matrix that gets multiplied in this extremely clean way.
And I feel like that leads to a lot of these very open ended and flexible approaches which, on one hand address the different forms and functions and settings that these kinds of questions are asked and at the same time are working, if not to address, at least to have continuity with classical discussions on a wide range of topics like sequence.

1:30:43 _Eric:_

Yeah, the question of not everything is a vector, not everything is a matrix.
You could have more complicated data structures.
That's really interesting and I think relevance to consciousness.
So it certainly seems like our thoughts, our experiences have this sort of symbolic structure in a way you can kind of think of them as like any thought as sort of a graph.
I have a couple of concepts in mind maybe in working memory and I have some idea of how they relate to each other.

1:31:16 If it's not a graph, it's something like that, maybe some kind of smooth representation of a graph.
On the other hand, when you just look at the brain all you see is neurons, all you see is distributed high dimensional neural activity.
So there's this really interesting question of how you link them together and I think attractor dynamics are another interesting avenue for getting there again, you kind of get a lot of things, you get these high dimensional continuous states that you could represent you get sort of discrete states that you could represent and they could compose together.
Yeah, I think there's something there.

1:32:01 _Guillaume:_

To.

1:32:01 _Daniel:_

Kind of extend that point to this very meta science area of discussion around pluralism in science that Guillaume opened the box on when practice in the behavioral lab, if not much more broadly, is using structures that have different column types than certain kinds.
Markov decision that might have been taken to be in principle or like arguments for the superiority, even contextually of one framework.
Those are just unveiled purely methodologically as modeler degrees of freedom.
Like whether you use a generative model that's continuous time or discrete time, continuous state space.

1:32:53 Discrete state space, the thermometer data, how you discretized it, where you put the thermometer all these broader factors that kind of instantiate the experiment and the pipeline.
They're just all embodied and cultured niche events in a scientific niche, in a social niche.
And that's a very pragmatic or people might use other words or like realist or I don't know what adjective would describe that take on starting with the scientific community and formal modeling and the modeling process as its own behavior object and then working to have the empirical practice more general, like leading the generality open endedness with practice.
Though that raises so many second order questions as well.

1:33:58 _Guillaume:_

Yeah, well, we can have also from a very pragmatic standpoint we need to have reproducibility so to have those norms in design of experiment and format tools makes sense but we need to just remind ourselves often that they also constrain our way of thinking.
And typically the history of science show us how mathematics is guided by the problems that we have to solve and speaker.
If we take quantum mechanics it was not like the formalism was popped out at first and then quantum physicists use it.
It was a generative process and a collaborative effort between mathematicians and physicists and interestingly they come up even with two different formalism that were shown to be compatible later on.

1:34:59 So it's a nice tales in a way showing how you can have even a stronger inter subjective consensus by adopting different formalisms that then later on are shown to be compatible and equivalent.

1:35:19 I have, unfortunately, to leave at some point to pick up my daughter, but we can go into category theory and more meta mathematics to try to show that those format in the end are potentially equivalent.
But from a history of science, I think it's not just about the equivalent.
It's also to have different viewpoints that confirm each other to make.

1:35:50 _Daniel:_

Our model.

1:35:50 _Guillaume:_

Of the world intersubjectively stable.
So to say, yeah, I'll give you.

1:35:58 _Daniel:_

A small short closing comment, Yom, and then we'll talk a little bit more.
Shoe and Eric, when I first saw some of your figures for hyper scanning, and there were nodes that were being connected with different edges that were within and among brains, and there was this one part dimension of my experience that was like, you can't do that.

1:36:22 They're not connected, but it's a statistical causal graph.
So they are exactly the same type of explanation and empirical data structure.
It's the same exact mutual information, linear causation, whatever you want to do in edges and edge in that representation.
And that's the map territory situation.
They're not the ones that are touching.

1:36:44 And it was just like by seeing two levels and the way that the representation could be used, it was approved by example what it meant at one level.

1:36:57 _Guillaume:_

Yeah, it was hard to publish at first because I think of that reason.

1:37:07 _Daniel:_

Thank you.
Farewell, Guill.

1:37:09 _Guillaume:_

Yeah, thanks again for the invitation.
Take care.

1:37:18 _Daniel:_

So what direction would you like to go?
Or I can read another comment or anyone else in the live chat in our last minute.
Okay, let's kind of read last comment from Yasha wrote, but these attractors presumably correspond to different concepts in the same sentence, are not independently sampled.
Sorry, it's not like verbatim, but what are these structures in language in terms of I thought that was a very memorable thing to say, that words are sequences, too.
It's like they're modular with respect to the dictionary, but then even the phonemes or the writing structures have their own compositional logic, like a periodic table, and then there's sub logics, and then there's just different uses of different levels of description, which is why we don't speak the same language unless we do.

1:38:25 _Eric:_

Yeah, well, directly, I think what Yasha is referring to is like when you sample a sentence, I guess, clearly these are their own discrete things, but you're not going to be sampling them independently from each other.
It's like different words will cohere more or less, and also they'll cohere more or less.
Given a context, you want to form some kind of sentence that describes some context or some observations.
So, yeah, in regards to these compositional attractors, again, the simple picture where you have different attractors converging along different dimensions, obviously these attractors are going to affect the convergence of others.
Right?

1:39:02 So it's not like everything is just moving independently along different dimensions.

1:39:07 _Xu:_

Yeah, I mean, simplifying assumption that we make in our simple computational model used in the paper is that we hide sort of dependencies as noise in the variables to avoid needing to consider these links explicitly to sort of highlight the main points about richness and affordability that we wanted to make.
But I really liked your point, Daniel, about how there is sort of the data, there's the physical reality and then there's the compositional structure that is sort of imposed on that.
I mean, it's a model, right?
So it's a modeling assumption that you make and you have to choose at what level of abstraction to define that model and it can feel a bit arbitrary.

1:40:18 _Eric:_

And then you also discussed kind of well, we all speak different languages.
Yeah.
An interesting question for that in our work is would that imply that we have different attractor structures across different cultures that have different languages?
Is there an interaction there or are these just these different languages equivalent ways of describing the same state of attractors?
And I think it's somewhere in the middle, regardless of what language we all have, I think similar concepts and similar conscious experiences.

1:40:56 But there's some kind of cases where you have a word in a given language that maybe identifies sort of a fundamental attractor and that's kind of like part of their conscious vocabulary, I guess.
Whereas regardless of what language we speak, we'd be able to get in that conscious state ourselves.
But maybe given our language like the attractors that you would need to compose to construct this conscious state would be a bit more complicated.
You'd need something like a longer sentence, a longer thought to have the same sort of experience.

1:41:37 _Daniel:_

Awesome.
Well, one thing that brought to mind was neural patches on the skin.
Like different parts of the body have different density of sensory types from very fine scale touch and action to some more broader patches like where two needles you can't determine the difference between them.
And then that relates to many areas to kind of development of taste and differentiability being able to determine differences.
And then you, of course, use this very evocative but also grounded dual representation of the samples that are discrete and may have compositional structure with a path that's moving through them and seeking to embed the topology of the sample points within an information geometry, which is the kind that are actual statistics input.

1:42:46 And then the neural patches are regions where to one person it's like, yeah, I drove through New Mexico and to the other person it's like every inch, they're having this rich experience.
They know the different stops.
And then I think one last great point from the presentation was that we could kind of I'm not exactly sure I said, but emulate this informational characteristic and maybe not even have the embodiment for that to even have consciousness.
Of course, that'll be the debate then.
But the debate used to be much less sophisticated than that.

1:43:33 And also people took principled stances.

1:43:40 _Eric:_

Yeah, I wasn't totally clear on that last point that you made.

1:43:47 _Daniel:_

Principled stances on whether this would be emulating or simulating or approximating analytical framework for consciousness, or whether this by implementing that machine, that it would be implementing consciousness versus the kind of linear regression package that does cognitive modeling that could be understood in a purely SPM like framework.
And SPM doesn't take a package perspective, except maybe implicitly on whether SPM models generate consciousness.
Most likely it's easy to say no because of generalized linear models.
So some people may take an in principle stance that any description or simulation, in certain ways, it's all good.

1:44:41 We're definitely not generating anything conscious.
It just would purely be a hugely energetically, expensive, potentially statistics exercise, which is fine.

1:44:56 _Xu:_

Yeah.

1:44:59 The chain of reasoning of our work, I suppose, is that if you assume a certain model of consciousness, then that implies ineffability as it is understood by information loss.
But obviously information loss does not apply, does not imply consciousness, even though it's an attribute of how consciousness manifests in humans.

1:45:31 So yeah, I mean, this question of what is the necessary desidorata to declare whether a system is conscious or not is not what we discuss in the paper at all.
I mean, from my perspective as a machine learning practitioner, it's closer to what I said in the last slide.
I would like to get the benefits of consciousness in an artificial model.
And it doesn't matter so much whether the form that takes is similar to how it manifests in biological systems or not.
Why should it?

1:46:23 You know, I mean, we don't have the kind of resources that evolution has had over over a billion years to optimize for this model.
So the question is, how do we design systems that can benefit from, for example, the generalization and robustness properties that being very contractive in processing can give you, rather than what's the exact definition of consciousness and how do we replicate that inner machines?
Because that to me is sort of a very superficial well, it's a more superficial problem in that it's looking at the how and not the why.

1:47:12 _Eric:_

And yeah, I have some thoughts on this.
Also, jonathan Simon, who's a co author on our work, he gave a really interesting presentation recently that I heard, which is, whatever model of consciousness you assume, let's say global workspace theory, there's a minimal model of it that you could construct.
We could easily construct some kind of model.
Like, to make this really concrete, there's a bunch of mini neural networks that are the sub processes and they're communicating through some shared Rnn, let's say.
So you can construct a minimal model like this, train it on some task, and then if your viewpoint was that a global workspace theory with such and such properties is what generates consciousness, well, then you'd be forced to say that your minimal model is conscious.

1:48:02 And this is in a way, I guess, not problematic, but sort of counterintuitive because the model could be doing really simple things.
It could not even be reporting that it's having any consciousness at all.
It might not even have language.
It might just be doing something like solving mnist in a global workspace type architecture.
Do you really want to say that that thing is conscious?

1:48:27 Yeah, it is a problem, I think, with most theories of consciousness.
Maybe one kind of exception in my view is theories that say we basically have a representation that we're conscious.
So one canonical example, I guess, is Michael Graciano's attention schema theory which basically says our brain constructs a model of what attention is doing in the brain.
And that model basically just describes something that is like experience.
It describes, oh, I'm aware of these things, they have these properties, I could report that I'm experiencing these things.

1:49:11 It's basically a representation, a set of neural activity in the brain.
And there you don't have the same problem where you can construct a minimal model because presumably this representation of consciousness is really complex.
And then I guess another set of theories would say that even if you emulate whatever processes in the brain we think generate consciousness, the physical implementation might be really important over here.
So the example that comes to mind is IIT, which would say it's basically substrate dependent in the sense that you could have the exact same function, the exact same mechanism implemented in different ways, like on a computer processor or a neuromorphic hardware.
And in one case there may or may not be consciousness, whereas you have the exact same function in another substrate and yeah, it is conscious.

1:50:05 So that's, I guess, another class of theories that would say that emulation does not necessarily imply that you're actually generating consciousness.

1:50:18 _Daniel:_

In our last 2 minutes, what are your closing thoughts or next directions exhortations to the humans and language models?

1:50:31 _Eric:_

Yeah, well, I guess I'm interested in this stuff a lot from a purely philosophical perspective.
So the hard problem for me is really salience of why would any physical mechanisms generate consciousness?
And the nice thing, at least for me about this work, the most satisfying part of it was that I initially had this intuition that experiences what the color red is.
It's not just information, it's kind of underdetermined there's something more than just information because I can't do things like describe it.
But now we have a theory that kind of breaks that intuition.

1:51:16 And now I have a satisfying explanation, I feel, for why I can't describe my experiences but under a physicalist framework.
So I think it'd be interesting to reason through some other of the thought experiments that make the hard problem salient and kind of develop some models that kind of break the intuitions.
For the hard problem in my case at least, I've seen it done in this scenario with the topic of ineffability.
So there's no reason in principle that it can't be done across other aspects of the hard problem.

1:51:51 _Xu:_

Yeah.

1:51:52 So I think if I were to sum up the work in one very high level sentence, it's that, well, reasoning subjectively about subjectivity is very difficult, but reasoning objectively about subjectivity is easier.
And that's sort of what we do in the paper because we take an objective standpoint and we try to formalize or characterize subjectivity from that standpoint.

1:52:34 That sort of makes the picture clearer.

1:52:40 From my perspective, I'm interested in consciousness mainly in terms of what it offers what it brings in terms of, for example, improving generalization of artificial learned models.

1:53:05 Yeah, it's interesting because another work that I'm doing is formalizing generalization bounds for information bottleneck, which is a regularization principle used in machine learning.
So it's just really interesting how evolution has sort of discovered by itself this this regularizer principle that that that it applies to to human cognition that we can also show mathematically, actually does improve guarantees on on generalization.
That that is really mind blowing to me.

1:53:59 _Daniel:_

Wow.
Great presentation.
So thank you both for joining you're welcome back anytime.

1:54:09 _Eric:_

Thanks so much, Daniel.
It was a lot of fun.
