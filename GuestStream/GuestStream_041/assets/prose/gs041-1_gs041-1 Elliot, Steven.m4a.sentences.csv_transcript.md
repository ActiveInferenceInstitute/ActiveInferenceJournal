00:00 _Daniel Friedman:_
Hello and welcome, everyone, to the Active Inference Institute.
This is ActInf GuestStream number 41.1 on April 25, 2023.
We're here with Elliot Murphy and Steven Piantadosi.
This is going to be quite a discussion.
We will begin with opening statements from Stephen and Elliot.
Elliot will then lead with some questions, and we'll have an open discussion at the end.
So Stephen, please, thank you for joining and to your opening statement.

00:30 _Elliot Murphy:_
Cool.

00:36 _Steve Piantadosi:_
Hi.
So I'm Steve Piantadosi.
I'm a professor in psychology and neuroscience at UC Berkeley.
And I guess part of the reason that we're here is that I recently wrote a paper on large language models, in part trying to convey some enthusiasm about what they've kind of accomplished in terms of learning, syntax and semantics.
And in part pointing out, I think, that these models really change how we should think about language, how we should think about theories of linguistic representation and theories of grammar.
And likely also theories of learning.

01:13 _Elliot:_
Awesome.
Yeah.
So I'm Elliot Murphy.
I'm a postdoc in the Department of Neurosurgery at UT Health in Texas.
I read Steven's paper with great interest.
I did a lot of people there were some areas of convergence, but the the things I want to kind of focus on today in responding to Steven and kind of probing are to do with areas of divergence, maybe.
So Steven's paper is based on the idea that modern machine learning has subverted and bypassed the entire theoretical framework of Chomsky's approach.
So I wanted to kind of respond to some of these main arguments and some other related arguments in the literature that some folks listening might have some insight and thoughts on.
So it's a very common criticism to say that large language models just predict the next token, which is obviously a bit of a cliche, right?
It's not quite true.
They don't just predict the next token.
They also seem to confabulate.
They seem to hallucinate, they maybe lie.
They randomly provide different answers to the same question.
They seem to stochastically mimic language like structures.
They sometimes correct themselves, sometimes when they shouldn't.
If you push them a little, they kind of change their mind sometimes.
In fact, if Fox News is currently looking for a replacement for Tucker Carlson, they could do less.
They could definitely do worse than using Chat GBT if they're looking for a similar caliber.
So these models seem to do all sorts of wild things.
And over the past ten years, there's been a sequence of different systems developed, like where to vet, load bed, and each of them is based on a different neural net approach.
But ultimately, they all seem to take words and characterize them by lists of hundreds or thousands of numbers.
So the GTP Three network has 175,000,000,000 weights, 96 attention heads in its architecture.
And as far as what I know, maybe Steven can correct me here.
We don't really have a great idea of what these different parts really mean.
It just seems to kind of work that way.
Like attention heads in GPT-3 can pay attention to much earlier tokens in the string in order to help them predict the next token.
But the whole architecture from start to finish is kind of engineering based motivations.
And I always kind of wonder, what about all the models that kind of failed from these LLMs, from the different tech companies?
It's like these companies often seem to make it seem like they have these models that really work very well straight out the box.
And they all seem to be named after some kind of famous artists, right?
They have daly after salador.
Dali they have DA Vinci.
Maybe pretty soon one of these companies will release a large language model called Jesus or something, I don't know.
But they always say, here's our new foundation model.
It's called Picasso.
It's the first one we tried.
It works just great, no problems, straight out the box.
But I always wonder, what about all the other black boxes that have kind of failed every time?
There doesn't seem to be a very open and clear structure to the kind of scientific reasoning behind selecting one model or another.
But again, I'm open to be corrected about that.
So even basic language models do pretty well on basic word prediction.
So the issue is whether these tools provide any insights into traditional psycholinguistic notions like grammar and passing.
So this is really why I kind of prefer the term corpus model rather than language model, as suggested by people like Sarba Veris.
So it's been pointed out that no one really thinks LLMs tell us anything profound about Python when they learn Python code just as well as natural language.
But Python is a symbolic language with a phrase structure grammar.
And nobody says LLMs are unveiling the secrets of Python, right?
So just to put various here, he says if an models can be construed as explanatory theories for natural language based on their successes on language tasks, then in the absence of counterarguments, they should be good explanatory theories for computer language as well.
Therefore, successful ann models of natural language cannot be used as evidence against generative phrase structure grammars in language.
So corpus model is really a more appropriate term for other reasons too.
People like Emily Bender and some others have shown that features of the training corpus in fact, I think Steven cites this, you cite this in your paper, actually, as a limitation.
They show that features of the training corpus can heavily influence the learning process.
So it's been shown that the performance of large language models on language tasks is really heavily influenced by the diversity of the training corpus.
But natural language itself is not biased, right?
It's just a computational system.
Human beings can be biased in what they say and how they act.
But natural language itself isn't biased, right?
So large language models, therefore it seems difficult for me to agree that they are being subject to all sorts of biases.
They therefore can't really be models of language, they're models of something else.
So just to kind of wrap up this argument, even though LLMs are clearly exposed to vastly more linguistic experience than children, again, this is something else that Steven concedes and talks about in his paper.
Even so, their learning outcomes may still be relevant in addressing what grammatical generalizations are learnable in principle.
So I do agree with this statement here that in principle they can tell us something about learnability rather than things like broad acquisitionist frameworks.
But that's about as much I think you can maybe say right now showing that some inductive biases are not necessary for learning is not really the same thing as showing that it isn't present in children.
So there's been a long debate about whether negative evidence and instruction and correction and feedback during language learning are necessary or even useful for infants and children.
But right now I kind of agree more with Yejin Choi and Gary Marcus and others who've highlighted how LLMs are currently very expensive to train.
They're clearly an example of concentrated private power in the hands of a few tech companies.
Their environmental impact is massive, and many of the people have been less constrained and conservative in their assessment here, much less so than Gary Marcus and eugen.
So Bill Gates recently wrote that Chat GPT is the biggest tech development since the graphical user interface, the GUI.
Henry Kissinger wrote in February in the Wall Street Journal that as Chat GBT's capacities become broader, they will redefine human knowledge, accelerate changes in the fabric of our reality, and reorganize politics and society.
Generative AI is poised to generate new forms of human consciousness.
So very radical claims happening at the moment.
And I do wonder if sometimes the AI hype may have seed into certain portions of academia, potentially a lot of grand claims being made.
But I think more concretely.
Just to put it back to Stephen here, I wanted to maybe raise the issue of there's a critique by Rosky and Beaumont that I think he's read on Lingbuz.
I think you saw on Twitter that you don't like the response they gave because the objection that they made is that science is an example of deductive logic.
Your objection is that science isn't deductive, it's inductive.
Right, but I think their general point might be more accurate, namely that you can't use the fact that language models do well predicting some linguistic behavior in humans and some neuroimaging responses.
You can't use that alone to claim that they can yield a theory of human language.
So in your paper, Steven, you know that it seems that certain structures work better than others.
The right attentional mechanism is important, prediction is important, semantic representations are important.
And that's what we can glean currently based on these models.
Right?
But so far that's really all I've been able to glean in the literature.
I'm not sure if you have more insights here.
So Rosky and Beaumont used the example of poor prediction, but strong explanation explanatory power and not predictive accuracy forms the basis of modern science.
And I want to explore this a little bit later maybe, but modern language models can accurately model parts of human Lagrange, but they can also perform very well on impossible languages and unnatural structures that humans can't learn and have great difficulty processing.
And I know you're familiar with these criticisms, right?
But you're definitely not alone here at the same time.
So Ilya Sutskeba, the chief scientist at OpenAI, he said in an interview recently, what does it mean to predict the next token well enough?
It means that you understand the underlying reality that led to the creation of that token, which is quite divergent from a lot of more conservative claims in the literature here.
And also, I would just say in response to that, that different components of science can be either inductive or deductive, right?
It's not really in either or.
You have an existing theory, you formulate hypothesis, you collect data, you analyze it.
That's kind of a deductive process.
But there's also cases where you start with a specific observation, you find some patterns, and you induce general conclusions, right?
And then there's abduction, where you magically invent hypotheses and reduce the hypothesis space.
You wouldn't really say that deductive reasoning is unscientific or inductive reasoning is unscientific, or abductive reasoning is unscientific, right?
These are all just different ways of doing stuff.
In your paper, you give the examples of using models to predict hurricanes and pandemics as being examples of stuff that is as rigorous as science gets.
And then you employ your reader to conclude that the situation is no different for language models.
But I guess for me, the issue is that models predicting hurricanes are not in the business of answering the question, what is a hurricane?
Right.
Models accurately predicting the weather are very accurate, but they're aligned with the meteorology department, but they're not a substitute for it.
So I guess I'll just hand it over to you.
Yeah.
Okay.

