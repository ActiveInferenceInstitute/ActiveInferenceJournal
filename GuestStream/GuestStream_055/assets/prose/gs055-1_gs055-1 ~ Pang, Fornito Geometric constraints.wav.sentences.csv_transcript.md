00:02 _Daniel Friedman:_
Hello and welcome everyone.
This is Active Inference guest stream number 55.1.
It's August 30, 2023.
Today we are going to have a presentation followed by a discussion on geometric constraints on human brain function by James Pang and Alex Fornito.
Thank you again for joining.
Really looking forward to the presentation and the discussion.
So please off to you two to introduce yourself and continue however you like.
Thank you.

00:33 _Alex Fornito:_
Well, thanks very much, Daniel.
My name is Alex Fornito.
I'm based in the School of Psychological Sciences and Turn Institute for Brain and Mental Health at Monash University, and James Penn, who is a research fellow working in the team.
And so the idea today was that we were going to talk a little bit about this work.
I'll begin by providing a bit of a historical and theoretical background and then James will take over and jump into the specifics of what we did and what we found.
We're assuming some basic understanding of neuroscience and some elements of human brain imaging and we'll go through a little bit of maths, but hopefully it'll be enough to give a picture and if there's any questions about it afterwards, we'll be happy to try and answer them.
So a key motivating factor for this work is really trying to understand how the structure or anatomy of the brain constrains its function.
And if you look at a diverse range of systems found throughout nature, we know that the structure of the system can change its dynamics.
So, for example, the shape of a racing car will influence its aerodynamics and how fast it can go.
The folding patterns of a protein will influence the other proteins that it can interact with and have quite large effects.
So here, for example, we've got example of the hemoglobin protein in a healthy person and someone with sickle cell anemia.
And this change in the geometry of the protein leads to a 20 year difference in life expectancy.
And here we've got the molecular structures of diamond and graphite.
So both of these materials are made of the same atoms.
They're all purely carbon atoms.
It's just the bonds between them that are different.
And that difference is sufficient to create quite a variation in the properties of the material.
So diamond being one of the hardest substances on Earth and valued at somewhere between twelve to 90 million dollars per kilo, whereas graphite is one of the most brittle and only costs you about $20 per kilo.
And so this is essentially the reason why we don't propose to people with H two B pencil, we use diamond rings instead.
Now, the brain is no different.
We think anatomy constraints function, but there has been a long standing debate about the specific properties that are the most relevant and how we should best conceptualize them.
And this can be traced back to the days of Ramani Kahal and Camilla Golgi, two people considered to be some of the founding fathers of modern neuroscience, golgi developed a technique for staining neurons that allowed you to visualize their structure under the microscope.
And Cahal really perfected that technique and studied the nervous system in extensive detail and really laid down the foundations for what we think about the anatomy of the brain to this day.
Now, both of these men were recognized for their efforts in 1906 with a Nobel prize.
But even at the award ceremony, when giving their lectures, they were in bitter disagreement.
So if you actually look at the recordings of their lectures, cahal says, we applied Golgi's method, and our observations revealed, in my opinion, the terminal arrangement of the nerve fibers.
Nerve elements possess reciprocal relationships in continuity, but not in continuity.
So here he's saying that cells are fundamentally discrete elements separated in physical space and that there's a gap between them at the synapse.
The synaptic cleft and signaling occurs through this gap.
Olga, on the other hand, didn't agree.
He said, while I admire the brilliancy of the doctrine, which is a worthy product of the high intellect of my illustrious Spanish colleague, I cannot agree with him on some points of an anatomical nature, which are for the theory of fundamental importance.
I found myself unable to follow the current of opinion because I was confronted by one concrete anatomical fact.
This was the existence of the formation, which I have called the diffuse nerve network.
And so, for Golgi, all the cells were continuous.
They form one continuous network.
There was no point of separation between them, and signaling occurred through this continuous network.
Now, ultimately, a growing body of evidence, and you can see it in Golgi's statements, was starting to favor Cahal's model.
But really, it was only resolved in the 1940s with the advent of electron microscopy, where people could actually resolve synapses and saw that they were spatially disjoint.
And this ultimately established the neuron doctrine as the fundamental theory about how the nerve, the system is organized at a cellular level.
And this basic idea that we can divide the brain up into discrete units was then carried through to different scales, most famously by Corbinian Broadman, who developed a parcellation of the cortex based on cyto architectonic grounds.
His idea was that different parts of the cortex have different cellular properties, and so they define these discrete areas that are functionally specialized in some way.
And certainly this has been a very influential idea in neuroscience ever since.
But around the same time, in fact, a couple of years earlier, the neurologist Alfred Campbell published his own cytoacyctonic map, and he agreed that you could identify discrete boundaries largely in primary zones, but then in the cortex in between, it was a lot more difficult to find sharp outlines or boundaries.
And he suggested that actually the changes were more gradual or continuous in nature.
Broadman's view became more popular and certainly became sort of the dominant theory in neuroscience, even though subsequent attempts to try to replicate it were different.
And so different anatomists would parcelate the brain in different ways, using different boundaries and so on.
But nonetheless, this kind of congruence between the discrete model of cahal and discrete model of Broadman eventually led to the idea that essentially we can think about the brain as a multiscale network where at the cellular level we can identify discrete cells that are connected by synapses.
Then we can scale up at the population level at a mesoscale resolution and identify how population of cells are linked by bundles of axons and then all the way through to the macro scales, which is what you sort of see when you look at one of Broadman's maps.
You have these broad, roughly so architectonic areas connected by white matter bundles.
And in the last two or so decades we've had the measurement techniques for characterizing these networks on a vast scale and there's been a pretty well established pipeline for mapping these networks.
So the basic idea is that we have the brain, we divide it up into these discrete areas and they act as our network nodes.
And then for every pair of nodes we measure some aspect of structural or functional connectivity between them.
Functional connectivity being some aspect of coupling in activity.
And then we can represent that in the form of a connectivity matrix.
So each row and column represents a different region and each element tells you about the type and strength of connectivity between areas that can equivalently be represented as a graph.
And then with that graph representation, we can apply all sorts of different analytic tools to understand different aspects about how the network is connected and organized.
And this basic approach has been used quite extensively to understand how the underlying anatomical properties of the network constrain function.
This is one of my favorite examples.
This was a study of two different worms, c Elegance and P Pacificus.
Both of their nervous systems in the head have been mapped at the level of each cell and synapse and they're actually identical.
So they've got the same type of cells, the same number of cells, it's just the connectivity between them that's different.
And that's what you see in this network projection here that the topology of the network is different.
And in this study they showed that changes in the connectivity of just two hub neurons were sufficient to elicit a difference in the behavior of the animals, such that P Pacificus is a predator of sea elegance.
And here you can see Pacificus eating poor sea elegance for lunch.
Now, we can't lock humans up in a room and see who eats who and try to understand how their anatomy constraints function in that way.
But we can do things like use MRI to measure anatomical connectivity and functional connectivity and correlate the two.
And it's pretty consistent finding that we generally find there is a correlation between them.
We can run computational models where we have a structural network, we simulate the activity.
Then we apply, say, a lesion to that network and look at the effects on the activity.
And we can show, for example, that if you lesion a hub area you have quite a dramatic impact on brain function compared to if you lesion a more weakly connected non hub area.
Or we could use clinical studies.
We could look at cases where there are naturally arising lesions through stroke or some other form of brain damage and we can understand the functional impairments that result.
So, for example, in this case, people with lesions to certain types of hub areas with diffuse connectivity showed much more generalized cognitive impairments than people with lesions to areas with more specific patterns of connectivity.
So this is great.
This has been really informative and great for understanding the role of individual brain regions or connections in brain function.
But it doesn't really give us a coherent, unified perspective about how dynamics emerge from the underlying structure.
It's all a little bit piecemeal.
Now, if we want to develop such a coherent understanding we can draw some inspiration from different physics and engineering where typically the structural constraints on the dynamics of a system are studied by understanding the eigenmodes of the system.
Now, the eigen modes of a system are found by solving an eigenvalue problem such as this one.
So an eigenvector we can think of as something that we measure about a system that doesn't change its direction if it's subjected to some kind of transformation.
So if that's the case, then this equality holds.
So the idea here is that PSI is our vector, something we measure about the system subjected to some transformation L.
And if PSI is an eigenvector, then the transformed eigenvector is equal to the eigenvector just scaled by some value.
So the transformation can scale the vector, but it doesn't change its direction.
And so if that's the case, then this scaling factor, lambda, is what we call an eigenvalue and PSI is an eigenvector.
This kind of equation is applied to a lot of different systems and a lot of different contexts.
But when we're studying the eigen modes of a system, typically our L term here is an operator called the Laplacian operator which essentially describes how smoothly some kind of structural property of the system varies through an appropriate spatial embedding.
So I'll come back a little bit to what that means because we can make different choices for what we use in L and that determines the specific anatomical properties that we prioritize.
But for now, I just want to emphasize that a key property of these eigenvectors is that they're orthogonal and so that then we can use them as a basis set for reconstructing different activity patterns that we might see in the network.
So I guess the most famous example of a basis set that many people will be familiar with is a Fourier set.
So, for example, here we have some one dimensional signal, and we can decompose that signal as a weighted sum of sine and cosine functions of varying frequencies.
So here you've got the different functions, different frequencies, and here you've got some weighting factors.
And we can reconstruct this signal as a weighted sum of these functions.
In a similar way, we can extract our Eigen modes of the brain based on some particular anatomical property.
And we end up with these spatial patterns here that are organized again in terms of spatial frequency or the wavelength of fluctuation.
So here you can see we've got a very low frequency fluctuation moving from back to front, top to bottom, medial, lateral, and then as you move up, you get these more high frequency fluctuations.
And so then we can use these patterns to reconstruct any spatial map that we observe on the brain.
So it could be a map of brain activity recorded during a particular task.
It could be, say, a map of cortical thickness variations or gray matter volume variations.
It's sufficiently general to allow you to reconstruct any type of map.
And so we can do that just as a weighted sum.
So here Y represents our map, and then we represent that as a weighted sum of our modes with the A coefficients representing the weights.
Sorry, I should emphasize that that explanation can be a little bit abstract for people who aren't familiar with Eigen modes.
And it is always a bit of a challenge to get an intuition.
And so you can do what one of the people in the team did and asked Chat GPT to explain eigenmodes to a ten year old.
And it turns out that it does a pretty good job.
I was quite happy with this explanation, so I thought I'd share it.
So our Chat GPT says, of course, let's imagine we have a wobbly jiggly bowl of jelly.
When you poke it, it wiggles and shakes, right?
Now, imagine if you poke the jelly in different spots or with different amounts of force, each time you poke it differently, the jelly wiggles and shakes in a different way.
Eigenmos are like those different ways.
The jelly wiggles and shakes when you poke it.
So essentially, seeing this video here, the jelly is poked and it wobbles in a particular way.
If you poke the jelly in a different spot or with a different amount of force, you'll trigger a different pattern of vibration.
And so commonly, Eigen modes are used in the context of systems that vibrate.
And the idea is these Eigen modes correspond to preferred patterns of vibration when the system is perturbed, and those preferred patterns are just dictated by the structural properties of that system.
We can extend it more generally and think about it more as how a system responds to any type of excitation and how an excitation spreads through some connected system.
And the Eigen modes correspond to the preferred patterns of excitation.
Again determined by the physical properties of the system.
So naturally, given everything we've been talking about and these ideas that the brain is a multiscale network, we need to make a choice about how we define alloplastian what specific anatomical properties are we going to extract our eigen modes from?
And so a natural choice would be to extract them from brain connectivity.
And we can do this quite in a reasonably straightforward way.
We get some map of the connections in the brain.
We map connectivity between every pair of nodes.
After we apply some discretization, we define our discrete nodes.
We map every pair of connections.
We represent that in the form of a matrix.
And then we extract this quantity here.
It's called a graph Laplacian.
The details are not so important, but that's essentially our l operator here.
And it describes how smoothly connectivity varies as we move from node to node in the network.
And when we do that, several studies have shown that you can use the eigen modes extracted from this graphaloplassian to reconstruct kind of classic functional networks that you record.
With functional MRI, we can reconstruct different patterns of functional connectivity between pairs of areas.
You can use it to reconstruct different eg signals.
And people have even shown that you can make predictions about the pattern of neurodegeneration that you see in different forms of dementia.
So this has been really fantastic important work and a really important proof of principle that this eigenmode framework can be used to understand how the structure of the system constrains its dynamics.
And in each case, the interpretation is that these dynamical patterns that we see with fMRI or EEG or so on, are reflecting excitations of these underlying eigen modes or the resonant modes of the anatomy of the brain.
This view very much aligns with what we would think of as a classical view of brain organization that I've just been discussing.
So, following from Cahal and Broadman's work, the idea is that at lots of different scales, we can divide the brain up into discrete areas.
They're connected in some way and it's the signaling along these connections between these discrete areas that drives activity.
But there are reasons to think that, particularly at coarser scales, so we know at the fundamental cellular scale, the network is discrete, but at coarser scales, perhaps a different set of approximations might be useful.
So if you look at dense reconstructions of neuronal tissue, so this is, say, with electron microscopy, you find that cortical tissue is extremely dense.
It's like a really rich, thick forest of cells and their processes.
And as we've talked about, there's been a lot of debate about where you can actually draw boundaries between discrete areas and how valid and reliable that is outside some kind of classic examples seen in primary cortex.
And if you look more deeply at the cellular organization of specific regions, here on the left we've got the cellular organization and on the right we've got a myelin stain.
You see, you get these deep penetrating fibers that are coming in from the white matter.
This is what this kind of classic graph approach will pick up because we define our nodes in the cortex and then we're mapping the connections that pass through the white matter.
But you can also see that there's a lot of connectivity that's moving horizontally or tangential to the geometry of the cortex.
And so these horizontal connections allow for the continuous spread of activity.
So rather than activity jumping between discrete nodes, it can actually spread as a propagating wave.
And just to emphasize some of the limitations of the discrete model, not long after Broadman's work, just a couple of decades, the renowned physiologist Lorenzo de Nou was pretty emphatic about his concerns with the approach.
He said the only really good cyto architectonic pictures are those of Campbell, who, let me put in capital letters, has been the only cyto architectonist who has described facts and only facts.
The German cyto architectonist has mixed facts and theory in such a manner that nobody can tell where facts ends and theories begin.
So again, this is just emphasizing the idea that while we might be able to define discrete areas at a mesoscopic or macroscopic resolutions, in some cases, especially around the borders of primary sensory or motor areas, for large swathes of cortex, those distinctions become a little bit blurry.
So an alternative approach has emerged out of neural field theory.
So neural field theory has been around for several decades now and this is a different approach to thinking about cortical activity.
So the basic idea is that instead of dividing the brain into discrete specialized areas or nodes, we can treat the cortex as a continuous sheep.
And we are actually interested in trying to capture how patterns of brain activity propagate through that continuous sheet.
And so this is something that you can see in diverse types of electrophysiological recordings.
So this, for example, this video is of the dynamics of voltage sensitive dyes recorded in the mouse brain.
And you can see that you observe these propagating waves of excitation that move continuously through the cortex rather than jumping from region to region as would be implied by a kind of strongly discrete model.
So a big emphasis in neural field theory is on describing these wavelike propagation patterns.
And it's been shown in recent theoretical work that if we accept that wavelike propagation drives neuronal activity, then really the eigen modes that we should be extracting or prioritizing are those that are derived from the geometry of the brain.
So our eigenvalue becomes this problem here where this operator here is called the LaPlace beltrami operator and it describes how smoothly the geometry or the shape or the curvature of the brain varies through space.
And just to briefly explain why that's the case, here we've got the wave equation that's used in some forms of neural field theory, at least the divisions that we've been focusing on.
And so the basic idea is that the firing rate of a given population of neurons B at location R and T is given by the Afferent field of incoming populations.
So other populations A.
So we've got other populations providing this Afferent field of activity that determines the firing rate of B.
And obviously, we then need to describe what this afferent field looks like and that's given by this part of the equation here.
So on the left here, this set of terms describes how the field evolves through time.
We're not going to focus on that today over here, which is what we're interested in, where we've got how the field is evolving through space.
And so here we can see our friend, the LaPlace Beltrami operator, which describes the geometry.
And here we've got the length scale of axonal connectivity.
In this model, we make a very simple assumption about connectivity.
We assume each point is connected to its neighbors in a distance dependent and isotropic way.
And that distance dependence is roughly exponential.
So the idea is that areas nearby to a given location R will have a strong influence and that influence declines roughly exponentially as a function of distance.
And the speed of that decay is given by this R term here.
You can see that geometry is firmly embedded in this equation.
Now, I should point out this isn't something that's just been plucked out of thin air.
This is a damped wave equation that has been used for centuries to describe wave dynamics in all sorts of different media.
And so from that physics, we know very well that the geometry of the system constrains the spatial properties of wave propagation.
And you can start from first principles of neuronal biophysics and derive this equation.
And given all that work, we know that the eigen modes of the LaPlace Beltrami operator actually correspond to the standing waves of the dynamics.
So what are standing waves?
So in this simple example, we've got two traveling waves here, a blue and a green.
And as they interact with each other, you get these patterns of constructive and destructive interference represented by this red line here, that cause these very large amplitude fluctuations that are fixed in space.
So they're not actually traveling like the original carrier waves, they're fixed in space.
So that's why they're called standing waves.
And they're a nice example of resonance.
So these fluctuations in the red trace are much larger in amplitude than the original carrier waves.
So it's an example of resonance where we're getting a larger response in the system than the energy that we put in.
And just to convince you that this is something real here, for example, we have a pool of water, a classic wave system.
If you apply vibrations at a specific point in the pool, you see these waves that travel out.
They hit the opposite wall, reflect back and start to interact.
And then you see the emergence of these standing wave patterns that are fixed in space but show these very large scale amplitude fluctuations.
Another classic example is the Cladney plate.
So if you arrange dust particles on a plate and then you apply some vibration at a particular frequency, the dust particles will settle into these complex patterns.
The pattern is determined by the specific frequency that you apply and specifically where you apply the vibration.
And the patterns correspond to the eigen modes of the plate.
And again, those patterns are determined by the physical properties of the plate things like its stiffness, its geometry and so on.
This is a little bit gratuitous, but you can extend the idea to three dimensions and you can actually cause the particles to levitate.
Again, in this case, they're trapped within the nodal lines of sound waves that are being projected in three dimensions.
And this does have real world consequences.
So this is a video of the Tacoma Narrows bridge in the 1940s.
The engineers didn't pay enough attention to eigen modes.
And so on this particular day, crosswinds hit the bridge in just the right spots and at just the right frequencies to excite the eigen modes of the bridge.
So you triggered these resonant responses and created these large scale amplitude fluctuations that ultimately led to the collapse of the bridge.
So hopefully, that background has kind of illustrated that there's sort of two different views of thinking about which anatomical properties of the brain might be more important in constraining dynamics.
So on the one hand, we have the classical kind of connectome centric view in which we view the cortex as comprising discrete areas and dynamics are dominated by node to node transmission.
The connectivity between areas is topologically complex and not homogeneous, and we very much think that that's very important.
And so we prioritize measuring that.
We don't really directly account for the spatial embedding of the network or its geometry.
We can look at it secondarily, but it's not baked into the model.
And because we're interested in connectivity, that means we need to measure it.
So from a practical perspective, at least, if you're dealing with neuroimaging data, you need a T one weighted image to measure brain anatomy but also diffusion MRI image to be able to measure brain connectivity.
The other perspective, which is a geometrically informed perspective that arises out of neural field theory, views the cortex as a continuous sheet.
We're not making distinctions between different areas of the cortex.
We think dynamics are dominated by propagating waves of excitation, especially at these mesoscopic and macroscopic scales.
We approximate connectivity between different points of the cortex as being homogeneous and distance dependent.
So we know that there is a strong distance dependent in connectivity.
It doesn't explain everything.
So some things are missed, but we know it's certainly an important feature.
So then the question is how far we can get with this approximation.
And a nice feature of this approach is that we are directly accounting for spatial and geometric effects, the physical properties of the brain, which are overlooked by the connectome approach.
A nice practical benefit of this approach is that because we approximate connectivity in a simple way, we don't actually have to measure it.
We can derive our basis set simply by looking at the geometry of the brain.
And so we only need a T one weighted scan, which is very standard in MRI experiments.
So hopefully that's set the scene for thinking about different anatomical constraints on the brain and which ones we might want to prioritize.
I'll now hand over to James.
He'll talk about how we went about testing these different ideas and trying to understand which constraints might be more important for dynamics.

