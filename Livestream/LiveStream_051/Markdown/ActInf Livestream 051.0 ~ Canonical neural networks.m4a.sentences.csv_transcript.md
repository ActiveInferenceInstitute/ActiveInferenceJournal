# Livestream #051.0
## 10/26/2022
## https://youtu.be/ZASG-rtkXDk
### Speakers:
Daniel Friedman

00:28 _Friedman:_

Intro.
All right, welcome.
It is.
ActInf lab Livestream number 51.0.
This is the background and context first discussion for canonical neural networks.

00:41 Perform active inference by isomerate et al.
It's October 26 2,022.
Welcome to the active inference institute.
We're a participatory online institute that is communicating, learning and practicing applied active coherence.
You can find us at some of the links on the page.

01:00 This is a recorded and an archived Livestream, so please provide us with feedback so we can improve our work.
All backgrounds and perspectives are welcome and we'll be following video etiquette for Solo live Streams head active coherence Jorge to learn how to get involved active Coherence Institute projects today.
It's the first of several discussions that we'll have on the paper.
Canonical neural networks perform active inference 2,022 by Takuya IsomerA, Hideaki Shimazaki and Karl Friston.
The video is just an introduction to some of the ideas.

01:41 It's not a review or a final word.
There will be an overview of the structure of the paper and then we'll go through many of the key points.
Also just to disclaim, there's many, many other and better resources to learn about neural networks.
So I would very much welcome those with a technical understanding of neural networks and or some of the more applied computational or otherwise aspects of neural networks.
It would be awesome to have them on for the dot one and the dot two, because it was not an area I was familiar with and so hope that I can hear more from the authors in our coming weeks and others.

02:26 I'm Daniel, I'm a researcher in California, and this will just be a solo dot zero, which I guess hasn't happened in a while in the making of this.
Here are some of the generative art prompts area 51 active Inference area 51 neural Network area 50 active coherence Lab ant area 51 active inference neural network just some interesting images coming out of stable diffusion.
So as to some big questions that the paper is addressing and that one might be interested in to come to the paper.
How can artificial neural networks be understood as generic optimization processes and what is the correspondence between neural dynamics and Modern statistical inference methods?
Other big questions are about the history and next steps of the enmeshment of natural intelligence, Egyptian neuroscience and artificial intelligence, as well as of course, whether to even play into this kind of distinction at all and have different integrated intelligence frameworks.

03:34 And one paper where any of the authors or anyone who has kind of resonated with this work is recent by Zador at all 2,022 towards the next generative artificial Intelligence catalyzing the neuro AI revolution.
And so this is a bunch of authors.
And so it's interesting just to quote in terms of what some areas of discourse are saying right now, which is neuroscience has long been an important driver of progress in artificial intelligence AI.
We propose that to accelerate progress in AI.
We must invest in fundamental research in neuro AI.

04:09 So that's one way to read some of the developments that are happening in the paper.
We'll discuss what does it mean to be particular but generic?
That's a phrase used in the paper, so maybe that's kind of a jumping off point.
And then how can active inference help us understand the past, present and future here of the interface with neural networks, statistics and neural AI?

04:39 Here's the abstract.
This work considers a class of canonical neural networks comprising rate coding models wherein neural activity and plasticity minimize a common cost function and plasticity is modulated with a certain delay.
We show that such neural networks implicitly perform active coherence and learning to minimize the risk associated with culture outcomes.
Mathematical analyses demonstrate that this biological optimization can be cast as maximization of model evidence or equivalently minimization of variational free energy under the well known form of a partially observed Markov decision process model.
This equivalence indicates that the delayed modulation of heavy and plasticity accompanied with adaptation of firing thresholds is the sufficient neuronal substrate to attain Bayesian optimal inference and control.

05:31 We corroborated this proposition using numerical analyses of May's tasks.
This theory offers a universal characterization of canonical neural networks in terms of Bayesian belief updating and provides insight into the neuronal mechanisms underlying planning and adaptive behavior control.

05:53 Here is the roadmap I'll be driving.
On the right side of the road, there's an introduction and a table with a glossary of different expressions used.
Then there's the Results sections, which has first an overview of equivalence between neural networks and variational Bayesian active inference formulated using a postdiction of past decisions.
Canonical neural networks perform active inference and numerical simulations.
So they work on the interface between neural networks and variational Bayesian methods and start with a more theoretical and mathematical background and then eventually present some maize simulations that are in MATLAB.

06:41 Then there's a discussion, and then the methods section is following the discussion, and it has the subsections generative model variational free energy inference and learning, neural networks, simulations and data analysis.
And I think that I have kept to the right color codes consistently from here on forward.
The black quotes are the direct quotes from the paper, Bleu quotes are related to perception, orange for action, complete class theorems, and neural networks together in purple.
And then red is commentary and then the highlighting for red is related to the variational methods, but it's kind of red ish okay.
The papers canonical neural networks perform active inference by the authors listed previously.

07:36 It's in Communications biology from 2,022.
And the key aims of the paper are laid out well in the first paragraph.
So that's in black and other colors.
And here the red is just kind of getting into initial conversation with the paper and connecting a little bit more to some previous streams before we go more into the specifics of the paper.
The sentient behavior of biological organisms is characterized by optimization.

08:07 Biological organisms recognize the state of their environment by optimizing internal representations of the external environmental dynamics generating sensory inputs.
So that's the sensory recognition model.
In addition, they optimize their behavior for adaptation to the environment, thereby increasing their probability of survival and reproduction.
So that is bringing the entire active and inactive control theory, formal theories of action, action selections, planning and planning, its inference.
All of these action oriented pragmatic turn type ideas come into play when this action orange aspect is brought in and it is, must be, should be, et cetera, oriented towards survival and persistence.