10:38 _Steve:_
Well, there's a lot there.
I guess I could start just by saying that I agree with many of these criticisms about these models being controlled by one or two companies.
That being very problematic.
They have all kinds of biases that they've acquired because they're trained on text from the Internet.
That's hugely problematic.
I certainly agree that there's things, at least at present, that the models don't do well.

11:09 _Elliot:_
Right.

11:14 _Steve:_
So I think it's easy to find examples of questions and problems that will trip them up.
I think why I've been excited about them, though, is not necessarily in those terms, right.
But in terms of performance on language, specifically syntax and semantics, I think they're far beyond kind of any other theory in any other domain.
Right.
So there's no other theory out of linguistics or computer science which can generate long, coherent, grammatical passages of text.
And so kind of admitting all of their problems as tools or things which are deployed by companies.
There's still this question of how are they at dealing with language?
And I think this is where a lot of the enthusiasm comes from, is there really hasn't been anything even remotely like them in terms of linguistic ability.
And that's the thing that I think is exciting.
So, yes, I agree with a bunch of these things you started with.
But nonetheless, I think in terms of syntax and semantics, there's just no other theory which is comparable to them.

12:31 _Elliot:_
Let me push that back, then.
Right.
The main objection from a lot of people I've spoken to in departments of linguistics who like a lot of the general thrust of your paper is to really say, well, you're right.
They do a wonderful job accurately modeling all aspects of a lot of aspects of syntax and semantics.
However, I don't know of any real just like Chomsky talks about facts about language, which is an old fashioned notion, but I really think that's kind of an important notion, too, right?
Like, is there some discovery about language itself that LLMs can uniquely provide?
So, like, if LLMs made some prediction about, let's say you have sentence structure type X being more difficult to process than sentence type Y, and this is a unique prediction that only they'd generated.
And no human linguist Chomsky, Holmes, Dean, Aja, none of these people had ever predicted that before, but it turns out to be true.
You do eye tracking experiments.
You do all sorts of different behavioral experiments, and it turns out, oh, after all, it turns out to be true.
This is a new insight about language processing.
It's a new insight about language behavior.
I just wonder I'm not saying that this is not possible in principle, because it might happen in the near future.
But that's, I guess, for me, the crux of why a lot of linguists speaking up, speaking on behalf of the entire linguistic community here.
I guess that would be one of the main objections.

14:01 _Steve:_
Yeah.
I think of the insights they've provided as kind, free energy principle.

14:08 _Elliot:_
Right.

14:12 _Steve:_
So I think about these things like the power of memorizing chunks of language, right?
So they seem to be very good at constructions, for example.
And there's lots of linguistic theories, Chomsky's in particular, which are about trying to find kind of minimal amounts of structure to memorize, right?
Trying to derive as much as possible from some small set, some small collection of operations.
And I think that hasn't gone well for those theories.
Right, whereas this goes really well.

14:43 _Elliot:_
Right.

14:45 _Steve:_
So if we think about something which has the memorization abilities, if we think about theories of grammar, for example, which build on humans really remarkable ability to memorize different constructions or different words, tens of thousands of words, tens of thousands of different constructions sorry, tens of thousands of different idioms.
Maybe our theory of grammar should be integrated with that, and they're in some sense a kind of proof of principle that that kind of approach can work well.
Right.
Can think about making other types ActInf prediction with them, some of which people are currently doing, but, for example, trying to use them to measure processing difficulty, measure surprisal, for example, from these models, their surprisal measures are much better than, say, context free grammars or other kinds of language models.
And then it's an interesting question how those surprisals or predictabilities relate to human processing.
Right.
And it may capture some of it, or might be nonlinear, or it might only capture a little bit of it or whatever.
That's an interesting kind of other scientific question.
But I think in principle, they can make predictions about, for example, the connections between sentences.
So in the paper, I gave this example of converting a declaration into a question in ten different ways, right?
And presumably when GPT or something is doing that, it's finding ten different questions, which are all in some way related kind of nearby in the model's underlying semantic or syntactic space.
And so those kinds of things are of the type that I think some linguists might want, which is here's some hidden connection between sentences or their structures.
But as far as I know, they haven't been evaluated empirically yet.

16:33 _Elliot:_
Right?

16:36 _Steve:_
Yeah.
These kinds of models are only a few years old, so I think it's reasonable to be excited about them, even though this kind of work hasn't been done yet.

16:39 _Elliot:_
No, that's right.
No, totally.
That's the right perspective to take.
But I think this gets to the issue of the you mentioned surprisal.
You mentioned Lenability LMS learn some syntax, but they do so with, obviously, way more data than infants do, such that observations of potential structure in and of itself is not a refutation of the poverty of the stimulus.
Well, the weaker version, I should say, of the property of the stimulus argument.
So the mere fact that LMS can do what they do without grammatical priors is very striking, I agree.
And in fact, you wouldn't have predicted that maybe five or six or seven years ago, but it doesn't yet invalidate the claim that humans have such priors, and we bring those priors with us.
So in order to see if computational linguistics can constrain hypotheses and theoretical linguistics, which I think it can do, by the way, this needs to be done with careful experiments in which different learning parameters are controlled and gigantic language models like GPT-3 are basically useless here.
So this gets to some of Tar Linson's complaints that we need something like a baby LM project, which I know you're interested in, where we have more ecologically valid training sets.
You make the prediction in your paper that some structure will be learned from that.
I suspect you might be right there.
But even so, even with the Baby LM challenge, there's still the kind of nontrivial issue of addressing more traditional issues, like when do kids start to generalize based on the amount of current input, based on different factors cross linguistically?
And that requires just traditional psycholinguistics and language acquisition.
So LMS do care about things like frequency and surprisal, as you said.
But there's a really nice paper by Sophie SLATSon, Andrea Martin, a really beautiful paper that I think you may have seen that shows very nicely that distributional statistics can sometimes be a cue to moments of structure building, but it doesn't replace these notions pertaining to composition.
So I'll just read a quote from Chomsky 57 which sounds a lot like what Slats and Martin say.
Despite undeniable interest and importance of semantic and statistical models of language, they appear to have no direct relevance to the problem of determining or characterizing the set of grammatical utterances.
I think that we are forced to conclude that grammar is autonomous and independent of meaning and that probabilistic models give no particular insight into some of the basic problems of syntactic structure.
So that second hedge of the second sentence turned out to be incorrect.
But it's true that what Chompsey said of available stat models in 57 is no longer accurate when applied to models today that can make abstract generalizations about novel strings and distributional categories, as you've mentioned.
Right, but the performance of a single model does not provide direct evidence for or against the endability of a particular structure.
Given the vast distance between any computational model available today and the human brain, model success does not mean that the structure is necessarily learned, and model failure also doesn't mean that the structure is not.
Lenable right, yeah.

