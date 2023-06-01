
00:05 _Daniel:_
This is active inference Livestream number 54.0.
We're discussing mathematical foundations for a compositional account of the Bayesian Brain.
Welcome to the active institute.
We're a participatory online institute that is communicating, learning and practicing applied active inference.
This is a recorded, archived and published Livestream, so please provide feedback so we can improve our work.
All backgrounds and perspective are welcome and we'll follow video etiquette for Livestream, head over Active Inference.org to learn more about getting involved in live streams and in a variety of other projects and learning groups.
All right, well, we're in stream number 54.0 and we're going to be learning and discussing the paper that was submitted on the 23 December 2022 as part of a dissertation work, mathematical Foundations for a Compositional Account of the Bayesian Brain by Toby St. Clere
Smithe.
The video is an introduction for some of the ideas in this multi hundred page thesis.
It's not a review or a final word or a thesis dissertation committee, this 54.0, given the scope and the complexity, but also accessibility of the ideas, we're going to be approaching it in a familiar way, but also with some twists.
We're going to begin with some introductions, the aims and claims, abstract and roadmap as usual.
Then we're going to approach the keywords and the context in a slightly different way than we've done in a lot of other zeros.
And then we're going to kind of bookend the dissertation and focus most on chapter one and chapter seven, the first and the final chapter and chapters two through six.
We're looking forward to unpacking more with Toby in the coming weeks.
So we'll begin with some introductions and warm ups.
We could all just say hello and something that was exciting for us about the paper dissertation or what brought us to the work.
I'll begin.
I'm Daniel.
I'm a researcher in California, and I have to say that six months ago, when we started this journey haw on the heels of the dissertation being posted when, along with Ali and Dean and others, we decided to embark on this weekly learning quest, I was very unfamiliar with category theory.
And thankfully, after closing the window, it all escapes my mind.
So it's been quite a six month period to learn and to forget so much.
I'll pass to Dean.

03:07 _Dean:_
I'm Dean, I'm here in Calgary.
I think the thing for me, when it was first broached the idea of taking this up about a decade ago, I started just scratching the surface of this idea called category theory, and to see this amount of work put together, to sort of bring a whole bunch of ideas together and, as Daniel already mentioned, make it somewhat accessible or I don't know if it's a beginner's guide or a category theory for dummies.
Exactly.
Because there's still a lot in here.
But in terms of giving us an opportunity to get some verifications, for me, at least that's what I got with some validations and some verifications was really helpful.
So I am excited about having a chance to talk about this and bring the author on eventually and have that conversation get extended and I'll pass it over to Ali.

04:15 _Ali:_
I'm Ali, I'm an independent researcher from Iran.
Well, I also had just a passing familiarity with category theory and wasn't familiar at all with lots of terminology and formalism in this thesis.
But after covering the whole thesis in our six month period, it now begins to make much more sense.
I definitely started seeing category theory in almost everywhere, both in sciences and also in some other, not specifically scientific areas.
So I'm really excited to have these discussions with Toby and learn even a lot more.
Thanks.

05:15 _Daniel:_
All right, on we go.
We'll begin here with a meta prompt.
So for all of you human and non human language models, please fill your context window with this metaprompt.
On to the big questions.
So we have some hidden questions that are in white font below that those who go to the slides will find and discover.
But we raised many questions.
And Dean or Ali, what's just a question that strikes you today?
What is a question that would lead someone to come to this dissertation?
And we're going to be covering a lot of Toby's summaries in terms of the contributions, Ames claims and foci of the dissertation.
But what does this dissertation ask or what would somebody ask to get to this dissertation?
Yeah, please, Dean.

06:16 _Dean:_
If you want to know why we tend to put things into groups, why things have a world where there's something that's in a category or outside of a category, and most importantly, where are the things that aren't in either of those two places?
This gives you some of the operational backbone to be able to start figuring that out.

06:59 _Daniel:_
All right, on we go.
Aims and claims of the paper.
So, paper or dissertation Draft mathematical Foundations for a Compositional Account of the Bayesian Brain was uploaded in late December 2022 and just several overview claims of the work.
Our main aim in this thesis is to formalize predictive coding through functional semantics and Bayesian lenses will provide an important part of the syntax of statistical models that we need.
In this 54.0 video, we're only going to cover chapter one and chapter seven, and we're going to review them for some really interesting, bold and ambitious claims.
And there's a few great overview claims for the entire work that do a great job of just distilling down so many hundreds of pages and so many technical contributions from page seven.
The main individual contribution of this thesis is the introduction of Bayesian lenses and the proof that Bayesian lenses compose optically and the first sentence of the abstract.
This dissertation reports some first steps towards a compositional account of active inference and the Bayesian brain.
Anything else to add on aims and claims?
Okay, either of you please start with the first half of the abstract.

08:30 _Dean:_
Go for it, Dean.

08:32 _Ali:_

08:32 _Dean:_
Specifically, we use the tools of contemporary applied category theory to supply functional semantics for approximate inference.
To do so, we define, on the syntactic side, the new notion of Bayesian lenses.
Think it's important to get the plural there and show that Bayesian updating composes according to the compositional lens pattern.
Using Bayesian lenses, and inspired by compositional game theory, we define categories of statistical games and use them to classify various problems of statistical inference.
On the semantic side, we present a new formalization of general open dynamical systems, particularly deterministic stochastic and random and discrete and continuous time as certain coalgebras of polynomial functions which we show collect into monoidal open text categories or alternatively, into algebras for multi categories of generalized polynomial functors.
We use these openexed categories to define monoidal bicategories of cilia dynamical systems which control lenses and which supply detarget for our functorial semantics.
Just one quick thing.
If you're like me, you had to spend a lot of time finding out what do these words actually mean?

10:11 _Daniel:_

10:20 _Ali:_
Along the way, we explain how to compose rate coded neural circuits using an algebra for a multicategory of linear circuit diagrams, showing subsequently that this is subsumed by lenses and polynomial functors.
Because category theory is unfamiliar to many computational neuroscientists and cognitive scientists, we have made a particular effort to give clear, detailed and approachable expositions of all the category theoretical structures and results of which we make use.
We hope that this dissertation will prove helpful in establishing a new well typed science of life and mind and in facilitating interdisciplinary communication.

