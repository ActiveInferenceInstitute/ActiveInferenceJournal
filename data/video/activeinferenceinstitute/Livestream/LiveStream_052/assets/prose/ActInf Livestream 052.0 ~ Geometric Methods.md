00:13 _Daniel Friedman:_

Hello and welcome.
This is ActInf Lab Livestream number 52.0, and it is February 28, 2023.

00:25 Welcome to the active inference institute.
We're a participatory online institute that is communicating, learning and practicing applied active coherence.
You can find us at the links here on this slide.
This is a recorded and an archived live stream, so please provide feedback so we can improve our work.
All backgrounds and perspectives are welcome and we'll be following video etiquette for live streams.

00:52 Head over active coherence.org if you want to learn more and participate in learning groups and projects at the institute, including these live streams.
Well, we're here today to learn and discuss the paper Geometric Methods for Sampling, Optimization, Inference and Adaptive Agents by Alessandro Barp, Lancelot Costa, Guilherme Franca, Karl Friston, Mark Girolami, Michael Jordan, and Grigorios A Pavliotis. This video, like all Dot-Zero videos, are anintroduction for some of the ideas.
It is not a review or a final word, and as we have joked before, it's more than anything a call for help.
So if you're curious about these topics, if you're knowledgeable about these topics, we would really look forward to you getting involved in the upcoming 52.1 and 52.2 discussions, as well as in an ongoing basis to help us understand some of the technical details.

02:03 This is going to get technical ant times and certainly beyond the technicalities I understand, though I am looking forward to presenting them and it'll be great to have those who have backgrounds of all different types to come together and talk about this awesome work.

02:24 Also, a big thanks to Ali and Candon for the assistance, technical and moral.
During the preparations here in 52.0, we're going to bring up some aims and claims, read the abstract, look at the roadmap and talk about the keywords, and then we will walk through the paper with an emphasis on the figures, formalisms and key points.
In the coming weeks, we're going to be discussing this paper with one or more authors.
So, as usual, get in touch if you want to participate or if it's after the fact, you can still get involved.
We can start with an introduction or a warm up.

03:08 I'm Daniel, I'm a researcher in California, and I'm tempted to say, just totally honestly, I'm happy to get this one over with, but that sounds a little bit different than I might intended to be.
I'm really excited to dive into this work, which is going to be approaching active inference from an angle that we haven't necessarily highlighted on these streams.
So I think it's going to be a fascinating discussion.
It's going to run the gamut, span the gap however you choose to see it, between technical sophistication and intuition, which is a great place to be.
So I've been really excited and motivated to prepare, and I'm looking forward to the dot zero we're doing right now and to the upcoming discussions.

03:58 So let's jump in with the big questions that might motivate one to read this paper, this kind of paper, even if they were not familiar with the authors or topics.
And these are just a few ways to write it up.
Of course, not the only ways.
So, first question how can we effectively and efficiently navigate information geometric or information theoretic landscapes?
And how can we tackle that question from an analytical, which is to say equation based as well as a computational, which is to say real implication based perspective?

04:35 Often it's really fun, intuitive, natural to talk about information theory, even for those who haven't taken the technical prerequisites.
And this work may help us navigate to a space where we're able to think with good intuitions about information geometry, information theory, and also make sure that those intuitions are going to be caught by our technical tools.
Second, how can we optimize inference in complexity models, including cases where we are doing inference on action as a parameter, also known active inference lab?
Optimization and functional analysis, as we'll come to see soon has long been interested in these complex or challenging models that are right at the margin, right ant the border of what is trackable or not.
Given the computational hardware that modelers have access to, for example, big data sets, high dimensional state spaces, complex dynamics and so on, how about cases where we're also interested in doing parametric inference and optimization on action or action plans as a parameter?

05:52 Also known active inference lab.
And third, what technical underpinnings support the rigor and applicability of active inference and what special cases are revealed when we consider possibilities and constraints?
These are those two branches of analytical and computational coming back again.
We want to make sure that when we're thinking within the active inference paradigm, the active coherence ontology is the language that we're speaking and that there's a technical rigor to what's being discussed.
Additionally, we want to make sure that it's not just an analytical rigor, but it's also going to be computationally plausible tractable or maybe even preferable.

06:34 That would be awesome.
Those are the questions that at least appeared.
We are discussing this paper Geometric Methods for Sampling, Optimization, Inference and Adaptive Agents by Barp and Costa at all shared first authorship and it was published on active.
I'll just note a few key claims from this paper.
They wrote Our goal in this chapter is to discuss the emergence of natural geometries within a few important areas of statistics and applied mathematics, namely optimization, sampling, inference and adaptive agents.

07:11 That's the title.
We provide a conceptual introduction to the underlying ideas rather than a technical discussion highlighting connections with various Fields of mathematics and physics.
Well, I can tell you that they do make connections with various Fields of mathematics and physics, though.
Whether it is a concept introduction or a technical discussion is all going to be about your perspective.
Third, to illustrate a generic use case for the previous methodologies that are going to be discussed.

07:43 We consider active inference a unifying formulation of behavior, subsuming perception, planning and learning as a process of inference.
So inference on adaptive agents is not necessarily new.
It goes by reinforcement learning, machine learning, and so on.
However, to use those methodologies in the context of active inference a unifying formulation of behavior is something that the authors are bringing forth here.
And last, we describe decision making under active inference using information geometry, revealing several special cases that are established notions in statistics, cognitive science and engineering.

08:25 So active inference is not just unifying, it's going to be shown to be generalized as well.
Which is to say that special cases of the generalization emergence different formalisms that were known disparately across Fields onto the abstract they write in this chapter, we identify fundamental geometric structures that underlie the problems of sampling, optimization, inference and adaptive decision making.
Based on this identification, we derive algorithms that exploit these geometric structures to solve these problems efficiently.
We show that a wide range of geometric theories emerge naturally in these Fields, foraging from measure preserving processes, information divergences, Poisson geometry, and geometric integration.

09:26 Specifically, we explain how, one, leveraging the symplectic geometry of Hamiltonian systems enable us to construct accelerated sampling and optimization methods.

09:38 Two, the theory of Hilbertian subspaces and Stein operators provides a general methodology to obtain robust estimators and three, preserving the information geometry of decision making yields adaptive agents that perform active inference throughout.
We emphasize the rich connections between these field e G inference draws on sampling and optimization, and adaptive decision making assesses decisions by inferring their counterfactual consequences.
Our exposition provides a conceptual overview of underlying ideas rather than a technical discussion, which can be found in the references herein.
And indeed, there are several hundred references in this paper.
Let's go to the roadmap.

10:29 So first we can start on the right side.
Here's an active agent room doing accelerated optimization in the carpool lane, looking ahead to the almost desert like visual representation of active inference.
That's where we're going to go.
And on the right side, it's just some cars.
One of them is accelerated, the other one isn't.

10:55 The paper begins with an introduction and then in section two gets into the topic of accelerated optimization covering the areas of principle of geometric integration, conservative flows and symplectic integrators rate matching, integrators for smooth optimization, manifold and constrained optimization, gradient flow as a high friction limit, and optimization on the space of probability measures.
In section three, they turn from accelerated optimization in general to Hamiltonian based accelerated sampling.
The subsections of three are optimizing diffusion processes for sampling and Hamiltonian Monte Carlo.
From the Hamiltonian based accelerated sampling, they turn towards doing statistical inference with kernel based discrepancies.
In section four, the subsections are topological methods for Mmds smooth measures and KSDS the canonical Stein operator and point Curray duality kernel Stein discrepancies and score matching information geometry of Mmds and natural gradient descent minimum Stein discrepancy estimators likelihood coherence with generative models.

12:06 Finally, in section five adaptive agents through active coherence, they're going to bring it home to active inference.
Section five one modeling adaptive decision making, behavior agents and environments, decision making in precise agents, the information geometry of decision making.
And five two realizing adaptive agents, the basic active inference algorithm sequential decision making under uncertainty world model learning as inference and scaling active inference.
A quick note we have all the formalisms entered Hinton our zero teams Coda document.
There are 46 numbered equations in this paper and 83 overall.

12:57 We're going to bring in some, but not all of these formalisms in the dot zero video.
And we're ready to bring in more during the dot one one and dot two discussions with the authors just for those who are watching along.
I'm going to scan through all of the formalisms from our Coda.
And again, for those who want to help get involved with a dot zero preparation.
This is a little bit of what dot zero preparation looks like.

13:25 I'm going to now scroll through the formalisms just in case anybody wants to screenshot or see them.

14:01 Great.
On to the keywords.
Keywords of the paper are information geometry, hamiltonian Monte Carlo, Stein's method, reproducing kernel variational, coherence, accelerated optimization, dissipative systems, decision theory and active inference in no particular pedagogical order.
Let's start with decision theory from the Stanford Encyclopedia of Philosophy.
The article begins Decision theory is concerned with the reasoning underlying an agent's choices, whether this is a mundane choice between taking the bus or getting a taxi or a more far reaching choice about whether to pursue a demanding political career.