08:57 Otherwise we don't see that kind of thing for log over appropriate definitions for thing and log, et cetera.
And this few sentences that the paper begins with summarizes a common theme in ActInf, which is that there's basically two pathways towards proficiency in the niche.
There's changing the mind, which is the perceptual and learning and then there's changing the world through action.
And that kind of integration of inference, cognitive inference, whether it's perceptual or learning or other and action as enacted is part of the active formulasm and shared with other areas.
This biological self organization is typically formulated as the minimization of cost functions wherein a gradient descent on a cost function furnishes neurodynamics and synaptic plasticity.

09:49 So they are working with a framework where the way that this perception action flow is trackable computationally either just for our current computers so that we can implement simulations and data fitting or whether more fundamentally like this is the computational context of action.
They're suggesting there's a way to think of it in terms of a cost function minimization and also note like inclination maximization.
In a way they're interchangeable because there's just sometimes negative signs that can flip them.
So it's the same energy and fitness landscape that is being navigated whether you're minimizing to the bottom of the bowl and thinking of action prediction that way and inference or whether you're climbing to the top of the hill.
Gradient descent, gradient ascent they're both kind of two sides of the same coin.

10:45 Two fundamental issues remain to be established.
Namely so this is what the papers saying they're filling the gap in literature the characterization of the dynamics of an arbitrary neural network as a generic optimization process and the correspondence between such neural dynamics and statistical inference found in applied mathematics and machine learning.
The present work addresses these issues by demonstrating that a class of canonical neural networks of rate coding models is functioning as and thus universally characterized in terms of variational Bayesian inference under a particular but generic form of generative model.

11:25 This is maybe the only slide that has resources from too far afield from paper.
Well, almost a few more.
It's just on neural networks.
The search on a very common search tool resulted in five plus million results for what are neural networks?
And the first one was 3 Bleu, one brown from 2,017, which is just a nice YouTube video as they very often make with these beautiful renditions.

11:58 And it's a very great video and there's many, many others.
A neural network is a network or circuit of biological neurons and that is variously purely computational and or biological map territory stuff.
And they can be thought of as nodes and edges, which are the firing rates and the connections between the biological neurons being modeled as weights between nodes.
A positive weight reflects an excitatory connection, while negative values mean inhibitory connections.
And here is data coming in and ending up activating different neurons in this final layer.

12:40 So this is kind of doing inference in a neural network and then there's an action part.
Okay, the paper says variational Bayesian inference offers a unified explanation for inference learning, prediction, decision making and the evolution of biological form, which can be considered over multiple timescales.
So this returns to the earlier theme of like perception, action and persistence within it among generations.
And the citations that are provided here for this are Friston Kilner Harrison 2,006 and Friston 2,010, both very classic active FEP papers.
Just to show one figure from each here's from the first citation with the winged snowflake, where if the snowflake ends up being somewhere that's too warm, that's not able for it to maintain the structure, then it melts, melts into a dew, et cetera.

13:46 And it must be ActInf lab if in one way or another it's staying above that phased boundary.
That's how it's statistically identified, it's how it's autogenetically identified, functionally identified.
And then here is one of the kind of pathetic figures in the Friston 2,010 paper with a tree of many different areas to connect to, informalisms to represent as, including probabilistic, neural coding, Bayesian brain, optimal control and value learning.
These three and others can be really seen ant play in this 2,022 paper.

14:41 The kind of inference variational basic methods use rests upon a generative model that expresses a hypothesis about the generation of sensory input.
Perception and behavior can then be read as optimizing the evidence for a generative model inherent in sensory exchanges for the environment.
And that's the integration of perception and action within a single imperative in terms of if only computation.
And that is described more on this slide, which one can pause and read, but the rest of the quotes are from the paper.

15:20 One key formalism that I had no familiarity with before this paper and associated readings and conversations with align was the Complete Class Theorem.
So it would be great for anyone who is familiar with Complete Class Theorem to help a little bit here.
But here's some interesting things that I came across crucially from the picture as a corollary of the Complete Class Theorem citations 19 through 21.
Any neural network minimizing a cost function can be viewed as performing variational Bayesian inference under some prior beliefs.
Here are the citations 19 through 21, from 19 47 19 81 2,013, and also found some interesting resources.

16:15 So quoting from this less wrong post linked here, Dutch book defines belief as willingness to bet and Money Pump defines preference as willingness to pay.
This is in terms of the foundational arguments for a Bayesian Epistemological worldview.
Hope that's correct.
Again, it'd be good to hear from anyone who knows more here, but in terms of different ways that one can consider the Bayesian proposition, which perhaps these are even better to use than referencing any person's last name.
Because the interesting thing will be the different lenses that these different framings on Bayesian Probabilities are interpreted as.

17:07 Just like what a Pvalue is interpreted as in the frequentist world.
Kind of analogously like a Bayesian factor interpretation.
So Dutch book defines belief as willingness to bet and Money Pump defines preference as willingness to pay.
In doing so, both arguments put the justification of decision theory into hypothetical exploitation scenarios which are not quite the same as the actual decisions we face.
If these were the best justifications for consequentialism we could muster, I would be somewhat dissatisfied, but would likely leave it alone.

17:40 Fortunately, a better alternative exists.
The complete Class theorem.

17:46 So here's an image from that post possible world states conversation likelihood maps to the possible observations hashtag a matrix then decision making rule may be probabilistic action selection as inference a possible actions affordances.
And here we commonly see the loop being closed from actions to world states like through the B matrix changing how the world changes through time.
And here these are both going to be mapped to a loss function l a real valued score from taking an Anthony G.
Chen the world turned out to be theta realized theta.
So that's quite an interesting framing.