11:20 _Daniel:_
Okay, here's the roadmap.
We're only showing a zoomed out view because if the other papers we've discussed were going on a road trip this is the continent scale road trip.
The dissertation is 230 plus pages long.
It's in seven chapters that are shown here, and in 54.0, we're going to be focusing on chapter one and chapter seven.
So it's quite a piece of work.
And this is just the background and context.
There's a table of contents with more information and on what the chapters do.
Let's take a few more steps or moments in the background and context to really set up the reading and expressing of this work and really this kind of work.
So thanks a lot to Jr for preparing some of the following slides.
Here we have some selections from several works in mathematics and category theory on reading math.
There is a real joy in doing mathematics.
We've all heard it before, but it really comes to be true when we enact it that way.
The challenge of mathematical understanding is to find a way to make new mental images in oneself on the basis of formal definitions, to make these definitions intuitive, to feel what they are talking about.
And Jr's summary of some of the ways that math is utilized in this dissertation.
So, in regards to the writing in this thesis, just like with anything else, something is being written for an audience.
Toby is writing to an audience of domain experts and a dissertation committee, ultimately to demonstrate and embed new contributions to knowledge.
He also takes a pedagogical approach, a teaching approach.
And Jr asked, is this pedagogical approach something you see in most PhD?
Theses briefly, I would suggest no.
And on the reading of this thesis, it helps to be clear why we're reading it.
If to help understand or sense make active inference models, then aim to read it at one level and take the rest on faith.
If we want to understand the formality better of the really nitty gritty category theory itself, then read to that level and go deeper.
Any thoughts, either of you fellows on the first Reading Math slide?
Okay.
And on the second Reading Math slide, a few more great tips on just reading math and what we're doing with math.
So, first, eyes on the prize.
Math is a language, and as such, it's there to convey something about the world, about the structure of this thesis overall.
And overwhelmingly, there is a plain English exposition of what concepts are needed and why, with nice transitions, foreshadowing and back references.
There's also a true wealth of beautiful diagrams, which in category theory have a formality that those used to schema type diagrams will be pleasantly surprised by.
They're definitely challenging to interpret.
It is a new visual language for some, however, it's one that can be admired without necessarily needing all the formality.
About roles of definitions in reading of math, what the audience knows is truth is a shared prior belief.
Things start from there.
These definitions are used to build up further truths through logic and the proofs, and from the Bessis citation in a mathematical text, the most important passages are neither proofs nor theorems.
They are definitions.
Mathematical language works as a construction game where words are truly defined, that is, constructed from other words that themselves have been previously defined.
And about role of proofs in reading maths, very similar to providing well argued evidence in any technical writing.
Math is technical writing with math as its particular structure.
And there's other great things to read.
But that's all I'll mention here, just at an overview, are there any other thoughts that either of you would add just about reading math or reading this kind of technical work, which can be like getting dropped in the deep end.
I mean, we're getting dropped into the cutting edge PhD contribution frontier of knowledge.
So how do we negotiate that, especially when there are these esoteric or inscrutable symbolic systems that seemingly constitute the majority of the words in certain passages?
Dean.

16:45 _Dean:_
All you basically have is the geometry, but when all the pieces fit together, you're then allowed to flip it over.
So you have to be really committed.
And my hat is often to the work that Toby has done because for him to make it coherent, given the actual volume of information that he would like to pass along.
Part of my grinding through this was the thought in my head that if I'm grinding through this, I can't imagine what the author had to go through.
So even if you're excited about this, it's still a huge commitment.

17:51 _Daniel:_
Ollie, anything?

17:57 _Ali:_
So I agree with Dean that doing such a I mean, such an admirable task of organizing the materials of the dissertation in such a coherent way is truly a herculean task to do so.
But another point is that, well, even in the realm of category theory, most of the things done so far is done in the purely mathematical world.
So applying those concepts of category theoretical concepts to some realms outside of mathematics is something that's just been explored for the last few years at least.
Seriously so I believe Toby didn't have much to start with, given that the scarcity of material in the applied category theory area.
But of course it's a burgeoning field and it's gaining traction quite rapidly.
So I hope to see much interesting works in the future and I believe Toby's dissertation will help a lot in shaping the future trajectories.

19:44 _Daniel:_
On to the keywords.
So three big keywords are category theory, Bayesian brain and active inference.
And then category theory is really a language of its own for some of the relevant keywords that we pulled out in our shared epistemic niche, the coda document that we utilized to collaborate over the last six months as a team.
Here's some of the terms that we had on the right side and we had a full table that people who go to the slides or the coda document can explore more.
But there were so many creative words, just words that you're not going to get outside of applied or basic category theory.
It was quite a learning journey just from a lexical perspective, so a lot of keywords and a lot of domain specific words in category theory.
But we keep the bigger picture in mind about Bayesian Brain and active inference.
And one last piece of information here before we head off into the dissertation itself.
Jr.
During their internship over the last several months at the Active Inference Institute, among other works, completed an absolutely beautiful Syllabus adventure mode syllabus for introduction to category theory applied to active inference, and it's hosted on our GitHub at the institute, so hopefully people can find it useful and continue to version and utilize it and make contributions to it.
I'll just read the summary.
It's for any curious, thrill seeking active Inference institute participant who wishes to study and conduct further research on active inference related papers that involve category theoretic tools.
And we have a fractal embedding of a quotation from Christopher White on model stream number 1.1 we have a finite time on this earth, right, and a finite time to dedicate to learning things.
The syllabus is centered around the Joy and the dissertation, so another category theoretic work for background and the dissertation itself.
The approach is based on experiences within the category theory learning group, insights from the Topos Institute Category Theory Outreach Panel and Chang and the Joy Book Club, and this great line from Emily Real in her book Category Theory and Context in the Note to the Reader's section.
Inevitably, given the diversity of mathematical tastes and experiences, the examples presented here will seldom be optimized for any particular individual, and indeed, each reader is encouraged to search for their own context in which to explore categorical ideas.
So this curriculum is something that will be living and versioning as we move forward in the active inference applied category space.
Super exciting.
So thanks again Jr, for the epic contribution and we all reviewed the syllabus and just found so many interesting aspects to it.
So there's a lot to learn, no surprises there.
But it's awesome when other adventurers help create spaces and ways for others to go on their own adventures.
And it really feels like in category theory that there is a culture of that.
So it's really encouraging.
Okay, to the overview of the dissertation itself.
As stated earlier, there are seven chapters.
Chapter one is an introduction.
Chapter two is a comprehensive review of the concepts and results needed to understand the mathematical contributions.
Chapter three begins to re approach neural modeling and more generally, the algebraic modeling of the structure of interacting systems.
Chapter four presents the first main result that Bayesian Updating composes according to the categorical lens pattern.
Chapter five introduces the corresponding semantical categories with a new abstract formalization of the concept of open dynamical system.
Chapter Six presents the functional formalization of predictive coding using a new notion of approximate inference doctrine by which statistical models are translated into dynamical systems, and chapter Seven reviews the prospects for future work from the Mathematics of the cognitive map a program called compositional cognitive cartography to the composition of multiagent systems and ecosystems and the connections with compositional, game theory, and other categorical approaches to cybernetics.
Aliyardine, any overall thoughts on the seven parthe structure of the dissertation?