19:42 _Steve:_
I think it's maybe worth unpacking kind of a couple of different versions of learnability arguments that people have made, because there have been very, very strong kind of impossibility claims coming out of kind of Chomsky's tradition that were never claims about the amount of data that was required.
They were claims about the logical problem of language learning and that it was just impossible.
It was impossible without having kind of substantial constraints on the class of languages or the class of grammars that you would acquire.
And people for a long time have been arguing against that version of things.
There's old work by Gold, and then there's whole kind of grammatical theories of acquisition built on that tradition that worry a lot about the kind of order in which you traverse through different hypotheses and consider different options and things.
And my favorite reference in this is this paper by Nick Chader and Paul Vitani called something like Ideal Learning of Natural Language that basically shows that an unconstrained learner could, with enough data, acquire the kind of generating rules or the generating grammar just from observing strings.
Right, but that paper was really in response to this huge body of work that was arguing that learning from positive examples, so from just observing strings was logically impossible, right?
Of course, people in Chomsky's tradition really liked that form of argument because it was one that said you had to have something innately specified in order for language acquisition to work.
It was like kind of a mathematical argument, right, that you had to have some kind of innate grammar or innate ordering of hypotheses or something.
And all of that just turned out to be totally wrong.
So if you move to slightly more kind of realistic learning settings, which Chader and Vitani do, then it turns out like an idealized learner can acquire stuff, and there's no statements about the amount of data that's required, even there, right?
That's the kind of pure logical ability to learn.
And that ability is what I think the big versions of large language models also speak to, right?
So Cheder and Vitani and other work kind of in that spirit is mathematical and kind of arguing in principle, but never created something which was really a grammar or a real kind of implemented language model.
So even a model which is trained on 100 million or 100 billion or however many tokens, even that kind of model, I think is relevant to that version of the debate and showing that language learning is not impossible from a very unconstrained space.
Okay, then there's a second version which is, can we learn language with the specific data that kids get, right?
And that's both amount of data and form of the data.
And so, for people who don't know, the Baby LM challenge is this thing to call it a competition, or.

23:04 _Elliot:_
I.

23:17 _Steve:_
Guess it is a challenge trying to get people to train language models on human sized amounts of data.
So that's something more like, I think there's two different versions, ten or ten or 100 million different words in the training set, which is like 100th or 1000th or something as big as these big AI companies are using for their language models.
And I think actually that's exactly the right kind of thing and exactly what the field needs, because you might find that on a child sized amount of data, you can essentially learn syntax, which I think would be the strongest argument against these poverty of stimulus claims.
You could alternatively find that maybe you can't learn very much.
Maybe you come up with a much crummier kind of language model, or it's lacking some syntactic or semantic abilities.
I actually think that the failures there are a little bit hard to interpret because kids data, when they're actually learning language, they get a lot more data than just strings of sentences, right?
They're interacting in an environment, so there's stuff in the world in front of them.
Their utterances are also interactive.
So you can say something and see whether your parent brings you the thing that you asked for, for example, right?
That's long been argued by people as an important cue in language acquisition.
So in the Baby LM challenge, there is an ability to train these models with kind of multimodal inputs.
I think you can give them as much video data as you want to give, but probably it's hard to kind of replicate exactly the type of setup and feedback that kids actually get.
So I don't know, I'm excited to see where that goes and how things pan out there.
I think that there is an interesting related question for large language models, which is understanding exactly what all of the data is doing.
So it could be that you need so much data for these models because they're effectively inventing some form of semantics internally, right?
So they're both discovering the rules of syntax and they appear to be learning quite a bit about word meanings.
And it's totally unclear, I think, how much of the data in these modern models is needed for syntax versus semantics.
My own guess, I think, would be that the syntactic side probably requires much less data than the semantic side.
Actually, a former student of mine, Frank Malika, and I wrote a paper a few years ago trying to estimate the amount of information a learner would necessarily have to acquire for learning the different aspects of language.
So you have to learn all the words and you learn their forms, you learn their meanings, you probably know their frequencies, you have to learn syntax.
And basically what we found in that analysis that was basically just a kind of backup, the envelope calculation for each of these domains is that syntax is actually very few bits of information.
It doesn't take that much information to learn syntax, whereas most of the information you acquire is actually for semantics.
So specifying 30 to 50,000 different word meanings, even if each meaning is just a few bits, that requires a lot of information, and probably each meaning is more than a few bits.

26:52 _Elliot:_
Right?

27:06 _Steve:_
So it could be that would make me guess that what's happening with large language models is most of their training data is about word semantics and you can think about other ways that kids get word semantics, right?
That's not just kind of co occurrence patterns in text.
But I agree, all of that is up in the air and really exciting to see what will happen.

27:24 _Elliot:_
Yeah, I know that some of the earlier results from Lindsay's lab suggests that at least restricted to ecologically valid training set sites, models seem to generalize linear rules for English, the ethno question formation, rather than the hierarchical rule, the correct hierarchical rule.
So I think there's a real sense in which the space of the correct syntactic prize and inductive biases really is yet to be really settled on.
But it seems, at least to me, pretty obvious that there has to be some.
So there's also some evidence that children in English, going back to this frequency issue, that children in English sometimes spell out an intermediate copy of movement in the specified position of the lower complementizer position of a long distance WH question.
So there's a thesis by Thornton and some other papers about this.
So they say, which person do you think who did that?
Rather than which person do you think did that?
So this is an interesting miss setting, because some languages do actually spell out these intermediate copies, but English doesn't.
So the kid makes the error in setting their grammar, but the frequency of the input is actually zero.
So our mutual friend Gary Marcus also has an argument against frequency determining a kid's output.
In the case of German noun plurals, a more regular form of the certain kind is preferred, not the frequent one.
And there's lots of examples like this.
So it's sometimes claimed that subject experience passives, where the subject is passively experiencing something, are very delayed in kids in comprehension studies until around eight, because they're not very frequent in the input.
But Ken, wexler and colleagues have gone through subject experience.
Like, who likes Mary?
And they discovered that these are as infrequent in the input as subject experience of passives.
But kids have no problem in comprehension studies of these questions, but they do have problems comprehending subject experience of verbal passives.
So frequency once again seems to be irrelevant, or at least it's not explanatory, right?
I guess it's not explanatory with respect to theory building.
So how can LMS help with these divergent cases when there's clearly something else going on besides frequency?
So, LMS, they seem to generalize just again, going back to this issue of the cases that you have in your paper, you show that they generalize the structure of polar screen ideas, which is obviously very cool, but the poverty of stimulus has never really been about not being able to learn language statistically.
I know you made that claim right?
But Chomsky's point in the 50s about statistical models of the day is not true of commercial LMS in 2023.
And that's correct, but we can't use that single point to undermine the entire generative enterprise.
Chomsky's basic point was that you could have a grammatical structure wherein every diagram has zero frequency and also fails to provide clearly interpretable instructions to the conceptual interfaces, so interfaces with other systems of the mind.
So, as you show in your paper, GPT mimics examples like clueless green ideas.
But again, this sentence yields over 150,000 results on Google, and it's discussed extensively in the literature.
It's able to mimic.
The fact that it can mimic this doesn't really tell us that much.
At least we cannot really say anything with much confidence.
So Abe University College, Dublin has this quote recently do not mistake your own gullibility for an LM's intelligence.
In fact, even young Lacoon wrote last year that critics are right to accuse LMS of being.
Engaged in a kind of mimicry.
And the example sentences from Chat GBT that you give in the paper actually don't do a good job because, as you say, it's likely that meaningless language is rare in the training data.
But they can either do it or they can't.
There's no middle ground in terms of giving us ten examples like this.
So you have cuddleless green ideas which are very different semantic objects from things like brown shimmering rabbits, white glittery bears, black shiny kangaroos, green glittering monkeys, yellow dazzling lions, red shimmering elephants, right?
These are all like semantically weird and a bit strange, but they're still like legal structures.
They're kind of meaningful syntactic semantic objects, right?

31:21 _Steve:_
I just said yeah, maybe I can respond to the first point first, right?
So you started off talking about these other kinds of acquisition patterns which maybe don't map directly onto frequency.
And I think it's actually a mistake to think that kind of modern learning models should be just based on frequency because they're clearly learning, like pretty complicated families of rules or constructions or something.
And I think it's very likely that when they're learning that they're in some sense searching for a simple or parsimonious explanation of the data that they've seen, right?
And how that caches out in a neural network is maybe complicated and depends on parameters and the specifics of the learning algorithm and those kind of things.
But I think I'd suspect maybe that it's likely to be the case that they're learning over a complicated set of things, right?
A complicated kind of family of rules and constructions.
And that means, I think, that their generalizations maybe like the examples of people that you gave might be kind of discontinuous in the input, right?
So sometimes you could imagine seeing some strings which lead you to a grammar.
And the simplest grammar of the data that you've seen so far is one which predicts an unseen string, right?
And if that happens, then you'll be taking the data, learning a representation which generalizes in some novel unseen way so far, purely because that generalization is sort of the simplest account of the data that you've seen to date.
Right?
I think that's sort of what linguists try to do, right?
Try to look at the data and come up with a theory of it.
And then sometimes that theory predicts some new phenomenon or some new type of sentence.
And so if they're learning over a sufficiently rich space of theories, then it wouldn't be unreasonable or unexpected for them to also show those kinds of patterns.
Now, whether they do or not, I think is still an open empirical question, right?
Because we have to train them on small amounts of data and test their generalizations and these kind of things.
But I don't think just the fact that humans do things which are not purely based on frequency is any evidence at all either way.

