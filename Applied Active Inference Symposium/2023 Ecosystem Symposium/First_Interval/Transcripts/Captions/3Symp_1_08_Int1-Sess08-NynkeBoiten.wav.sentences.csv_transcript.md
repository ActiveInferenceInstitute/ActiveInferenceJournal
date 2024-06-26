00:02 _Daniel Friedman:_
All right.
And on to the last session of the first interval.
Greetings, Nynke!
Greetings.

00:21 _Nynke Boiten:_
Hello.
Good morning.

00:23 _Daniel:_
Yes, good morning.
How goes it?

00:29 _Nynke:_
Yeah, I'm doing fine, thanks.

00:33 _Daniel:_
Would you like to present and then we'll discuss?

00:38 _Nynke:_
Yes, that sounds like a good idea.
Great.
Let's see.
Just going to share my screenplay.
Yes.
Can you see the presentation?

01:08 _Daniel:_
Not yet.

01:10 _Nynke:_
Okay.
See flex.

01:15 _Daniel:_
Yes.
Looks perfect.

01:17 _Nynke:_
Okay, great.
Yeah.
Should I just start?

01:23 _Daniel:_
Yeah, go for as long as you want, and then anyone can ask questions in the live chat, and I'll write down some things, too.
Thank you.

01:29 _Nynke:_
Okay, great.
Yeah.
So my presentation today will be on advances in machine theory of mind and theory of mind.
Sophistication I'm currently a student at the University of Amsterdam and finishing my master's thesis on this topic.
And I'll be giving a broad overview of current machine theory of mind and an idea or concept for an active inference approach based on previous work related to active inference theory of mind.
So to start okay, sorry.
So for a global overview, we'll start with giving a short basic definition of what theory of mind is and how it's been used.
Then I'll give you a global overview of current approaches to designing machine theory of mind, including evasion approaches, approaches using Biphysical models, et cetera.
Then I'll zoom into active inference models of theory of mind and social intelligence and collective intelligence more broadly.
And I'll get into the issue of theory of mind.
Sophistication, which is basically the depth of recursivity of beliefs that you can have about another person's mental states and their thoughts or beliefs or goals about you.
And then we'll get into the issue of how to implement recursive beliefs.
And as an example, we'll discuss Bayesian theory of mind with K levels of depth.
And then we'll get into the more specific paradigm that I'm using right now to build a theory of mind model, which is based on a very simple model of the matching panning paradigm.
So we'll talk a little bit about that, and then we'll get into the model itself and current ideas for implementing theory of mind sophistication using active inference.
So first of all, what is theory of mind?
Theory of mind has been introduced by the very famous paper by Primac and Woodcherf in 1978, I think it was called does the Chimpanzee Have a Theory of Mind?
And they define theory of mind as the ability to impute mental states to himself and others as a system of inferences.
And they say system of inferences of this kind is properly viewed as a theory, first, because such states are not directly observable, and second, because the system can be used to make predictions specifically about the behavior of other organisms.
And I think there's already a lot in this definition.
And a lot of authors looking at theory of mind right now still use the same view of theory of mind as a theory, a structured theory of different kinds of mental states such as goals, beliefs and desires that facilitate the prediction of observable behavior in other agents such as facial expressions, movement or speech.
And I find it very interesting how much this aligns with maybe a predictive processing view of social cognition, but also how weird it is that this theory, theory of theory of mind is still so widespread in the theory of mind literature, modeling literature.
So there's been some discussion on whether you can properly regard theory of mind as a theory and if so, what kind of theory it is.
So within the philosophy of mind, there's been basically two mainstreams or main perspectives on theory of mind.
According to the classic theory, theory of Tom, theory of mind is a causal theory of how these internal mental states generate other agents'behaviors.
So it's the same kind of view that we just saw.
And then the opposite side is called simulation theory of theory of mind, which posits that we use the same kind of cognitive and neurological resources for understanding and predicting other agents as those that we use for understanding the self.
And simulation theory can also take on different forms.
The sun is coming up next to them.
So that's why I'm based in light at the moment.
But basically there are lots of versions of this.
Some posit that we use the same kind of action prediction mechanisms for ourselves as for others.
And there is this new version of simulation theory that Gordon proposes in 2021 which very broadly says that we have the same kind of theory for other agents for ourselves.
So there's this general theory for what it means to be an agent that is refined at different stages to facilitate context sensitive predictions in social interactions.
So this is also interesting to look at when you model theory of mind, what you think theory of mind is and how it is specifically implemented.
So why would we be interested in creating computational models of theory of mind?
So I think there are three important reasons why this is very relevant at the moment.
First of all, there is a technical reason or the reason of technological advancement.
There's been some proposals that argue for the development of artificial social intelligence.
Oh wait, yes.
So the technical reason for developing computational models of theory of mind is to improve artificial social intelligence, especially as we start to live in a world in which research on human AI interaction becomes more relevant.
And that's been this paper Bob Williams, for example, that's argued that improving artificial social intelligence is needed for successful AI human cooperation and it could improve communication, trust and maybe also value alignment.
By utilizing theory of mind for value alignment.
For example, there is a very strong foundational reason to study social cognition generally and the evolution of social cognition through in silica hypothesis testing and clarifying the conceptual boundaries of theory of mind.
One great example for this is research by Devane ETL, which used a computational model of recursive theory of mind compared to alternative models to study different cognitive strategies in non human primates.
And they find no evidence for the hypothesis that theory of mind sophistication involved with an increase in herd size, but they do find a correlation with, for example, neocortex ratio.
So in this way, theory of mind models can give us some insight into the evolution of social cognition.
On the clinical side, theory of mind models can be used to understand relevant social variations in clinical populations, for example, through computational phenotyping and diagnostics and by studying social behavior in groups that have some difficulty with social interactions.
And groups that show some kind of variation in social cognition, such as people with autism spectrum, people in the autistic spectrum, people with ADHD or schizophrenia.
So I hope that with some of these reasons, I convinced you that modeling theory of mind is very relevant at the moment.
And there have been a lot of people already on this.
And I've created this very global overview of some approaches that are representative or some models that are representative of their more general approaches.
There's this brain Tom model which aims to basically build up clear mind abilities and abilities facilitating social interaction from the bottom up using Biphysical models of neural firings.
That's why I've placed it on the dynamic scale.
So I've tried to align these modeling approaches along the axes of how they treat time, how broad their description is from the individual level to maybe describing more broader social and cultural processes and along the level of description from the molecular biophysical to the behavioral.
And one thing you can see is that there is a lot of work based on invasion inference and active inference that moves along that has relevant ties to the molecular and neurobiological level but moves along the lines of making behavioral and cognitive predictions.
And there are very little models that really also formalize the concrete implementation of theory of mind.
And there is also, I think, this need for connecting this dynamic implementational level to individual level social cognition and putting that in the context of social interaction more generally.
So some of the representational approaches that I selected are the TOMNET, which basically uses neural network embeddings to train reinforcement learning agents.
We have Ktom, which is a Bayesian recursive model which I'll come back to later, some or theory of mind with self other modeling uses multiagent reinforcement learning with goal inference.
And we have the more theoretical active inference model of implicit cultural learning called thinking through other minds, which could be seen as an alternative or a redefinition of theory of mind.
Okay, so to sum up, we have this stream of biophysical models, most notably Brain Tom, which was developed by Zhao et al.
And its strengths are its neurobiological plausibility at making dynamic predictions about neural activation in populations that are associated with theory of mind abilities and its weaknesses is that it's quite computational and costly and it's probably difficult to implement in an interactional setting.
There are some deep learning models such as Tomnets by Rabinovitz and Self other modeling which I just mentioned that are also quite neurobiologically plausible and also make some dynamic predictions.
But there is this strong danger of shortcuts, which has been addressed in deep learning models, that the task might not be solved by learning the relevant ability of being able to infer another agent's goals or beliefs, but just by learning simple lower level associations between, for example, the perspective or how another agent stands and where, for example, a food reward would be.
So there are a lot of ways to solve the task and there's this finding that deep learning models sometimes use these kinds of shortcuts so that's something that's needed to be addressed.
Then there are some Bayesian belief based models such as K Tom for Recursive theory of Mind and Beijing Tom which was originally developed by Baker et al.
In 2011 and its strengths are that it's quite efficient, it's very easy to interpret and its weaknesses are that the road to the implementational level is longer and it requires many priors and there's this question about whether it's scalable because of the prior specifications that you have to give.
Okay, so as one of the I think the interesting newer developments on a theory of mind wait, yes.
Is Hierarchical active Inference for collaborative agents which has been recently published and Haika is based on the Asian theory of mine by Baker et al.
But it adds this formalization of belief resonance which is the incorporation of beliefs about another's intentions with top down predictions and this influence of these other agents beliefs are modulated by susceptibility parameter which controls this influence.
And what I find I think it's important to note here that they use an approach based on active inference but they don't use the free energy principle for example.
So they do couple perception and action but just in a different way using a karma filter.
So the way they formalize this is slightly different but I think the overall structure can still be informing or inspiring for active inference methods.
So what is interesting about their simulation results is that they show that agent that there is some emergent collaboration on tasks for low values of the susceptibility parameter without any explicit planning or communication needed.
And this means that they improve upon the original Bayesian model, which explored different sort of overall plans for all of the agents, which means that an agent employing Bayesian Tom would need to reason about the roles of all of the other agents, which was very costly.
And the authors wanted to improve on that to model maybe on the fly coordination, which is more spontaneous and takes less time.
And they also show that incorporating belief resonance has a very positive effect in scenarios in which there's unbalanced information.
They did this simulation, the overcooked domain in which agents have to collaborate on different cooking tasks and the goal is basically the order, the cooking order.
And then the intention would be any kind of action that has to do with completing the order.
And they show that incorporating the leaf resonance seems to be especially useful in situations with unbalanced information which, for example, one agent knows the order and the other doesn't.
And these agents develop some kind of leader follower dynamic in which one is more susceptible to the other agent's intentions and one agent attends more to the evidence from the environment.
And this also aligns with what we know about your mind mainly being employed in situations in which there is some asymmetry in what the agents know about the environment.
So I thought that was very insightful.
Okay, so I'm going to go into some active inference approaches that I think are relevant for developing active inference theory of mind.
First of all, there's this very broad proposal on inculturation and non development thinking for other minds, a variational approach to cognition and culture, which we'll go into a little bit.
We'll go into Castle and HAF's paper on ideas for spreading a free energy proposal for cumulative cultural dynamics.
We'll go into Kaufman et al's.
Model on collective intelligence and finally also the proposal by Mutusis et al.
On Beijing inferences about the self and others.
Okay, so first of all, I am starting with beta inference about the self and others because it gives a very sort of broad introduction to, I think, predictive social cognition.
And that's also why I've added this figure on the right that is from the Tam Thoughts and paper in 2018, which explores the predictive social brain and what kind of features seem to be relevant for categorizing and understanding others behaviors.
Some figure on the right, you see that there is this space, this trade space, which is ordered by power, sociality and balance, and that constraints the state space which seems to be ordered by rationality, social impact and balance.
Of course, these are just correlations, but these futures seem to be most predictive of what they're seeing in the brain.
And you can see that there is this sort of basically a very strong top down constraint of the possibility space in which you interpret other people's actions.
And you can also see that based on another agent's actions, you learn something about where they fall within that space in a given context and also where they fall in that trade space.
What kind of so at the same time, you might have already have some priorities on what kind of a person this is, but you're also learning about it.
You might also have some priors on how someone behaves when they're mad, for example, or when they're sociable versus unsociable.
And all these kinds of priors informative priors.
They inform your predictions in the context, and they make this task much more manageable of predicting other people's behaviors on the fly.
And I think that links very well back to Mutuses proposal, which is basically that inferences about the self and others at different timescales facilitates interpersonal minimization of surprise and thereby optimal social decision making.
And these self and other representations that facilitate personal minimization of surprise could be seen as representations that inform our inferences and predictions on the fly.
I think it's also important to mention that one of the main key points of their paper is that self representation, so beliefs about how beliefs about the self can facilitate interpersonal minimization of surprise.
So even what I think about me and how I represent that, while communicating, will facilitate the other person's optimal decision making at that moment, maybe by providing the right kind of information that they need to optimize.
Okay, so to the next two interesting papers, ideas Worth spreading and an active inference model of collective intelligence.
So the key idea, I think, for both of these papers is the emergence of group behaviors from local interactions.
For Caston Hess, this is the global group behaviors cultural transmission or transmission of beliefs and norms.
And they describe this process as the mutual achievement of actively inferring agents through communication.
And theory of mind is one of the many mechanisms that facilitate this process of achievement.
So that's the link.
And they show that the spread of certain kinds of beliefs through a group can be modeled just by making agents interact in diadic groups and stimuli.
Kaufman et al.
Show that you can create a system of free energy minimizing agents with some minimal properties of social intelligence, such as the ability to assess how self similar another agent is to themselves, the ability to infer another agent's intentions, and the ability to align their goals to another agent, more or less.
And they show that if you put all of these agents together in those diets, they don't only minimize free energy on the dietic scale, but they also minimize free energy as a collective.
And thereby, this is a very simple model of how adaptive behaviors, group adaptive group behaviors, could emerge from agents with very simple social abilities.
Okay, so now we get to thinking through other minds, which is not technically a proposal for theory of mind, but it's a proposal for how social cognition shapes inculturation more generally and what kind of abilities agents need to facilitate this kind of normation.
And I think it's a very interesting proposal because I think it highlights an important function of social behavior more generally.
And you could even see it as a way to redefine theory of mind as more of an interactional concept than as an individual level cognitive ability.
So, according to this proposal, thinking through other minds is a property of multiple interacting minimizing agents and a process by which agents infer other agents expectations.
And based on this, the authors propose a definition of enculturation as a process of learning social expectations through the selective patterning of attention that guides agents towards relevant affordances within their social and cultural niche.
I'm not sure if you're all familiar with the concept of affordances but it was quite hyped up a couple of years ago.
In general it is defined as relational construct denoting possibilities for action offered by an environment that are code determined also by an agent's interest, goals and abilities.
So I think that the standard example for this is when you are thirsty, a glass of water might appear as an affordance or you might not consciously or might also tend to it otherwise.
And cultural affordances in this sense are epistemic affordances.
So affordances that give you some epistemic value that have come to stand out as reliable and relevant based on a history of culture information they encode.
And good examples for this are different kinds of signs of traffic signs.
We learn what they mean from a young age and we sort of inherited the symbolism of the traffic signs and they guide our intention towards points in traffic and they regulate our behaviors.
So when you look at the complete proposal, it sketches how the regulation of social behavior depends on the learning of shared norms and expectations and also how this connects to utilizing cultural affordances and thinking through other minds.
As this profits interactional processing, in which agents learn to infer each other's expectations to optimize collective behavior and decision making.
Okay, so from these interesting active inference and broader proposals of fear of mind we get to the issue of form.
Sophistication in active inference so what is fear of mind?
Sophistication a short recap it's the depth of reclusivity that can be utilized for fear of mind of the form.
I think that they think that I think, and it has been found that agents generally use a reclusivity of between zero and four and that humans, humans ability for recursive belief reasoning is generally limiting but in principle, formally this could go on forever.
And one way to implement this kind of sort of arbitrarily recursive belief inference is proposed by Vada et al.
Uses a Bayesian model of sophisticated theory of minds with Ktom agents and provides simulations in which K tom agents play against agents that are just one level of recursivity under them.
And this model has been used for a lot of interesting simulation experiments.
For example.
Devane Et Al Showed that in a trade based analysis but with agents having a fixed depth of theory of mind reclusivity there is a specific distribution of agents with level one tom and level two tom that could provide an evolutionary advantage compared to populations with larger proportions of serotonin three tom agents.
So they look at the adaptive properties of systems with different kinds of ratios of theory of my sophistication.
And in another experiment, which is a state based analysis for Joe et al.
Showed that if you use computational phenotyping on autistic individuals, this shows reduced sensitivity to task framing and strategy switching within the game that they'll be using and theoretical line sophistication.
So these are just some interesting applications for theoretical mind sophistication.
And the promise of modeling theoretical mind sophistication would be that you could investigate how people flexibly switch between different social strategies while solving a social task.
And one of them would be to increase the depth of fear of my sophistication or decrease it depending also on what you think about the other agent's.
Sophistication.
So what I've been working on at the moment is an active inference model of social prediction during the Matching pennies game.
The matching pennies game is a game farm economics with a very simple format.
There are two rules.
You have the guesser and the challenger.
The challenger hides a penny in one of the two hands.
The guesser needs to guess which hand, if the guesser is correct, they win, if the guesser is wrong, be challenger wins.
This game has some logical equivalents.
One version of the game makes both of the agents select heads or tails.
So the challenger selects heads or tails and the getter guesses the tests or tails.
But both have the same formal structure.
And psychological experiments of subjects performing this task have shown that there is a strong social framing effect in the Matching Pennies game.
So participants will behave and perform differently depending on whether they're seeing that they're playing against a human agent versus an AI for example.
Additionally, a comparison of Ketone and other computational strategies that were fitted on experimental data of subjects playing the game revealed that participants seem to use fear of mind when playing the game.
So there is a strong indication that theory of mind use does play a role in the Matching pennies game and that social framing will influence the social strategy that's being employed by the players.
So this is the very simple zero sum architecture for the Matching pennies game.
And I included beliefs about self choices as also kind of monetary self states beliefs about other agents choices on whether the agent thinks the opposing agent has hidden the penny left or right.
And then the agent also tracks the war dates.
Since the game in this setting is devised in a way in which the agents both make an observation simultaneously and then all of the observations are revealed, this set up made sense so just going to drink a little water.
The outcome modalities or observations that the agents have are its own choice observations, the choice observations of the opposite agent and the reward observations and the possibility the action space is very limited.
The seeker can choose to seek left or right and the hider which is the same as the challenger before, has the possibility of hiding penny left or right and the reward is uncontrollable since it depends on both agents choices at the same time.
Yeah.
So this is sort of a summary of the architecture that I just described and this is another visualization of this setup.
And you can see here that if you look at the likelihoods the reward mapping for the seeker is just the opposite as for the hider.
And I think that this simple setup is very suited for studying fear of mind in these kinds of simple competitive interactions.
Okay, so if you wanted to study the use of theoretical bind sophistication in the matching penny scheme using active inference, I ran into a couple of challenges and one of them was how to steer the problem of recurring s.
So how can we make a difference between the focal agent and the other agents?
If we try to model the other agents within one agent, especially if you want to introduce or formalize desperate cave reclusivity, you can't just make one agent simulate the other agent simulating their self.
There needs to be some kind of sort of structure that distinguishes the self inferential mechanism, a self learning mechanism from what the agent focal agent thinks the other agent is thinking and seeing and doing.
And I think the gentleman with the bowler hat by firster in 2003 is a good example for this problem.
So the basic setting is that our world is populated by beings like ourselves experiencing themselves as a subject, as the focal point of their world, with their own thoughts and feelings.
And they all think that they're the one and only subject.
But there can't all be.
So there needs to be sort of either an outside focal point or one ultimate main subject.
I think more practically, the questions that arise from this example are how do we distinguish between focal agents and simulated agents and how can we simulate other agents in a way that is computationally efficient and maybe uses the same kinds of resources that the agent already has?
So I actually had a lab meeting at the Theoretical Neurobiology Lab a while ago and we were brainstorming about this issue and one of the ideas that came up was to use sophisticated inference for period mind.
So in this case, an active inference formulation of belief recursivity could be used for modeling recursive period, line.
Basically, serious planning using predictions about the other agents into account would consist of evaluating all the kinds of hypothetical scenarios, all kinds of counterfactuals on how your actions might influence their beliefs and their actions and so on and so on.
So this would be one road to go into.
But this would also mean that all these counterfeituals would need to be evaluated.
So I was thinking is there a sort of more efficient way to sort of use these kinds of either internal simulations or kind of special evaluation?
And the current approach I'm working on, which I'm also sort of still developing.
So I'm very much open to feedback and comments on how this could work and possible alternative approaches at this point.
But the general idea would be to create a partial internal simulation of the other agent's control mechanism.
So taking the learning mechanism of an active inference agent as sort of the definition of what the focal agent is, that is the agent that perceives and learns and infers from the environment and what the agent does when predicting the observations of the other agent or the predicting the other agent's behavior is basically performing partial simulation about what it thinks the other agent preferences are and what it thinks that the other agent strategy is, which is encoded by the transition from state to state.
And one of the potential ways in which you could include reclusivity in this way is that you pretend that you have control over the other agent's actions and you predict the other states.
You predict self states, you evaluate the state action probabilities, choose the most valuable action based on that distribution, simulate the other states that come forth and simulate the self states that come forth.
And then you have a new and then this can be used for the next round of action selection by the other model.
So in this case, only the per preferences and the agent specific transition probabilities would be needed as sort of information on the other agent.
And because you also want to include some kind of learning about the other agent strategies, one of the things you could implement would be learning also the Bay metrics.
So having sort of the specific having the agents accumulate as evidence about these state transitions over time to also better predict the other agents potential actions.
The basic principle would be to simulate control from the perspective of the other agents and the recusivity comes into play when you simulate the other when you've already simulated the others predicted actions and predicted other states and you've simulated your own actions as a consequence of those simulated actions.
You can feed that back into the other model to predict what they would do if they thought that you were in the state that you were in.
And I think that could be a way to develop repressivity in a way that does not need complete simulations of parallel agents within the same system.
And of course there should be some kind of temporal discounting subparameter that discounts evidence based on the simulated planning horizon that is defined by the K number of steps.
So yeah, this is sort of a conceptual outline of how you could implement because the fear of mind using active inference we haven't been able to perform simulations using this yet, but we're working on that and we're very much open to discussions on this and technical comments on how to improve on this outline.
And one of sort of the open questions that we are still thinking about is how to make the agent effectively infer the depth of reclusivity of the other agent in.
A setting.
Yeah.
Special thanks to Guillaume Dumas, who will also be there at a panel, I think, in session two, who's supervising me during this project.
Thanks to the PPSP labor, I'm doing my internship to Rudy Said, who's also working on a related project, the Pi MDP team, for that great coding package that I'm using, and for Kofristen for his feedback and ideas on my previous presentations.
Thank you very much for listening.
Cool.