25:01 _Dean:_
But you also will find that you can work backwards.
In fact, there's stuff in chapter seven that literally points you in that direction.
So you might want to give it like a once over just to sort of orient yourself.
And then you should feel free to be able to go bi directionally, just a strategic prompt, because if you get bogged down and it's very easy to get sort of caught up in the minutiae of this, I would just say Zuma, step back.
And if it's not registering on the first pass, it might register if you start going a little bit backwards and forwards instead of just one directional.

26:03 _Daniel:_
And just to summarize some of the primary contributions few quotes.
The main contribution of this thesis is the formalization of models of predictive coding circuits as functional semantics and the associated development and exemplification of categories of statistical games, as well as the introduction of Bayesian lenses and the proof that Bayesian updates compose optically that is in some sense like optics.
We believe our presentation of general open dynamical systems as certain polynomial coalgebras also to be novel, along with a concept of cilia and their associated monoidal bicategories.
We hope that this dissertation contributes to a renaissance of cognitive and computational neuroscience through the adoption of categorical methods.
We're going to be returning more to all of these, so it's going to be cool.
And Ollie, it's all good with a video off for internet's sake, but just raise your hand or bring your video on whenever you would like to speak.
Before we take the jump, we just pulled out two small quotes that's going to help us leap off this cliff to map the gap, respect it and beyond.
So first, from page 226, this is from chapter seven.
This resemblance becomes even closer when one considers the recent Diegetic open parentheses Diegetic occurring within the context of the story and able to be heard by the characters within the story.
The recent Diegetic formulation of open games in which strategies themselves can be updated using a backwards map from the arena of the game back into strategies or rather strategy updates.
And then fundamentally, from page 225, this is also the idea underlying the successor representation of the cognitive map, which says roughly that the brain's representation of where it is is equivalently a representation of where it soon expects to be.
And so how as we bring that last foot of the 6ft off the other side of the cliff and jump through the unknown, how do we take this immense work and update our strategies backwards so that we can successfully represent and disseminate ourselves?
Any final words before we jump into chapter one on this topic?

28:49 _Dean:_
So I think it's very important to now take the leap.

29:23 _Daniel:_
Now we're in chapter one.
So for the coming slides, Ali or Dean, please just, if you'd like, select one bullet point.
Feel free to read the bullet point or give any remark.
And on these coming slides we're just going to move through.
But either of you or both of you, please take the first pass.
All right.
So chapter one introduction.

29:59 _Dean:_
I think the one that we bolded here, category theory is the mathematics of pattern, composition, connection and interaction.
I think you can read that, but I believe you also have to kind of sit back and ask yourself, so what does that mean?
So right away they're taking a superordinate and they're breaking it up into its parts.
And so again, there's this world within world within world thing that is reinforced just in the way that we have to try to communicate the ideas to the readers.

30:39 _Daniel:_

30:42 _Ali:_
These two issues, I believe, are the organizing themes of the whole dissertation.
And we see these issues addressed time and time again throughout the thesis and particularly in chapter seven, which these issues are addressed quite explicitly, both in terms of the work or the contribution done in this thesis and the suggestions for future research.
The other point is that the language of category theory is homo iconic and can be used to translate constructions between contexts.
So again, right at the beginning, this dissertation tries to put a particular perspective in order to address the two issues just mentioned.
So in this case, Toby uses the homo iconic property of category theory to address those two issues.
Or more explicitly, category theory resolves both problems of scientific translations in this way that concepts expressed categorically are inevitably expressed in context and not in isolation.
And secondly, these contexts are naturally interconnected as if by a categorical web with the connections and expressed categorically.
So in other words, category theory provides probably the ideal toolkit to address those situations, those issues, which I believe is not restricted only to scientific endeavors.
So these two issues come up in many other areas and outside science as well.
So in that case, I believe category theory can provide a much more general framework to address them, even in non scientific fields as well.

33:18 _Dean:_
I agree with you 100%, Allie, about the toolkit.
And I would add that I also believe it gives us an opening to develop a rule kit so that we can actually figure out how to do that translation piece.
And it also gives us a pool.
I like to use things that rhyme because it's easy to remember, but the way that we collect how things congregate, what that attractor state becomes so that we can then figure out how things are moving in that dynamic situation.
So I think it provides a toolkit, a rule kit, and a pool kit.

34:02 _Daniel:_
All right, next slide on chapter one.
I'll just pick one and then either of you please.
The one that's exciting to me is we show that the theory of predictive coding has a clear compositional structure that explains the bi directional circuitry observed in the brain.
So even outside of the connection to the empirical grounded embodied biology, the idea that a lot of the ways that in retrospect, informally, we've been talking over the last years as a field and in the institute about the compositionality of models and can we just plug in the sense states here to the action states here?
Can we nest the models these ways?
And the ways that we've been thinking about the active inference cognitive kernel like a Lego kit.
All of this is realizing a level of formality, which doesn't mean inaccessibility, really quite the opposite.
That's just accelerating what's possible with predictive coding.
Bayesian brain active inference free energy principle.
So we're really seeing like a dawning of the formal compositionality and to be able to compose and to be able to construct are going to have a relationship that we can continue to weave in the coming sessions.
Either of you want to highlight some other piece here?

35:34 _Dean:_
deconstructure meaning there's a lot of pruning and sculpting that they actually speak to if we were to talk about real things that form and shape and give us that sense of what's in and what's out.
So yes, they are building an infrastructure, but then Toby goes along and speaks a whole bunch about so why does this stay and why does this not get included?

36:17 _Daniel:_

