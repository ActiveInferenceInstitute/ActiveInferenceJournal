---
title:  'Physics as Information Processing - Lecture 2, "Why Quantum Physics?"'
author:
- 'Chris Fields (Allen Discovery Center at Tufts University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-4812-0744)'
- 'Ander Aguirre (Ohio State University) [![Orcid](images/orcid.png)](https://orcid.org/0000-0002-6337-8292)'
- 'Daniel Friedman (Active Inference Institute; University of California, Davis) [![Orcid](images/orcid.png)](https://orcid.org/0000-0001-6232-9096)'
date: "2023-06-15 Version 1.0"
...

## Lecture 2, "Why Quantum Physics?"

_Daniel:_
 Hello, everyone.
 It's June 15th, 2023.
 We are here in lecture two of Chris Field's course: Physics as Information Processing.
 So,

 Thank you, Chris.
 Looking forward to the lecture.

_Chris:_
 Thank you, Daniel.
 And, yes, welcome to this session.

 This section is titled "Why Quantum Physics?".
 And, if you will recall, from the first session, we reviewed the History of Physics and some of the History of Mathematics and Computer Science, from the end of the 19th century through to the beginning of the 21st century.
 And, we discussed the slow development from classical thermodynamics of Quantum Information Theory and specifically we characterized Quantum Information Theory as a new kind of physics that describes systems that are exchanging finite amounts of discretely encoded information across some intervening boundary.

 And so, we use this very conventional graphical notation of two agents or physical systems, Alice and Bob (A and B), that are exchanging energy and information across some boundary.
 And I always use a blue ellipse like this to indicate the boundary that separates Alice from Bob.

 And, this new approach to physics is entirely topological.
 It's not geometric.
 So, it doesn't assume a particular background spacetime. So, it doesn't assume that Alice and Bob are spatially separated.
 And, so, this makes it a very different kind of theory from Classical Information Theory in that the channel that separates Alice from Bob, this boundary, is a boundary in state space.

 It's not a boundary in some geometric embedding space.

 And, in particular, it's not a boundary or a channel that's embedded in a three-dimensional space that separates Alice from Bob.
 So, that's what we talked about last time. And today, what I want to discuss is how Quantum Theory in particular makes this idea of physics as a theory of communication simple and obvious.
 And, Quantum Theory, of course, has a terrible reputation of being abstruse and mathematically incredibly complicated and counterintuitive and difficult to understand.
 And, this is one quotation among many from leading physicists pointing out that quantum mechanics is just difficult.

 And, as you probably know, there's an entire philosophical industry of interpretations of Quantum Theory that try to make sense of its ontology.

 And so, what I don't want to do today is try to introduce quantum mechanics.
 We're not doing any of this.
 Some of you will recognize this as the table of contents, the first part of the table of contents of the famous textbook by Landau and Lifshitz.
 If you've studied Quantum Theory in undergraduate or graduate school, you've probably dealt with a textbook structured much like this one.

 And, you've probably been introduced to quantum mechanics as it was traditionally conceived: as essentially a mechanical theory, a theory of motion, with wave functions and particle representations, and on, and on, and on.

 So, we're not going to try to do that
 (this). What we're going to do instead is take a completely information theoretical approach, and we're going to characterize information transfer in a quantum theoretical way without any assumptions about mechanics or spacetime or any of that.
 So, instead of this, we're going to ask a simple question.
 By a simple question, I mean a question with just a "yes-no" answer or a binary answer.

 So, let's use "up or down" as our example question.
 And, to ask this question, we need three things:
 First, we need an action.
 We need a way of asking it.
 For example, making a sound or writing something down.

 Second, we need a thing that we can ask the question of.

 We need an environment or a friend or the rest of the world or an experimental apparatus or some system or other that we're going to act on to ask this question.
 And, the third thing that we need to ask this question is a shared language.
 And, it's the shared language that's often neglected in models based on physics.
 And, I think the importance of the shared language became clear in Classical Information Theory.

 And, it's become clear again, of course, in Quantum Information Theory.
 But this has only happened over the last few decades.
 So, what I want to do today is to construct in a step-by-step fashion a formal representation of these three things that we need to ask a simple question.
 And, what we'll find is that that formal representation is, in fact, Quantum Theory.

 So, it's the Quantum Theory that provides us with a formal representation of asking these simple binary questions.

 And of course, if you can ask a binary question, you can ask any finite number of binary questions.
 So, you can construct an arbitrarily complex, finite decision tree that ends up formulating an arbitrarily complex but still finite question.
 So, this really is a general model of communicative interactions between agents.

 So, let's go about this. And, talk first about the action of asking you a question.
 And, so, the first thing I want you to do is actually say out loud "up or down?". Actually, ask a question, and then note two things about what just happened.

 The first thing to note is that it took some time to do that.
 That action actually required a finite amount of time, a couple of seconds, not very long, but it's not zero.
 It always takes time to ask a question.

 And the second thing to note is that it took energy to actually say "up or down".
 It requires a little bit of exertion to ask a question.
 So, let's put those two together and define a word.
 We're going to define the word "action" to mean some energy that's been spent in some time.
 So, asking a question is an action and it qualifies as an action because it requires spending some energy in some finite amount of time.

 And, so, we can write this as action equals energy times time.

 Or I'll sometimes use the abbreviation E times T.

 And, action is always required when there's some inter-action or two-way-action between systems.
 So, whenever we talk about physical interaction, we're always talking about two systems doing something to each other that requires both energy and time.
 So, let's define another concept.
 A concept of a minimum action needed to ask a question, and, specifically, a question with a binary answer.
 And, we'll just pick a symbol to stand for that minimum action.

 And the symbol we'll use because it's conventional is "h".
 And it turns out that this h is Planck's constant, the number that Planck came up with when he was trying to solve the black-body problem back in 1900 that we talked about last time. And, recall that was the problem of characterizing the spectrum of radiation emitted by some physical system that was hot.
 How much energy comes out as a function of temperature.
 And, if you assume that the spectrum of energy coming out is continuous, you get predictions that are wrong.

 And, Planck got predictions that were correct by assuming that that spectrum was discrete and that this h represented the minimum amount of energy that could be emitted in a particular time.
 So, it represented the minimum energy times time or action.
 So, let's look at an example of that.
 And, here's an example that may be familiar.
 It's the example of your own visual system.

 So, in the retinal, the cells of your retinas, there are many, many molecules that are rhodopsins (of one variety or other) that respond to different wavelengths of visible light. And they have some efficiency for capturing light.

 And, let's just assume that they're optimally efficient, that they're as efficient as they could possibly be.
 And that means that they require the minimum amount of energy to change shape, which is what they do when they're impacted by light, to capture the energy and hence the information that's available in the light. And, the minimum energy to do anything that records one bit of information, so yes or no, up or down, is 0.7.

 So, log two of Boltzman's constant times the temperature.
 And again, we saw this last time.
 This is from roughly 1875 and was then built into Classical Information Theory by Shannon and then by Landauer in the mid-20th century.

 So, what we're doing is assuming that, since rhodopsin is optimally efficient, all it requires is this amount of energy to change shape.
 And, it's known experimentally, that rhodopsin takes about 200 femtoseconds to change shape.

 So, that's 200 times ten to the -15
 seconds.
 So, it's a very, very fast reaction, chemical reaction.
 So, we can just calculate what the action is. And, at 37 degrees centigrade, so human body temperature, KT is about 4.3 times 10 to the -21 Joule, and Joule is just a standard unit of energy. And, so we can multiply everything together:
 KT times 0.7 times this response time of 200 femtoseconds. Multiplied together gives you an action of about 6 times 10 to the -34 joule seconds.

 And, if you're familiar with quantum mechanics, you'll instantly recognize that number because it's very close to the value of Planck's Constant, which is 6.6 times 10 to the -34 Joule seconds.
 So, this says that rhodopsin is very near to optimal.

 The best it would be able to do would be Planck's constant.
 That's the minimum action that can be undertaken.
 So rhodopsin is clearly doing very well.
 It can't be as efficient as we're assuming it to be, but it's pretty efficient.
 So, this number Planck's constant (is) and this idea of a minimum action is not something we just pulled out of the air.

 It's something that one can observe.
 When you're looking at what real biological systems in particular do, and other physical systems do.

 So, let's think about the second component of this project of asking a question.
 And, that's the thing to be asked.
 And, we want to ask a very simple question.

 We want to have a theory of asking very simple questions.
 So, let's define the simplest thing that we can ask a binary question to.
 And, let's say this is the thing that we can ask a binary question of using just this minimum action h.
 So, we're going to ask for the minimal thing that it's possible physically to ask a question of.
 And, this thing needs a name, so let's call it a "qubit".

 And, that word is a contraction of "quantum bit".
 And, we can draw it like this.
 A little sphere with an arrow through it.
 That's called a "block sphere".
 And, we use a symbol |q>.
 And, that notation with the bar and the angle bracket is called a "bra notation".

 And, it originates with Durac.
 So, it's a traditional way of writing inner products, actually, in Quantum Theory to indicate the state of q.
 So, this thing called a qubit only responds to binary questions.

 So, it clearly can have only two states.
 The state that answers yes and the state that answers no.
 And, conventionally, we draw the arrow going up if the answer is yes and the arrow going down if the answer is no.

 And, so those are the two states that the qubit can be in when it's answered a question.
 So, now let's draw a picture for the act of asking a question of |q> in the state q, and let's draw it like this.
 This curvy arrow is the action of asking the question and getting the answer back.

 And, we're asking it of this minimum system, the qubit.
 And, let's call this entire act of H and write H acting on |q> by this expression H|q>.
 So again, we're developing the notation of Quantum Theory, which all of you who know the theory already will find familiar.

 So, the third thing that we have to build into this picture and into the theory is the shared language.
 So, we have to know what we mean by "up" or "down" if we're going to ask the question "up or down?".
 And, we have to have some representation of what it means for the qubit to distinguish up or down.
 So, let's say that to us, "up" and "down" mean this little diagram with an arrow that's labeled "up" on one end and "down" on the other end.

 So, we're defining "up" and "down" in a very simple way as just opposites.

 We don't know anything else about them except that they're opposites.
 So, this is a stripped-down one-bit question.
 We could have called them 1 and -1.
 We could have called them A and B.
 We could have called them anything.

 We're just indicating that up and down are two opposing concepts.
 And so, this object that we've used to make this definition of the relationship between our two words (up and down) is called a reference frame.
 It's a physical object that encodes a concept or a meaning.
 And, if you think about using language, using English, for example, you can understand me speaking in English because your brain has the right sorts of neural circuits to allow you to understand English and produce English using your hand and your mouth.

 And, those neural circuits are reference frames in your brain for understanding and producing English.

 And, they encode the relationships between different words.
 So, you all know about Chat GPT.
 You can think of all of the weights on all of the 10th to the 19th or however many parameters there are in GPT-4 as a reference frame that describes the relationships between words and phrases in English and many other languages.
 So, this idea of a reference frame is an instance of Landauer's principle, which is often summarized as saying that "information is physical".
 What that means is that information always has to have some encoding and that encoding, that object, can always be thought of as a reference frame.

 So, let's put all this stuff together.

 What we have now is a reference frame that defines the difference between up and down.
 We have an action that we've labeled h, and the action acts on this object, the qubit, which is in some state.
 And, what we've drawn here now is an experiment.
 And, you can think of the incoming part of the arrow that goes from the reference frame to the qubit as a preparation of the qubit.
 So, you can think of it as I'm doing something to the qubit to put it in a particular state like up because that's the state I want it to be in.

 And I can think of this returning part of the arrow as a measurement of the state that the qubit is actually in.

 So, if the qubit is actually in this state with the arrow pointing up, then I'm going to get back the answer up when I act on the qubit to measure its state.
 So, now we can recognize this action H as the Hamiltonian operator in Quantum Theory, which always takes some time, which we represent by an interval dt, to act on some state and in particular this binary state, |q>.
 So, this whole picture depicts the action of a very simple Hamiltonian operator.

 And again, I want to emphasize that we've just defined the qubit as the simplest thing that we can ask a binary question of.

 So how does this H work?

 We can use H to prepare this qubit in one of two states, which we're going to label "1" and "-1".
 The state 1 corresponds to the up direction, and the state -1 corresponds to the down direction. And, doing this to |q>, so, preparing |q> in one of these two states takes energy, and we know how much.
 Boltzman told us back in 1875 that the minimum energy to reduce the entropy of the universe by one bit is log two of KT.

 We saw that earlier when we were thinking about rhodopsin.
 So, we can say that acting with H always requires some number times KT, where that number is bigger than the log of two.
 Remember, the log of two is just in there to get units of bits of binary questions, as opposed to units of nats, which are questions that have e answers, where e is the exponential base, the natural exponential base.

 But we want to use units of bits, so we have to always have this factor of log two.
 So, this lets us write H in a particular way.

 We can take out this energetic term that Boltzman tells us we have to include beta times KT.
 And, what's left over is, in a sense, the pure representation of the action, stripping out the energy requirement.
 And, we're going to call that M, because M is the standard symbol to use in Quantum Theory for a measurement operator.
 And, M is now dimensionless.
 H has units of energy, KT is an energy, and M has no units at all.

 So, it's H without the energy.
 So, now we can ask, what is this operator M that we've defined as the simplest possible action on a qubit, but abstracting away the amount of energy that we have to use to act on the qubit.

 Well, what M does is just encode a bit or decode a bit.
 So, we can use this operator M to say: I want Q to have the value 1.
 I want it to be up, so I can sort of reach out with my operator M and grab |q> and turn it so that its arrow is pointing up.

 And that's the operation.
 That's called preparation in physics.
 It's what it means to prepare an experimental apparatus.
 For example, you actually grab hold of the apparatus, and you twist some knobs, and flick some switches to prepare it to be in some state.
 And you can use M to measure a state that isn't known.

 So, I can use M to grab a hold of |q> and look at it and determine whether it's in state 1 or -1.
 And, I can represent these as just a cycle that starts with measuring and then preparing, or that starts with preparing and then measuring.

 And, if I represent it that way, what I see is M having a value which is either the value I want to encode or the value that I have measured.
 And q and M act on that value and q to produce a particular state of q, to put q in a particular state, or to realize that q is in that state.
 And so, M is actually an identity acting on some value and q.

 So it maps 1 in |q> to 1 in |q>, and it maps -1 in |q> to -1 in |q> if you do the whole cycle of preparation and then measurement.
 And that makes sense.
 It's actually an axiom in some formulations of Quantum Theory that if I measure the state of some object, what I'm doing is also preparing it in that state.

 So, if I immediately measure it again, I'll see the same value.
 And that makes sense physically.

 If I, you know, put my coffee cup on the table and then I look for it, it's likely going to be on the table unless something else intervenes.
 Well, what does this mean?
 It means that we can do a little bit of algebra.

 It means that we can write this original expression of acting on q with our Hamiltonian in this somewhat more explicit form of using the energy beta KT and our operator M|q>.
 And what I get out of that is the energy beta KT multiplied by |q>.

 So H|q> equals E|q>.
 That's the Schrodinger equation.
 So that's one of the central equations of Quantum Theory.

 What it says is that this operator, H, is the total energy operator on a system.
 Its eigenvalues are the total energies of the system.

 And, we can now see where that energy is coming from in this very, very simple, stripped-down kind of representation of an action.
 The energy is the thermodynamic energy that has to be spent to determine one binary outcome (up or down).
 Now, if you're familiar with quantum mechanics, you will have seen exponentiated operators like the next line here of algebra.
 This operator P, which is time-dependent and which is the exponential of H multiplied by it over H bar, is called the propagator.

 It's the unitary operator in Quantum Theory, the operator that conserves probability or conserves information.

 And so, using the representation of H as beta KT, we can see that this operator P is just E to the minus beta M.
 If we recall the Wick rotation from the first session, this strange equivalence of it over H bar with one over KT (that) wasn't discovered until 50 years after the invention of Quantum Theory.
 And it's still a very debated thing.
 I mean, people worry about what this equation really means.
 But one thing that it means in this setting where H has this particularly simple form is that the propagator is now just the exponential of a number multiplied by this very simple strip-down operator that encodes a bit or decodes a bit.

 But we know something about the exponential propagator just by looking at its form.
 If you're again familiar with these sorts of exponential operators, you know that they're wave equations.
 And we can make sense of that using the diagram up above.
 What M is doing is just performing a cycle.
 It's just mapping 1 and |q> back to itself, or -1 and |q> back to itself.

 So we can think of M as just taking this object and flipping it back around until it gets itself again.
 And that kind of cycle can always be turned into a wave equation and e to the i over h bar times Ht is a canonical form of a wave equation, where the horizontal axis here on the wave is time.

 Or if you look at the little cycle that I've drawn as a circle with an arrow, it's the time of the thing spinning around like this, which is exactly the same thing as a wave traveling through time.
 So, that tells us something very important.

 It tells us that this equivalent expression, e to the minus beta M, is also a wave equation.
 So it tells us that this operator M has built into it some sense of time.

 It's the sense of time of this prepare measure cycle.
 And that's implicit in M, right?
 We've used the Wick rotation to get rid of what I'll end up calling the external time T, the objective time T.
 And we'll see in July where this internal time comes from, in terms of the Wick rotation.

 But we can say now that it's an agent-specific time.

 It's an internal time reference frame that's built into our idea of this system, Alice, that can act on the world. And it represents the time that's required to ask this question. Ok.

