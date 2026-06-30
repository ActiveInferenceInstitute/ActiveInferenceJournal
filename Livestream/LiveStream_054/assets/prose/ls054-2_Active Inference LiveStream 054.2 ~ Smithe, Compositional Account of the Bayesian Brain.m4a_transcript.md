
00:06 _Daniel:_
Hello and welcome.
It's June 15, 2023.
We're in active Livestream.
54.2.
So welcome to the active institute.
We're a participatory online institute that is communicating, learning, and practicing applied active inference.
You can find us at the links here.
This is a recorded and an arch Live Livestream, so please provide feedback so we can improve our work.
All backgrounds and perspectives are welcome and we'll follow video etiquette for Live Streams.
Head over to activeinference.org to learn more about participating in Live Streams and other projects.
All right, we're in Live stream 54.2.
Continuing with our third discussion on the work, mathematical foundations for a compositional account of the Bayesian brain, we're back with Dean Ali and Toby.
So if each want to say hello and anything to begin with otherwise, Ali has some questions ready and we have some questions that people have submitted in the meantime as well.
So shall we just proceed to the questions as we have the same people as dot one?
Great.
Okay, I'm going to jump into some of the presubmitted questions.
So would it be correct to call equation 4.2 compositional Bayes theorem, which is or are Bayes's theorem categorically?
And we have the document ready or anything that you want to share, but what does it mean for Bayes theorem to be categorified?
And where is that in the dissertation?

01:55 _Toby:_
Yeah, okay, so that's a nice question.
I would say that equation 4.2 is like a sort of basic is like a sort of it's like a basic representation of the product law of probability theory.
And so I wouldn't say it's particularly inherently compositional.
It's just something that is just like an axiom that is just like a consequence of the sort of standard axioms of probability theory.
The thing that makes it a little bit different from the way that it's normally written in probability theory is that I've kind of annotated those P symbols which represent the probability of a certain event.
I've annotated them each with a subscript, and that subscript represents where the probability is coming from or the probability according to whom.
That's kind of how you can think of it.
And so normally I find this kind of like P notation to be a little bit confusing because people often write P of B given A, and they also write like P of X given Y or like P of W comma a comma z.
And so in each of those cases, the sort of content of the P is kind of different.
Like the A and the B might be events of a different kind to X and Y, and yet they're all put into this P symbol, whereas in this case, with the annotations, it says, like, as I say, it says according to what?
And so here the little subscript C represents what's typically called in compositional probability theory like a channel or a kernel.
But that is like a kind of abstract way of just saying conditional probability distribution.
And so the little C means it's a conditional probability distribution from space X to Y, a space Y.
And here I'm thinking of the B as being an event of type Y and A as being an event of type A, sorry, of type x.
And so the PC says it's the probability of the event B of type Y given the event A of type x.
And so that means that when you plug these kind of flows of information together, you make sure the types match.
It's kind of like working with a strongly typed programming language.
So that type information is like the main thing that's different between this and the standard product rule of probability and it's from that product rule of probability theory that you can just write down Bayes theorem, which is the equation 4.3.
I would say that the reason why I slightly hesitate to call equation 4.3 like a sort of abstract or categorical version of Bayes theorem, even though it's annotated by these channels, is because you have this division.
And that division isn't something that's well defined in all categories, in all situations that you might want to consider probability theory.
For instance, you might have this P of C dot pi thing and that means the kind of Y marginal of the joint distribution or it's otherwise known as the push forward of the distribution pi through the channel C.
That thing might have what's known as measure zero, which means the probability might be zero.
And so the division isn't very well defined and so that expression doesn't always make sense.
Now the thing that does always make sense on the other hand is that just product law equation which tells you how the two ways you can write down this joint distribution.
So if you have a joint distribution like on the space x times y, I've written it there, then you can decompose it into a prior on x and a channel from x to y.
So that then if you put the information from the prior through the channel you get the marginal on y and that's that push forward thing.
Or you could write the joint distribution as a prior on Y and a conditional distribution from Y to x.
And the thing is, obviously we're talking about the same joint distribution in both cases.
So those two decompositions, they're sometimes called disintegrations, those two disintegrations need to be equal and that's what that equation is saying.
So that's kind of because it doesn't have this division in it and because Bayes'law follows from it and because it's something you can write down in all settings, it's kind of more fundamental.
But I quite like the kind of string diagrammatic form of it which is something that is drawn.
It's not my invention.
I think I originally saw it in a paper by Bart Jakobs and I think his student at the time, Kenta Cho.
So in, let's see equation 4.5 so that's section 4.1.2 on abstract Bayesian inversion.
So yeah, if you scroll down a little, it's on like page 130 or 130 in my version, which might be hopefully around the same place in your version.
Yeah, a little further.
Oh man, no, maybe not.
Let me get up the version on because I've realized I've opened the wrong version.
Meanwhile, see it so so the the thing I'm going for here is the sort of, as I say, the string diagrammatic depiction.
Yes.
4.1.2, it's page 120.
Sorry about that.
Yeah, so it kind of shows you how the information flows.
And so this makes the two processes quite explicit.
So here on the left, the prior of the joint distribution is pi.
And then you take the sort of probability, the information from pi and you copy it and you keep one of the copies and that gives you your X marginal.
And then you feed the other one through the likelihood or the conditional channel C, and that gives you the other marginal.
And so if you throw away this X information, you get the Y marginal.
And that's what marginalization is.
And that's why the Y marginal, if you look on the right hand side, the prior is C after pi, that's the Y marginal.
So this is like depicting that Product Law.
And then you say you can call something a Bayesian inversion of C with respect to the prior pi if it is something that can go in the box on the right hand side where I've written C dagger pi.
And the reason I've used this dagger symbol is because under certain technical conditions, this Bayesian inversion thing gives you what's known in category theory as a dagger function.
And that's something that swaps the direction of a morphism.
And so here you've taken the thing that goes from X to Y and you've swapped it and it goes from Y to X, but it depends on the prior.
And so I've written this little subscript and so for me, this picture.
It's
kind of equivalent to that Product Law equation 4.2.
But I think although it's a kind of new kind of language, I think it's a kind of more intuitive one because you can sort of see how the information flows through the system.
Sorry, that was a bit of a long answer, but I think that's how I think of it.

11:05 _Daniel:_
Great.
Okay, next question.
Could be a short one.
I'm mostly wondering about how chapter six will be rewritten.
Will it be major?
And when we promise we didn't write this question primarily to select the best policy as to where to direct my regime of attention?
Like, should I wait to dig deeper into chapter six until the updated observations arrive?
Is reflecting deeply up until chapter five where I should focus for now?
Or is chapter six something that won't change too much?
And I can still explore that next week.