30:26 _James Pang:_
Thank you, Alex.
I'm going to focus more on the things that we found in the paper that we recently published.
I think a lot of you have the link for it, but let us know and send us a message if you want to want us for the link.
So basically we start with we're trying to answer and test the theory on which modes of the brain could best describe activity measured in FMI.
So we'll begin by how do we actually measure these modes.
So geometric modes are based on the T one weighted image, which is a standard imaging tool that people use in the field.
And you can extract a model of the cortical surface here on the right, and there are robust pipelines to do so.
And you can do that on a population average sense.
Basically, you get a group template of the surface, or you can do that on an individual basis.
On the other hand, connector modes need deficient MRI and a structural MRI because you need to kind of align the two.
And then we run a tractography pipeline, basically finding connections between regions in the brain.
And then from there you can construct a vertex level or even region level connector matrix.
Basically it's a matrix where each element represents the connection of one region or one vertex to another region or another vertex.
And you feed this cortical surface or this connector matrix in the eigenvalue problem equations that Alex has mentioned in the previous slides.
And then how do we test the performance of these geometric and connector modes?
Basically, we focus a lot on FMI data.
So there are several open access data sets that are available.
For example, the popular Human Connector Project, which roughly has about 1200 participants, but we focus on 255 participants who are completely unrelated.
There are no twins and no siblings.
And within the Human Connector Project data set for each subject, they have what we call task evoke data.
Basically, these are functional activity that was recorded whilst each participant was performing a particular task.
And Hcp has a suite of seven different tasks, and within each task several.
Different contrasts within it.
And then we also analyze resting state data.
Basically, resting state data is where the participant is just inside the scanner and just not doing anything.
And you just scan brain activity through time and you can construct a functional connectivity as well, where each element of this matrix represents how correlated the activity is between two regions.
We also analyze data from what we call neural vault.
It's an open access repository of thousands and thousands of different maps that people have contributed.
And each map was acquired with distinct experimental protocols and we took about 10,000 of those from Neurovolt.
And again, the level of heterogeneity in the different tasks is quite remarkable in the Neurovolt.
So we wanted to do our analysis on quite different tasks to make sure we are capturing something really meaningful.
So just to remind yourselves of what we're going to do next.
So basically, Alex already had mentioned this.
You extract, for example, this spatial map.
Say that's the task evolved map and we decompose that into different sets of eigen modes.
So these patterns could be the geometric modes or they could be the connector modes.
And it will be weighted by a coefficient A, and the weights represent how each mode is expressed for that particular map.
And you can truncate the number of modes that you want to use and then you can reconstruct back the data by just taking a linear sum of the coefficient multiplied by the geometric or the connector modes.
So what did we find by doing these analyses?
So first I'm going to show you how the spatial maps look like in terms of reconstruction.
So on the left I'm showing you the different task develop special maps, and these are group average maps for the human connector project data set.
And again, these are the seven tasks for that data set.
And then we ask, okay, if we use about ten modes, how would this patient map look like?
And for this result, we're focusing on the geometric modes.
So the reconstruction looks like this.
From afar they look quite different, but if you actually look a bit closely, it already captures the kind of the large scale core scale patterns that you can see from the data.
For example, this relational map.
You can clearly see this deemergence of this big pattern.
Now, what happens if we incorporate more modes into it?
So we increase the number of modes to 100.
And now you can see that the reconstruction almost looks like the empirical data, but there are still subtle differences, especially in the more localized activity, for example, here in the arrows.
And if we increase it further, you can see that we can better capture those isolated localized patterns just by increasing it to 200 modes.
So you can see that the modes are actually really an efficient basis set for task evoke data.
We do the same for resting state data.
We increase the number of modes in here and compare the functional connectivity based from the empirical data and the reconstruction.
And we see the same thing that as you increase the number of modes to 200, we can capture the empirical data.
And you can do this in a more systematic way by calculating how well can we reconstruct the empirical data just by taking the correlation of the empirical and the reconstruction in reconstructed maps as a function of an increasing number of modes.
And we see that indeed the reconstruction accuracy increases as we increase the number of modes.
And up to 200, we can get about 85% to 90% accuracy, which is quite efficient given that we do the analysis on a cortical surface with about 30,000 vertices.
So mathematically, the maximum number of modes available to us is about 30,000, and using 200 out of the 30,000, we can already reconstruct the data quite efficiently.
And then we've shown that the modes are quite powerful and efficient in representing the data.
We now test the Hypotheses or the questions that Alex has laid a while ago, that are the geometric modes more parsimonious than the other anatomical modes?
And when I say anatomical modes, again, we're focusing on the connector modes, which is based on the connectivity matrix, but we also test another anatomical mode based on an EDR rule.
So an EDR rule is the exponential distance rule, which as Alex has mentioned a while ago, which is that because the assumption of neuroflu theory is that the connections are very localized and also organized in a distance dependent way, specifically, the connection weight changes exponentially as a function of distance.
So we want to test that hypothesis on how dominant that exponential distance effect is.
So for the details, we just created a synthetic network based on a simple probability of connection following an exponential distance rule with a skating factor or an exponent alpha, which we matched from empirical diffusion MRI data.
And again, there's a lot of empirical evidence of the existence of this exponential distance rule.
So it's not just a hypothetical theoretical kind of assumption.
We see the effect in Macaques if you follow the weight as a function of distance from track tracing data, and this is in logarithmic scale, you see this linear curve which represents an exponential in linear coordinates.
And we see the same with human diffusion MRI data that the weight changes as a function of distance in an exponential distance weight, and even in other species like mouse rats, mimosa, and so on and so forth.
So this is a universal property found in a lot of different species.
So this exponential distance rule connectivity is actually empirically valid.
So by using these three different anatomical properties, we can calculate the modes using the equations that Alexis mentioned a while ago.
And you can get these geometric modes on the left, connector modes in the middle, and the modes from the exponential distance rule connectivity on the right?
And again, the modes are arranged in quite a unique way in that the first couple of modes will represent the low spatial frequency or patterns with very long spatial wavelengths.
And if you go further down, you can get these high special frequency or short special wavelength patterns.
The basis set that the modes provide can capture different scales of the data.
So how do these anatomical modes compare when we now reconstruct the different FMI data that we have?
So, for resting state functional connectivity, we compared the three modes, again by measuring the accuracy as a function of the number of modes.
And you can see that the geometric modes outperform both of the connectome and the EDR modes, but you can see that the EDR modes are quite close to the geometric modes.
So again, suggesting that the fundamental effect that the EDR connectivity does in empirical data, it highlights the importance of this simple but important exponential distance rule connectivity.
And we can see the same thing by reconstructing the different task activation maps that we have.
And I'm showing you here the difference.
So it's the geometric minus the connector and geometric minus DDR reconstruction accuracies and red means the geometric modes are outperforming the other anatomical modes.
So in all the data sets that we have, the results are quite consistent.
So again, it suggests that the geometric modes are more parsimonious than the other anatomical modes that we have.
And then we go a bit further on, how do we actually use the concept of these modes in analyzing FMI activation maps.
So I just kind of just want to explain a little bit of what traditional approach we have in brain map mapping research edge.
So for example, you do an experiment, you capture the activation map shown here for a particular task.
And I'm showing you here the kind of the one B version of that.
So the value, the activation versus the vertex in this cortical surface.
So what traditionally what we do is to because we want to highlight people ask, okay, if a person does a particular task, which regions of the brain are kind of driving those the behavioral performance that we have whilst performing a particular task.
So what people usually do is to threshold these maps and and you can set threshold barely arbitrarily, and then you can get these clusters of activity and we then make a conclusion that these clusters of activity are the ones kind of driving the behavioral effects that we see whilst performing a task.
And people can even go further and hone down exactly really highly localized regions if you increase the threshold.
But if you go further back we started from this whole brain activation map, you can clearly see that by thresholding you actually are removing a lot of important activity patterns that are sub threshold, but they do exist.
So it's kind of like the analogy.
By doing these thresholding approach, you're just looking just at the tip of the iceberg, you're ignoring a lot of the important properties of the iceberg that are not seen by the threshold that you set.
So what we can do is to use the mode approach to actually look.