18:37 And there were some other useful posts online.
And from this Zhat blog the argument boils down to if you agree with expected utility as your objective, then you have to be Bayesian.
In a nutshell, a strategy is inadmissible if there exists another strategy that is as good in all situations and strictly better in at least one.
If you want your strategy to be admissible, it should be equivalent to a Bayes estimator Complete Class Theorems.
Only Bay's strategies are Admissible.

19:12 And Admissible strategies are Bayes.
So there's probably a lot of interpretations of this, but it seems kind of related to optimal control or Bay's optimal inference, perhaps a little bit more keenly.
So these are some next two slides were contributed by Ali.
So if you or if anyone familiar in this area wants to come on and the discussion would be great, but Ali pointed me to this book.
Fundamentals of Bayesian Epistemology by title bomb 2,022 table of contents shown here and some challenges and objections to Bayesian Epistemology are listed which can be read.

19:58 And then also there's some quite interesting logical structures which can be read here in terms of their premise, theorem and conclusion in the areas of arguments for Bayesianism being representation theorem argument for probabilism, the Dutch book argument for probabilism, and the gradational accuracy argument for probabilism.
So pretty interesting.
Back to the paper they wrote we have previously introduced a reverse engineering approach that identifies a class of biologically plausible cost functions for neural networks.
Citation 22 Previous paper of Isomerra and Friston 20 20 the paper was reverse engineering neural networks to characterize their cost functions, the abstracts shown here.
But this letter considers a class of biologically plausible cost functions for neural networks using generative models based on partially observable Markov decision processes.

21:03 POMDP we show that neural activity and plasticity perform Bayesian inference and learning respectively by maximizing model evidence.
So this is a precursor paper from 2,020 that is cited and foundational for the 2,022 paper.
Here are some figures from that paper.
They have a comparisons among a Markov decision process scheme and a neural network.
For example, a Markov decision process scheme expressed as a fourney factor graph based on the formulation in Friston.

21:42 So here is the Markov decision process as a fourni factor graph and on the right side is the neural network with the hidden states, sensory inputs and neural activity, and some figures and concordances.

22:06 And they wrote in this context, the neural network can in principle be used as a dynamic causal model to estimate threshold, constants and implicit priors.
This reverse engineering speaks to estimating the priors used by real neuronal systems under ideal Bayesian assumptions, sometimes referred to as metabasian inference.
So they're laying out their research agenda and much of the work is going to reference this earlier paper and other work.
And then there's also some new integrations and especially the maze simulation in this paper and probably more so let's find out.
Referring to the earlier paper, this foundational work identified a class of cost functions for single layer feedforward neural networks of rate coding models with a sigmoid or logistic activation function.

23:04 We subsequently demonstrated that mathematical equivalents between the class of cost functions for such neural networks and variational free energy under a particular form of degenerative model, which is similar broadly to what the 22 paper dot.
Two, this equivalence licenses variational Bayesian inference as a fundamental optimization process that underlies both the dynamics and function of such neural networks.

23:30 However, it remains to be established whether the active inference is an apt explanation for any given neural network that actively exchanges with its environment.
In this paper, we address this active or control aspect to complete the formal equivalents of neural network optimization and the free energy principle.
So this earlier work was not including action.
And so this paper's key addition, as I understand it hopefully, is that they bring action more formally into the model and it'd be interesting to know what else is that change associated with, or what else happens or doesn't.

24:23 Here's some more text about the approach that they're going to take, and many of these details are going to be addressed later on here's table One glossary of expressions.
So these will also be broadly addressed later on.

24:51 Maybe it's useful though just to read the first one a canonical neural network in this work, the canonical neural network is defined by differential equations of neural activity derived as a reduction of realistic neuron models through some approximations which give a network of rate encoding neurons with a sigmoid activation function.
In particular, we consider networks comprising a middle layer that involves recurrent connections and the output layer that provides feedback responses to the environment.
So some category of neural network architectures or anatomies physiologies whatever with sensory, cognitive and action like features in an environment or a generative process.
So the results section, they write an overview of equivalence between neural networks and variational base.

25:51 First, we summarize the formal correspondence between neural networks and variational base.

25:56 A biological agent is formulated here as an autonomous system comprising a network of rate coding neurons.
Figure One a so here's a small figure one A we'll see it larger based upon the assumptions which will be brought up later on in a different fuller form.
The update rule for the ith component of Phi, which is the internal states so the cognitive studies and the output layer y.
So middle layer x and output layer y, these can be seen as the cognitive and the action generative aspects which are the autonomous states in contrast to the particular states of the active coherence entity which is the whole blanket, and the cognitive states so including the sensory states.
But the sensory states can't be directly controlled, however action can influence them.

26:53 And so that's what closes the causal loop and that set of the particular states comprising the autonomous states.
The update rule for the ith component of Phi is derived as the gradient descent on the cost function.
So the change in that Phi sub I is proportional to a generative on the loss function.
This determines the dynamics of neural networks including their activity and plasticity.
So l common loss function o observations sensory states by internal states comprising the middle and output layer neural activity.

27:34 That's the rate coding part and synaptic strengths w the parameterisation and other free parameters, including that that characterize L.
Then there's the output layer activity.
Y is determining the network's actions or decisions.
Delta O x and Y.
Y is the outputting action environment.

27:56 Generative process hidden state, passing observations to the sensory, cognitive active layers of the neural network.
And that is analogous topologically to the variational Bayesian formulation in Figure One.
B.
So left side gradient descent on a neural network cost function L determines the dynamics of neural activity and plasticity.
Thus L is sufficient to characterize the neural network and then being shown next to on the right side variational free energy minimization allows an agent to self organize to encode the hidden states of the external milieu and to make decisions minimizing future risk.