11:42 _Toby:_
So this is a great question.
And I'm sorry that the rewritten version isn't online yet, but it is really close, I promise.
And I am kind of aiming for it to be done like next week or maybe let's not hold myself hostage to fortune.
So let's call it the next couple of weeks.
But it's quite a change in the sense that it's kind of annoying because it's simpler but also kind of more structured.
And so that means that there were a lot of finicky details that I didn't anticipate needing to deal with, that I had to deal with, even though fundamentally the basic idea is kind of the same but also neater and simpler at the same time.
I can go into some details about the differences if you'd like, or I can just leave it at that.
What would you rather?

12:51 _Daniel:_
Let's return to this in the three.

12:53 _Toby:_
Okay, yeah, let's do that.
That's a nice idea.
So, yeah, I would say don't dig too deeply into it, because basically the thing that I've managed to do away with and sorry for all the people who've kind of tried to bang their heads on it already, is.
The kind of pro functor, like optics.
Kind of like the sort of pro functor stuff with those weird coen things, the kind of integral symbols that I was using to define context for statistical games, that whole thing.
It turns out you don't actually need the complexity of that structure.
And the notion of context is really given just by two things.
It's really just the prior, which we've already talked about, and also the observation you take from the environment.
And so before I thought you needed to consider not just the observation, but also the stuff that might go on in the environment around the observation that gives you correlations.
But it turns out actually you don't need that, at least not for the free energy principle.
And so that makes things a bit simpler because you don't need that kind of weird structure.
But there's, as I say, some technical stuff which is very annoying, which made it also a little bit slightly annoying to write down and involved by categories and sorry about that.
But it's actually the fundamental idea of a statistical game being like a Bayesian lens which describes the inference process, maybe like a parameterized Bayesian lens that allows you to learn, but a Bayesian lens that comes with a loss function that's still the same idea.
And it turns out that loss functions like the relative entropy and the free energy, they actually have a really neat categorical structure.
So the things I was calling like free energy games before or Bayesian inference games, those are actually now a lot even neater still.
So that's really nice.
And the way you get predictive coding is still as like a functor from these statistical games to dynamical systems.
So that idea is still the same.
It's just actually it turned out that the statistical games themselves.
There was actually a lot more nice stuff going on there than I had realized before.

15:42 _Daniel:_
Awesome.

15:44 _Toby:_
All right.

15:47 _Daniel:_
You cite Erisman and Van Bermesh work on memory evolution systems.
To what extent have you used their work in the thesis?
Would it be correct to say that there might exist a functor from that book to your dissertation or indeed to any of your citations, is there work someone could do to explore the connection between the two?
To me, this is a question of one instance if a learner or researcher performs active inference on the interface between a work and a citation more generally?
Great question.

16:20 _Toby:_
Yeah, I think it's a really nice so I I read this work by Erisman of Rambamish on memory reevoltative systems a few years ago, and I found it very abstract and confusing.
And I was like, yeah, this is all really nice, but how does it actually connect to the brain and how things like brains work?
But I've kind of softened my stance on it recently, and I think actually there's some really cool stuff in that work, some really great ideas about hierarchical complex systems and emergence and even things like neural coding.
It's kind of, I think, slightly in danger, I think, of being forgotten because people see it and think, okay, well, how does it actually make contact with things I know about now, things that actually scientists use?
And so I think it would be great to explore the connections in a kind of more detailed way.
I don't know precisely what that would look like.
I heard a talk, actually, by don't know.
There may be some on YouTube, I don't know.
This was in Consciousness Maths of Consciousness like workshop at the end of April, and she explained some of the more recent stuff they'd been doing, and it sounded like actually there is a proof, I think, that Hebian learning does actually give you sort of what she calls cat neurons.
And so before I've been like, okay, well, it's a nice story, but does it actually relate to things like heavy learning, or is it just like an analogy?
But it sounds like it's actually a bit more precise than I had thought.
And obviously, because of the connection between things like heavy and learning and predictive coding, it sounds like there should be a way to relate something like predictive coding to memory evolutive systems.
And that would be really nice because I sometimes think about this is kind of a direction that I'm trying to go in slightly, but try to think about nested active inference systems.
Like, you might have a little region of the brain and all the cells are doing active inference, and the circuits do predictive coding, and they make up a brain and the brains make up society and an organization.
And that story of hierarchical complex systems is really the story that this work is trying to tell as well.
Just in a different kind of way.
And so I think it's a really fruitful area, and I really hope somebody does dig into it, because I think it's great work, and I think it's just work that was kind of maybe ahead of its time, so it kind of got left by the wayside maybe a little bit.
But I'm really glad to see somebody ask about it now.
Cool.

19:56 _Daniel:_
Just one short remark on this, and then alir Dean, please.
It's almost like when people draw associations, like a line of sight.
Oh, well, emergence is like this.
It's like they're surveying and can have quite far vision.
But category theory is like building the high speed rail where it's, like, locked in.
And then we can say there really is a relationship of this exact formal type between Hebian learning and predictive coding.
Let's just say some type so then that can be really relied on as a foundational building block.
And it kind of brings those literatures and merges those streams or at least adjoins the streams or naturally transforms the streams, or whatever the appropriate terminology would be, but in a really solid way that's not just like, well, one person on a mountaintop saw that these two things could be connected.
It's more like an engineering project that really locks it in for everybody.

21:00 _Toby:_
Yeah, I think so.
And I hope people are incentivized to do that engineering.
I think that'd be great.

21:08 _Daniel:_
All right, last of the presubmitted questions.
So, in the par, pazulo and Friston 2022 active inference textbook, the first question in the recipe for designing an active inference model this is chapter six is which system?
This entails three pieces of data one, the agent generative model, two, the interface sensory data and actions, and three, the external environment, the generative process.
So how do these relevant big chunks of notions from the recipe for making an active inference model in the par at all textbook map to the sections of what you've done in your dissertation?

21:54 _Toby:_
That's a nice question.
And it takes me on to a question of action and active inference beyond the sort of approximate inference that I was talking about in my thesis, predominantly.
Maybe here I could draw some stuff, and so I don't know how easy that is for you, but I can share my screen.
Yes.
Let's see how this will work.
Yeah.
Okay.
Share.

22:25 _Daniel:_
All right.

22:26 _Toby:_
Can you see my cursor thingy?

22:29 _Daniel:_
Yeah.

