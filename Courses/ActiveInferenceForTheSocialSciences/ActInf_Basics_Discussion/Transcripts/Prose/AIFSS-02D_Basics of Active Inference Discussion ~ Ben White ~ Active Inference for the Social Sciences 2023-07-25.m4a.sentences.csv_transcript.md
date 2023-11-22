
00:05 _Daniel:_
[[start:5180][end:5896]] All right.
[[start:5998][end:7896]] July 25, 2023.
[[start:7918][end:13780]] And we are in the discussion section, basics of Active Inference.
[[start:13860][end:20148]] This is the first discussion section that we've had for this course, so thank you all for joining.
[[start:20324][end:27260]] And it's going to be regarding the topics that Ben White introduced in his recent lecture.

00:27 [[start:27420][end:33810]] So everyone will be welcome to pop in and introduce themselves.
[[start:34260][end:44468]] And then I know that Ben has some ideas to discuss and many other spontaneous and written questions will come into play.
[[start:44634][end:55240]] So with that exit for now and pass to perhaps some of our first time live streaming guests.

01:07 _Darius:_
[[start:67850][end:71686]] I guess I've already spoken, so I may as well continue.
[[start:71788][end:73050]] So I'm Darius.
[[start:73790][end:75002]] I am Master's student.
[[start:75056][end:80006]] I'm just about to finish at UCL in sort of social distributed cognition.
[[start:80118][end:94202]] I work in a social cognition lab looking at salience regulation and attentional mechanisms within social contexts, but all within an Active Inference framework, within the Bayesian brain hypothesis framework.

01:34 [[start:94346][end:98762]] And, yeah, it's a sort of recent discovery and obsession.
[[start:98826][end:102740]] And so I'm sort of getting to grips with both the high road and the low road.
[[start:103350][end:113430]] And so I've had the opportunity to chat to Mark and some other researchers who have been super informative, but always looking to learn more and get my head around even more of the sort of philosophical and mathematical theory.

01:55 _Ben:_
[[start:115770][end:116520]] Cool.
[[start:117530][end:118600]] Sounds good.

02:04 _Francesco:_
[[start:124170][end:124822]] Hi, everyone.
[[start:124876][end:125880]] Can you hear me?

02:06 _Daniel:_
[[start:126410][end:127298]] Yep.

02:07 _Francesco:_
[[start:127474][end:129022]] I'm Francesco Balzan.
[[start:129106][end:137040]] I'm a PhD student at the University of Bologna, Italy, actually working on intersection between artificial intelligence and education.

02:17 [[start:137890][end:146494]] I have a background in cognitive anthropology and philosophy of science, and I met Axel and Maxlin a few years ago.
[[start:146692][end:160222]] So I dive into the rabbit hole of Active Inference and currently pretty much interested in multiscale Active Inference models of scientific cognition.
[[start:160286][end:169842]] So pretty interested about the agent level modeling of scientific reasoning assumption that might emerge from the interaction with a scientific environment.
[[start:169906][end:176398]] So we're referring to scientific nature, construction and all these type of top down and bottom up interactions.
[[start:176434][end:180202]] So super interested to hear something from you.

03:00 _Ben:_
[[start:180336][end:181260]] Thank you.

03:03 [[start:183630][end:185020]] Thank you very much.

03:08 [[start:188760][end:191990]] Would anybody else like to introduce themselves before we start?

03:14 [[start:194840][end:196310]] So you go first.

03:16 _Gina:_
[[start:196840][end:197348]] Okay.
[[start:197434][end:199504]] Hi, I'm Regina Zaghi-Lara.
[[start:199632][end:200844]] You can call me Gina.
[[start:200912][end:202340]] I'm from Guatemala.

03:22 [[start:202420][end:205348]] And well, I'm not from the social sciences.
[[start:205444][end:207828]] I come from biology and neuroscience.
[[start:207924][end:218008]] And I'm here because I'm working on a project as a technical operator in this big project in the Xscape and material minds.
[[start:218104][end:224680]] And I do the technical part and experiments, but I want to learn the philosophical part.
[[start:224770][end:228880]] That's the background that makes the theory of everything.

03:48 [[start:228950][end:231436]] We're going to experiment.
[[start:231548][end:233330]] So I'm here to learn.
[[start:234340][end:246384]] And also, I am like when you see the Olympics, that you see all the swimmers, and I wish there was a normal guy to see how good these people are so you could compare.
[[start:246432][end:248292]] So that's me today, right?
[[start:248426][end:253656]] I understand half of what's going on, but I'm happy to be here, so yeah.

04:13 [[start:253758][end:254410]] Hi.

04:21 _Ben:_
[[start:261560][end:261924]] Sorry.

04:21 _Lee:_
[[start:261962][end:262736]] I'm Leigh.
[[start:262848][end:264128]] So my name is Lee.
[[start:264224][end:270120]] I'm a PhD student at the University of York studying systems transformation.
[[start:271420][end:283748]] And I'm joining because I'm using perceptual control theory at the minute to model examples of effective practice in organizations.

04:43 [[start:283844][end:299404]] And I've read quite a lot of Active Inference papers, and I understand that there's a lot of resonance overlap between perceptual control theory and Active Inference, although I understand it's within a predictive framework.
[[start:299532][end:311684]] And also it's kind of a level of abstraction higher, so you're able to kind of quantify the difference between sort of the predictive state or the outcome state and the current state.
[[start:311802][end:327080]] So what I'm really trying to understand is how might that level of abstraction be useful in what I'm doing, actually, because I understand it's a much more kind of concurrent theory and framework than perceptual control theory.

05:30 _Ben:_
[[start:330950][end:332260]] Yeah, very cool.
[[start:333350][end:334500]] Anybody else?

05:37 [[start:337830][end:338980]] Is that everybody?

05:41 [[start:341670][end:349240]] Okay, well, has everybody seen the lecture that I gave a couple of weeks ago?
[[start:350170][end:362540]] Okay, so I think it might be helpful then, if I kind of very briefly go over what we covered in that lecture just to kind of jog people's memories, and then we can maybe pick up some questions from there.
[[start:363070][end:373374]] So the lecture last week was on the basics of Active Inference, and it was intended to be an introduction to the framework on a very abstract, philosophical level.
[[start:373412][end:377818]] So it left out all of the kind of mathematics and technical aspects of the framework.
[[start:377994][end:389454]] And the objective really was to lay the groundwork for future weeks in this course, because this is obviously a course on Active Inference in the social sciences.

06:29 [[start:389582][end:398914]] And so in the subsequent weeks, we're going to be looking at topics like collective behavior, social cognition, shared norms, and niche construction.

06:39 [[start:399042][end:410534]] And so what I wanted to do was to put on the table a kind of fully fleshed out picture of what the individual agent looks like in Active Inference.
[[start:410662][end:427066]] And so to do this, we looked at emotion, agency, mind, so we looked at kind of the role of action and perception, the role of internal representations in Active Inference.
[[start:427178][end:441490]] And then as a case study, we looked at an Active Inference based account of addiction to kind of bring all of these threads together, to kind of articulate a lot of the things that I'd said in the previous sections.

07:26 [[start:446250][end:450786]] The questions here don't have to be specifically tethered to that lecture.
[[start:450898][end:461980]] I suppose we can just start with any general questions about Active Inference and philosophy and how Active Inference applies to individual agents, or if anybody did want to pick up on any threads from the lecture, then we can go from there.

07:46 _Gina:_
[[start:466210][end:469858]] Can I ask something just for the basic questions?

07:50 _Ben:_
[[start:470024][end:471140]] Yeah, of course.

07:51 _Gina:_
[[start:471830][end:482770]] I don't understand because I think you explain it later, but how does creativity and science in general enters active imperents?
[[start:483130][end:490360]] How does trying to be creative and not doing what you predict enters this room?

08:10 _Ben:_
[[start:490810][end:493640]] Yeah, this is a really good question.

08:15 [[start:495710][end:497210]] Did you see the lecture?

08:18 _Gina:_
[[start:498670][end:501100]] Yeah, but I remember half of it.

08:21 _Ben:_
[[start:501630][end:506620]] That's fine, but do you remember the dark room problem?

08:27 _Gina:_
[[start:507090][end:510000]] Yeah, I know that's where the answer is.

08:33 _Ben:_
[[start:513090][end:521410]] I think there are several interesting dark room problem, some of them more interesting than others.
[[start:521480][end:525890]] And I tried to cover I obviously didn't have time to cover all of those in the lecture.
[[start:527750][end:548810]] But for those that perhaps aren't familiar, the dark room problem is this kind of canonical philosophical worry about predictive processing and Active Inference that says essentially, if all we're trying to do is minimize prediction errors, why don't we just find maximally predictable environments?
[[start:549150][end:556250]] And why do we not just lay in a dark room hooked up to an intravenous drip and enjoy kind of error free lifestyle?
[[start:556910][end:560894]] So I think that's the question that you're articulating there.

09:21 [[start:561092][end:563306]] I just quickly see a hand from Darius.
[[start:563338][end:565760]] Darius, did you want to jump in, or was it a separate question?

09:27 _Darius:_
[[start:567490][end:568814]] It's a separate question.
[[start:568932][end:570794]] So I thought I would just do it in advance.
[[start:570842][end:571806]] But yeah, no, ignore me.

09:31 _Ben:_
[[start:571828][end:573218]] I'll circle a call background in a second then.
[[start:573224][end:575506]] But feel free, I should say.
[[start:575528][end:584514]] Actually, this is the first time I've kind of chaired a discussion like this, so I'll be explicit and say people should just feel free to jump in whenever they want.
[[start:584552][end:591880]] If you want to take the disco, if you want to kind of add something or kind of build on a question that we're answering, feel free to jump in.
[[start:592970][end:610510]] But, yeah, with the dark room problem, as I'm aware, the first answer to that question and this is something that I did cover in the lecture, is essentially a big part of Active Inference is to recognize that agents are it's a kind of fundamentally embodied framework, okay?

10:10 [[start:610580][end:614462]] So that can be kind of cashed out in various ways.
[[start:614516][end:630210]] But one of the most important ways is that the expected states of the organism or that the agent are necessarily rooted in the phenotype of the organism and the kind of evolutionary biological needs that come with having a particular body.
[[start:630360][end:636774]] So there was a paper that I referenced in a lecture by there's three authors on this paper.

10:36 [[start:636892][end:641794]] It's andy Clark, Karl Friston, and then I'm forgetting the name of the third author.
[[start:641842][end:645494]] If anybody can recall, feel free to drop it in the chat.

10:45 [[start:645622][end:665146]] But this is an answer to the dark room, where it builds on that notion of embodiment and says, look, creatures like us, human agents, could sit in the dark room and do nothing and just kind of enjoy the very predictable march of hunger, thirst, et cetera.
[[start:665178][end:668110]] But obviously, those particular biologists out of the room.
[[start:668260][end:671060]] And so you have this very fundamental level.

11:13 [[start:673830][end:679314]] We have this very fundamental kind of basis upon which we have these needs that need to be met.
[[start:679352][end:686614]] And so we need to engage in exploratory behaviors on the topic of novelty, because that's a kind of base.
[[start:686652][end:689160]] I take that to be a kind of baseline answer.
[[start:689770][end:706230]] But there are clearly kinds of activities and behaviors that we do engage in going beyond the dark room kind of curiosity play, creativity, engaging in kind of why do we create works of art?

