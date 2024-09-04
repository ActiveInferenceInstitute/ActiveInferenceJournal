
00:00 _Daniel:_
[[start:410][end:17710]] All right, the next presentation is by Sanjeev Namjoshi, and this presentation is going to be called developing next gen Active Inference Tools, broadening Accessibility, Educational Resources, and the Software Ecosystem.

00:22 [[start:22440][end:28470]] I'm going to start this talk right now.

00:32 _Sanjeev:_
[[start:32720][end:35612]] Hello everyone, and thank you for being here.
[[start:35746][end:37768]] My name is Sanjeev Namjoshi.

00:37 _Daniel:_
[[start:37864][end:38796]] I'm just going to restart it.

00:38 _Sanjeev:_
[[start:38818][end:40876]] Machine learning engineer working at the AI.

00:40 _Daniel:_
[[start:40908][end:43680]] Services firm just because it's a little quiet.

00:47 [[start:47310][end:49500]] All right, restarting the talk.

00:56 _Sanjeev:_
[[start:56140][end:58972]] Hello everyone, and thank you for being here.
[[start:59106][end:69840]] My name is Sanjeev Namjoshi, and I'm a machine learning engineer working at the AI services firm Kung Fu AI, where I primarily focus on computer vision projects.
[[start:70340][end:80240]] Today I'm going to be talking to you about my progress toward providing greater accessibility, visibility, and knowledge of active inference and the free energy principle.
[[start:80820][end:94696]] I'm excited to be presenting this material at the active inference symposium this year because the idea of an enacted ecosystem of shared intelligence perfectly captures the philosophy that underlies the projects I'm currently engaged with.
[[start:94878][end:109820]] I've spent the last seven months on sabbatical for my job to work exclusively on an active inference textbook and related tools, presenting chapter presentations, code reviews, and receiving feedback weekly at the active inference institute.

01:50 [[start:110640][end:119096]] The institute has provided a space where interdisciplinary research can flourish as the connections and influences of active inference spread to other fields.

01:59 [[start:119208][end:125872]] It has consistently fostered the spirit of collaboration and shared intelligence that I wish to embody in my own work.
[[start:125926][end:134980]] As part of this ecosystem, I intend to continue closely working with the Institute to provide materials that will bring active inference to a much wider readership.
[[start:135480][end:152440]] I originally chose this project when I saw the great potential in the active inference field and couldn't help but make a comparison to the state of deep learning in 2006, when neural networks were one of just many possible models rather than the dominant choice in academia and in industry.
[[start:153660][end:164430]] This, of course, all changed in 2006 when Hinton and his colleagues released the Deep Belief Network paper, which is generally understood as the start of deep learning as we understand it today.

02:45 [[start:165040][end:175810]] After some hardware innovations and the release of the Wellknown ImageNet Library, we started to see coverage and success of AI in the news as well as in academic research.
[[start:176260][end:186500]] But in 2012, deep learning truly provided its value with AlexNet, and for the first time, deep learning achieved better than human performance on image detection tasks.

03:08 [[start:188440][end:189892]] But this was just the start.
[[start:190026][end:194468]] What followed was a proliferation of deep learning all across industry and research.
[[start:194634][end:203370]] I've added in some Wellknown milestones just to highlight the explosion of progress in deep learning in the last decade, though there is so much more here that we could discuss.

03:23 [[start:203900][end:206644]] So what about the state of active inference as a field?
[[start:206782][end:211260]] From my perspective, active inference lies in the same position as deep learning.
[[start:211330][end:229280]] In 2006, influential and on the brink of exploding in popularity, this paper which is from contributors at the Active Inference Institute, shows the current growth of publications in the institute and its community in active inference.
[[start:229620][end:234820]] In the last three years, the active inference field has seen a number of important milestones.
[[start:235560][end:239876]] Here I show just a few that broaden the scope and attention to the field.

04:00 [[start:240058][end:244196]] We had the first International workshop on Active Inference in 2020.
[[start:244378][end:249924]] We had the first active inference symposium and the founding of the active inference institute.

04:10 [[start:250052][end:252090]] Then called the active inference lab.
[[start:252700][end:269760]] We had the release of the Par at all 2022 textbook and the Pymdp Python package, and I see myself now as perfectly poised to bring active inference to greater visibility and attention.
[[start:270180][end:280348]] This is in part because of the current academic interest in deep reinforcement learning and generative modeling working alongside the institution and other organizations.