22:30 _Toby:_
Okay, cool.
So I like to draw this picture, and this is like, the little channel c, which does prediction, and it goes from here, and it goes outwards.
And this is the inversion, the approximate inversion, and it takes in, like, a prior, which comes from here, and it takes in an observation.
So we could think of this as, like this is, like, high level belief and, like, lower level.
And this is like somehow you get something which gives you an observation, and then this gives you like new belief, high level.
And this thing is a Bayesian lens.
So that's what the Bayesian lenses are all about.
And the thing that I was talking about in my thesis is turning this into like a predictive coding dynamical system.
Because you've got neurons which do this sort of prediction part and then neurons which do this passing back of error signals to do this updating part.
And they have this kind of like bi directional form and that's really neat.
And so you can put in another one here, another one here, or you can just start with your prior which is like something that I often write as pi up here.
And then this gives you like a new pi at this point.
And so this is going always from higher level beliefs to lower level beliefs.
And down here you might eventually get to the lowest level, which is like if you're thinking about visual systems, then this would be like the V one visual cortex stuff or like the stuff you get in the retina and you get prediction about let's say visual signals.
But then the world, you get this predicted.
But then the world comes back and it actually gives you actual this is predicted, gives you actual signals and then the brain uses that to update its beliefs up here.
And so really the interface is somehow like this, okay?
And so this is like lens world and this is like external world.
So that's where the external environment comes into the picture.
And you could think of everything in here as like agent.
But this doesn't really tell us much about action and it doesn't tell us much about interaction.
And so there's another kind of story for that which is kind of similar in many respects, which is the story that is told at least in category theory by what's known as categorical systems theory.
And there you get pictures like this.
So this is like your world.
And there you've got some system inside the world and here you've got another system inside the world.
And so people then draw like things that are called wiring diagrams to kind of represent how these things interact.
So let's call this a for a.
Maybe there's another system over here and this is B.
And maybe that's C for A.
Its environment is like everything that isn't A, it's B and C.
So maybe it's connected like this, I don't know, some weird wiring thing actually, maybe that should go round to here and then this goes like to that.
I don't know, something like this.
This is just what's known as a wiring diagram.
It just tells you how the systems are coupled together.
And that would be like specifying how the information flows across the Markov blankets of your systems.
And so this box is like the Markov blanket of A.
And then this wiring is like the data of the coupling of the blankets.
And so there's a whole theory, a whole sort of story in category theory about how to sort of compose if you've got like, you know, if you you know, it has to compose dynamical systems of this kind.
And so, you know, what?
What we do is we say, okay, well, we we write down like the type of if we say if we call if we write IA to represent the interface like the data of this is like X and this is like Y or something like that the kind of shape of the Markov blanket.
Then what system theory tells us is that for each interface we get a whole category of systems that you could put in that box to animate it to make it like a living system.
And then this is like a closed box at the moment.
And so maybe it just represents the whole universe which doesn't have any external environment.
But you might also have something like a company, so you call it like company X, and that has some agent which decides what the company does, or some agent here which takes in information from the environment.
And so this wiring is then something that gives you a morphism from like A and B and C to X.
And what this dynamical systems theory tells you is that let's call that W for wiring is that you get this functor from din A and din B and din C to din X, which tells you then how to wire all these dynamical systems together to give you one that fits into this outer box.
And so this tells you how to do all this for just dynamical systems.
But of course, we're kind of interested in active inference systems.
And so here you don't just have some DX by DT thing to go in here.
You've got the data of prediction and plans and goals and maybe then something about how to actually do the inference, like the statistical game stuff.
But really the story is the same.
And so if you have these boxes, again, what we can do is if we have a box like this x to Y is we can think of an agent as having as a part of it a way of predicting, say, X.
We think of let's call these something else, sorry, let's call these S.
So this is like the sense data that goes into the system.
And then let's call this A, and then this is maybe like the actions that it takes.
Let's now call this box, I don't know B.
Oh, no, I don't like B.
Let's call it y.
So now let's think.
Okay, well, part of what an active inference agent is doing is that they're predicting they've got some high level belief of type Y, and then they make a prediction about not just the sort of sense data, but also about their actions and then their body samples from this belief about how they should act.
Or you've got these little cells, these little mechanisms which try to correct the prediction errors to make those actions into reality.
And then maybe that gets coupled to some other system which receives those actions as inputs.
And you might have another part here which goes in the other direction which says, okay, given my actual sense data and my actual actions, maybe my body is still learning how to play tennis or something, what are my new high level beliefs?
And so you can do this whole story again of Bayesian lenses.
And this goes like that, and this is now just why?
And then this is like S times A.
And this is s times a So you can tell this story and you can build like, hierarchical systems, but now you have a way of filling in each box and in principle, a way of coupling them together to give composite active inference systems, like companies or like colonies of cells or things like that.
This isn't a story yet that I've written down, but I know it works.
And I'm in the process of slowly writing it down.
So the kind of fundamental structures that are in the thesis are like part of the story.
The main thing that's missing is kind of like reorienting it's, just like reorienting this picture so that it's not like going from here from left to right.
It's like sort of poking down into the box, if you see what I mean.
And this is like the stuff you put in.
So this is like your lens thing here, and you sort of fill in the box with your lens.
So I think that tells I mean, that tells you how the chunks of the thesis kind of fit into the standard act of inference story.
The main job, at least as far as I'm concerned now, is to spell out the details and then start to talk about things like what happens if we've got Y and you've got Z's here?
What if they're trying to form part of an organization, but they disagree about what to do?
How does an organization resolve disagreements?
What if you've got two signals from your brain to your muscles that tell you to do different things?
How do you resolve?
How do you get harmonious active inference systems in some sense?
So I'll stop sharing my screen now, and then we could sort of return to the discussion.
But that's, again, my kind of long winded answer.

34:20 _Daniel:_
Awesome.

34:23 _Toby:_
I can share the pictures I see.
Dean you said you shared something, but I can share some more things.

34:32 _Daniel:_
Dina unmute and then go for it and then Ali no, I just shared.

34:37 _Speaker D:_
Something from about nine years ago that I was doing in my programming that everything you just wrote out was I just wanted to share one part of it.
That confirms that you could come from completely different places and arrive at the same destination.
The whole bi directionality, the whole predictive parabolic.
Yeah.
You can bring this into classrooms and have it make sense.
It doesn't have to be esoteric or too remote, I guess.

35:15 _Toby:_
Yeah, that's great to hear.
I'm really glad to hear that.

35:19 _Speaker D:_
Yeah, it's really awesome.

35:22 _Toby:_
Thanks.
Yeah, as I say, there's lots left to do, but I think an important part of that is like spreading the word.
It's really great that process is beginning, thanks to you guys.

35:37 _Daniel:_
So, yeah, the rehearse play reflect cycle actually begins when you reverse the direction of thought reading from Dean's email.
Interesting.

35:51 _Speaker D:_
Self organized.
Yeah.
It's all part of this whole cat.
This is the like, I love the questions that we've had so far and I want to hear Ali's questions and then I want to be able to take it and have people not be intimidated by it because you can really find yourself doing these things on a daily basis.
You just don't necessarily identify them the way that we are.
But that doesn't mean that we have somehow lost access to the things that we're discussing today.
So I'll just leave it at that for now.

36:32 _Toby:_
Yeah, cool.

36:36 _Daniel:_
All right, in the rest of the time that we have with you for the two Toby.
Ali.

36:54 _Speaker C:_
Okay, thank you.

