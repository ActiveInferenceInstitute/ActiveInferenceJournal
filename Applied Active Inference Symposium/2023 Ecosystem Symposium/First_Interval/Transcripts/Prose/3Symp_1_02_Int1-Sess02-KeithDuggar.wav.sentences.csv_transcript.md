
00:01 _Daniel:_
[[start:1290][end:7630]] All right, next up is going to be Keith Duggar, who has submitted a pre recorded video.
[[start:7780][end:10922]] The pre recorded video is called active inference.
[[start:10986][end:15920]] And the actor model So I will bring that up right now.

00:29 [[start:29430][end:37660]] Okay, here comes Keith's pre recorded video on active inference and the Actor model.

00:44 _Keith:_
[[start:44240][end:46956]] Active inference and the actor model.
[[start:47138][end:47580]] Hello.
[[start:47650][end:48076]] Hello.
[[start:48178][end:48732]] I'm Dr. Keith
[[start:48786][end:54012]] Duggar, platform CTO at X Ray, an extended reality AI

00:54 [[start:54076][end:58880]] Company, and co host of Machine Learning Street Talk podcast.
[[start:59780][end:72320]] Now, as we all work to build an ecosystem based on active inference, software will obviously play a foundational role to make the most of active inference.
[[start:72400][end:81928]] We'll need to use software engineering paradigms that align with the principles of active inference, and I think there is one tailor made for our needs.
[[start:82094][end:83770]] It's called the actor model.
[[start:85100][end:90750]] Active Inference and the Actor Model are two deeply connected understandings of the world.

01:31 [[start:91280][end:104160]] They provide foundational frameworks for dealing with the dynamics of complex systems, with a focus on autonomous agents that interact in an ecology of nested systems.

01:45 [[start:105220][end:117300]] I'd like to explore some of their key connections, including the role of agents concurrency, autonomy, uncertainty, and behavior adaptation.
[[start:118680][end:138680]] We will see that active inference and the Active model are both paradigm shifts away from a deterministic, centralized, step by step thinking to a decentralized network concurrent perspective of both computation and cognition.
[[start:139920][end:142430]] Just a little bit of history about the Actor model.
[[start:142960][end:166020]] Back in 1973, Karl Hewitt, Peter Bishop, and Richard Steiger were all working at the Massachusetts Institute of Technology AI lab to Fundamentalize, a concept of concurrent computation that included both structure as well as adaptable algorithm execution.

02:47 [[start:167480][end:173140]] Conventional methods at the time lacked robustness and secure mathematical foundations.
[[start:173960][end:178490]] Their collaborative effort ultimately led to the creation of the Actor model.
[[start:179180][end:189660]] At the time, it was viewed as revolutionary due to its characteristics of both increased error tolerance and distributed computation abilities.
[[start:190320][end:206480]] Throughout the 1980s and the 1990s, the Actor model became a basis for numerous research projects as well as practical projects, gaining popularity for its flexibility and intuitive approach to concurrent computation.
[[start:208020][end:213084]] It was primarily used in artificial intelligence and multi agent systems.

03:33 [[start:213212][end:214400]] Sound familiar?
[[start:215880][end:232810]] New Actor based languages like Actor, Saulson and Erlang contributed to the refinement of the model, shaping it into a more robust and flexible approach to concurrent computing, and it remains alive and well in computer science today.

03:53 [[start:233580][end:247310]] More recently, the Actor model has gained renewed interest, mainly due to the growing need for distributed systems, cloud computing and edge computing, fueling the Internet of Things and Web 30.
[[start:248480][end:268710]] These computer tasks are ideally suited to take advantage of the ACA model's architecture, which is designed exactly for modeling concurrent handling of both large volumes of data on the one hand, and fine grained disparate autonomous systems on the other hand.
[[start:269640][end:287108]] This application of the Actor model has had profound effects on major companies that have utilized its principles to handle big data problems such as Twitter, Facebook, LinkedIn, so what does this have to do with active inference?

04:47 [[start:287284][end:290908]] I'm guessing you've already heard some of the parallels in the intro.
[[start:291074][end:299420]] But let's start by looking at a few core principles of the actor model and how they relate to the principles of active inference.

05:00 [[start:300000][end:302480]] Let's start with the concept of isolation.
[[start:303540][end:311280]] Isolation means that an actor in the actor model does not share its state with any other actor.
[[start:312100][end:315670]] It can only be affected by receiving a message.

05:16 [[start:316040][end:324100]] And it can only affect change in the state of other actors by sending a finite number of messages in response.
[[start:324840][end:344910]] From a software engineering point of view, this isolation principle limits potential side effects of an operation to a single actor, thus improving the system's overall predictability reliability, and most importantly, if embraced fully, can actually simplify the design.
[[start:346560][end:357040]] Looking at the diagram, we see an ecosystem of actors sending messages to a particular actor, which in turn sends back messages to other actors.
[[start:358340][end:359916]] Where is active inference?