36:22 _Ali:_
It reminds me of Mario Bongay's work on causality and also Alan Garfinkel's theory of explanation and particularly in Garfinkel's work.
In his book Forms of Explanation, he provides a theory of explanation based on rigorous modeling of problems in terms of state spaces and how we can address the context dependent explanations based on the contrast space on one hand and the relevant space on the other.
So category theory, I believe, somehow unifies, or in other words, translates these kinds of theories into a rigorous and coherent framework that can be used to formalize or rather to frame all of these theories of explanations and causalities within a unified framework.
So that's, I believe, one of its greatest advantages.

37:37 _Daniel:_
Okay, anyone want to give a comment here?
I'll just give a quick comment, which is and this is just a peek ahead to chapter two we're only going to have a few snippets from the medium, the meso chapters, the space between.
But don't we see diagrams like this all the time in active inference with internal external blanket states, the particular partition, hierarchical predictive processing, Bayesian brain architectures?
We see these diagrams all the time.
And section 2.1 is extremely provocative with the analysis of neural circuitry and two other types of systems in really establishing that the drawing, if it's informal, is insufficient to completely convey the argument and to really represent the situation.
However, if we use the kind of string diagrams or just diagrams more generally that category theory provides, we really get a graphical compositionality that just drawing on a page, though obviously wonderful and fun, does not reach.
And so we're going to be able to talk about how these types of diagrams, which again we see all over the literature, can be enriched with this category theoretic perspective so that we can assess, well, what if I draw a line from this one over to that one?
Is that valid?
How is that going to change the properties?
And so we're going to be able to know a lot more about that when we understand the compositional structure via the Bayesian lenses of these compositional Bayesian systems.
Anything else to add on this slide?
All right.
Dean or Ali?
Go ahead.

39:56 _Ali:_
On the other hand, the underlying equations of the free energy principle exhibit a form of compositionality which is used to obtain the hierarchical models.
Despite the hint of compositionality, the equations of motion for these hierarchical systems are typically derived from scratch each time a redundant effort that would not be required had a compositional formalism, such as category theory being used from the start.
So this thesis supplies such a categorical formalism and exemplifies it with hierarchical predictive coding under the free energy principle.
Category theory has a rich formal vocabulary for precisely describing universal constructions.
And so not only does a categorical formulation of.
The free energy framework promise to clarify the current confusions around FEP, but it may be expected also to shed light on its potential universality.

41:13 _Daniel:_
And in terms of the current, the past, present and future status of the free energy principle and active inference, it's an absolutely consequential direction of work.
Dean, anything here?

41:34 _Dean:_
I know that in seven four one, which we'll talk about later, the introduction of the term fuzzy and fuzzy distributions comes up.
So even though they're being precise, they're being precise, their fuzziness as well.

41:53 _Daniel:_
Like a high resolution picture of a fuzzy jacket onwards.
So in this thesis, we do not get as far as a completely general formulation of active inference.
And it goes without saying this expression could be added to every single thing that we read today.
But in the coming videos and beyond, we're going to discuss what this all means and just one more exciting piece from this page.
Because active inference models and the free energy framework more broadly are descriptions of systems that are open to an environment, interacting with it, and therefore situated in context, they are particularly suited to a category theoretic reformulation.
So that's very exciting because we've from qualitative philosophical, humanistic approaches and also from statistical, numerical, formal approaches.
We've discussed a lot of this openness and now we have another entree or another vector or another toolkit rule kit, pool kit to work with, and that is just opening the space up a lot.
Ollie or Dean, want to add anything.

43:14 _Dean:_
We've talked in other live streams.
We've used images of ice cream cones and ice cream trucks and what's in the foreground and what's in the background, what's actually the context and what is the content.
And this reinforces that idea of as the observer, as the one using their optic nerves, what did you choose to put in front and what is in behind?
And we have to keep that in mind because we shouldn't assume that everybody chooses the way that we do.
So, again, just making sure we understand what's being said here in this slide.
It's really important.

43:58 _Daniel:_

44:02 _Ali:_
Because, as we all know, one of the distinguishing features of active inference theory and what sets it apart from other related theories such as Bayesian brain and predictive coding theories, is the fundamental integration of action into perception.
So as long as this dissertation doesn't provide a full fledged account of this kind of action integration, I believe it would be more appropriate to term it as a compositional account of the Bayesian brain and not particularly active inference.
But of course, in chapter seven, toby suggests some potential ways that this kind of integration can potentially be done in the future.
Research.

45:10 _Daniel:_
All right.
Chapter One is already foreshadowing the idea of cognitive maps.
And Toby writes current models of cognitive maps.
Some are expressed in the language of approximate variational inference.
We talk about that a lot.
Some are expressed in the language of reinforcement learning.
Some attempt to combine the two.
We expect that the foundations developed here will help us unify these accounts.
So how can we be reimagining?
Maps?
Cognitive maps?
Aren't they all?
Alir, Dean, anything else to add here?
All right, and last few selections from chapter One.
Either of you, please.
What's the first take?
Here?
I'll go first.
Our primary motivation in writing this thesis is to lay the groundwork for well typed cognitive science and computational neuroscience.
It's a very interesting topic about the implications of well typing and what does it mean for something to be well typed?
What is a programming language or a scientific culture or a framework that's well piped?
The free energy framework, like the structurally adjacent framework of compositional game theory, has a strong flavor of teleology what is that taste like?
And systems act in order to make their predictions come true.
We come to this so many times and in so many ways.
In reinforcement or reward oriented learning, you have a reward function, and systems work to maximize reward, whereas in free energy as a bounding variable or functional on surprise, the imperative is to bound and reduce surprise such that expectations or preferences are realized.
And so here it's expressed qualitatively.
We've approached this in many different paper discussions from a statistical, numerical, formal, analytical angle, and here we're approaching it from another formal avenue of category theory.
And either of you have any comments on this or want to talk about the last piece?

47:51 _Dean:_
In the programming that I did, we had a little axiom or expression that was, if it isn't history, then it's a mystery.
And I think that's part of what this scientific faith piece is all about.
I mean, if you have some data, if you have some way of recording or taking in or gaining some sense of, that's great, that's the historical part.
But you still also need that curiosity and that sense that there is yet still to be witnessed and observed.
And you have to have some faith that sticking around is going to be able to provide that opportunity.
I don't know if a well typed science will buttress scientific faith.
I think sometimes the personality matters.
I think if you're the kind of person who believes in curiosity being resolved and wayfinding being a really good strategy to find out who you are and what the world is about, I think that's the faith piece that some of us just seem to carry around, whether we like it or not.