36:58 _Daniel:_
Your video is frozen.
Your video is frozen.
Maybe you can just turn it off.
Yeah, go for it.

37:07 _Speaker C:_
Thank you.

37:09 _Toby:_
All right.

37:13 _Speaker C:_
In basically three to ridiculously.
Next.
Sorry, the notion of Marko, I noticed in your thesis.

37:30 _Daniel:_
Sorry, Ali there's just a lot of lag.
Yeah.
What would you say is the chapter six equivalent?
Is there yet a recipe for designing the kind of categorical, kind of compositional organization that you alluded to?

38:14 _Toby:_
I can answer that quickly.

38:16 _Daniel:_
Yeah, go for a quick answer and then I think now it's better.

38:19 _Toby:_
Ali yeah, so the quick answer?
Well, it's a quick answer, but it's not a quick thing to do.
But there's a great book on categorical systems theory in its kind of great generality, which doesn't explicitly talk about active inference like I've been, but it does talk about this kind of composing dynamical systems in this hierarchical way idea.
And that's the book that's currently being drafted by David Jazz Myers.
I can circulate a link to it.
Myers that sort of spells out the kind of general structure and I believe he and Mateo Capucci have got a paper upcoming at the upcoming Act Conference on Applied Category Theory this year, talking about using that framework to do kind of cybernetic like things.
And so what I've been thinking about lately is trying to fit active inference and the stuff I've been doing into that framework, which has been sort of developing in parallel and kind of fortunately and maybe slightly unsurprisingly, they fit very nicely together.
And so the pictures I was sketching are kind of a fragment of that other framework.
And as I say, I think they go quite well together.

40:06 _Daniel:_
Awesome.
Okay, Ali, go for it.

40:11 _Speaker C:_
Okay.
Sorry about that.
All right, so I noticed in your thesis that you don't rely too much on the notion of markup blankets, but instead you use this notion of polynomial functions as its more formal or perhaps more rigorous replacement.
With regard to that in your paper Polynomial life, you say in the literature on active inference sorry.
And the free energy principle, there is much debate about the concept and role of markup blankets, which are sometimes conceived to represent the boundary of an adaptive system.
We believe that the algebraic polynomials will help to make such thinking precise where it departs from the established usage of markup blankets and Bayesian networks.
So would you care to elaborate a bit on that?
And how do you see polynomial functions as overcoming some of the limitations of the notion of markup blankets?

41:13 _Toby:_
Yeah, okay.
So I will preface this by saying I think some people might disagree with me, but there is a notion of Markov blanket that for me is nicely defined, that exists in the sort of Bayesian statistics literature.
And it says if you've got a Bayesian network, you can consider the nodes in that network and you can ask what are their Markov blankets?
And in particular, you can just define the Markov blanket of a particular node to be its parents.
So those nodes that it's conditionally sort of dependent on its children, sort of those nodes which are conditionally dependent on it and what are known as its coparent, so the other parents of its children.
And that's a very nicely well defined notion, but it's only nicely and well defined in this context of Bayesian networks.
And so it's like generalizing that to kind of situations where you've got interacting dynamical systems is something that informally makes total sense.
You want to say, okay, well, I have this thing in the world and it behaves so it changes in time, and it's sort of a coherent unity in some sense.
And so it has a kind of boundary.
And because it has a boundary, information and energy from the environment always has to flow through this boundary in order to interact with it.
And that sort of boundary notion, it seems, is like what is in other contexts also called a Markov blanket.
And I think if you set up your dynamics in a particular way or your definition of Bayesian network in a particular way, that the two ideas that might coincide.
But I don't think that's true in general.
And I think what people mean in the literature when they're talking about Markov blankets, but in this dynamical context, I think all they really mean is like boundary or interface.
So the data of the system, like capacity for interaction or something like that, the stuff that is on the edge of the system through which interactions with its environment are mediated, that sort of general idea is something, again, that appears nicely in categorical systems theory, but in a very general way.
And it doesn't require any of the notions of Bayesian statistics, and it doesn't require conditional dependence or parents or children of a graph because you might have something more complicated than a graph.
Like you might have edges which are allowed to connect more than one node, and that gives you a hypergraph.
And there, of course the notion of Bayesian of marker blanket in the standard sense that doesn't make sense at all, but of course the notion of interface does.
And there are certain categories of interfaces.
And those wiring diagrams I was drawing before are an example of a category of interfaces.
Like they don't have any data of the systems themselves.
The category just tells you how to sort of plug interfaces together.
And so I think it's kind of neater to think about this connectivity in the interfaces sort of separately from the stuff that fills the interfaces, like the data of the dynamical systems or of the active inference, like games that I've been talking about.
And so a really nice kind of category that you can use to talk about interfaces and indeed to talk about lots of other things, but in particular to talk about interfaces is this category of polynomial functions.
And it kind of generalizes these wiring diagrams that I was drawing earlier.
And it does so in a particularly useful way, I think, which is that if you sort of formalize the interface of a system using this polynomial language, you can start to talk about interfaces that themselves might change depending on the context.
So when you get into the car to drive somewhere effectively, you've sort of changed your interface because now you've got this car around you and it behaves in a different way than if you're just on your own or if you're just normally going about your life.
You might blink right, or you might close your eyes, and that means that you're no longer receiving visual signals from the world.
And so if you just say you're writing down your active inference model and part of the model is that it receives visual signals, then talking about situations where those visual signals go away.
You.
Can do it right, but it's not very neat.
And so to sort of account for interfaces that might change like this, it's nicer to be able to say, okay, well, my interface actually is allowed to depend on what I'm doing right now.
So I'm currently on a video call and it means I can do certain things, but I'm currently wired into the computer so I can't so easily go and walk around like the set of signals I receive or actions I might take might change.
And so I think it's easy to start by saying, okay, when we're talking about Markov blankets in dynamical systems, we just mean like, there is some set that is like the action set and some set which is the sort of sensory set.
For me it's just not enough because of the fact that the world is dynamical context change coupling might be dependent on like you might be in an organization and there's some executive who's in charge of defining the team structure.
And that means the team structure is like the wiring of the agents in that organization, but how they behave depends on the decisions that that executive makes.
And so their markup blankets are conditional on those decisions.
And that's something you can talk about nicely in this polynomial language because you're allowed to have systems which affect the wiring of other systems.
But it's really not something that's easy to talk about in this standard framework of interfaces and boundaries that is dominant in the active inference literature.
And I think that's because really in the active inference literature, there isn't a framework for interfaces and wiring and that framework is supplied by these categories of interfaces.
And so you can just choose one and you can hope it does choose one that's appropriate for your situation that you're trying to model, but it helps to actually have one that allows you to do this wiring and that's something that using category theory allows you to do because it's all about composition.

49:28 _Daniel:_
Awesome.
The textbooks will be rewritten. Dean.

