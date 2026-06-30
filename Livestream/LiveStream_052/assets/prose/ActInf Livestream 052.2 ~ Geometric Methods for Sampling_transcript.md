00:07 _Daniel:_

Hello and welcome.
It's ActInf Lab Livestream 52.2 on March 9, 2023.
Welcome to the Active Inference Institute.
We're a participatory online institute that is communicating, learning, and practicing applied active inference.

00:25 You can find more information on these links.
This is a recorded and archive live stream, so please provide feedback so we can improve our work.
All backgrounds and perspectives are welcome, and we'll be following video etiquette for Livestreams head over Active Inference.org to learn more about getting involved with projects and learning groups.
All right!
We are back in Livestream 52.2, in our third discussion on the paper geometric methods for sampling, optimization, inference and adaptive agents.

01:04 We had a Dot-Zero background and context video and last week Lance joined for 52.1, where we had a great overview discussion on the paper.
So today we're going to see where it goes, see where our last week has taken us and how we're thinking about it or curious about it.
If you're watching live, of course, feel free to write questions in a live chat.
Otherwise, let us pick up on a mostly blank slide.
And just thanks again, Lance, for joining.

01:43 If you want to give any sort of introduction or recap opening here, go for it.

01:52 _Lance:_

Well, yeah, I mean, thanks a lot, Daniel, for organizing this.
I'm super happy to be here, I think.
Well, last time we went through most of the paper, we discussed a lot about sampling.
I guess the idea of sampling.

02:07 We discussed a bit less about Hamiltonia Monte Carlo, which is one of the, I guess, state of the art methods for sampling in continuous space.
We discussed a lot about optimization.
There's a nice figure actually that we can discuss today which gives some nice intuition about the kind of optimization methods that we reviewed in the paper.
And then there's another section on statistical inference.
So this is a bit of a different section than people in the free energy principle literature and active inference are used to.

02:45 Because here the goal of inference is about approximating expectations as opposed to just approximating distributions in of themselves.
It turns out to be these two perspectives turn out to be dual.
But I guess here we want to develop notions of divergences and discrepancies that are a bit more general than the KL divergence and that can use to solve problems that the KL divergence cannot.
And I guess the overall picture for why we want to do that is the Kale divergence turns out to have a lot of really nice properties that we can discuss.
One of them is that if the Kale divergence is reduced, it means that the two distributions in play are more similar in terms of information.

03:38 So there is this idea of information monotonicity where the KL divergence sort of gives an ordering as to what extent two distributions quantify.
So if you had three distributions and you compute the KL divergence between them and now KL of AB is lower than KL of AC.
It means that B is more closer in terms of information to A than C is to A.
So you have this really nice thing that is captured by the Kel divergence, which makes sense when we're dealing with information.
The Kel divergence also has so many other nice properties.

04:21 It's not a distance, but it turns out to behave a bit like a square distance.
So you have this kind of like, really nice pitagorian theorem.
And I won't get into the exact statement, but it's like if you have a B and C distributions, then KLAB plus klac equals KLBC.
If you have like a rectangle triangle, if ABC defines a rectangle triangle in information space, you have other properties like the KL divergence gives and so on.
So the KL divergence is in general, I would say, the distribution, the divergence of choice.

05:01 But it turns out that in many cases you just can't use it.
For example, when you have samples and you want to approximate some samples with a distribution, then the Kale divergence just is not going to work there.
So you need to derive some other things.
So this is to say that we're considering statistical inference a bit more generally than what we do in active inference in general.
And so this speaks to why the section here is a bit different from the standard inference literature that we usually consider.

05:35 And then I think that the well, then this section five, which is about active inference, and I think we should discuss that a little bit more because the formation active inference lab that's presented there is to my mind the most general and also the simplest conceptually that's been out there.
I mean, we sort of recap the derivation active inference lab and also like the properties of the expected community properties of active inference and also how to scale active inference and so on.
And we do that in just seven pages or five pages.
I mean, it's just very short.
So it stands, sure, but it's like a really concise summary.

06:16 And actually from there you can really derive a lot of technical papers.
Active inference lab, to me, it's the most general, and if you as a reader can understand that section, then you can sort of really understand what active inference is about.
This is kind of the overview for today.
I would really like to be discussing questions because last time we read discussed about most of the papers.
But yeah, whatever comes up.

06:51 _Daniel:_

Awesome.
All right, great.
Well, let us talk about some of the more foundational pieces hamiltonian Monte Carlo and then on through section four with the points that you raised about the KL, which generalized inference beyond how it may have been brought up in other octave.
And then we can spend most of the time in section five and looking at some of those figures connecting some of the intuitions about the ball rolling down the bowl to the person running.
So.

07:32 _Lance:_

Sounds good on Hamiltonian?

07:35 _Daniel:_

Monte Carlo.
Where do you want to pick up?

07:38 _Lance:_

Sure.
I meantonian so last time we discussed a lot about the problem of sampling and why that's the difficult problem.

07:47 And we arrived at the conclusion, or I presented like Monte Carlo methods, how they work.
So you're basically running a stochastic process, like a random motion and sort of the distribution defining the process is going to convert your target distribution, which means that when you run the process long enough, then every point that it's going to be in is going to be like a sample of the distribution that you want to sample from.
Now, there's a lot of issues with that.
Conceptually, it's not so difficult, but actually, when you want to implement this in practice, it turns out to be really hard because if you just implement the simplest stochastic process to sample your target distribution, it's going to be extremely slow.
And I think that's the main bottleneck when developing Monte Carlo methods.

08:41 Monte Carlo sampling in general is slow.
And that's also one of the reasons why one might want to do variational inference instead of sampling.
So something is slower, but it's also more accurate.
It can approximate distributions that are completely arbitrary.
So if you care about accuracy and you have time and computational resources, then for sure go for sampling.

09:08 If you care about speed, about doing things online, and you don't care about accuracy so much, then the variational inference is the way to go.
At least that's my understanding right now.
So let's say you wanted to sample a distribution in a continuous space.
So it could be just as last time.
Let's imagine the state space is the desk where I'm at, and you sort of have the distribution, which could be like multimodal, very weird, and you just want to take samples from there.

09:39 HamiltonI Monte Carlo is probably the state of the art methods method to do that.
There's a lot of other methods out there, but Hamilton Monte Carlo typically just works very well and in a wide variety of situations.
Instead, the idea of HamiltonI Monte Carlo is you're going to augment the state space with so let's say that the original state space you start with are the positions.
And so you're going to a mend that with a velocity state space.
If your original state space was Euclidean space of N dimensions, you just end up with a nuclear space of two N dimensions.

10:22 So you double the size of the state space.
And now you say, okay, well, the distribution that I want to stumble from actually defines an energy landscape.
So technically it's like if you have distribution which is P, then minus lock, p is an energy landscape.
So points where minus lock P is low are points where P is high.
And so these are points that you want to sample a lot from.

10:55 And contrary wise, if minus Lock t is very high, then P is low.
And you don't really want to go there so much because these are points of low probability.
So I think this minus log P, actually there's many reasons why minus Lock P is meaningful in physics.
But just note for now that minus Lock P is just like a function and the minimum of the functions of that function are the high probability points and these are high energy points where you basically don't want to go there so much.
So let's call this minus Lock P potential energy.

11:40 And so this is what this really is in physics.
Technically in physics, P would be a gives measure, what people call an equilibrium distribution.
Last time we saw like soft max, minus something.
The something is the potential energy anyway.
And so minus Lock P would be the potential energy.

12:08 And then if you add kinetic energy on your velocities, then you get what's called a Hamiltonium, which is the sum of the potential and kinetic energies.
So what is exactly kinetic energy?
The kinetic energy is like velocity squared pretty much.
So if you add remember that your state space is position and velocity.
If you add and you take a point in state space, so you would have kinetic energy, which is velocity squared, and a potential energy which would be minus lock peak.

12:46 Now, if you add the two together, what you get is a Hamiltonian, which is the sum of the kinetic energy and potential energy.
And this is just standard physics.
Hamiltonian is the sum of kinetic and potential energy and it gives us the total energy of the system.
So why we start with the problem of sampling.
And here I just told you something very complicated where we get a Hamiltonian, there's actually a good reason why I want to do that.

13:14 And it comes back to the idea of geometric integration that we talked about last time, which is that typically maybe I have a process that I know will give very efficient sampling, but actually when I implement it on the computer in discrete time, I just lose all the properties that make that sampling efficient.
So actually it turns out that most people working in Monte Carlo sampling, they're working on efficient discretizations of continuous processes as opposed to on the continuous process themselves.
Really the bottleneck.
And the difficulty here is the implementation part, implementing process on a computer like you and I had in such a way that we retain all the good sampling properties.
So one very powerful idea is that of geometric integration, which is of preserving geometric properties of a system.

