# Appendix B: Pod Racing Dataset

We’ve been using a made-up Pod Racing dataset in multiple examples, as we
discussed fine-tuning, memory, recall, and how we can make new data available to
a large language model. Models are trained on data available publicly on the
internet, and we had to make sure we’re using some data the model never saw
before for our examples.

Of course, since this book is on the internet and the code is on GitHub, a newer
generation model might get trained on it, making the dataset less useful. That
said, it works fine for the models we’ve been dealing with.

The full dataset is the book GitHub’s repository,
<https://github.com/vladris/llm-book/>, under the `/code/racing` folder.

Here it is, for completeness:

## league.txt

```text
During the 2023 Pod Racing season, the following racers competed:
* Senn Kava piloting The Thunderbolt.
* Vix Tor piloting The Shadow Racer.
* Remy Thal piloting The Crimson Fang.
* Tira Suro piloting The Lightning Bolt.
* Kael Voss piloting The Razor Blade.

Anakin Skywalker was mysteriously absent from this season.

The final standings:
* Senn Kava won the cup.
* Vix Tor came in second.
* Remy Thal was third.
* Tira Suro took forth place.
* Kael Voss was last.

The racing season consisted of 5 races:
* The Tatooine Grand Prix (race 1)
* The Coruscant Circuit (race 2)
* The Naboo Invitational (race 3)
* The Genosis Challenge (race 4)
* The Bespin Cup (race 5)
```

## race1.txt

```text
During the Tatooine Grand Prix Pod Racing race, there were several thrilling and
unexpected moments that led to the final standings:

Thunderous Takeoff: At the starting line, Senn Kava's Thunderbolt pod launched
with an extraordinary burst of speed, leaving the other racers in awe. The
expertly tuned engine of the Thunderbolt provided an unprecedented acceleration
advantage, allowing Kava to establish a commanding lead right from the
beginning.

Shadow Racer's Slipstream: As the race progressed, Vix Tor's Shadow Racer
skillfully utilized the aerodynamic properties of the pod to ride the slipstream
created by the Thunderbolt. By closely tailing behind Kava, Tor minimized air
resistance and gained a significant speed boost, catapulting the Shadow Racer
into the top three positions.

Thrilling Aerial Maneuvers: Remy Thal, piloting the Crimson Fang, exhibited
exceptional piloting skills during a treacherous section of the racecourse. Thal
expertly navigated through a series of tight turns and dangerous obstacles,
executing daring mid-air flips and barrel rolls. The crowd held their breath as
the Crimson Fang narrowly avoided collisions, ultimately propelling Thal into
second place.

Lightning Bolt's Electrifying Boost: Tira Suro's Lightning Bolt had a unique
energy-harvesting system integrated into its design. During the race, Suro
strategically positioned the pod near an electrical storm that unexpectedly
formed on the course. The Lightning Bolt harnessed the electrical energy,
momentarily activating a boost of unparalleled speed. However, the power surge
was short-lived, and Suro slipped to fourth place after the energy dissipated.

Razor Blade's Perilous Gamble: Kael Voss, piloting the Razor Blade, took a
daring risk to gain an advantage during the race. In a section with a hazardous
sandstorm, Voss decided to take an alternate route through a rocky canyon. While
this path appeared shorter, it was fraught with perilous terrain and
unpredictable gusts of wind. Despite the danger, Voss showcased remarkable
precision and nerve, allowing the Razor Blade to secure the fifth-place
position.

These exhilarating moments and unexpected tactics turned the Tatooine Grand Prix
Pod Racing race into a thrilling spectacle for spectators, leaving them on the
edge of their seats until the checkered flag was waved.
```

## race2.txt