33:58 _Elliot:_
Right?

34:07 _Steve:_
Because once you're learning over rich and interesting classes of theories, then that is the expected behavior.
Actually, I had a paper about a year ago that I think you're familiar with, Yang and Pianta Dosi, where we were looking at kind of what happens when you give a program learning model strings from different formal languages.
So think of like giving a general model, just ten or 20 maybe simple strings that obey some pattern and then asking it to find a program which can explain that data, which often means finding some way of kind of programmatically writing down the pattern in the strings.
And in that figure, we have a paper which is really relevant to this point where the generalizations that that kind of model makes are, I think, kind of qualitatively like the ones you're describing for people right, where you can give them a small amount of data and it will predict unseen strings with very high probability, even though there's zero frequency in the training input.
Right?
And the reason it does that is that often the most concise computational description of the data that you've seen is one that predicts some particular new unseen output.
So that model is essentially an implementation of the kind of Chader and Vitani program learning idea that I brought up earlier.
But it's one that I think if you think about in the context of these arguments of kids saying unusual or unexpected things, that is predicted by all of these kinds of accounts, right?
Because as long as these things are effectively comparing an interesting space of grammars, then they'll show that kind of behavior, I think.

35:51 _Elliot:_
Okay, so I guess the argument would be that at least from the gender perspective, syntax is functioning separately, but it still maps to semantics.
It informs pragmatics.
Right?
So in the minimalist program, syntax is obviously minimalist.
It's very small.
It's just linearization and labeling.
They're the two only operations.
You have a linearization algorithm to central motor systems and some kind of categorization algorithm at the conceptual systems.
So Chomsky's architecture is kind of reliant on the process of mapping syntax to semantics, right?
It's form meaning regulation.
It's not just structure and it's not just meaning.
So LMS don't really have this mapping process, right?
Like, where's the mapping to semantics?
And if there is a mapping, what does the mapping process look like?
What are the properties of its semantics?
What the properties of the semantics place on their own sets of constraints on the mapping process, like they do for natural language?
Do these kind of constraints inform each other?
Is there kind of a back and forth process?
Right?
Like LLMs don't really seem to describe this form meaning pairing, which meaning which strings, for example.
Right.

37:11 _Steve:_
Sorry, are you saying that they don't have semantics at all?
Or are you saying that there's just not a clear delineation between how the structures get mapped onto the semantics?

37:17 _Elliot:_
Yeah, the latter.
Right?
So they clearly have potentially some kind of semantics.
I know you've argued for conceptual role theory being relevant here, right?
The rest of it may be a little bit more mysterious.
So in linguistics, there's a theory of the mapping process itself.
It's explicit and you can see it in action and you can test different theories of it in psych linguistic models and what have you, the actual regulation, the kind of constrained ambiguity, ambiguity in the sense of one word, multiple meanings or one structure, multiple interpretations, et cetera, right?

37:36 _Steve:_
Yeah, I mean, if you think they have semantics, then I think they have to have a mapping from the syntax of the semantics.
I agree.
Nobody really understands how they're working on any deep level, right?
So I agree it's not as clear as, say, in generative syntax and semantics, where you kind of write down the rules of composition and can derive a compositional meaning from a sentence from the component parts or something, right?
That's not how they're working.
Right, but I wouldn't take for granted that it has to be like that.
It could be that how they're working is actually how we work, right?
That everything is represented in some high dimensional vector space, and there's some complicated way in which that vector semantics gets updated with each additional word or whatever in a linguistic stream.
But I think it's clear that they have some kind of representation of the semantics of a sentence, right?
Like they can answer questions, for example, at least approximately.
I mean, it's not perfect, but it's not like an Ngram model or something, which really doesn't have semantics.
So I think that they're definitely representing semantics and updating that as they process language, it just happens not to look like these other formal theories.
And I guess I don't see why that's a problem, right?
Like those other formal theories could just be poor approximations or just totally wrong, right?