49:33 _Speaker D:_
Quick thing, Toby, does the timing of the choice in your experience really matter?

49:44 _Toby:_
The timing in what whenever, whenever you.

49:48 _Speaker D:_
Do decide to make a choice, doesn't the effect of the timing, the whenness of activating that choice play a huge part in what follows in terms of the category?

50:04 _Toby:_
Yeah.
So do you mean like if you're choosing to use a particular kind of interface language, say or describe a thing with a particular interface or like particular kind of boundary?
Yeah.
So I agree.
And that's why I kind of tend to work quite abstractly.
So rather than saying I'm working with a particular kind of interface language, I'm just saying I will assume my interface language allows me to do these certain things.
And so that's not so useful for actually implementing a particular model.
But if you're trying to think about systems in general, it's helpful to work agnostically in that way.
And so the reason I sort of advocate like this for polynomial functions is I think that they sort of fit at a nice sort of intermediate level of abstraction.
It's not to say, okay, well, there is a collection of interfaces and some collection wiring them together because that doesn't tell you actually how that works.
So it is slightly opinionated.
It's different from certain choices that people in other bits of applied category theory make.
But it does generalize this simple case where you have just a single set of outputs and a single set of inputs or single set of actions and a single set of observations.
And so I think because of that it's a nice sort of intermediate level and I think it's one I've tried to work with, because I think it's quite natural.
But yeah, you can sort of totally work at a very abstract level.
And that's what David Jazz does with his systems, just he just talks about interfaces in general.
You might not have actions at all.
It's completely agnostic.

52:10 _Daniel:_
Awesome.
Ollie.

52:14 _Speaker C:_
OK, thank you so much.
So my second question is about the relation between your compositional account of active inference and the recent line of research done in Bayesian mechanics, namely the discovery of the duality between FEP and constraint maximum entropy principle as discovered primarily through the work of Dalton Saktive Adebel in the last couple of years.
There's this nice duality between the observer dependent the viewpoint from the inside observer of the agent and the outside observer.
So, respectively, the perspective of FEP as opposed to constrained maximum entropy principle.
But Dalton has demonstrated that actually, those two perspectives can be unified through showing the equivalency between the Bayesian optimality and James optimality.
So from Bayesian optimality, we can obtain FEP, and from Jane's optimality, we can acquire CMAP.
So, given that the notion of Bayesian lens also comprise both Bayesian inference and its inverse process, do you think the Bayesian lens as providing a kind of, I don't know, a tool to account for showing this kind of duality between FEP and constraint maximum entropy principle?

54:02 _Toby:_
I think the answer is probably yes.
But I think this is a really great question, because genuinely, I don't know the story mean, I know a bit about Dalton's work, and I think it's wonderful, but I really don't know yet how it connects to the stuff I've been doing.
And it's really like an open question for me.
But there are some tantalizing signs that, as I say, I think the answer to your question is yes.
There is a kind of unification of the two kinds of story, and some of the ingredients of that story are kind of floating around out there.
So I know that there seems to be a connection, or like I know that there is a connection between quantities like the relative entropy and energetic concepts you get in physics.
And through that, you can make a link to the kinds of things that Dalton has been doing with gauge theory.
And I feel like there is a kind of geometrical structure that you can put on top of these statistical games that I've been working with, because, remember, they are these lenses with these loss functions.
And these loss functions seem to have this kind of, as I say, this kind of geometric thing going on with them.
But really explaining or putting constrained maximum entropy into statistical games language is not something that I've done and it's something that I've been thinking about doing, and I'd be delighted to talk to people about more.
And so I don't know precisely the details.
There is a kind of other duality, which I think is quite nice which is related to this.
And I think again, at the nexus of these is this systems theoretic idea, because of course, all of this work of Dalton's lives in this kind of dynamical systems world where you have dynamical systems that are interacting and information flowing between them.
And there are some really tantalizing connections, again, of course, between physics and information processing.
And I learned the other day, for instance, that there are certain classes of generative adversarial networks sorry, this is just a slight tangent, but I think you might be interested to know certain classes of generative adversarial networks that you can set them up.
And the two parts of the network tend to instead of settling into an equilibrium, they seem to exhibit some orbits around each other so they don't achieve some equilibrium state in the game they're playing.
They kind of just got around.
But somebody was telling me about if you have an orbit and you're a physicist, you think, okay, well, what is that orbit conserving?
Is there like a quantity that it's conserving?
And in this case, and I don't know the details, but in this case, this person found that the quantity that was conserved in this orbit was the relative entropy.
And so there's this weird thing going on.
These things are playing a game, but they're still at this kind of somehow steady state of relative entropy.
And so there seems to be this deep connection between these kinds of game like systems and sort of information physics in some sense.
And I'm aware I need to head off for the moment, but I just want to draw one more picture.
And I'm sorry, Elliot, you probably had loads of questions, but we kind of ran out of managed to answer many of them, but hopefully we'll get to the rest of them soon.
But if I just draw, as I say, one more picture, which is a kind of slightly different kind of duality, but a similar kind of similar kind of flavor.
So what we have in systems theory is this category.
You have this category of interfaces of systems and the morphisms tell you how to wire these systems together to give like hierarchical or like composite systems.
And if you have something like this thing which I wrote before Din, which I said for each interface I was like a category, then you can sort of think of this as a functor from int to like cat the category of categories.
And one thing you can do with index categories of this kind is you can sort of turn them into what are called like vibrations using what's known as the Groton deconstruction.
And if you know about physics, you've probably heard of a concept called a fiber bundle, which is just like a collection of spaces indexed by points of another space.
And so what you can do is you can write this vibration which says, okay, well, for each interface I've got a category of systems on that interface and they're all like glued together correspondingly with the wirings of your interface category.
And so you write this as like another function which kind of forgets about the dynamical systems and just returns the interface again.
And so you have this vibration thing here and this is like where kind of like physics lives.
And so what I've been trying to tell this story about, in this story about active inference is that you have a similar one where you have for each type of interface, the category of agents that might have that interface.
Like we're all humans and so we are all like the type that might fit in like a human shaped box and so we're all in that particular category and we come together to form organizations and that's another object of this category of interfaces and another kind of agent category on those interfaces.
And so that gives you another one of these vibrations.
And the thing that something like predictive coding tells you is it says, okay, well, given a certain story about a type of agent, can I turn that into a dynamical system which actually animates it?
And so that's like a functor like this.
So maybe what we could do is we could think of this as maybe like some version of biology or we could think of this as like we could think of this as like body and we could sort of think of this as like mind.
And so this is telling us how to go from a description of a mental system to a sort of embodied system.
And I think some of what the free energy principle is trying to say is that for certain kinds of systems there's a way to turn your description of a dynamical system into something that looks like an agent.
And so the thing I'm wondering is that whether there's some adjunction or maybe this is like I don't know.
I don't know which way we might write labels on these, but maybe there's, like, some adjunction here that allows us to compare these two processes of turning a sort of mental system into a physical one and then going in the other direction from a physical system into a mental one.
And so maybe this is also where information comes in.
And it's a kind of similar story in category theory where there's a sort of duality between geometry and logic that that's sort of sometimes written like this.
You have truth values down here and you have logic over here and you have space over here and there's a way to sort of draw a picture like this that says, okay, well, logic is somehow like dual to space in some sort of mumbo Jumboy way.
I mean, again, I've run out of time, but I think there's a story that people try to tell about science in this kind of abstract world and I think it's a similar story to maybe something that's being told over here.
Again, lots of details, and I don't know precisely the connection with Dalton's work, but I think it's kind of pointing in this kind of direction.