14:49 Decision theory is about agents making decisions, cognitive things making decisions.
And we can take a peek ahead to figure three, which is shown here as well as invoke some of the keywords that we're about to walk into now.
So if this is your first time hearing some of this vocabulary or you're super familiar, either way, it's great.
In this paper and in this discussion, we're going to see how different decision theoretic settings such as no ambiguity, no ambiguity or no coherence, no extrinsic value and no intrinsic value are going to be operationalized within an information theoretic formalism an information geometric formalism and specifically one that we're able to do accelerated inference on using variational methods.
We're going to be involving action as a parameter.

15:45 So we can call that active coherence and that's how we're approaching decision theory and getting from here to there with all those fun stops in between.
Let's go to information theory.
The paper in the introduction writes of particular relevance to this chapter is information geometry, E g, the differential geometric treatment of smooth statistical manifolds whose origin stems from a seminal article by Rao 23, who introduced the Fishermetric tensor.
On parameterized statistical models and thus a natural domain geometry that was later observed to correspond to an infinitesimal disturbance with respect to the Kolback libelr or Kale divergence.
So going into citation 23 and 24.

16:35 Citation 23 is Rao from 1992.
And Rao wrote the objective of the paper is to derive certain inequality relations connecting the elements of the information matrix as defined by Fisher 1921 and the variances and covariances of the estimating functions.
A class of distribution functions which admit estimation of parameters with the minimum possible variance has been discussed.
The concept of distance between populations of a given type has been developed, starting from a quadratic differential metric defining the element of length.
So I'm only going to give the disclaimer one time.

17:13 Everything in red text is beyond speculative.
It's just priming the pump for discussions with those who know more and with those who know less.
And it's just a first pass that we're going to continue to develop on.
But broadly, if we can compute inequality relationships, which this paper developed in 1992, we can bound estimators, test for relative improvements and basically do stuff with those distinctions.
And if we can compute certain kinds of statistical distances such that a distance requires a length metric, we can find optimal estimators of parameters, specifically their variances and covariance structure in principle and in practice by finding that maximum informational alignment to other estimators or empirical data.

18:07 So we'll often say, like if you had the radial parameterisation, you'd be predicting as well as you could.
And so we want to be able to operationalize that using distances and metrics and citation 24 this is an invariant form for the prior probability and estimation problems by Harold Jeffries.
And Jefferies wrote It has shown that a certain differentiate form depending on the values of the parameters in a law of chance, is invariant for all transformations of the parameters when the law is differentiable with regard to all parameters.
For laws containing a location in the scale parameter, a form with a somewhat restricted type of invariance is found even when the law is not everywhere differentiable with regard to the parameters.
This form has the properties required to give a general rule for stating the prior probability in a large class of estimation problems.

19:02 So if all the parameters in our model, whether there's one, two or more, are differentiable, which is to say they're smooth, et cetera, et cetera, there are technical details, then there are certain transformational invariances.
So just like every Gaussian distribution, by shifting it and stretching and shrinking it, you can map those on to each other.
It's like that.
It turns out that some of those constraints can even be somewhat relaxed.
For example, this approach may still be effective even where parameters are not differentiable everywhere.

19:38 And this is big for helping us do Bayesian estimation, which can be seen as a special case of informational transformations or of manipulations of statistical distributions in the information theoretic or information geometric sense.
Functional analysis.
So let's begin as tradition in our year 2023 with a brief quote from Chat GPT how is functional analysis helpful for us who are learning and applying active inference?
I'll just read the last section.
Overall, functional analysis provides a powerful mathematical toolset for understanding and analyzing the principles active coherence lab, and one can read more.

20:25 Functional analysis is the study of functions.
And here we see one way of showing what a function does in terms of being this box f of x that takes in an input, an argument x and outputs a result y and also that can be understood as a mapping between or amongst spaces.
And there's a lot more to go into.
Just wanted to bring up that in math, sometimes people have analyzed functions and their properties and we're interested in the properties of a special class of functions, which are probability distributions, well behaved probability distinctions.
What do we do with those probability distinctions?

21:13 Well, one thing we might want to do is sample.
So the paper writes sampling methods are critical to the efficient implementations of many methodologies.
Most Modern samplers are based on Markov chain Monte Carlo methods, which include slice samplers, piecewise deterministic, Markov chains and so on.
The original Hamiltonian Monte Carlo or HMC, which we're going to get to algorithm, was introduced in physics to sample distributions on gauge groups for lattice quantum chromodynamics.
It combined two approaches that emerged in previous decades, namely the Metropolis Hastings algorithm and the Hamiltonian correlation of molecular dynamics.

21:59 So the way that they state it in the beginning of section three of the paper is the purpose of sampling methods is to efficiently draw samples from a given target distribution row or more commonly, to calculate expectations with respect to row.
By equation 33 and other, they write, Modern Hamiltonian Monte Carlo which again we're going to get to in a second relies heavily on symplectic integrators another keyword to simulate a deterministic dynamics responsible for generative distant moves between samples and thus reduce their correlation while at the same time preserving important geometric properties.
Now, we want to make our samples as informative as possible.
If we're just foraging samples and it's the same sample again and again, one can imagine that it is uninformative.
Conversely, one can imagine a situation where samples are informative and that is brought into practice by making sure that the samples are minimally correlation with each other, as noted above.

23:10 And this also has analogy in cryptography.
So if we're sampling something where the successive samples are 99% correlated, you can imagine that you're over sampling.
So you're taking 10,000 frames per second of a YouTube video with 30 frames per second.
I think I'm streaming at 25 frames per second right now.
Conversely, if one were to sample every ten minutes, then their correlation structure would also not capture the videos 25 frames per second.

23:43 So in order to generate good and large moves in the space, we would need perfect knowledge of what the space is or how it's generated, which is sometimes knowable in cryptography, however empirically, we need to use heuristics and statistical approximations.
So this is the applied statistics angle on the analytical relationships that we're going to be talking about.
And it's going to come up again and again this tension between analytical formulations, what's true in principle, and the statistical or numerical or computational applications.
Two Hamiltonian Monte Carlo from Wikipedia the Hamiltonian Monte Carlo algorithm, originally known as hybrid Monte Carlo still HMC is a Markov chain Monte Carlo method for obtaining a sequence of random samples which converge to being distributed according to a target probability distribution, for which direct sampling is difficult.

24:45 So just a few first pass reflections.

24:48 We're sampling, which is to say Monte Carlo.
And Monte Carlo is harkening back to a different time when gambling was done in Monte Carlo and the state space of all the hands of poker were too vast to compute analytically or equations were not known.
And so what one used to do, and still does, is draw samples and say, well, I don't know if this is the final estimate on how likely a royal flush is, but from the 2 billion hands that I sampled, there were two royal flushes.
And so it's one in a billion based upon my sample.
So we're sampling because this is a complex distinctions for which an analytical solution is not possible, not known, not relevant, or not trackable computationally.

25:32 So there's various situations where we want to sample and we don't necessarily have an analytical solution.
When we're sampling from a converged stationarity, hashtag live stream 26 of a statistical landscape from a numerical perspective, we understand that landscape well enough to do coherence.
So imagine that we're sampling height estimates from GPS locations in the X and the y coordinates, and we're getting a z value in our sample.
At some point we can say we're unsurprised by new samples.
At that point we understand the landscape well enough to do statistical inference.

26:11 And just like the frames per second in the previous example, one can imagine if the landscape is changing on the spatial scale of 1 mile and you're sampling every millimeter, you might be over sampling.
If you were sampling every league, maybe you'd be too coarse grained with your samples.
And so one reason that comes up in science all the time for using sampling is that the search space might be just too large.
For example, the combinatorics of a phylogenetic tree with a thousand species might be vast.
And so it might be better to say something like, well, 99% of the million samples we drew were consistent with X, because an analytical solution or a brute force search, neither might be possible.

26:56 And the Wikipedia wrote this sequence of samples can be used to estimate integrals with respect to the target distribution.
So sometimes we're sampling not from the target distribution itself, but rather from a distribution that is related or transformed from the target distribution.
This is because sampling directly from the target distribution might be difficult or less than perfectly informative.
So we might, for example, hint hint sample from the derivative of the target which might help us identify points where, for example, the derivative is flat in all directions.
In the case that we're sampling from a derived landscape of the target distribution, this is called a symplectic integrator.

27:41 So let's look at what a symplectic integrator is.
So first, backing up to what is differentiate geometry.
Differential geometry is a mathematical discipline that studies the geometry of smooth shapes and smooth spaces, otherwise known as smooth manifolds.
Symplectic geometry is a branch of differential geometry and differential topology that studies Symplectic manifolds, that is, differentiable manifolds equipped with a closed, nondegenerate two form.
Symplectic geometry has its origins in the Hamiltonian formulation of classical mechanics, where the phase space of certain classical systems takes on the structure of a symplectic manifold.