14:14 Geometric integration is the field that develops computational methods of numerical integration and numerical discretion in such a way that they preserve important geometric properties of the system.
Here, the geometry in play is a Hamiltonian.
And so you might think, well, that's pretty weird.
I mean, a Hamiltonian is an energy here we're talking about preserving the geometry and preserving the Hamiltonian.
How do these two things fit together?

14:46 And so it turns out that the presence of a Hamiltonian and the fact that we have a state space that has positions and velocity, technically, in mathematics, what we then get is what people call symptom geometry.
So symptom geometry just arises when we have those states that comprise positions and velocity and where you have Hamiltonians.
So this is just like a way of explaining why the Hamiltonian is closely and intimately related to geometry.
So geometry integration enables you to discrete processes in such a way that the Hamiltonian is preserved.
Now, when you think about the Hamiltonian, the Hamiltonian gives you the energy of a particular point in space.

15:45 And so if you simulate trajectories that preserve the Hamiltonian, what you're effectively doing is sampling from the contours of the probability distribution, contours that have the same probability.
So basically going around, let's say, for example, in circles in a region that has the same probability, when we want to sample, we want to go everywhere.
I mean, we want to sample regions of high probability, low probability, and want to be able to go from one to the other.
So what geometric integration allows us to do is to simulate dynamics that are going to preserve the contours of the probability distribution, and they're going to do so very well.
The advantage here is that when we use geometric integration to simulate Hamiltonian dynamics, which are conservative and again, staying the contours, what geometric integration allows us to do is to take time steps that are very long.

16:54 So it enables us to travel very far in the landscape while still preserving the Hamiltonian.
So you don't need to take very small time steps to remain accurate and preserve the Hamiltonian.
But actually, dramatic integration allows you to take very long time steps and still preserve the Hamiltonian.
So now we have a dynamic that's Hamiltonian preserving that's just very good because you can take very long time steps, and that enables you to go around the contours of the probability distribution.
So what you want to do next is to change contours.

17:30 You want to go to contours that are of high probability, contours of lower probability.
And you want to do so in a way that the contours of high probability are sampled much more and much more often than the contours of lower probability.
So what you do is that you augment your Hamiltonian dynamic with what people call a velocity refreshment or a momentum refreshment.
And so this is how it works.
So you're going to simulate your Hamiltonian dynamics for some time, and then after a while, you're going to be like, okay, well, now I'm going to change the velocity at random by just drawing a new velocity from a Gaussian distribution.

18:24 And so by drawing a new velocity from a Gaussian distribution, you're just going to change contour completely.
And then there's what's called the constraint that I just talked about, which is you want to change contours of the probability distribution in such a way that contours of high probability are visited much more often than contours of low probability.
So you want to preserve that.
You want to do that in a way.
So the third ingredient of Hamiltonian Monte Carlo comes in, which is metropolis.

19:02 Hastings.
And so Metropolis Hastings is this accept reject that we discussed briefly last time.
And so Metropolis Hastings is just super clever and it enables you to say it just tells you whether this momentum refreshing step is actually a good one or a bad one and should be rejected.
A momentum refreshment is good if overall your sampling is going to remain faithful to the target distribution, but it is bad if it remains unfaithful.
So actually running this metropolitate things except rejects, that allows you to change contours of the property distribution in a way that remains faithful to the target distribution.

19:58 And so there you go.
That's basically Hamiltonian Monte Carlo.
So to recap, you a mental state space by adding velocities.
This allows you to build the Hamiltonian by declaring that the original probability distribution gives you potential energy and you add a kinetic energy on the velocities, which is just velocity squared.
Because you have a Hamiltonian, you can use geometric integration to simulate Hamiltonian dynamics very accurately and with very long time steps.

20:35 The very long time steps is a crucial thing because it means that with very low computational costs, you can sample very far.
So it means that you don't get stuck in a region of the probability distribution, but you can actually visit it much more fast and efficiently.
So that's the first part.
The problem with those dynamics again, is that they remain on the contour of the probability distribution.
And so you want to sample the whole probability distribution.

21:03 So what you do is every once in a while, and I think that's a hyper parameter in your, in your sampling algorithm, let's say every ten iterations of the Hamiltonian dynamic, every ten time steps of the Hamiltonian dynamic, you're going to sample you're, you're just going to randomly take a new velocity.
So you're going to change contour in the probability distribution.
And the crucial point there is you want to change contour in a way that's faithful of the probability distribution and that's faithful of the sampling problem that you want to do.
There comes the last thing, which is Metropolis Hastings, which ensures that the momentum reflect freshman will be good for sampling, I mean, will preserve your target probability distribution.
So with that, you just get a very efficient sampling algorithm.

22:02 And so it seems a bit convoluted, right?
And one bottleneck, of course, is that you need to double the dimension of the state space.
And if your state space is already extremely large, that could be a bottleneck.
It could be the case that actually doubling the dimension to add velocities, it could be a computational bottleneck.
So that's a problem, but still, in most cases, that's not a problem.

22:32 Again, Hamilton in Monte Carlo is convoluted.
But the overall take home message I would want you to take from this is that it is a method that remains faithful to the probability distribution they want to sample.
And this is crucial.
And it is also a method that through geometric integration, it enables you to take time steps that are very long and still get accurate sampling.
So this is the really cool thing.

23:04 If you could come up with a whole bunch of other methods that did not require to double the dimension of the state space or that didn't use geometric integration, the problem that you would probably run into is that the thing that you came up with when you implemented in the computer, it doesn't exactly preserve the probability distribution that you want to sample.
And so the problem with that is that this would lead to biased sampling.
And biased sampling is like you're going to sample a different probability distribution, which might be just a bit different, but still a different probability distribution than what you really want to sample.
And this would bias your predictions.
So the really cool thing of Hamiltonia Monte Carlo is that you're actually able to have unbiased sampling through the Metropolis Hastings step.

24:08 And this is a crucial thing.
So it's computationally implementable in general, there's no computational bottlenecks apart from this doubling of state space, and it leads to unbiased sampling.
It's also relatively simple.
So this is why this is really used all over the place.

24:27 There's another few perspectives that might explain why it works so well.
So in the paper in the last subsection of section two, which is about optimization, so the action on optimization is about how to accelerate optimization, how to derive an optimization algorithm.
2.6.
That's the one.
So the whole thing about section two is about deriving an optimization algorithm that accelerated in a physical way.

25:06 And by accelerated, what I mean by accelerated, it's not about just going faster, but it's about having acceleration, which means that if you go slightly up in the paper on the figure, I think this figure is great.
And by the way, I wasn't the one who came up with this figure, but I think this figure is great.
It really gives a lot of intuition for what acceleration really is.
So if you look at the green cup, or I know how you call this, the green well on the left, this would be like a bowl rolling down the well.
And the well is still that honey to like a certain level.

25:56 And so there you get a lot of friction.
So your ball would just roll down very slowly, and the speed of the ball would be proportionate to the slope of the well.
So this is not accelerated because there's a lot of friction.
And so the speed is just proportional to the slope of the well.
So this is actually what gradient descend does.

26:21 But now if you go on the right, you get what people coin physics on under the hand system, which is also an accelerated system, a system that's meaningfully accelerated.
So if you replace the honey in the well by some water, then there's going to be way less friction and your bowl is actually going to accelerate and overshoot the minimum of the well and then sort of stabilize.
But the point here is that this bulb is just going to get so much faster to the minimum.

27:02 This idea for optimization is just extremely powerful.
And by the way, on the right hand side in the graph, you can see the improvements that you get when you implement these sort of ideas.
So this was on a I'll come back to sampling in a bit, I promise.
But this is actually very well, very related.
You can see on the graph on the right what kind of improvements you get when you go from under damp, first order system grade in the sense system, when you go from an over damped first order grade in the sense system to an underdamp second order accelerated system.

27:43 And so you can see the curve, right?
So the black orange curve is over damp.
There's no acceleration.
It's very slow.
The last curve, the blue one, it's accelerated and it's just super fast.

28:00 So you can see it sort of gives you like quantitative data as to how many improvements you can get by implementing this acceleration in a physically meaningful way.

28:13 _Daniel:_

Could you just describe the axes of the graph and also what the league group is here?

28:21 _Lance:_