49:12 _Daniel:_
Ali, anything on this slide or enclosure of chapter one?

49:21 _Ali:_
I believe Toby somehow implying a kind of more or less claim for disunity of sciences as opposed to a unified vision of science.
Because you see, in the unified vision for science, every explanatory models and every theory can theoretically be unified within an overarching principle or overarching theory, which has not been discovered yet.
But some philosophers advocate the position of disunity of sciences.
In other words, although there are some commonalities between every scientific areas, but there are some individual types, or individual concepts, if you will, that cannot be taken.
I mean, this individuality cannot be taken for granted simply by just explaining it away, by proposing some unifying principle.
So in this sense, well typed science is quite a rigorous and individualized notion of scientific endeavor, at least in my opinion.
But I'm curious to know Toby's opinion.

51:04 _Daniel:_
Obviously, people point to the way that a well typed language can prevent illegal operations or use safer handling of short term memory, working memory, and avert logical errors.
So it's very interesting to think about what that means in science in terms of not just the reproducibility of experimentation, but in terms of what experiments and what research avenues are pursued overall, as well as even cognitive security.
So there's so many different angles where well typing is going to matter for the way that we think about compositional, cognitive cartography, which we're going to come to.
Now, chapter seven, we skipped over a few pieces, didn't we?
That's how the last six months felt.

52:02 _Dean:_
Yeah.

52:10 _Daniel:_
That's the part that you want to take lightly.
That's the bottom of the bathtub.
You jump into chapter one and it's exciting.
It's like skiing downhill.
And then this vast tundra opens of chapters two through six, which again was the last half year for us and several others.
So now let's get to chapter seven, and then the sandwich will be dissected with Toby.
Okay.
With absolute humility and accuracy, toby points to three prominent shortcomings of the thesis.
Ali, do you want to summarize these three shortcomings?

53:02 _Ali:_
So the first one is that the notion of approximate inference doctrine should be tested with further exemplification.
In other words, specifically with the problem of double counting, which is addressed in chapter six.
The other one is that the general models that Toby is considered in this dissertation are somehow static despite its application in modeling dynamical systems.
So again, this problem is addressed.
I mean, some suggestions for overcoming this shortcoming is addressed in this chapter, specifically in relation to Meyer's Categorical theory of dynamical systems.
And finally, although we consider lower level neural circuit models, we did not explicitly connect our approximate inference doctrines to these more biological models.
So in other words, it's not a theory for modeling the whole Iguana, it's just a modeling framework for modeling a very specific function or the cognitive function of the brain.

54:32 _Dean:_
That's just philosophical me going knowing.
Okay, so of the three of us, I'm the one guy who's proud to say I get it wrong 20% of the time.
I don't give a rat's backside most often about precision and perfection.
I want to try.
And so if somebody says, well, the thing that I'm talking about here has its limits and it's not going to solve all the problems of the world, I just think that's being realistic and honest.
So call it shortcomings, I see it as a bit of a feature, being self aware of not being able to do everything at once.

55:15 _Daniel:_
And there's always an adjacent possible, indeed an expanding one.
So to make an exponentially expansive apology rather than pointing to the adjacent possible and seeing what can become is just two sides of the same coin with a third side being the rim on that coin.
7.1 structured worlds and 7.1.1 Bayesian sensor fusion.
Ollie, how do you see sensor fusion?

55:53 _Ali:_
So in category theory there is an obvious choice for addressing this particular problem, namely the notion of sheets, which is a spatially coherent data type, something like a bundle for which local sections can always be uniquely glued together into a global section, as Toby described here.
And it reminds me of the theory of, I mean the derivation of the duality between FEP and CMEP in Bayesian mechanics paper by deploying these notions of bundles.
So in other sense, sheath theory and the related fields of applied topology and chromology allow us to judge when it is possible to form a consensus and quantify the obstructions to the formation of consensus.
Hence, the consensus between FEP and CMAP as done in Bayesian mechanics paper, I believe is done in the same sense of sheath theory as providing a possibility for emerging such a consensus.
And also missing from the current chief theoretic understanding of sensor fusion is a thorough treatment of belief and uncertainty, especially from a Bayesian perspective.
A first possible extension of the work presented here is to extend statistical gains and approximate and approximate inference doctrines and hence the classes of model that they encompass, to structured data types such as sheets.
We expect that the first step will be to consider categories of channels between sheeps.

58:13 _Daniel:_
And just to give a more mundane or empirical example of sensor fusion, what if we have many EEG sensors on a head and we need to synthesize into one joint representation?
Or what if we have temperature sensors across an agricultural field and humidity sensors?
How this happens is called sensor fusion, and category theory is helping us understand the compositionality of such issues.

58:44 _Dean:_
I think where they say something like a bundle for which local sections can always be uniquely glued together into a global section.
Well, of course they can, but I don't know that that's necessarily the magic what if in a counterfactual sense.
What if they are glued?
Is that something we must commit to?
And then if it is going to be glued together into some sort of global composition, when that timing of when to do that, I also think is something that we judge.
So is that the data set, the what if and the when, is that the data set that we're going to eventually bump into?
I would argue yes.
Does that mean we're going to have to pass through that moment and come out on the other side of it, hopefully still intact?
Yes, to me, that is consensus building.
So I know that that's one little sentence in a 200 page paper.
But again, there are so many nuggets in this paper where if you just slow down and read it and think about what the implications of what they're saying are, you could literally go off right there on that one sentence and spend hours trying to figure out, okay, so really, what should we be doing with this?
Is this a priority?
Whatever.

1:00:25 _Daniel:_
Continuing on to address that first shortcoming, we already mentioned Sheaves, and we hope that these tools will suggest new connections to work on quantum theoretic formulations of the free energy framework.
That's something we've discussed in several stream series.
Livestream 17 with Chris Fields on information flow in context dependent hierarchical Bayesian inference, Livestream 40 with Friston, Levin, Glazebrook and Fields on a free energy principle for generic quantum systems and the ongoing Chris Fields course, Physics as Information Processing 2023.
So category theory and adjacent tools are already widely utilized in quantum sciences, quantum information science, more broadly, quantum computation, and so on one hand, we see the quantum and free energy principle synthesis outlined in these stream series.
And here we have the category theory, active inference, Bayesian brain, free energy principle synthesis.
So all three category theory, quantum and FEP walk into a sheath.
What do they say?
All right, Ali, what is a summary or overview on learning structure and structured learning?