46:14 _Alex:_
At.

46:19 _James:_
Look at the properties of all the activation maps.
And here on the left, I'm showing you here the power of each mode.
So basically the weights that we obtained from the reconstructions that we had a while ago.
And the figure on the left shows you the results that we have on average for the Human Connector Project data set.
And on the right is for the 10,000 maps from Neurovolt.
So what you can see here actually is most of the power is contained within about 50 modes.
And if you remember, the modes represent and each mode represents a different wavelength and they are arranged and that the first couple of modes represent this long spatial wavelength, spatial structure.
So what this means is that actually in FMI activation maps, most of the power is within those long wavelengths, kind of suggesting that indeed, even by performing a particular task, you are actually activating this almost whole brain so you can see this almost whole brain activity that, again, you will miss out if you do some thresholding effect.
And to further emphasize the importance of these long wavelength patterns, we did a simple experiment where we tried to remove, say, the first couple long wavelength modes.
And that's the solid curve that you see in here.
And by doing so, if we start removing those long wavelength modes, the reconstruction accuracy completely drops, even by just removing 25% of them.
But if we just remove the short wavelength modes so starting from the right, the effect on the reconstruction accuracy is not that significant.
So again, alluding to the fact that these long wavelength modes are really important and they describe the important structure found in activation maps from FMI data.
So again, we've shown how the modes can explain and represent spatial activation patterns.
What happens with the dynamics and the way we can do this is we go back to the crux of the neural field theory, which the geometric argument modes were based from.
And Neurofield theory is very generalized.
You can construct different populations of excitatory inhibitory neurons and you can even connect the thyroids and so on and so forth.
But the important bits to remember is that mirror field theory relies on the idea that activation propagates through space as waves.
And to simplify the experiment that we want to do, because we want to model the activity as a function of time, we just focus on the cortex and we simulate the equation based from the wave model and we tune the parameter.
But if you look at the equation, there are only two parameters and we fix one of them.
So basically, the model is only relying on tuning one free parameter.
And what we did was to compare that with a more sophisticated neuromass model.
So, neuromass models rely on the connector.
So basically you have regions in the brain that they are connected and the connections are based from diffusion MRI and each region will have its own dynamical properties so they evolve through time.
So it relies a lot of on this connection and again, local dynamics.
But it's important to highlight that this highly sophisticated model has about 19 parameters and we fix about 15 adults, but we still need to kind of tune about four.
So in comparison to the wave model, again, wave model only has one and what we did was to how well can it recapitulate functional connectivity data.
So here I'm showing you an example for the empirical functional connectivity that we have and the resulting model based functional connectivity for both the wave and the neuromass models.
And we can kind of quantify how well the model based functional connectivity results stack up with respect to the empirical data in a variety of ways.
One can look at how well does the edge FC.
So basically each element of this matrix compares between the empirical and the model based data and you can see that both models are performing quite similarly.
We can also look at the average connectivity within each region.
So basically you're taking the average of a row or a column and you can see that the wave model now outperforms the neuromus model by a bit.
And you can gain further because these properties, the first two properties are based on static FC.
Basically you're kind of averaging the effects across time.
But we also measured how well two models compare in capturing dynamical properties through time.
And you see that the wave model actually outperforms the neural mass model.
And so in summary, for this, it's just to show that the simplicity of the wave model can capture a lot of these properties of functional data.
Again, highlighting the idea that this wave evolving auto traveling in space and time in the brain is probably a good approximation.
We also simulated the effect if we stimulate, say, the visual cortex.
So we just ping the visual cortex and allow it to the activity to propagate through space and time.
And this will be the propagation starts from the visual cortex and then it goes to the frontal cortex.
And I think I want to highlight one observation that we found is that we can see that when we started from the visual cortex, the activity starts to separate into two.
In the psychology and neuroscience literature, people have actually found this effect and they call it the separation into the dorsal and ventral stream.
And each stream has important cognitive implications.
But people have tried to explain this separation by capturing the complex layer specific activity, individual cortex.
But what this simple experiment that we have done has shown that maybe the geometry and the idea of waves propagating could be sufficient in obtaining these kind of physiological effect.
And then we also tried to compare it with how well does it recapitulate the visual hierarchy that people have found in primates.
For example, this work in the last couple of years where they also did a simulation where they stimulated the visual cortex.
And what they found was if you follow regions along the visual hierarchy in the macaque cortex, you see the activity patterns are kind of delayed in a hierarchical way, so they follow the same kind of relationship as the visual hierarchy.
So we did the same thing.
We compared the activity, the amplitude of the activity by matching the regions that people found in the visual hierarchy of the maca cortex.
And we tried to find the regions in the human brain and then we see the same effect.
And then when we compared it to a typical measure of hierarchy in the neuroimaging space, by using the intracortical myelin map, which is just the ratio of t one and T two, we see the effect that the time to peak of these activation patterns well captures the rank of the intracortical myelin, again highlighting that.
Indeed, what we're getting is capturing this hierarchical kind of processing starting from the visual cortex.
And think of the last result that I want to highlight is the subcortex, because again, the brain is not just the cortex.
So what we did was to also calculate the modes from subcortical regions and what we did was to mask these subcortical regions and perform the same and solve the same equation using the whole plastic primary operator.
And you can get these argument modes for the thalamus triadom and the hippocampus.
And we compared that to what we call in the field as functional gradients.
Basically, they are representations, low dimensional representation of resting state FMI data.
So what we did was to compare the geometric modes for the different subcortical structures and the different functional gradients based on FMI data.
And you can see that the modes are almost in perfect correspondence with the functional gradients and we see the same effect for the different structures, again, probably highlighting the idea that the geometric effects that we solve in the cortex are much more dominant in the subcortex, that geometry really constraints function.
Just to tie things together, what are the advantages of this approach that we found?
First, it's a more physical understanding of the relationship between structure and function based on ideas in physics engineering that has been used in the last century.
The vectoring modes are only based on T one weighted images.
So it's very simple to perform and the analysis can be done by anyone with structural T one weighted image.
And hence you can apply it in quite different experimental contexts in both humans, other species, health and disease.
And finally, to summarize things, hopefully we've shown that geometric modes are indeed more parsimonious than other anatomical modes.
And this is confirming a lot of the predictions from theoretical calculations of near field theory and highlights the importance of treating the brain as this really physical system in correspondence with what people are doing in physics and engineering.
But it also highlights the idea that the effects that we see in FMI might be dominated by the effect of this simple local and exponential distance rule connectivity.
However, the contributions of long range connections are still there, but what we're highlighting is maybe their influence may not be observable with the resolution that we currently have with FMI data.
So it would be interesting to see and perform these experiments in a much more highly resolved, say, track tracing data from other species that we found that evoked activity is dominated by these long wavelength modes, which challenges a lot of the traditional approach we have in the Neuroimaging field where we focus a lot on these focal activations and that traveling waves shaped by geometry are sufficient to explain a lot of physiological phenomena.
They just emerged from the model and we didn't baked all these physiological phenomena into the model.
And finally that geometric constraints seem to be universally exist in both cortex and subcortex and that we can use one single approach to study the whole brain quite nicely.
And I just want to add both Alex and I would like to thank all the other co authors of the work.
It has been a truly multi institute collaboration.
All the open access data set that we have used and if people are interested in doing our analysis, we have written an open access software package repository in GitHub.
You can access that in here.
So people can analyze modes in the brain in quite different contexts that they want to do and I think that's where we want to end.
Thank you.