The lead group is in the figure legend.
In the fourth line, you see the leg group is so n.
So that's technically that's the special orthogonal group of dimensions n.

28:36 If I remember correctly, these are all the matrices, all the square matrices of size n by n that have a determinant equal to one.
So the determinant is just like a function where you give it a matrix and it gives you a number.
The fact that the fact that the determinant is equal to one means that here we're just taking matrices which are, which produce not translations, but changes of coordinates that preserve the geometry in a system.

29:16 Just to elaborate on this a little bit, because for people who are not intimately familiar with matrices, it might seem a little opaque.
So when you have a matrix, a matrix can multiply vectors.
So a square matrix takes in vectors of side of dimension n and it outputs vectors of dimension n by multiplication.
So if you have a square matrix, it just induces a transformation of your state space because each vector, each point which is a vector, gets converted into another point which is another vector.
Now there's a lot of, I guess, properties there, right?

30:04 You could have all sorts of translations of state space or rotations in state space or transformations of state space.
If the determinant of the matrix is equal to one, it means that the transformation of state space that the matrix induces will preserve the geometry of the sixes.
It will preserve distances and it will preserve crucially orientation as well.
Because if you only asked the determinant to be equal to one or minus one, then the matrix transformation would preserve the geometry, but it would not preserve the orientation.
It could mirror things.

30:50 So if you only asked the determinant to be equal to one or minus one, you would get a lead group that's called the orthogonal group, which is usually denoted O of N.
And here we require the determinant to be just equal to one.
And so you get the special orthogonal group.
And so it's this group of matrices that have this property.
Now this is not really important for the example here because you could have taken any other lead group and got something similar and got a similar difference in performance.

31:33 I guess it's just interesting for its own sake.
And so the graph though, the K is the number of iterations.
So the number of time steps, so that's the x axis and the y axis is how close you are from the minimum.
And, and it's in lock scale.
So as you can see, the, the blue curve is going to get like in 100 iterations, it's going to get basically at ten to the minus 410 to the minus five distance from the minimum.

32:05 So it's like super, super close.
It basically gets there in 100 iterations when you take the other normal gradient descent methods where you see that it's going to take so much longer.

32:19 So yeah, this is really the advantage of using second order methods.
And what I mean by second order methods is that by second order means that you actually double the state space to introduce velocities.
So that you not only have a dynamical system over positions, but you have a dynamical system of velocities.
And so it means that you have a physical notion of acceleration because acceleration is a movement of velocities.
And so if you double the state space by saying this is position, this is velocities, and you see I have a motion in this like a state space that's twice as big, then you have a meaningfully, a meaningful notion of acceleration.

33:07 And this is really powerful.
And so you can see already a parallel here, which is that Hamiltonia Monte Carlo also has this notion of acceleration in some way, at least just intuitively, because we also doubled the size of the state space to introduce velocities.
And so it turns out that this intuition is actually you can make it into a formal correspondence.
And I think this is something that quite interests me, to be honest.
So if you remember, if we come back to the intuition for sampling.

33:46 The intuition for sampling through Monte Carlo methods is we have a target distribution that we want to sample from.
So we're going to run a dynamic, random dynamic towards that distribution.
Now, what makes sampling efficient is that the distribution that characterizes the process because again the process is random so that each time it is at a random location that is characterized by distribution.
What makes sampling efficient is that the distribution characterizing the process just converted as fast as possible to the thing that you want to sample from.

34:23 This is to say that you can think of sampling as an optimization on the space of probability distributions.
You want to move your probability distribution of the process as fast as possible to your target.
And so you can see from there that sampling is actually not so different from variational inference.
It's just the same idea, only variational inference.
You're typically going to take a parameterized family of distributions and approximate the targets, while here you have a non parameterized family that's given by your dynamic that's going to perfectly match the target.

35:08 Again, with that, I want you to have the take home message that sampling, you can think about it as an optimization on the space of probability distributions in the sense that you have a target distribution and you want to get there as fast as you can with the process.
Now let's suppose, and so here is the crucial connection between sampling and optimization in the way that we've described it here.
Let's suppose that you run this accelerated optimization scheme on the space of probability distributions then the process.
So you would get the dynamic on the space of probability distributions that has a meaningful notion of acceleration through the accelerated method that was shown here.
So if you look at what kind of dynamic this really gives you, it gives you a process which is given by a stochastic differential equation that is known as under damp launch of a dynamic.

36:18 So there's an equation for it and I think action subsection 2.8.
But the point is under dynamics is a stochastic differential equation whose density or probability distribution stole this accelerated optimulation problem on the space of probability distributions.
So just from there, you know that under that logo on dynamics, it's going to be a very efficient sampler because it meaningfully accelerates and gets the target, I mean, quite fast.
The problem is under label logo on dynamics, you cannot simulate it accurately.
Well, you can simulate it accurately, but you cannot simulate it exactly on your computer in practice.

37:04 So this comes back to the numerical integration problem that we discussed just before.

37:12 And so you have to find a way to discretize or in other words implement under dumpling bound dynamics on your computer in such a way that you retain that the thing that you implemented on the computer retains this meaningful notion of acceleration.
It turns.
Out that you can see Hamiltonian Monte Carlo as a faithful numerical discretion or numerical implementation of under damp launcher and dynamics that's going to preserve these acceleration properties and therefore this efficient sampling.
So this is all like, yeah, a lot of interesting connections.
But basically what I want to get at is you really have this notion of acceleration that permeates well, I guess physics.

38:08 But here it permeates sampling and it permeates optimization.
And so the method that was shown here about optimization and Hamiltonian Monte Carlo, they're just the same in a way.
Only one is applied to optimization, the other is applied to optimization on probability distributions of Aka sampling.

38:32 Great.

38:33 _Daniel:_

I guess last question on this part.
What is the shadow Hamiltonian and why does it sound so cool?

38:40 _Lance:_

I know, right?
Yeah, it's really cool.

38:44 It's a recall name.
So the shadow of Hamiltonian is okay, so let's go back to the Hamiltonian.
So we have a Hamiltonian, and we want to simulate the dynamic that preserve the Hamiltonian.
We want to implement that on the computer.
We're going to do that through geometric integration.

39:04 Geometric integration gives you a bunch of algorithms to preserve the Hamiltonian.
I mean, a bunch of algorithms they can implement on the computer, and they're going to preserve the Hamiltonian.
Do they actually really preserve the Hamiltonian?
It turns out that no.
So what I said before is a bit of a shortcut, because the numerical integration that you get through any numerical method, including geometric integration, is not going to exactly preserve the Hamiltonian, but it's going to preserve what people call a shadow hamiltonian, which is almost the same as the Hamiltonian, but with extra terms that sort of vanish if the time step is very short.

39:56 So this is to say that your numerical dynamic implemented through geometric integration is going to exactly preserve the shadow Hamiltonian and approximately preserve the true Hamiltonian.
In the papers, we show I don't know if it's well, it's probably algorithm dependent, but basically, depending on the algorithm that you choose, you want to show to what extent the shadow Hamiltonian truly approximates the true Hamiltonian.
The virtue of geometric integration methods is that actually the shadow Hamiltonian turns out to be extremely close to true Hamiltonian, which dean that you can take a very long time steps and still be very good at preserving the true Hamiltonian.
So here, when you implement these methods, you don't exactly preserve the true Hamiltonian, but you still do it pretty well.

40:57 And so in Hamiltonian Monte Carlo, the momentum refreshment, and Metropolis, usually the Metropolis Hastings accept rejects that is going to correct for those failures of truly preserving the Hamiltonian.

41:17 So even though you don't exactly preserve the Hamiltonian in your numerical integration, in Hamiltonian Monte Carlo, the Metropolis hating accept reject step is going to correct for this inaccuracy.
And so this is like, really the true beauty of Hamiltonian Monte Carlo is that even though you get a lot of things that are not exactly preserved when you implement things on a computer.
Thanks to Metropolitan Hastings, overall your sampling is going to be perfect in the sense that you're going to truly preserve your target distribution.
So this is really the key.
Now, a follow up question to that is, okay, well, if Metropolis Hastings is just so crucial and it just gives your dynamic the property that it's going to preserve, whatever it does, even if it samples really badly if?

42:19 You add Metropolis Hastings, it's still going to preserve your Target distribution.
Then why can't You Just Come up with an average process, like whatever Kind Of process?
And that Metropolis Hastings at the end?
And so you can do that.
You can take any kind of process.

42:43 Let's say you take a random process, it could be the worst in the world.
Let's say you wanted to sample from a gaussian and you actually take a Brown in motion.
Now this is clearly not going to work because Brown Emotion just goes all over the place.
It could go infinitely far.
Brown in motion, it's just like random action, right?