1:01:56 _Ali:_
So an interesting distinction is provided right at the beginning between structured learning and learning structure.
So structured learning, at least Toby, means extending the process of learning to a structured setting.
But by learning structure, he means learning the underlying structures themselves.
So in the categorical semantics of dependent type theory, the context is witnessed by the object over which a slice category is defined.
And in so in some sense it defines the shape of the universe by the growth in the construction.
There is correspondence between sheaves and certain bundles as objects of slice categories.
And so we can think of structured inference and learning as taking place in appropriate slice categories.
So both of those somehow address the binary concepts of structured learning and learning structure in a complementary way.
So we can think of bundle morphisms as generalized parameters maps.
And in that case, the problem of learning structure then becomes a problem of generalized parameter learning.
And this is the way that some reinforcement learning techniques have been deployed by using this kind of generalized parameter learning.
So we expect this line of inquiry to clarify the relationships between our formalism of approximate inference and other related work on the categorical foundations of cybernetics which have typically been studied in a differential rather than probabilistic setting.
We expect the connection to be made by information geometry where Bayesian inference can be understood both using gradient descent and as a kind of parallel transport.
In other words, it is a way to unify both the physical formulation of physical formulation of system as done through the differential equations in cybernetics and also the probabilistic formulation of the systems as done in Bayesian mechanics.

1:04:24 _Daniel:_
Just two quick notes on this.
First, the growth and deak construction.
Shauna Dobson spoke about this in the Math Art Guest Stream in the context of the evolution of art and other areas in math and philosophy over the last hundred years with this progressive swarmification sheafification of self.
So that's really cool to see.
And then we expect the connection to be made.
What we expect is what we prefer, and then what we expect prefer is shaping our action selection to realize it.
So again, once we, as mentioned earlier, understand that systems act in order to make their expectations realized, we see that these kinds of expressions are more than just the expression of a belief, they're also in some ways an action imperative.
Dean, any thoughts?

1:05:29 _Dean:_
I'll just start there and wait for Toby to come on because I could literally have a field day.
I'm at the circus, the carnival and every single theme park in the world when it comes to this stuff.

1:06:04 _Daniel:_
All right, now we get to seven one three compositional, cognitive, cartography sailing, the three C's.
Ali, what is this section about?

1:06:23 _Ali:_
In other words, the topus theoretic developments sketched so far may provide a suitable setting in which to understand the neural basis for navigation and help explain how, ostensibly spatial navigation processes and circuits are invariably involved in more abstract problem solving.
Atopos is not only a richly structured category of spaces or spatial types, but it can also be understood as a category as a categorified space itself.
But an important notion here is that under the free energy principle, there's a close relationship between beliefs about the geometry of an environment and beliefs about expected future trajectories in that environment.
So this is basically the idea behind successor representation of the cognitive map, which says roughly that the brain's representation of where it is is equivalently a representation of where it soon expects to be.
So under the free energy principle, and similarly, under the successor representation, the expected dynamics is a geodesic flow, which is determined by beliefs about the spatial geometry.
But crucially, these beliefs are not a static.
They depend on what the agent believes will happen.
And this has been suggested as an explanation for the predictive nature of the cognitive map.
In other words, if we don't take into consideration the uncertainty behind the information available to the agent, then we wouldn't get to formalize the behavior in a truly predictive way, because obviously there isn't any uncertainty to predict about and then compare the prediction with the actual data.
The cognitive map has its central locus in the hippocampus, which we may therefore understand as representing the base space over which the big topus is sliced.
And since changes of plan seem therefore to induce changes of base, we might see the functional connectivity of the brain as witnessing this mathematical structure.
And this particular claim, I believe, is maps perhaps perfectly onto Boujaki's theory of brain from inside out.
So Boujaki provides a kind of theory that sets the hippocampus as the agential center of all the cognitive tests that needs to be reconstructed from inside out, as opposed to just processing the coming data in a kind of purely computational unidirectional way.

1:09:58 _Daniel:_
Okay, continuing on, on the compositional cognitive cartography, there's some discussion about the internal universe of the topos, not just the Topos institute, but the concept and the way that the representations of the cognitive map are inherently context dependent.
Therefore, it fits naturally within the subjectivist metaphysics implied by the free energy framework, a topic that I know Ali is extremely interested in.
And Dean Ali, any other comments on this?
Slice?
Maybe we can start calling them a slice or a bundle instead of a slide.

1:10:50 _Dean:_
I think for most people, in context, geometry or geometric stability is usually the association, whereas geodesic flow, which was mentioned in the last slide is a lot more dynamic.
And I think that if we're going to talk about a composition like the flow of the piece of music that's now playing out, we have to think of this as both framed and filtered.
And so these sheaves allow for that sense of distribution, that movement part, I think, metaphorically of exploitation and exploration now being the two passengers in the HOV Lane and HOV Lanes in North America at least, are designated by a diamond.
So you can see how the geometry and the geodesic again can all be put together, and you're starting to build a picture in these different models and maps that you may be constructing great.

1:12:10 _Daniel:_
What would it even be, Ali?
Want to add anything more on the forwards and backwards, perhaps, and the compositional structure?

1:12:34 _Ali:_
So we can say that a collection of purely passive agents is no assemblage as well.
But in any case, the doctrines of approximate inference introduced in this thesis are inherently perceptual.
But the forward channel of a statistical gain points towards the environment predicting the expected incoming sense data, whereas the backwards channel points from the environment into the agent, terminating in the agent's most causally abstract beliefs one way in which we can incorporate action and thereby shape the framework of this thesis into a framework for active inference.
The forwards channel should predict not only sense data incoming from the environment, but also the actions to be taken by the agent.
So up until now in the dissertation, he has provided in quite elaborate detail how this kind of formulation of the bi directional channels can be used to reframe the perceptual side of active inference.
But as I mentioned earlier, he doesn't go so far as to integrate the action into this framework as well.
But of course, here is a potential way forward which we can deploy the same forward channel as being the actions to be taken by the environment because of the same directionality it possesses.
We therefore expect the compositional theory of active inference to have forwards channel rather so that an agent's sensorium depends on the configuration or quote unquote action that it has chosen.
And another very, in my opinion, significant point here is the substitution of the notion of markup blankets throughout the whole dissertation with the notion of polynomial fontors, because, as have been discussed in the previous chapters as well, Markov blanket doesn't provide a rigorous enough concept to be applied quite at least directly in category theory.
So polynomial functions substitute the well known notion of markup blanket as used in active inference literature to characterize basically the same thing or the interaction boundaries of adaptive agents.