28:24 So the keyword density is high.
These topics are all very closely linked from the paper.
It has been known for a long time that the class of symplectic integrators is the preferred choice for simulating physical systems, only the finest for our simulations of physical systems.
These discretization techniques are designed to preserve the underlying symplectic geometry of Hamiltonian systems and they also form the basis of Hamiltonian Monte Carlo or hybrid Monte Carlo methods.
We're going to come back to this tension again and again, which is what good is an in principle, smooth and differentiable analytical correlation.

29:08 If our discreditization scheme, the way that we actually implement the steps on a computer, are inferior, we might ruin all those nice properties that we work to get about the analytical form.
We might just throw those out when we discretize it coarsely or inappropriately.
So what is the symplectic integrator?
It's a numerical integration scheme for Hamiltonian systems.
Symplectic integrators form the subclass of geometric integrators, which by definition are canonical transformations.

29:42 They're transformations we know a lot about.

29:47 Symplectic integrator schemes are referring to, again, just broadly, both the analytical formulations and the software packages and approaches that we can use to implement those formalisms.
And these integration schemes are useful across difficult estimation problems, which is why they're used to study nonlinear dynamics, molecular dynamics like protein simulation, discrete element methods, accelerator physics, plasma physics, quantum physics, celestial mechanics.
The time evolution of Hamilton's equation is a symplectomorphism, meaning that it conserves the symplectic two form.
A numerical scheme is a symplectic integrator if it also conserves this two form.

30:40 Let's hear more if this is not correct or not complete.
But the one form is like the differentiation and integration of a line.
The two form is like the differentiation and integration of a surface.
And the three form is like integration or differentiate of a volume.
And John Denker has a great blog post on the basic properties of a symplectic integrator.

31:04 Some really interesting quotes that are good to just keep in mind when we're hearing about all these avenues we're going to be exploring in the paper.
A symplectic integrator can serve the area in phase space delimited by an ensemble of systems.
For a periodic system, there is an area that is conserved, namely the area inside the phase space orbit of the system.
The main reason for mentioning the orbit is to make the point that there are lots of different things with dimensions of area in phase space.
Some are conserved and some not.

31:36 Some are interesting and some not.
You have to specify which sort of area you are talking about.
So another thing that's going to arise is we're interested in very well behaved outcomes from a very specific or constrained, still broad, but definitely constrained set of distributions.
For example, distributions that can be interpreted in an information theory sense as probability distinctions.
What was that mention of the Hamiltonian and the shadow Hamiltonian?

32:12 So the author is right.
For symplectic brackets, which is the kind of operation that reflects the symplectic integrator, the existence of a shadow Hamiltonian can be guaranteed beyond the case of splitting methods, e.
G for variational integrators, which use variational inference, which use a discrete version of Hamilton's principle of least action.
And we've heard it before that free energy principle is a principle of least action for inference and action and more generally for most symplectic integrators in which the symplectic bracket is preserved up to topological considerations described by some technicalities that we can learn about.
As we shall see, such geometric integrators can be constructed by leveraging the shadow Hamiltonian property of symplectic methods on higher dimensional conservative Hamiltonian systems.

33:08 In short, as a consequence of having shadow Hamiltonian, such geometric integrators are able to reproduce all the relevant properties of the continuum system.
These arguments are completely general.
So even before one knows what the shadow Hamiltonian necessarily is, the authors are letting us know that if we can discretize the shadow Hamiltonian appropriately through symplectic integration, we can provide a inclination scheme that ends up staying consistent and compatible and all down the middle with the analytical properties that we've worked so hard to get.
And there were some different papers that were cited and some that were found during research.
This paper Time Step in Shadow Hamiltonian and Molecular Dynamics Simulations by Kim demonstrates symplectic integrators on the simplest possible system a simple harmonic oscillator.

34:11 So if one wants to go to a technical example, but one that builds intuition, that's a great place to start.
And from the Wikipedia article on energy drift, these integrators do not in fact, reproduce the actual Hamiltonian mechanics of the system.
Instead, they reproduce a closely related shadow Hamiltonian whose value they conserved many orders of magnitude more closely.
The accuracy of the energy conversation for the true Hamiltonian is independent on the time step.
So if we can, for examples, just metaphorically speaking, capture a high evolution image of the shadow, then we'll be able to know something, do something with the actual some technical details on Stein's method, which is a general method in probability theory to obtain bounds on the distance between two probability distributions with respect to a probability metric.

35:11 And Stein's method is used in the context of Stein operators and Stein class, which we're going to get to in the subsequent discussions.
Reproducing Kernel our discussion of inference builds upon the theory of Hilbertian subspaces and in particular, reproducing kernels.
These inference schemes rely on the continuity of linear functionals such as probability and Schwartz distributions over a class of functions.
To geometrize the analysis of integral probability metrics, which measure the worst case integration error, we shall explain how maximum mean kernelized and score matching discrepancies arise naturally from topological considerations.
So we've added some background links here to the slide, but it'll be a Brea place to start with.

36:01 Authors, what is a reproducing kernel and how is it used?
In this paper onwards, through the keywords we go accelerated optimization and variational inference.
So here's a 2016 paper from Michael Jordan and other authors and some quotes from the abstract.
Accelerated methods achieve faster coherence rates than gradient methods, and indeed, under certain conditions they achieve optimal rates.
However, accelerated methods are not dissent methods and remain a conceptual mystery.

36:36 We propose a variational continuous time framework for understanding accelerated methods.
We provide a systematic methodology for converting accelerated higher order methods from continuous time to discrete time.
Our work illuminates a class of dynamics that may be useful for designing better algorithms for optimization.
And this is going to be, again, something awesome to discuss.
We've talked about, on many streams, variational inference in the context of gradient based optimization.

37:11 For example, the ball is rolling to the bottom of the bowl, bottom of the hill, and what you can do is you can take the gradient div, grab curl and all that of where the ball is and just go downhill.
And if you designed the hill to be the right shape, or you're using a chosen family of variational estimators that are the right shape, are a good shape, well behaved shape, then you follow the gradient on down.
And that's how we've talked about variational inference.
Accelerated optimization is going to be accelerated from that.
And so it's fun to think about and it'll be great to talk about.

37:51 Dissipative systems.
The vast majority of statistics and machine learning applications involve solving optimization problems.
The author is right.
Accelerated gradientbased methods and several variations thereof have become workhorses in these Fields.
Recently, there has been great interest in studying such methods from a continuous time limiting perspective.

38:13 Such methods can be seen as first order integrators to a classical Hamiltonian system with dissipation.
This raises the question on how to discretize the system such that important properties are preserved, assuming the system has fast conversions to critical point and desirable stability properties.
Originally, such a theory of geometric integration was developed with conservative systems in.
Mind, while optimization in optimization, the associated system is naturally a dissipative one.
More recently, it has been proved that a generalization of symplectic integrators to dissipative Hamiltonian systems is indeed able to preserve rates of coherence and stability, which are the main properties of interest for optimization.

38:58 So from the Wikipedia on Hamiltonian systems an example of a time independent Hamiltonian system is the harmonic oscillator.
So it's just a frictionless spring oscillating around the Hamiltonian of the system does not depend on time, and thus the energy of the system is conserved.
And so we can say that that is a conservative Hamiltonian.
If the Hamiltonian decays in time, it is dissipative.
Recently, the advances of these authors and others have extended our ability to make distinctions of dissipative Hamiltonians that respect the rates of conversions and stability, which are the main properties of interest for optimization.

39:47 And we've talked about Hamiltonians on Livestream number 49 with Dalton Sakthivadivel Devil on Bayesian mechanics.
So pretty cool.
What is conservative?
What is dissipative?
We'll explore as the final keyword here, I just wanted to start with a blank slide on active inference and see what happens in 52.1.

40:11 So consider the slide to be blank and for the authors and discussants looking forward to hearing Hohwy.
Are we approaching active inference?
Given everything that we've just loaded onto the table and everywhere that we're about to go with the paper?
Let's get into it.
Section One introduction so, the authors begin with differential geometry plays a fundamental role in applied mathematics, statistics and computer science, including various domains.

40:45 Citations one through 22, which can be shown here.
Various citations from this well cited paper.
The geometric study of statistical models has had many successes, ranging from statistical inference, where it was used to prove the optimality of maximum likelihood estimator, to the construction of the category of mathematical statistics generated by Markov morphisms.
So what are Markov morphisms from Ncat lab?
The formalism of Markov categories can be thought of as a way to express certain aspects of probability and statistics synthetically.

41:26 In other words, it consists of structure and axioms, which one can think of as fundamental in probability and statistics, which one can use to prove theorems without having to use measure theory directly.
Intuitively, for the purposes of probability, a Markov category can be seen as a category where morphisms behave like random functions or Markov kernels, hence the name.
So, just some red text speculation.
It was a big success and a breakthrough to think about the category from a formal category theoretic perspective, to think about the category of statistical distinctions from an information geometric perspective.
This means that we can understand many analytical properties and transformations of statistical distributions hashtag Bayesian and develop general methods that work for that whole category, like accelerated optimization.