39:27 _Elliot:_
Yeah, totally.
I mean, there's also ways in which some of the formal theories in semantics are already potentially compatible with what some of these things are doing, right?
So another way to think about this is, well, LMS are compression algorithms, but natural language understanding is kind of more about decompression.
It's disambiguating meaning x out of meanings XYZ.
It's all about making inferences about meta relations between concepts that are not in the training data.
So some examples that Melanie Mitchell gives are things like on top of she's on top of a game, it's on top of the box.
All these kind of vary with context.
So there's a lot of other things that are going on.
Right, and I think you discussed some of those examples in your paper.
But the faculty of language is still not, at least again, under this theory of language, it's not about string generation, it's about this form meaning pairing machine.
So some semanticists in the gentle tradition even think all the risk to semantics is just and so paul Petroski's conjunctivist theory of semantics is that human semantics is just and that's it.
Which again, is very simple, elegant, it's interpretable, it's compatible with all the things that are maybe going on in your neck of the woods.
Right.
But regardless, natural language is still more compositional than things like formal languages.
Just to make a clear distinction that's been made.
They have a much richer compositional structure.
There's more stuff going on.
Maybe so.
It's been pointed out before that things like attention based machine mechanisms and transformers allow for combinations of discrete token bindings, which is more approximate to a merge like operator than simple recurrent matrix multiplication.
But the issue of binary branching, binary branching of merge, just to choose another example here to talk about the four meaning regulation, one principle, binary branching in merge is an interesting question, but Gemtogrammer has always been open to different origins and locations of this apparent constraint in syntactic computation.
Like where does it come from?
Maybe it's a condition on merge, maybe it's imposed by a smoke system, maybe it's a kind of prior.
Who knows?
And in fact, some more recent work in Gemtogrammer has tried to ground do away with all of the set theoretic assumptions of Mage, right?
Maybe set theory isn't the best way to model the gentle grammar.
Maybe Mario logical accounts are more appropriate.
There's lots of other recent ideas there which which are all compatible with Chomsky's approach.
Right?
In fact, one of the things that Chomsky likes the most is when he's proven wrong.
A lot of these theories are going against the poor mainstream minimalist architecture.
I think it's a very diverse, vibrant field.
The people who are Aja, Bornstein, Petrosky, Hajjibura, they disagree in fundamental ways with a lot of what the mainstream of Gemtive grammar would say.
But there's still more scope for disagreement.
But it's still compatible with certain core assumptions.
Right.
So a lot of David IJ's work, for example, kind of deviates in this core respect, but it's still trying to ground these intuitions in different formal systems.
I want to get your thoughts again on I mentioned Mitchell, right?
So Mitchell and Bowers 2020, they have this paper prior list recurrent networks, laying curiously, that I think you might be aware of, right?
So it's a really good example just to kind of get to the heart of the issue.
So recurrent neural networks have been shown to accurately model nonvade number agreement.
But Mitchell and Bowers show that these networks will also learn number agreement with unnatural sentence structures.
So structures that are not found in natural language and which humans have a hard time processing.
Right.
So the mode of learning for RNNs is at least for RNNs, qualitatively distinct from infant Homo sapiens.
Right.
So the story is Mitchell and Bowers show that while their LSTM model has a good representation of singular versus plural for individual sentences, there's no generalization going on, right.
They can represent at the individual level.
So the model doesn't have a representation of number as an abstraction.
What number is only concrete instances of singular versus plural.
So successfully predicting language behavior via LM or successfully predicting neural responses in a similar way is obviously great, and maybe we can get into that issue later.
But there's only one side of the coin here, right?
The other side of the coin is explaining why this type of behavior and not some other behavior, why this structure and not some other.
And that's maybe Chomsky's most important point, really.
Why this and not some other system?
So linguistic theory kind of gives you that other side of the coin, right, whereas LMS really don't.
So the Michelin Bowers paper does something that well, yeah.
So, like, take Yay La Crettez and Stanislaster Haynes work from 2019, right?
They looked at number agreement in an LSTM and found two specialized units that encoded number agreement, but the overall contribution to performance was low.
And then in 2021, Yakretz have this paper where they show that in their neural language model, it did not achieve genuine recursive processing of nested long range agreement, gender marking in Italian, I think.
Even if some hierarchical processing was achieved, as you've argued before, right, some hierarchy was lent.
It was there.
But the question is, is it the right mapping?
Is it the right kind of hierarchy?
They found that LSTM based models could land subject web agreement over short spans, one degree of embedding, but they failed at some longer dependencies.
And in their most recent paper, La Crete Satell with the Hayne showed that they evaluated modern transformer LMS, including GPT-2 Excel, on the same task.
And the Transformers perform more similarly to humans than Lscms did and performed above chance overall.
But they still perform below chance in one key condition, which is the, as I mentioned, the multiple embedding one, the difficult structures.
So the reason why I mentioned these studies is because it's not just to explore the limits of LMS, which is an interesting question, but consider work by people like Neil Smith at UCL, right?
He did work in the Polyglot, Savant and Neurotypical controls, comparing them.
So he investigated second language learning of an artificial language containing both natural and unnatural grammatical structures, like the Michelin Bowers paper.
Right.
The whole framework is natural versus unnatural.
And they found that while both the savant Christopher, the Savant, and the controls could master the linguistically natural aspects, only the controls could eventually handle the structure dependent unnatural phenomena, and neither of them could master the structure independent aspects.
So some weird rules where it's like you mark the emphasis on the third word of the sentence, things like that.
So they argue that Christopher's abilities are entirely due to his intact linguistic faculties, but the controls could employ more domain general kind of cognitive resources like tension control, et cetera, which is why they could deal those difficult processes.
But I just mentioned a minute ago that the LSTM in the Michelin Bowers paper approaches natural and unnatural structures in pretty much the same way.
So it's not a psychologically plausible model, I would argue, for whatever humans are doing.
And similar observations can apply to the limits of transformer models in Lacrete's way.
And all of these themes are like, right up, they're staying with us all the way to the present.
So another one of Tar Lindsen's recent papers that he posted a few weeks ago, looking at child directed speech showed that LSTMs and Transformers limited to ecologically plausible amounts of data.
Generalize, as I mentioned, the linear rules for English, right, rather than the abstract rules.
And in fact, more recent work from Lynson's lab last week looking at well, last year, I should say, shows that looking at garden paths surprisal does not explain syntactic disambiguation difficulty, right?
surprisal under predicts the size of the garden path effect across all constructions.
And this gets to this issue that you mentioned before.
Maybe surprisal is related to some aspects of syntax, but maybe not other ones.
It's a very non trivial issue that it's open to discussion.
It hasn't been settled yet.
But so Lindsey showed that garden path effects are just way more difficult than you would expect from me, unpredictability.
So another way of phrasing this argument is to quote a recent argument of chomsky's.
To get at this natural versus unnatural issue, he says, suppose we have an expanded periodic table that includes all the elements that do exist, all the elements that can possibly exist, and all the elements that cannot possibly exist.
And let's say you have some model, some artificial model that fails to distinguish between these three categories.
Whatever this model is doing, it's not helping us understand chemistry.
It's doing something else.
It's doing something for sure, but whether or not it's helping us understand chemistry is something separate.
And I know that you've said in response to some of these studies, I think you've said that in order to show that something is likely to be impossible somewhere in your paper, I think you say in order to show that something is impossible with normal bounds on false positives, you need to look at something like 500 independently sampled languages.
So you cite this in your paper, right, which you probably can't do.
It's not a feasible thing to do.
I'm not too sure that this really refutes the principled argument that I'm making here, right?
Because people like Mitchell and Bowers are making an argument about impossibility in principle, not in some kind of extensional sense, just like searching across the world languages to see, to prove across every single language that it is impossible.
It's a different argument whether it's impossible in some random language in the Amazon compared to actually impossible based on the principles of what the language system is actually doing, like what it can do.
So I would just say that all of us.

48:49 _Steve:_
That point is that you don't actually know what is typologically not possible, right?
So people like to say things like there's no language that does X.
Therefore we have to build that restriction into our statistical models.
But if it's not statistically justified that there is no language that does X, right.
If you've only looked at 20 European languages or something right.
That shouldn't motivate doing anything to the models, right.
If it's not a statistically justified universal, I think well, I think you're totally.

49:25 _Elliot:_
Right, but that just applies more generally to the social sciences and psychological sciences, right?
Like typologically very difficult to establish these things.
Right.
So I guess you're just kind of steal manual.
You're saying that the strong claim is very difficult to prove, right.
Like there is no language that has x.

49:49 _Steve:_
The strong claim that something is not allowed in natural language is, I think, very difficult to prove.
And I think that there have been lots of strong attempts, there's been lots of strong claims, often from generative syntax, about what all languages do.
And I think that people have been very good at finding kind of counterexamples to a lot of those things.
I cite this paper by Evans and Levinson, which actually I had heard for years about how no language does x and that's what we're using to construct our theories.
And that Evans and Levinson paper really kind of changed my mind about this.
Right.
That language is actually much more diverse than I think most Syntacticians will try to construct theories for or something.
Going back to kind of the beginning of what you said, I think we'd agree that you need language architectures which learn the things that kids learn and learn it from data that they learn.
And those architectures might be unlikely to be things like LSTMs or simple recurrent networks or whatever.
Right.
I think all of that work is very useful in kind of honing in on the right architecture.
So I'm just trying to remember all of the points you were making.
Oh, yeah.
But I think that there's a kind of flip side to this, which is that I think that the space of things people can learn is actually kind of underestimated.
There's this bias to say people can't learn X, Y and Z, but people, at least outside of language, have this really remarkable ability to learn different kinds of patterns, like the patterns you find in music or mathematics, for example.
We can learn sophisticated types of algorithms.
We can learn to fly a space shuttle or to tie knots for rock climbing or whatever, right.
There's all kinds of kind of procedural and algorithmic knowledge which is structural, that people are able to acquire.
And I think that that notion very rightly.
Kind of motivates looking for learning systems which can work over pretty unrestricted spaces, right?
You might say that.
Okay, well, language is different because language is a restricted space and it might be true that language is restricted, but it also might be true that the things we see in language come from other sources.

52:28 _Elliot:_
Right?

52:39 _Steve:_
It could be that language is especially pragmatic, for example, compared to music or mathematics.
Right.
And those kinds of pragmatic constraints are the things that constrain the form of language.
Or language is communicative.
It's probably more communicative than music, for example, and that might constrain the form of things.
As you know, this is a very old debate in linguistics about kind of where the properties of natural language come from.
And I guess what I'm trying to say is that there's one kind of perspective where you look at all of the things humans can do, even outside of language, all of the rich structures and algorithms and processes we're able to learn about and internalize.
And you say, okay, maybe language is like that, and then, yes, language also has some of these other funny little properties, but maybe those come from some other pieces of where language comes from.
Right.
We have pretty sophisticated pragmatic reasoning.
We're using it to achieve certain communicative ends.
You can find all kinds of kind of communicative features within the language system itself.
And so maybe some of these other properties are properties that have some other origin.
And that view, I think, could be wrong, but it's one that I think needs to be looked at to see if it's wrong.
Right.
I think it's been kind of dismissed by large chunks of linguists.
I've heard people say stuff like, oh, well, communication doesn't really explain anything about language, right.
And what they mean often is it doesn't explain the particular island constraints or something that they're working on.
There's all kinds of other things in language that communicative pressures probably do explain.
So I guess my pitch is always for kind of breadth in consideration of the forces that can shape language and not needing to put it all into some form of innate constraints or something like that.