43:02 Completely random motion.
There is structure to it, but the structure in Brown in Motion means that it's such that brown in motion is just going to just spread really far.
So Brown in motion is not going to preserve your target distribution and it's also going to be very slow, by the way.
So it's not going to be a good sampler if you add Metropolis Hastings on Brown emotion, which is you integrate brand action.
So you simulate a step of brand emotion on the computer and then you do Metropolis Hastings to know whether you should accept or reject that step.

43:44 Metropolis Hastings will tell you whether you should do it or not.
You either accept and you keep going from that new position, or you reject and you start from where you started from and take a new sample.
Accept, reject.
If you accept, you keep going.
If you reject, you go back and you sort of go like that.

44:05 So if you do materially facing there, your standard is going to be exact.
So it is going to preserve the target and so you're going to have accurate sound plan.
And so this is crucial.
This really highlights the importance of Metropolis Hastings.
But there is a big but your sampler here is going to be extremely slow.

44:31 It's going to be extremely slow, first of all, because brand in action in and of itself, it doesn't at all preserve the target distribution.
I mean, it just goes all over the place.
And you just want to sample a lot around the mode of the gaussian, for example.
So it means that Metropolis hasting will reject a lot of your steps because a lot of your steps will try to go further away while you want to stay around the mode typically of the gapsin.
So you're going to do a lot of steps for nothing and also Brown in Motion just does not have the qualities that make a sampler efficient.

45:13 And so the reason why Hamiltonian Monte Carlo is so good is because it's able to integrate Metropolis Hastings and still preserve a lot of other properties that make the sampler efficient.
So if we remember, HamiltonI Monte Carlo has this geometric integration that does not exactly preserve the Hamiltonian, but it does still does it pretty well approximately by preserving a shadow Hamiltonian.
So this means already that integration step is going to be really good.
So there's going to be a lot of acceptance in the Metropolis Hastings and also the way the scheme is set up, there's going to be a lot of acceptance set in the Metropolis Hastings.
So it means that most of the samples that you would draw will actually be used instead of being rejected and you have to start over again.

46:15 That's one advantage.
The other advantage of Hamiltonium and T Carlo, and this is a crucial one and we kind of discussed this last week, is that one crucial thing to be a good sampler is this idea of time irreversibility.
So I'll emphasize it again because it's really crucial and there's a lot of literature on this and it's something that we reviewed also in the paper.
So a sampler that is time reversible that is time irreversible is always going to be better or it's at least not going to be worse than a sampler that is time reversible.
So what do we mean by this?

46:58 A sample is time irreversible?
If and on the if were you to play the dynamics forward or backward, there will be going on your bullet point here.
A sample is time reversible if and on the if you were to play the dynamics forward or backward in time, so forward in time and then maybe you would play them by reversing the movie by playing the movie backwards.
If you were to do that, then the two movies that you would see would be qualitatively the same and statistically the same.
So the process is time reversible if and only if the process, if you're running forward or backward, it's basically statistically the same.

47:51 Now, what does this mean in practice?
Well, if your process is time reversible, then it's going to backtrack very often, actually.
So it means that you would be somewhere in the probability distribution, just something there and you will go forward and then you probably go backward and so on and you kind of get stuck in a region until you go somewhere else.
But it's just going to be very slow to move around and so it's going to be very slow to get good sampling because it's going to take you a long time to visit all the regions of the probate distribution.
In other words, the distribution characterizing the process.

48:34 It's going to move very slowly to the target distribution that's another way to look at it.
If the process is time irreversible, on the other hand, then it's a lot less likely to go backward during the sampling process.
So it means that it's going to visit the target distribution a lot more.
I mean, it's just going to go around.
Imagine if you're not allowed to go backward just as a human being and you're walking around, you're just going to end up in many more places than if you were allowed to go backward.

49:08 And if you were just going backward all the time to where you started, then you wouldn't be able to do a lot of visiting.
So it would be a bad sampler.
So again, there's some, like straightforward intuition there.
So one idea is in sampling is we want to optimize the extent to which a sampler is timely reversible.
We want to increase time irreversibility as much as we can force a sampler to just move around as much as possible.

49:42 So that's an idea.
It is explored currently.
I guess it's a bit of an open problem of how do you really do that and how do you implement that on the computer in a way that works and preserves all the properties.
But the point I wanted to get to is that Metropolis Hastings is a blessing and it's also a curse.
It is a blessing because when you add it to any kind of process, you will make your sampling unbiased.

50:14 So it means that you will sample the Ride distribution even though you're implementing this on a computer.
And there can be a lot, so many issues with the numerical integration, numerical approximation and so on.
But it's also a curse because whenever you add Metropolis Hastings on the process, it's going to make it time reversible.

50:45 Actually, yeah, if you just took a random process and added metropolisA, you would get something that's inevitably going to be quite slow.
And so now you get to the problem or the conundrum.
What do I do?
Do I go for unbiased sampling?
Do I care about accuracy?

51:08 And then I should add Metropolis Hastings.
Or do I not care about accuracy so much and then I should not have Metropolis Hastings and it's going to go faster generally.

51:23 And so Hamiltonia Monte Carlo actually has the blessing and does not have the curse.
And this is why Hamiltonian Monte Carlo is just so good.
And again, it's also complementary to all of the things that we've been discussing.
And the reason why Hamiltonian Monte Carlo is blessed and not cursed is because the momentum, how do you call this?
The Metropolis Hastings is just done on the momentum refreshment step as opposed to being done on the overall dynamic.

52:01 So because if you remember, you do geometric integration to simulate Hamiltonian dynamics, every once in a while you will take a momentum refreshment and then do Metropolis Hastings on that momentum refreshment, as opposed to doing Metropolis Hastings on both the Hamiltonian dynamic and the momentum refreshment.
So it's not something that I can really explain how that works, but it turns out that by just doing the Metropolis method, montacarlo is a way of having Metropolis Hastings in a way that you preserve the unbiasedness so that your sampling is accurate, but you don't sacrifice the time irreversibility.
And so you get both.

52:53 And this is because the Metropolis hasting is just on one of the components and not on both.

53:01 _Daniel:_

To kind of connect that to an example.
As we move into active inference here, we have some probability isocontours, some, we have the high probability carpool lane, and then we have some lower probability lanes, and we can go different speeds in these lanes.
And we want to have a full accelerated model here.
It's almost like the MH is refreshing our velocity just asking when we want to change the lanes.

53:34 But it's not our full self driving car Metropolis Hastings algorithm.
But we're able to use our position and acceleration when we're in our lane to take full advantage of the acceleration following the shadow road.
Not necessarily the true road, but the shadow road is close enough, or the shadows on the road, and then lane changes.
Are these computationally costly and reversible, but still super useful propositions?

54:12 _Lance:_

Exactly.

54:13 And they're actually not computationally costly.
They would be if you were to reject many samples.
But here in Hamiltonian Monte Carto, typically you don't get to reject many samples.
So yeah, that's such a great picture.
So the car follows the Shadow Road by just doing geometric integration and following the shadow.

54:38 Hamiltonian every once in a while, you get a momentum refreshment.
Velocity refreshment, which is, oh, now I move to the first lane, or the second lane, third lane, and so on.
And you get a Metropolis Hastings Corrections step that says, do I accept this proposal of lane change or do I reject it?
And still on the coast.

55:01 _Daniel:_

So how does this connect active inference lab?

55:06 _Lance:_

Well, I mean, great question.
So active imprints in active inference proper, you don't have any sampling in active imprints.
Whenever you want to scale active inference to implement it, to solve any kind of problem in the world, you want to do sampling because there's a lot of computations that are not going to be trackable otherwise.
And so one cool example is in the figure after this, actually.
So for any kind of decision making active inference lab, you need to approximate the expected free energy.

55:53 The one just before yeah, perfect.
So if you look at the second equation there, you get this minus lock p of an action sequence equals expectation of something.
This minus lock p of the action sequence is our notation in this paper for the expected free energy.

56:20 You probably all know this, the expected free energy is given by the expectation of something.
Now typically, and when you have a very high dimensional model, which happens in most applications, I would say you get a very high dimensional expectation.
What is an expectation?
An expectation is an integral with respect to probability distribution.
How do you compute expectations while you do that?

56:50 Through sampling, or at least sampling is the way to compute high dimensional expectations.
That's the most efficient in statistics.
And this is the reason why sampling is studied in statistics, is because that's how you solve these problems.
I mean, expectations just come up everywhere, just like so many things about machine learning bowl down to computing expectations.
And so here in particular, the expectation that is very dear to us, very close to our hearts, is the one that gives you the expected free energy.