11:46 [[start:706400][end:716990]] And there's not an obvious link between those kinds of behaviors and the kinds of biological needs that are emphasized in the original answer to the dark room worry.

11:57 [[start:717970][end:730174]] So in answer to Regina's question about creativity, I think that a good starting point for this is the section on aerodynamics that I introduced in the lecture.
[[start:730222][end:744690]] So this was the idea that there's this strong connection between affectivity as a kind of emotional, embodied feeling state and the changes to the rate in prediction error minimization.
[[start:744850][end:746070]] So I don't know.
[[start:746220][end:749994]] I am now very much articulating Mark's work here.
[[start:750032][end:754940]] So I don't know if Mark wants to jump in at any point and do a much better job than I can.

12:38 [[start:758530][end:762170]] I think there's certainly work on the horizon.
[[start:762330][end:772770]] I know that there are people who are currently building up theories of artisticity that are based on this idea of aerodynamics.

12:53 [[start:773110][end:805290]] So Mark's paper on play with Mark Anderson that I mentioned has a really interesting idea where if you explore playful behaviors which are kind of fundamentally creative and it's an inherently creative exercise, I think the really interesting idea that comes out of that is one thing that we engage in because it feels good is we create niches of very manageable prediction error that we can then minimize.

13:27 [[start:807410][end:812382]] So, yeah, that's playful behavior is the answer to the puzzle of play.
[[start:812436][end:823374]] So the puzzle of play is why do we engage in metabolically quite costly and they don't have any obvious benefit.
[[start:823502][end:833566]] And the idea there is that, well, there's kind of several ideas in there, but one of them is that it just literally feels good because minimizing prediction error feels good to us.

13:53 [[start:833608][end:837480]] So whenever we do better than expect at minimizing prediction error, it feels good.

14:00 [[start:840010][end:851980]] Obviously, I don't know for sure, but I think that any answer that we give regarding artistic creativity is going to fall within that kind of bulb that essentially we engage in.
[[start:852350][end:869306]] The part of the creative process is just constructing those that give us tasks of manageable prediction error that ideally fit at the boundaries of our skilled capabilities.

14:29 _Mark:_
[[start:869338][end:871170]] Can I add two quick things there, Ben?
[[start:871510][end:881250]] So that was a great explanation, but just to hit two points a little bit harder, one, you might think all that matters error.
[[start:882250][end:891938]] That's why it looked a little bit paradoxical that we also create antithetical to our modus operandi, which is to reduce error.

14:52 [[start:892034][end:898330]] But when you remember that for our kind prediction error minimizing system, we have a really deep temporal model.
[[start:898480][end:906310]] We're managing uncertainty at a big horizon, maybe even multigenerational, where we're thinking about our kids or our kids.
[[start:906400][end:909354]] I mean, who knows how deep the Generative model actually runs?
[[start:909482][end:929490]] It turns out that error over that stops developing error minimizing skills and abilities and just hangs out in one microniche, because that microniche is going to be upset sooner, right?

15:29 [[start:929560][end:939014]] I mean, it's such a great example of where we thought we were in a really set vector state and then suddenly it gets jostled and all of us go, oh my goodness, what do we do?

15:39 [[start:939052][end:940230]] We've been bumped.
[[start:940810][end:951174]] And it turns out that the best error minimize will be the two kinds of errors that are hates.
[[start:951222][end:953782]] Those errors are digestible.
[[start:953926][end:959614]] So that means not too complex that you can't do anything with it, you can't learn anything from it, but also not so boring that there's nothing to learn.
[[start:959732][end:971714]] If we hang out, if we're sensitive to and we hang out at the edge of our capability, then we keep developing new error minimizing abilities, which actually sets us up to be good error minimizing systems over the long run.

16:11 [[start:971752][end:982978]] So even though we're investing metabolism now, we're setting ourselves up to be able to manage, especially in the deep end of the pool, black swans manage uncertainty that we're not going to be able to predict.
[[start:983074][end:984242]] They're really unpredictable.
[[start:984306][end:988050]] Unpredictable that comes from hanging out at this edge.
[[start:988130][end:997906]] So part of our curiosity and playfulness and creativity are going to be about us making and digesting novel slopes of Volatility.

16:38 [[start:998018][end:1004038]] I think that's one really great answer for why you get playfulness and curiosity out of this and creativity.

16:44 [[start:1004134][end:1007194]] I'll just drop one more and we don't have to get into it too deeply here.
[[start:1007232][end:1009580]] But here's one other one that we're thinking of.
[[start:1010030][end:1018640]] There's something really special in the creation of art, especially in a public sphere, that I think is so interesting and that somebody needs to be sort of looking at this.
[[start:1019330][end:1029730]] There's actually a new collection coming out in Philosophical Trans B on Art and Predictive Processing, which I think you should check out if you're interested in these topics.
[[start:1030310][end:1037922]] But the idea that we've been thinking about is there are ways that we can bring our Generative model out and put it into a public sphere.

17:18 [[start:1038066][end:1049580]] You can take something which is typically on the inside and you can put it outside, and then you can have other error minimizing systems look at it and fiddle around with it and then we can reimbibe it.
[[start:1050110][end:1051674]] We're doing this all the time.
[[start:1051792][end:1054554]] That's what language allows us to do and what writing allows us to do.
[[start:1054592][end:1055542]] Think about maths.
[[start:1055606][end:1065150]] You're bringing up part of your predictive understanding, you're laying it out and then other predictive agents can fiddle around with it and then you can take it back in as part of your updating your own model.

17:45 [[start:1065300][end:1067902]] And I don't know how much more I can say here.
[[start:1068036][end:1069834]] I just think this is a kind of horizon.
[[start:1069882][end:1071906]] But I think there's a really juicy thing to say here.
[[start:1072008][end:1074434]] About where real art is.
[[start:1074472][end:1075214]] Like Tolstoy.

17:55 [[start:1075262][end:1095574]] Maybe Leo Tolstoy was already on this, where you put something of the Creator in the Creation and then other people receive that and then they can do something else with it, and then you're able to sort of take it back in all under the guise of sort of Minimizing Volatility or understanding Volatility, maybe.
[[start:1095612][end:1096790]] That was a bit deep.

18:17 _Ben:_
[[start:1097130][end:1099046]] No, that was really good.
[[start:1099148][end:1099800]] Yeah.
[[start:1101390][end:1110554]] So in the chat I just dropped a link to yeah, so somebody just asked about papers related to hanging out at Edge of Our Capabilities.

18:30 _Mark:_
[[start:1110682][end:1111920]] I'll do that right now.

18:32 _Ben:_
[[start:1112370][end:1114446]] There sure are some papers on that.
[[start:1114548][end:1115598]] Mark's got a few.
[[start:1115684][end:1131380]] I already dropped a link in there to an Aon article by some of the old Expect project crew, including Mark Kate Nave, George Dean and Andy Clark on the value of uncertainty, which is I think it's a really good start point for some of these questions.
[[start:1132390][end:1140642]] Just because Aeon is a kind of non academic place where, you know, it's a non technical introduction.

19:00 [[start:1140706][end:1145922]] And there's a wonderful example in that paper of a guy named I think it's Max Hawkings.
[[start:1145986][end:1146474]] Is that right?
[[start:1146512][end:1146810]] Mark?
[[start:1146880][end:1148314]] Max who?
[[start:1148512][end:1153338]] He's a kind of tech guy and he realized he was getting kind of bored with his life.

19:13 [[start:1153504][end:1161850]] He'd inadvertently trapped himself in a dark room because his life had become so rote and scheduled and systematic.
[[start:1161930][end:1172722]] He realized that he would be kind of incredibly easy to kidnap because he was in the same place at the same time every single day and he took drastic action to break out of that dark room.

19:32 [[start:1172776][end:1184498]] So he kind of introduced a randomization algorithm that it would kind of choose for him where he was going to eat, where he was going to go, which shows he was going to attend.
[[start:1184674][end:1188310]] And this example is a really nice centerpiece in this article.
[[start:1189370][end:1204202]] I think this is a nice place to start because it's also grounded in discussions about epistemic actions as well, because there's also as cool as play and art and creativity are there's also really good reasons that uncertainty is valuable as well?

20:04 [[start:1204256][end:1204522]] Right?
[[start:1204576][end:1223282]] Because while we might want to exploit all of the opportunities for kind of nourishment and valuable prediction error minimization in our environment, there are of course going to be times where those opportunities are exhausted and we need to go and explore different ones.
[[start:1223416][end:1230482]] And I think there's some stuff in there as well on epistemic actions within the context of navigation as well.
[[start:1230536][end:1239014]] So sometimes we're going to have to temporarily move further away from our target in order to minimize our uncertainty about where we're going.

20:39 [[start:1239132][end:1250230]] So there's lots and lots of stuff on the value of uncertainty and it kind of is very much at the forefront of some of the really interesting philosophical applications of the framework.

20:50 [[start:1250310][end:1251100]] For sure.
[[start:1252110][end:1254522]] Okay, by all means.
[[start:1254576][end:1255660]] Yeah, we've got time.

20:56 _Gina:_
[[start:1256350][end:1260442]] I know you have a question that is but with the value of uncertainty.
[[start:1260506][end:1275406]] It's just that I'm thinking because I've been working a lot with the magicians and there's a way of using uncertainty as entertainment that it's very difficult to understand as a concept for entertainment.

21:15 [[start:1275438][end:1283458]] Why would you like to be in a place where you want to predict but you cannot, and you still want to participate in this activity?
[[start:1283554][end:1287320]] So for me, magic shows, it's kind of breaking a little.

21:30 _Ben:_
[[start:1290730][end:1300998]] Spoke to I forget the person's name, but there was an Xcape meeting here at Sussex and I spoke to one of the guys on Escape who had been working on magic.
[[start:1301174][end:1305210]] I don't know if you know who I'm talking about, but I think they have a book on magic.
[[start:1305710][end:1314410]] And I think that's really cool to think about from a predictive processing perspective, the idea that magic is just these wonderful kind of violations of expectations.
[[start:1314570][end:1321300]] In a certain sense, I think predictive processing provides a nice, really intuitive framework for thinking about those kinds of things.

22:01 _Mark:_
[[start:1321670][end:1323502]] One little point there, Regina.

22:03 [[start:1323566][end:1333998]] Just about again, if it feels paradoxical just to sort of complexify your view, remember that this is always happening in a hierarchical system.
[[start:1334184][end:1342802]] So just because you have errors at one level of the system doesn't mean you're going to have sort of critical, cascading, unbearable errors at higher levels.
[[start:1342946][end:1345826]] So that's why it's fun to go to horror movies.
[[start:1345938][end:1347334]] So I dropped the paper here.
[[start:1347372][end:1349606]] Also, we have a new paper coming out on horror movies.

22:29 [[start:1349638][end:1354714]] I'm pretty interested in this, but it's the same as going to the magic show in some way.
[[start:1354832][end:1361150]] Now, the reason why those errors are fun is because we're safe in a theater.
[[start:1361570][end:1363054]] We're with our friends.
[[start:1363252][end:1366910]] We have lots of sugar in our system from eating popcorn and candy.
[[start:1367490][end:1373220]] We can control the amount of scary by covering our eyes.

22:54 [[start:1374870][end:1376738]] There's lots of control here.
[[start:1376824][end:1395490]] And yet we're getting media that's pinging all of our evolutionarily ancient error tracking systems so that we're getting jumps in the physiology as if there's a bunch of volatility that we need to manage, and yet we're in a completely safe space, which is really fun for our kind of system because we're hierarchically deep predictive systems.