42:26 And the applications are vast.

42:31 Originally, such a theory of geometric integration was developed with conservative systems in mind.
While in optimization the associated system is naturally a dissipative one.
Nevertheless, symplectic integrators were exploited in this concept.
More recently, it has been proved that a generalization of symplectic integrators to dissipative Hamiltonian systems is indeed able to preserve rates of convergence and stability, which are the main properties of interest for optimization.
So, citation nine, what is it about 2021 paper on dissipative symplectic integration with applications to gradient based optimization by some of the authors, and it's interesting to pull out some quotes from the abstract and just hear a little bit about what they're up to.

43:21 Recently, continuous time dynamical systems have proved useful in providing conceptual and quantitative insights into gradient based optimization widely used in Modern machine learning and statistics.
An important question that arises in this line of work is how to discritize the system in such a way that its stability and rates of convergence are preserved.
So this is the sampling problem.
In continuum time, the math is continuous and nice.
However, the sampling problem which actually comes into play when we use Modern computational methods that are implemented on discrete time, space and constraints, what happens when we use unconventional computing?

44:00 That's an interesting discussion question, but in active today, the discretization approach is going to matter a lot.
In this paper, we propose a geometric framework in which such discretizations can be realized, systematically enabling the derivation of ratematching algorithms without the need for a discrete coherence analysis.
More specifically, we show that a generalization of symplectic integrators to nonconservative, and in particular, discipline of Hamiltonian systems is able to preserve rates of convergence up to a controlled errors.
So this is the advance of this paper that within a controlled error good enough, they can model conservative and nonconservative, even dissipative Hamiltonian systems.
Moreover, such methods preserve a shadow Hamiltonian despite the absence of a conversation law extending key results of symplectic integrators to nonconservative cases, our arguments rely on a combination of backwards error analysis with fundamental results from symplectic geometry.

44:57 We stress that although the original motivation for this work was the application of optimization, where dissipative systems play a natural role, they are fully general and not only provide a differential geometric analysis for discipline of Hamiltonian systems, but also substantially extend the theory of structure preserving inclination.
So they made this generalization.
In the case of optimization, however, it's exciting that it extends even deeper into the math and the symmetry.
Those are a few highlights from section one on to section two.
Accelerated optimization vroom, vroom.

45:34 Here we go.
So there are going to be a lot of slides from sections two through five, and to keep the video a reasonable length, I'm going to just highlight a few pieces.
Not even necessarily what I intended to highlight, but I'm just going to go for it so we can get through it.
Section two we shall be concerned with a problem of optimization of a function finding a point that maximizes V of Q or minimizes negative V of Q over a smooth manifold M r in the real numbers, many algorithms and optimization are given as a sequence of active inference.
Even when these algorithms are seen as distinctions of a continuum system whose behavior is presumably understood.

46:26 It is well known that most discretizations break important properties of a system, and they continue to write.
The analysis of such finite difference iterations is usually challenging, relying on painstaking algebra to obtain theoretical guarantees such as conversation to a critical point, stability and rates of conversation to a critical point.
Even when these algorithms are seen as discreditizations of a continuum system whose behavior is presumably understood, it is well known that most discreditizations break important properties of the system.
It can't be highlighted enough when we implement optimization algorithms on Modern computers, we have to make discreditizations in space and time and in practice.
So even if the analytical properties of the distribution are totally fire, when we try to solve and fit models to empirical data, unless we also match that elegance and power with a inclination approach, we end up failing to realize analytical promises.

47:31 2.1.
The principle of Geometric Integration fortunately, the author's right here comes into play one of the most fundamental ideas of geometric integrations.
Many numerical integrators are very close exponentially in the step size to a smooth dynamics generated by a shadow vector field.
A little whisper of a shadow Hamiltonian and the shadow vector field is a perturbation of the original vector field.
This allows us to analyze the discrete trajectory implemented by the algorithm using powerful tools from dynamical systems and differential geometry, which are a priori reserved to smooth systems.

48:09 So we're going to be able to discretize our cake and have it be smooth too.
Crucially, while numerical integrators typically diverge significantly from the dynamics they aim to simulate, geometric integrators respect the main properties of a system in the context of optimization.
This means respecting stability and rates of coherence seems like a good idea to respect the main properties of the system.
This was first demonstrated in nine and further extended in ten.
Our discussion will be based on these work.

48:43 So citation Nine, Franca, Jordan and Vidal mentioned previously and citation ten, Franca, Mark, Girolami and Jordan optimization on manifolds a symplectic approach authors previous work So big development we can use geometric rather than course numerical integrators, so our sampling based optimization schemes, including their discordization, respect the main properties of the system.
Sounds great.
Section Two Two conservative flows and symplectic integrators as a stepping stone, we first discussed the construction of suitable conservative flows.

49:30 These are very well studied and they're very intuitive.
More intuitive.
To construct vector Fields along the derivative of x, which is the function of flows along which some function is constant, we shall need brackets geometrically.
These are morphisms x star to x, also known as contravariant tensors of rank two in physics.
So calling back the two form and the brackets, importantly, vector Fields that preserve f correspond to bracket vector Fields in which B is antisemitic.

50:10 Constructing conservative flows is thus straightforward.
Unfortunately, it is a rather more challenging task to construct efficient discretizations that retain this property.
Most well known procedures, namely discrete gradient and projection methods, only give rise to integrators that require solving implicit equations at every step.
And they may break other important properties of the system inclination.
96 this is the issue again.

50:40 No matter how nicely behaved in principle, our analytical underlying smooth differentiable function is if we discretize it and we chop it up in a way that's inappropriate.
We don't respect the properties of the system, we don't end up with being able to realize those analytical promises.
Indeed, in practice, the Hamiltonian usually decomposes into a potential energy associated to position and independent of momentum, and a kinetic energy associated to momentum and invariant under position changes, both generating tractable flows.
Thanks to this decomposition, we are able to construct numerical methods through splitting the vector field.
A few ideas coming together here, recalling some of our generalized coordinate based approaches to non equilibrium steady states and Bayesian mechanics, and also decomposition of complex functions.

51:40 Note also that for symplectic brackets, the evidence of a shadow Hamiltonian can be guaranteed beyond the case of splitting methods, eg.
For variational integrators, which use a discrete version of Hamiltonians Hamilton's principle of Least action and for most symplectic integrators in which the symplectic bracket is preserved up to topological considerations described by the first Dean cohomology of FaceBase.
So for discussion with authors annual what are the splitting integrators?
What is split from what and why?
What is the bracket notation or operation?

52:17 And what is a piss on bracket?
What is a piss on system?
Section 23 rate matching integrators for smooth Optimization so, having obtained a vast family of smooth dynamics and integrators that closely preserve F, we can now apply these ideas to optimization.
What is being set up in this section and why?
In equation seven we see that the damping coefficient gamma of t being greater than zero reflects the dissipative component, or the second term in that right hand side of equation seven.

52:57 So damping coefficient controls the strength of the dissipation.
One can imagine that if the damping coefficient is zero, the dissipative side zeros out and b has conservative behavior and so on.
So what is being set up here and why?
Dot dot dot dot dot the existence of such a Leopold function described above implies that trajectories starting in the neighborhood of Q star will converge to Q star.
So it's like a ball rolling to the bottom of a hill, just like we've always wanted.

53:34 In other words, the above system provably solves the optimization problem minimum of V on Q, such that Q is in the D dimension.
Real punchline.
We're setting up a system with good smooth optimization characteristics ball rolling to the bottom of a smooth hill that is also on the path or using the notation of or prepared to make the transformation to attractable discretization approach.
So some more on the damping coefficient.
They bring up some common choices for the damping coefficient.

54:16 And Big O notation describes on the order of which something occurs.
For example, linearly order of the variable or sub or super linearly as a function of time or data points.
So in computational complexity analysis, people are often interested as I double the amount of data I'm analyzing, does that make the algorithm take twice as long?
That's linear computational complexity?
Does it take four times as long?

54:46 Does it take the same amount of time?
And so on.
And it'll be great to talk about the intuitions and implications and generalizations about how the damping coefficient influences the computational complexity estimates for convergence in different settings.

55:11 They write the conservative system from equation 16 reduces precisely the original dissipative system 13.
The second equation in 16 reproduces 14, and the remaining equations are equivalent to the equations of motion associated to 13, which in turn are equivalent to eight.
As previously noted.
Formally, what we have done is to embed the original dissipative system with phase space r 2D, so real with 2D dimension into a higher dimension conservative system with phase space r 2D plus two.
The dissipative dynamics thus lies on a hyper surface of constant energy k equals zero in high dimension.

55:53 The reason for doing this procedure, called implication, is purely theoretical.
Oh, come on.
It's not purely theoretical.
Since the theory of symplectic integrators only accounts for conservative systems, we can now extend this theory to dissipative systems settings by applying a symplectic integrator to 13 and then fixing the relevant coordinates 17 in the resulting methods.
Geometrically, this corresponds to integrating the time flow exactly.