57:33 The expected is the expectation of something.
So how do you compute that in a high dimensional model where you have to use something?

57:45 There comes the usefulness of Hamiltonian Monte Carlo.
If you have a discrete state space based model, you're not going to be able to use Hamiltonian Monte Carlo because Hamiltonian Monte Carlo is on continuous states based models.
It's on continuous state space, right?
We talked about continuous positions, continuous velocity.
I talked about something a probability distribution on my desk, which is a continuous state space.

58:12 So you're not going to be able to use Hamiltonian Monte Carlo if you have partially observed mark of decision process and you're doing active inference there.
But if you have for example, I've been talking recently to Ryan Smith, who does a lot of active inference, and he's really leading a lot of the modeling work with active inference and real data of patients of all sorts, many medical data, and also using active inference to model psychological experiments.
And one of the things he told me about well is, okay, well, I have a bunch of data, and partially observed markup decision process is just not going to do it.
Why is he not going to do it?
Because the data that he has lives on a continuous space.

59:04 I don't remember exactly what it was, but let's just say, for the sake of example, that that data was the temperature in the room, and the subjects had to infer the temperature in the room based on their sensations.
So that's a continuous state space problem.
Now, imagine that you ask someone to infer the temperature in the room.
Then maybe you would change the temperature in the room or not, and you would ask them again.
Change the temperature or not and ask them again, and so on.

59:41 When you have this sort of set up, you have a discrete you have a phenomenon that unfolds in discrete time because you just repeatedly ask some questions and sometimes elapses between the questions.

59:57 But you also have a state space that's continuous.
When you have this sort of data, then the kind of model that you want to use is a partially observed mark of decision process that we know and love but the state space is going to be continuous instead of discrete.
The planet is still going to be discreet.
Now, when you have this sort of model, I just want to say it or as an aside, that for the moment, a lot of the modeling work and simulation work in Active inference uses the sweet state space pound DPS, partially observed mark of the same process just because it's been sufficient.
And when you simulate agent is often like in grid worlds and when you maybe have a state spaces in experiments they often by design discrete because it's just easier to handle.

1:00:49 But that's not something, that's not an assumption, a simplifying assumption that we're going to be able to keep for that much longer.
There's just so many things that you cannot account with these sort of models.
So one other model that is interesting to have is partially observed Markov decision process, but with a continuous state space.
So with those you get the problem of estimating the expected free energy which would be then an expectation or in other words, an integration, an integral in a continuous takes place.
And so how do you do that efficiently if you are in a high dimensional state space?

1:01:34 Where do you use?
Hamilton, monte Carlo.
I think this wouldn't be really the best.
So this is how you join the dots in this paper.
We didn't talk about sampling in discrete space because the methods are quite different.

1:01:52 So we really had to choose what to focus on.
There's of course a lot more methods in the literature than there are in this paper.
We just wanted to sort of review what were the main ones and what people really used in practice.
But when you have the expected principal in a discrete state space, computing the expectation that defines the expected priority can often be a little bit easier because it comes down computationally to a bunch of matrix multiplications.
Matrix vector multiplications, which generally is doable, unless the state space is enormously high.

1:02:37 And then we'd have to think of sampling methods in this sweet space.
But as soon as you move to a partially observed markup decision process with a continuous space, which are argu and Ryan Smith argues and I'm sure a lot of people have run into this as soon as you have this kind of model, well, yeah, you just have an integration problem in continuous space.
And so Hamiltonium Altekaro is the way to go there.

1:03:08 _Daniel:_

Awesome.
And your 2020 paper was a synthesis on some of the discrete statespace formalisms of active.
So it's very interesting to see how you're now talking about where continuous time, continuous state spaces can come into play and how interesting the Active inference has the capacity to deal with discrete and continuous date spaces.
And sometimes we lean on one leg or the other leg more, but it spans the gap in a way that's actually like a value adding, not like there's some sort of missing piece from one side or the other.

1:03:52 _Lance:_

Yeah, definitely.

1:03:54 I think active inference is great because it's so flexible in the sort of models that you can consider.
But yeah, historically the first models to be developed were continuous space and continuous time.
And then it works quite well because you can take gradients of the free energy and just minimize them over time.
So you could get around basically everything by doing a grain and assemble free energy.
And then after that around like so that was like 2010.

1:04:27 And then around 2015, people started thinking, okay, well, how do I model discrete time decision making with active inference and typically decision making tasks, at least the simple ones that are studied in neuroscience and behavior neuroscience, just to make things simple, the number of actions that you have is discrete.
So you have a finite number of actions, which is pretty small.
You would also have a finite number of states, which would be pretty small.
And then people started to think, okay, well, how do we active inference lab to actually account for that?
And so, yes, and so that's how the whole expectation free energy and partially observed mark of decision processes came into play.

1:05:20 And now the community has grown a lot and there's more and more data that we want to account for.
There's more and more projects that are going on and, you know, people are realizing it's an obvious realization.

1:05:38 It's not surprising at all that these two models developed in 2010, 2015.
They they're just not going to account for everything.
You need to think about other kinds of models.
It really depends on what kind of data you have at hand.
And then one important and obvious type of model would be partially observed Markov decision process with continuous space.

1:06:02 And actually, this is not a new thing.
I mean, people have been using these kind of models in reinforcement learning and control for a long time.
I don't know to what extent they've arrived at practically I mean, they arrived at practically instrumental algorithms.
I don't know to what extent they're used, to what extent their state of the art.
But the point is, it's something that it's a kind of model that has existed for a long time.

1:06:34 And so this sampling would be a way to actually practically implement this and scale it when you want to put that within active inference.
So I think it's an important thing to think about.

1:06:51 _Daniel:_

Awesome.

1:06:52 _Lance:_

Yeah.

1:06:52 _Daniel:_

Thomas Parr, also recently in a discussion on the textbook was sharing some timelines.
And it's just so interesting how these things have been developing and from continuous through characterization of the discrete, in a sense not culminating, but being synthesized in your 2020 paper.
And now there's with an increased emphasis on empirical data, the desire to bring in a lot of these methods that actually help us implement it rather than just think about it, really parsimoniously.

1:07:29 So what is your active inference representation in the figure of the running person?
And then how do the variables and the processes described in this figure relate to all of this?
5 hours of talking about Shadow Hamiltonians.

1:07:54 _Lance:_

And all of this, right?
Yeah, that's a broad question.

1:07:59 We might need another Daniel to answer that in detail, but just very short.
Well, the active inference section was meant to be as complete as possible, even though it was very short.
And by completeness I mean that we started by deriving active inference and deriving active inference free energy principle.
So this is really what the free energy principle does, even though we weren't able of course, to review the whole free energy principle in like one or two pages.
But what we focused on was deriving the expected free energy free energy principle and then from there you get the full active inference algorithm.

1:08:46 So full active inference algorithm, I think you just went past it's just below if you go slightly below, I think maybe page 29 or page 30 still, I think next realizing an active agents.
So this is the active infrastructure algorithm, like 0.12.3 or something, just from a duration of the expected pre energy.
You actually get as a corollary from there, the active imprint algorithm that we know and love.
This is actually a more general version than what people use and I'm be excited and I'm actually talking to people to actually implement that.
But this is actually the most general version that has been established in the literature and it is more general in a meaningful way in the sense that all the beliefs, all the probability distribution, they are over trajectories or sequences of events.

1:09:44 So it means that all the computations, they not only consider events at a particular time in the future, for example, but they consider trajectories of sequences of events.
And so this is considering different events at different points in time and their independencies and dependencies between them.
So this is just to say that if you would take then this algorithm and you would perform a mini field approximation over time, which is saying that all the things that you see in the future are sort of independent of each other at different points in time, then you would recover what people typically use in the literature, which is easily implementable.
The point I want to make here is that you can actually not have that limitation and have things that are a bit more complex, that are able to capture more complex relationships in the time series and input that.

1:10:55 They may be receiving, like, the kind of sensory data that they may be receiving and the kind of generative models that they would have.

1:11:02 So anyway, this is the active inference algorithm, the most general one.
We derive that from first principles by deriving the expected community from first principles.
And so this relates us to that figure that you just showed.
So that figure that you showed with S on A is the starting point of the free energy principle described in this paper.
And so the point is that we want to describe decision making, want to describe actions as a function of sensations, and we want to come up with the most general description of actions as a function of sensations to be able to account for everything.