04:40 [[start:280444][end:292340]] My aim here is to provide some of the fundamental materials to capture the attention and notice of machine learning researchers and students to bridge this gap to bring active inference into its renaissance.

04:55 [[start:295000][end:302120]] To this end, I've been working for the past seven months on Sabbatical to finish work on a comprehensive textbook.
[[start:302620][end:320620]] The aim of the textbook is to provide the tools to bring active inference to a wider audience, primarily those in machine learning research and applied fields such as robotics, and to decrease the challenge in learning the material largely by separating it from much of the neuroscience background that is usually a prerequisite.

05:21 [[start:321600][end:337940]] This decrease in prerequisites means labs will have to spend less time helping students becoming acquainted with the field, and researchers outside of neuroscience will find this book an accessible entry point that uses terminology familiar to machine learning rather than neuroscience and fMRI image analysis.
[[start:338920][end:342980]] All derivations are in one place currently in the field.
[[start:343050][end:353320]] Many derivations are spread across different papers, even behavioral papers instead of just technical ones, and it's hard to know where to look if you want to understand a particular equation or concept.

05:54 [[start:354620][end:363660]] Part of the success of deep learning in the last decade has come directly from focusing on narrow improvements to specific aspects of the modeling.
[[start:364000][end:374880]] There are many open questions in areas of research, such as how to prune policy trees, exploring second order optimization rules for state and parameter updates, and scaling active inference.
[[start:375620][end:385060]] The increased accessibility for researchers would also lead to many new industry applications, such as autonomous vehicles, robotics, video game design, and AI.

06:25 [[start:385880][end:395880]] The textbook would also put a spotlight on Bayesian mechanics and invite contributors and contributions from researchers as this exciting nascent field grows and develops.
[[start:397420][end:408424]] Part Four is largely a literature review and can be very helpful to those writing about active inference from fields such as philosophy, psychology, sociology, and many others.

06:48 [[start:408622][end:425490]] And the historical context sections that are part of this book provide a lot of that context, as Active Inference is built upon decades of research in neuroscience, psychology, and many other fields, and also draws upon current work in many fields that have emerged in the last 25 to 30 years.
[[start:426740][end:435190]] Finally, LaTech reproducibility may offer interesting ways to rearrange the book and integrate it with the code for an online only experience.

07:19 [[start:439960][end:444868]] Now I'd like to share with you some of the progress of my textbook and the general structure.
[[start:445044][end:447748]] The textbook is divided into four parts.

07:27 [[start:447924][end:451860]] The first part introduces fundamental concepts to set the stage.
[[start:452020][end:463900]] In particular, I have focused here on presenting wellknown statistical ideas from the perspective of an agent modeling its environment, who states it must infer from an observed noisy signal.
[[start:464720][end:476720]] The second part focuses on continuous and discrete state space formulations of active inference, where the algorithm of focus for the continuous state space formulation is active generalized filtering.

07:57 [[start:477140][end:488420]] Part three, which I'll begin writing in a couple of months, focuses on a sketch of Bayesian mechanics and the required background designed with the knowledge this field is still dynamically, changing and evolving.
[[start:488920][end:500280]] Here I will focus on some of the fundamental concepts and ideas, as well as code simulations to allow readers to get a deeper and more intuitive understanding of some of these challenging ideas.
[[start:501020][end:510348]] Finally, part four is a systematic literature review that covers all the various applications and extensions to active inference that have been innovated in the last six to eight years.

08:30 [[start:510514][end:519650]] These applications include things like robotics, all the behavioral modeling and neuropsychiatry, and human and animal behavior, theory of mind, and so on.
[[start:520660][end:535350]] The extensions talk about how applications of active inference can be used to talk about dynamic systems more generally, and apply to things like ecosystems and to economies and other types of things like governance, and so on.

08:56 [[start:536840][end:544920]] As of this week, the rough drafts of part one and two are complete, and ten chapters have been presented to the Active Inference Institute.
[[start:545740][end:551640]] In support of this textbook are four separate tools that I will discuss over the next few slides.
[[start:553260][end:560620]] But before I do that, I would like to first highlight some special aspects and features of my approach to this textbook.

09:24 [[start:564400][end:571948]] The major focus is on writing this book for a machine learning audience or students learning in this and adjacent areas.