1:15:44 _Daniel:_
Markup blanket used in the informal active inference literature, like everything we've been studying for the last few years, all of that casual light, airy, breezy we had fun.
Now it's time to formalize that.
And there's so much more we can say about backwards and forwards, but we'll just carry on.
7.21 active Inference there are some mentions about the resemblance between active inference and economic games in terms of they're both having lenses into the area or the arena of interaction.
And this line of inquiry naturally leads onto the consideration of multi agent systems.
Perhaps this can be investigated with poly algebras.
7.2.2 what is the type of a plan?
Perception and action are thus in general, the two dual ways in which a system can minimize its free energy change your mind, change the world.
Akin to the two degrees of freedom available in an autoencoder game discussed in the thesis a system that acts must necessarily be motivated towards some goal and in order to realize its goal, the system must enact a plan.
Dean, pick it up from here.

1:17:17 _Dean:_
At the very end of this section, Toby writes this prompts us to ask what is the form of this data and how can we incorporate it into the compositional framework?
In other words, what is the type of a plan?
These seem to us to be key questions for future work.
This prompted me to go and then we wonder why teachers struggle sometimes to necessarily remember what it was like to be the learner.
Because we can come up with a plan.
Because we've done the learning.
We're now the learned, right?
The learner now changes because of one tense present to past tense change.
Or why the plan that we put before learners removes all the critical work for self organizing.
This is the cost of being a teacher.
Because if we do the planning for somebody and I understand why we have to do it, because if they're walking into a space, we don't want them falling off jumping off cliffs necessarily and not having a soft landing.
However, we do need to talk a little bit about what is the type of a plan and what are the benefits and the costs of choosing to use that strategy going forward, especially if we're in the role of somebody who's supposed to be guiding, opening up worlds, horizons and all that other stuff.

1:18:49 _Daniel:_
Ollie, any other comments on this section?

1:18:55 _Ali:_

1:18:58 _Daniel:_
So that's very interesting in light of, again, the statistical, numerical, quantitative way that we've approached policy selection as inference planning as inference action and inference.
What does it mean to differentiate this choice?
Okay, reinforcement learning, open games and ecosystems.
Ali, any summary here?

1:19:40 _Ali:_
But the standard algorithm for gaining an optimality for policy selection is usually called backward induction in reinforcement learning, or Akas dynamic programming.
So namely, backward induction is structured according to a similar bi directional pattern, or the optic pattern to that of both Bayesian inference and reverse differentiation, and that MDPs themselves fit into the associated general framework of open games.
So in the informal active inference approach to MDPs, the system in question counterfactually evaluates policies using a backward induction like process, accumulating free energies in order to score them.
Now, in this process, it is this process that results in the prior that we're all familiar with in active inference context, which is then updated by the agents inference process.
But future work will need to untangle this not of interrelated bi directional process, in other words, how we can explicitly determine in what way those kinds of processes, although being quite in a quite different opposite directionality, can be unified into a unified framework.
So we hope that having done so, we will show how the whole picture emerges and how it relates to the developing geometric or diegetic framework in categorical cybernetics, possibly involving the further development of our notion of cilia.

1:22:02 _Daniel:_
Continuing on with reinforcement learning, open games, and ecosystems.
Since the free energy principle underlying active inference asserts a certain informal universality, we might also hope that the satisfactory development of compositional active inference might exhibit a universal property that any other doctrine of cybernetic systems factors uniquely through it.
There's some discussion of multiagent systems and their implied global search.
Casting this account into the emerging framework of compositional active inference will point towards a bridge to multiagent reinforcement learning.
The resulting general account of multiagent intelligence will encompass both reinforcement learning and active inference, allowing us to understand their relative strengths and difference.
We hope that one distal outcome of the work will be a new and beneficial understanding of corporate activity, sometimes called organizational cybernetics or metagovernance.
We should expect any framework resulting from this work to capture existing models of collective active inference, such as recent work on spin glasses or ant colonies.
Any other thoughts on this?

1:23:26 _Dean:_
It's the work that I did essentially for ten years.
And so I think that everything that you're seeing here may become a new model that can be optioned into in terms of how you would.
Want to structure your learning.
So I think this is really important stuff.

1:24:08 _Daniel:_
7.3.
The mathematics of Life we move on to consider the relationships between compositional active inference and the contemporary mathematics of life.
We hope that compositional active inference may supply part of the story of a modern theory of autopoiesis the ability for life to recreate itself.
So just some brief notes on topics that are near and dear to us as we get close to the end.
7.3.1.
Bayesian mechanics and the free energy principle.
Recently it has been suggested in various venues citation 53 and 54 Karl Friston 2019 a free Energy Principle for a Particular Physics and fort.
54 Par DeCosta and Friston Markov blanket's information geometry and stochastic thermodynamics that the free energy framework provides a universal way to understand the behavior of adaptive systems.
Bayesian mechanics promises to build upon the nascent understanding of random dynamics via inference.
245, 245 dalton's activity Bell towards a Geometry and Analysis for Bayesian Mechanics and Ramstead et al.
On Bayesian mechanics, a physics of and by beliefs.
Also check out Livestream number 49 to supply a new theory of mechanics for statistical systems.
The present formulation of Bayesian mechanics is constructed using mathematical tools from physics, but not yet the kinds of compositional tools promoted in this thesis.
We expect that developments along the lines sketched here will unify the ongoing developments of Bayesian mechanics with the new synthetic understanding of mathematical physics by casting all dynamics as abstract inference.
We should also expect this line of inquiry to begin to quantify the persistence of things and imbue much of physics within elon vital with a vital energy.
Any thoughts on this?

1:26:26 _Dean:_
I think that the relation and the translation are kind of the on and through of this part of where the Bayesian mechanics and the free energy principle help us understand that there is a statistical game that's also strategic.
Again, I'll be interested to talk to.

1:26:58 _Daniel:_