54:30 _Elliot:_
No, totally.
And I think I think a lot of that stuff is is compatible with with the minimus program, because the minimus program wants syntax to be minimal.
It doesn't want it to be complicated.
It doesn't want it to be any more complicated than it has to be.
So you mentioned the curious properties, right.
So there are some other properties that need to be accounted for in any model of language that are I'll give you one example, right?
The setting of person features.
And these person features exhibit very nontrivial generalizations that do not seem to be accounted for via domain general learning mechanism.
So I'm citing here the work of Daniel Harbor queen Mary.
So, for example, the morphological composition of person, its interaction with number, its connection to space, properties of its semantics and its linearization, they all appear to be strong candidates for our knowledge of language.
Right.
What we mean by knowledge of language.
But on the other hand, we have things like case and agreement and head movement.
And these are all structural phenomenon.
However, they seem to resist a purely meaning based explanation in theoretical linguistics.
Right?
It would be great if syntax were nothing but a computational engine that builds structured meaning.
And that's the minimalist program, the goal.
But that's not what we actually find.
That's not in any actual minimalist, like, concrete model, any concrete minimalist theory.
The goal is just the program is language is perfect.
Okay?
That's the program.
Is that what we find?
No, obviously not.
No linguist actually believes that.
So it would be great if syntax was like that.
But I think the program is to look for perfection, but not always find it.
So case and agreement and head movement are morphophological phenomenon.
They're properties of the performance systems, what's called performance systems.
And so the minimalist program itself is really compatible with a lot of what you're saying about language.
Language.
There are aspects of language that can be perfected and optimized for communicative efficiency.
Absolutely, totally.
No doubt about it.
But where is that locus of efficiency?
Is it in the syntax itself, or is it some kind of extra linguistic system?
Is it in pragmatics?
Is it in sensory motor?
Is it in the speech properties of speech and phonology?
Probably.
I mean, who knows?
But I think all other things demand much more serious consideration into old fashioned notions like structure, dependence, compositionality, and what have you.
Things like that which you can maybe find somewhere in the literature.
But even just basic topics like quantifier, raising, extended projections, adverbial hierarchies, all of these things in the minimalist program can be extra linguistic.
They can actually be outside of syntax and very queer properties of the semantic conceptual systems, which are in themselves kind of domain general weird leftovers from ancient primate cognition, right?
That features of the way we pass events, the way we pass agents and patients, things like that, that's not human specific, but the way that syntax provides instructions to these systems, you know, probably seems to be.
So, you know, generative linguists have different theories of also Lagrange production too.
I'll just talk about language production based on whether we store Lemmers or whether we build words in the exact same way we will have phrase and sentences.
So I know that you make distinction between construction grammar and kind of generative grammar and the weight they place on memorizing constructions, various is just building things from the bottom up, from the ground up, right?
So in some generative inspired models, mechanisms which generate syntax structure make no distinctions between processes that apply above or below the word level.
There's no point at which meaning, syntax, and form are all stored together as single atomic representations.
Each stage in lexical access is a transition between different kinds of data structures, right?
There's meaning, there's form, and there's syntax.
These three features kind of commingle together and they don't always overlap.
Different languages realize them in different ways.
And so the basic definition of a word is just this weird multi system definition where lots of things, lots of different cognitive systems enrich the basis of every lexical item, right.
You have there's nothing like this, really, this enrichment process anywhere else in linguistic theory, right.
Or at least in what LLMs are doing.
So I guess I'll ask you, what is your definition of a word?
And what can LLMs really provide insights into wordhood?
Right.
Because if you don't have a definition of what a word is, then you're really in trouble.
Right.
We have to at least use LMS or artificial systems to inform what we mean by a word.
Or maybe we don't need that anymore.
I'm not sure.
What do you think?

59:14 _Steve:_
I'm not sure what you mean.
I don't have what is a word?
Why does that matter?
That's just a convention about how we use the term word.

59:25 _Elliot:_
Right?

59:27 _Steve:_
You could use lemmas or word firms or whatever.
That just feels like a conventional choice.
I'm not sure what's at stake there.

59:36 _Elliot:_
So how would you I guess I would say I agree word is a conventionalization our intuitive concept of word is often biased by orthography the way we put spaces between things.
Right.
I agree with that criticism.
Word in the intuitive sense is not really a scientific construct.
However, I guess let me rephrase my question.
How would you decompose the intuitive concept of word into something that is more kind of scientifically amenable or psychologically plausible?
Which is exactly what Gemtive Grammar tries to do.
By decomposing words into distinctive features, morphological categories, conceptual roots being merged with categorical features.
You get a concept and you merge it with a noun or a verb category.
To get a noun or a verb, different models make different predictions, right?

1:00:21 _Steve:_
Yeah, I think that general idea is likely to be right for large language models.
I think they kind of must have things that are kind of like part of speech categories, for example.
And I think that they kind of must be able to update their categories based on the language that they've seen so far.
Right.
GPT puts nouns and verbs in the right places, and to do that, you kind of need some representation of the nouns versus the verbs, and you need some ability to locate yourself in a string of other words and figure out if there's likely to be a noun or a verb next.
So I think that on that level, those kinds of properties of words are very likely to be right.
And there are also things which are very likely to be found kind of in the internal representations of these models.
I don't see how it could be any other way other than that, but as far as I know, that's not where the main debates or disagreement I think is.
Right.
I think all.
Theories of language have to say that there's different kinds of words that can show up in different places or something like that.

1:01:37 _Elliot:_
Okay, so how about the issue you mentioned communication, right?
And you're totally right when Trumpy says things like language is a thought system or language didn't evolve.
He's kind of being a little bit cheeky.
He doesn't really mean that.
He kind of means it in a very specific sense.
Right?
But when we say language is a thought system, what we mean is worth trying to get it an architectural claim.
So if you look at the architecture of the Minimalist Program, the syntactic derivation and the conceptual systems are literally different systems, right?
The conceptual systems take stuff from syntax and then does its own business with it.
And the CI systems have their own peculiar rules and principles, which is why thought and language are both similar symbolic compositional systems, but in different ways.
Only a subset of thought is properly called the CI Interface system.
Since the CI systems are, by definition whatever conceptual systems human have that can access and read out instructions from syntax.
And we don't know what they are fully.
They seem to have something to do with events and grammatical reference and definiteness.
They seem to be the main categories that language cares about conceptually, but we don't really know that's.
Kind of just a hypothesis.
Right.
But what we do know is that they don't seem to make use of color all that much.
So no language morphologically marks shades of color or other conceptual features like worry or concern.
Like no language morphologically marks a degree of worry or concern about an issue, but we do make use of epistemological notions like evidentiality and things like that.
So I guess what I'm saying is the Minimalist Program does a good job of trying to figure out which aspects of thought language is intimately tied to and which aspects of thought it's not tied to.
So the Minimalist Program allows us to kind of carve that up quite neatly.
And this is a much more nuanced framework than when Chomsky says language is thought.
Again, maybe he means it, maybe he doesn't.
But that's not what the actual architecture of his theory says.
It's a rhetorical device that is very useful and interesting to attract undergraduate audiences.
But if you look at actual theories that are coming out of the Minimalist Program, no one really believes language equals thought, right.
The language system seems to.
It tries its best to access and reformat and manipulate various conceptual systems, but it has its limits, right?
We know what systems, spell keys, core knowledge systems are hooked up to with respect to the syntax engine and which ones are not.
So this kind of gets back to the idea that lexilization of a concept seems to maybe alter it in some way.
It kind of imbues it with elements that are not there in the concept itself.
So if you lexicalize a concept, you suddenly transform it a little bit.
You give it a little extra, you sprinkle something else on top of it, and that seems to vary across different noun types.
But these are all, like, very clear architectural claims within geometry grammar that make very clear empirical predictions.
So, in other words, I guess what I'm saying is, all these neuropsychology studies that are often cited in a lot of work in this vein, what does it really show?
I think it shows that when language is damaged in the brain, it loses its particular sway or mode of influencing those systems.
But there's no real prediction from within the Gem to grammar enterprise that those non linguistic systems should be impaired or should suddenly shut down if the core language system is compromised.
Right?
In fact, if anything, that just emphasizes the principal divorce between the syntactic system and non linguistic systems.
Right.
So I think a lot of predictions here from the language and communication literature are kind of missing the point of the architectural claims.