1:11:49 That's kind of the idea of the pre engineer principle.
So what do we do is we consider a world, a world in which there is an environment and an agent.
And so the environment here is denoted by S, and S is a stochastic process.
Why a stochastic process?
Because a stochastic process is the most general type of dynamic that exists, at least as far as I know.

1:12:15 It's really a random dynamic.
And it could be random in all sorts of ways.
It could also be non random.
We sort of take the stochastic, the random aspect, as an extra ingredient, just to include a lot more types of scenarios and things you can be confronted with.
So you partition the world into the agent, which is O and A, and the environment, which is S, and the agent.

1:12:40 Then you subdivide it into two more components, which are O and A.
O are what we call the observable states.
These are like the sensations of the observations that you get at any point in time, also a stochastic process.
And finally, you have the autonomous states.
Or you could think about it loosely as the active states.

1:13:03 They turn out to be the active states in the implementation.
But so the active states, they're really like the muscles, the things you can actually activate and make and then activate to influence the world.
So we just partitioned the world into these three sets of states that interact and evolve in some way.
They're both stochastic processes that interact.
And the goal of the community principle, at least when applied to decision making, is that you want to describe A as a function of O, because what happens as an organism, you have control over A, you have access.

1:13:48 To O, but you don't have direct control of O over your sensations.
And you don't have access to S because that's the environment and beyond the markup.
Like it beyond you, beyond your envelope.
So you don't have access to S.
You know, O and you can control A is what you can choose from.

1:14:07 And so the free energy principle just answers the question, okay, well, if I take this very general description of the world, what is the equation of A as a function of O?
How can I describe A as a function of o?
And so it turns out there's some mild assumptions in this.
And these assumptions, they're guided by physical considerations about how humans are and how humans interact with the world, but they're very mild.
But whenever you take.

1:14:45 These assumptions, you get that the active states or the autonomous states minimize expected free energy.
So this is like a very 16th derivation of the expected free energy.
From first principles, we start with the partition of the world.
We describe active states as a function of observations.
As it turns out, that the expected free energy is what describes the active states as a function of observations.

1:15:19 The basic active inference algorithm, which everybody uses and which we have also in paper, is about computing the expected free energy and then selecting actions that minimizes expected free energy.
So the expected free energy, as we saw, I think it's in the next figure.
So the one with all the panels, we've seen it a couple of times already.
It's an expectation with posterior distributions in it.
What I mean by posterior distributions here is that these are distributions conditioned on the history of the agent, so on the observations that he has already seen and on the action that he has already taken.

1:16:08 In any case, the expected free energy is an expectation with posterior distributions within.
So it means that to compute the expected free energy, you have two problems.
You have computing posterior distribution through Bayes and inference, Bayesian rule.
And once you have them, you can plug them in into this equation.
And then you need to complete the the expectation, and then you get the expected free energy.

1:16:34 So the first thing is about computing the posterior distributions.
Now, what has been proposed in the literature so far is, well, how do you do approximate inference?
How do you actually approximate distributions?
You do that through variational inference or approximate inference by minimizing free energy.

1:16:55 The treatment here, the derivation, and our aim was to do that, provide a derivation that was as conceptually simple as possible.
Actually, it highlights that the free energy is not the most important thing here.
The important thing is really the expected free energy.
The free energy is just a tool to approximate the posterior distributions, to then get the expected free energy.
But you could actually use any other type of divergence.

1:17:26 The free energy is just like a KL divergence plus some term that makes the whole thing tractable.
And so you can minimize the KL divergence to approximate the target distribution.
But actually, what this view highlights, and by the way, I'm not at all against the free energy.
I think it's really cool.
And there's so many methods to minimize free energy.

1:17:48 If you can do that, then fine and sure, go for it.
Like, way to go.
But imagine you could not do that.
It would not at all be a problem because you could use any other kind of divergence to solve those inference problems.

1:18:04 So that would be the first step.
You can approximate those particular distributions by doing some kind of approximate inference, which would be through minimization of reenergy or through minimization of something else.
And then you have the second step, which is computing the expectation.
Now, either you're in a low number of states, discrete states from the P like thing and it's all a matter of vector matrix multiplications that are attractable.
Either you have a very high number of discrete states and then you need to think about sampling in discrete states, which we didn't discuss in this paper.

1:18:45 Either you are in a continuous state space and then you have an expectation in continuous state space and then you want to think about an alternative Monte Carlo, for example.
So now with these two steps you have now an estimate of the expected free energy which gives you the quality of any action sequence.
And so it's not only the quality, but it's actually the negative Lock probability of any action sequence regarding in this formalism.
Because if you remember, the premise of all this was to describe actions as functional sensations in a physical system, not even a physical system, but in interacting stochastic processes.

1:19:34 And so the answer to that was well, the expected free energy gives us how actions relate to sensations, the expected free energy.
And this is why we used the letter, we used minus Lock p as opposed to G to emphasize that the expected free energy is not just like a function of action sequences, but it is really the negative log probability of an action sequence given some sensations.
And so once you have computed the expected free energy, you had this minus log probability of an action sequence.
If you take the exponential negative of that, the exponential negative of the expected free energy, you get the probability distribution over action sequences.

1:20:32 And so by the way, this exponential negative of expected free energy is what we use all the time.
You might recognize this as the soft max of negative expected free energy.
This is just all the time kind of fundamental thing, active inference lab models.
So I'm really talking about the same thing here.
So once you take the soft max of negative expected free energy, you get P of A, which is the distribution over action sequences.

1:21:03 And now you have two possibilities.
Either you want to stimulate the most likely action sequence, in which case you want to simulate the action sequence that maximizes the probability distribution.
So in effect, you have an optimization problem out of all.
Yeah, you need to find the action sequence that is going to maximize this probability distribution that's given by the expected free energy or you want to simulate a typical action.
So when do I mean a typical action?

1:21:41 A typical action or a typical action sequence is just a sample from the distribution.
And so if you want to sample from I mean, if you want to do that, then you have a sampling problem where again you need to sample from a distribution over action sequences given by the expected free energy.
So this is really how all these methodologies connect.

1:22:13 I think that's kind of it, yeah.
One last thing is, typically when we stimulate active inference, we never do the sampling at the end.
We always take the action sequence that minimizes expected free energy.

1:22:29 In other words, the action sequence that maximizes that probability distribution.
And this is because when we simulate things, it turns out this is how people have done it in the literature.
People are more interested in the most likely action sequence that an organism or an agent would produce.
But if you want to model data, if you want to use active inference to model data, then you actually want to not just simulate the most likely action sequence, but simulate any kind of action sequence that would fall out of this.
And so this is really the case where you need to sample from that final distribution as opposed to do your optimization.

1:23:17 So depending on the use case, you either have a sampling or an optimization problem after you've computed the expected free energy.
So this is how these whole things fall together.
And so you might be asking, okay, well, you talked about sampling and optimization.
There's also a section about inference.
Where does that fit in?

1:23:39 And so it fits in on the remark I gave that we have these postered distributions within the expected free energy.
How do we compute them?
How do we approximate them?
One way is by minimizing free energy.
Another way is by minimizing any other kind of divergence.

1:24:00 And in that section over there, we just reviewed some kind of divergences that are very popular in the statistical inference literature, mainly because they have desirable properties.
And so if you weren't able to use the variation of free energy for some reason, or maybe something to be explored, and something to be explored is just to use other types of divergences and just see what happens.

1:24:34 So the open problem to be explored is whether we can get better performance by using different kinds of divergences and see what we get.
Maybe there's part of algorithms that are out there with these other types of divergences that we can make use of to do better performance, to get better performance.
Can we actually describe and quantify the improvements in performance that we get by using these other types of algorithms?
When would these be appropriate and useful?
These are all open questions.

1:25:09 Another open question that I think is interesting is can we model maladaptive behavior by using different kinds of divergences that would not work as well as the free energy?
And there's an interesting paper on that by newer sajid and colleagues.
I think it's called Bayesian Brains and the Rennie Divergence.
It's been published on neurocomputation, I think, last year or the year before.
And so in that paper, instead of using the variation of free energy to approximate all these posterior distributions, she used the rainy divergence, which is which generalizes the KL divergence in some way, and show that for different rainy divergences, you get different types of approximate posteriors.

1:26:05 And she basically looked into what kind of differences you get from there in terms of perception, in terms of decisionmaking.
And she showed that for that particular divergence, divergence, I think the conclusion was that you basically get different phenomenology, you get different behavior, suggest something to be explored.
I think the upshot was that maybe I don't remember how far the paper went in this, but I think kind of the goal was to model maladaptive behavior using some kinds of rainy divergences that did not work as well as the free energy.
So this is to say, so this is an interesting work.
One could examine other kinds of divergences and see whether you actually get better or worse performance than with the free energy.