1:03:04 _Daniel:_
Thank you, topy.
After you have revised and proceeded, let's have 54.3 and talk more about action, active inference.
So thank you.

1:03:18 _Toby:_
Yeah, great.
Thank you so much for having me.
And I look forward to speaking again and answering your questions.

1:03:23 _Speaker C:_
Ali, thank you so much.
That was great.

1:03:26 _Toby:_
Okay, great.
Bye, guys.

1:03:29 _Speaker C:_
Bye.

1:03:31 _Daniel:_
Well, I'd like to ask Dean a oh, Ali, please make a remark.

1:03:44 _Speaker C:_
And then I have a yeah, you know, I really think of Toby's work as really provocative as it really opens up Pandora's box of many, many different fertile questions.
So I'm a firm believer of this old saying that a sign of a great book is not how many answers it provides, but actually how many questions it gives rise to.
So I really wanted to congratulate Toby on writing such a I mean, it looks as if he began from the perspective of trying to address some of the I don't know, some long held questions, but then it turned out to be much more deeper than that in terms of actually giving rise to many fertile questions.
So, yeah, that's really great.

1:04:52 _Daniel:_
Dean, I'd like to ask, what is the difference or how can we think about being on time in time and out of time?
Because Toby said he was out of time with the answer.
And I know that we've spoken about this when we consider some of the time consciousness and category theory work previously.
So what is it to be out of time?

1:05:22 _Speaker D:_
Yeah, that's a great question.
All I can say at this point is that it's easier to discretize when you're in time and out of time as a comparator than it is to say when you're on time versus those first two positions.
That's all I can say about that for now, because I'm sure Toby, from a diagrammatic perspective, could probably tell us what is happening when he's actually using his stylus versus not right.
Like the result of that leaves something in and out.
But while he's actually on point, he's literally in a different place.
Here's an interesting thing, back to the provocative Ali in the Dot.
One was talking about virtual and actual models and was probably saying it in a way that's completely different than how I use.
I believe those same two models are in effect.
And so if you, for example, draw up a play, say, in sports, because we're talking a lot of strategy while Toby was on today and a lot of gaming theory and stuff, you draw up a play, then you confirm that you have all of the elements or resources that you need in order to be able to carry that out.
And then you're as a group communicating with one another like we are doing on this live stream, right?
Like you're literally calling out the play in North American football.
You'd huddle up and literally call out a sequence of code and then you'd have to literally reverse that and turn the inference as the shortest time window into a prediction.
Like you would literally line up and then you would carry out the simulation in actual terms.
All of that together means that I believe that the virtual version of the model is, as Toby was saying, in the bi directional sense, going in one direction, and the actual model is going in 180 degrees the opposite direction.
And then when he mentioned the dagger symbol today, I was just like, okay, where does that fit in to this bi directionality and the difference between.

1:08:41 _Toby:_
The.

1:08:41 _Speaker D:_
SIM, the digital, the virtual, and the actual?
So these are the things that literally pop up at any given moment, aren't necessarily part of what you consider to be the space that is inhabited by virtuality and actuality.
And yet there it is.
It just appears.
And then you have to sit down and figure out, well, where does that categorically fit?
So again, don't want to go off on a deep rabbit hole philosophical take on this, but I just find that at any given moment, there is again, so much math in this philosophy that it's kind of staggering.
And just to be able to have somebody who can explain that and draw it out is pretty impressive.
I don't know if it's provocative what I just said.
I hope it isn't because, man, I did this work for almost a decade and it seemed like young people weren't scared by it.
Maybe older folks are, but I don't know.

1:10:00 _Speaker C:_
So if I may add a brief comment on just what you said, I was recently watching this talk by John Bayes about the history of applied category theory.
So he had this nice diagram showing the relationship between different areas of knowledge, I mean, going from business to pure mathematics.
And he claimed that most people in category theory, or in most other areas, consider category theory as being on the top of the pyramid, as being the purest of the pure, so as being even kind of being on a meta level than even the pure mathematics.
But then he said that I believe category theory can actually be seen as kind of permeating all of these levels.
So it's not something that sits on top of the hierarchy.
It's something that actually can be seen as influencing and permeating all the levels.
So at least from the perspective of applied category theory, it seems to be, if not self evident, but something that gathers much, I mean, more evidence as the research goes by.
So I'm really optimistic in the research direction that applied category theory is going.
And hopefully in near future we can see it applied to many, many different areas, many different unforeseen areas.

1:11:52 _Speaker D:_
I think I'll just tag on to that.
Ali, if you use an abductive logic lens, then it's simply a question of when did you enter, at what point did you enter the abstracted timeline?
Because if you see it that way, it's not just top down and it's not just bottom up.
It's back to my question to Toby was, does the whenness of this really matter if you want to be able to take it off the shelf and use it?
And of course, his answer was, yeah, if you want to deal with idiosyncrasies, you're left with no choice but actually to acknowledge the point in the continuum where you take this up.
But I think that actually makes it quite easy to see it permeating every level.
But again, it's the abduction, the abductive piece of this back to last year in August, right?
We're coming up on one year since we talked about how important that is, and yet here we are, what, ten and a half months later, and we're circling back.
We have another predictive parabolic on our.

1:13:26 _Speaker C:_
Heads.

1:13:31 _Daniel:_
Few comments on that.
It's reminding me of Professor Mike Levin's work on basal cognition and the idea that intelligence isn't on the top of the pyramid either.
Rather, it's something that's distributed compositionally across levels and something that exists at all levels.
And so we can then still talk about higher order properties of systems or properties of composites or aggregate systems while also grounding in the foundations.
Um.

1:14:22 _Speaker D:_
Yeah, and that, and that grounding and anchoring and stabilizing, that's by itself is nothing but a feature.
I think you also want to be able to, though, because there was a lot of talk today about being able to see this in the way that things dynamically play out.
So, again, we're back to the what's the minimum two ways that we want to incorporate this observation, both as stabilized and as searching.
Right.
If we can have one eye on each at all times, it does take a bit of rethinking.
There is a there is a there is an interoceptive piece to this.
What we feel from that is different.