28:41 Here, variational free energy F is sufficient to characterize the inferences and behavior of the agent.
So sentence structure parallelism, and these two schemes or approaches being linked and applied is a focus of this area.

29:05 So neural networks are minimizing the cost function L.
In contrast, variational Bayesian inference depicts a process of updating the prior distribution of external states P of theta to the corresponding posterior distribution q of theta based upon a sequence of observations.
And we see other familiar terms from discussions on variational bays like minimization of surprise.
And there's some more model details shown here.
A few points are about choosing the family of distributions that one is doing variational inference with, and that allows for the gradient update rules in that family of distinctions to be made simpler.

29:54 For example, choosing a linear regression with an L two norm.
At the very least, you can say that it has a simple decision rule for being fit.
I'm sure there's like also counterarguments and other algorithms that are better and so on, but just to say that a simple decision rule in a known family of distributions can often be good enough as an approximation, if not more crucially.
According to the Complete Class theorem from earlier, a dynamical system that minimizes its cost function can be viewed as performing Bayesian inference under some generative model and prior beliefs.
The Complete Class theorem goes on to describe it ensures the presence of a generative model that formally corresponds to the above defined neural network characterized by L.

30:46 Hence, this speaks to the equivalence between the class of neural network cost functions and variational free energy under such a generative model.
Equation one loss function on the time series of observations comma parameters three lines is defined as f the free energy function on the same o through time comma parameterisation.
So there's a parallel being shown slashdefined wherein the internal states of a network by encode or parameterize the post tier expectation theta.
This mathematical equivalence means that an arbitrary neural network in the class under consideration is implicitly performing active inference through variational free energy minimization and more is written.
But this is one of many statements that will be made corresponding to correspondences between neural network loss function, generative models, active free energy minimization, and associated formalisms.

32:02 Note that being able to characterize the neural network in terms of maximizing model evidence lends it in explainability in the sense that internal neural network states and parameters encode Bayesian beliefs or expectations about the causes of observations.
In other words, the generative models explains how outcomes were generated.
However, the Complete Class theorem does not specify the form of a generative model for any given neural network.
To address this issue in the remainder of the paper, we formulate active inference using a particular form of partially observable Markov decision processes POMDP models whose states take binary values.
So this is one of several simplifications is one way to see it or areas for later generalization.

32:52 Figure Two in this section we define a generative model and ensuing variational free energy that corresponds to a class of canonical neural networks that will be considered in the subsequent section.
The external milw is expressed as a discrete state space in the form of a POMDP figure two.
So to make figure two larger, there's a lot to probably say about this figure.
I'll just note that the caption is informative and some of the highlighted lines.
It'll be awesome to have the author and other people who is familiar with some of the differences and symmetries between the, for example, bottom and top, above and below the observations, and also about the role of time and what these two risks are.

33:56 What is fictive causality?

34:00 Here's more details on that POMDP then equation two.
This is in this section active inference formulated using a postdiction of past decisions.
So if it was a prediction of future decisions, it's the opposite, a postdiction of past decisions.
Hence we define the generative model as follows PO delta s gamma theta, which is the model of observations decisions, observations decisions, hidden states risk and theta.

34:39 Theta equals A, b and C constitutes the set of parameters and more details are provided.
This is the familiar notation with some slight differences that will be described.
And equation two reflects the factorizability and the dimensions and the kind of computational tractability expression.
So that would be interesting to also learn about.
Under what conditions can this joint distribution be factorized?

35:21 Under what simplifications or constructions the agent is making decisions to minimize a risk function capital gamma that's on the bottom of figure two, active causality leading to this gamma coming from that gamma, equation three is shown.
And to characterize the optimal decisions as minimizing expected risk in our POMDP model, we use effective mapping from the current risk gamma to past decisions that's that retrodictive active causality, although this is not the true causality in the real generative process that generates sensory data.
Here we intend to model the manner that an agent subjectively evaluates its previous decisions after experiencing their consequences.
This victim causality is expressed in the form of a categorical distribution, so it could be other families hypothetically.

36:22 But this equation three is describing victim causality and this interesting sign indicates the elementwise division operator.

36:34 Also note throughout the manuscript, the overly variable indicates one minus that variable, so gamma bar equals one minus gamma.
Or it can be understood as the complement of a statistical probability probability of a happening and the probability of not a happening in that one way.

36:56 Importantly, the agent needs to keep selecting good decisions while avoiding bad decisions.
To this end, equation three supposes that the agent learns from the failure of decisions by assuming that the bad decisions were sampled from the opposite of the optimal policy, mapping some more details and then by convention, active inference uses C to denote the prior preference.
That's how we've seen the C variable in many models as preferences.
Prior Preference this work uses C to denote a mapping to determine a decision depending on the previous state.
Herein the prior preference is implicit in the risk function.

37:42 Due to construction, C does not explicitly appear in the inference.
Thus it is omitted in the following formulations so that's a key point about the notation of the variable C and something kind of maybe interesting to explore.
Equation Four variational Bayesian inference refers to the process that optimizes the posterior belief q of theta based on the gain field approximation.
Q of theta is expressed as and here is the factorization representation of the q of theta variational and another notation.
Note throughout the manuscript, bold case variables such as bold s subtau denote the posterior expectations of the corresponding italic case random variables and some more details about the model.

38:40 For example, for simplicity, here we suppose that state indecision priors d and e are fixed, so one could imagine they don't have to be, but for simplicity they will be.
Here, under the above defined generative model and posterior beliefs, the ensuing variational free energy is analytically expressed as follows equation Five this is a variational free energy F and recall equation one that it is being connected to juxtaposed with, et cetera.
The loss function.
The gradient descent on variational free energy updates the post tier beliefs about hidden states s decisions, delta and parameters data.
The optimal post tier beliefs that minimize variational free energy are obtained as the fixed point of the implicit gradient descent, which ensures that change in F with respect to the change in hidden states through time equals zero.