1:27:13 _Ali:_
So the emerging biosymiotic reconceptualization of life explicitly acknowledges the importance and universality of communication in context, proposing that in any such situation, the interpreting system necessarily has an internal representation of the external world, so to speak, its own belt, which is updated by interpreting incoming signals.
We can in principle reconstruct the external world by understanding it as that which a collection of systems agrees about.
Perhaps then, the shared universe, as determined topus theoretically of a fusion of active inference agents is a good model of this semi sphere.
It seems therefore, that mathematics resulting from our work on internal universes and their interactions and more broadly, many of the formal ingredients of compositional active inference is well aligned with the informal structures of biosymiotics, and so it may be desirable to reexpress biosymiotics accordingly.
In doing so, perhaps the mathematics of a modern Bayesian subjectivist metaphysics will be found, for instance, by expressing communication and its phenomenology as a geometric morphism, a generalized base change between agents internal universes.
And it might be worth mentioning here the work of people like Terrence Deacon and also Karen Broad's agential Realism.
Because in Terrence Deacon's work, and particularly in his book called Incomplete Nature, he provides a kind of nested hierarchy.
Of how various kinds of informations as provided to biological organisms are structured in a nested, hierarchical way that would allow the agent to distinguish the purely informational data as opposed to the semantic data that is, in the innermost level of the nested hierarchy.
And also, Karen broad's agential realism provides this notion of intra action, which allow the agent or the system of interest to co constitute itself via the very interaction with the environment.
So it's not just pure interaction between the system and its environment, but rather both the agent and the environment co constitutes themselves through the intra action.
So it might be worth exploring some of these ideas with Toby as well.

1:30:21 _Daniel:_

1:30:24 _Dean:_

1:30:27 _Daniel:_
And the final section Fundamental Theory future work connected to this thesis need not only be an application.
A number of purely theoretical questions raise themselves too.
So for people who we could already hear in the live chat in the YouTube comments complaining that this was too practical, too application oriented, don't worry.
There's also some theoretical questions that raise themselves so first, geometric methods for structured belief updating the mathematics of belief is in large part about replacing definite points with Fuzzier distributions over them.
In fact, this PDF copy error with a fuzzy interpretive system allows the word to be read by a human independent type theory.
We replace points with terms.
Non dependent terms are exactly points.
So a type theory with belief should somehow encompass fuzzy terms.
We might well want to express beliefs about things whose identity we are not quite sure.
Seven four two dynamics.
Chapter five supplies the beginnings of a compositional coalgebraic theory for open, stochastic and random dynamical systems in general time.
And we hope that this theory could provide a home for a modern account of nonequilibrium systems.
Home, home on the state space.
And seven four three computation.
A new understanding of computation may follow the semiotic understanding of information processing that we propose above.
Perhaps we could say more precisely that computation is the dynamics of semiosis.
The time is right for such a reconceptualization, as human made systems increasingly move away from von Neumann architectures towards more biosimilar ones such as Mem risters optical processors, Neuromorphic technology, graph processors, or even many core and mesh based evolutions of classical processors.
So some absolutely fantastic theoretical avenues to pursue.
Any of you want to comment on some of these avenues?
Dean, please.

1:32:43 _Dean:_
He says here, chapter five has supplied the beginnings of the composition of Coalgebraic theory for open, stochastic and random dynamical systems in general time.
Me being a time guy.
That's cool.
And we hope that this theory could provide a home for a modern account of non equilibrium systems with category polynomial functions, applying a satisfactory account of these systems.
And then I'm going to slow down because this is the part that I really like.
Interfaces in brackets, I e, the boundaries across which information flows along and in the word along, there's the word on in the middle, which they compose and through which they interact, and me being an on and through being the same thing.
This was fantastic confirmation of that in a dynamic sense.

1:33:43 _Daniel:_

1:33:49 _Ali:_
And also, again, I think some of the work done by Bob Coke and his colleagues regarding the Bayesian quantum inference and especially proposing a kind of string diagrams in the sense of using category theory to explore the whole theory of the quantum Bayesian inference.
I believe it maps unto this sense of dynamics as provided by Toby in the final pages of his dissertation.
In the case that in the basing quantum inference, it is also a question.
Of how to provide the exact time evolution of each state or each agent.
Not strictly in a linear sense, but both in linear and sorry in the predictive and also the retroactive sense.
In other words, by taking into account the whole arrow of time, not just a particular instant or particular moment of it.
So in the sense, I think the discussion of non equilibrium systems, which is still an underexplored area of physics, by using category theory, can help to unify or at least make connections between these kinds of predictive models as used in classical physics and also some of the retroactive models as recently proposed in quantum Bayesian theory.

1:35:47 _Daniel:_
And so we couldn't escape without showing at least a little bit of a hint of what realistically much of the dissertation looks like.
So next time we're going to jump into the thick of it.
These kinds of equations and diagrams are what you're going to find when you unpack the dissertation.
And of course, there's so much to add and we did so much work on just scratching the surface of what these diagrams are and how they actually convey formality in category theory.
And it's going to be great to work and talk together on them.
And with Toby, where does that leave us, fellows?
Dean with the pre penultimate thought and then Ollie?

1:36:48 _Dean:_

1:36:54 _Ali:_

1:36:58 _Dean:_
I think it's going to be a lot more sophisticated and there's going to be a little bit more work to do, but I think at least we've started down a path that hopefully we've piqued your curiosity.
As the last question says, what are you still curious about?
I think there's a lot coming up that should be pretty good for those that want to really dig now into the real formalisms and the real structure of this.

1:37:39 _Daniel:_
Ali?

1:37:45 _Ali:_
So I think it's really a good mark of an influential work, be it dissertation or a book or paper or any other kinds of academic publication to peak people's mind, to explore in even some unexplored areas and try to connect the dots in particular in the category theory sense, in a very rigorous, well typed and even insightful ways.
And maybe some exciting developments and results can emerge from these kinds of dot connections.

1:39:08 _Daniel:_
I have so much gratitude for the whole category theory team, not just the sheaves around Toby that enable and scaffold this work, but also the way that we were able to collaborate over the last months and in the bigger picture, maybe the end of a chapter.
We just finished chapter one or chapter zero, and that's really what the dot zero is.
So we were in the dot.
Now we are bringing the dot zero to a closure.
Soon we're going to jump into the dot one and the dot two with Toby and even that in some other nested scale is AOO or a dot zero.
So thank you again, Ali and Dean et al.
Till next time.

1:40:08 _Dean:_