56:21 We're going to talk about a relationship between time and dissipative systems.
After all, it's dissipative systems that are dissipating in time.
And so discreditization of time plays a role in the appropriate inclination of a dissipative Hamiltonian.
And in citation nine previously raised, such a procedure was defined under the name of presymplectic integrators.
And these connections hold not only for the specific example above, but also for general non conservative Hamiltonian systems.

56:53 So what is happening here?
What's and intuition for conservative and dissipative systems?
And how have the recent works of Franca at all expanded what is possible?
We are now ready to explain why this approach is suitable to construct practical optimization methods.
The coordinate t sub k becomes simply the time discreditization, which is exact, and so is U sub k, since it is a function of time alone.

57:21 Importantly, U does not couple to any of the other degrees of freedom.
So it is irrelevant whether we have access to U or not, because we're looking to solve a function of t 17.
A can be substituted in 15 to get 18, and you can replace 13 to get 19.
We'll talk more about it with the authors.

57:49 Therefore, the known rates.
Equation eleven for the Continuum system are nearly preserved, and so would be any rates of more general time dependent dissipative Hamiltonian systems.
Let us now present and explicit algorithm to solve the optimization problem.
This is all happening as a consequence of having a shadow Hamiltonian such that geometric integrators are able to reproduce all the relevant properties of the Continuum system.
Section Two Four manifold and Constrained Optimization following ten, we briefly mentioned how the previous approach can be extended in great generality to an optimization problem.

58:32 So equation 21 we present our minimization problem V of Q variational distribution on Q.
Citation ten Franca et al.
They write There are essentially two ways to solve this problem through a dissipative Hamiltonian approach.
One is to simulate a Hamiltonian dynamics on T star M by incorporating the metric of M in the kinetic moving part of the Hamiltonian.
Another is to consider a Hamiltonian dynamics on RN and embed M into RN by imposing several constraints.

59:09 The first approach uses a Lee group.
We'll talk more about it.
An example of a second approach one can constrain the integrator on RN to define a symplectic integrator on M via the discrete constrained variational approach by using some techniques.

59:31 The above method consists in a dissipative generalization of the well known rattle integrator from molecular dynamics.
Citations 100 through 103 used in computational biology.
Section Two Five gradient Flow as a High Friction Limit let us provide some intuition why simulating second order systems is expected to field faster algorithms.
As an illustration, consider figure one.
On the left, we'll look at in a second where a particle immersed in a fluid falls under the influence of a potential force.

1:00:06 Negative delta sub q on V in Q.
So partial differential with respect to Q of V on Q that plays a role of gravity and is constrained to move on a surface.
So ball rolling down the hill.
We weren't joking about it.
In the underdamp case, the particle is underwater, which is not so viscous, so it has acceleration and moves fast.

1:00:33 It may even oscillate.
In the over damped case, the particle is in a highly viscous fluid such as honey, and the drag force that damping coefficient gamma is comparable or stronger to the gradient.
Thus the particle moves slowly since it cannot accelerate during the same elapsed time.
Delta T, an accelerated particle would travel a longer disturbance.
Here's figure one.

1:01:01 So here y simulating second order systems yields accelerated methods.
So on the left, constrained particle falling in fluids of differential viscosity.
Here on the left, we have the particle falling through honey.
It's slowly making its way to the bottom of the bowl, but it never really builds speed.
Its terminal velocity is being dominated by the viscosity of the fluid, whereas this bowl falling through water or falling through air is with respect to the honey dampened bowl.

1:01:38 This is like an accelerated optimization, and they present some numerical results that help us bolster that intuition.
Really fun and embodied way to think about optimization.
We've talked about that ball rolling to the bottom of the hill and what the ball does when it hits a small bump.
But we have not talked about what media the Bull is floating through and the media is the message and the fish doesn't know what it's swimming through.
Section 2.6 optimization in the space of probability measures.

1:02:16 It'll be great to explore more because we're going to see free energy calculations on the stationary density, KL divergence and more.
For now, we can just say all those optimization techniques we were bringing up earlier, we're going to be able to do them on information geometric spaces that correspond to probability measures that are well behaved.
Not all distinctions are probability measures or probability distributions.
Just because you draw a line doesn't mean you can use that in part of your variational inference scheme.
For Bayesian statistics.

1:02:52 That's section two.
On to section three Hamiltonian based accelerated sampling.
So we talked about the Hamiltonian conservative and dissipative and the shadow Hamiltonian, which is going to be orders of magnitude better to approximate.
We talked about gradientbased methods and how accelerated sampling is going to help us accelerate those sampling techniques.
And now section three brings it together with Hamiltonian based accelerated sampling.

1:03:20 Section Three the purpose of sampling methods is to efficiently draw samples from a target distribution row, or more commonly, to calculate expectations with respect to row.
And from the end of the paragraph.
An efficient sampling scheme is one that minimizes the variance of the Monte Carlo Markov chain.
Estimator Monte Carlo, that means that we're sampling hands from the poker table and Markov chain, which means that the past only influences the future through the present.
It's a quote memoryless process.

1:03:56 In other words, fewer samples will be needed to obtain a good estimate.
Intuitively good samplers are Markov chains that converge as fast as possible to the target distribution.
It's like if you laid down a jump rope on a mountain.
If that jump rope converged quickly to the topography of the mountain, it would have been a fast converging jump rope.
And we're doing something like that, but with sampling from the jump rope.

1:04:25 3.1.
Optimizing diffusion processes for sampling as many MCMC methods are based on discretizing continuous time stochastic processes.
The analysis of continuous time processes is informative of the properties of efficient samplers and diffusion processes possess a rich geometric theory extending that of vector Fields and have been widely studied in the context of sampling.
Lot of very fascinating ideas here.
Stratinovich stochastic differential equations are going to come into play.

1:05:06 Equation 34 more technical details on diffusion.
The calculus of twisted differentiate forms allows us to have a measure informed calculus on multivector Fields.
What are twisted differential forms?
I'm looking forward to that conversation.
What is the untwisted differential form?

1:05:30 Have we been twisted all along or not?
And they go on to write a fundamental criterion for efficient sampling is non reversibility.
A process is non reversible if it is statistically distinguishable from its time reversal when initialized at the target distribution.
So once the jump rope is lying flat on the mountain, it's like in a position of reversibility.
Mixing metaphors at will.

1:06:01 Here measure preserving diffusions are non reversible precisely when some cognition are met intuitively non reversible processes backtrack less often and thus furnish more diverse samples.
So if you're that ball rolling on the mountain, you want to just plow forward and whether you're going up or downhill, you want to be sampling and making moves, but you don't want to be going back and forth because at that point it's not and efficient sampling path.
It's well known that removing nonreversibility worsens the spectral gap and the asymptotic variants of the MCMC estimator.
So time discreditization spectral gap in dimension with linear coefficients, one can construct the optimal non reversible matrix a to optimize the spectral gap.
We can have well behaved parameters that help us get at optimal discretization schemes so that that shadow Hamiltonian can be preserved when we do discretize it during optimization, so that we can respect the key properties of the system.

1:07:13 However, there are no generic guidelines on how to optimize nonreversibility in arbitrary diffusions.
This suggests a two step strategy to construct efficient samplers one, optimize reversible distinctions dimension and two and a non reversible perturbation equation 36 citation 125 diffusions are manifolds.
Diffusion on manifolds are reversible when certain things are the case, and they're not when other things are the case.
Equation 37 we got a triangle pointing down and a triangle pointing up.
We're going to talk more about it.

1:07:56 Under damped Langevin dynamics combine all the desirable properties of an efficient sampler.
It is reversible, has degenerate noise, and achieves accelerated coherence to the target density.
So all of this groundwork is helping us get to an analytical formalization that's going to have the right kind of properties so we can do that discretion right on the shadow Hamiltonian, so we can agent the accelerated optimization done.
3.2 hamiltonian Monte Carlo a challenging task consists of constructing efficient sampling algorithms with strong theoretical guarantees.
We now discuss an important family of wellstudied methods known as Hamiltonian Monte Carlo HMC, which can be implemented on any manifold for any smooth, fully supported target measure that is known up to a normalizing constant.

1:08:52 Some of these methods can be seen as an appropriate geometric integration of the underdamped Langevin diffusion diffusing down that hill.
But in simpler, it is in general simpler to view them as combining a geometrically integrated deterministic dynamics with a simple stochastic process that ensures ergodicity.
Equation 38 if we interpret the negative log density v of q as a potential energy a function depending on position q, one can then plug in the potential within Newton's equation to obtain a deterministic proposal that is well defined on any manifold.
As soon as the acceleration and derivative operators have been replaced by their curved analogues.
So what pulls the ball down the hill?