23:15 [[start:1395570][end:1397798]] The high level here isn't jeopardized.
[[start:1397974][end:1404054]] It knows I'm in a theater, but the low level stuff is still registering all sorts of literal volatilities.
[[start:1404102][end:1405574]] But of course, they get squashed.

23:25 [[start:1405702][end:1407740]] They don't cascade all the way up.
[[start:1408990][end:1418286]] Or if you're the kind of person where they do tend to cascade all the way up, then you're also the kind of person who doesn't like going to horror movies because it kind of scares you.
[[start:1418388][end:1422626]] Go home and think, oh, goodness, maybe ghosts are real and maybe I live with them.
[[start:1422648][end:1423650]] You wouldn't be going there then.
[[start:1423720][end:1431570]] So with magic, it's the same sort of thing with error.

23:52 [[start:1432810][end:1441938]] I don't know if you've ever who does the really extreme magic.
[[start:1442034][end:1444002]] David Blaine, where he was in a block.
[[start:1444066][end:1445318]] Yeah, david Blaine, have you ever seen him?
[[start:1445324][end:1449270]] He goes to Haiti where you have a community that really believes in magic, and he does some magic and he gets into trouble.
[[start:1449350][end:1454550]] Like suddenly all the young men are, no, no, that's no bueno.

24:14 [[start:1454710][end:1455834]] That you're doing this.

24:15 [[start:1455872][end:1460326]] And then the camera pans back and he, no, no, hold you here, I'll show you how it's done.
[[start:1460368][end:1461514]] It was just a trick.
[[start:1461642][end:1462494]] I'll just show you outside.
[[start:1462532][end:1466410]] It's not real magic because there they're not having fun with it anymore.

24:26 [[start:1466490][end:1470434]] They're like, no, that's not a good thing to do.
[[start:1470632][end:1479794]] So it just goes to show that our engagement with magic is mostly a sort of scary play, I think.

24:39 _Ben:_
[[start:1479832][end:1482526]] One thing I just kind of sorry about the seagulls.
[[start:1482558][end:1483574]] I don't know if you can hear those.
[[start:1483612][end:1486710]] There are seagulls going crazy just outside my window.

24:47 [[start:1487450][end:1501526]] One thing I would add is, I think, another aspect to this part of the framework wherein you have this value of prediction error, kind of epistemic and effective emotional value of prediction error.
[[start:1501558][end:1513902]] It's one of the kind of key elements in this notion of agency get in Active Inference that I think is really going to be really important to in mind as you go through the further weeks of this course.
[[start:1513956][end:1527822]] As well, like I said in the lecture, it's not necessarily speaking to the metaphysical question of free will, but it's certainly moving us away from this picture of the agent as a kind of automaton that's just following rules.
[[start:1527886][end:1532360]] There's real space here for kind of individuality and creativity as well.

25:34 [[start:1534730][end:1540310]] Okay, Darius has been waiting a little while, so let's go over to him.

25:40 _Darius:_
[[start:1540460][end:1543846]] Happily patient, happily mean.
[[start:1543868][end:1559420]] This is this question, I guess, is deriving from my thoughts about the meeting of the high road and the low road, some of the recent work that's been coming out of Maxwell Ramstead and actually a conversation I had with him, which is that the generative model.

26:02 [[start:1562450][end:1567006]] So my question, given that given and.

26:07 _Francesco:_
[[start:1567108][end:1567760]] Talk.

26:09 _Darius:_
[[start:1569810][end:1584002]] Is regarding the notion of affordances, I think it's natural that as cognitive scientists and philosophers, we take the perspective intuitively of the agent in the agent arena relationship and how the agent is in the business of reducing prediction error.
[[start:1584146][end:1596354]] I was just wondering whether, as philosophers, you and Mark have thought about what is it like for the whole system to be in the business of reducing its prediction error?
[[start:1596402][end:1598578]] So I'm interested in flow states.
[[start:1598764][end:1617514]] And so, for example, my thinking is that in a canonical example of a flow state, let's say a rock climber, the climbing wall, is also in the business of reducing its prediction error as to afford the opportunity for it to be exploited stealth or themselves are in the business of reducing prediction error.
[[start:1617562][end:1624500]] So I'm wondering whether this expansion of affordances is bi directional trial, infinitely directional, better?

27:09 _Ben:_
[[start:1629430][end:1632020]] That's an amazing question.
[[start:1633050][end:1642150]] You mentioned Axel constant, but somebody else.

27:22 _Darius:_
[[start:1642220][end:1642646]] Someone else.
[[start:1642668][end:1645240]] But I spoke to Maxwell Ramsey's last week.

27:28 _Ben:_
[[start:1648350][end:1651210]] There's a paper on I'll find it in a second.
[[start:1651280][end:1657462]] On niche construction and affordances.
[[start:1657526][end:1660250]] I think it's Axel comps.
[[start:1662110][end:1668640]] They talk about the kind of the symmetry between a niche and an agent.
[[start:1669250][end:1671634]] Very much in the same vein as you were just talking about.

27:51 [[start:1671672][end:1685510]] There this idea that there's not just this unidirectional kind of fit between the agent and the environment or the niche is actually modeling generative model of the agent as well, implicitly.
[[start:1686250][end:1698250]] So I think the best I can do there direction of some really interesting work on that, but certainly it's not something that plays a central role in my thinking recently.
[[start:1698590][end:1698954]] Yeah.
[[start:1698992][end:1702650]] So we have the participants chat.
[[start:1703470][end:1704220]] Yeah.

28:24 [[start:1704590][end:1706886]] A variation approach to niche construction.
[[start:1706998][end:1707274]] Yeah.
[[start:1707312][end:1715082]] I don't know if Mark has anything to add or anybody else worth thinking about.

28:35 _Mark:_
[[start:1715136][end:1715798]] Yeah.
[[start:1715984][end:1717406]] Darius, can I just check one thing?

28:37 [[start:1717428][end:1717822]] You asked.
[[start:1717876][end:1725006]] I don't know how much I need to add here, but did you think that the wall was reducing free energy relative to the climber?
[[start:1725038][end:1725954]] Did you say that?

28:46 _Darius:_
[[start:1726072][end:1726980]] That's right.

28:49 _Mark:_
[[start:1729270][end:1731042]] I don't know how that can that be the case?
[[start:1731096][end:1732280]] Can that be the case?
[[start:1732650][end:1739202]] The wall as a thing is maintaining itself relative self evidencing.

28:59 _Avel:_
[[start:1739266][end:1739494]] Right?

28:59 _Mark:_
[[start:1739532][end:1740214]] Yeah.

29:00 [[start:1740412][end:1742454]] But it's not really a duet of one here.
[[start:1742492][end:1749740]] It's not like it has a generative model that's deep, where it's modeling the climber, modeling it the same way as tango dancers do.
[[start:1750830][end:1771466]] A tango duo are having cooperative flow states because each movement opens a vista of possible error, minimizing opportunities for the partner, who in turn opens a vista of error minimizing opportunities for the partner and backwards and forwards into this ever opening expanse of affordance capabilities.
[[start:1771578][end:1774926]] But an inanimate object and an agent don't really have that same dynamic.
[[start:1774958][end:1776642]] So I was wondering what you were thinking there.

29:36 _Darius:_
[[start:1776776][end:1786610]] So my thinking was that this kind of bleeds into the notion of fluidity of affordances in the kind of Gibsonian sense and the fluidity of concepts.
[[start:1786690][end:1794762]] So I agree in the sense of physical self evidencing, it needs to model the rain, it needs to model the physical environment so as to maintain itself.
[[start:1794896][end:1807498]] But what about as it's a for it's it's so a sheer rock face is not a climbing wall.
[[start:1807584][end:1812378]] And that's because it doesn't self evidence as a climbing wall, it doesn't offer the affordances to be climbed.
[[start:1812474][end:1818606]] That's why I was kind of referring to which is that affordances change based on the agent arena relationship, right.

30:18 [[start:1818628][end:1821150]] Your car's affordances change whether it's working or broken down.
[[start:1821220][end:1825762]] Similarly, the climbing wall changes whether it's got footholds handholds or whether it's just a sheer rock face.
[[start:1825816][end:1826740]] That was my thinking.

30:27 _Mark:_
[[start:1827590][end:1832660]] It seems slightly spooky to me that we'd think of the wall as self evidencing in that way.
[[start:1833190][end:1844600]] I think the language that we tend to use because Julian Kirsten, Eric Reitfeld, Yelly Brunberg and folks often use the idea of affordances and fields of affordances in the Active Inference way.

30:46 [[start:1846250][end:1865360]] The radical end of the pool there is typically that the affordances don't only happen on the agent side, but rather happen from a dynamic of the changing volatile environment and the generative model of the agent and that they're collaborating in dynamic ongoing ways such that the affordances are emergent between them.
[[start:1866050][end:1868142]] That certainly seems right to me.
[[start:1868276][end:1875300]] The idea to push it a little bit further and think about the wall self evidencing, I think it's a step too spooky for me.
[[start:1875750][end:1891000]] I think I would feel safer a little bit closer to thinking about the affordances are changing relative to the dynamics of the wall, but I don't know what it would mean for the wall to be evidencing, the climber or itself.

31:31 _Ben:_
[[start:1891450][end:1922290]] Ben that's stirred a couple of thoughts a little longer on the work by affordances because there's this really nice distinction in their work between what they call well, I'm not sure if they I think I think that the term landscape of affordances is a little bit older, but they make this distinction between a landscape of affordances and a field of affordances.

32:02 [[start:1922710][end:1935762]] And I think the reason this is really important to get on the table is because this distinction is kind of directly targeting the dynamic, shifting, very affective nature of affordances.
[[start:1935826][end:1941030]] So on the one hand, you have this landscape of affordances that is relatively static.
[[start:1941850][end:1945510]] So right now my landscape of affordances is Brighton.
[[start:1946250][end:1953018]] And the landscape of affordances in that sense is not really going to change very rapidly unless I kind of jump on a plane and go somewhere else.

32:33 [[start:1953184][end:1960030]] But the field of affordances has this thoroughly kind of normative, affective character to it.

32:40 [[start:1960180][end:1970746]] So depending on my internal state at any given time, depending on my expectations or my desires, say, my field of affordances is going to shift very rapidly.
[[start:1970938][end:1976066]] So not just predicated on my internal state, but also kind of contextual cues as well.
[[start:1976168][end:1984710]] So if something were to happen in the environment that was afforded very high precision weight in, then that's likely to shift my field of affordances significantly.
[[start:1986570][end:2008154]] I think that the reason that I'm kind of emphasizing this to Darius's point is and kind of building on what Mark said, it doesn't seem like this distinction at least would apply from the perspective of the wall, say, because this kind of affectivity and normativity just isn't a feature of the wall's experience of the world.
[[start:2008272][end:2011482]] And also to kind of run with affordances.

33:31 [[start:2011626][end:2014926]] Perhaps you could say a bit more about how you would kind of think about this.

33:34 [[start:2014948][end:2023594]] Darius because affordances are kind of opportunities for to.
[[start:2023652][end:2033150]] There's some debate about this, but I like to think of them as like a relational property between you have the skilled capabilities of an embodied agent and then you have some feature of the environment.
[[start:2033310][end:2038854]] So I think when you're thinking from the perspective of the wall, you have the features of the environment because you.
[[start:2038892][end:2043522]] Have the embodied characteristics of the agent are kind of playing that role.