39:46 And some more definitions.
All of them are zero.
That 1 might be an O, but they're all zero.
And this is saying the ball rolls to the bottom of the hill in this gradient descent, and when the rate of change is zero, then that is a fixed point, a tractorlike dynamic, and that can be used as a way to incrementally fit statistical models like the loss function is used to incrementally fit neural networks.
To explicitly demonstrate the formal correspondence with the cost function for neural networks, consider in the next section we further transform the variational free energy as follows some Details Using these relationships, equation five is transformed into the form shown in Figure three.

40:38 See the Methods section variational Free Energy for further details.
In what follows, we demonstrate that the internal states of canonical neural networks encode posterior beliefs.
Here's figure three on the top from the caption figure three is the mathematical equivalence between variational free energy and neural network cost functions depicted by one to 1 correspondence of their components.
Top variational free energy transformed from equation five using the Bayes theorem and foreshadowing equation seven.
Using this relationship, equation seven is transformed into the form presented at the bottom of the figure.

41:20 So here's f variational free energy and L the neural network cost function and different elements as they're represented here with some resonances and concordance and beyond which we can explore, they're being shown to be equivalent.
And it was in the conversation preparing for this dot zero with Dean, where we saw this as some chromosomes.

41:58 In this section, canonical neural networks perform active Coherence in this section, we identified the neuronal substrates that correspond to components of the active imprint scheme defined above.
We consider a class of two layer neural networks with recurrent connections in the middle layer.
Figure one a those are those connections with loops recurrent in the middle layer.
The modeling of the networks in this section, referred to as canonical neural networks, is based on the following three assumptions that reflect physiological knowledge.
One gradient descent on a Costa function l determines the updates of neural activity and synaptic weights.

42:34 Method Section neural Networks Neural Two Assumption 2 neural activity is updated by the weighted sum of inputs and its fixed point is expressed in a form of the sigmoid or logistic function.
And assumption three a modulatory factor mediates synaptic plasticity in a post hoc manner.

42:55 They write based upon assumption two, which is neural activity is updated by the weighted sum of inputs and its fixed point is expressed in the form of a sigmoid or logistic function.
Based on assumption two, we formulate neural activity in the middle layer and output layer the autonomous states as follows.
Equation six without loss of generality.

43:25 Equation six can be cast as the gradient descent on cost function l such.
A cost function can be identified by simply integrating the right hand side of equation six with respect to x and y.
Consistent with previous treatments.
Citations because neural activity and synaptic plasticity minimize the same cost function l, the derivatives of L must generate the modulated synaptic plasticity under these constraints, reflecting assumptions one through 3, a class of cost functions is identified as follows equation Seven loss function awesome to hear somebody read this directly.

44:10 So there's a firing rate aspect that's related to neural firing in the short term more perceptual aspect of function.
And there's a slower neurotransmitter neuroglial factor mediated learning over perhaps a different time scale and with some different features.
And they're being included as a joint model of inference.
And here that is being connected to doing inference on action.
Synaptic Plasticity and Neural Networks so, synaptic plasticity rules conjugate to the above rate coding model can now be expressed as a gradient descent on the same cost function l according to assumption one.

44:56 Equations 8 and nine showing that neural networks can integrate those modes of firing rate like and synaptomdulatory like.
Neural networks.
Cost Functions and Variational Free Energy Based on the above considerations, we now establish the formal correspondence between the neural network cost function and variational free energy.
Under the aforementioned three minimal assumptions.
We identify the neural network cost function as equation seven.

45:31 Equation 7 can be transformed into the form shown in figure three bottomed, using sigmoid functions of synaptic strengths.
So equation seven loss function transformed into the form shown in figure three bottom.

46:03 Hence, this class of Costa functions for canonical neural networks is formally homologous to variational free energy under the particular form of the POMDP generative model defined in the previous section.
We obtain this result based on analytic derivations without reference to the complete class theorem, thereby confirming the proposition of equation one loss function and free energy.
This in turn suggests that any canonical neural network in this class is implicitly performing active inference.
Table two summarizes the correspondence between the quantities of the neural network and their homologs in variational bays.
So two, a great concordance table.

46:51 On the left side, neural network formation.
On the right side, variational bays formulation.
So just like in figure three, we had the two long lines.
Then table two, we have rotated 90 degrees and the variables for different parts of these models are laid next to each other.

47:28 So what papers of neural networks can we make active models for?
Is it already done or is there just one script that needs to be done?
And then conversely, what interesting, variational Bayesian models have interesting applications or some other value or information gain from being cast as neural networks or integrating neural networks into what had previously been only analytical variational Bayesian models as well as the empirical data fitting aspect which is related that's highlighted by the authors.
So in summary, when a neural network minimizes the cost function with respect to its activity and plasticity, the network self organizes to furnish responses that minimize the risk implicit in the cost function.

48:28 This biological optimization is identical to variational free energy minimization under a particular form of the POMDP model.

48:36 Hence, this equivalence indicates that minimizing the expected risk through variational free energy minimization is an inherent property of canonical neural networks featuring delayed modulation of Hebbian plasticity.
Okay, brief seconds to view some image memes and take a breath in a stretch.

49:09 On the left side, the top panel says every neural network is implicitly performing active inference question mark.
That's awesome.
In the middle image meme, one simply makes a neural network and it is implicitly performing active coherence.
Also question mark.
And then in the right image meme, there are two pieces of paper neural network and implicit performance of active inference.