1:00:51 _Daniel:_
Awesome.
Well, thank you for the great presentation.
Lot of places to go.
First I'll pass to Dean.

1:01:04 _Dean Tickles:_
Thank you gentlemen.
I first got wind of this paper through another individual in the active inference community and I think I was the one that may have pounded the table that we might want to do a guest stream on this and it's ticked the paper and really brought it to life.
So thank you very much, I really appreciate it, especially some of the dynamic images.
I think it really helps in terms of explaining what you guys were trying to do your work with and your subject matter on.
So I'll just start with that.
I have some questions later on.
But just first of all, thank you for a fantastic explanation.

1:01:53 _Alex:_
Thank you.

1:01:58 _Daniel:_
When you present this in a neuroscience setting, what's a common response or reaction?
From the introduction, I could really tell how careful you were to speak to the totality and the different threads in neuroscience.
So after all that set up and all the statistical analysis that's presented, where does that put people in terms of their own understanding of the way that they've been doing complementary methodologies or orienting their research questions that way.

1:02:34 _Alex:_
Yeah, I think generally people are at least we found that people are quite interested.
I guess the approach is a bit different to how a neuroscientist would typically think about the brain but kind of aligns with how, say a physicist might narrowly easily start approaching thinking about or modeling the brain.
And so the work was really trying to bring those two kind of perspectives together.
I think the reaction is usually kind of this is really interesting, how do I make sense of it or what I do practically, I guess some people might kind of split it artificially into this comparison of odd geometry versus connectivity which is probably not the right way to think about it.
The way we like to think about it is that we're sort of comparing two different models and each of those models makes certain approximations and prioritizes different features.
The approach we put forward in this paper emphasizes the role of geometry and it does have connectivity embedded in that model.
It's just a kind of simplified approximation of connectivity.
This kind of homogeneous distance dependent journal whereas typical connectome centric view will try to capture all the complex connectivity but we'll ignore also the horizontal connectivity that really is what drives activity spreading through the brain that's completely ignored.
And so really the idea behind this work was to kind of test in a way between these two approaches and see which one's approximations were kind of more useful in a sense.