34:03 [[start:2043666][end:2048506]] But it's not clear to me what the kind of skilled capabilities of the wall is.
[[start:2048608][end:2051226]] So yeah, if you could just say a bit more about that.

34:11 _Darius:_
[[start:2051408][end:2059450]] Yeah, I mean, it may be the case, as you pointed out, that actually the technical term affordance as being opportunities for action is misplaced.
[[start:2061390][end:2080370]] This is a lot of this I've been formulating, having read this very new paper by Ramsey and colleagues on Bayesian mechanics of physics of and by beliefs, where he really rams home this point, that the system, the generative model is the system of the kind of stochastic differential equations across the state space.
[[start:2080440][end:2085398]] So across the Marko blanca, across the particle with its Marko blanket and the external states.

34:45 [[start:2085564][end:2091638]] And that is the system which is in that system itself is in the business of reducing free energy.
[[start:2091724][end:2098282]] So it's not just the Active Inference agent, it's the whole system which is embedded in a whole system of other things.
[[start:2098336][end:2110446]] And so that was my general thinking, is that just on the prerequisite that these systems exist just on that a prior axiom, there has to be some kind of self evidencing of that system itself.
[[start:2110548][end:2112640]] So maybe affordance is the wrong word.

35:14 _Mark:_
[[start:2114850][end:2116142]] That might be the trick right there.
[[start:2116196][end:2120538]] As soon as you provoke affordance, you're provoking phenomenology.
[[start:2120634][end:2123582]] And so now we're not talking just about statistical variations.
[[start:2123646][end:2125460]] Now we're talking about lived experience.
[[start:2126310][end:2128994]] That might be the linchpin right there, I think.

35:29 _Ben:_
[[start:2129112][end:2130034]] I think that is right.
[[start:2130072][end:2130418]] Yeah.
[[start:2130504][end:2136858]] And I would say I think, Darius, you're absolutely on the right track and there is this ambiguity about affordances.
[[start:2136894][end:2148154]] But aside from that, I think you're absolutely mean it's just nonsensical to think about an agent absent an environment under active to.
[[start:2148352][end:2152860]] It is this agent environment system in its totality that's minimizing free energy.

35:53 [[start:2153310][end:2154986]] They have to be taken together as one.
[[start:2155008][end:2158366]] And I know Avel, you've had your hand up for a little while there.
[[start:2158468][end:2160080]] Is there something you wanted to add?

36:02 _Avel:_
[[start:2162050][end:2162798]] Yes.
[[start:2162964][end:2163886]] Do you hear me?

36:03 _Ben:_
[[start:2163908][end:2165230]] Well, we do.
[[start:2165300][end:2166126]] I do anyway.

36:06 _Avel:_
[[start:2166228][end:2177070]] Okay, so about the afferences world having afferences and basically the symmetry of agents and environment is a property of Active Inference.
[[start:2177150][end:2179038]] Well, of the frenzy principle.
[[start:2179214][end:2193106]] So if you buy the frenzy principle and you also buy that it entails that agent have affordances or any approximal notion, then you also buy that walls have affordances.

36:33 [[start:2193298][end:2197100]] So there are basically three position you can have on that.
[[start:2198030][end:2200746]] One is that Active Inference is correct.
[[start:2200848][end:2205900]] Wall are fucking affordances and they do self evidencing, which I would not go with.
[[start:2206450][end:2213038]] Another option is that you have basically devolved in the detail.
[[start:2213124][end:2217358]] So, for example, maybe the adjunct environment is not the wall.

36:57 [[start:2217444][end:2223058]] It's something that is broader, like Gaia system, whatever, and it just happens.
[[start:2223144][end:2226562]] It includes the wall, but it is not the wall.

37:06 [[start:2226616][end:2229010]] And it does do self balancing.
[[start:2229830][end:2232774]] And the third is that Active Inference is wrong.
[[start:2232972][end:2239030]] We don't have affordances based on whatever is the formal presentation of Active Inference.

37:19 [[start:2239450][end:2247402]] And I would go in that direction of this phenomenology stuff.
[[start:2247456][end:2255334]] So we have, I would say, philosophical evidence in the sense that denying this would lead to nonsense.
[[start:2255382][end:2263198]] But information is based on observation, and some system do observing much more actively than others.
[[start:2263364][end:2265946]] And maybe it's a good thing to have in your formalism.
[[start:2266058][end:2268400]] I'd say so.

37:49 [[start:2269190][end:2286726]] You have maybe a stronger case for the way phenomenology affordances are constructed in the quantum formulation of the FEP, if there is such a thing, which, like Chris Fields, someone who we should baseline believe claims there is.

38:06 [[start:2286908][end:2298486]] Because then you have formalization which is not in terms of dynamics per se, so causal constraints, but observation and indirectly phenomenology.
[[start:2298598][end:2300522]] Maybe you have something that is stronger there.
[[start:2300576][end:2334210]] But right now, the link sorry, there is actually a bunch of people who have a quite good hold on science, which are the ecological activity and cognition on one hand and between cognition and the metabolism, the constitution of the living thing that cognites on the other and one of their definition of agency cognition.
[[start:2334290][end:2341480]] Pick one entails interactional, asymmetry I think is the word.

39:06 [[start:2346670][end:2357530]] That is something we would need to translate into Active Inference, well into the FEP for Active Inference to have a strong grip over this affordancing.

39:18 [[start:2358030][end:2362046]] Until then, we have a kind of handwriting way.
[[start:2362068][end:2369950]] It relates it to more conceptual approaches that are related to an active and ecological approach to psychology.
[[start:2370110][end:2377460]] And, yeah, the formalism lags basically behind the concept for now.
[[start:2378230][end:2380260]] Sorry for the long talk.

39:41 _Ben:_
[[start:2381690][end:2382758]] No, that was great.
[[start:2382844][end:2383990]] Much appreciated.

39:47 [[start:2387210][end:2390834]] Anybody else want to come in on a question of affordances?
[[start:2390882][end:2396410]] Because I know affordance has played a fairly substantial role in the lecture.

40:03 [[start:2403870][end:2412080]] Anybody has any questions related to affordances or action perception affordances, then now's the time.

40:13 _Francesco:_
[[start:2413090][end:2417678]] Yeah, I do have one, but it's not well structured yet.

40:17 _Ben:_
[[start:2417844][end:2418960]] That's really fine.

40:20 _Francesco:_
[[start:2420130][end:2430094]] Something that I've been thinking about for the last month because I started to depend on artificial intelligence field coming from a humanities background and philosophical background.
[[start:2430142][end:2441602]] So I'm mixing many things in this period, mainly following the Active Inference as a crossroad between many disciplines, and this is very beautiful about the framework.

40:41 [[start:2441746][end:2467418]] And I was super curious about the question proposed by Darius, and I was then thinking about now we're actually facing a new environment and a new landscape in which we're interacting with actually generating over revolutionary time and synchronizing over evolution.

41:07 _Ben:_
[[start:2467594][end:2475406]] Technological alien agencies operating within our landscape and field of affordances.
[[start:2475518][end:2481090]] So I think there's a lot of really interesting work to potentially be done there.
[[start:2481160][end:2503980]] I will take the opportunity to shamelessly plug a preprint that Mark and I have released recently, where one thing that I'm really interested in, that I can kind of speak with some confidence on is the fact that I do think there's a point at which the theory of affordances or the language of affordances, starts to break down to.

41:47 [[start:2507410][end:2515002]] So the preprint I'll share around is looking at ambient technology specifically.
[[start:2515066][end:2524626]] So this is technology that the whole kind of impetus behind its design and conceptualization is that the user doesn't have to actually do anything.
[[start:2524808][end:2528062]] So it precedes the user Pragmatically and epistemically.

42:08 [[start:2528126][end:2532354]] It knows what kinds of things you want it to do, and it just does them in the background.
[[start:2532482][end:2541480]] And it works by shifting kind of it subtly shifts the material environment such that it impacts your field of affordances in real time.

42:22 [[start:2542890][end:2562122]] And the argument that we make in that paper is essentially that the affordances approach doesn't really work for this and that we need to kind of think again, I think that that might be how to conceptualize generative AI, for example, under the affordances framework.
[[start:2562266][end:2566720]] I don't know of anybody that's done any work on that, but it would certainly make a really cool project.

42:50 _Avel:_
[[start:2570090][end:2572440]] You are making it right now.

42:53 _Ben:_
[[start:2573770][end:2574840]] What's that?

42:56 _Avel:_
[[start:2576410][end:2578246]] You are making it right now.
[[start:2578268][end:2580840]] I know because you sent me the paper to review.

43:01 _Ben:_
[[start:2581450][end:2582520]] Oh, yeah.

43:04 _Francesco:_
[[start:2584910][end:2585820]] Thank you.

43:10 _Ben:_
[[start:2590030][end:2594914]] Early stages of a paper on the role of generative AI in classrooms.
[[start:2595062][end:2614210]] So, from the perspective of thinking about what kinds of affordance does generative AI represent in a learning environment, particularly, we're kind of applying Active Inference to classroom design and looking at it from the angles of different educational and pedagogical theories.
[[start:2614630][end:2617700]] But it's very early days.

43:40 [[start:2620070][end:2623122]] It probably depends on your view of generative II in general.
[[start:2623176][end:2627640]] I mean, it depends whether you would consider it a real cognitive agent or not.
[[start:2628490][end:2641162]] I think some people are more inclined to think of it as this is a thing that has agency, it has real understanding, and other people are maybe less inclined to think of it in those terms.
[[start:2641216][end:2645580]] And I think that might bear significantly on how you think of it.

44:06 _Francesco:_
[[start:2646930][end:2647966]] Yeah, that's super cool.

44:07 [[start:2647988][end:2655514]] That basically the last project you mentioned is very in line with my PhD project right now because my main PhD.
[[start:2655562][end:2665410]] Project is our European foundings, and it's about the AI for personalized education, and I'm trying to follow it through the Active Inference framework from a multi level perspective.

44:27 _Ben:_
[[start:2667350][end:2668130]] Very cool.
[[start:2668200][end:2670500]] Yeah, we should we should probably talk more about that.

44:33 [[start:2673690][end:2674342]] Okay.
[[start:2674476][end:2675350]] Darius.

44:37 _Mark:_
[[start:2677930][end:2678294]] Yeah?

44:38 _Darius:_
[[start:2678332][end:2691820]] I wanted to ask I mean, this may be directed more mark so I know this is kind of his work in terms of slopes of uncertainty and about doing better than expected at reducing prediction error over time.
[[start:2692350][end:2713602]] I was wondering kind of how the architecture of that is built into the particle, into the generative model because we have the kind of for me, I don't know if it's an hour and out sort of conflict, but we have these kind of implicit priors that we're going to fulfill certain expectations or minimize prediction error regarding certain things.

45:13 _Avel:_
[[start:2713656][end:2713826]] Right.

45:13 _Darius:_
[[start:2713848][end:2718850]] So homeostatic priors or happiness, well being, whatever it is.