1:09:45 Or, if you're an instrumentalist, what force describes the movement of the ball moving down the hill?
Gravity, I think there's a John Mayer song about it surprises like gravity.
It can be understood as the minimizing force that pulls the ball down the hill or describes the movement of the ball on its path of least action down the hill.
How cool.
More discussion around 38 bringing these ingredients together, we thus have the following HMC algorithm given dot dot dot.

1:10:29 We're going to compute a function according to one, a heat bath, two shadow Hamiltonian dynamics and three metropolis correction.
That's the recipe.
We're bringing those ingredients together.
The above Rudimentary HMC method was proposed for simulations in lattice quantum chromodynamics, with M being the special unitary group Su N, and used a Hamiltonian dynamics ingeniously constructed from the Mauer carton frame to compute the partition function of discretized gauge theories.
This method has later been applied in molecular dynamics and statistics.

1:11:14 There are three critical properties underpinning the success of HMC in practice.
The first two are the preservation of the reference measure and the existence of a conserved shadow Hamiltonian for the numerical method.
The third critical property is the existence of splittings methods, for which all the composing flows are either tractable or have adequate approximations, namely the geodesic integrators.
So geodesic methods buckminster, fuller, tensegrity, cybernetics, or however you think about geodesics as paths and curved space.
That is the kind of approximation and splitting we're gaining access to, with appropriate distinctions on those balls rolling to the bottom of the hill.

1:12:04 Let us also briefly mention some useful upgrades that have been proposed in recent years.
So for those who it's been a few years since you checked in with this domain, this is a great place to look.
First, you can grant the method extra integration steps when the proposal is rejected, or you can use criterion that aim to ensure the motion is long enough to avoid random walks, but short enough that we do not waste computational effort, such as the no uturn examples, which is integrated in a lot of software packages.
Second, Modern HMC methods bypass this issue of slow convergence by replacing the heat bath with an ornstein olbeck process, which ensures the overall algorithm is irreversible.
An ou process is like a Brownian diffusion with a linear regression, so it vibrates and has volatility, and it has a trend line that's linear.

1:13:06 Third, many modifications of the Rudimentary HMC algorithm only provide improvements when the acceptance rate is sufficiently high.
A third class of upgrades improve the acceptance rate by using the fact that the shadow Hamiltonian is exactly preserved by the integrator big point of the whole paper.
Finally, the metropolis step can be replaced with a multinomial correction that uses the entire numerical trajectory, accepting a given point along it according to the degree by which it distorts the target measure.
Some path based inference methods with some caveats all right, on to section four statistical inference with kernel based discrepancies.
So, section four the problem of parameter inference consists of estimating an element theta star within big theta using a sequence of random functions or estimators theta hat n of omega onto big theta equations conveniently reproducing Colonel Hilbert spaces.

1:14:12 RKHS are precisely Hilbert's spaces over which the Diroc distinctions, which is a statistical distinctions type where it's like a spike at one location and zero elsewhere, act continuously.
So whether we're talking about events or spiking neurons, this is a really good property.
And more generally, the probability distributions that act continuously by integration on an RKHS h are exactly those for which all elements of h are integral.
So analytically we have that nice property denoting by fancy piece of h, the set of such probability measures such that dot, dot, dot, we can define the maximum mean discrepancy, or Mmd, as such more definitions, a practical expression for the squared Mmd.
So just like in linear regression, we're often interested in the sum of squared errors.

1:15:15 Here we're interested in the sum of squared Mmd.
4.1.
Topological methods for Mmds just remember Mmds maximum mean discrepancy.

1:15:31 A key feature of RKHS is that there are Hilbertian subspaces, more details about embedding in Hilbert spaces and subspaces.
The geometric Analysis the geometric description of RKHS and Mmd allows us to swiftly apply topological methods in their analysis.
There are reasons this reduces the matter to a topological question.

1:15:59 Instead of defining T star to be the set of probability measures it is commonly done to define statistical manifolds.
It's desirable to embed franca p within a more structured space, such as the space of finite radon measures, which enables the method to learn the target function independently of the data generating distribution.
What is a radon measure?
We're going to find out.
However, it enables the method to learn the target function independently of the data generative distinctions sounds pretty important if we want that tale of two densities Mmd can discriminate distinctions that makes it useful to do other things.

1:16:45 Let's find out more.
Section 4.2 smooth Measures and KSDS So more information on Mmds and about making them computationally.
Tractable and citations to Stein's Method are provided for 195, which is the 1972 Stein paper, and 196, which is a paper written by some of the authors about Stein's Method meets statistics.
A review of some recent developments from 2021, and I thought it'd be fun to look at some figures from this paper and look at the abstract, so I'll put the figures up above.

1:17:31 Stein's method compares probability distributions through the study of a class of linear operators called Stein operators.
While mainly studied in probability and used to underpin theoretical statistics, stein's method has led to significant advances in computational statistics.
The topics that are discussed in that review include tools to benchmark and compare.
Sampling methods such as approximate Markov chain, Monte Carlo deterministic, alternatives to sampling methods, control variant techniques, parameter estimations, and goodness of fit testing.
And from the paper they write the list of results given in this paper are but a mere sample of the ongoing activity in this newly established area of research at the boundary between probability, functional analysis, data science, and computational statistics.

1:18:23 For instance, Stein's method has been used for designing sampling based algorithms for nonconvex optimization learning semiparametric multi index models and high dimensions and Bayesian statistics physics.
Stein discrepancies have been used as variational objectives for posterior optimization, which is what we're all about free energy functionals, using variational inference as objectives for posterior approximation of inference and action free energy principle.
And these images have some nice intuitions too.
Here we see, depending on our step size, we're getting different sampling.
When our step size is to the negative fifth power, we're over sampling one part of the space.

1:19:13 Then, as we make the step size larger, our samples are drawn from different distributions.
So that's selecting the step size epsilon for a stochastic gradient Langvin dynamic and also from the anastasio paper.
Here's another fun way to see that.
Here we have that bowl that we're rolling the ball to the bottom of, and the Stein points and the Stein thinning, which is helping us understand maybe how starting the ball in different locations or critical locations accelerates what we're doing with optimization.
So cool to talk about.

1:19:52 4.2.1 the canonical Stein operator and Poincare duality there are two fundamental theorems that help us understand the integral differentiate geometry of the manifold durham's theorem and the Poncare duality.
The former Durham's theorem relates the topology of the manifold to information on the solutions of differential equations defined over the manifold.
The latter, which contains the fundamental theorem of calculus, describes the properties of the integral pairing alpha beta of differential forms, which include the pairing of test functions with smooth measures.
Let's learn more about it.
Four, two, two kernel stein discrepancies and score matchings technical definitions facilitating Stein variational gradient descent.

1:20:47 4.3 information geometry of Mmds and natural gradient descent.
These tools have proved to be useful in a wide range of contexts.
More information about the divergence and how divergence can improve the speed of coherence by following the natural gradient descent.
Okay, red text speculation beware.
So the operator, which is a phone routing system like ring ring, hello, operator is constructed in action.

1:21:25 4.2.22 colonel Stein discrepancies and score matching you can't have a Ttest without the T distribution.
The Ttest statistic is using a T distribution.
So a class of fancy V, a set fancy V of vector Fields, or more generally, tensorfields whose image f under the operator ring ring has mean zero under Mu that's going to give us this discrepancy, the SD and the Stein variational gradient descent.
So there's some class of V vector Fields such that the mean of something about them is zero.
Does this enable the central limit theorem or just statistics more broadly, like the parametric and non parametric methods that we know and love from SPM?

1:22:27 Does that mean zero enable us to use Gaussian methods, generalized Gaussian methods, generalized linear methods, SPM?
And does it enable the proposed smooth distribution, the one generating the shadow Hamiltonian that's getting inferred over, to be interpreted or used truly as a statistical distribution?
It's easy to forget that not all distributions are formal probability distributions.
For example, the area under the curve from zero to one of a probability distribution is one.
Something has to happen.

1:23:08 But not all functions have an area under the curve of one between zero and one.
So in variational Bayesian inference, the kind which we do in active inference, in fact, the kind that's done in machine learning and statistics more broadly.
But we're interested when action is a parameter that we're doing inference on.
We're concerned with the extremely well behavior properties of a certain subset of distributions.
So why are we doing this?

1:23:40 Why is it important that we didn't need the input data that we could construct measures that are independent of the input data?
Because we want to enable the tail of two density.
We want to make generative models that can be used generatively, generative AI in the forward or the generative direction.
But we also want to be able to enable the recognition distribution, which is from empirical data, to do hidden state inference.
And so just like least squares regression in the linear modeling case, where the sum of squares above and below the regression line should be as low as possible l two norm sum of squares minimization always works, never complains.

1:24:35 We want that kind of ball rolling to the bottom of the hill with free energy functionals variational and expected free energy functionals as the optimized or satisfied imperative for optimal perception, which is signal processing, signals intelligence and control which is control theory or action selection.

1:25:01 More technical details and equations 39 B and 39 C.
So what does it mean that the resulting Stein discrepancy can be thought of as an Mmd that depends only on row and is known as a kernel Stein discrepancy.
What is that?