_Ander:_
 Can I ask a question at this point?

_Chris:_
 Yes.

_Ander:_
 So, on this slide with the operator M, I'm curious.
 How can the agent deploy in the operator M tell the difference or break the symmetry between preparation and measurement?

 Or are they just completely dual pictures?

_Chris:_
 Yeah, they're completely dual.
 So the agent never breaks the symmetry.
 The agent can't actually distinguish the act of preparing from the act of measuring.
 Every preparation is a measurement, and every measurement is a preparation.

_Ander:_
 Right.

_Chris:_
 That's, in fact, what this axiom of (unitarity) measuring a state leaves the particle in the measured state means.

_Ander:_
 Right.

_Chris:_
 So, yeah, mathematically, they're duals.

_Ander:_
 Thank you.

_Chris:_
 Okay, so let's now use this theory that we've developed to describe the interaction between Alice and Bob.
 And, let's think of a situation in which Alice prepares a qubit that Bob then measures, and then Bob prepares the very same qubit, and then Alice measures it.
 So, Alice acts with her Hamiltonian operator, which we'll label "Ha", and Bob acts with his Hamiltonian operator that we label "Hb".
 And, let's say that Alice prepares the qubit as in state up.
 And, Bob can then measure the qubit in state up and say: "Oh, the qubit is now up".

 And, if Bob then prepares the qubit in state down, Alice can measure the qubit in state down and say: "Oh, the qubit switched from the up that I prepared to down".

 So, Bob must have prepared it as down.
 So, what's happened here?
 Alice and Bob have actually shared a bit flip.
 Alice said "up" and Bob said "down", and Alice heard him say "down".

 So, they've shared this idea of change by interacting with each other.
 Now, this works as long as they mean the same thing by "up" and "down".
 So, we've implicitly assumed, in talking about them communicating, that they both have this reference frame that distinguishes "up" from "down".
 And, this is actually a completely general model of what I'll call a noiseless 1-qubit channel.
 Now, what does that mean?

 It's noiseless because there's nothing else in the picture, right?

 There's nothing in the picture that can jiggle the qubit when Alice and Bob aren't looking.
 Alice and Bob are the only systems we're talking about, and they share this qubit and there's nothing else in the picture.
 So, there's no kind of third party or environment or heat bath or anything like that that's going to mess with the qubit and disrupt their interaction.
 So, that's a noiseless channel and it's a 1-qubit channel because they just have one qubit that they're interacting with and they're alternately preparing and measuring its state.

 Now, clearly, if they can interact using 1-qubit, they can interact using any finite number of qubits.
 So, here's a picture of an N-qubit channel that Alice and Bob, which here I've labeled A and B, (because I took this figure from a paper) are sharing.
 And, Alice and Bob both have N operators, one for each of the N-qubits that they share.

 And, they just do this prepared measurement cycle on all N-qubits.
 So, you can think of Alice preparing the N-qubits, Bob measuring the N-qubits, and then Bob preparing and Alice measuring, and that allows them to exchange N-bit messages.

 And, we can make N as large as we want.
 And so, they can exchange messages of arbitrary complexity.
 And, if they share the meaning of "up" and "down", then they can exchange these messages with no noise, so they can communicate.
 And, we now have our theory of two communicating agents that are sharing arbitrary finite information.
 Now, I've labeled q1 through qN in this picture, a Holographic Screen.

 And, in fact, that's exactly what it is.

 Recall from Session 1 this slide illustrating the Holographic principle.

 Shannon made this point that a bit of information is an answer to a yes-no question.
 And so, we can write down a number of possible states.
 We can write down an entropy.
 And, the limiting case of that entropy is the entropy of a black hole.
 The densest possible encoding of information in space or on a boundary.

 And, this Holographic principle allows us to see any boundary, as we discussed in Session 1, as an encoding of bits.
 So, the previous boundary of these in qubits, we can think of as a Holographic Screen.

 Now, why is that important?

 It's important because it allows us to use this idea of holography and this idea of a fixed encoding of a message or a fixed encoding of an observable entropy at some density that was developed in Cosmology to talk about arbitrary quantum communication channels.
 So, we can import a whole bunch of theory that was done someplace else into Quantum Information Theory and see that it works perfectly because it describes exactly the same situation.
 Now, what does this tell us?
 Philosophically, it tells us that Alice and Bob can learn about each other at most N bits per communication cycle.

 So, the maximal amount of information that they can get from an observation is the N bits that the other one wrote on the screen.

 So, this tells us something very important, that when an agent is looking at their environment, which is this other agent, Bob, the amount of information that can be extracted from the environment is actually proportional to the size in bits of the boundary.
 And, the Holographic principle just makes that size finite in space.
 And, I said early on that there's no embedding spacetime in this theory, that Alice and Bob are not thought of as separated in space.
 But as soon as we use the Holographic principle, we can think of the boundary between them as having a spatial coordinate, even though they don't have a spatial coordinate.
 So, we'll get back to this point in September when we talk about theories of emergent spacetime, but all of these theories of emergent spacetime come back to this idea that boundaries can have spatial extent, even though the systems that they separate don't have any natural spatial description or natural spatial degrees of freedom.

 Okay, so now let's recall another picture from Session 1.

 We talked a little bit about Feynman's theory of scattering, the origin of Feynman diagrams, and the idea that if Alice prepares some system in some initial state and then measures the state later. If we want to calculate what the new state is, we have to take into account all of the possible paths that join the initial state that Alice prepared to the final state that Alice measured.
 So, what does that mean?
 I mean, here effectively, if we think of... Suppose I'm Alice and the boundary is my screen. I'm talking to the screen, and then later on, I'm going to measure the screen.

 And, between my preparation actions and my measurement actions, a bunch of stuff happens on the other side of the screen.

 And, if I want to predict what's going to happen on the other side of the screen, I've got to take into account every possible thing that could happen.
 And, I have to give some weight to those possible things that could happen.
 And, Quantum theory, in fact, tells you how to assign those weights to things that could happen, in order to make a measurement, given some theory of the mechanism that makes things happen.
 But the fact that all of the paths have to be counted is what unitary evolution means.

 This evolution that preserves information that doesn't take any away, it doesn't add any, it just represents it in different ways.
 So, if you look at this screen and imagine that Alice is interacting with her boundary and then she's interacting with her boundary again, it looks just like the previous screen.

 And the wavy red arrows are what's happening inside Bob.
 The wavy red arrows are a representation of what's going on inside Bob as he measures his side of the screen and then prepares his side of the screen.
 So, what Feynman is representing here is just the action of the environment or the action of the system while Alice isn't looking.

 Between Alice's preparation stage and her measurement stage, while Bob is doing his measurement and preparation.
 So this diagram is actually completely symmetrical.
 We could have drawn an arrow where the wavy red things are and drawn wavy red things where we talked about Alice.
 And, we'd have the same picture just from Bob's point of view.
 We can also think of this, of course, as Alice communicating with her future self by writing a memory record someplace in the world and then coming back and reading it.

 And if Alice writes a memory in the world and then comes back later on and reads it, she actually has to take into account some theory of all of the things the world might have done to her memory while she wasn't looking.
 So, this picture of Feynman's actually tells us a lot about memory.
 And, when we think about organisms running around in the world doing things like we do all the time, we tend to think of memories as things that are persistent and unchanging and all of that.
 But we know that that's not true.
 We know that memories degrade in various ways.

 We know that adversarial third parties can come and change what we've done so that they fool us into thinking that we've remembered something that we haven't.
 And so on, and so forth.

 That whole picture of memory is actually encoded in this picture that Feynman drew in the late 1950s to represent the scattering of particles.

 So, what we've done here is started with this simple idea of asking questions.
 And, we've actually constructed a fair amount of Quantum Theory.
 We constructed the Schrodinger equation. We constructed the unitary propagator.
 We constructed the idea of a reference frame, which we'll talk about intensely next time in July.
 So, we can sum this up by saying that Quantum theory simply is a theory of communicating agents.

 And that quantum mechanics, the theory that Feynman was complaining about in that earlier slide, that quantum mechanics generates this problem that seems intractable of how to understand measurement because the theory is in fact about measurement.

 It's not about mechanical motion at all.
 So, Quantum Theory actually tells us nothing about ontology.
 And, this is why the interpretations of Quantum Theory, the many worlds interpretation, where you have all these branching universes and so forth, are not really science.
 They're philosophy.

 They're attempts to understand an ontology that's generated by a theory that doesn't talk about ontology.
 It talks about communication between agents.
 But we've left something very important out.
 We've left out a consideration of what happens when Alice and Bob don't mean the same thing by "up" and "down".
 And, we've left out the famous phenomenon of entanglement - the spooky action at a distance, as Einstein called it.

 And, it turns out these things that we've left out are very, very closely related.

 And, we're going to see why in July.
 But I'm going to give you a brief preview now.
 So, what happens when Alice and Bob actually mean different things by "up" and "down"?
 What if their reference frames aren't aligned?

 Well, the first thing to note is that nothing in the theory says they have to be aligned.
 So, we have to consider the possibility that they're not.
 And, in fact, both Alice and Bob have to have what's called "free choice" of reference frame.
 When Alice prepares her instrument, she has to be able to prepare it any way she wants to, in order to do an experiment.
 And, when Bob makes up a sentence to tell Alice, he has to be able to choose any language he wants to use, he's a free agent in this way.

 And, if they don't have that freedom, it turns out they're entangled.
 So reference frame, nonalignment, and entanglement are very, very closely coupled.

 Now, the misalignment of reference frames is what produces superpositions of outcomes.
 So, if Alice makes her measurements with her up-down arrow arranged vertically, for example, but Bob prepares his qubit with his up-down arrow arranged at 90 degrees to Alice's, Alice is not going to have any idea what Bob did.
 I mean, she can't see distinctions in the left-right direction.
 She can only see distinctions in the up-down direction.
 So, all she can do is flip a coin.

 If she wants to know what Bob prepared, it's 50% likely he prepared up for her what she calls 1.
 And it's 50% likely that he prepared what's down for her.
 She can't tell.
 Now, if Bob's reference frame is pointing at about 45 degrees, so, up for him means 45 degrees off of Alice's up, then she can sort of tell what he did.

 If he's pointing 45 degrees from up, then she's probably going to measure up.
 And if he's pointing 45 degrees from down, she's probably going to measure down.
 So, her outcomes are 75% for 1 and 25% for -1.
 If he prepares at this 45-degree angle.
 So, we can write this in a particular way.

 We can say that the value that Alice gets acting with her M on a qubit that Bob prepared is some number times what she measures as up plus some other number plus times what she measures as -1, where those numbers, the squares of those numbers, add to 1.
 So, why do they have to add to one?
 Well, they add to one because of the Pythagorean theorem.

 1 is the distance, the total distance between the two outcomes.
 And A squared plus B squared are the other two sides of that triangle.
 So, another way to think of it is that the metric distance in possibility space is 1 and A squared and B squared are just the Euclidean distance components.
 Again, Euclidean distance is based on the Pythagorean theorem.
 So, this is the Born rule in Quantum Theory.

 It's the rule that tells us what happens when we're trying to measure a superposition and it tells us where these superpositions come from.
 We have a mismatch in reference frames between two agents that are communicating.

 So, if we go back to the Free Energy Principle, which is what this whole active inference class is about, and we formulate it in Quantum Theory, we get a very simple idea of what the Free Energy Principle is.

 The FEP and Quantum Theory just say that interacting systems are going to behave in a way that aligns their reference frames and that makes their communication as good as it can be.
 But since aligning reference frames perfectly leads to entanglement, the Free Energy Principle drives systems asymptotically toward entanglement.

 Well, the Principle of Unitarity says that all systems will approach entanglement asymptotically.
 So, we can see the FEP is actually a classical statement of the Principle of Unitarity.
 And, what we'll see in the next Session is why this is the case, why active inference, when we think of it quantum mechanically, is a way of talking about the Principle of Unitarity, which is the deepest axiom of Quantum Theory.

 And, we'll also see that this question of alignment becomes more and more complex as the complexity of the messages that the systems are trying to communicate to each other increases.
 And that message complexity correlates with system complexity.

 So that aligning complicated systems is very hard, although aligning very simple systems is fairly easy.
 And, if you think about what's the simplest possible theory in science, it's particle physics, because you're dealing with these very simple things that interact in extremely simple ways.
 And, the really difficult parts of science are things like sociology, where you're dealing with incredibly complicated systems like humans that interact in incredibly complicated ways.
 And, all we have are very vague kinds of folk theories of how that works.

 But we know from that example that aligning complex systems is extremely difficult.

 So, humans don't get along very well.
 So, the 2nd Session well, the 2nd discussion section which Andrew will be leading is on Saturday, the 1st of July, a couple of weeks from now.
 The 3rd lecture Session will be on July 13th and I hope you all will contribute to the interactive question and answer session on the web and show up for the discussion on Saturday, the 1st of July and join us again in July for the discussion of quantum reference frames and reference frame alignment.
 So thank you very much.

_Daniel:_
 Thank you, Chris.

 All right.

 Thank you all again.
 Please check out the course syllabus, ask questions through the site, and see you at the discussion.
 See you next time.

 Thank you.
 Bye.