45:19 [[start:2719000][end:2731958]] But then your claim is that we have the higher order beliefs, the higher order predictions that over and above, that I also need to do well, better than expected at reducing prediction error over time.
[[start:2732124][end:2735434]] So it's still quite fuzzy in my mind.
[[start:2735472][end:2751002]] But is there a kind of potential conflict there between the general priors that the system has and then actually, in a sense, violating those expectations by going over and above them, which itself constitutes an expectation?
[[start:2751066][end:2754110]] How do you kind of resolve that tension?

45:55 _Mark:_
[[start:2755810][end:2760366]] Yeah, that's interesting, but this is very much in Ben's wheelhouse too.

46:00 [[start:2760468][end:2786146]] Ben and I have been working on sloppy stuff for almost as long as I've been doing on his original paper called We'll Get It Up.
[[start:2786168][end:2792500]] They do a really good job of showing technically where this sits within a deep parametric model.
[[start:2793430][end:2806278]] Lara Senved Smith's paper on metacognition also does this by showing you have these depths of modeling where models above are modeling models below, and optimizing over those models below.
[[start:2806364][end:2817100]] So we have some good computational backbone for thinking, for not only thinking that this is the case, but beginning to express how it does the work it does.

46:57 [[start:2817630][end:2826830]] So let's leave that for digging into it, though, technically, sort of on our own, let me say sort of at a higher, more abstract level still, hopefully it's useful.

47:07 [[start:2827490][end:2844462]] It's not weird to think that this kind of anticipatory system is not only making predictions about the world, but it's also part of what it's predicting is how fast or slow, how efficient it is in particular contexts at resolving certain kinds of errors.
[[start:2844606][end:2849990]] That's a perfectly fine thing to think that we're also predicting slopes of engagement.
[[start:2851050][end:2860634]] And then all we're saying then is system also pays attention to when those expectations are breached and it's learning from those breaches that should just be the bread and butter for what the system does anyway.
[[start:2860752][end:2882318]] So precision is a second order process in much the same way precision is about how reliable are lower level predictions and then using that amount to toggle how impactful either errors or predictions are.

48:02 [[start:2882404][end:2897860]] So we've already got baked into the system, right from early days, this idea that the system is not only making predictions, but monitoring its own predictive processing regimes and then toggling based on how reliable those substreams are.

48:18 [[start:2898310][end:2915100]] All we're adding here is when we first thought about those mechanisms, one thing that can happen, this is just good for everybody who's interested in Active Inference, because I bump into this with my students all the time when we say something like precision weighting, a tendency to think of thing.
[[start:2916830][end:2924566]] So we go to find this precision like where's the biological or precision weighting?
[[start:2924598][end:2932414]] But when we actually get into a biosystem and we look for these things, the truth is precision is going to be weighted in lots of different ways.
[[start:2932452][end:2939086]] I mean, that's the real frontier of this research is to actually find how these things are instantiated and the answer is going to be multifarious.
[[start:2939118][end:2943138]] I mean, you're going to have precision adjustments happening throughout the system in lots of ways.

49:03 [[start:2943224][end:2947042]] It could be synchrony and asynchronous and desynchronies between systems.
[[start:2947106][end:2953842]] It can be neuromodulatory chemicals, it can be structural shapes within the brain.
[[start:2953906][end:2957718]] I mean, precision is going to be set in lots of different ways.
[[start:2957884][end:2983486]] So all that we're pointing out here is that one of the ways that precision is being set, one of the ways that the system is tracking how efficient it is and then upping or lowering the amount of impact error signals or predictions have, is that it's happening in an embodied way.
[[start:2983588][end:2994690]] So we've looked over to the effective search and lo and behold, there are all these signatures that we were looking for for this part of the machinery.

49:56 [[start:2996470][end:3000394]] So not weird that the system is tracking its own regularities and adjusting.
[[start:3000462][end:3002338]] That was baked in right from the beginning.
[[start:3002514][end:3005826]] How it does that, that's one of the frontiers.

50:05 [[start:3005858][end:3007654]] It's going to happen in lots of different ways.
[[start:3007772][end:3008594]] Lo and behold.

50:08 [[start:3008642][end:3027898]] Affect the dynamics, the shoe fits, they look like they do that stuff and then you bring it to the lab and you go back to like reward prediction error research and sure enough, neuromodulatory chemicals, reward systems are tuning affective dynamics relative to better than and worse than slopes of uncertainty management.
[[start:3027994][end:3031760]] It's exactly what we would expect given the computational model.
[[start:3032290][end:3046242]] So then it was an easy next step to start saying, well look, there's one of the ways that precision, there's one of the ways that affect system.
[[start:3046376][end:3051554]] Now just notice there it's the only precision, it's not the only thing the affected system is doing.
[[start:3051592][end:3057570]] We never want to say we're careful not to be reductionist to say, oh, affect is always aerodynamics.

50:57 [[start:3057650][end:3058678]] I don't think that's right.
[[start:3058764][end:3070390]] I think it's that aerodynamics are expressed in part effectively and they have this impact on the system that we've known about for a long time, even from just the reward prediction error literature.

51:10 [[start:3070550][end:3073340]] Does that help or was that a bit is that okay?

51:14 _Darius:_
[[start:3074190][end:3074940]] Yeah.

51:18 _Ben:_
[[start:3078370][end:3083950]] Just to add two things really quickly there because I know time is kind of catching up with us.
[[start:3084020][end:3097586]] I would emphasize as well, just as a kind of general .1 of the things I really like about the work on aerodynamics and affect is it has this nice kind of broad capture of the kinds of affectivity that agents can experience.
[[start:3097688][end:3106934]] So when we talk about affectivity, we're not just talking about full blooded emotions or even just moods, but we're talking about what?
[[start:3107052][end:3121142]] One of the things I kind of drew attention to in the lecture was Matthew Ratcliffe's work on existential feelings, which I think is just such the connection between Active Inference and phenomenology that you find in some of this work is just insanely powerful.
[[start:3121206][end:3133626]] And it's one of the things that really drew me into the framework the second thing, just building one thing that I don't think I mentioned in the lecture is Active Inference.

52:13 [[start:3133738][end:3138190]] It has been described as a quintessentially metacognitive framework.
[[start:3138350][end:3154534]] So you have kind of built into the architecture, you have expectations over expect, so you have kind of predictions about predictions and this has proved to be just, again, just phenomenally useful for thinking about certain aspects of phenomenology as well.

52:34 [[start:3154572][end:3159590]] So yeah, I think that these are like real strengths of the framework.

52:45 [[start:3165140][end:3171600]] Okay, I don't know how we're doing for time.
[[start:3171750][end:3174256]] Are we strictly limited on or can.

52:54 _Avel:_
[[start:3174278][end:3177190]] We we are not as far as I know.
[[start:3177800][end:3178980]] Daniel.

53:01 _Ben:_
[[start:3181480][end:3187270]] Well, I can probably do I definitely do another 15 if anybody has any more questions.
[[start:3187640][end:3193284]] And people, I should say as well, that doesn't mean that we're all held captive to my time frame.
[[start:3193332][end:3202620]] So if people do need to leave within the next five or ten minutes, that's absolutely fine, but I'm certainly happy to carry on if anybody has any more questions or comments.

53:27 _Lee:_
[[start:3207060][end:3229796]] If no one else has got any, I would quite like to go back to earlier in the discussion you were talking about the value of uncertainty because in organizations in which I'm working with, we often have conversations about uncertainty and what we find is over time there tends to be a drift towards risk aversion.
[[start:3229908][end:3242312]] So we're working with a large international construction company at the Minute, and they used to have a culture in which innovation was quite well embedded.
[[start:3242376][end:3270900]] And over time, it's kind of drifted towards very, very risk averse culture where actually, rather than learning through the process and being able to tolerate uncertainty around opportunities and what can be accomplished and that kind of surveillance that comes with the intrinsic reward, I suppose, of being able to reduce uncertainty about capabilities to a situation where they're trying to anticipate all of the risks upfront before they even get involved in the project.

54:30 [[start:3270970][end:3273616]] So there's some kind of valence switch.
[[start:3273728][end:3289184]] Mark and you mentioned David Blaine earlier and something about the context there was a switch in valence from yeah, this is a kind of a play, this is a safe thing to do, to actually know this has real consequences.

54:49 [[start:3289332][end:3297100]] So I'd like to explore that a little bit more actually, if anyone's got kind of any insights or papers or comments.

55:00 _Ben:_
[[start:3300000][end:3303090]] Yeah, I think that's a really interesting question, actually.
[[start:3304900][end:3317380]] It seems like one of the things we've been talking about is this connection between uncertainty, prediction, error, minimization and affectivity in individual agents.
[[start:3317450][end:3324576]] And it sounds like what you're asking is how does that translate to collectives?
[[start:3324688][end:3338360]] So one of the things about Active Inference that we're going to see in subsequent weeks is how it scales up to kind of larger systems like companies or groups that are trying to achieve some kind of shared goal.
[[start:3339820][end:3344764]] How does the value of uncertainty translate onto how is it scalable in that sense?

55:44 [[start:3344802][end:3345390]] Right?
[[start:3345760][end:3347470]] Would that be a fair kind of.

55:48 _Lee:_
[[start:3348640][end:3350430]] Yeah, I guess so.

55:55 [[start:3355940][end:3366388]] Uncertainty often when it's talked about uncertainty is talked about as risk, which is, I suppose, is predictions or anticipation of outcomes that we don't want.

56:06 _Darius:_
[[start:3366474][end:3366916]] Right.

56:07 _Lee:_
[[start:3367018][end:3375824]] Whereas there's also positive uncertainty, which is, I suppose, simply stated opportunities through curiosity.
[[start:3375952][end:3388600]] What might we be able to achieve this kind of novelty seeking, I guess that new opportunities that we haven't exploited, and they're just in the kind of organizational systems.
[[start:3389500][end:3405570]] I think there are various pressures that cause it, but over time, you see these cultural shifts towards a very kind of risk averse where the valence is obviously quite negative, quite an unpleasant feeling for people.

56:47 _Mark:_
[[start:3407780][end:3408928]] Yeah, this is good.
[[start:3409014][end:3411090]] This is right at the heart of my current work.
[[start:3411620][end:3412608]] I'm really interested.
[[start:3412694][end:3421136]] So we just had a big stint where Active Inference models were starting to be used in computational psychiatry, especially for pathological disorders.
[[start:3421248][end:3425780]] So addiction, depression, disassociative disorders, OCD PTSD.

57:07 [[start:3427800][end:3435096]] It's quite a sexy framework for thinking about some of the ways that the cognitive system breaks down and the sort of new move right now.
[[start:3435118][end:3437860]] I mean, we have a collection coming out right now in Neuroscience of Consciousness.
[[start:3437940][end:3456168]] Is to think about these things in terms of, okay, if we are predictive systems and we have a sufficiently rich model of how that system works in a particular niche, what sorts of ways can we intervene on that system in order to have positive outcomes, rather than just modeling what the negative outcomes are?
[[start:3456274][end:3458224]] And I hear that a lot in what you're saying now.
[[start:3458262][end:3460976]] So I'm just going to drop one link for you there.

57:41 [[start:3461078][end:3467948]] This is Casper Hess again wrote a very small paper with a nice little model called Sophisticated Affective Inference.

57:48 [[start:3468044][end:3473670]] Here's a little bot that tends towards catastrophe catastrophizing the future.
[[start:3474760][end:3480100]] If it's given like, fun medium fun medium fun dangerous.
[[start:3480260][end:3485850]] Over time, it tends to expect the dangerous one.
[[start:3487100][end:3497260]] Like after 10,000 iterations, it basically lives in the worst possible scenario, which is a nice little this is my wife, this is most people today.