06:00 [[start:360028][end:374630]] Well, let's recast receiving and sending messages to a perception action cycle and denote external, internal, sensory and active states.

06:15 [[start:375480][end:382600]] And we now clearly have the necessary foundation of active inference a Markov blanket.
[[start:383660][end:389660]] The actors of the actor model map directly to the agents of active inference.
[[start:390480][end:401150]] In addition, the finiteness, the fact that an actor can only send a finite number of messages in response is also an important shared property.
[[start:401940][end:409852]] Because active inference models reality, it necessarily respects the resource constraints of real systems.
[[start:409996][end:414390]] And this is nicely bathed into the foundation of the active model.

06:55 [[start:415320][end:419860]] Let's look at another core principle asynchronous message passing.

07:00 [[start:420840][end:424100]] Communication between actors is asynchronous.
[[start:424440][end:429064]] This means an actor doesn't wait for a response after sending a message.
[[start:429262][end:433210]] It continues working, it continues living, as it were.
[[start:433820][end:449660]] This is critical as it decouples the actors, leading to a system that can continue functioning, living and making progress even when parts of the system are slow or even temporarily unavailable.

07:30 [[start:450800][end:461490]] Professor Friston has said that the free energy principle is the ultimate existential question if things exist, what must they do?
[[start:462660][end:467350]] Well, the actor model claims they must not wait on others.
[[start:468360][end:477528]] Of course, an actor can choose to wait on others, but it must not be forced to do so in the model.
[[start:477614][end:479770]] It must be free to choose.

08:01 [[start:481820][end:487640]] This leads us to another critical principle that both models share autonomy.
[[start:488860][end:496620]] The free energy principle is a model of physical reality and our reality is, after all, concurrent.
[[start:497360][end:505196]] All throughout infinite space, systems are evolving simultaneously according to their local dynamics.
[[start:505388][end:510560]] And therefore this is reflected at the heart of the free energy principle.
[[start:510980][end:516560]] Of course, a model of computation need not constrain itself to physics.

08:36 [[start:516720][end:518068]] But Hewitt et al.
[[start:518154][end:524560]] Were seeking to develop a model that did model the reality of distributed concurrent systems.
[[start:524720][end:538040]] And luckily for us, the actor model embraces both concurrency, seen from the principle of isolation and actor autonomy, making it compatible with active inference.
[[start:539200][end:541820]] Next we come to nesting.

09:02 [[start:542640][end:558240]] The actor model allows for an actor to not only receive and send a finite number of messages to perceive and act, it also allows as an action the creation of a finite number of new actors.

09:19 [[start:559220][end:568864]] These actors can either be nested within the parent, say, the parts of an animal cell, or it can be released into the environment as independent actors.
[[start:568912][end:577960]] From then on this principle, the model fits nicely with the beautiful concepts of multiscale nesting and active inference.
[[start:578940][end:587290]] This allows for actors to contain ecosystems of actors both all the way down and all the way up.
[[start:589200][end:597020]] Last, I want to cover two more actor model design principles behavior change and persistence.

09:59 [[start:599040][end:604450]] Actors have the ability to change their behavior in response to a message.

10:05 [[start:605140][end:614130]] This adaptability allows for the construction of complex stateful entities that can evolve over time.
[[start:614760][end:622660]] And indeed, it allows for entire ecosystems to evolve new emergent behaviors.
[[start:624040][end:631800]] When used for software engineering, this adds a powerful tool for managing complex dynamic systems.
[[start:632700][end:636920]] Active inference, of course, embraces this to the extreme.

10:38 [[start:638220][end:654240]] The very essence of thingness is the ongoing attempt to predict and adapt to an environment and thereby continue to exist to maintain one's Markov blanket in a broiling sea of activity.
[[start:656180][end:659920]] Along with this also comes the concept of persistence.
[[start:660660][end:671300]] Persistence allows actors to sade their state and to restore or modify it later a feature that embodies the principle of memory.

11:11 [[start:671800][end:676180]] Memory is a prerequisite for learning and adaptation.
[[start:676700][end:688360]] An agent's ability to predict depends on its ability to remember past experiences and thus minimize the surprise associated with unexpectedness.

11:28 [[start:688880][end:701470]] The vital role of memory is also emphasized when we assume that agents have inductive priors, either from experience or inheritance, contributing to their world model.
[[start:702340][end:714240]] This world model both guides their current behavior and it is continuously updated based on new experiences contributing to their ongoing adaptation and existence.

11:56 [[start:716600][end:717492]] Okay, great.
[[start:717546][end:723940]] You say there are clear and deep connections between the actor model and active inference.
[[start:724280][end:729370]] But how does this help us in the active inference community?
[[start:730620][end:736520]] Well, firstly, in my opinion, it is a software engineering paradigm we should embrace.

12:16 [[start:736860][end:759120]] And if we do, there are of course, actor model libraries and frameworks that we can use such as ACA, Orleans, thespian Actix Protoactor and many more, which we can immediately use when building active inference software modules and applications.