1:05:10 _Steve:_
Daniel, do you want to go ahead, give a little bit of background there.
So there's these papers from EV Federenko and Rosemary Varley that are examining in part of them aphasic patients.
So people who have impaired linguistic abilities, basically showing that with impaired linguistic abilities, you can still have preserved kind of reasoning abilities.
So people like chess masters, chess grandmasters, for example, who are obviously very good at reasoning, might not have kind of intact linguistic abilities and then complementing that kind of patient work.
There's also work from Ed's lab showing that the parts of the brain that care about language are separable from the parts of the brain that care about other domains, even ones which seem kind of language like.
So things like music and mathematics tend not to happen in the language areas.
So EV and others have argued that this is basically evidence against the Chomskyan claim that language is the medium for thinking, right?
Because there's thinking that can happen in the absence of language, and the brain areas that care about language seem not to be the brain areas that care about thinking, I guess.
Elliot, you're saying that people don't really believe that.
They don't believe that distinction.
I mean.

1:06:56 _Elliot:_
Also, there's a lot of self contradiction even within these arguments, right?
So in your paper, you sometimes say that Chomsky thinks that language is a thought system, but then a few pages later, you'll say Chomsky also believes that syntax is some totally separate system from anything else, right?
Autonomy of syntax, et cetera.
Does Chomsky think that's not my contradiction.

1:07:17 _Steve:_
I mean, he said both of those things, right?

1:07:20 _Elliot:_
Exactly.
So therefore, you may want to ask yourself, does he really believe these things, or what is the prediction that arises from the architecture?
Right?
So just saying language is a thought system, what does that mean?
That doesn't mean anything.
It's just a very vague statement.
The question is, how exactly is language contributing to thought and how is it not contributing?

1:07:37 _Steve:_
Yeah, I think his claim is mainly evolutionary or something, right.
That this is the origins of the system, which I think is sort of equally hard to square with the kind of patient and neuroimaging data.
But if he doesn't think that, then he shouldn't say it or people will respond to what he said, I think.

1:08:01 _Elliot:_
Well, no, the argument is that language is a kind of thought system.
It regulates some aspects of thought and it yields some aspects of thought that are clearly unique to humans, but it's not intrinsically or causally tied to it.
The architecture of the system is very different from the kind of generalizations you can rhetorically evince from the architecture.
So, for instance, when you cite work from ephasic patients showing no deficits in complex reasoning, as you just mentioned, playing chess and so on, we would actually expect this under a kind of non lexicalist framework of Germany syntax, where meaning, as I said, meaning syntax and form.
Form just meaning anything that you can externalize language and all these things are separate features and separate systems.
Right.
The autonomy of syntax doesn't mean what a lot of people think it means.
It just means there are certain syntactic operations that are not semantic.
There are certain things you can do with syntax that you can only do with syntax and you can't do a semantics.
So this gets back to the difference between Petrovsky's theory that semantics is just and right, versus a lot of Syntacticians belief that there are certain peculiar, weird things you can do with syntax that are just syntactic.
So there is a divorce even within the kind of architectural framework.
So it's not too surprising that you also find that divorce at the neuropsychological level, I would say.

1:09:19 _Steve:_
Well, I think I would want a prediction of the language is thought evolutionary idea then.
Right?
So if you're saying that doesn't predict that thought relies on language, then I think whoever likes that theory should come up with some predictions about what that theory actually means.
I feel like those kinds of predictions are often really necessary for understanding the content of a prediction.
So sorry.
Daniel, your hands been up for a while?

1:09:59 _Daniel:_
No, it's all good.
Just kind of wanted to bring a breath in and an opportunity for anyone to ask any other questions.
But wow, thank you both for the many topics we have covered.
We'll have, in the last minutes kind of conclusion and next steps.
But Dave, would you like to ask a question or just give a short reflection?
Okay.
No, there are many comments in the chat, so I hope that both of you can read them on your own time to see what everyone added.
Where do we go from here?
As we roar into May 2023 and beyond, what can linguists large language model developers and users, cognitive scientists, what do you each think are some of the most fruitful pathways forward?

1:10:51 _Elliot:_
Well, I would say the most fruitful pathway forward is to really take cognitive psychology seriously.
There's a lot of nice work recently trying to align things like chat GBT Wolfram alpha plugins, the way that chat GBT can interface with different kind of modules.
The way of building a legitimate kind of aji system doesn't necessarily have to be psychologically reliant on the kind of modules that human beings have, but I think it will benefit from it.
So there have been some claims that large Lagrange models can maybe do all sorts of things, everything you like, but I think in the long run, it's most likely going to be the case that LLMs can do something very important and very interesting, but it's only going to be one piece of the puzzle.
So in fact, even OpenAI CEO Sam Altman said last week that what we can do with LLMs has really kind of been exhausted.
We need new directions, new avenues and so on.
I guess he was probably speaking to investors more than linguistic students here.
But I think he's also right.
LLMs can do something spectacular, but they're probably going to form a small part of the general AGI architecture, right?
If you want to think about AGI as a potential goal here, give me another example here.
So Anna even over, who's a very good cognitive scientist, she has a paper recently arguing for a kind of modular architecture for LLMs, which is a very nice framework, right?
It's very cognitively plausible.
It's exactly the kind of thing that we should be pushing for.
It's compatible with Howard Gardner's notion of multiple intelligences and so on.
But I think at the same time, just to finish this comment, there was a tech talk last week, I think, or maybe a few days ago, where a lot of this stuff can be conflated with AI Hype in unproductive ways.
So Greg Brockman from OpenAI, he gave one of these big Ted Talks where he showed different plugins that Chat GPD can do.
I mentioned Wolfram Arthur, right?
But there's also things like image generation, Instacart shopping, where you can get Chat GPD to buy you things and what have you.
And again, this takes you back to the idea that multiple subsystems can do different sub functions.
So Brockwinch also showed an example of giving Chat GPT an Excel file, a CSV file from an archive database of academic papers, where it just listed a bunch of papers and their titles and what have you, right?
And he said that using Chachi petite, it uses world knowledge to infer what the titles of the columns mean.
So it understood that title means the title of the paper.
It understood that authors mean the number of authors per paper.
It understood that created means the date of the paper submitted.
Right?
And because it's a Ted Talk, the audience gave this a standing ovation, right?
But the ability to describe labels on an Excel file is, I guess, nice, but I'm not sure you'd really call it world knowledge.
So I guess I would just say there's a lot of progress needs to be made alongside reducing anthropomorphism.
You have to have the right balance of it.
So, like I said, you have to have the right balance of psychologically plausible kind of modular architecture, but you can't have too much anthropomorphism because then you'll get carried away.
We have to find the right balance between modeling kind of human like modular systems, but not doing it to a degree that is a bit implausible or scientifically unhelpful.

1:14:21 _Steve:_
I think I agree with all that.
I'm really excited about these ways of kind of connecting language models to other forms of information processing, which does seem like what people have.
I've been very surprised at the things they are able to do just as language modeling.

1:14:49 _Elliot:_
Right.

1:14:56 _Steve:_
So different kinds of reasoning puzzles and things that they can solve I think is really fascinating and maybe will require us to rethink the relationships between language and thought and try to figure out a way of being specific about what it means for something to have a representation or to reason over that representation.
But ultimately, I think I agree that people have different modes of thinking about things and that seems important for intelligence.
I'm also super excited about the Baby LM challenge.
So I think on the kind of linguistics side, that's exactly the right thing of seeing how far we can get with smaller data sets, and maybe eventually after that trying to understand some more about the kinds of semantics.
That kids acquire and where they get it from and how kind of external semantics can inform language learning.
Or specifically, maybe grammar and syntax learning.
I guess my other path forward point would be that I feel like these kinds of models have really gone far beyond people's expectations for this kind of class of model, right.
Kind of ground up statistical learning, discovering patterns in text seems to give really pretty remarkable results.
And that for me, going forward, I think has just introduced a huge wave of uncertainty over theories.
So I think that our theories of basically everything in language for sure, but cognition, probably neuroscience, all of those things I think are going to be reworked when we really come to kind of understand the ability of really general kinds of learning systems like these.
So that makes it, on the one hand, kind of a bummer for past theories, especially theories which relied on learning not being able to work well.
But on the upside, I think it it makes it a very exciting time both for for AI and cognitive science and, and linguistics, where now there's these, these really, really powerful tools that, that seem like a qualitatively different size step towards human human abilities.
And I think kind of integrating them and taking both the kind of engineering lessons and the kind of philosophical lessons about how they're made and what kinds of principles go into designing intelligent systems.
I think that those things will really shape the field over the next five or ten years.