1:27:03 One thing, one word of caution, though, is the free energy is just so good in the sense that it uses the KL divergence.
And as I mentioned at the beginning, the KL divergence has so many properties and it's just so fundamental.
It's not straightforward to see that when you first come up with it.
But I guess the more I read in different disciplines and the more the Chao divergence comes up and the more the more I see properties of Kale divergence in different disciplines that just make it so interesting.
Like, for example, the Kale divergence, Bayesian Statistics Physics is the relative entropy.

1:27:47 So it quantifies the amount of entropy that a distribution has with respect to another.
Entropy, as we know, is just a very fundamental thing in information theory.
The KL divergence quantifies the difference in information between two distributions, the amount of bits that you would need to if you take two distributions, A and B, the KL between the two quantifies the amount of information that it takes to go from one to the other.
So now you might object and say, okay, but KL A and B is different from KL, B and A.
And so how can it be that it quantifies the amount of information they need to go from A to B or B to A because it's not symmetric.

1:28:41 So the answer is it's either KL of A and B that has this meaning, or KL of B and A that has this meaning.
And I just can never remember which direction, but it's one of them that has this interpretation in terms of the difference in information anyway.
So Kia is just like something, it just comes up everywhere and it's just so useful, and it has all of these nice properties which makes these free energy really a construct of choice.
But that said, there's other divergences, one of them which we describe a bit in the paper called the maximum mean discrepancy, which I think also has properties.
It's not necessarily well, it's very different in terms of how you construct it from the KL divergence.

1:29:37 But I think my current understanding right now.
And my current understanding right now is that if you cannot use KL, then maximum mean discrepancy is just like, be nice.

1:29:51 But yeah.
So the word of caution was that probably most divergences out there are not going to do as good of a job as a free energy, but some clever ones might.
And it's an open problem of determining which is how we get the link between all these different sections.
So to do perception, we need the inference.
To do decision making, that is, computing the expected free energy, we need sampling typically.

1:30:25 And then to do action selection, we either need sampling or optimization.
And also inference is an optimization of belief.
Updating also, as we've discussed, is also an optimization of probability distributions.
You can see that as an optimization of beliefs as well.
So it's all very tightly interconnected.

1:30:50 Wow.

1:30:51 _Daniel:_

Thank you, Lance.
That's very informative.
Brings up a lot of ways to go and it really shines a different light on even what, learning active inference or learning free energy principle.
It was a roller coaster just listening.

1:31:14 When you describe the figure of the running person and the new generalized representation here, which is so sparse it looks like it's pseudocode, but it's actually basically necessary and sufficient to describe action.

1:31:33 _Lance:_

Yeah, it is pseudocode and it is also exact like this is really what active inference boils down to.
And that was kind of like where we got at.
We're like, okay, well, we had this mess of papers of active inference.
Not that they're actually immense, but, you know, there's so much information and we're really thinking, reading all the latest free energy principle literature that I've also worked on a lot and also active inference lab literature and really thinking, okay, well, how do we strip all that of the neuroscience?

1:32:06 How do we strip all that of the cognitive science?
How do we just retain the math and present it in the simplest way possible?
That would be appealing for mathematician and also hopefully for a computer scientist.
It turns out that we got a way simpler perspective than anything that's out there, I think.
And really?

1:32:27 Yeah.
So this is the active inference algorithm in pseudocode and in detail also in a way.

1:32:37 _Daniel:_

So totally agree.
Again, thanks for the work and for sharing it this way because it is the fewest pixels for the highest resolution picture.
Then to describe the fundamental cybernetic challenge as a partition, an axiomatic partition, which one can then say also has grounding in the spatial temporal boundaries of the world or in geometric boundaries in informational spaces.
But the particular partition is used to separate in the map, not necessarily making claims about the territory and the actual nature of the objects and their articulations or anatomy, but on the map, which we get to construct.
We make it in a way that's amenable to the particular partition, which is not too much more than the separation of figure from ground or agent based modeling.

1:33:39 It's just a separation of some autonomous entity from some external process.
Then the task of the free energy principle applied to decision making, as you said, was to describe action as a function of observation and everything in between is broadly considered cognitive but for any given system it's going to play out in this immensely nuanced way with a lot of bespoke mechanisms.
And why do we take that particular partition step?
Well, it's kind of like read, write access in the computer system there's things we don't have access to hidden states and also the reverse of that which is we can't access hidden states nor them influence or affect us.
So I think of that as like no telekinesis, no telepathy.

1:34:35 You can't go directly across the blanket.
You have to intermediate through the blanket of observation and action.
And then with respect to our particular states, our blanket and internal states, we have access to observations, but not direct control, nor necessarily would we want to.
Because if we had the lever to change what we directly received, then algorithms might learn strategies that basically self deceive so that the observations look good, look good, look good, until the whole system crashes.
So we want access to observations but not direct control.

1:35:13 And then the autonomous states are what we in the optimal ideal situation have total control of which is like our mind and our body, what we think and what we do.
It turns out through the pragmatic turn and the inactivist insights in cognitive science that a lot of action sequences have to do with changing what observations are sought after like epistemic affordance.
So there is an enmeshment of action but it's also really important that we have access but not control of observations.
We don't want to have our control on the thermometer but we want the best possible thermometer and then we want to control the best possible interpretation that's like signal processing and the best possible action sequence which is like decision making and control theory.
And then free energy principle is addressing that question what is the equation of action as a function of observation?

1:36:17 But then it was quite a rollercoaster when you said that the free energy wasn't even necessarily the only way to do it.
But it's absolutely true.
The properties of the free energy are inherited from one of the terms being KL divergence and the other having the ability to basically ignore in certain relative expected free energy calculation contexts.
So then in that situation differences in free energy do come down to differences in the KL which does have all these properties.
But that doesn't mean that the free energy is itself axiomatically posited it's actually downstream of the particular partition to use free energy or anything like that at all and other discrepancies may have other properties in different ways.

1:37:08 _Lance:_

Exactly.
There's a bit of a nuance in the sense that here we presented version of the free energy principle, just describing decision making as you summarize though describing A as a function of O.

1:37:25 And by the way, about that, we didn't even talk about Markov blanket in this paper.
I would say that the markup blanket is under the hood because we're saying, okay, well, these are the states that you have access to and these are the states that you do not.
The states that you have access to are A and O.
The states are the agent.
The states that you do not have access to are the environment.

1:37:47 So in some sense there is a markup blanket, but we didn't even have to mention that in the paper.
It's just you partition the world into three sets of states, S, O and A, that are by definition A.
And you just yeah, just from this trip partition, you want to describe one as a function of another, ignoring the third.
And so that's how you derive expected green energy.
You see that action sequences are described by the expected free energy.

1:38:23 And this is a functional sensations if we want further in the and so this is just what you need crucially, this is just what you need to derive.
Active Inference Lab Algorithm if we went further in reviewing the free energy principle, then we would see the fundamental role that the free energy plays.

1:38:48 And so actually, when reading the latest papers on the mathematical theory of the free energy principle, the role of the variation of free energy is pretty clear.

1:39:01 But here the point is that if we just care about decision making, if we just care about the normal active inference algorithm, then we don't even need the variation of free energy.
So sure, the free energy should be preferred.
Why not, if it is available?
But if it is not for some reason, then there's no reason why not to use another kind of divergence.

1:39:32 _Daniel:_

Very interesting.
It's making me think about linear regression and the sum of squares, the L two norm is one approach that's often used to fit a regression line because it has good optimization properties, there's good software packages, there's good education, there's good communication around it and so on.
But one can select other norms and choose to fit a linear regression with an L one norm or with an L three norm.
And so that entire question of fitting the linear aggression is a degree of freedom.
How the regression is fit, that's downstream of a commitment to, for example, model a system in a generalized linear modeling framework.

1:40:21 And so analogously, the upstream commitment or the first principles which yes, can be understood as axiomatic and also have some empirical status in terms of this partitioning.
A figure from ground the particular partition can simply be accepted axiomatically, which is to say without appeal to evidence.
Or somebody might have another upstream axiom and choose to model things according to a particular partition.
From there, just like we could have chosen the L one, two, three norm there are different discrepancy criteria or measures that we might want to use, and some of them apply better or worse or not at all, depending on what software, hardware, data set, and generative model we have.
And so it makes sense.