49:36 Corporate needs you to find the differences between this picture and this picture.
And here is the paper.
They're the same picture.
So the previous sections have successfully extended the variational bays meets inference neural network result from the 2,020 paper with an action loop and a loss function only on the autonomous states.
So that was the conceptual and technical feature that this paper brought in.

50:22 Again, it'll be awesome to hear the author describe it more and differently.
And then in this part of the paper, they turn from that kind of analytical theoretical towards some numerical simulations in MATLAB.
Here we demonstrate the performance of canonical neural networks using may's tasks.
As an example of a delayed reward task, the agent comprised the aforementioned canonical neural networks figure four a thus it implication performs active inference by minimizing variational free energy.
So now some entity or agent is going to be constructed and numerically simulated to support some of the aspects of their model and point towards utility in other settings.

51:20 So here's figure four simulation of neural networks solving maize tasks in part A there is the architecture of the agent sensory input layer O of T synaptic weights into the middle layer x internal states and the output layer y decision action with risk gamma of T.

51:57 The sensation comes in a neural network then outputs a decision.
There's some task that the entity must perform which is to move towards the goal from the start across this lateral maze.
So one could imagine that if it were just a hallway with no maze features, simple strategies would be very overfit but effective like always move simply towards the goal.
Whereas in more complex settings, which this is an example of where there's uncertainty as well as many local optima.
So one has to sometimes take one or 2 or three or 4 or more steps or however many to get closer to the goal and sometimes may not know for example how long those backtracking situations are going to be and all these other complexities for which this may's example is symbolic of.

53:18 So maybe there's some interesting mythos maze connections and computational and here's some performance measures on the maze task with the neural network entity.
This way before training, the agent moved to a random direction in each step resulting in a failure to reach the goal position right end within the time limit.
During training, the neural network updated synaptic strengths depending on its neural activity and ensuring outcomes, ie.
Risk.
This training comprised a cycle of action and learning phases.

53:59 This treatment renders neural activity and adaptive behaviors of the agent highly explainable and manipulable in terms of the appropriate prior beliefs implicit in firing thresholds for a given task or environment.
In other words, these results suggest that firing thresholds are the neuronal substrates that encode state and decision priors as predicted.
Mathematically big if true.

54:24 Furthermore, when the updating of parameters is slow across these two now linked domain parameters of the variational Bayesian autonomous state inference and the neural network loss function parameters, when the updating of these parameters are slow in relation to the experimental observations, the parameters can be estimated through Bayesian inference based on empirically observed neuronal responses.
C Method section Data Analysis for details using this approach, we estimated implicit prior E, which is encoded by PSI from sequences of neural activity generated from the synthetic neural networks used in the simulations reported in figure four.
We confirmed that this estimator was a good approximation to the true e.
So that's also pretty interesting.
This is showing they don't just lay out this architecture and show that it's possible to fulfill this maze task with the best whatever.

55:37 It's not a classification accuracy generative alone.
They're describing that from empirically observed neuronal responses, which is to say the experimenter's observation the sequences of neural activity generated from the synthetic neural networks used in that figure numerically.
So statistically, that estimator was a good approximation to the true e.
Figure five a so here's figure five.
Estimation of implicit priors enables the prediction of subsequent learning.

56:21 So that's pretty interesting and will be great to hear what each of the axes are and what all the variables mean.

56:34 With this setup in place, they did some numerical validation and talked a little bit more about fitting data from this simulation model.

56:51 Here's the discussion action so the first paragraph of the discussion biological organisms formulate plans to minimize future risks.
In this work, we captured this characteristic in biologically plausible terms.
Under minimal assumptions, we derive simple differential equations that can be plausibly interpreted in terms of a neural network architecture that entails degrees of freedom with respect to certain free parameters, e.
G firing threshold.
These free parameters play the role of prior beliefs in variational Bayesian formulation.

57:25 Thus, the accuracies of inferences and decisions depend upon prior beliefs implicit in neural networks.
And here's some more stable diffusion ant neural network ant brain neural network so some more summarization of what they did based on the view of the brain as an agent that performs Bayesian coherence.
Neuronal implementations of Bayesian belief updating have been proposed which enables neural networks to store and recall spiking sequences eight learn temporal dynamics and causal hierarchy nine extract hidden causes 10 solve maize tasks 11 and make plans to control robots 12 so citations eight through 12 listed here.
In these approaches, the update rules are generally derived from Bayesian cost functions e.
G variational free energy.

58:23 However, the precise relationship between these update rules and the neural activity and plasticity of canonical neural networks has yet to be fully established.

58:37 We identified a one to 1 correspondence between neural network architecture and a specific POMDP implicit in that network.
Equation two speaks to a unique POMDP model consistent with the neural network architecture defined in equation six, where their correspondences are summarized in table two and the figures.
This means that our scheme can be used to identify the form of the POMDP given an observable circuit structure.
Moreover, the free parameters that parameterize equation six can be estimated using equation 24.
This means that the generative model and ensuring variational free energy can in principle be reconstructed from empirical data.

59:24 This offers a formal characterization of implicit Bayesian models entailed by neural circuits, thereby enabling a prediction of subsequent learning.
So what can be done with this?
What is this new?
What is new here?
Does this second selection fully establish the precise relationship between these update rules and the neural activity and plasticity of canonical neural networks.

1:00:03 Here is a discussion action on Hebbian plasticity, neurotransmitters and glia with a lot of citations listed.
And here was just one interesting follow on discussion from the computational aspects.
Neurocognitive and computational aspects of Hebbian plasticity is these modulations have been observed empirically with various neuromodulators and neurotransmitters such as Dopamine, Noradrenaline, muscarine, and GABA, as well as glial factors.
So here's a picture by Alexandra Mikhailova Cultured Astrostites release signaling and growth factors that regulate proper neuronal development so Cool, Glial, Pick, Dopamine, and reinforcement learning.
In particular, a delayed modulation of synaptic plasticity is well known with Dopamine neurons citations 35 through 37.