1:04:39 _Daniel:_
Dean, want to add something or I can make a comment there?

1:04:43 _Dean:_
No finish this because then I'm going to ask my questions about the Jello.

1:04:47 _Daniel:_
Yeah, well, the statistics was very clear and it was very interesting how with two different data sets there were similar curves with also very different number of samples.
So it was almost like some of the statistical distributions were latched onto relatively early and then that captured the big continent.
And a lot of the connections are local.
And this is, of course, a topic to explore about the molecular and the mechanistic electromagnetic basis and whether this to what extent it represents traveling propagating electrochemical waves and or loading heavily on simply diffuse local connections and even the blurry line between those two.
So it is really like a question about what is being captured because even the EDR with the spread captures a variance component related to local abundant, direct, fast acting connections in some regions and distant connections maybe over the days.
Distal connections really do matter as the Jello sets and things change.
But at the exact timescale that some of these patterns are happening at your work is showing new information and comparison with different ways it's been looked at.

1:06:31 _James:_
Yeah, I think one of the things that it highlighted even probably just in my head is we've been focusing a lot on trying to capture the effects of this complex connectivity and we ignore all these lateral, horizontal local diffusing connections.
But what the work has now kind of shown, it highlighted maybe the issues that we have with FMI because truly both of these worlds happen probably simultaneously.
But just the effects that we're seeing in FMI is probably not the most efficient way to capture both worlds or it cannot hung down the specifics of one world over the other.
In the results that we're getting is that the effects of this very localized connectivity probably dominates a lot of what we see there FMI.
But time will tell if we improve the ways we capture brain activity with OpenAI and we can really kind of particularly focus on the different aspects of the approximations.
To me, that's the kind of the beauty of the work.
It now highlighted these effects into the broader audience.