1:25:19 As we did previously, we can remove the super mum by rewriting the above as a super mum over some unit ball of continuous linear functional.
Is this like simulating or modeling a sphere rolling on a landscape like we've been talking about?
Is the ball of optimal radius for rolling on that landscape?
Or what is being optimized?
And what is the unit, the scaling or the scale specificity that this scale friendly sphere is scaled to?

1:25:53 Equation 42 and 42 a while in the Euclidean space yields the diffusion score matching.
Citation 204 Barp et al again minimum Stein discrepancy estimators from 2019 they write the main strength of our methodology is its flexibility, which allows us to design estimators with desirable properties for specific models at hand by carefully selecting a Stein discrepancy.
We illustrate this advantage for several challenging problems for score matching, such as non smooth, heavy tailed or light tailed densities.
So again, just with a little bit of speculation here and I think my camera has frozen.

1:26:46 It's all good.
I'll just go without the camera.

1:26:54 Okay.
One can estimate infer or optimize the zero point and hence the variance structure of the distribution.
This is going to ensemble generalized wellbehaved modeling again, from all of those nice perspectives that we raised earlier, like Gaussian central Limit theorem, smoothness, statistical disturbance, Euclidean, all of those well behaved properties that we're looking for.
This is going to help us get there.
We are only talking about a specific subset or type of landscape here, the one that we're doing variational inference on, that's the map.

1:27:33 This is not the structure of the territory.
These well behaved attributes of models for better, worse and different through sickness and health is because they're maps.
It is always the case that our statistically nice generative models are of a different structure or form than the generative process.
So this is actually not a criticism of quantitative modeling as a process.
In fact, this is the entire basis of quantitative modeling.

1:28:03 So we've approached this map territory distinction.
Map territory fallacy, fallacy, fallacy from many angles and one will still hear things like well, the structure of the statistical model is not the same as the territory.
Or how can you say that the organism has these well behaved properties just because the model does?
And this brings a really sharp light on it, which is we're doing this insane amount of analytical groundwork so that the map has the good properties not to constrain what the territory is.
So map territory, all of the math we've been talking about is map.

1:28:47 We want wellbehaved maps so that we can describe wellbehaved and unruly territories.
But it isn't the case that the organism minimizes variational free energy.
It's the generative model that minimizes variational free energy.
So, little bit of a leading discussion topic or question for you all.
Feel free to give a thought in the live chat or write a comment or join our discussions.

1:29:15 How is this line of basic and fundamental math research by Barp et al.
Creating new models that have the operational or denotational semantics that we want for computational statistics, which is to say applied information theory.
For example, distributions that can be interpreted or used as statistical distributions, ideally directly compatible with current computational methods SPM in MATLAB, Pi, Mdp in Python and fourney Lab in Julia and so on.
Section 4.3.1 minimum Stein discrepancy estimators, more technical details, more inclination to 204.
The parameters can be adjusted to active characteristicness consistency, bias, robustness and obtain central Limit Theorems C 204.

1:30:07 2019 paper with Barp et al.
And let's just look at a really cool image from that paper.
Figure one and figure two pretty cool.
SD estimators looking nice.
Section 4.3.2 likelihood Free Inference with Generative Models so for many applications of interests, the densities of the model mu sub data cannot be evaluated or differentiated.

1:30:48 We thus need density free inference methods super convenient for Bayesian statistics, more technical details, information tensor.
Under appropriate choices of kernels and models, one can derive theoretical guarantees such as concentration and generalization boundary consistency asymptotic normality and robustness.
So, little bit of a summary we have good analytical and computational footing in certain kinds of situations or under certain constraints.
Certainly not all constraints, but definitely for some that might enable the efficient computation, not just specification, but actual implementation of large generative models such as described in the paper of Friston et al.
2022 designing Ecosystems of Intelligence from shared sorry.

1:31:42 Designing Ecosystems of Intelligence free Energy Principle And they use the term ecosystems of shared intelligence in that paper.
And so it's relevant to learn about the actuality and build intuition.
Why?
How do we know?
Well, here's the one figure in that paper of Friston at all, the one figure in this absolutely positional paper that they have released believes as parameters of a probability distribution.

1:32:13 Here's the sharpening of a belief as a distance belief updating as traversing a statistical manifold, which is to say a lower dimension projected space and what's being shown as the parameter space of a probability distribution.
So whether we see this as gradient ascent to climb to the top of the hill or we take the negative and we have gradient descent to the bottom of the hill, this is the figure chosen by some very well informed authors to describe Bayesian mechanics.

1:32:49 And long last we get to section five adaptive agents through active coherence.
We close, as the authors write, with a generic use case called Active Coherence, a general framework for describing and designing adaptive agents that unifies all aspects of behavior, including perception, planning and learning as processes of inference.
By exploiting this geometric structure in a generic framework for designing adaptive agents, we derive the objective functional overarching decision making and describe its information geometric structure, revealing several special cases that are established notions in statistics, cognitive science and engineering.
So section five one modeling.
Adaptive decision making.

1:33:35 First, they're going to talk about behavior, agents and environments.
Behavior is going to be defined as the interaction between an agent and its environment.
And the system is going to describe the agent plus its environment.
There's going to be a set of states that are partitions from a statespace big x external states.
S are going to be unknown to the agent and constitute the environment states belonging to the agent.

1:34:06 Pi particular states are going to be a subset of two different things.
So here is S, which is here external states.
Note that in some other settings S will refer to sensory states.
So look at the notation in this paper and Pi, which in other papers is sometimes used to describe policy inference here is going to describe particular states.
So Pi is O and A.

1:34:36 O are the observable states, states that the agent can see but cannot directly control sense states and A are the autonomous states that the agent sees and can directly control.
And those are going to be internal states and active states.
Figure two has a great representation and again note the way that Pi, So and A are being used in this paper.
S is the external process hidden state, latent state, causal coherence.
O are the observations and the agent process concepts of Pi, which is the observations and alpha or A.

1:35:25 A is consisting of, according to the particular partition, two different kinds of states, which is internal states, cognitive states and action states.
And so we're going to compute bounds for free energy functionals with a special focus on autonomous processes.
Because controlling our perception is not possible, and maybe not even preferable by controlling it at the level of what we observe.
But rather, if we control our internal states, which is our interpretation of the perception and our action states, we'll be doing optimal perception and optimal action.
So those are the two sides of the coin with inference as perception learning and action selection.

1:36:17 That's how we unify action and inference.
Inactive inference is by caring about the bounding of selfsurprisal, just like gravity on our autonomous processes.
So this will be super fun to discuss more.
5.1.2 decision making and precise agents so, what distinctions people from small particles people are subject to classical as opposed to statistical mechanics.
Check out Active Livestream 49 for more on Bayesian mechanics and some of these distinctions with classical statistical quantum and thermo.

1:36:54 In other words, they are precise agents with conservative dynamics.
Precise agent definition 5.1 an agent is precise when it evolves deterministically in a possibly stochastic environment.
More definitions and it's useful here to highlight Friston et al's.
Recent paper path integrals particular kinds and Lagrange things which provides a taxonomy of things taxonomy of particular entities that run the gamut of sophistication from inert particles which have no active states active particles which have active states generative process which have cognitive dynamics that are described as classical and strange particles which represent in this visualization the highest level of cognitive sophistication in which those internal hidden states themselves have this kind of what would happen if this happens counterfactual type or thinking through other minds type cognitive model structure doing forward and inverse inference on these great times.

1:38:11 5.1.2.

1:38:12 Decision making and precise agents we have mathematical formalisms for decisions, preferences and predictions all using the partitioned variables.
5.12 more formalisms we get to expected free energy.
Expected free energy is equation 41K.
Active inference is Hamilton's principle of leased action on expected free energy and expresses the most likely decision where certain features are met principle of least action on manifolds of inference and action subsuming or bringing together inference and action active inference, free energy principle 5.1.3.
Active Inference Framework AIF looks like it describes agents that engage in purposeful behavior.

1:39:12 We can rearrange the expected free energy EFE in several ways, each of which reveals a fundamental trade off that underwrites decision making.
This allows us to relate active inference to information theoretic formalizations of decision making that predominate in statistics, cognitive science, and engineering.
Figure three, as hinted ant in the early, early keywords.
Here on the top, we have the general formalizations of active inference.
And one of the partitions, or better to say competition, is shown here, where extrinsic value is the surprising about observations, making sure that what we're getting in observations are what we expect slash prefer if the body wants to be expecting homeostatic temperature.

1:40:04 That's what this is going to determine.
And it plays a role equivalent to reward in reward and reinforcement learning based approaches, because we don't need to actually set a reward function, but we get something that looks like selfsurprisal aligned with reward using the preference variable over observations.
A lot more to say there.
And the second term is the intrinsic value, the epistemic value, curiosity, novelty, learning, reduction of uncertainty.
And another partitioning is between risk and ambiguity.