1:41:22 Pull back into the upstream understanding active inference lab as a process theory for particular partitioned systems.
And then for those who want to engage in the modeling to have that discussion about the garden of the branching paths, well, you could use a discrete time or you could use a continuous time, and then from here, you could do this sampling.
Or you could do that one.
And if we have this computer access, we can do that.
But if we have to do it this way, we'll do it like that.

1:41:58 And that's all operational and logistical, but it's actually all under the umbrella or under the auspice of the theoretical or conceptual commitments that are actually not being questioned once one is in that modeling discussion.
Just like you could have the L one two three norm conversation, and maybe a reviewer asks you why you chose the two norm versus the three.
But it's a broader level of questioning why one took on the linear modeling framework at all.
And our analogous upstream bottleneck, not in terms of rate limiting, but just in terms of like, eye of the needle is the particular partition.

1:42:44 _Lance:_

Yes, definitely.
And I just want to add something actually about the choice of divergences or the choice of discrepancy that you might want to use to solve the inference problem.
I think the analogy with linear regression is a really good one.
When you do linear regression, yeah, you can use all types of norms, and it's really a design choice here in the algorithm, you also have that design choice that you're going to use KL.
So free energy to do active inference.

1:43:14 By the way, the inferences are really equation 43 and 44, which are approximate actually, you had them in the slide.

1:43:24 _Daniel:_

Already, 43 and 44 here, got it.

1:43:30 _Lance:_

Which are approximate some posterior distribution with an approximate posterior distribution.
So you can do that with the pre energy, which is the same as the KL divergence, or you could do that with a whole bunch of other divergences.
One that I mentioned and that I think is particularly interesting is the maximum mean discrepancy.

1:43:49 And so here's the difference between KL and maximum dean discrepancy, at least, I guess, an important conceptual difference.
So the KL, when you look at distributions that are very close to each other, it's basically going to become symmetric when the distributions are very close, and it's going to measure the amount of information that differs between them.
The maximum mean discrepancy, when you take two distributions that are very close, it reduces to what people call the Earth movers distance, also called like the vanishing distance so here's an intuition.
If you take two distributions that are very close, just imagine distribution A as a pack of dirt and distribution B as a pack of dirt or a sand with some shape.
The maximum mean discrepancy is going to tell you the amount of work that you need to put all that dirt from distribution A and pile it in the shape of distribution B.

1:45:01 So of course, there's so many different ways in which you could take all that dirt from distribution A and remodel it in distribution B, but you're interested in the minimal energetic cost that would take.
So like the optimal way of doing that movement, people call that optimal transport.
Now, if you're familiar with optimal transport, you know that the Vaster Stein distance is a distance between probability distribution that regardless of how far they are, is going to measure, is going to give you this cost of optimal transfer.
So the energetic cost of moving all that pack of dirt from place A to place B in the optimal way.
So the vaster shine distance is something that we could use here.

1:46:02 But maximum mean discrepancy, it has a lot of very nice properties and basically reduced it to the Vaster Stein distance.
When we consider very close distributions, this is not something that just a mathematical curiosity, but it's done that when one builds a distance out of a divergence, what one does is one takes very close distributions, measures the divergence between them, at which point the divergence is pretty much symmetrical.
And then you basically keep adding divergences along the trajectory until you get to the final one.
And this way, by aggregating divergences between very close distributions and doing that and adding that along a trajectory, you get a distance, a meaningful distance between distributions that could be very far.
If you do that with the Kale divergence, you get what's called the fisher information distance, which measures really the amount of information that took you from to go from one distribution to another distribution, regardless of how far they are.

1:47:15 If you do that with the vast search time distance, you will get the optimal transport cost.
So the amount of energy that you need to put all that dirt, place A to place B in the optimal way.
If you do that with the maximum discrepancy, you would also get that you will also get the optimal transport thing.

1:47:38 I just want to say that the maximum discrepancy discrepancy between two distributions that are far away will not coincide with the Vaster Stein distance, which gives you this optimal transport cost.
But when you actually derive a distance from these divergences, the distance derived from the maximum discrepancy and the Vaster Stein distance will end up being the same and the distance that you actually get or the topology that is derived from the distance.
So by topology, a topology is really a notion of closeness.
And so to understand closeness, you need to understand infinitesimal distances.
So the infinitesimal distances derived from Vaster Stein or Mmd, they're the same.

1:48:28 The topology that results is the topology of what people call weak convergence, which is a standard topology that's considered in probability theory.

1:48:40 So Mmd and Vaster Stein, they are very natural in that sense, in the sense that people say that they met rise, weak conversions, like they give rise to the standard topology between probability distributions.
So coming back to the choice of divergences, if you're interested in approximating distributions in the sense of approximating their information content, then KL is very natural.
But if you were for some reason and maybe would not be in this kind of application, but another kind of application, if for some reason you're interested in approximating distributions for the sake of how close they are when you look at them, then you wouldn't use Mmd or Vassagetein.

1:49:36 _Daniel:_

Wow, great information.
And I'm just thinking about we're switching lanes on the highway we're trying to get from here to there.
Yes, we want to know about the informational closeness of this tale of two densities, but we also want to know about the transport closeness because we have a schedule and a budget and decisions to make, and there are trade offs.
So being able to move the Earth optimally while we're switching lanes and accelerating and slowing down, I know this is mixing many angles informally.
We want to have a lot of options for how to think about that challenge of moving dirt between the tail of two densities and make sure everybody is driving in the right lane at the right time.

1:50:33 _Lance:_

Definitely, yeah, it's a design choice and it's an important one because it depends on what kind of properties we want to preserve.

1:50:43 All these divergences, some are not so useful, I guess, but some of them, they're just very natural and vasterstein and Mmd, they're very natural in that sense.
Very important to keep in mind.
And not only active inference lab, but just in general for any kind of inference problem.

1:51:09 _Daniel:_

Well, let us each have a closing round or reflections, any thoughts or any next steps or any suggestions or other information you'd like to provide.

1:51:24 _Lance:_

It's hard to say.
I feel we've covered so much already.

1:51:31 I think to me, what's most exciting about is scaling active inference right now, because you get this active inference algorithm in the paper that's the right compares principles and just from the derivation, you see.
Okay, well, there's actually so many things I dean, the assumptions are so small that there are so many things that you can model with this active inference algorithm.

1:51:59 And all the heavy lifting is done by the generative model.
So if you use one generative model, you will get one behavior.
If you use another generative model, you will get another behavior, but all the equations will remain the same.

1:52:14 It speaks to the generality.
Now in having something that's very general, you.
Get something that's also very non specific.
And I guess for neuroscientists and people who are interested in intelligence, generality comes at a cost of being non specific and non specific about the brain in general.
So really the big question to me long term is what kind of generative models do we need to simulate brain like behavior?

1:52:46 Because this is really the interesting behavior or the most interesting behavior.
So it speaks to a big research program that a lot of people are carrying and have been carrying for a long time.
But it's about what kind of representations do we have of the world?
What kind of priors do we have?
Can we identify the priors that we are born with?

1:53:13 There's a lot of research on computational or just playing cognitive science, like normal cognitive science, just studying babies and seeing what kind of priors, what kind of basic information they have when they come out of the womb.
There's a lot of things that they can already do there.
Our genetic code is preconditioning us to operate efficiently in this world and be able to flexibly adapt to any kind of situations that might arise in the natural world.
And so it's a huge research program to understand and model these priors.

1:53:51 And not only the priors, but also the likelihood, all the representation, all the state spaces.
So I think that's the way forward.
The creation principle is very elegant because it gives you a very succinct description in terms of a giant model that enables you to simulate pretty much everything.
But we're not interested in simulating anything.
We're interested in simulating brain like behavior.

1:54:15 And now we need to drill down even more onto the kind of Janitor models that would be amenable to that.

1:54:27 _Daniel:_

Great.
My closing reflection I feel like I know less about fep, but more about something else.
For what we've discussed.
Earth was moved, Bayesian mechanics were called in, decisions were made, and it's been a really great series.
So I'm appreciative and thankful that you suggested this paper in our correspondence as one to discuss.

1:55:03 You were absolutely right that it is relevant to bring to the attention of the active community.
And I hope that everybody who reads or listens thus far has shifted lanes so they can be where they want to be too.

1:55:25 _Lance:_

Well, yeah.
Thank you so much.
I also really enjoyed the session and think we had a really cool discussion.

1:55:34 So thanks again.
I hope to do this again soon.

1:55:38 _Daniel:_

Excellent.
Anytime you'd like.
Very well.

1:55:42 See you, Lance.