12:39 [[start:759860][end:775444]] There are also libraries, languages and even language features that align very well with the actor model principles such as Zero, MQ, tokyo and Rust, Erlang, Async, Await and C.
[[start:775482][end:777480]] Sharp, et cetera.
[[start:778380][end:792940]] But more important than the tools available to us today is the software design mindset that will guide our creation of the active inference software of tomorrow.
[[start:793680][end:805280]] The actor model provides a paradigm of software design and engineering that is the most perfect match that we have for active inference.

13:26 [[start:806900][end:819990]] This is evident not only from the alignment of the core principles we previously discussed, but also from the insights that active inference in the actor model bring to each other.

13:41 [[start:821000][end:824870]] For example, consider what is now called Hewitt's Law.
[[start:825880][end:849310]] Informally stated as everything is everywhere, this law signifies the idea that in a truly asynchronous distributed system, it can take an arbitrary amount of time for a message to go from one place to another, and any actor must be prepared for that event.
[[start:850000][end:862000]] There is simply no such thing as instantaneous in such a system, and no component can make an assumption about the timing of another component's actions.
[[start:862580][end:868260]] In fact, one must act as if a message may never arrive.

14:29 [[start:869560][end:871860]] This has important implications.

14:32 [[start:872760][end:888410]] It suggests that it is impossible to accurately and consistently determine the state of the entire system at any given time, because the information just may not have even propagated across the system.
[[start:889760][end:898780]] And also attempts to implement global synchronization will inevitably introduce bottlenecks and reduce efficiency.
[[start:899920][end:919460]] Hewitt's Law emphasizes the need for systems to be designed in a way that they can effectively handle these unavoidable delays and uncertainties, highlighting the importance of robust nonblocking communication mechanisms and local decision making abilities.
[[start:920200][end:926020]] In short, Hector model systems are by nature nondeterministic.
[[start:927180][end:928760]] Does this sound familiar?

15:29 [[start:929340][end:937720]] What other paradigm highlights operation under uncertainty and the autonomy to continue despite the environment?

15:38 [[start:938940][end:941720]] Active Inference and the free energy principle?
[[start:942640][end:949660]] Active inference reflects the reality of an unpredictable world in which our software systems operate.
[[start:950080][end:959250]] Different outcomes may result from the same initial conditions due to the occurrence of events in a random, unpredictable order.
[[start:960260][end:973060]] This is the concept of surprise that we all know well, where an agent updates its beliefs about the world when the sensory input it receives does not match its predictions.

16:13 [[start:973720][end:979560]] Both the actor model and active inference acknowledge that the world is unpredictable.
[[start:980780][end:989530]] Even more than acknowledge it, the models accept this uncertainty as a given and not something to be managed away.
[[start:990780][end:1001020]] Indeed, as we know in the free energy principle, the uncertainty that we maintain in our models is what gives us the flexibility to adapt.

16:43 [[start:1003540][end:1024100]] Perhaps this is just my personal flight of fancy, but I imagine a future where software modules guided by active inference do away with hard coded error handling and swap in probabilistic learning algorithms that optimize themselves as the error landscape evolves.
[[start:1025320][end:1041660]] Modules that are robust and self healing distributed systems with no single points of failure that focus on predictive disaster avoidance rather than reactive disaster recovery.
[[start:1043040][end:1055570]] Looking towards the future, we as a community have the potential to push the boundary of both active imprints theory and practical implementations of the actor model.
[[start:1056020][end:1069620]] By leveraging the strengths of these two paradigms together, we can create software systems that are robust, adaptive and more aligned to the physical world in which they actually operate.

17:51 [[start:1071080][end:1085370]] Imagine a future where software components using active inference in the actor model can anticipate potential issues, learn from past mistakes, and adapt in real time to environmental changes.

18:06 [[start:1086620][end:1092780]] With this approach, we can build systems that are fundamentally more resilient and more efficient.
[[start:1093360][end:1113010]] In my opinion, this can bring a step change in software reliability and performance and scalability, and heralds a new era of computing, weaving principles of biology and cognition into the fabric of our software systems, bringing them closer to life in the process.

18:35 [[start:1115080][end:1126820]] In conclusion, the coupling of active inference to the actor model provides a powerful new lens through which we can look at software design and engineering.
[[start:1127180][end:1139400]] Whether we leverage existing languages and libraries aligned with active inference or invent new ones, we are standing on the brink of an exciting frontier.

19:00 [[start:1140480][end:1151980]] So let's seize the day, have a look at the actor model and its relationship to active inference, and let's shape the future of intelligent distributed computing.
[[start:1153040][end:1154460]] Thank you for listening.

19:17 _Daniel:_
[[start:1157790][end:1158540]] Awesome.
[[start:1159950][end:1161734]] Great talk by Keith.
[[start:1161862][end:1163978]] Thank you, Keith, for sending that in.
[[start:1164144][end:1166690]] There were some comments in the chat.
[[start:1167030][end:1173950]] So, Keith, potentially if you want to join for A-Q-A some future time, but really cool presentation.