1:40:43 There are four colored dots red, tan, gray, and Bleu corresponding to special cases.
So under the setting where there's no ambiguity, we realize or manifest the special case where control can be seen as inference, maximum entropy, reinforcement learning, prospect theory, and KL optimal control.
This is like doing as good as you can strategically or tactically, given that there's no ambiguity in how your decisions play out.
Now, under the setting where there's no ambiguity or preferences, a maximum entropy principle is realized.
And work with Bayesian mechanics.

1:41:29 And Dalton et al.
Has shown that the constrained maximum entropy principle is dual to the FEP in the case of no extrinsic value.
So no quote reward, no quote goals.
We don't use reward or goals in the active inference ontology, but borrowing those words from some long, long forgotten ontology, in the case of no extrinsic value, we realized the special case of maximum information gain, Bayesian experimental design.
So not to prove or disprove, but the maximally informative experiment that's the Bayesian scientific epistemology intrinsic implication and Bayesian surprise seeking out optimally informative stimuli.

1:42:19 And contrast that with a setting where there's no intrinsic value.
So where there's nothing to learn, we realize expected utility theory, Bayesian decision theory, reinforcement learning, and optimal control.
So special cases from many different Fields, ranging from statistical mechanics to Bayesian decision making and statistics integrated or perhaps better generalized across in the formalisms of active inference, which is something like a Hamilton's principle of least action on variational or expected free energy, expressing the most likely inference and action under certain constraints.
Not the most rewarding, but the most likely.
5.1.3.

1:43:15 Decision making minimizes both risk and ambiguity.
Risk, first term on the right hand side, ambiguity second, term minimizing ambiguity leads to a type of observational bias commonly known as the streetlight effect.
When a person loses their keys at night, they initially search for them under the streetlight.
Because of the resulting observations, I see my keys under the streetlight, or I do not see my keys under the streetlight accurately disambiguate external states of affairs.
First place to look make sense under the streetlight, and the last place you look is where you find it more in.

1:43:54 5.1.3.
Decision making maximizes extrinsic and intrinsic value another decomposition of the formalisms of active inference maximizing information gain leads to a goal directed form of exploration driven to answer what would happen if I did.
That true counterfactuals this decision making procedure underwrites Bayesian Experimental Design in Statistics, which describes optimal experiments as those that maximize expected information gain.
And we've had some great discussions recently in textbook groups and in discussion hours, where we contrasted that falsificationist concept of accept or reject hypothesis, and even the idea of a scientist or a researcher setting out to accept or reject hypothesis.
Whether you take that Positivist or you take the other path of falsificationism, in both cases, you might end up with an informative experiment or not.

1:44:56 But you can easily imagine cases where you end up with an uninformative experiment because you set out to confirm something you knew, or you set out to disprove something by constraining your experiment so that it was locally disproven.
In contrast, when we take into account the richness of our generative model, we motivate this Bayesian epistemology and ultimately professional Bayesianism, where we make optimal experiments in terms of their maximum expected information gain, which requires you to also state your generative model.
Decision making under active inference weighs the imperatives of maximizing utility and information gain, which suggests a principled solution to the exploration exploitation dilemma.
Great point to jump into.
Does active inference, simply by written down, by being written down on a paper, resolve or transcend or dissolve exploration exploitation?

1:45:55 No.
Does it provide a space or a framework, a method, an approach, software packages, a research community that can help us address and navigate and surf on the edge of that dilemma?
Absolutely.
5.2.1.
The basic active inference algorithm we're going to go through it with authors preferential inference.

1:46:20 We want to infer preferences about external and observable trajectories.
Two for each possible sequence of past, present and future actions.
A we're going to engage in both sides of the coin perceptual inference what would I perceive if that happened?
And planning as inference assess the action sequence by evaluating its expected free energy.
And then three, decision making execute the most likely decision at T plus one, according to some distinctions, sample from your action posterior, action prior that's, like your habits, it gets sharpened or modified with expected free energy, and then you sample from the action posterior.

1:47:07 5.2.1.
Sequential Decision Making under Uncertainty a partially observable Markov decision process POMDP is a discrete time model of how actions influence external states.
In a POMDP, each external state depends only on the current action and previous external state.
That's the Markov property.
Each observation depends only on the current external state, and one can additionally specify a distribution of preferences over external trajectories.

1:47:37 One and two form the agent's POMDP prediction model.
Two and three form the agent's hidden Markov preference model, which defines the active inference agent.
A simple simulation of active inference on a POMDP is provided in figure four.
Implementation details on generic POMDPs are available.
For more complex simulations of sequential decision making, e.

1:48:03 G involving hierarchical POMDPs, please see citations.
Figure four.
It's a prediction model.
This is sequential decision making in a Team A's environment.
On the left, the agent's prediction model as a POMDP, represented here as a Bayesian network.

1:48:24 On the right, information on the team A's.
So here we have some type of Bayesian graph reflecting hopefully a statistical system that's going to have all of these well behaved properties that we've been talking about in the paper.
And then the team AZ is played out.
We'll talk about it.
5.2.3.

1:48:50 World model learning is inference due to a lack of domain knowledge, it may be challenging to specify an agent's prediction and preference model.
For example, how do external states map to observations?
Should external states be represented in a discrete or continuous state space?
Also, some great questions that come up every day.
And Clark addressed in chapter six a recipe for active inference modeling by the Par Pazulo and Friston 2022 textbook.

1:49:18 So how do we get the right priors, or at least approximately adequate priors?
One way to answer the question lies in optimizing a free energy functional F, which is an evidence lower bound.
We see here variational free energy decomposed into an energy minus entropy and decomposed into a complexity minus accuracy.
Framing maximizing accuracy usually results in generative models involving universal function approximators minimizing complexity results action action oriented representation sparse compartmentalized in hierarchical generative models where higher levels of the hierarchical model more abstract representations, and vice versa.
A computationally efficient method to compare priors by their free energy is Bayesian model reduction, free energy, unifies inference, and model selection under a single objective function.

1:50:18 5.24.
Scaling active inference planning for all possible courses of action is computationally expensive.
One way to finesse this is by planning only for intelligently chosen subsets of action sequences using sampling algorithms like Monte Carlo Tree Search.
If you're interested in that, check out the recent research on branching time active inference.
Similarly, Monte Carlo sampling finesses the expectations inherent in assessing action sequences.

1:50:48 A complementary approach is to assess actions instead of action sequences by conditioning all future actions to be optimal in the sense that they minimize the expected free energy.
It leads to smarter agents whose computational complexity scales linearly as opposed to exponentially in the length of action sequence.
Let's learn more about it.
Scalable inference methods can be used to make active inference more efficient.
We can train neural networks to predict the various posterior distributions, including the posterior over action while training the output of the neural network can be used as an initial conditions for variational coherence, resulting active inference whose computational costs decrease as the network learns.

1:51:39 Additionally, optimizing free energy reduces to efficient message passing schemes when one imposes certain simplifying distinctions to the family of candidate distributions.
Lots of really exciting work in neurobiology and statistics around message passing getting close to the end here a much cheaper implication of active inference exists for continuous states evolving in continuous time.
Pretty cool.
Par et al.
2022 Textbook Chapter Seven Discrete time Active Inference generative Models Chapter Eight Continuous time Active Inference Models this method frames perception and decision making as variational inference by simulating a gradient flow on free energy in an extended state space.

1:52:28 It can be combined with discrete active inference to operate efficiently in generative models combining discrete and continuous states.
We talked about that in live stream 46 Active inference does not contradict folk psychology, discrete active inference decision making, active inference dai, and continuous time motor active inference being used together, also seen in the paradigm textbook.
As an example, high dimensional observations in the continuous domain, e.g. speech processed through continuous active inference are converted into discrete abstract representations, e.g. semantics, and we can even go further and say rhetorical and narrative information spaces based on these representations, the agent makes high level categorical decisions, e.g.

1:53:19 I want to move over there, which contextualize low level continuous actions, eg. the continuous motion of a limb towards the goal location and that is how the paper ends.
So, closing thoughts if anybody wants to write a comment live, feel free to do so.
We'll be over very shortly.
What are the implications of this work?

1:53:46 We have an open space to talk about it.

1:53:53 What questions and discussion topics are you interested in?
Please write comments before or after the dot one and the dot two so we can have those interesting discussions.
And just as a little bit of a closer, I'll share some stable diffusion images that were generated using the paper title as well as various other terms free energy, lots of fun images, a lot of good balance to some of the technical aspects that were being described in the paper.
Was good to look at what diffusion looks like aesthetically and so that is the end of this Livestream.
52.0 I hope that you found it useful that you're interested to act in first, serve to learn more, contribute more, write a comment, make it happen in your own life or in your own way with this honestly challenging paper.

1:55:05 So if you've listened this far, thanks a lot for your attention and looking forward to 520 One and Zero Two when we will speak with some authors and some of you.
So till next time, thanks again and see you in the dot.
One.
Bye.