45:02 _Daniel:_
Great presentation.
Very comprehensive review of a lot of the different theory of mind options out there.
Well, if anyone has questions, they can write it in live chat.
What do you want to explore?
Or can I ask a question or what would be fun for you?

45:28 _Nynke:_
I'm blinded by the light at this point, so I can't easily read from my screen.
So maybe it would be nice if you could read out the questions that are the live chat.
Sure.

45:41 _Daniel:_
Oh, yeah, sure.
Well, first one part I found interesting, you mentioned that people play differently when they are playing a human or when they believe that they're playing a human.
So what is that like?
What is the difference in play when we believe that we're playing another person?

46:15 _Nynke:_
If I look at the original paper, there is one study on this, and then they did the computational phenotyping study using Ktom and alternative strategies, and they showed that if you use the social framing condition, that subjects will more probably employ figure five strategies compared to other simple reward based strategies.
So maybe those strategies could better be described using some kind of reward learning mechanism.
What the difference in their overall sort of trajectory of choices is, I don't know.

47:05 _Daniel:_
Yeah.
A few themes then that you brought up that came up earlier in the session.
So one was using Pymdp and sophisticated inference, which Aspen Paul gave a walkthrough on.
And this question about recursivity and about the way in which you can on one hand talk about abstractly like K Recursivity, yet the biological system doesn't implement that kind of a logic.
Could you maybe describe a little bit again?
How does the structure that you laid out for the generative model capture some of those features of recursivity without falling into the trap of just theory of mind all the way down?