58:17 [[start:3497410][end:3504724]] So the question is, I want to know, given the model, why does that happen and what can we be doing to intervene?
[[start:3504872][end:3511644]] And part of the answer is going to be we need to become more tolerant of uncertainty.
[[start:3511692][end:3514384]] That's one of the things that the system can be better or worse at.
[[start:3514502][end:3520020]] So this just takes the computational modeling and then looks to things that we already know about emotional regulation.
[[start:3520760][end:3522310]] That's part of the story.

58:43 [[start:3523480][end:3533336]] So we've done a little bit of work on this with our predictive dynamics of happiness and wellbeing, and Ryan Smith is definitely doing work on this with Active Inference and well being.

58:53 [[start:3533518][end:3536810]] So definitely check that out if you're interested here.
[[start:3538540][end:3544860]] I'll just flag one interesting thing here that relates just to what we were just talking about, about layers of modeling.
[[start:3545600][end:3548316]] One way that let's say two ways.
[[start:3548418][end:3550776]] There's two ways that a system, and it's probably going to be lots.

59:10 [[start:3550808][end:3556988]] But the two that come to mind that a system can become more tolerant to uncertainty is one exposure.
[[start:3557164][end:3561440]] So this is why exposure therapy might be useful for our kind of a system.
[[start:3561590][end:3569268]] You want to expose the system to volatility at the lower and middle levels of the hierarchy and have it turn out okay.
[[start:3569434][end:3579588]] So that one of the things that the system can come to predict is not only particular outcomes, but it can also predict how much error is involved in particular outcomes.
[[start:3579684][end:3595256]] So, for instance, when I used to give a pro talk, I was always really nervous, and I don't know if that ever really went away, but I've had so much exposure to the anxiety of giving a professional talk that basically I don't notice it anymore.

59:55 [[start:3595288][end:3600488]] But if you were to ask me at the beginning of my talk, mark right now, what's your phenomenology?
[[start:3600664][end:3604536]] And I sort of meditatively looked, I'd probably say, yeah, I'm nervous.
[[start:3604648][end:3607052]] But if you hadn't have said that and you were just like, hey, what's up?
[[start:3607106][end:3608720]] I've been like, oh yeah, I'm great.
[[start:3608870][end:3609424]] It's all good.

1:00:09 [[start:3609462][end:3610588]] I don't even notice it anymore.
[[start:3610684][end:3617828]] That's because the system knows that I have errors go up, but as soon as I start talking, they drop away.
[[start:3617914][end:3622256]] And because I know the arc that even error in the system, it becomes non newsworthy.
[[start:3622288][end:3626288]] It's no longer interesting volatility to be tracking that's just from exposure.
[[start:3626464][end:3634596]] So what's happening is you're having errors at a lower or middle level that a higher level is now modeling, saying when we come here, we should expect this arc of error.

1:00:34 [[start:3634628][end:3639370]] Same thing when you work out like real gym rats, they can feel good.

1:00:42 [[start:3642400][end:3655360]] You're having your system right, but at the higher level, it's now learned not only that that has a natural arc, but that that's a good sign at a higher level.

1:00:55 [[start:3655430][end:3662976]] So now you're getting positive prediction error slope high and negative prediction error slope low.
[[start:3663158][end:3666160]] Okay, so one exposure.
[[start:3666320][end:3669840]] Two, you can model your own responses.
[[start:3669920][end:3672900]] This is something Ben and I work on with horror movies.

1:01:15 [[start:3675800][end:3682900]] You can take an active role in mindfully observing your own reactions to volatility.
[[start:3683060][end:3685956]] And this comes up in our paper on horror.
[[start:3685988][end:3688120]] We've already dropped the link today if you want to check it out.
[[start:3688190][end:3692232]] Something really special happens when the system models its own reaction to volatility.
[[start:3692376][end:3703536]] It starts to learn that even reactions to volatility, they don't need to be compounded up into dangers, that it's okay to be uncertain at certain levels of the system.

1:01:43 [[start:3703718][end:3711650]] So how that translates into business, I'm not sure, other than I know tolerance to uncertainty is a marker of business success.
[[start:3712180][end:3722100]] And I suspect the framework in a fit with lots of mindfulness work about learning to tolerate uncertainty.

1:02:02 _Lee:_
[[start:3722440][end:3728932]] Is there anything about the role of language in kind of modulating those metacognitive?

1:02:09 _Mark:_
[[start:3729076][end:3730024]] Oh, it's good.

1:02:10 _Avel:_
[[start:3730142][end:3736170]] If I may, I was preparing an answer on that specifically, and I was nervously waiting for opportunity.

1:02:16 _Ben:_
[[start:3736540][end:3737530]] Sorry, Mark.

1:02:22 _Avel:_
[[start:3742400][end:3753708]] Meta in terms of evolutionary cognitive archaeology, we don't know when language emerge, but we do know that, let's say an encouraging semantic system.
[[start:3753794][end:3760400]] So you can build things in language, and you can expect things in the world to correspond to things in language.
[[start:3760820][end:3775924]] So, for example, if you that's abstract, as I say, it's abstract, but you can, for example, have a self identity, and I'm a French, and I communicate with the expectation that are embedded in that identity with other people.
[[start:3776042][end:3777844]] And that means we communicate over norms.
[[start:3777892][end:3781656]] So we have specific expectation of what we will do.

1:03:01 [[start:3781838][end:3788280]] And those expectations, they become embedded in specific symbolic markers that are embedded in language.
[[start:3788960][end:3814240]] And something that the thing that it was strongly evoked in my mind when you talked of tolerance to insecurity is that as far as documented history goes, Europeans well, Indo Europeans, they are pretty strong on the idea that things have a nature and they act lawfully.

1:03:34 [[start:3814680][end:3819760]] And their nature and their laws, they somehow correspond to linguistic categories.
[[start:3819920][end:3829240]] So I can say stuff like chickens quack, and that's a proper explanation of what are chicken and why they quack.
[[start:3829980][end:3839536]] And if you look in Chinese philosophy, as far as written history goes, you have a much accent on Wei Wu Wei.

1:03:59 [[start:3839588][end:3845100]] So a poor translation would be effortless action.
[[start:3846400][end:3850296]] Closer translation would be action without action.
[[start:3850488][end:3864790]] So it's something that is quite close to the phenomenology of flow in that you observe yourself doing things and you do not apply a conscious effort to the flow of what you're doing.
[[start:3865560][end:3871332]] And that looks like something that is closer to the phenomenology you'd expect.
[[start:3871386][end:3898156]] If you apply recursive preactive cognition with less or less heavy or more effectively integrated symbolic concurring like use of language as something that you actually expect to be meaningful and to constrain strongly your actions and marginally, I'd expect, very strongly expect that linguistic categories will map and what you build with it.

1:04:58 [[start:3898178][end:3903420]] So, I don't know, self identities, plans, whatever will map cleanly onto what you observe.
[[start:3903500][end:3907570]] You will be very anxious about things, because that does not happen usually.

1:05:10 [[start:3910020][end:3924676]] And yeah, besides grand discourse on interpret traits, which are usually not that constructive sorry, I got lost because I did.

1:05:24 _Mark:_
[[start:3924698][end:3930330]] Not let me just say one thing before we move off this point.
[[start:3931340][end:3935396]] A simple way that language might help is by invoking cognitive flexibility.
[[start:3935508][end:3942844]] So oftentimes we think about the management of error being either updating predictions or acting on the world.
[[start:3943042][end:3944072]] That's the dyad.

1:05:44 [[start:3944136][end:3951868]] Usually what it overlooks is the third one, which is we can also manage volatility by redeploying precision in a better way.
[[start:3952034][end:3963264]] So rather than just updating your model to fit the world or updating the world to fit your model, you can just change the set of what matters so that you're not really updating the model and you're not really changing the world.
[[start:3963302][end:3965308]] You're just changing the problem landscape.
[[start:3965404][end:3967620]] And that's something language allows us to do.
[[start:3967690][end:3976832]] It's maybe one of the really amazing things that language allows us to do is we can use language to bootstrap that kind of precision adjustment.

1:06:16 [[start:3976896][end:3980744]] So if the train doesn't come on time, we both notice it.
[[start:3980782][end:3980984]] Okay.
[[start:3981022][end:3983492]] And we feel bad that's perceptual updating.
[[start:3983636][end:3987044]] We might go and get a taxi that's active updating.

1:06:27 [[start:3987172][end:3996776]] But I might just say to you, wow, look, isn't it lovely that now we get a little bit more time to read our book or to continue our conversation or let's finish our coffee with a little bit of ease.

1:06:36 [[start:3996808][end:3998060]] I mean, we get an extra 20 minutes.
[[start:3998130][end:4002012]] Now even just saying that redeploys precision over the problem.
[[start:4002066][end:4006690]] Space now the train being late isn't volatility in the system.
[[start:4007220][end:4011836]] The train being late is signaling to the system that a better than expected slope has been achieved.
[[start:4012028][end:4013136]] Isn't that so interesting?

1:06:53 [[start:4013238][end:4018896]] The exact same occurrence is either undigestible volatility, right, like you're going to be late.
[[start:4018928][end:4019600]] Oh my goodness.
[[start:4019680][end:4026676]] Or it's an opportunity for an improvement in the system, which is now you get more time with the person that you're taking the train with.
[[start:4026778][end:4034552]] And that was just a matter of linguistic perturbance of the way that precision is being looking at.
[[start:4034606][end:4042750]] If you wanted to dig into the research here, I would look up cognitive flexibility and language or coaching cognitive flexibility is such a good point here.

1:07:25 _Avel:_
[[start:4045520][end:4050952]] So you have a paper by Nick Clark on this specific encouraging role of language.
[[start:4051016][end:4062876]] And something it entails is that basically you get like if the active infrastructure is correct, you flexibly predict a flow in the interoceptive proprioceptive exteriorceptive.
[[start:4062908][end:4064864]] Is that even a thing space?
[[start:4065062][end:4071344]] And that is what builds an integrated experience and integrated cognition and language.
[[start:4071392][end:4073024]] It adds another layer of complexity.

1:07:53 [[start:4073072][end:4081016]] If you can just talk to yourself in your head, that is another dimension that you can predict and that can be coherent or incoherent with your world.
[[start:4081198][end:4091228]] And so that is an extremely powerful encouraging system because I just have to tell a plan to myself and boom, that pushes me, nudges me nicely throughout the plan.
[[start:4091314][end:4097144]] But then you can have a different level of meta expectation over how language corresponds to reality.
[[start:4097192][end:4109664]] And I'd say a very strong factor of aversion to uncertainty is whether you expect your plans or your linguistic structure to nicely map onto reality because it will not happen.

1:08:29 [[start:4109782][end:4115036]] But if you expect strongly that it will be the case, you will have to make it happen somehow.

1:08:35 [[start:4115148][end:4124292]] And here you will adapt rigid strategies and you will lose flexibility, but also language necessary for flexibility to be the case in the first place.
[[start:4124346][end:4127960]] So it's about coupling between dimension of cognition.