1:01:07 Those citations are listed here.
This speaks to a learning scheme that is conceptually distinct from standard reinforcement learning algorithms, such as the temporal difference learning with actorcritic models based on state action advantage function.
Please see the previous work citation 50 for a detailed competition between active inference and reinforcement learning that is, Sajid, Ball, Par and Friston active inference demystified and compared from 2,021 and that's also active model stream number 2.1.
We mathematically demonstrated that such plasticity enhances the association between the prepost mapping and the future value of the modulatory factor, where the latter is cast as a risk function.
This means that postsynaptic neurons self organized to react in a manner that minimizes future risk.

1:02:06 So the neural network had three layers it's the second and the third layer, not the initial sensory layer, but the second and the third layer, the cognitive and the active states, which are the autonomous states of the particular states.
So that's quite interesting the self organization of postsynaptic neurons to react in a manner that minimizes future risk.
Crucially, this computation corresponds formally to variational Bayesian inference under a particular form of pom DP generative models, suggesting that the delayed modulation of Hebbian plasticity is a realization of active inference and regionally specific projections of neuromodulators may allow each brain region to optimize activity to minimize risk and leverage a hierarchical generative models implication in cortical and subcortical hierarchies.

1:03:11 This is reminiscent of theories of neuromodulation and metallarning developed previously.
Citation 52 Doya 2,002 metallarning and Neuromodulation cool.

1:03:25 Our work may be potentially useful when casting these theories in terms of generative models and variational free energy minimization.

1:03:37 They then return the discussion to the complete Class theorem and neural networks.
So the Complete Class Theorem same citations from before ensures that any neural network whose activity and plasticity minimize the same cost function can be cast as performing Bayesian inference.
However, identifying the implicit generative model that underwrites any canonical neural network is a more delicate problem, because the theorem does not specify a form of the generative model for a given canonical neural network.
Which is pretty interesting.
Is that to say that the form of the generative model as modeled is different in what ways?

1:04:22 From the given canonical neural network, the posterior beliefs are largely shaped by prior beliefs, making it challenging to identify the generative model by simply observing systemic dynamics.
To this end, it is necessary to commit to a particular form of the generative model and elucidate how posterior beliefs are encoded or parameterisation by the neural network states.
This work addresses these issues by establishing a reverse engineering approach to identify a generative model implicit in a canonical neural network, thereby establishing one to 1 correspondences between their components.
Remarkably, a network of rate coding models with sigmoid activation function formally corresponds to a class of POMDP models, which provide an analytically tractable example of the present equivalence.
Please refer to the previous paper citation 22 for further discussion.

1:05:21 So some of the analytical details, especially on the inferential side cognitive side, were captured in the earlier paper.
This paper goes further into mapping the potentially necessary and sufficient aspects of the particular entity, which is to say the risk minimizing features of the autonomous states with respect to the entire particular states, including sensory states.
Connecting that back of the envelope verbally expressible formulation to some complete class of neural networks.
So what's outside of the complete class, and why?

1:06:24 And then what groups within the class have special or different features?

1:06:33 It is remarkable that the proposed equivalence can be leveraged to identify a generative model that an arbitrary neural network implicitly employs.
This contrast with naive neural network models that address only the dynamics of neural activity and plasticity.
If the generative model differs from the true generative process that generates the sensory input, inferences and decisions are biased I e.
Suboptimal relative to Bay's optimal inferences and decisions based upon the right sort of beliefs.
Prior Beliefs in general, the implicit priors may or may not be equal to the true priors.

1:07:11 Thus, a generic neural network is typically suboptimal.
Nevertheless, these implicit priors can be optimized by updating free parameters e.
G threshold factors, phi PSI based on the gradient descent on cost function l.
By updating the free parameters, the network will eventually, in principle become Bayes optimal for any given task.
In essence, when the cost function is minimized with respect to neural activity, synaptic strengths, and any other constants that characterize the cost function, the cost function becomes equivalent to variational free energy with the optimal prior beliefs.

1:08:00 So the cost function for the neural network activity and synaptic strengths underlying the loss function are equivalent to the kind of gradient descent enabled variational free energy minimization under the Bay's optimality scenario from a risk perspective.
Simultaneously, the expected risk is minimized because variational free energy is minimized only when the precision of the risk gamma is maximized.
See method section Generative Models for further details.
Very interesting.

1:08:53 They then say the class of neural networks we consider can be viewed as a class of reservoir networks.
Citation 54 citation 55 here, the proposed equivalents could render such reservoir networks explainable and may provide the optimal plasticity rules for these networks to minimize future risk by using the formal analogy to variational free energy minimization under the particular form of POMDP models.
A clear interpretation of reservoir networks remains an important open issue in computational neuroscience and machine learning.

1:09:38 So from Wikipedia reservoir computing is a framework for computation derived from recurrent neural network theory that maps input signals into higher dimension computational spaces through the dynamics of a fixed nonlinear system called a reservoir.
After the input signal is fed into the reservoir, which is treated as a black box, a simple readout mechanism is trained to read the state of the reservoir and map it to the desired output.
Then there are two key benefits of this approach.
The first key benefit of this framework is that training is performed only at the readout stage as the reservoir dynamics are fixed.
The second is that the computational power of naturally available systems, both classical and quantum mechanical, can be used to reduce the effective computational cost.