1:17:47 _Elliot:_
And also, I would just say in the context of broader themes here right, you're totally right.
I remember when I was reading about when Deep Blue beat Casperov was it the chess thing?
Right.
Yeah.
And there were some commentators who said, chess is over.
If an AI can beat a human, then it's game over.
What's the point in studying chess?
There's no need, it's boring anymore.
And I guess if AI has achieved seemingly everything that humans need to do to play chess, what's the point of playing it?
But I think, if anything, it turns out to increase the popularity of chess.
Right.
There are now many chess celebrities there's worldwide tournaments, and I would predict that the same is probably going to happen with language too.
LLMs do not mean it's the end of language.
No more language, no more linguistics.
I would actually push back and say maybe it would be the opposite.
The success of LLMs will increase general interest in linguistic theory due to their weird constraints and apparent limitations.
Right.
Because I would also say scale.
At this point, the chess issue scale is kind of definitely far from all that's needed.
What is lacking is an ability of LLMs to really abstract their knowledge and experiences in order to make robust predictions and generalizations and so on.
I gave some examples, but this mother's in the literature where it doesn't seem to really be good at generalizing, it can kind of mimic particular token types.
But I would guess my final claim would be that the language acquisition literature doesn't necessarily need LLMs, though cocktail scientists don't really need LLMs.
We could potentially me and Steven obviously disagree here, but I would say big tech companies profiting off LLMs, need LLMs.
Right.
They're the only ones that really do.
It may be the case that the mind is a very I will say the mind is a very diverse space.
It may be that there are certain forms of behavior and learning that might be captured by processes similar to what LLMs are doing.
So Stephen has given some interesting examples in his papers about magnetism and weird kind of rules of learning that are very domain general and very quick and very mysterious.
So maybe for those sorts of things, that kind of learning will be relevant.
But I still think it's unlikely that one of the candidates will be natural language, at least the way natural language works in its full glory in terms of the form, meaning, regulation and what have you.
So I guess it kind of reminds me of where you have this image of I saw John Wick chapter four recently, right?
And he has this there's this scene where he's walking in the desert and he's not sure if he's seen this guy that he wants to assassinate.
It's kind of like when you walk in the desert and you have an illusion of seeing an oasis because it turns out you're hallucinating, but then you realize that sometimes before it's too late that you actually are hallucinating.
You're not seeing an oasis, you're still in the desert.
And I think that's kind of maybe the situation we're in right now with linguistic competence of language models.
We have the illusion of linguistic competence, but you always see the illusion before you find the oasis.
Right?
So I think right now we're in the hallucinating stage of the desert where we're seeing potential sparks of linguistic competence, but it's still not very clear and unrebust.
We haven't actually reached the oasis yet.

1:20:57 _Daniel:_
Just a rapid fire question.
So see if you can give a short response.
So Spinojino writes question is it correct to say that large language models have no priors?
Do large language models have priors?

1:21:18 _Steve:_
I'd say yes, they definitely do.
And I think the difference to how people are used to thinking about priors in Bayesian inference, for example, if you write down a Bayesian statistical model, you say here's the parameters, and here's what the priors are on the parameters.
Large language models, I think the priors are and maybe neural nets in general, I think that the priors are much more implicit, right?
So there's some functions which they find easier to learn than other functions.
And there's even some work trying to discover some statement of what those kind of implicit priors are.
But that's actually how I think about comparison of different neural network architectures, which is maybe something Elliot and I might agree on, right?
Like you have to find priors which allow them to learn the things that kids learn, right?
And not all architectures will do that.
Even among architectures which are Turing complete or capable of learning any kind of function, not all of them will do it even on kind of huge data set sizes.
So I think of this sort of search over neural net architectures as really one of a search over priors.
But it's not priors or I mean, you could think of it as a search over universal grammar or something, right?
But it's not priors or universal grammar in the sense that people have talked about it as like an explicit statement about what kinds of rules are allowed, or an explicit statement about what kinds of functions are high probability or something like that.
It's all implicitly coded there.

1:22:55 _Elliot:_
Yeah, totally.
I think that's right.
The real question is reducing the space of what those prizes are like, and if it's anything remotely like what human beings are doing.
So LLMs, like, I would at least say that things like GPT-3 are an existence proof of that building fully functioning sync tactic categories from surface distributional analysis alone is possible.
Yes, that is correct.
But even so, I would say most Syntacticians don't really believe that syntactic categories are innate.
So the prior issue is slightly less relevant.
Here, it's the operations that are said to be innate.
So in the syntax domain, it's particular linguistic computations that are said to be innate and categories themselves.
In fact, even Charles Yang has admitted in the last couple of years that they are maybe innate, but maybe not.
So people have given another relevant priority are things like me and Gary Marcus have talked about compositionality.
That seems to be a big problem.
So people have given chat, GPT, BBC News articles, asking it to compress it and then re explain it.
So one example I saw was Peter Smith, 58 is being arrested on charges of manslaughter.
And you get it to compress it and reexplain it, and it comes out as 58 people are being charged with manslaughter.
That's a pretty clear example of a lack of compositionality being built into whatever compression it's doing.
And there's another example where there are some examples of potential analogical reasoning.
So in Bing chat, Bing has this chat function.
The question is, is it just finding meta relations that have already been documented by humans, or is it genuinely creating new relations, the new stuff that is being built?
So someone asked, draw me a table comparing Jesus Christ with the Nokia 99 Ten, the cell phone, Nokia 99 Ten, and it said it compared the release dates, it compared the size, the weight, it compared the CPU with Jesus's all powerful knowledge, it compared the memory of the phone with the all knowing nature of God.
Right?
Also, I think it said that they were both resurrected because the Nokia was rereleased a couple of times.
Right.

1:25:05 _Steve:_
That sounds like a great answer.
What's wrong with that?

1:25:08 _Elliot:_
Maybe it sounds a lot like analogical reasoning, but then it also had some quite weird ones where it was like for the camera, it said no, it just gave Jesus's description, but it's not really what a camera is there's some kind of things that look like analogical reasoning?
Maybe, but it's unclear.

1:25:24 _Steve:_
I think that sounds like an awesome answer to me.
I was going to say you said large language models learn there's an existence proof of part of speech categories, but they don't just output part of speech categories.
Right?
They have a lot of grammatical syntactic knowledge and moreover, they have a lot of semantic knowledge and probably some pragmatic knowledge, and they're not bad at translation.
And it's way more that they have discovered than just part of speech categories.

1:25:57 _Elliot:_
Well, I said syntactic categories, right?

1:26:04 _Steve:_
But they've discovered way more than that.

1:26:10 _Daniel:_
I'm going to as a teaser motivator for hopefully both of you to join again in the future, with or without other guests.
A few of the exciting questions just for us to include in this transcript and then.
Thank you both Elliot and Stephen for joining.
So, just a few of the last questions that were asked.
Juan asked, how do small transformers Zhang at all 2020 compare with children learning language?
96 asked, what are your thoughts on implicit priors versus animal instinct?
Rojda asked, what constraints that space in LLMs?
Don't they get there by training?
So are they discovering it?
That's not what they implement at the start.

1:26:49 _Elliot:_
Maybe.

1:26:52 _Daniel:_
And there's many more questions, so I hope that we can all review and reread each other's works and come together for 41.2 in some future time.
Thank you, Elliot and Steven, for this excellent stream.
Thank you, Dave.

1:27:06 _Elliot:_
Thank you both.
Yeah.

1:27:08 _Steve:_
Thank you so much.

1:27:09 _Daniel:_
Farewell.

1:27:10 _Steve:_
Bye.

1:27:11 _Elliot:_
See you.