48:03 _Nynke:_
Yes.
So my general idea was to simulate the other agent's action prediction based on learning about the transition probabilities for what we think how the other agents face transition.
And then if you've predicted what the other agent would do, you can use that as a prior for calculating action dependent expected states.
And based on those evaluating those expected states, you simulate your own choice mechanism.
And I think in principle, you could use this recursive simulation indefinitely.
But also, it's also devised in a way that it uses the same kind of sort of just the architecture of the focal agent.
So the other idea was to just use internal simulations all the way down and but that would be very cognitively implausible and yeah, I think it's a very good question, because why would you even need to formalize belief?
reclusivity all the way down.
If in end effect, people only use tom with a set sort of maximal depth and the fact that we use fear of mind with a maximum depth might also be sort of a hint that he might also use a different or what we do might also be described by a different strategy.
So yeah, I'm not sure if that's an answer to your question.

50:08 _Daniel:_
Yeah, well when I saw this and some of the other generative models you mentioned maybe here like you pretend like you can control the other person's mind and that's kind of the fundamental weaving of action into the inference challenge and then that uses expected free energy just like any other policy selection.
So it's like pragmatic value would be bringing that controllable state your social partner's mind or beliefs bringing them into alignment with your preferences is pragmatic and then learning more about them is epistemic.
And so then that might enable some theory of mind like behavior where it's like when you don't know enough to put the squeeze on then you have a kind of open ended learning and curiosity and question driven theory of mind.
But then once one has enough to kind of exploit rather than explore then without necessarily even updating the model or engaging any deeper recursivity or strategic shifting you could get social behavior that's oriented towards control and pragmatic value rather than just like learning and questioning.

51:36 _Nynke:_
Yeah, I think you're very right.
The idea was also to enable the agent to maybe first use strategies that are more useful in gathering evidence about the kinds of strategies that the other agent is using before exploiting thing what you've learned about the other agent and.