1:15:26 _Daniel:_
That brings us to the sensor fusion aspects of the dissertation 7.1.1 Bayesian sensor fusion.

1:15:38 _Speaker D:_
Yeah.

1:15:40 _Daniel:_
A situation that is common in natural embodied systems, but which is not yet well treated by current statistical machine learning methods.
Also, Ali, thanks so much for asking the Markov blanket question.
I think his response is worthy, honestly, to review and unpack in the time we have, we can just sort of review a little bit and think about what other questions we want to prepare for.
Two, how would you, Ali, restate the limitations of the Markov blanket concept for all the positive things that we've said in the previous 300 live streams and where category theory can help address and move past some of that?

1:16:33 _Speaker C:_
Yeah, you see, this notion obviously is one of the most or, I don't know, probably one of the most controversial concepts in whole FEP literature because it has received a fair amount of criticism from many various perspectives.
But some criticisms, at least as far as I know, they're basically directed toward the universality of Markov blanket.
How universal is this notion as it's claimed to be ranging from, I don't know, inert rocks to the brains, right.
So does it apply equally for modeling inert rocks as well as the most complex system we know of in the whole universe, namely the brain?
So the response this line of criticism got from the researchers in the active inference area, again, to the best of my understanding, is to the effect that although theoretically, it can be applied to many different systems with many different levels of complexity.
But then again, for simple linear systems such as I don't know, many non complex systems, it doesn't have anything interesting to say.
So rather than being applicable to all of these systems, the relevant question should.

1:18:20 _Toby:_
Be.

1:18:25 _Speaker C:_
There are enough insights we can gain from applying this notion to many different situations and systems.
So I believe Toby's alternative for this problem by proposing the polynomial function as a replacement for Markup blanket can cover this line of criticism pretty nicely.
It can address this criticism pretty nicely due to its abstractness and a kind of more rigorous way of talking about both the universality and the individuality of each system.
So I think that's a nice way to at least a viable answer to this question that needs a lot more consideration.
So that's my take on it as far as.

1:19:34 _Daniel:_
Okay, I'll give my take two, which is the Markov blanket concept, since the work of Pearl in the 1990s is actually not doing that much philosophical work in and of itself.
It just describes the parents, the children and the coparents of any given node within a graph.
So first, we're talking about maps, not territories.
We're not talking about features of the world, carving nature of the joints, necessarily hashtag malandrus.
We're talking about the Bayesian graph.
And secondly, even on the graph, it's not that a node is like by its essence an internal state or a blanket state or an action state if you use the Friston blanket.
Rather it's always in relationship to others.
So the concept by itself does very little work.
However, people have deployed the concept implicitly and explicitly to describe interfaces of cybernetic entities, the kinds of entities that it makes sense to describe as an active inference agent.
So we know from the particular physics and the strange kinds work the path integrals paper that we can describe using the formalism, the rocks, the simple active systems and the sophisticated active systems.

1:21:03 _Toby:_
In.

1:21:03 _Daniel:_
Order to have an interface concept that does justice to on one hand the relatively inert interfaces, on the other hand, potentially extremely conditional or contextual interfaces.
Just having some tagging system of nodes on a Bayes graph is going to get extremely messy.
It's not that it couldn't be done, but just in terms of actually doing the programming, it's going to be extremely messy.
You're going to need to have a lot of accessory or auxiliary variables that indicate what the current interface is at this time or what it would be if this happened.
And all these kinds of conditionalities would be like a less elegant way of describing what our category theory colleagues have been developing explicitly with the wiring diagrams and interfaces.
So just to kind of conclude there people draw the Bayesian graphs and the particular physics is using a Bayesian graph.
However, Bayesian graphs don't naturally have a lot of these properties that were really being conflated with interfaces more generally.
And by using an interface concept, as Toby said, at an intermediate level of abstraction, that's slightly opinionated but also really flexible, that is kind of the right coarse graining, the right optimal grasp on the interfaces that we actually want to talk about for active inference agents.
And again, just trying to get down to the firmware with the Bayesian graph, we're going to get lost in the details.
And any accounting system that we develop is going to be ad hoc and certainly less principled or powerful than what the category theorists are developing.

1:23:08 _Toby:_
Yes.

1:23:09 _Speaker D:_
Dean, I'm really curious what you think of this.
If we're talking about the relationship with the interface, could we see and I'm really asking this question.
I don't know, I'm spitballing could we see the Markov blanket as the more stabilized version or form of the relationship and see the polynomial version of that as the search version of that relationship?
What do you guys think of that?
And I'm really asking, just listening to both of you talk here, I'm just wondering if I'm having one of those unitary moments myself or if I'm way out to.

1:24:07 _Daniel:_
Ali, give a first thought, then I'll also give a speculative answer.

1:24:12 _Speaker C:_
Yes.
So one thing that comes to mind is, you see, sometimes people consider markup blanket as being a kind of static boundary or interface that just separates the agent from its environment.
But actually what it really is is kind of providing really a dynamic interface between those two internal and external states.
So it's not a static or stabilized in any way.
But of course, in some situations we treat it as if it's stable or, I don't know, static coding.
Maxwell Ramstead every theory of markup blanket is inherently per se, so there isn't any static conception of markup blanket at all.
But on the other hand, well, obviously for the polynomial function, not just polynomial function, but the whole area, category theory deals with objects not in their static sense, but rather in the meaning they acquire through their relations, through their morphisms.
And it's not about so one of the main differences between category theory and the set theory is exactly hinges on that distinction between the static viewpoint of mathematical or, I don't know even non mathematical objects and the inherently dynamical or relational identity of the objects as defined in categories.
So I believe polynomial functions again, by themselves are inherently and intrinsically dynamical, perceptual, and in the terms of some continental philosophers, such as Alan Badu, they acquire existence through their imminent relations.
They don't need any notion of pre existence as some of the Platonic notions of mathematical objects and ideas.
So yes, in this sense, I think polynomial functions, I'm not sure which one can be seen as, I don't know, more dynamic or processual than the other, but at least to a degree, both of those concepts can be seen as sufficiently processual, in my view.

1:27:21 _Daniel:_
Awesome.
Okay, I'll just add with a few other associative comments.
One is to blanket something is to dampen and stabilize it, whereas polynomial seems to invoke, like many names, polynomos, polytopos.
So potentially there's a multiplicity in the polynomial that is not acknowledged.
So lexically in the Markov blanket and then a more formal way to say that would be a Markov blanket might be like a specific realization of some little neighborhood within the polynomial.
So polynomial functor is a generalization of the Markov blanket.
And so in that sense, it requires more searching and it is more abstract and it is more general.
But when you do stabilize it down, then the Markov blanket formalism may absolutely apply.
But wherever the Markov blanket formalism does apply, like, let's just say that we stabilize down to a computer system and we have an API and we consider that that's one of our blanket states.
That would also be seen as an interface, of course, which is happy we'll talk about it.
And so it would be a polynomial function.
And so this helps us look back at the literature and see, as has been done many, many times in FEP and other literatures, recent developments enable previous developments not to be invalidated, but understood as special cases or constrained or stabilized cases.
And it only makes sense that we would start.
Well, putting aside what makes sense in active inference, it seems that we are taking both paths.
In some cases leading with the stabilized and generalizing, but in other situations making unstable generalizations that then precipitate stability inside of them.