1:08:50 _Ben:_
[[start:4130540][end:4130856]] Yeah.
[[start:4130878][end:4141256]] And I would just kind of risk and danger are two things that I've been really interested in across a kind of variety of different contexts.
[[start:4141288][end:4145548]] And I would say some of the.
[[start:4145554][end:4161152]] Things that have been said like how you can influence the system by externalizing things through language and the different strategies that systems, whatever scale they're on, have minimizing prediction error, minimizing free energy.
[[start:4161286][end:4165344]] But also I would just emphasize the importance of external context here as well.

1:09:25 [[start:4165382][end:4172432]] So even in the case of a collective like a business, you still have to take into account the environment in which the business is operating.
[[start:4172496][end:4177100]] And I've been really interested in a particularly extreme example of context.
[[start:4177280][end:4199020]] I used to still do some work in philosophy of sport and I've been really interested in dangerous sports and why there seems to be this insane contextual effect where within a very kind of narrow contextual band of sporting practice, people seem willing to take on risks that outside of that context would just be completely insane.

1:09:59 [[start:4199680][end:4215620]] And I think this is something that's probably going to come up again in subsequent weeks as well here when we talk about the way that expectations on an individual or a collective basis can be set through other minds.

1:10:19 [[start:4219400][end:4223012]] So what somebody else expect myself to do?
[[start:4223146][end:4224710]] And so on and so on.
[[start:4226120][end:4227780]] Darius, you've had your hand up a while.
[[start:4227850][end:4229112]] Do you want to jump in?

1:10:29 _Darius:_
[[start:4229246][end:4229960]] Yes, please.

1:10:30 [[start:4230030][end:4236760]] I'm not sure this is the sort of grand synthesis of any of this, but flow was mentioned.
[[start:4236830][end:4243596]] As I said, it's a kind of pet topic of mine and something that.

1:10:43 _Ben:_
[[start:4243618][end:4245192]] We know about flow.

1:10:45 _Darius:_
[[start:4245256][end:4262268]] And this is why it's integrated into this idea of language and agency, is that at least in its original conception, success, mahali, and the sort of qualitative experience associated with flow, you would find stuff like not only the dilation of time, but also the reduction in self consciousness.
[[start:4262444][end:4271188]] And now this is sort of picking up a lot of work that happens at UCL and people like Jeremy Skipper how integrated language is into the sense of self.

1:11:11 [[start:4271354][end:4290510]] And it seems to me, and this is kind of shooting from the hip, that all of these very deep rooted, I guess they're kind of psychotechnologies the self language seem to dissipate at this goldilocks zone, at this point of at this edge of criticality, at this flow state.
[[start:4291040][end:4307068]] Which makes me think if the flow state is a phenomenological offshoot of being optimally reducing prediction error, what is the kind of role of the concept of the self or linguistic functions?

1:11:47 [[start:4307244][end:4313250]] Because it seems to me that that becomes a regulatory function when that optimality is reduced, when stuff starts going wrong.
[[start:4313940][end:4319408]] So I think you can also think about this in the kind of Heideggerian or draythe's sense of just opening a door.
[[start:4319504][end:4321988]] You only start to represent the door in yourself.

1:12:02 [[start:4322154][end:4326740]] You only give it the linguistic object of a door when you can't open it.
[[start:4326810][end:4330884]] When you open a door standard, there is no representation going there.
[[start:4330922][end:4332952]] I mean, you could even argue there's no qualia there.
[[start:4333006][end:4346328]] So I'm wondering how deep that runs and what we can say about the role of agency, selfhood, maybe even consciousness because they don't seem to be that prevalent, at least from my understanding.
[[start:4346504][end:4348700]] When we are at the edge of criticality.

1:12:29 _Ben:_
[[start:4349360][end:4357390]] The suggestion you're making there is it sounds like what you're saying that these things you call them psychotenologies, which I really like.
[[start:4357760][end:4362604]] Like language, like certain aspects of self modeling.
[[start:4362652][end:4381480]] They are a kind of scaffolding or like a ladder that you then kind of gets kicked away once you reach a certain kind of edge of criticality, like where the performance becomes I don't know what you're performing at such a level that you just don't need those scaffolding.

1:13:02 _Darius:_
[[start:4382060][end:4382664]] Yeah.
[[start:4382782][end:4393800]] Or the self regulatory mechanisms that we harness when we're not in flow are linguistic or agentic in essence.

1:13:13 [[start:4393880][end:4401340]] And you don't need that when you're at this edge of criticality.
[[start:4402820][end:4410944]] And I only postulate that because I'm only thinking, how deep does that go?
[[start:4411142][end:4416868]] Because I know, obviously the Active Inference framework is trying to tackle in some ways the hard problem as well.
[[start:4417034][end:4431496]] And there are some flotations of the idea, at least within the flow community, about the kind of I don't want to say elimination, but the moderation, the modulation of qualia under flow states.
[[start:4431678][end:4445708]] So could we also consider that to be a construct which happens when we're not necessarily optimally producing prediction error, a couple of things.

1:14:05 _Ben:_
[[start:4445794][end:4451348]] So I'm certainly not the person to stop talking about consciousness, so I won't.
[[start:4451544][end:4459292]] But some of the readings that I mentioned in the lecture might be interesting for you on this topic.
[[start:4459356][end:4486628]] So if we're talking about certain structures that seem very pervasive in our phenomenology and how those structures can sometimes kind of dissolve away and how that might be accounted for under an Active Inference framework, there's some really interesting work on psychedelics by George Dean and some of George Dean's co conspirators.
[[start:4486724][end:4509004]] I know Mark and Sam Wilkinson worked on a paper with George so George Dean's done some work on kind of ego dissolution and certain kinds of experiences related to selfhood, kind of and I kind of don't want to overstep the mark, but I think they fall generally under this kind of rebus model of psychedelic efficacy.

1:15:09 [[start:4509052][end:4517200]] So I don't know if people are familiar with this, but this kind of finds natural articulation through predictive processing and hierarchical self modeling and that kind of stuff.

1:15:17 [[start:4517270][end:4520124]] I also wanted to really quickly flag on this topic.
[[start:4520252][end:4525284]] I'll find the paper and I'll put it up on the coder because I don't think I'll be able to find it quickly enough now.
[[start:4525322][end:4535400]] But there was a paper that came out very recently that showed the efficacy of internal self talk on sports performance.

1:15:37 [[start:4537660][end:4555984]] They did an experiment with cyclists and they found that when cyclists were allowed to engage in kind of constant self talk with them, like an inner monologue in their head, their performance at cycling was measurably boosted, which I thought was really interesting and kind of relevant here.
[[start:4556102][end:4567716]] But it's interesting because it sounds like it might prima facia be in tension with what we were saying about flow states as well.
[[start:4567738][end:4567924]] Right.
[[start:4567962][end:4582680]] So if the real edge of performance is a place where these structures of phenomenology bleed away, it kind of calls into question, like, to what extent are these psychotechnologies effective and in what way are they effective?

1:16:23 [[start:4583740][end:4587690]] There's just a whole kind of universe of really interesting questions there.

1:16:28 _Avel:_
[[start:4588380][end:4594620]] So, if I may, self food, indirectly will be the central topic of the last two sessions.
[[start:4595520][end:4614344]] My position about it is that self food, in a sense, we use all of the time, is a quite high level construct that emerges from the ability we have to compare our activity to a socially embedded model of our activity.
[[start:4614492][end:4626352]] So that is something that is quite specific to humans because of their linguistic ability and or because of their tendency to what Thomaslo calls shared intentionality.
[[start:4626416][end:4628970]] So the ability to collectively define an.

1:17:11 [[start:4631180][end:4641368]] So basically, this is something that enables a very deep, very profound and robust transmission of cultural knowledge and transmission of norms.
[[start:4641464][end:4643980]] This is what enables the construction of norms.
[[start:4645360][end:4662784]] But it's quite heavy cognitively and it is predictable that if you're busy comparing what you do to what an idealized version of yourself is doing, you're going to invest less creative energy in actually doing the thing that you would if you just did a thing.

1:17:42 [[start:4662982][end:4670870]] So I'd say you have a pretty direct entailment of this flow thing from this model.

1:17:55 _Ben:_
[[start:4675720][end:4676228]] Yeah.

1:17:56 _Avel:_
[[start:4676314][end:4676708]] Yes.
[[start:4676794][end:4677744]] This is my conclusion.

1:17:57 _Ben:_
[[start:4677792][end:4678390]] Sorry.
[[start:4680120][end:4688024]] So we've run almost 30 minutes over time and I know Mark's had to go and I'm going to have to go very I think I pretty much have to go.

1:18:08 [[start:4688062][end:4695710]] So I just wondered if anybody has any final kind of quick questions or comments, maybe we can move towards wrapping it up.

1:18:18 _Daniel:_
[[start:4698560][end:4706130]] I'll make a few comments, but Ben, you're welcome to leave and other people welcome to stay if they would like.

1:18:27 _Ben:_
[[start:4707700][end:4708770]] Thank you for.

1:18:32 _Daniel:_
[[start:4712180][end:4717856]] Well, first, just on a logistical note, there was a little bit of lag.
[[start:4717968][end:4736724]] So I'll encourage everyone who's listening, as well as who's participating, that we eventually plan to, as with all of our live streams, develop a transcript which will be curated and published, and eventually not so far away in the future, that'll be enabled with speech modeling to generate podcast quality audio.
[[start:4736852][end:4739560]] So the future will be smooth, we promise.
[[start:4740380][end:4748040]] But a few really interesting pieces that I picked out while I was embodying and listening.
[[start:4749420][end:4758028]] So, Regina, you opened the discussion with surprise and creativity, and indeed, it sounds like it's going to be attention.

1:19:18 [[start:4758124][end:4764220]] How can a framework whose imperative is bounded surprise as opposed to, say, maximized reward?
[[start:4764380][end:4770704]] How can a framework whose imperative is surprise, minimization and bounding be used to generate novelty?
[[start:4770752][end:4774224]] And I felt like people provided a lot of really cool answers.

1:19:34 [[start:4774352][end:4781884]] And one other thing it reminds me of is Doug Hofstadter's notion of spectishnish.
[[start:4781952][end:4788692]] I don't know, how do you pronounce it, but sphexishness, and it's the specs wasp.

1:19:48 [[start:4788836][end:4798392]] And so he says, well, forget this whole creativity thing, because when we talk about creativity, it's like some sort of pantheon, like divine status.
[[start:4798456][end:4801116]] The muses have to be called in.
[[start:4801218][end:4804540]] And so then, oh, that's not real creativity, and this isn't real creativity.
[[start:4804620][end:4808108]] So instead, he says, well, let's just focus on what would be the opposite.
[[start:4808284][end:4815660]] And that would be the rote procedural following, even when there's an opportunity for what we would call creativity.

1:20:15 [[start:4815820][end:4817048]] And then there's a continuum.
[[start:4817084][end:4819056]] So why does somebody paint that painting?
[[start:4819168][end:4821328]] Well, why didn't they invent a new genre?
[[start:4821424][end:4823668]] Well, why didn't they invent a new media?
[[start:4823834][end:4839204]] And so all activity is existing within this continuum of creativeness, which has many features such as generativity and productivity, but also novelty, but abounded novelty.

1:20:39 [[start:4839252][end:4851824]] It's not creative to knock the chessboard pieces off in a way that there might be an elegant chess move who only somebody in a certain cognitive setting could detect the aesthetics of.
[[start:4851862][end:4853330]] But I think that was awesome.
[[start:4854100][end:4862370]] And then the second piece that really was powerful was what mark's train.
[[start:4862900][end:4883000]] I guess the trains don't run on time where Mark is, but that's okay, because he was able to, rather than treat that as an undigestible surprise, that was able to be basically cognitively metabolized into an opportunity for friendship through language as a social medium.
[[start:4883500][end:4888340]] And then he connected that to cognitive flexibility and coaching.