1:10:29 Here's some stable diffusion reservoir computing, active inference, neural network so this would be interesting to discuss.
And I remember some active institute participants who are specifically interested empirical analyses and hypotheses.
They write the equivalence between neural network dynamics and gradient flows on variational free energy is empirically testable using electrophysiological recordings or functional imaging of brain activity.
So then another summarization crucially the proposed equivalence guarantees that an arbitrary neural network that minimizes its cost function, possibly implemented in biological organisms or neuromorphic hardware, can be cast as performing variational Bayesian inference.
So to state it a few more times in the final paragraph, in summary, a class of biologically plausible cost functions for canonical neural networks can be cast as variational free energy.

1:11:45 Formal correspondences exist between priors posteriors and cost functions.
This means that canonical neural networks that optimize their cost functions implicitly perform active inference.
This approach enables identification of the implicit generative model and reconstruction of variational free energy that neural networks employ.
This means that in principle, neural activity, behavior and learning through plasticity can be predicted under Bayes optimality assumptions.

1:12:21 There's a code availability statement.
The MATLAB scripts are available at GitHub in the repo of the first author.
And it would be awesome for the author or anyone to bring this working MATLAB script up and see if we could do some realtime active inference.
Then, as mentioned earlier, from the roadmap the methods are following the discussion.
I'll just show the equations but not go into any details because there is not time nor familiarity.

1:13:08 So those who have more of one or the other would be welcome to fill in some dots because this is a really awesome and important paper.
So I hope that it can be interpreted and critiqued and elaborated on and so on by those with familiarity in both sides of that free energy loss function.

1:13:36 Equation one generative model section many details are provided.
Equation 10 is shown.
It's a larger unpacking of the generative models.
Section variational free energy many details are provided equation 11, 12, 13, 14 and 15 section inference and learning details are provided.
Equations 16, 17, 18.

1:14:08 Then section on neural networks so there's just some interesting writing here, so I wanted to highlight that.
In this section we elaborate the one to 1 correspondences between components of the canonical neural networks and variational bays via an analytically tractable model.
So that's the figure three that we've been returning to.
Neurons respond quickly to a continuum stimulus stream with a timescale faster than typical changes in sensory input.
For instance, a peak of spiking neurons in the visual cortex of V one appears within 50 and 80 milliseconds after a visual stimulation citation 62, 63, which is substantially faster than the temporal correlation timescale of natural image sequences about 500 milliseconds.

1:15:03 Citation 64 65.
So that's pretty interesting.
What is the temporal auto correlation timescale of natural sequences?

1:15:16 What time scale do neural firing and neuroplasticity et cetera processes actually occur at?
And when might some type of function at a given time scale be understood to be function or not?

1:15:41 Thus, in other words, downstream of the fact that neurons respond quickly at a time scale faster than typical changes in sensory input, we consider the case where the neural activity converges to a fixed point given a sensory stimulus.
We note that the present equivalence is derived from the differential equations equation six, but not from its fixed point.
Thus, the equivalence holds true irrespective of the time constant of neurons to rephrase neural networks with a large time constant formally correspond to Bayesian belief updating with a large time constant, which implies an insufficient coverage of the posterior beliefs.
Pretty interesting related to learning rates and Bayesian updating rates, and all of the nooks and crannies of Bayesian coherence and the challenges associated with dynamics, uncertain, rugged fitness and free energy landscapes.

1:16:56 These optimization challenges, which are addressed differently methodologically, culturally, et cetera.

1:17:05 In the variational Bayesian and in the neural cases, they have to deal with time.
And so all of those different nooks and crannies mentioned, like catastrophic learning, catastrophic forgetting, simply memory, anticipation, attention, local maxima, choosing when to play all these higher order questions are connected here.
Does that make it what kind of a problem space now or just what kind of space?
Pretty interesting and equation 19, 20, 21, 22, 23 they have some more details on the simulation.
Maybe we could see the simulation go and in the last section data analysis.

1:18:11 So this is kind of returning to that point about the time constants in Bayesian and neural network systems when the belief updating of implicit priors D and E is slow in correlation to experimental observations.
D and E, which are encoded by Phi and PSI, can be viewed as being fixed over a short period of time as an analogy to homeostatic plasticity over longer time scales.
66 Homeostatic plasticity in the developing nervous system 2,004 very interesting in light of our recent discussions on allostasis and other topics, Thus, fi and PSI can be statistically estimated by a conventional Bayesian inference or maximum likelihood estimation given a flat prior based on empirically observed neuronal responses.
In this case, the estimators of phi and PSI are obtained as follows nice equation number 24 mentioned earlier, so that will be definitely one to look into more.

1:19:27 Well, I hope you found this a useful and interesting dot zero.
I'm looking forward to the discussion with the author.
And again, any other institute participants or those with knowledge or strong feelings to express about neural networks, active inference, applied active inference, computational modeling of perception, cognition and action, neural networks in the wild, AI, ethics, all these different areas.
Can hopefully have a nice discussion in 51.1 and 0 2.
That'll be the last paper.

1:20:19 Streams for 2,022.
There will still be a few guest streams upcoming, so those discussions will close the paper focused, prepared Livestream number 2,022.
And yeah, if you want to be more involved with live streams whenever you're listening to this, join or recommend someone to join or help in any number of other ways.
Just listening and learning is awesome.
And we also really look forward to those who want to help make some of these connections that are agent and sometimes exposed in these papers and conversations, and with a few motivated people who want to connect, for example, to the neural network communities and those who can facilitate discussions on these topics, that would be awesome.

1:21:25 Just using my final thoughts on this zero, because it's always great to have others also join in the preparation for the dot zero.
So just want to add that note on this rare solo stream.
So thanks again, looking forward to talking or seeing you later.
Bye.