09:32 [[start:572124][end:574736]] Neuroscience is out of scope for this book.
[[start:574918][end:586500]] Many of the recommended and even optional prerequisites that are shown here are typically known by undergraduate students in science and engineering and certainly by graduate students in these fields.
[[start:586840][end:605800]] Nonetheless, the book is written to be readable by those that desire to focus on everything that is, the math, the code, the concepts, those that just want to focus on the math but are not interested in implementation, and even those that may skim over the math and just try to understand the ideas intuitively.

10:09 [[start:609520][end:620816]] One thing that's very important to me in trying to express these ideas clearly is by spending a lot of time working on typesetting and style, which is very important to successful learning.
[[start:620918][end:625460]] So I would spend a lot of time attempting to make my work clear and readable.
[[start:626520][end:643000]] To this end, I have margins which collect specific key terms for references later, which you can see in some of these figures that are shown here, and these terms will eventually correspond to the ontology project ongoing at the Active inference institute.

10:44 [[start:644220][end:652460]] Margins also provide further explanation to accompany the text, and this will be useful to readers who want more detail and explanation.
[[start:654080][end:658324]] There's a large focus on building an intuitive understanding of the concepts.

10:58 [[start:658472][end:662732]] For example, importantly, all algorithms are explained from scratch.
[[start:662876][end:668336]] In this book, we typically start with a description of the agent environment modeling problem.
[[start:668518][end:676096]] We then start the book with a univariate case, extended the multivariate case, then we introduce variational inference.
[[start:676208][end:685960]] We add dynamics, generalized coordinates where applicable, hierarchical models, action and also learning and other modifications we might add to our models.
[[start:687820][end:701324]] We have a very big focus on figures clearly walking the reader through the text and giving detailed visualizations of important concepts and in terms of how the textbook is set up.

11:41 [[start:701362][end:711650]] The early part of the book focuses on basic concepts such as hidden state estimation, that is, estimating the conditional distribution of a latent variable given some observed data.

11:52 [[start:712660][end:733700]] The aim here is to explain the modeling paradigm in the context of an agent attempting to infer the states of the environment, that is, the interaction between a generative model and a generative process, a perspective that differs from the Bayesian inference style that is normally taught in universities and many introductory textbooks.
[[start:735340][end:752510]] Typically, introductory textbooks on Bayesian inference focus on parameter estimation or learning, and part one introduces the expectation maximization algorithm as a way to explain the connection and separation between hidden state inference on the one hand and parameter learning on the other.
[[start:754400][end:769010]] Additionally, a large focus has been placed on variational inference, which is explained in detail, and the book features a catalog of all the different forms of variational free energy and expected free energy in the literature and how they can all be derived from one another.

12:51 [[start:771720][end:787320]] The book also covers Rau and Ballard style predictive coding terms and ideas such as key ideas such as prediction error minimization as well as clear and intuitive explanations of fundamental concepts such as surprisal.

13:08 [[start:788220][end:802136]] The textbook focuses heavily on building intuition through derivation and the general flow of most of the chapters is to set up the problem that needs to be solved which is defining an interaction between the agent and the environment.
[[start:802328][end:819200]] Showing the elements needed to solve it, which is usually random variables and parameters that form a joint distribution or generative model replacing probability distributions with their algebraic formulations and then moving through the algebra to a final analytic or gradient based equation.
[[start:819940][end:823216]] The readers should be able to recognize most equations in the literature.
[[start:823328][end:835130]] Upon reading this book, I'm also making extensive usage of Bayesian networks and other types and styles of graphical models such as factor graphs will appear in part four.

13:56 [[start:836380][end:856620]] There are hundreds of custom figures that have been created so far, and the figures are detailed to give the readers a deep understanding of the different types of content that is covered throughout the books, and also summarizes much of the information and equations that are pervasive throughout the active inference literature.

14:18 [[start:858560][end:866800]] Another important focus of the textbook is that many of the models that are presented are also shown in pseudocode, which should aid the reader in implementation.
[[start:867780][end:872716]] And finally, each chapter is filled with numerous what I call experiments.
[[start:872828][end:879600]] And these experiments correspond to the Jupyter notebook and try to show the application of a concept in a simulated environment.
[[start:879760][end:882596]] So a lot of these experiments start out by generating data.