1:29:36 _Speaker D:_
So more bi directionality.

1:29:43 _Daniel:_
Great.
Well, we will have a 54.3 with a focus more on action.
Are there any other topics that you fellas would like to raise?
Or if anyone in the chat wants to ask a question, please go for it.
In our last bit here, let's look back to the table of contents or Ali, please go for it.

1:30:10 _Speaker C:_
No, just I wanted to ask Toby about the relationship between his theory or compositional account of statistical inference as opposed to the category theoretical account developed about, I don't know, more than probably ten years ago by people like Bob Kirky and others specifically related to the distinction between classical and non classical Bayesian inference.
That's been clearly distinguished in one of the papers from 2011.
I guess so, yeah.
That's one question I wanted to ask Toby, and of course a subsequent question about the relation of this distinction nondistinction to the accounts of quantum FEP.
Because in quantum FEP markup blanket is kind of replaced, or rather blended with the notion of holographic inner screen.
So how can we see quantum FEP as arising from quantum Bayesianism rather than from, I don't know, predictive quantum theory and the relation between those two frameworks of Bayesian inference to that topic?

1:31:53 _Daniel:_
Awesome.
Yes, the quantum category theory active FEP triangle.
And also, I think the question about reading the literature in terms of the interfaces between a work and the citations, I think is extremely rich.
It's a really novel way to perform bibliographic metaanalysis, but also just in our own learning journeys.
This following this category theory dictum of knowing a thing by its relations understanding the paper within the web of the past papers which it cites, all of which are past and actual and then its future time cone of possible relationships to things that haven't happened yet.
The co parents haven't even happened yet, necessarily.
But that becomes part of the evaluation of the significance in the moment.
And if we could have the right generative model and understand how much attention to weight onto different things in the moment, that would be like being able to see the whole time cone at the right core screening.
But of course, as limited nest mates we can't do that.
But we have our rules, our heuristics and our approaches that address that nonetheless.
Anyone in the Chat or Dean, what would you like to explore in 54.3?

1:33:43 _Speaker D:_
I'm just going to follow the two of you.
I got two big workhorses here.
I just got to get out of the way so I don't get trampled.

1:33:57 _Daniel:_
Let's look at the table of contents here.
We're just shifting to the code of document, the back end that we use to coordinate a lot of our work just so that it can all be seen in the video.
Chapter one is short.
Chapter two, if someone is looking for another account of like, why does category theory matter?
Toby begins chapter two with three examples of situations neural circuits, Bayesian networks and computations where people often just use a kind of schematic diagram but it's not necessary or sufficient to really convey all of the richness that we can add on with category theory.
Chapter three starts getting into more detail with string diagrams and developing towards circuit diagrams in this rate coding neural setting, a lot more new vocabulary arising along the way.
Chapter four, which the question the beginning of this Livestream brought a focus to, is on the compositional aspects of probability.
The copy discard structure is introduced, which we saw in the diagram today.
That's when the piece of information is duplicated and then one of them can be thrown away Bayesian inversion, the dagger, Lady Macbeth's dagger always just dangling there.
Then the growth and deek construction, bringing back strong recall of Shauna Dobson, Chris Field's, math, art and the complexity of the self.
Chapter five went into dynamical systems.
Markov chains open and closed dynamical systems with this polynomial interface concept.
It's really built up in an extremely methodical way.
First the dynamical system is kept, within a nutshell, extremely bounded, but then it's progressively opened up.
And so even though it's going to be a lot of new information reading the dissertation, it's done in a way that does also clearly build upon itself.
Chapter six goes into the Bayesian lenses, connects to several more prevalent concepts in statistics maximum likelihood estimation, approximate Bayesian inference, auto encoders, and connects this to the emerging concepts of Bayesian lenses and statistical games in terms of the approximate inference doctrines in chapter seven.
Yeah, Ali, please.

1:37:23 _Speaker C:_
No, I just wanted to mention this particular chapter is being rewritten at the moment, so yeah, that's thank you.

1:37:31 _Daniel:_
Absolutely.
Yes.
As we discussed a little earlier, chapter six is going to get simpler but better, but it was tricky.
But it's simpler.
But it's better.
But it was tricky.
And then chapter seven closes it out, but really opens it up with the compositional, cognitive cartography sailing the Three Seas society of systems more alliteration, many, many connections to areas of interest for all system scientists and complexity enthusiasts.
What a tour de force and a journey.
And it's going to be awesome that we'll get to see some of the next increments in the work.
Talk more with Toby.
Yes, Dean?

1:38:30 _Speaker D:_
Can I just throw this in?
And it's going to indicate how old I am.
But a long time ago, the first time a needle dropped on the first Van Halen album, something changed about everything that we thought about guitar playing.
And if you weren't there in that moment, you wouldn't know how everything changed.
I'm not sure what category theory taken up on a mass scale will do if it will be the equivalent moment for all people who use math in all the different ways that they use it, but I think that we are at the beginning of something that it is going to change things.
And I don't know exactly how it's going to change things, but I think this will always now be included as how we try to both figure things out and out the figures in that three dimensional space.
I mean, one of the things that I thought was interesting in the dot one was when Toby said, well, I work in 2D space and now I'm curious about I wonder what that would look like.
Well, we exist in a 3D space and so I think the applicability of it is going off at any given moment.
But I do really think this is the start of something.
I'm not sure exactly what, but I don't think we'll be able to unlearn this.
I think it's going to remain influential for a long time.

1:40:17 _Daniel:_
For those about to categorify, we salute you.

1:40:22 _Toby:_
Yeah.

1:40:23 _Speaker D:_
Right.
There we go.
Thank you.
You can always make it better.

1:40:33 _Daniel:_
Any other thoughts on this?
Otherwise.

1:40:41 _Speaker C:_
Great.

1:40:42 _Toby:_
Yeah.

1:40:43 _Daniel:_
Ali, please with any last thoughts?

1:40:46 _Speaker C:_
No, I just wanted to say I'm really looking forward for the next installment.
I hope it happens soon because again, I have so many burning questions.
I try mean whittle it down to some I don't know, not too much time consuming questions.
But yeah, I'm really interested in I'm curious to know Toby's answers to them.
So thank you so much for everything, for organizing this and inviting Toby.

1:41:20 _Daniel:_
Oh, absolutely.
All right, thank you, everybody.
See you in 54.3.

1:41:32 _Toby:_
Bye.