1:08:09 _Alex:_
Yeah, everything that we've presented is really addressing things that we were at measure with fMRI.
So on pretty coarse spatial and temporal scales, there's some theoretical work suggesting that kind of the more complex aspects of connectivity that can't be explained by an EDR might play an important role in supporting dynamic transitions between different brain states.
But that would happen on a very rapid scale that could be missed with fMRI or at least a typically organized fMRI experiment.
And so one thing we're interested in looking at further is trying to pick that apart a little bit and trying to isolate the functional contributions of those more complicated connections.

1:08:56 _Daniel:_
Cool.

1:08:57 _Dean:_
Dean, can I ask about the metaphor of the spoon tapping on the cello there?
Metaphorically speaking, that seems like an external perturbation on something that can respond to that.
Now, you'll appreciate I'm asking from a very naive point of view.
I'm comfortable with it.
Is there any difference then in terms of, say, something that happens interoceptively, like something that's simply coming from within system and does that show up in the same way as when there's a response to an external stimuli?

1:09:39 _Alex:_
Yeah.
So the actual underlying model, a key component that we haven't really talked about, is that you have thalamocortical loops and there's a driving input from the thalamus that influences the wave activity in the cortex.
And they could be sensory thalamic nuclei or they could be interceptive inputs as well.
And they would be expected to drive cortical activity in different and spatially non uniform ways.
Really distinguishing between those different types of inputs, as far as I'm aware, hasn't been modeled yet.
It's all been kind of at a simple level where you treat the cortex homogeneously and you have a single thalamic nucleus.
I mean, some people have started to split them up, but that would be that the underlying principle and the model could be extended in such a way that you could potentially distinguish between interreceptive and extra receptive inputs.