1:21:28 [[start:4888500][end:4894140]] And then I thought about self talk and our inner monologue inner voice.
[[start:4894800][end:4913730]] And then Darius, that was very provocative, that we aren't having self talk, potentially not even having a self in the flow, manifold experience of the self or the self talk, or again, potentially even the total actual self as a technology.

1:21:54 [[start:4914120][end:4947576]] And so then healthy self talk would guide us to the flow and be kind of like a self limiting technology because it would be used in order to not be needed to be used, which is kind of how we would hope adaptive technologies would be versus a maladaptive technology would be something that entrenches its own utilization potentially at the expense of the functionality.
[[start:4947768][end:4949992]] Kind of like doom scrolling status.
[[start:4950136][end:4951864]] But that's internal rumination.

1:22:31 [[start:4951912][end:4955360]] And those are the kinds of things that people have simulated in Active Inference.
[[start:4955700][end:4958412]] So those were some really cool pieces.
[[start:4958476][end:4960000]] That was a great discussion.

1:22:41 _Ben:_
[[start:4961060][end:4967284]] Could I just add something on the topic of creativity that I should have said earlier as well?
[[start:4967322][end:4975024]] Because I think it's really relevant to Regina's question and just the topic of creative and novel behaviors in general under Active Inference.

1:22:55 [[start:4975072][end:5000876]] I think that whenever we talk about especially artistic creativity, there's a tendency, even for people who are kind of very well burrowed into Active Inference and activism and these kinds of frameworks from cognitive science, I think there's a tendency to think of creativity as still like it's almost like the last bastion of internal cognitiveist thinking.
[[start:5001058][end:5004780]] We think creativity is something that happens in here and bursts outwards.
[[start:5004860][end:5010300]] And so how does that happen with this kind of whatever cognitive architecture we're positing?
[[start:5010460][end:5020064]] But there's really very cool work by I have to give a shout out to Mike Wheeler, who has written some papers on the extended mind and creativity.
[[start:5020192][end:5031896]] And one thing that's not really come up very much that I didn't get time to talk about in the lecture is this really nice natural marriage between the extended mind and Active Inference, something that Andy Clark has been working on.

1:23:51 [[start:5031918][end:5035016]] And I know he's going to be doing a lot more work on it.
[[start:5035038][end:5055680]] But the claim Wheeler makes and some others I think Joanna Zelenska has written a little bit about this as well, is the fact that creativity itself is just as subject to kind of material, the sculpting effects of material environments and sociocultural environments as everything else is.
[[start:5055830][end:5069204]] So creativity is not this kind of romantic with a capital R kind of internal process that kind of bursts forth, but creative thinking is just as much extended and embedded as everything else.
[[start:5069242][end:5073940]] And there's some really great examples in Mike Wheeler's essay.
[[start:5074280][end:5077190]] I don't know, is anybody familiar with the band Alt J?

1:24:37 [[start:5077640][end:5079116]] They're a British band.
[[start:5079168][end:5081080]] They were kind of really big a few years ago.
[[start:5081150][end:5085130]] They won the Mercury Music Award because they have a super original sound.
[[start:5085900][end:5089320]] So AltJ have this really quiet tinkling.
[[start:5089740][end:5090868]] Yeah, they are a great band.

1:24:50 [[start:5090884][end:5091876]] They're one of my favorites.
[[start:5091908][end:5101340]] And they have this really quiet tinky sound that everybody kind of assumed was just the result of some kind of internal genius on the part of the band.

1:25:01 [[start:5101840][end:5114460]] And as it turns out, AltJ, originally they tried to rehearse as an indie rock band, but they were confined to rehearsing in an apartment block, and they kept getting noise complaints.
[[start:5114620][end:5123200]] And so they ended up developing this quiet tinkly sound because it was the only sound they could rehearse that wouldn't get them kicked out of their apartment.
[[start:5123360][end:5139024]] And I think this is a really beautiful example of how even the most creative processes that seem, on the face of it, really creative, are in fact just a subject to these external kind of this kind of agent environment system that underpins the whole framework.

1:25:39 [[start:5139092][end:5142750]] So that's something that's going to apply to absolutely everything.

1:25:44 _Daniel:_
[[start:5144000][end:5144748]] Awesome.
[[start:5144914][end:5152896]] And just the last question, people are welcome to drop off the next section that we're heading into.
[[start:5152998][end:5158988]] I'll be doing the lecture that's going to be in August, and it's going to be on collective behavior.
[[start:5159084][end:5167220]] So what would people like to learn or focus on about collective behavior?

1:26:17 [[start:5177640][end:5189320]] Anyone who hasn't spoken or it can just be a thought question, but I haven't prepared the slides at all, so I'm happy to take suggestions.

1:26:32 [[start:5192620][end:5194590]] Yeah, Darius and then anyone else?

1:26:34 _Darius:_
[[start:5194960][end:5203260]] I think what might be interesting is if we're saying that these systems are all in the business of reducing prediction error, of self evidencing.
[[start:5203760][end:5217080]] Why do we see a diversity why do we see a diversity of social cultures, of norms, of standards at a global scale?
[[start:5217260][end:5232372]] Why do we not just see some homogeneous way to reduce picture there, which would manifest as the kind of singular culture which is in the kind of business of self evidencing?
[[start:5232516][end:5234250]] That just kind of popped in my mind.

1:27:16 _Ben:_
[[start:5236060][end:5236810]] Cool.

1:27:21 _Daniel:_
[[start:5241920][end:5246024]] Anyone else want to give a thought on collective behavior or on any other aspect?
[[start:5246152][end:5247710]] Otherwise it's been great.

1:27:28 _Avel:_
[[start:5248320][end:5261330]] I'd like to make a comment of creativity, but does anyone like at the moment, if you want to make a comment on the next session, I want to put that.

1:27:42 _Michael:_
[[start:5262900][end:5264290]] Okay, go for it.

1:27:45 _Avel:_
[[start:5265460][end:5280890]] I'd say that to complement what Ben said, that creativity is intrinsically very hard to model because by definition, creativity is something that brings about something new, let us say.

1:28:01 [[start:5281340][end:5288410]] And the mathematics we have to describe physics and life, they are not very good at new things.
[[start:5289340][end:5305070]] Because the most basic tool you have, the basic way to represent a system that literally everyone uses, is a stead space, which is the least of all possibilities of a system.
[[start:5305440][end:5311404]] If you say something is creative, you're likely to think that it means it can bring about new possibilities.
[[start:5311532][end:5316824]] And this intuition, it conflicts directly with the very basic use of math.
[[start:5316972][end:5317924]] Describe it.

1:28:38 [[start:5318042][end:5326960]] So it is basically the same issues I was referring to earlier when I talked about the comparison between Active Inference and an activist.

1:28:47 [[start:5327120][end:5337364]] So let's say activity biology inspired model of cognition, and a core concept historically in those circles is autopoiesis.
[[start:5337412][end:5342940]] So the ability of the living to self create, literally, this is Greek for self creation.
[[start:5343360][end:5353096]] And you had a lot of drift and conceptualization and ambiguities that were resolved or not resolved and led to the crisis of framework, blah, blah, blah.
[[start:5353208][end:5357476]] But today we talk of autonomy rather than autopoiesis.

1:29:17 [[start:5357608][end:5367090]] And we define autonomy as the property for a system of constraints over the activity of a system to reproduce themselves.
[[start:5367480][end:5379712]] And because we're talking constraints, just the ability to influence causality outcomes, there is no really a prior that dynamics in this space would be conservative.
[[start:5379776][end:5385144]] So we have a possibility for constraints to bring about new things and reconfigure themselves.
[[start:5385342][end:5389050]] And the notion of Hydrancy ADUs is based on that.

1:29:49 [[start:5389500][end:5400028]] It's the ability to, let's say, reconfigure constraints in your environment, and so is the notion of creativity, which would be likely a very close proxy to that.

1:30:00 [[start:5400114][end:5404110]] But it's something that we do not know how to present.
[[start:5405220][end:5410316]] And most of the mathematics that exist are structurally enabled, represent.
[[start:5410508][end:5413330]] And so, yeah, that's a big one.

1:30:17 _Daniel:_
[[start:5417400][end:5418390]] So true.

1:30:21 _Ben:_
[[start:5421000][end:5421860]] Michael.

1:30:26 _Michael:_
[[start:5426600][end:5427396]] Good to be here.
[[start:5427418][end:5428580]] Sorry I was late.
[[start:5429800][end:5435320]] What comes to mind for me at the know, I mentioned units of collective, like, what is it, a we?
[[start:5435390][end:5436840]] Is it a we a pair?

1:30:39 [[start:5439420][end:5440584]] What are the units of we.
[[start:5440622][end:5442910]] And any thoughts or insights about that?
[[start:5444000][end:5458944]] The stages of the emergence of formation into a collective from a me to a we, for example, or god, I had one was on the tip of my tongue, and it just escaped me.
[[start:5459062][end:5459730]] Oh.
[[start:5460740][end:5495740]] This idea of precision that I think it was Mark Miller was talking about, or Matt saying at the if there's options in the looking at collective what might be some of the most well understood limiting beliefs about when we use language of collective that keeps us repeating the same blind spots.

1:31:37 [[start:5497520][end:5505310]] And how might we think differently about collective so that we escape those predispositions, if you will?
[[start:5505760][end:5506770]] Makes sense.

1:31:49 _Daniel:_
[[start:5509700][end:5511824]] They'll do what I can do in.

1:31:51 _Michael:_
[[start:5511862][end:5515392]] The solo lecture, and I'll look forward.

1:31:55 _Daniel:_
[[start:5515526][end:5517884]] To the conversation where we can unpack.

1:31:57 _Darius:_
[[start:5517932][end:5518530]] It.

1:32:00 _Michael:_
[[start:5520260][end:5520812]] Exciting.

1:32:00 [[start:5520876][end:5521664]] Thank you for doing it.
[[start:5521702][end:5523376]] I'm looking forward to it.

1:32:03 _Daniel:_
[[start:5523478][end:5524336]] Yeah, it's awesome.
[[start:5524438][end:5526690]] Nathan or David, you want to add anything?

1:32:12 [[start:5532170][end:5533414]] All right, then.
[[start:5533452][end:5534150]] Thank you all.
[[start:5534220][end:5536902]] Hope everyone is enjoying the course so far.
[[start:5536956][end:5539414]] Thanks, Avel, again for coordinating it.
[[start:5539452][end:5542482]] And to Ben for this great section.

1:32:22 [[start:5542626][end:5545320]] Now you can put on your student hat again.

1:32:26 _Avel:_
[[start:5546010][end:5547750]] And to you for organizing.

1:32:28 _Daniel:_
[[start:5548650][end:5549318]] Thank you.
[[start:5549404][end:5550214]] See you all next time.

1:32:30 _Francesco:_
[[start:5550252][end:5550840]] Thanks.

1:32:31 _Mark:_
[[start:5551610][end:5552210]] Bye.

1:32:32 _Michael:_
[[start:5552290][end:5553080]] Thank you.

1:32:34 _Darius:_
[[start:5554010][end:5554660]] Thanks, everyone.