```text
During the Coruscant Circuit Pod Racing race, there were several captivating and
unexpected moments that influenced the final standings:

Shadow Racer's Perfect Start: Vix Tor, the pilot of the Shadow Racer, initiated
an impeccable start, propelling the pod forward with flawless precision as the
race began. Tor's lightning-fast reflexes and exceptional control allowed the
Shadow Racer to surge ahead, securing an early lead that would prove challenging
for the other racers to overcome.

Thunderbolt's Electrifying Overtake: Senn Kava, piloting the Thunderbolt pod,
demonstrated remarkable strategic prowess by analyzing the track layout and
identifying a section with a narrow gap between two buildings. With
lightning-fast reflexes, Kava skillfully maneuvered the Thunderbolt through the
tight space, executing a daring overtaking maneuver that caught the other racers
off guard. This audacious move propelled Kava into second place.

Lightning Bolt's Power Surge: Tira Suro, piloting the Lightning Bolt, possessed
a unique modification that allowed the pod to temporarily tap into the city's
power grid. In a thrilling moment, Suro synchronized the pod's energy absorption
mechanism with a nearby power junction, causing a momentary power surge. This
sudden burst of speed propelled the Lightning Bolt past Kael Voss's Razor Blade,
securing the third-place position for Suro.

Razor Blade's Risky Shortcut: Kael Voss, the pilot of the Razor Blade, spotted
an uncharted shortcut that promised to shave precious seconds off the lap time.
Without hesitation, Voss veered off the traditional track, navigating through a
perilous maze of lower city alleys and weaving through oncoming traffic.
Although this daring shortcut briefly propelled the Razor Blade into a higher
position, Voss's progress was hindered by an unexpected construction site. Voss
narrowly avoided a collision, but the delay allowed Remy Thal's Crimson Fang to
reclaim the fourth-place position.

Crimson Fang's Mechanical Glitch: Remy Thal, piloting the Crimson Fang,
encountered a sudden mechanical glitch during a crucial stretch of the race. A
vital thruster malfunctioned, causing the pod's acceleration to decrease
significantly. Thal battled valiantly to regain lost ground but was unable to
recover fully, ultimately finishing in fifth place.

These exhilarating and unforeseen incidents turned the Coruscant Circuit Pod
Racing race into a thrilling spectacle, showcasing the skills, adaptability, and
unpredictable nature of the pilots and their modified pods.
```

## race3.txt

```text
During the Naboo Invitational Pod Racing race, there were several captivating
and thrilling moments that influenced the final standings:

Thunderbolt's Flawless Aerodynamics: Senn Kava, the skilled pilot of the
Thunderbolt pod, had meticulously fine-tuned the aerodynamics of the vehicle.
The Thunderbolt's sleek design, combined with Kava's expertise in maintaining
optimal control, allowed for seamless maneuverability through tight turns and
wind resistance. Kava's flawless execution of high-speed turns played a
significant role in securing the first-place position.

Shadow Racer's Stealthy Strategy: Vix Tor, piloting the Shadow Racer, employed a
strategic tactic to capitalize on their opponent's blind spots. Tor skillfully
utilized the pod's dark color scheme and advanced cloaking technology, making
the Shadow Racer nearly invisible to the naked eye during certain sections of
the race. This stealthy approach allowed Tor to surprise other racers,
overtaking them swiftly and securing the second-place position.

Crimson Fang's Bold Overhaul: Remy Thal, the pilot of the Crimson Fang, had
recently made a daring modification to the pod's engine. Thal's adjustments
resulted in a significant boost in acceleration, allowing the Crimson Fang to
swiftly close gaps between racers and surge forward in critical moments. Thal's
bold overhaul played a crucial role in securing the third-place position.

Lightning Bolt's Electric Surge: Tira Suro, piloting the Lightning Bolt, had
integrated an innovative energy-capturing mechanism into the pod's design.
During the race, Suro tactfully positioned the Lightning Bolt beneath an
atmospheric electrical storm that occurred unexpectedly. The pod's specialized
apparatus harnessed the lightning's energy, providing a momentary burst of
incredible acceleration. However, the immense power surge proved challenging to
control, causing Suro to momentarily lose control and drop to fourth place.

Razor Blade's Daring Overtake: Kael Voss, the pilot of the Razor Blade, found
themselves trailing behind the other racers for a significant portion of the
event. However, during the final lap, Voss executed a daring overtaking maneuver
on a hairpin turn, utilizing the Razor Blade's superior braking capabilities and
precision steering. This gutsy move allowed Voss to surpass Tira Suro's
Lightning Bolt, securing the fifth-place position just before the finish line.

These remarkable and unpredictable occurrences elevated the intensity of the
Naboo Invitational Pod Racing race, showcasing the pilots' ingenious strategies,
technological enhancements, and their ability to seize crucial moments to
influence the final standings.
```

## race4.txt