14:42 [[start:882698][end:893624]] So we have some kind of generative process and then we have that data passed to a generative model or the agent which then attempts to either perceive and learn from that data and even act on it.
[[start:893822][end:907276]] And the example that's shown on the right margin here, this is just a perception problem on a continuous grid which has been divided into pieces for the purpose of the simulation, but represents a continuous state space.
[[start:907458][end:915308]] And the agent in the bottom left corner, shown as a mouse, has a prior belief about where some reward food is and its environment.
[[start:915404][end:928068]] But it then needs to perceive from sensory data that it observes the true location of that reward or food which is obscured or occluded in some way by the mist that's shown in that figure.

15:28 [[start:928234][end:940250]] So these types of experiments give the reader a better sense of how to apply these statistical ideas to a real world situation so we can understand how it might apply to some kind of autonomous agent.

15:42 [[start:942860][end:959440]] Next, I'd like to cover and shift my attention toward Jupyter notebooks and videos and like to note that upon publication of the textbook these Jupyter notebooks will be released on GitHub and should be fully reproducible using Docker and other version handling tools.
[[start:960740][end:971364]] One of the big emphasis on the Jupyter notebooks is it has to be a direct correspondence between the equations and explanations in the code and in the text.
[[start:971562][end:976500]] This will build a direct understanding and show applications of the concepts explained.
[[start:978360][end:984890]] Notebooks are filled with simulations and visualizations many that appear in the main text.

16:27 [[start:987020][end:995588]] And in addition to that, I have also over the last seven months been presenting chapter presentations to the Active Inference Institute.

16:35 [[start:995764][end:1010210]] So far, a draft version of the first ten chapters of the book have been recorded at the Active Inference Institute and these are just some sample slides that I've prepared that try to explain these concepts in great detail.
[[start:1011060][end:1016976]] In the final stages of writing this textbook, video lectures will be re recorded and released alongside the book.
[[start:1017158][end:1024100]] I also plan to create detailed code walkthrough videos that walk through the different examples in the Jupyter notebooks.

17:06 [[start:1026280][end:1038360]] Now I'd like to talk about a few planned future resources I'd like to work on after the book is complete, or toward the final stages of the book to have further support and educational tools.
[[start:1039980][end:1060568]] Some of these planned future resources include a software suite in Python to enable an alternative learning approach for those who do not wish to learn about the algorithms from scratch, and this will expand the possible landscape of engagement as Pymdp already exists.

17:40 [[start:1060664][end:1078180]] I will not be working on a discrete statespace Python package, but I'd like to fill the space for things like active generalized filtering, and also just an availability of different types of simulations of Bayesian mechanics as it's currently defined today, or at least the different versions and varieties of some of those key concepts.
[[start:1079400][end:1092516]] I'm also very much interested in interactive learning, and my aim would be to have these preset simulations concepts that are explained in text, with various simulations interspersed in the form of plots and demos and other visualizations.
[[start:1092708][end:1106750]] And the idea would be that the user could manipulate sliders and knobs to tweak various parameters that would help aid in learning as they get a feel for how these systems behave, especially ones most of these systems we talk about are dynamics, so seeing how they change over time.

18:30 [[start:1110420][end:1120748]] The Active Inference Institute has made tremendous progress in the past couple of years to provide a collaborative environment for researchers and for students of active inference.

18:40 [[start:1120924][end:1134010]] I hope to be part of this ecosystem as I continue to support the spirit of accessibility and collaboration, and I'm excited to continue to contribute to this ecosystem of shared intelligence and look forward to what we can build together.

18:58 [[start:1138380][end:1152250]] I would like to thank the Active Inference Institute for hosting my presentations, code reviews, and feedback sessions and inviting me to present at the symposium, and also thank my employer, Kung Fu AI, for letting me take time off to write for the past seven months.
[[start:1153100][end:1155352]] Please feel free to contact me at any time.
[[start:1155486][end:1161436]] Email is the easiest way, but I'm also available on the active inference institute discord.
[[start:1161628][end:1168288]] If you would like access to the textbook and related materials, please send an email requesting access and I can get you set up.
[[start:1168454][end:1169904]] And that's all I have for today.

19:29 [[start:1169942][end:1171010]] Thank you very much.

19:35 _Daniel:_
[[start:1175080][end:1175828]] Awesome.
[[start:1175994][end:1176532]] All right.
[[start:1176586][end:1177440]] Thank you, Sanjeev.