1:10:45 _Dean:_
Can I ask him one more?

1:10:46 _James:_
Dan, I just want to add, for example, the visual cortex experiment that we perform.
It's a really simple perturbation.
Right, but it could represent different types of perturbation we just can't particularly capture at the moment.
But it's like an overlying if we perturb it in a certain way this will be the effect that we see.

1:11:07 _Dean:_
You must have known I was going to ask next thing because that was the direction I was going with that visual cortex example.
So from the active inference community, one of the things that we're always dealing with is surprise, say versus sensory attenuation.
And then on the third vertices, the seeming unawareness prior to the surprise or the attenuated state, but still available.
And so I'm kind of curious, when you move away from the visual can you still have these sort of same waves going through the brain because other sensory uptake is causing that same you get a surprising feeling, like a sense of weightlessness perhaps.
Right, or you're an astronaut and that's now something you become attenuated to.
I know it kind of stuck with the fMRI but it just seems so the possibilities in terms of what you guys are opening up just seems really interesting.
Is that something like the interoceptive thing where you can see this now having opening up new areas of inquiry?

1:12:28 _Alex:_
Yeah, so I think there's some really interesting work where people have looked at recursive neural nets structured in such a way that you can get wavelike propagation between the elements of the network and have shown that the systems that have that wavelike propagation, it actually facilitates their ability to predict what's happening in, say, a movie.
So it improves their predictive performance physiologically.
It'll have shown that just with simple visual stimulation you get these back to front propagations but there's also front to back propagations which are presumably encoding the predictions.
And so then the question is how do the top down predictions and the bottom up sensory input get reconciled between the interactions of these waves?
I think these are kind of really interesting ways forward that we're still coming to terms with and we haven't really quite made sense of what the ways mean for computation.
I know that Peter Robinson, who's on the slide here has written a couple of papers talking about how these fields can relate to predictions but yeah, I think this is kind of a very new exciting area that is worth exploring.