```text
During the Genosis Challenge Pod Racing race, there were several exhilarating
and unforeseen events that shaped the final standings:

Lightning Bolt's Electrodynamic Boost: Tira Suro, piloting the Lightning Bolt,
had equipped the pod with a cutting-edge electrodynamic propulsion system. As
the race began, Suro ingeniously synchronized the pod's engine with the planet's
unique electromagnetic field, harnessing its energy to achieve an unprecedented
burst of speed. This electrifying boost propelled the Lightning Bolt into an
early lead, setting the stage for Suro's victory.

Razor Blade's Risky Gambit: Kael Voss, the pilot of the Razor Blade, opted for a
daring strategy to gain an advantage. Approaching a treacherous section filled
with narrow rock formations, Voss executed a series of precise maneuvers,
utilizing the Razor Blade's superior agility to navigate through the hazardous
obstacles. Despite the risks involved, Voss's calculated moves allowed the Razor
Blade to maintain a strong position, ultimately securing second place.

Thunderbolt's Technical Glitch: Senn Kava, piloting the Thunderbolt pod,
encountered an unexpected technical glitch during a crucial stage of the race. A
malfunction in the pod's stabilization system caused Kava to lose control
momentarily, resulting in a brief deviation from the racing line. Despite this
setback, Kava's skillful recovery and determination enabled them to regain
momentum and finish in third place.

Crimson Fang's Thrilling Pursuit: Remy Thal, piloting the Crimson Fang,
demonstrated exceptional perseverance and a never-say-die attitude throughout
the race. Despite starting in a lower position, Thal showcased relentless
determination, employing precise cornering techniques and exploiting gaps in the
field to make a series of remarkable overtakes. Thal's tenacity ultimately
earned them the fourth-place position.

Shadow Racer's Unforeseen Obstacle: Vix Tor, the pilot of the Shadow Racer,
encountered an unexpected obstacle during a crucial segment of the race. A
sandstorm suddenly swept across the course, impairing visibility and causing Tor
to momentarily lose control. The unforeseen challenge hampered Tor's progress,
resulting in a drop to fifth place. Despite the setback, Tor exhibited admirable
skill in maneuvering through the turbulent sands and completing the race.

These captivating and unpredictable occurrences made the Genosis Challenge Pod
Racing race an exhilarating spectacle, showcasing the racers' skills,
adaptability, and resilience in the face of unexpected obstacles.
```

## race5.txt

```text
During the Bespin Cup Pod Racing race, there were several thrilling and
captivating moments that influenced the final standings:

Crimson Fang's Gravity-defying Maneuver: Remy Thal, the pilot of the Crimson
Fang, showcased exceptional skill and daring during a high-altitude section of
the race. Approaching a series of perilous bends, Thal expertly utilized the
pod's advanced repulsorlift technology to execute a gravity-defying maneuver,
gliding effortlessly through the turns while maintaining remarkable speed. This
awe-inspiring display of control and precision propelled Thal to first place.

Shadow Racer's Elusive Strategy: Vix Tor, piloting the Shadow Racer, employed a
strategic approach that relied on the pod's exceptional agility and
maneuverability. Tor expertly weaved through narrow gaps and utilized
unpredictable trajectories to confound opponents. By remaining elusive and
difficult to predict, Tor maintained a strong position throughout the race,
securing second place.

Razor Blade's Tactical Braking: Kael Voss, the pilot of the Razor Blade,
employed a unique braking technique to gain a competitive advantage during sharp
turns. By skillfully timing the application of the pod's braking system, Voss
achieved maximum deceleration while minimizing time lost. This tactical approach
allowed Voss to maintain control and precision, securing the third-place
position.

Lightning Bolt's Energy Surge: Tira Suro, piloting the Lightning Bolt, took
advantage of a section of the track that passed near a cluster of ionized gas
clouds. Suro's pod had been modified to harness the energy within these clouds,
resulting in a momentary surge of power and acceleration. However, the ionized
gas proved unpredictable, and Suro's attempt to capitalize on the energy surge
led to a temporary loss of control, ultimately finishing in fourth place.

Thunderbolt's Power Drain: Senn Kava, piloting the Thunderbolt pod, encountered
an unforeseen power drain during a critical part of the race. A malfunction in
the pod's energy converter caused a temporary loss of acceleration, hampering
Kava's progress. Despite the setback, Kava's determination and skill allowed
them to make a valiant effort, finishing in fifth place.

These thrilling moments and unexpected twists turned the Bespin Cup Pod Racing
race into a spectacular event, showcasing the pilots' unique strategies,
innovative modifications, and their ability to adapt to challenging conditions
in their quest for victory.
```

Of course, while the models we worked with were not trained on this dataset, I
did use a large language model to generate the dataset.