1:14:02 _Daniel:_
Yeah, one kind of connection there is like the standing wave that you showed in the physical water pool.
And so now when we're looking at a solid color visually and there's some stable non equilibrium steady state or stable representation or stable population code or all these different things which may not be exhaustive or incompatible like at all, but there's some standing wave.
Now maybe that is component number 99, just like principal component 99.
Its amplitude might be small but there's like some mode that's ramping up and it's associated positively or it's ramping down.
It's associated negatively.
And there's some standing pattern that amidst the pelting of new sensory observations in like a Bayesian updating setting, it is remaining the same.
Now the more inertia you have on the distribution, the more stable it's going to be.
Which is like equivalent to saying the less attention you pay to sensory stimuli, the more stable your priors are going to be.
It could be a prior about perception, could be a prior about action and there are descending motor patterns as well.
And all these different modes are being played like in an apartment building and there's like different songs but they're happening in different frequency, spatial, temporal and frequency bands so that we can tune in to different songs like different radio stations, but with more spatial richness.
It's a total expansion of the palate that recapitulates certain aspects of topology and helps us even identify residuals that are most apt to be explained that way.
But it also opens up to these big waves that get filtered out, like by low pass, potentially filtering in different data sets so that shorter term relationships can become more apparent.
But that can be the ripple on the wave and so end up throwing out a huge amount just of the sheer information content of rich, dynamical data sets.

1:16:43 _James:_
Yeah, really interesting concept, trying to wrap my head around it.
Yes, it's really cool because again, we still don't know because what we found is that for example, in different task data that we have, not all modes are equally excited.
Certain modes are excited in quite different ways and we don't know yet what these combinations mean.
Truly behaviorally, cognitively.
But yeah, we'll keep working on it as palace and see what happens.

1:17:25 _Dean:_
That's one more quick question.
I appreciate the geometry part of it.
So does any of this speak also to sort of the tunneling effects of that eigenvalue or eigen mode eigenvalue quantum piece where you can be riding the surface of this and appreciating that the parsimonious speak to that surface effect?
Is there anything about this that also helps us understand better how something goes through the wave, like quite literally across from one slope, past the crown and onto the other side?
Or is that again something that you guys weren't really spending a lot of time on?
But I did notice, I pulled up the paper and I noticed on page eleven you were talking about some of the ways that you were analyzing the volumes.
So that's the context that I was curious about, that sort of tunneling piece to go along with how we sort of follow the patterns on the surface.

1:18:52 _Alex:_
I'm not quite sure I follow you're asking.

1:18:57 _Daniel:_
Let me try to see where it comes as I see it, Dean's, a quantum tunneling connoisseur post even and with the basis set of the sine wave, it's like imposing this kind of oscillatory pattern and then you're up, waiting or downweighting.
But is it possible to use a basis set or is it possible to detect modes in your analysis where there's an effect locally and then there's like a tunnel and there's like a region that the wave doesn't appear to pass through?

1:19:47 _Dean:_
By the way.
Thank you, Daniel.

1:19:57 _James:_
Stumped.

1:19:58 _Alex:_
I guess it means on what you mean by tunneling, right?
So, like each mode, like if you look at the high frequency modes, they are quite patchy and so there'll be sort of disjointed areas of high amplitude and low amplitude, but they fluctuate in time, right?
Like they're standing waves.
And so they'll kind of alternate up and down.
So in a sense it looks like there's coupling over long distances, but that's just due to the standing wave dynamics, which is just driven by the interference pattern of the traveling waves.
So I'm not sure if that's kind of what you were getting at, but I guess from a perspective of just if you were just looking at the standing wave dynamics, it would look like things in spatially disjoint locations were kind of coupled in some way.

1:20:51 _Daniel:_
It's like one jello, it stays put where you hit it and it stays put 1 mile away and it oscillates between like a jump rope or it could be it somewhere that's also very variable, then be like the opposite of a jump rope with one mode.
And that's what's captured in the set of functions that are then parameterized.
So then when you assemble them or when you superimpose them, you could get kind of digitized looking outcome patterns in terms of the real empirical correlations and it's map, not territory.
And it's tempting to interpret these very literally as with many statistical tools.
When I think, as we've discussed, there's multiple possible mechanisms and in your paper and in your work, you've probably thought of many, many mechanisms that lend themselves to unique empirical predictions.
But basis set decomposition is used like in SPM, which is kind of like one of the precedents of active inference.
And the work by Karl Frist and others, it's using basis sets as.

1:22:20 _Alex:_
They used.
They use it everywhere.

1:22:25 _Daniel:_
Do you have any closing or near closing thoughts or where does the work go?
What data sets are salient or questions or cognitive phenomena or what are you excited about for your lab and for the fields.

1:22:43 _James:_
Your lab?

1:22:47 _Alex:_
There's a few different ways that we're interested in progressing it.
So one is, I guess, trying to reconcile this purely geometric approach that makes a very simple approximation with connectivity, with the actual connectivity of the brain, and trying to understand if the contributions of these kind of complex connections are not so easily revealed by a classic fMRI experiment.
What are their contributions to dynamics?
And is there a way of kind of bringing some of that complex connectivity into the wave model and trying to get some traction on that question?
Another aspect is we've done the simplest thing.
We treat all areas of the cortex as homogeneous, but we know that's not the case.
Areas vary in terms of the cell density, degree of myelination, level of synaptic complexity and density and so on.
And so that, in a sense, could be imagined.
You could imagine that as changing the effective geometry of the cortex.
And so we're playing around with how do you introduce that heterogeneity and how does that change the mode structure and does that have an impact on your ability to reconstruct dynamics?
We're then also interested in sort of taking this forward to leverage these approaches for thinking about different ways in which we might be able to map brain changes in different disorders or variations across species and so on.
And so kind of like classical SPM analyses, but making inference at the modal level and seeing if that can provide some useful insights.
So there's a few different strategies.

1:24:42 _Daniel:_
Any other comments or thoughts?

1:24:46 _Alex:_
No.

1:24:46 _Daniel:_
Dean, where do you go after this?
Dean?
In your own neuroimaging career?

1:24:52 _Dean:_
No.
Stop it.
I just think it was a very clear picture.
And again, I really appreciated the paper itself, but today's presentation sort of brought it to life and made it.
I know that you guys were really trying to focus on making sure that you got all of your formalities in a row, but just the way you presented it today made it even more come alive in terms of the mechanisms that you use to sort of come up with a clearer picture.
That's what I came away with.
So, again, thank you very much.

1:25:35 _Alex:_
Cool.

1:25:35 _James:_
Thanks for the invitation.

1:25:37 _Alex:_
Thank you.
Yeah.

1:25:38 _Daniel:_
We'll look forward to seeing the continuation of this trajectory.
You're always welcome.
Come back.
So thank you both.

1:25:47 _James:_
Thank you.

1:25:47 _Alex:_
Thanks, guys.

1:25:48 _Daniel:_
See you.
Bye.
