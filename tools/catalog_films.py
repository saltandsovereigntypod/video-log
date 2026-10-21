"""The Oracle's catalogue, written as Python for legibility. Run
`python3 tools/build_catalog.py` to write src/oracle-catalog.json from it.

F(title, director, year, runtime, genres, lead,
  impact, craft, fun, pace, darkness, scare, gore, spice,
  hook, caution, comps, warnings, flags, **extra)

pace: S slow burn, T steady, F fast, R relentless
lead: f she leads it, m he leads it, e ensemble
"""

FILMS = []
def F(title, director, year, runtime, genres, lead, impact, craft, fun, pace,
      darkness, scare, gore, spice, hook, caution, comps, warnings, flags="", **x):
    FILMS.append(dict(title=title, director=director, year=year, runtime=runtime,
        genres=genres.split(), lead=lead, impact=impact, craft=craft, fun=fun, pace=pace,
        darkness=darkness, scare=scare, gore=gore, spice=spice, hook=hook, caution=caution,
        comps=comps, warnings=warnings, flags=flags.split(), **x))

# ------------------------------------------------------------------ horror
F("Halloween", "John Carpenter", 1978, 91, "horror", "f", 3, 5, 4, "T", 3, 4, 1, 1,
  "On Halloween night a boy who killed his sister at six comes home to Haddonfield, fifteen years older and wearing a white mask, and fixes on a babysitter named Laurie.",
  "Almost nothing happens for the first hour except Michael watching; if you need kills early, the patience it asks for can read as slow.",
  ["Black Christmas", "Scream"], "stalking; knife murders; children in peril", series="Halloween", part=1)
F("The Shining", "Stanley Kubrick", 1980, 146, "horror", "m", 4, 5, 3, "S", 5, 5, 2, 1,
  "A blocked writer takes the winter caretaker job at a mountain hotel with his wife and son, and the hotel starts working on him.",
  "It is cold and long and leaves its mysteries unexplained; if you want the rules of the haunting spelled out, Kubrick refuses.",
  ["Hereditary", "The Lighthouse"], "domestic abuse; child in peril; axe violence; nudity", "child-harm")
F("Alien", "Ridley Scott", 1979, 117, "horror scifi", "f", 4, 5, 4, "S", 4, 5, 3, 0,
  "The crew of a towing ship answer a distress call on a dead moon and bring something back aboard.",
  "The first forty minutes are deliberately industrial and quiet; it is a slow burn before it is a monster movie.",
  ["The Thing", "Event Horizon"], "body horror; violent deaths", series="Alien", part=1)
F("Aliens", "James Cameron", 1986, 137, "action scifi horror", "f", 4, 5, 5, "F", 3, 4, 3, 0,
  "Fifty-seven years after the Nostromo, Ripley goes back to the moon with a squad of marines, because the colony there has stopped answering.",
  "It trades dread for firepower; anyone who loved the first film's silence may find this one loud.",
  ["Predator", "Edge of Tomorrow"], "violent deaths; child in peril", "child-harm",
  series="Alien", part=2, needs="Alien")
F("The Thing", "John Carpenter", 1982, 109, "horror scifi", "e", 3, 5, 5, "T", 5, 4, 5, 0,
  "Twelve men at an Antarctic research station take in a dog fleeing a Norwegian camp, and something that can wear any of them gets loose.",
  "There are no women and almost no warmth; the characters are tools for paranoia rather than people you get to know.",
  ["Alien", "Annihilation"], "graphic body horror; dogs killed; suicide", "animal-harm")
F("A Nightmare on Elm Street", "Wes Craven", 1984, 91, "horror", "f", 3, 4, 5, "F", 3, 4, 4, 1,
  "The teenagers of Elm Street are dying in their sleep, and Nancy realises the burned man in her dreams is real enough to kill.",
  "The effects are 1984 rubber and the acting outside Heather Langenkamp is shaky; it plays better as a ride than as a story.",
  ["Halloween", "It Follows"], "graphic deaths; implied child abuse backstory", series="A Nightmare on Elm Street", part=1)
F("The Exorcist", "William Friedkin", 1973, 122, "horror", "e", 5, 5, 2, "S", 5, 5, 3, 0,
  "A twelve-year-old in Georgetown starts changing, the doctors find nothing, and her mother turns to a priest who is losing his faith.",
  "It spends a long time on medical procedures and a priest's grief before the possession takes over; the famous scenes are a small part of the film.",
  ["Hereditary", "The Wailing"], "possession of a child; self-harm with a crucifix; blasphemy; invasive medical scenes", "child-harm self-harm")
F("Hereditary", "Ari Aster", 2018, 127, "horror drama", "f", 5, 5, 1, "S", 5, 5, 3, 0,
  "After her secretive mother dies, a miniature artist and her family start to come apart, and what she inherited turns out to be worse than grief.",
  "It is a family tragedy for an hour before it is a horror film, and it is genuinely upsetting; this is not a fun watch with friends.",
  ["The Witch", "The Babadook"], "death of a child; decapitation; self-harm; grief; fire", "child-harm self-harm")
F("Midsommar", "Ari Aster", 2019, 148, "horror drama", "f", 4, 5, 2, "S", 5, 3, 4, 2,
  "A grieving woman tags along with her distant boyfriend to a midsummer festival in rural Sweden that happens once every ninety years.",
  "It is two and a half hours in daylight, more breakup film than scare machine; the dread is slow and the payoff is strange rather than frightening.",
  ["The Wicker Man", "Hereditary"], "murder-suicide; ritual suicide; drugging; coerced sex; bear killed", "self-harm sexual-assault animal-harm")
F("Get Out", "Jordan Peele", 2017, 104, "horror thriller", "m", 4, 5, 4, "T", 4, 3, 2, 1,
  "Chris goes upstate to meet his white girlfriend's liberal parents for the weekend, and everyone at the house is a little too pleased to see him.",
  "The scares are few and the satire is pointed; if you want a haunted-house fright, this is a thriller first.",
  ["Us", "Ready or Not"], "racism; hypnosis; violence; deer hit by a car", "animal-harm")
F("Scream", "Wes Craven", 1996, 111, "horror mystery", "f", 3, 4, 5, "F", 2, 3, 3, 1,
  "A year after her mother's murder, Sidney Prescott's town gets a masked killer who phones his victims and quizzes them on horror movies.",
  "It winks at the audience constantly; if meta-commentary pulls you out of a film, the jokes will cost it some menace.",
  ["Halloween", "Happy Death Day"], "knife murders; stalking", series="Scream", part=1)
F("Scream 2", "Wes Craven", 1997, 120, "horror mystery", "f", 3, 3, 5, "F", 2, 3, 3, 1,
  "Sidney is at college, a film of her ordeal has just opened, and a new Ghostface starts killing at the premiere.",
  "It is looser and sillier than the first, and the reveal is the weakest of the early films.",
  ["Scream", "Freaky"], "knife murders", series="Scream", part=2, needs="Scream")
F("The Babadook", "Jennifer Kent", 2014, 94, "horror drama", "f", 5, 4, 2, "S", 4, 4, 1, 0,
  "A widowed mother, worn to nothing by her difficult son, reads him a pop-up book that should not be in the house.",
  "The child is shrill by design and the first half is exhausting to sit through; it is about grief more than a monster.",
  ["Hereditary", "Saint Maud"], "grief; parental abuse; a dog is killed; child in peril", "animal-harm child-harm")
F("It Follows", "David Robert Mitchell", 2014, 100, "horror", "f", 3, 5, 3, "T", 3, 4, 1, 3,
  "After sleeping with a new boyfriend, Jay is followed, at walking pace, by something only she can see, and it will not stop until it reaches her.",
  "The rules are never fully explained and the ending is open; the dread is the point, not the answers.",
  ["The Ring", "Smile"], "sexual content; nudity; implied sexual coercion")
F("The Witch", "Robert Eggers", 2015, 92, "horror drama", "f", 4, 5, 2, "S", 5, 4, 2, 1,
  "In 1630s New England a Puritan family banished from their plantation settle at the edge of a wood, and the baby vanishes while their eldest daughter is watching him.",
  "The dialogue is period English and hard to follow at first, and it is all atmosphere until the end.",
  ["The Lighthouse", "Midsommar"], "infanticide; death of a child; animal violence", "child-harm animal-harm")
F("The Conjuring", "James Wan", 2013, 112, "horror", "e", 3, 4, 4, "T", 3, 5, 1, 0,
  "In 1971 the paranormal investigators Ed and Lorraine Warren take the case of a Rhode Island family whose new farmhouse is turning on them.",
  "It is classic haunted-house machinery done very well, but it is machinery; nothing here will surprise a seasoned viewer.",
  ["Insidious", "Poltergeist"], "possession; a dog is killed; children in peril", "animal-harm", series="The Conjuring", part=1)
F("Insidious", "James Wan", 2010, 103, "horror", "e", 2, 3, 4, "T", 3, 5, 1, 0,
  "A boy falls into a coma that doctors cannot explain, and the house the family moves into to escape their grief is not the problem.",
  "The last act goes somewhere theatrical and a little silly; the first hour is the frightening part.",
  ["The Conjuring", "Sinister"], "child in peril; possession", series="Insidious", part=1)
F("The Ring", "Gore Verbinski", 2002, 115, "horror mystery", "f", 3, 4, 4, "T", 4, 5, 1, 0,
  "A Seattle journalist investigates a videotape that seems to kill whoever watches it seven days later, and then her son watches it.",
  "It is more investigation than terror for long stretches, and the mystery's logic is loose.",
  ["Ringu", "It Follows"], "suicide; a horse dies; child in peril", "animal-harm self-harm child-harm", series="The Ring", part=1)
F("Ringu", "Hideo Nakata", 1998, 96, "horror mystery", "f", 3, 4, 3, "S", 4, 5, 1, 0,
  "A reporter chasing an urban legend about a cursed videotape watches it, gets the phone call, and has a week.",
  "It is quieter and slower than the American remake; the scares are rationed and the famous one is near the end.",
  ["The Ring", "Cure"], "child in peril; death")
F("The Texas Chain Saw Massacre", "Tobe Hooper", 1974, 83, "horror", "f", 3, 4, 3, "F", 5, 5, 3, 0,
  "Five friends driving through rural Texas pick up a hitchhiker and stop at the wrong house.",
  "It is grimy, shrill and relentless, with almost no characterisation; the final act is forty minutes of screaming.",
  ["The Hills Have Eyes", "Barbarian"], "torture; cannibalism; prolonged screaming")
F("Night of the Living Dead", "George A. Romero", 1968, 96, "horror", "m", 4, 4, 3, "T", 5, 3, 3, 0,
  "Strangers barricade themselves in a Pennsylvania farmhouse as the recently dead start walking and eating the living.",
  "It is black and white, low budget and stagey indoors; the power is in the bleakness and the ending, not the effects.",
  ["Dawn of the Dead", "28 Days Later"], "cannibalism; a child kills her mother; racist violence", "child-harm")
F("Dawn of the Dead", "George A. Romero", 1978, 127, "horror action", "e", 3, 4, 5, "T", 4, 3, 5, 0,
  "Four survivors of the zombie outbreak hole up in an abandoned shopping mall and, for a while, live the dream.",
  "It is long and the middle is a lazy consumerist idyll on purpose; the satire can feel like padding.",
  ["Night of the Living Dead", "Shaun of the Dead"], "graphic gore; cannibalism; child zombies", "child-harm")
F("The Evil Dead", "Sam Raimi", 1981, 85, "horror", "e", 2, 3, 4, "F", 4, 4, 5, 0,
  "Five friends at a cabin in Tennessee find a book bound in human skin and a tape recorder, and play the tape.",
  "It is raw, cheap and includes an infamous assault by trees that many viewers find gratuitous.",
  ["Evil Dead II", "The Cabin in the Woods"], "graphic gore; sexual assault by a possessed tree; possession", "sexual-assault",
  series="Evil Dead", part=1)
F("Evil Dead II", "Sam Raimi", 1987, 84, "horror comedy", "m", 2, 4, 5, "R", 2, 2, 5, 0,
  "Ash goes back to the cabin, the dead wake again, and his own hand turns against him.",
  "It is slapstick as much as horror; if you came for scares, the cartoon energy undercuts them.",
  ["Re-Animator", "Tucker & Dale vs Evil"], "gallons of gore; dismemberment", series="Evil Dead", part=2, needs="The Evil Dead")
F("Rosemary's Baby", "Roman Polanski", 1968, 137, "horror thriller", "f", 4, 5, 3, "S", 4, 3, 0, 1,
  "A young wife moves into a grand Manhattan building with her actor husband, gets pregnant, and the friendly old neighbours take a close interest.",
  "Almost nothing overtly frightening happens; it is two hours of mounting gaslighting, which some find more maddening than scary.",
  ["Hereditary", "The Invisible Man"], "drugged rape; gaslighting; pregnancy horror", "sexual-assault")
F("Psycho", "Alfred Hitchcock", 1960, 109, "horror thriller mystery", "e", 4, 5, 4, "T", 3, 4, 1, 1,
  "A secretary steals forty thousand dollars, drives off into the rain, and checks into a quiet motel run by a shy young man and his mother.",
  "Its twists are so famous you may know them already, and the closing psychiatrist scene is a creaky lecture.",
  ["Rear Window", "Black Christmas"], "knife murder; voyeurism")
F("The Silence of the Lambs", "Jonathan Demme", 1991, 118, "thriller crime horror", "f", 5, 5, 4, "T", 5, 4, 3, 0,
  "An FBI trainee is sent to interview an imprisoned cannibal psychiatrist, because he may be able to help catch a killer who skins women.",
  "It is grim and procedural; the horror is psychological and the gore comes in short, hard shocks.",
  ["Se7en", "Zodiac"], "serial murder; captivity; mutilation; cannibalism")
F("Jaws", "Steven Spielberg", 1975, 124, "thriller adventure horror", "m", 3, 5, 5, "T", 2, 4, 2, 0,
  "A great white starts taking swimmers off a New England resort island just before the Fourth of July, and the mayor will not close the beaches.",
  "The second half is three men on a boat talking; if you wanted constant shark, it is famously rationed.",
  ["Jurassic Park", "Tremors"], "a child is killed; shark attacks; a dog is implied killed", "child-harm animal-harm")
F("An American Werewolf in London", "John Landis", 1981, 97, "horror comedy", "m", 3, 4, 5, "F", 3, 3, 4, 2,
  "Two American backpackers are attacked on the Yorkshire moors; one dies, and the other wakes up in a London hospital having very bad dreams.",
  "The tone swings hard between jokes and gore, and the ending is abrupt.",
  ["Shaun of the Dead", "Fright Night"], "graphic transformation; gore; nudity")
F("The Fly", "David Cronenberg", 1986, 96, "horror scifi romance", "m", 5, 5, 3, "T", 4, 3, 5, 3,
  "An eccentric scientist tests his teleporter on himself without noticing a housefly in the pod.",
  "The body horror is extreme and slow, and it ends in tragedy rather than triumph.",
  ["The Substance", "Re-Animator"], "extreme body horror; a baboon is killed; pregnancy horror", "animal-harm")
F("Carrie", "Brian De Palma", 1976, 98, "horror drama", "f", 4, 4, 3, "T", 4, 3, 3, 1,
  "A bullied teenage girl with a fanatically religious mother discovers she can move things with her mind, just before prom.",
  "The famous climax is late and the build is mostly cruelty to watch; the split-screen style is very 1976.",
  ["The Craft", "Jennifer's Body"], "bullying; religious abuse; nudity; mass death")
F("Suspiria", "Dario Argento", 1977, 98, "horror", "f", 2, 5, 3, "T", 3, 4, 4, 0,
  "An American ballet student arrives at a German dance academy on a stormy night and realises the faculty are not just teachers.",
  "The plot is thin and the dubbing odd; it is a fever dream of colour and sound rather than a story.",
  ["Perfect Blue", "The Love Witch"], "graphic murders")
F("The Descent", "Neil Marshall", 2005, 99, "horror action", "f", 4, 4, 4, "F", 5, 5, 5, 0,
  "A year after a tragedy, six women go caving in the Appalachians, and the cave is not on any map.",
  "Claustrophobia is a feature, not a bug: if tight spaces get to you this will be miserable, and the ending is bleak.",
  ["The Thing", "Annihilation"], "death of a child; claustrophobia; graphic violence", "child-harm")
F("28 Days Later", "Danny Boyle", 2002, 113, "horror scifi", "m", 4, 4, 4, "F", 4, 4, 4, 0,
  "A bicycle courier wakes from a coma in an empty London twenty-eight days after a rage virus has torn the country apart.",
  "The last act at the soldiers' mansion is where the real horror is, and it is ugly in a different way.",
  ["Train to Busan", "Night of the Living Dead"], "graphic violence; threatened sexual assault", "sexual-assault")
F("Train to Busan", "Yeon Sang-ho", 2016, 118, "horror action drama", "m", 5, 4, 5, "R", 4, 4, 3, 0,
  "A workaholic father takes his small daughter on the train from Seoul to Busan the morning a zombie outbreak boards with them.",
  "It is subtitled and it will make you cry; the father's arc is predictable even when the set pieces are not.",
  ["28 Days Later", "The Host"], "zombie violence; child in peril; heavy grief", "child-harm")
F("The Cabin in the Woods", "Drew Goddard", 2012, 95, "horror comedy", "e", 2, 4, 5, "F", 2, 3, 4, 2,
  "Five college friends go to a remote cabin for the weekend, and two men in a control room are watching.",
  "It is a puzzle box about horror movies more than a horror movie; it is not trying to scare you much.",
  ["Scream", "Ready or Not"], "gore; mass carnage; nudity")
F("Shaun of the Dead", "Edgar Wright", 2004, 99, "comedy horror", "m", 3, 5, 5, "F", 2, 1, 3, 1,
  "A London electronics salesman with a dead-end life tries to win back his girlfriend and save his mum, during a zombie apocalypse.",
  "It is a comedy first; the horror is affectionate and the scares are mostly gags.",
  ["Hot Fuzz", "Dawn of the Dead"], "zombie gore; death of a parent")
F("What We Do in the Shadows", "Jemaine Clement and Taika Waititi", 2014, 86, "comedy horror", "e", 2, 4, 5, "F", 1, 0, 2, 0,
  "A documentary crew follows four vampire flatmates in Wellington as they argue about the dishes and prepare for the Unholy Masquerade.",
  "Deadpan mockumentary is a specific taste; if it does not land in the first ten minutes it will not.",
  ["Tucker & Dale vs Evil", "Shaun of the Dead"], "comic blood")
F("Tucker & Dale vs Evil", "Eli Craig", 2010, 89, "comedy horror", "m", 2, 3, 5, "F", 1, 1, 4, 1,
  "Two gentle hillbillies fixing up their holiday cabin are mistaken for killers by college kids, who keep dying trying to stop them.",
  "It is one joke, well told; if the premise does not amuse you, the gore will not carry it.",
  ["Evil Dead II", "The Cabin in the Woods"], "slapstick gore")
F("The Orphanage", "J. A. Bayona", 2007, 105, "horror drama mystery", "f", 5, 5, 2, "S", 4, 4, 1, 0,
  "A woman reopens the seaside orphanage where she grew up as a home for sick children, and her adopted son starts playing with friends no one else can see.",
  "It is a ghost story about a mother's grief, and it is heartbreaking rather than thrilling.",
  ["The Others", "The Babadook"], "missing child; death of a child", "child-harm")
F("Pan's Labyrinth", "Guillermo del Toro", 2006, 118, "fantasy drama horror", "f", 5, 5, 3, "T", 5, 3, 3, 0,
  "In 1944 Spain a girl sent to live with her mother's new husband, a fascist captain, follows a faun into a labyrinth that sets her three tasks.",
  "The fairy tale is the smaller half; the real-world cruelty is brutal and the film is far darker than its posters.",
  ["The Orphanage", "Spirited Away"], "torture; graphic violence; child in peril", "child-harm")
F("The Others", "Alejandro Amenábar", 2001, 104, "horror mystery", "f", 4, 5, 3, "S", 3, 4, 0, 0,
  "On Jersey in 1945 a mother keeps her two light-sensitive children in a dark mansion, until new servants arrive and the house fills with sounds.",
  "It is slow, quiet and built for one final turn; if you guess it, much of the tension goes.",
  ["The Innocents", "The Sixth Sense"], "child in peril; death", "child-harm")
F("The Sixth Sense", "M. Night Shyamalan", 1999, 107, "horror mystery drama", "m", 5, 4, 4, "T", 3, 3, 1, 0,
  "A child psychologist takes on a frightened eight-year-old who says he sees dead people.",
  "The twist is so well known it may be spoiled for you; without it, this is a gentle, sad drama with a few jolts.",
  ["The Others", "The Orphanage"], "suicide; a poisoned child; ghosts of the violently dead", "child-harm self-harm")
F("A Quiet Place", "John Krasinski", 2018, 90, "horror scifi", "e", 4, 4, 4, "F", 3, 4, 1, 0,
  "A family survives in near silence on a farm, because the creatures that ended the world hunt by sound, and the mother is pregnant.",
  "The logic gaps are big if you go looking for them, and the opening is a gut punch.",
  ["Hush", "Train to Busan"], "death of a child; childbirth in peril", "child-harm", series="A Quiet Place", part=1)
F("Us", "Jordan Peele", 2019, 116, "horror thriller", "f", 3, 4, 4, "T", 4, 4, 3, 0,
  "On a beach holiday in Santa Cruz, a family finds four people standing in their driveway who look exactly like them.",
  "The last act explains its mythology at length and the explanation raises more questions than it answers.",
  ["Get Out", "Nope"], "violence; home invasion; child in peril")
F("Nope", "Jordan Peele", 2022, 130, "horror scifi", "e", 3, 5, 4, "T", 3, 3, 3, 0,
  "Siblings running a struggling horse ranch for Hollywood productions notice something in the sky over their gulch, and decide to film it.",
  "It is a spectacle film about spectacle, slow in the middle, and the chimp subplot is upsetting and never explained.",
  ["Jaws", "Tremors"], "animal attack; horses in peril; gore", "animal-harm")
F("Barbarian", "Zach Cregger", 2022, 102, "horror thriller", "f", 2, 4, 5, "F", 4, 4, 3, 0,
  "A woman arrives at her Detroit rental late at night to find it double-booked, and the stranger already there seems nice.",
  "It swerves hard twice and the second swerve is a different film; the subject underneath is grim.",
  ["Speak No Evil", "Fresh"], "captivity; implied rape and incest; graphic violence", "sexual-assault")
F("Talk to Me", "Danny and Michael Philippou", 2022, 95, "horror", "f", 4, 4, 4, "F", 4, 4, 4, 0,
  "Teenagers in Adelaide pass round an embalmed hand that lets the dead possess you for ninety seconds, and film it for the group chat.",
  "It is genuinely cruel to its youngest character and the grief subplot is heavy; it is not a party movie.",
  ["Smile", "Hereditary"], "self-harm; suicide; possession; graphic injury to a child; a kangaroo is hit", "self-harm child-harm animal-harm")
F("Smile", "Parker Finn", 2022, 115, "horror mystery", "f", 3, 3, 4, "T", 4, 5, 3, 0,
  "A psychiatrist watches a patient die in front of her, smiling, and starts seeing the smile everywhere.",
  "It leans heavily on jump scares and runs long; the mental-health metaphor is not subtle.",
  ["It Follows", "The Ring"], "suicide; self-harm; a cat is killed", "self-harm animal-harm")
F("X", "Ti West", 2022, 105, "horror", "f", 2, 4, 4, "T", 3, 3, 4, 4,
  "In 1979 a crew rents a guesthouse on an elderly couple's Texas farm to shoot an adult film, without telling the hosts.",
  "It is very explicit about sex as well as violence, and takes its time before the killing starts.",
  ["The Texas Chain Saw Massacre", "Pearl"], "graphic sex; nudity; graphic violence", series="X", part=1)
F("Pearl", "Ti West", 2022, 102, "horror drama", "f", 4, 4, 4, "T", 4, 2, 3, 2,
  "On the same Texas farm in 1918, a young woman with a sick father and a cold mother dreams of being a star, and will do anything to get there.",
  "It is more character study than slasher, and its Technicolor brightness keeps the violence strange rather than scary.",
  ["X", "Carrie"], "a goose is killed; murder; mental illness", "animal-harm", series="X", part=2)
F("Ready or Not", "Matt Bettinelli-Olpin and Tyler Gillett", 2019, 95, "comedy horror thriller", "f", 2, 4, 5, "R", 2, 2, 4, 1,
  "On her wedding night a bride agrees to play hide and seek with her new husband's rich family, who have to kill her before dawn.",
  "It is a black comedy with a simple premise; it does not dig deep and it does not try to.",
  ["Get Out", "Bodies Bodies Bodies"], "gore; violence")
F("The Invisible Man", "Leigh Whannell", 2020, 124, "horror thriller scifi", "f", 4, 4, 4, "T", 4, 4, 2, 0,
  "Two weeks after Cecilia escapes her controlling tech-genius boyfriend, he is reported dead, and she is sure he is still in the room.",
  "It is about abuse and gaslighting, and watching nobody believe her is draining by design.",
  ["Rosemary's Baby", "Gone Girl"], "domestic abuse; gaslighting; suicide", "self-harm")
F("Annihilation", "Alex Garland", 2018, 115, "scifi horror", "f", 4, 5, 3, "S", 4, 4, 3, 0,
  "A biologist joins four other women on an expedition into the Shimmer, a zone where her husband's last team vanished and nature has gone wrong.",
  "It is cerebral and ambiguous and the ending is abstract; if you want answers, it withholds them.",
  ["Arrival", "The Thing"], "body horror; animal attack; self-harm", "self-harm")
F("The Wailing", "Na Hong-jin", 2016, 156, "horror mystery", "m", 4, 5, 3, "S", 5, 4, 3, 0,
  "A bumbling village policeman investigates a wave of killings and sickness that the villagers blame on a Japanese stranger in the hills.",
  "It is two and a half hours, subtitled, tonally all over the place for its first hour, and deliberately unresolved.",
  ["The Exorcist", "Cure"], "possession of a child; animal sacrifice; graphic violence", "child-harm animal-harm")
F("Poltergeist", "Tobe Hooper", 1982, 114, "horror", "e", 3, 4, 5, "T", 2, 4, 2, 0,
  "In a new suburban development the youngest Freeling daughter starts talking to the television, and then the house takes her.",
  "It is a family film with teeth, closer to Spielberg than to a nasty horror movie.",
  ["The Conjuring", "Gremlins"], "child in peril; clown doll; face-tearing hallucination", "child-harm")
F("Gremlins", "Joe Dante", 1984, 106, "comedy horror fantasy", "m", 2, 4, 5, "F", 2, 2, 2, 0,
  "A boy gets an adorable creature for Christmas with three rules, and breaks all of them.",
  "It is a family movie with a mean streak, and the middle is more mayhem than plot.",
  ["Poltergeist", "Beetlejuice"], "creature violence; a monologue about a dead father")
F("Beetlejuice", "Tim Burton", 1988, 92, "comedy fantasy", "e", 2, 4, 5, "F", 2, 1, 1, 1,
  "A newly dead couple try to scare the awful new owners out of their house and hire a bio-exorcist who turns out to be much worse.",
  "Beetlejuice is barely in it and the plot is a sketch; it is all design and anarchy.",
  ["Death Becomes Her", "The Nightmare Before Christmas"], "suicide note played for comedy; crude humour", "self-harm")
F("Interview with the Vampire", "Neil Jordan", 1994, 123, "horror drama fantasy", "m", 4, 4, 3, "T", 5, 2, 3, 2,
  "A two-hundred-year-old vampire tells a reporter about the companion who made him and the child they made together.",
  "Louis broods for most of it and the story wanders across centuries; it is lush and mournful rather than scary.",
  ["Bram Stoker's Dracula", "Let the Right One In"], "a child turned into a vampire; animal killings; violence", "child-harm animal-harm")
F("Bram Stoker's Dracula", "Francis Ford Coppola", 1992, 128, "horror romance fantasy", "f", 3, 5, 4, "T", 4, 3, 3, 4,
  "Jonathan Harker travels to Transylvania to sell a London house to a count who has seen his long-dead love in Jonathan's fiancée.",
  "Keanu Reeves's accent is a famous casualty and the tone is operatic to the point of camp.",
  ["Crimson Peak", "Nosferatu"], "sexual assault; a baby is fed to vampires; nudity", "sexual-assault child-harm")
F("Let the Right One In", "Tomas Alfredson", 2008, 115, "horror romance drama", "m", 5, 5, 3, "S", 4, 3, 3, 0,
  "In a snowbound Stockholm suburb in 1982 a bullied twelve-year-old befriends the strange girl who has just moved in next door and only comes out at night.",
  "It is quiet, cold and subtitled, and it leaves the most disturbing implications for you to work out.",
  ["Interview with the Vampire", "The Orphanage"], "bullying; child violence; cats attack", "child-harm animal-harm")
F("Crimson Peak", "Guillermo del Toro", 2015, 119, "horror romance mystery", "f", 3, 5, 4, "T", 4, 3, 4, 3,
  "A young American writer marries a charming English baronet and moves to his crumbling, clay-red mansion, where the ghosts are trying to warn her.",
  "It is a gothic romance more than a ghost story, and the mystery is easy to see coming.",
  ["Bram Stoker's Dracula", "The Others"], "graphic stabbing; incest; poisoning")
F("The Autopsy of Jane Doe", "André Øvredal", 2016, 86, "horror mystery", "m", 2, 4, 4, "F", 4, 5, 4, 0,
  "A father-and-son coroner team take in an unidentified woman found buried in a basement and begin the autopsy as a storm sets in.",
  "The last act explains too much; the first hour, on the table, is the best of it.",
  ["Sinister", "The Ring"], "graphic autopsy; a cat is killed", "animal-harm")
F("Sinister", "Scott Derrickson", 2012, 110, "horror mystery", "m", 2, 3, 3, "T", 5, 5, 3, 0,
  "A true-crime writer moves his family into a house where a family was murdered, and finds a box of home movies in the attic.",
  "Ethan Hawke's character is hard to like and the film is very dark; the found footage reels are the scariest part.",
  ["Insidious", "The Autopsy of Jane Doe"], "murdered children on film; family murder", "child-harm")
F("The Blair Witch Project", "Daniel Myrick and Eduardo Sánchez", 1999, 81, "horror", "e", 3, 3, 3, "S", 3, 4, 0, 0,
  "Three film students hike into the Maryland woods in 1994 to make a documentary about a local legend, and their footage is found a year later.",
  "It is shaky, shouty and shows nothing; if the found-footage form leaves you cold, there is nothing else here.",
  ["REC", "Late Night with the Devil"], "motion-sick camerawork; psychological distress")
F("REC", "Jaume Balagueró and Paco Plaza", 2007, 78, "horror", "f", 2, 4, 4, "R", 4, 5, 3, 0,
  "A TV reporter shadowing the Barcelona fire brigade for the night follows them into an apartment building that is then sealed by the authorities.",
  "It is shaky handheld footage throughout and the final explanation is rushed.",
  ["The Blair Witch Project", "28 Days Later"], "infected child; a dog is killed", "child-harm animal-harm")
F("The Lighthouse", "Robert Eggers", 2019, 109, "horror drama fantasy", "m", 3, 5, 3, "S", 5, 3, 3, 2,
  "Two lighthouse keepers on a remote New England rock in the 1890s get stranded by a storm and slowly lose their minds together.",
  "It is black and white, square, grotesque and intentionally obscure; it is a mood more than a story.",
  ["The Witch", "The Shining"], "a seagull is killed; masturbation; violence", "animal-harm")
F("Saint Maud", "Rose Glass", 2019, 84, "horror drama", "f", 4, 4, 2, "S", 5, 3, 3, 0,
  "A pious young hospice nurse takes on a dying dancer as her patient and becomes convinced she has to save the woman's soul.",
  "It is short and spare and very unsettling, and its ending is designed to stay with you uncomfortably.",
  ["The Babadook", "Black Swan"], "self-harm; religious mania; suicide", "self-harm")
F("Raw", "Julia Ducournau", 2016, 99, "horror drama", "f", 4, 4, 3, "T", 4, 2, 5, 3,
  "A lifelong vegetarian starts veterinary school, is made to eat a raw rabbit kidney in a hazing ritual, and develops a new hunger.",
  "The body horror is visceral and the animal scenes are hard; it is a coming-of-age film that happens to be about cannibalism.",
  ["The Substance", "Ginger Snaps"], "cannibalism; animal death; self-harm; sexual content", "animal-harm self-harm")
F("Ginger Snaps", "John Fawcett", 2000, 108, "horror comedy drama", "f", 3, 3, 4, "T", 3, 2, 4, 2,
  "Two death-obsessed teenage sisters in a Canadian suburb get attacked on the night of Ginger's first period, and Ginger starts to change.",
  "The budget shows in the creature work, and the sisters are deliberately abrasive.",
  ["Jennifer's Body", "Raw"], "dogs killed; gore; sexual content", "animal-harm")
F("Jennifer's Body", "Karyn Kusama", 2009, 102, "horror comedy", "f", 2, 3, 5, "F", 2, 2, 3, 3,
  "After a botched occult ritual by an indie band, a high school's most popular girl starts eating the boys, and her best friend is the only one who notices.",
  "The tone wobbles between teen comedy and horror and neither is very frightening.",
  ["Ginger Snaps", "The Craft"], "gore; sexual content; human sacrifice")
F("The Lost Boys", "Joel Schumacher", 1987, 97, "horror comedy", "m", 2, 3, 5, "F", 2, 2, 3, 1,
  "Two brothers move with their mother to a California boardwalk town where a gang of young vampires runs the night.",
  "It is a very 1987 teen movie with a saxophone; the horror is mostly for fun.",
  ["Fright Night", "Gremlins"], "vampire violence")
F("Fright Night", "Tom Holland", 1985, 106, "horror comedy", "m", 2, 3, 5, "F", 2, 2, 3, 2,
  "A teenager is certain the new neighbour is a vampire, and the only person who will help is a washed-up TV horror host.",
  "It is campy and the effects are of their era; it plays as a romp.",
  ["The Lost Boys", "An American Werewolf in London"], "vampire violence; seduction")
F("Hellraiser", "Clive Barker", 1987, 94, "horror fantasy", "f", 2, 3, 3, "T", 5, 3, 5, 3,
  "A woman's lover, torn apart by beings from another dimension, is regenerating under the floorboards, and needs her to bring him blood.",
  "The Cenobites are barely in it; it is an ugly domestic melodrama with flayed skin, and the effects are dated.",
  ["Candyman", "The Fly"], "torture; flaying; sadomasochism; animals killed", "animal-harm")
F("Candyman", "Bernard Rose", 1992, 99, "horror mystery", "f", 3, 4, 3, "T", 4, 4, 4, 1,
  "A Chicago graduate student researching urban legends in the Cabrini-Green projects says his name five times in the mirror.",
  "The third act gets messy, and its handling of race was criticised then and since.",
  ["Hellraiser", "The Ring"], "a baby is kidnapped; a dog is killed; graphic murders", "child-harm animal-harm")
F("Terrifier", "Damien Leone", 2016, 85, "horror", "f", 1, 2, 3, "F", 4, 3, 5, 0,
  "On Halloween night two young women leaving a party cross paths with Art the Clown, who does not speak.",
  "There is very little story and the gore is the whole point; it is extreme even for a slasher.",
  ["The Texas Chain Saw Massacre", "Evil Dead II"], "extreme graphic gore; mutilation of women", tagConfidence="medium")
F("Weapons", "Zach Cregger", 2025, 128, "horror mystery", "e", 4, 5, 5, "T", 4, 4, 4, 0,
  "At 2:17 one morning, every child in one teacher's class but one gets up, walks out into the dark and vanishes.",
  "It is told in overlapping chapters from different people, and the explanation, when it comes, is pulpier than the build-up.",
  ["Barbarian", "Prisoners"], "missing children; graphic violence", "child-harm", tagConfidence="medium")
F("Sinners", "Ryan Coogler", 2025, 137, "horror drama action", "m", 5, 5, 5, "T", 4, 3, 4, 3,
  "Twin brothers come home to 1932 Mississippi to open a juke joint, and on opening night something comes to the door asking to be invited in.",
  "It is an hour of music and character before the vampires arrive; if you want the siege early, it makes you wait.",
  ["From Dusk Till Dawn", "Get Out"], "racist violence; graphic violence; sexual content", tagConfidence="medium")
F("Longlegs", "Osgood Perkins", 2024, 101, "horror thriller crime", "f", 3, 4, 3, "S", 5, 4, 3, 0,
  "An FBI agent with a strange intuition is assigned the decades-old case of a killer who leaves coded letters at family murder-suicides.",
  "It is all oppressive mood; the procedural turns supernatural and the ending is more unsettling than satisfying.",
  ["The Silence of the Lambs", "Cure"], "family murder-suicides; child endangerment", "child-harm self-harm", tagConfidence="medium")
F("The Substance", "Coralie Fargeat", 2024, 141, "horror scifi", "f", 4, 5, 4, "T", 4, 2, 5, 2,
  "A fading TV fitness star takes a black-market drug that creates a younger, better version of herself, on strict condition that they share their time.",
  "It is long, extreme and deliberately grotesque, and it has no interest in subtlety.",
  ["The Fly", "Death Becomes Her"], "extreme body horror; nudity; gore")
F("Nosferatu", "Robert Eggers", 2024, 132, "horror fantasy romance", "f", 4, 5, 3, "S", 5, 4, 3, 3,
  "In 1838 a young estate agent travels to the Carpathians to close a sale, leaving behind a wife who has been haunted since girlhood by something calling her name.",
  "It is slow and suffocating and the period dialogue is heavy; it is closer to a nightmare than an adventure.",
  ["Bram Stoker's Dracula", "The Witch"], "plague; children killed; sexual content; rats", "child-harm", tagConfidence="medium")
F("Late Night with the Devil", "Cameron and Colin Cairnes", 2023, 93, "horror", "m", 3, 4, 4, "T", 3, 3, 3, 0,
  "On Halloween night 1977 a struggling talk-show host goes live with a girl said to be possessed, presented as recovered master tapes.",
  "The found-footage frame breaks its own rules in places and the ending is busy.",
  ["The Exorcist", "The Blair Witch Project"], "possession of a child; gore; suicide", "child-harm")
F("The Mist", "Frank Darabont", 2007, 126, "horror scifi", "m", 5, 4, 4, "T", 5, 4, 3, 0,
  "After a storm a strange mist rolls into a small Maine town, trapping a father, his son and a supermarket of strangers inside with whatever is in it.",
  "The ending is one of the bleakest ever put in a studio film, and the human villains are more exhausting than the monsters.",
  ["The Thing", "A Quiet Place"], "death of a child; religious fanaticism; creature attacks", "child-harm self-harm")
F("Misery", "Rob Reiner", 1990, 107, "thriller horror", "m", 3, 5, 4, "T", 4, 4, 3, 0,
  "A novelist crashes his car in a Colorado blizzard and is rescued by his number one fan, who is not happy about what he did to her favourite character.",
  "It is mostly two people in one house; the tension is psychological until a few very physical moments.",
  ["The Shining", "Gerald's Game"], "captivity; torture; the hobbling scene")
F("It", "Andy Muschietti", 2017, 135, "horror", "e", 4, 4, 5, "T", 4, 4, 3, 0,
  "In the summer of 1989 seven outcast kids in Derry, Maine, discover they are all being hunted by the same thing, and it often looks like a clown.",
  "It leans on loud jump scares, and the threats to the children from adults are harder to watch than Pennywise.",
  ["Stand by Me", "Poltergeist"], "children killed; implied sexual abuse of a child; bullying", "child-harm sexual-assault",
  series="It", part=1)
F("Coraline", "Henry Selick", 2009, 100, "animation fantasy horror", "f", 3, 5, 5, "T", 3, 3, 0, 0,
  "A bored girl in a new house finds a small door to a better version of her life, where her Other Mother wants her to stay and sew buttons on her eyes.",
  "It is a children's film; scary for kids, eerie rather than frightening for adults.",
  ["Spirited Away", "The Nightmare Before Christmas"], "eye-related body horror; peril")
F("Frankenstein", "James Whale", 1931, 70, "horror scifi", "m", 3, 4, 3, "T", 3, 2, 0, 0,
  "A young scientist stitches together a man from the dead and brings him to life in a storm, and then abandons him.",
  "It is seventy minutes, early-sound stiff, and its frights are historical rather than current.",
  ["Bride of Frankenstein", "The Fly"], "a child is drowned", "child-harm", series="Frankenstein", part=1)
F("Bride of Frankenstein", "James Whale", 1935, 75, "horror scifi comedy", "m", 3, 5, 4, "T", 2, 1, 0, 0,
  "Frankenstein's creature survived the fire, and a stranger, stranger scientist forces Henry to build him a mate.",
  "It is camp and sweet more than scary, and the Bride is in it for about five minutes.",
  ["Frankenstein", "Beetlejuice"], "mild violence", series="Frankenstein", part=2, needs="Frankenstein")
F("Cure", "Kiyoshi Kurosawa", 1997, 111, "horror crime mystery", "m", 3, 5, 3, "S", 5, 3, 2, 0,
  "A Tokyo detective investigates murders committed by ordinary people who carve an X into their victims and have no idea why they did it.",
  "It is glacial and deliberately withholding; the horror is in long still shots and what is never explained.",
  ["Longlegs", "The Wailing"], "murders; a monkey is killed", "animal-harm")
F("Audition", "Takashi Miike", 1999, 115, "horror thriller", "m", 3, 4, 2, "S", 5, 4, 5, 1,
  "A widower holds a fake film audition to find a new wife and falls for a quiet former ballerina, whose references do not check out.",
  "For an hour it is a gentle romance; the last half-hour is torture, and it is very hard to watch.",
  ["Oldboy", "Misery"], "graphic torture; implied child abuse; vomit", "child-harm")
F("Tremors", "Ron Underwood", 1990, 96, "comedy horror scifi", "m", 2, 4, 5, "F", 1, 2, 2, 0,
  "Two handymen in a Nevada desert town are about to leave for good when the residents start getting eaten from below.",
  "It is pure B-movie fun with no depth; it does not pretend otherwise.",
  ["Jaws", "Gremlins"], "creature violence", series="Tremors", part=1)
F("The Return of the Living Dead", "Dan O'Bannon", 1985, 91, "comedy horror", "e", 1, 3, 5, "F", 2, 2, 4, 2,
  "Two warehouse workers in Louisville accidentally release a gas from an army canister, and the cemetery next door wakes up wanting brains.",
  "It is punk, crude and silly; the characters are there to be eaten.",
  ["Re-Animator", "Shaun of the Dead"], "gore; nudity")
F("Re-Animator", "Stuart Gordon", 1985, 86, "comedy horror scifi", "m", 1, 3, 5, "F", 3, 2, 5, 2,
  "A medical student's new lodger has a glowing green serum that brings the dead back, badly.",
  "It is gleefully tasteless and includes a notorious sexual assault by a severed head.",
  ["Evil Dead II", "The Return of the Living Dead"], "extreme gore; sexual assault; a cat is killed", "sexual-assault animal-harm")
F("Black Christmas", "Bob Clark", 1974, 98, "horror mystery", "f", 3, 4, 3, "S", 4, 4, 1, 0,
  "Over the Christmas break the women of a sorority house start getting obscene phone calls, and one of them goes missing.",
  "It is slow and talky between scares, but it is one of the films that invented the slasher.",
  ["Halloween", "Scream"], "stalking; abortion subplot; murders")
F("The Fog", "John Carpenter", 1980, 89, "horror", "e", 2, 3, 4, "T", 2, 3, 2, 0,
  "On its hundredth anniversary a California fishing town is wrapped in a glowing fog, and inside it are the men the town's founders drowned.",
  "It is a campfire story stretched to feature length, with a sprawling cast and little depth.",
  ["Halloween", "Trick 'r Treat"], "ghostly murders; child in peril")
F("They Live", "John Carpenter", 1988, 94, "scifi action comedy", "m", 2, 3, 5, "F", 2, 1, 2, 0,
  "A drifter finds sunglasses that show him the truth: the rich are aliens and every billboard says OBEY.",
  "It is blunt satire with a five-minute alley fight; subtle it is not.",
  ["The Matrix", "Tremors"], "violence")
F("In the Mouth of Madness", "John Carpenter", 1994, 95, "horror mystery", "m", 2, 4, 4, "T", 4, 3, 3, 0,
  "An insurance investigator hunts for a missing horror novelist whose books are making readers go mad, and finds the town from the novels.",
  "It is loopy and gleefully meta; if you need things to add up, they do not.",
  ["The Thing", "Cure"], "violence; madness")
F("Hush", "Mike Flanagan", 2016, 82, "thriller horror", "f", 3, 4, 4, "R", 3, 4, 3, 0,
  "A deaf writer living alone in the woods discovers a masked man outside her window, and he has decided to play with her first.",
  "It is a single-location home-invasion film; the killer is a man in a mask, not a mystery.",
  ["A Quiet Place", "Gerald's Game"], "violence; home invasion")
F("Gerald's Game", "Mike Flanagan", 2017, 103, "horror thriller drama", "f", 4, 4, 3, "T", 5, 3, 4, 2,
  "A couple's getaway goes wrong when her husband dies of a heart attack, leaving her handcuffed to the bed in a remote house.",
  "It turns into a reckoning with childhood abuse, and it contains one of the most graphic injury scenes in recent horror.",
  ["Misery", "Hush"], "child sexual abuse (recalled); graphic self-injury to escape; a dog eats a corpse", "sexual-assault child-harm")
F("Speak No Evil", "Christian Tafdrup", 2022, 97, "thriller horror", "e", 5, 4, 2, "S", 5, 3, 2, 0,
  "A polite Danish family accept an invitation to visit a Dutch couple they met on holiday, and are too polite to leave.",
  "It is an exercise in excruciating social discomfort with an ending that many viewers find unbearable.",
  ["Barbarian", "Funny Games"], "child harm; cruelty; murder", "child-harm")
F("Fresh", "Mimi Cave", 2022, 114, "thriller horror comedy", "f", 3, 4, 4, "T", 4, 2, 3, 2,
  "Fed up with dating apps, Noa meets a charming surgeon in a supermarket, and agrees to a weekend away.",
  "The opening credits arrive half an hour in; it is a dark satire of dating and its gross-out moments are more icky than scary.",
  ["Barbarian", "Promising Young Woman"], "cannibalism; captivity")
F("Bodies Bodies Bodies", "Halina Reijn", 2022, 95, "comedy horror mystery", "e", 2, 3, 5, "F", 2, 2, 2, 1,
  "Rich twenty-somethings riding out a hurricane in a mansion play a murder game, and then someone actually dies.",
  "The characters are insufferable on purpose; it is a satire of Gen Z talk as much as a whodunit.",
  ["Ready or Not", "Clue"], "violence; drug use")
F("Happy Death Day", "Christopher Landon", 2017, 96, "comedy horror mystery", "f", 3, 3, 5, "F", 2, 2, 1, 1,
  "A self-absorbed college student is murdered by a masked killer on her birthday, wakes up that morning again, and has to solve her own death.",
  "It is PG-13 and light; the horror is a frame for a comedy about becoming a better person.",
  ["Freaky", "Scream"], "repeated deaths; suicide played for comedy", "self-harm", series="Happy Death Day", part=1)
F("Freaky", "Christopher Landon", 2020, 102, "comedy horror", "f", 2, 3, 5, "F", 2, 1, 4, 1,
  "A shy teenager swaps bodies with the local serial killer the night before homecoming, and has twenty-four hours to swap back.",
  "It is a body-swap comedy with gory kills; there is no real dread.",
  ["Happy Death Day", "Jennifer's Body"], "gory kills")
F("The Haunting", "Robert Wise", 1963, 112, "horror", "f", 3, 5, 3, "S", 3, 4, 0, 0,
  "An anthropologist invites a lonely, fragile woman to Hill House to help him prove it is haunted, and the house chooses her.",
  "Nothing is ever shown; the terror is sound and suggestion, and the narration is heavy.",
  ["The Innocents", "The Others"], "psychological distress; suicide", "self-harm")
F("The Innocents", "Jack Clayton", 1961, 100, "horror drama", "f", 4, 5, 3, "S", 4, 4, 0, 0,
  "A governess takes charge of two orphaned children at a vast country estate and begins to believe the previous staff, both dead, have not let them go.",
  "It is black and white, restrained and ambiguous by design; you have to decide what is really happening.",
  ["The Haunting", "The Others"], "implied abuse of children; death of a child", "child-harm")
F("The Wicker Man", "Robin Hardy", 1973, 88, "horror mystery", "m", 4, 4, 4, "T", 4, 3, 1, 3,
  "A devout police sergeant flies to a remote Scottish island to find a missing girl, and the islanders tell him she never existed.",
  "It is partly a musical, and the folk songs and pagan comedy can seem silly until the final ten minutes.",
  ["Midsommar", "The Witch"], "human sacrifice; nudity; animal imagery")
F("Don't Look Now", "Nicolas Roeg", 1973, 110, "thriller horror drama", "e", 5, 5, 2, "S", 4, 3, 2, 4,
  "Grieving their drowned daughter, a couple go to Venice in winter, where a blind psychic tells the wife the girl is happy and her husband is in danger.",
  "It is elliptical, cut in fragments, and devastatingly sad; it is not built for thrills.",
  ["The Orphanage", "Vertigo"], "death of a child; explicit sex scene", "child-harm")
F("Event Horizon", "Paul W. S. Anderson", 1997, 96, "scifi horror", "e", 2, 3, 4, "F", 4, 4, 5, 0,
  "A rescue crew is sent to Neptune to recover an experimental ship that vanished seven years ago and has just come back from somewhere.",
  "The script is clunky and the gore is extreme in brief flashes; it is hellish rather than smart.",
  ["Alien", "Annihilation"], "graphic gore; self-mutilation; suicide", "self-harm")
F("Pet Sematary", "Mary Lambert", 1989, 103, "horror", "e", 4, 3, 3, "T", 5, 4, 3, 0,
  "A doctor moves his family to rural Maine, next to a road with fast trucks and a burial ground the locals say brings things back.",
  "It is mean and sad in equal measure, the acting is uneven, and the death of a toddler is central.",
  ["The Mist", "Hereditary"], "death of a child; a cat is killed; terminal illness", "child-harm animal-harm")
F("Trick 'r Treat", "Michael Dougherty", 2007, 82, "horror comedy", "e", 2, 4, 5, "F", 3, 3, 3, 1,
  "Four interlocking Halloween stories in one small Ohio town, all watched by a little trick-or-treater in a burlap mask who enforces the rules.",
  "It is an anthology, so some stories land harder than others, and a few children do not survive.",
  ["The Fog", "Halloween"], "children killed; gore", "child-harm")
F("The Love Witch", "Anna Biller", 2016, 120, "horror comedy romance", "f", 2, 4, 4, "S", 2, 1, 2, 4,
  "A beautiful modern-day witch moves to a small California town and uses love magic to find a man, with fatal results for the men.",
  "It is a deadpan pastiche of 1960s Technicolor melodrama; if the stilted style does not charm you, two hours is long.",
  ["Suspiria", "Practical Magic"], "nudity; sexual content; poisoning")
F("The Host", "Bong Joon-ho", 2006, 120, "scifi horror comedy", "e", 4, 5, 5, "F", 3, 2, 2, 0,
  "A creature mutated by chemicals dumped in the Han River snatches a snack vendor's daughter, and her ramshackle family goes after her.",
  "It flips between slapstick, satire and tragedy without warning; the tone is the point and also the hurdle.",
  ["Train to Busan", "Parasite"], "child in peril; creature attacks", "child-harm")
F("Friday the 13th", "Sean S. Cunningham", 1980, 95, "horror", "e", 1, 2, 4, "T", 2, 3, 4, 2,
  "Camp counsellors reopen Camp Crystal Lake, which closed after a boy drowned there decades ago, and start dying one by one.",
  "The characters are thin and the acting thinner; it is a kill-count movie with a great final reveal.",
  ["Halloween", "Black Christmas"], "graphic kills; nudity", series="Friday the 13th", part=1)
F("The Craft", "Andrew Fleming", 1996, 101, "horror fantasy drama", "f", 3, 3, 5, "T", 3, 2, 2, 1,
  "A new girl at a Los Angeles Catholic school falls in with three outcasts who practise witchcraft, and their spells start working too well.",
  "It is a 1996 teen movie through and through, and the last act tips into melodrama.",
  ["Jennifer's Body", "Practical Magic"], "attempted sexual assault; self-harm scars; suicide attempt; snakes", "sexual-assault self-harm")
F("Sleepy Hollow", "Tim Burton", 1999, 105, "horror mystery fantasy", "m", 2, 4, 4, "T", 3, 2, 4, 1,
  "In 1799 a squeamish New York constable is sent upstate to investigate a string of beheadings blamed on a headless horseman.",
  "It is gorgeous and goofy; the mystery is thin and Depp plays Ichabod as a nervous comedian.",
  ["Crimson Peak", "Bram Stoker's Dracula"], "decapitations; a child is killed", "child-harm")

# ------------------------------------------------------------------ everything else
F("Gone Girl", "David Fincher", 2014, 149, "thriller mystery drama", "f", 4, 5, 4, "T", 4, 1, 3, 3,
  "On their fifth wedding anniversary Nick Dunne's wife disappears, and the more the town learns about their marriage, the worse he looks.",
  "Its view of marriage is acid and nobody is likable; one burst of violence is shockingly graphic.",
  ["The Talented Mr. Ripley", "Promising Young Woman"], "graphic murder; false accusation of rape; domestic violence")
F("Se7en", "David Fincher", 1995, 127, "thriller crime mystery", "m", 5, 5, 4, "T", 5, 3, 3, 0,
  "A detective a week from retirement and his hot-headed replacement hunt a killer staging each murder as one of the seven deadly sins.",
  "It is relentlessly grim, the crime scenes are grotesque, and the ending is famous for a reason.",
  ["The Silence of the Lambs", "Zodiac"], "graphic crime scenes; implied sexual violence; torture", "sexual-assault")
F("Zodiac", "David Fincher", 2007, 157, "crime mystery thriller", "m", 3, 5, 3, "S", 3, 2, 2, 0,
  "A cartoonist, a reporter and two detectives spend decades obsessed with the Zodiac killer in San Francisco.",
  "It is over two and a half hours of procedure and it does not solve the case; obsession is the subject.",
  ["Se7en", "Prisoners"], "realistic murders")
F("Prisoners", "Denis Villeneuve", 2013, 153, "thriller crime mystery", "m", 5, 5, 3, "S", 5, 2, 2, 0,
  "When his young daughter and her friend vanish on Thanksgiving, a father takes the investigation into his own hands.",
  "It is long, cold and morally queasy, with a torture subplot at its centre.",
  ["Zodiac", "Weapons"], "child abduction; torture", "child-harm")
F("Parasite", "Bong Joon-ho", 2019, 132, "thriller comedy drama", "e", 5, 5, 5, "T", 4, 1, 2, 1,
  "A poor family in a semi-basement scheme their way, one by one, into jobs with a wealthy family in their architect-designed house.",
  "It turns sharply in the second half, and the ending is violent and bitter.",
  ["The Host", "Knives Out"], "sudden violence")
F("Knives Out", "Rian Johnson", 2019, 130, "mystery comedy crime", "e", 3, 5, 5, "T", 1, 0, 1, 0,
  "When a wealthy crime novelist is found dead after his eighty-fifth birthday, a Southern gentleman detective interviews his grasping family.",
  "It is a puzzle and a comedy; if you dislike whodunits that show their hand early, the structure may annoy you.",
  ["Clue", "Glass Onion"], "suicide; mild violence", "self-harm", series="Benoit Blanc", part=1)
F("Glass Onion", "Rian Johnson", 2022, 139, "mystery comedy", "e", 2, 4, 5, "F", 1, 0, 1, 1,
  "A tech billionaire invites his old friends to his private Greek island for a murder-mystery weekend, and Benoit Blanc turns up uninvited.",
  "It is broader and longer than the first, and the satire is about as subtle as its villain.",
  ["Knives Out", "Bodies Bodies Bodies"], "mild violence", series="Benoit Blanc", part=2)
F("The Talented Mr. Ripley", "Anthony Minghella", 1999, 139, "thriller drama crime", "m", 4, 5, 4, "S", 4, 1, 2, 2,
  "In 1958 a young man is paid to bring a rich heir home from Italy, and falls in love with the life, and the heir.",
  "Tom's choices are hard to watch and the ending leaves him exactly where you fear.",
  ["Saltburn", "Gone Girl"], "murder; violence")
F("Rear Window", "Alfred Hitchcock", 1954, 112, "thriller mystery", "m", 3, 5, 4, "S", 2, 2, 0, 2,
  "Laid up with a broken leg, a photographer starts watching his neighbours across the courtyard and becomes sure one of them has killed his wife.",
  "It is one room and a lot of talk for the first hour; the tension is all slow pressure.",
  ["Vertigo", "Psycho"], "implied murder")
F("Vertigo", "Alfred Hitchcock", 1958, 128, "mystery thriller romance", "m", 4, 5, 3, "S", 3, 1, 0, 1,
  "A retired detective with a fear of heights is hired to follow an old friend's wife, who seems to be possessed by a dead woman.",
  "It is slow, strange and obsessive, and Scottie's behaviour towards Judy is deeply uncomfortable.",
  ["Rear Window", "Don't Look Now"], "suicide; obsession; emotional abuse", "self-harm")
F("Promising Young Woman", "Emerald Fennell", 2020, 113, "thriller drama comedy", "f", 5, 4, 4, "T", 4, 1, 1, 2,
  "By night, Cassie pretends to be blackout drunk in bars to see which nice guys take her home, and her revenge on the past is only beginning.",
  "It is sugar-coloured but bitter, and its ending is deliberately upsetting.",
  ["Gone Girl", "Saltburn"], "sexual assault (discussed and depicted); suicide; violence", "sexual-assault self-harm")
F("Black Swan", "Darren Aronofsky", 2010, 108, "thriller drama horror", "f", 5, 5, 3, "T", 5, 3, 3, 3,
  "A perfectionist ballerina is cast as the Swan Queen and, chasing the darker Black Swan, starts to crack.",
  "It is claustrophobic and paranoid; the self-harm and body horror are close and frequent.",
  ["Perfect Blue", "Saint Maud"], "self-harm; eating disorder; sexual content; body horror", "self-harm")
F("Saltburn", "Emerald Fennell", 2023, 131, "thriller comedy drama", "m", 3, 4, 4, "T", 4, 1, 2, 4,
  "A scholarship student at Oxford is invited to spend the summer at his glamorous friend's family estate.",
  "It is designed to provoke, several scenes exist mainly to shock, and the final reveal explains everything twice.",
  ["The Talented Mr. Ripley", "Promising Young Woman"], "explicit sexual content; suicide; death", "self-harm")
F("Nightcrawler", "Dan Gilroy", 2014, 117, "thriller crime", "m", 3, 5, 4, "T", 4, 1, 2, 1,
  "A driven loner discovers the business of filming crime scenes for local TV news in Los Angeles, and is very good at it.",
  "Lou is repellent from the first scene and the film never asks you to like him.",
  ["Taxi Driver", "Gone Girl"], "graphic accident and crime scenes; sexual coercion", "sexual-assault")
F("Oldboy", "Park Chan-wook", 2003, 120, "thriller mystery action", "m", 5, 5, 4, "T", 5, 2, 4, 2,
  "A man is kidnapped and kept in a hotel room for fifteen years without explanation, then released, with five days to find out why.",
  "Its final revelation is one of cinema's most disturbing, and there is real cruelty to animals on screen.",
  ["The Handmaiden", "Audition"], "incest; torture; suicide; a live octopus is eaten", "sexual-assault self-harm animal-harm")
F("The Handmaiden", "Park Chan-wook", 2016, 145, "thriller romance drama", "f", 4, 5, 5, "T", 3, 1, 2, 5,
  "In 1930s Korea a pickpocket is placed as maid to a Japanese heiress to help a con man seduce her, and falls for her instead.",
  "It is long, told three times from different angles, and very sexually explicit.",
  ["Portrait of a Lady on Fire", "The Talented Mr. Ripley"], "explicit sex; sexual abuse of a child (implied); torture", "sexual-assault")
F("Memento", "Christopher Nolan", 2000, 113, "mystery thriller", "m", 4, 5, 4, "T", 3, 1, 2, 1,
  "A man who cannot form new memories hunts his wife's killer using tattoos, Polaroids and notes, told backwards.",
  "The structure demands attention; tune out for five minutes and it is hard to catch up.",
  ["Shutter Island", "Oldboy"], "violence; sexual assault referenced")
F("Shutter Island", "Martin Scorsese", 2010, 138, "mystery thriller", "m", 5, 4, 4, "T", 4, 3, 2, 0,
  "In 1954 two US marshals arrive at a hospital for the criminally insane on an island off Boston to find a patient who has vanished from a locked cell.",
  "If you see the twist coming, the long middle drags, and its subject matter is very heavy.",
  ["Memento", "The Others"], "drowned children; war atrocities; mental illness", "child-harm")
F("Fargo", "Joel Coen", 1996, 98, "crime comedy thriller", "e", 3, 5, 5, "T", 3, 1, 3, 1,
  "A desperate Minneapolis car salesman hires two criminals to kidnap his wife, and a very pregnant, very polite police chief starts to unpick it.",
  "The violence arrives in sudden ugly bursts amid the deadpan; the tone takes a moment to tune into.",
  ["No Country for Old Men", "Knives Out"], "kidnapping; violent murders")
F("No Country for Old Men", "Joel and Ethan Coen", 2007, 122, "crime thriller", "m", 4, 5, 4, "S", 5, 3, 3, 0,
  "A hunter finds two million dollars at a drug deal gone wrong in West Texas, and a killer with a captive bolt pistol follows him.",
  "It denies you the ending a thriller promises, on purpose.",
  ["Fargo", "Prisoners"], "violent killings; a dog is shot", "animal-harm")
F("Pulp Fiction", "Quentin Tarantino", 1994, 154, "crime comedy", "e", 3, 5, 5, "T", 3, 1, 3, 1,
  "Two hitmen, a boxer, a gangster's wife and a pair of diner robbers cross paths in Los Angeles, out of order.",
  "It is long and talky, the timeline jumps, and it includes a male rape scene.",
  ["Kill Bill: Vol. 1", "Fargo"], "sexual assault; overdose; violence; racial slurs", "sexual-assault")
F("Kill Bill: Vol. 1", "Quentin Tarantino", 2003, 111, "action crime", "f", 3, 5, 5, "F", 3, 1, 5, 0,
  "A bride shot at her own wedding wakes from a four-year coma and starts crossing names off a list.",
  "It is half a story; the revenge is spectacular and the motive is mostly saved for part two.",
  ["John Wick", "Lady Snowblood"], "extreme stylised gore; sexual assault of a comatose woman", "sexual-assault",
  series="Kill Bill", part=1)
F("Kill Bill: Vol. 2", "Quentin Tarantino", 2004, 137, "action crime drama", "f", 4, 5, 4, "T", 3, 1, 3, 0,
  "The Bride finishes the list, and finally meets Bill.",
  "It is slower and talkier than the first, and its climax is a conversation.",
  ["Kill Bill: Vol. 1", "Mad Max: Fury Road"], "violence; being buried alive",
  series="Kill Bill", part=2, needs="Kill Bill: Vol. 1")
F("Mad Max: Fury Road", "George Miller", 2015, 120, "action scifi", "e", 4, 5, 5, "R", 3, 1, 3, 0,
  "In the wasteland, Imperator Furiosa drives a war rig full of the warlord's escaped wives across the desert, and a captured drifter is chained to the front of the pursuit.",
  "It is essentially one two-hour chase; if you need dialogue and plot, there is very little.",
  ["Aliens", "Kill Bill: Vol. 1"], "violence; implied sexual slavery", "sexual-assault",
  leadNote="Furiosa drives the story; Max mostly rides along")
F("John Wick", "Chad Stahelski", 2014, 101, "action crime", "m", 3, 4, 5, "R", 2, 0, 4, 0,
  "A retired hitman is mourning his wife when the son of a Russian mobster steals his car and kills the puppy she left him.",
  "The puppy is killed on screen early; and the story is a thin wire for the fights.",
  ["Kill Bill: Vol. 1", "The Matrix"], "a puppy is killed; gun violence", "animal-harm", series="John Wick", part=1)
F("The Matrix", "The Wachowskis", 1999, 136, "scifi action", "m", 4, 5, 5, "F", 2, 1, 2, 1,
  "A hacker called Neo is contacted by a woman called Trinity, and told the world he lives in is a simulation.",
  "Its look has been copied so often it may feel familiar, and the exposition in the middle is heavy.",
  ["Blade Runner", "Edge of Tomorrow"], "gun violence", series="The Matrix", part=1)
F("Blade Runner", "Ridley Scott", 1982, 117, "scifi thriller", "m", 4, 5, 3, "S", 4, 1, 2, 2,
  "In rainy 2019 Los Angeles a burned-out cop is ordered to hunt four replicants who have come back to Earth looking for their maker.",
  "It is slow, moody and more interested in atmosphere than action; one 'romance' scene is coercive.",
  ["Ex Machina", "Arrival"], "violence; a coercive sexual scene", "sexual-assault")
F("Arrival", "Denis Villeneuve", 2016, 116, "scifi drama", "f", 5, 5, 3, "S", 2, 1, 0, 0,
  "When twelve alien ships appear over the Earth, a linguist is recruited to work out what the visitors are trying to say.",
  "It is a quiet film about language and grief; the aliens never become a threat to fight.",
  ["Annihilation", "Interstellar"], "death of a child from illness", "child-harm")
F("Ex Machina", "Alex Garland", 2014, 108, "scifi thriller", "m", 4, 5, 4, "S", 4, 2, 2, 2,
  "A programmer wins a week at his reclusive boss's mountain estate and is asked to judge whether a robot named Ava is truly conscious.",
  "It is three people in a glass house talking; the tension is cerebral until the last ten minutes.",
  ["Blade Runner", "Annihilation"], "nudity; self-harm; violence", "self-harm")
F("Everything Everywhere All at Once", "Daniel Kwan and Daniel Scheinert", 2022, 139, "scifi comedy action drama", "f", 5, 5, 5, "F", 2, 0, 2, 1,
  "A laundromat owner being audited by the IRS learns she must connect with infinite versions of herself to save the multiverse.",
  "It is maximalist and chaotic, with hot-dog fingers and butt plugs; if absurdity tires you, it is a long two hours.",
  ["Spider-Man: Into the Spider-Verse", "The Matrix"], "comic violence; crude humour; suicidal despair", "self-harm")
F("Interstellar", "Christopher Nolan", 2014, 169, "scifi drama adventure", "m", 5, 5, 4, "T", 2, 1, 0, 0,
  "On a dying Earth, a former pilot leaves his children to fly through a wormhole looking for a new home for humanity.",
  "It is nearly three hours, the science talk is dense, and the sound mix buries some dialogue.",
  ["Arrival", "Dune"], "peril; grief")
F("Dune", "Denis Villeneuve", 2021, 155, "scifi adventure", "m", 4, 5, 4, "S", 3, 1, 2, 0,
  "The heir of House Atreides goes with his family to rule the desert planet Arrakis, the only source of the most valuable substance in the universe.",
  "It is the first half of the story and ends mid-stride; much of it is setup and staring at sand.",
  ["Blade Runner", "The Lord of the Rings: The Fellowship of the Ring"], "violence", series="Dune", part=1)
F("Dune: Part Two", "Denis Villeneuve", 2024, 166, "scifi adventure action", "m", 4, 5, 5, "T", 4, 1, 3, 1,
  "Paul joins the Fremen of the deep desert and rides the line between revenge and the holy war he has foreseen.",
  "It is long and heavy with prophecy, and its hero's arc is deliberately troubling.",
  ["Dune", "Mad Max: Fury Road"], "violence; genocide", series="Dune", part=2, needs="Dune")
F("Edge of Tomorrow", "Doug Liman", 2014, 113, "scifi action", "m", 3, 4, 5, "F", 2, 1, 2, 0,
  "A cowardly PR officer is thrown into a beach invasion against aliens, dies, and wakes up the morning before, again.",
  "It is a crowd-pleaser with a weaker final act than its middle.",
  ["Happy Death Day", "Aliens"], "repeated deaths; war violence",
  leadNote="Emily Blunt's Rita is the war hero he has to become")
F("The Princess Bride", "Rob Reiner", 1987, 98, "fantasy adventure comedy romance", "e", 3, 4, 5, "F", 1, 1, 1, 1,
  "A grandfather reads his grandson the story of Buttercup and Westley: true love, a giant, a swordsman with a grudge, and Rodents of Unusual Size.",
  "It is gentle and knowing; if you want swashbuckling played straight, the jokes win.",
  ["Stardust", "Labyrinth"], "mild violence; torture played for comedy")
F("Stardust", "Matthew Vaughn", 2007, 127, "fantasy romance adventure comedy", "m", 3, 4, 5, "F", 2, 1, 2, 2,
  "A young man crosses the wall out of his English village to bring back a fallen star for the girl he loves, and the star is a woman.",
  "It is busy, with three plots chasing each other, and some of the humour is broad.",
  ["The Princess Bride", "Howl's Moving Castle"], "fantasy violence; animal sacrifice", "animal-harm")
F("The Lord of the Rings: The Fellowship of the Ring", "Peter Jackson", 2001, 178, "fantasy adventure", "e", 5, 5, 5, "T", 3, 2, 2, 0,
  "A hobbit inherits a ring that would let its maker rule the world, and sets out to destroy it with eight companions.",
  "It is three hours and the start of a nine-hour story; the Shire opening is slow.",
  ["The Lord of the Rings: The Two Towers", "Dune"], "battle violence; frightening creatures",
  series="The Lord of the Rings", part=1)
F("The Lord of the Rings: The Two Towers", "Peter Jackson", 2002, 179, "fantasy adventure action", "e", 4, 5, 5, "T", 4, 2, 2, 0,
  "The fellowship is broken: two hobbits head for Mordor with Gollum, and the rest are drawn into the war at Helm's Deep.",
  "It is a middle chapter with no beginning or end of its own.",
  ["The Lord of the Rings: The Fellowship of the Ring", "Dune: Part Two"], "battle violence",
  series="The Lord of the Rings", part=2, needs="The Lord of the Rings: The Fellowship of the Ring")
F("The Lord of the Rings: The Return of the King", "Peter Jackson", 2003, 201, "fantasy adventure action", "e", 5, 5, 5, "T", 4, 2, 2, 0,
  "Frodo and Sam reach Mount Doom as the armies of the West march on the Black Gate to buy them time.",
  "It ends several times; the epilogue alone is longer than some short films.",
  ["The Lord of the Rings: The Two Towers", "Interstellar"], "battle violence; giant spider",
  series="The Lord of the Rings", part=3, needs="The Lord of the Rings: The Two Towers")
F("Spirited Away", "Hayao Miyazaki", 2001, 125, "animation fantasy adventure", "f", 5, 5, 5, "T", 2, 2, 0, 0,
  "A sulky ten-year-old moving house wanders into a spirit world, where her parents are turned into pigs and she has to work in a bathhouse for the gods.",
  "It runs on dream logic; if you need the rules explained, Miyazaki does not.",
  ["Howl's Moving Castle", "Coraline"], "mild peril; creepy spirits")
F("Princess Mononoke", "Hayao Miyazaki", 1997, 134, "animation fantasy action", "m", 5, 5, 4, "T", 3, 1, 3, 0,
  "A cursed young prince travels west and finds himself between an ironworks town and the forest gods, and the wolf girl, at war with it.",
  "It is far more violent than most Ghibli, with severed limbs, and its sympathies are complicated.",
  ["Spirited Away", "Pan's Labyrinth"], "decapitation and dismemberment; animals killed", "animal-harm")
F("Howl's Moving Castle", "Hayao Miyazaki", 2004, 119, "animation fantasy romance", "f", 4, 5, 5, "T", 2, 1, 0, 1,
  "A young hatmaker cursed into the body of an old woman takes refuge as the cleaner in a wandering castle owned by a vain wizard.",
  "The plot dissolves in the second half and the war story is never quite explained.",
  ["Spirited Away", "Stardust"], "war imagery; mild peril")
F("Spider-Man: Into the Spider-Verse", "Bob Persichetti, Peter Ramsey and Rodney Rothman", 2018, 117, "animation action comedy", "m", 5, 5, 5, "F", 2, 0, 0, 0,
  "Brooklyn teenager Miles Morales gets bitten by a radioactive spider the same week a collider brings Spider-People from other dimensions into his.",
  "It is visually dense to the point of overload, and it is a superhero origin at heart.",
  ["Everything Everywhere All at Once", "Puss in Boots: The Last Wish"], "death of family members", series="Spider-Verse", part=1)
F("The Nightmare Before Christmas", "Henry Selick", 1993, 76, "animation fantasy musical", "m", 3, 5, 5, "F", 2, 1, 0, 0,
  "Jack Skellington, Pumpkin King of Halloween Town, is tired of scaring and decides to take over Christmas.",
  "It is short and a musical; if songs are not for you, a third of it will not be either.",
  ["Coraline", "Beetlejuice"], "mild peril; spooky imagery")
F("Labyrinth", "Jim Henson", 1986, 101, "fantasy adventure musical", "f", 3, 4, 5, "T", 2, 1, 0, 1,
  "A teenager wishes the goblins would take her baby brother, and the Goblin King obliges, giving her thirteen hours to solve his labyrinth.",
  "It is puppets and Bowie songs; the plot is a string of encounters.",
  ["The Princess Bride", "Spirited Away"], "child abducted (fantasy); mild peril")
F("The Shape of Water", "Guillermo del Toro", 2017, 123, "fantasy romance drama", "f", 4, 5, 4, "T", 3, 1, 3, 4,
  "In 1962 a mute cleaner at a government lab falls in love with the amphibian man held captive there.",
  "It is a fairy tale that commits fully to the romance, which some find sweet and others absurd.",
  ["Pan's Labyrinth", "Crimson Peak"], "graphic violence; a cat is killed; sexual content", "animal-harm")
F("Practical Magic", "Griffin Dunne", 1998, 104, "fantasy romance comedy", "f", 3, 3, 5, "T", 2, 2, 1, 2,
  "Two witch sisters raised by their aunts, under a curse that kills the men they love, have to hide a body that will not stay dead.",
  "It cannot decide whether it is a romcom or a horror film and the tonal shifts are sharp.",
  ["The Craft", "Hocus Pocus"], "domestic abuse; possession; death")
F("Hocus Pocus", "Kenny Ortega", 1993, 96, "comedy fantasy", "e", 2, 3, 5, "F", 1, 1, 0, 0,
  "On Halloween in Salem a teenager lights a candle that brings back three seventeenth-century witch sisters who need children to stay young.",
  "It is a family comedy; adults will enjoy the Sanderson sisters and little else.",
  ["Practical Magic", "Beetlejuice"], "children in peril; mild peril")
F("Edward Scissorhands", "Tim Burton", 1990, 105, "fantasy romance drama", "m", 4, 4, 4, "T", 2, 1, 1, 1,
  "An Avon lady finds a gentle artificial man with scissors for hands alone in a castle and brings him home to her pastel suburb.",
  "It is a simple fable and the townsfolk are cartoon villains.",
  ["The Shape of Water", "Beetlejuice"], "mild violence; attempted seduction")
F("Pride & Prejudice", "Joe Wright", 2005, 129, "romance drama", "f", 4, 5, 5, "T", 1, 0, 0, 1,
  "The second of five unmarried Bennet sisters meets the proud Mr Darcy and decides she cannot stand him.",
  "It is a condensed Austen; purists miss subplots and the second ending.",
  ["Little Women", "Portrait of a Lady on Fire"], "none of note")
F("Portrait of a Lady on Fire", "Céline Sciamma", 2019, 122, "romance drama", "f", 5, 5, 3, "S", 2, 0, 0, 3,
  "In 1770 a painter is hired to paint a reluctant bride's wedding portrait in secret on a Breton island.",
  "It is slow, quiet and subtitled, and its romance builds in glances.",
  ["The Handmaiden", "Past Lives"], "an abortion is depicted; nudity")
F("Before Sunrise", "Richard Linklater", 1995, 101, "romance drama", "e", 4, 5, 4, "S", 1, 0, 0, 2,
  "A young American and a French student meet on a train and spend one night walking around Vienna before he flies home.",
  "Nothing happens but talk; if you need plot, it is ninety minutes of conversation.",
  ["Past Lives", "When Harry Met Sally..."], "none of note", series="Before", part=1)
F("When Harry Met Sally...", "Rob Reiner", 1989, 96, "romance comedy", "e", 3, 5, 5, "T", 1, 0, 0, 2,
  "Over twelve years in New York, two people who agreed men and women cannot be friends keep running into each other.",
  "It is very 1989, and its central question has dated as much as its knitwear.",
  ["Before Sunrise", "Crazy Rich Asians"], "sexual humour")
F("Crazy Rich Asians", "Jon M. Chu", 2018, 120, "romance comedy", "f", 3, 4, 5, "F", 1, 0, 0, 2,
  "An economics professor goes to Singapore for her boyfriend's best friend's wedding and discovers his family is extraordinarily rich and his mother disapproves.",
  "It is a classic romcom template; the surprises are in the setting and the cast, not the story.",
  ["When Harry Met Sally...", "Pride & Prejudice"], "none of note")
F("Titanic", "James Cameron", 1997, 194, "romance drama", "f", 5, 5, 4, "T", 3, 1, 1, 3,
  "A seventeen-year-old engaged to a cruel millionaire falls for a penniless artist aboard the Titanic's maiden voyage.",
  "It is over three hours and the dialogue is broad; the sinking is the last hour and a half.",
  ["Pride & Prejudice", "Interstellar"], "a suicide attempt; mass drowning; nudity", "self-harm")
F("Phantom Thread", "Paul Thomas Anderson", 2017, 130, "romance drama", "e", 3, 5, 3, "S", 3, 0, 0, 2,
  "A fastidious 1950s London dressmaker takes a young waitress as his muse and lover, and she does not intend to be discarded like the others.",
  "It is mannered and quiet and its romance is decidedly odd.",
  ["Rebecca", "Portrait of a Lady on Fire"], "poisoning")
F("Clueless", "Amy Heckerling", 1995, 97, "comedy romance", "f", 2, 4, 5, "F", 1, 0, 0, 1,
  "A rich, well-meaning Beverly Hills teenager makes over the new girl at school and plays matchmaker for everyone except herself.",
  "It is light as air and very 1995; there is no more to it than charm.",
  ["Mean Girls", "Heathers"], "teen drinking")
F("Mean Girls", "Mark Waters", 2004, 97, "comedy", "f", 2, 4, 5, "F", 1, 0, 0, 1,
  "Homeschooled in Africa until now, Cady starts at an Illinois high school and infiltrates its most powerful clique.",
  "It is a teen comedy with a tidy moral; it is sharper than most and still very much of 2004.",
  ["Clueless", "Heathers"], "teen sexual humour")
F("Bridesmaids", "Paul Feig", 2011, 125, "comedy", "f", 3, 4, 5, "T", 1, 0, 0, 3,
  "A broke baker in Milwaukee is made maid of honour for her best friend's wedding and competes with the bride's perfect new friend.",
  "It runs long for a comedy and the gross-out scenes are very gross.",
  ["Mean Girls", "Crazy Rich Asians"], "sexual content; crude humour")
F("The Grand Budapest Hotel", "Wes Anderson", 2014, 99, "comedy adventure crime", "m", 3, 5, 5, "F", 2, 0, 2, 1,
  "Between the wars, the concierge of a grand Alpine hotel and his lobby boy are drawn into the theft of a priceless painting and a murder.",
  "If Wes Anderson's symmetry and deadpan do not charm you, this is the most Wes Anderson of all.",
  ["Knives Out", "Fargo"], "a cat is thrown from a window; fingers severed", "animal-harm")
F("Hot Fuzz", "Edgar Wright", 2007, 121, "comedy action mystery", "m", 2, 5, 5, "F", 2, 1, 4, 0,
  "London's best police officer is transferred to a perfect English village where accidents keep happening.",
  "Several deaths are surprisingly gory for a comedy, and it is long for one.",
  ["Shaun of the Dead", "Knives Out"], "graphic gory deaths")
F("Death Becomes Her", "Robert Zemeckis", 1992, 104, "comedy fantasy", "f", 2, 4, 5, "F", 2, 1, 2, 2,
  "Two rivals for the same man both drink a potion of eternal youth, and then try to kill each other.",
  "It is a broad cartoon and the ending is cold; nobody here is likable.",
  ["The Substance", "Beetlejuice"], "comic violence; suicide jokes", "self-harm")
F("Heathers", "Michael Lehmann", 1988, 103, "comedy crime", "f", 3, 4, 5, "T", 4, 1, 1, 2,
  "Veronica is tired of her clique of three girls called Heather, and the new boy at school has a way of making problems disappear.",
  "Its black comedy is about teen suicide and murder, and the jokes are very dark.",
  ["Mean Girls", "Jennifer's Body"], "staged suicides; murder; sexual assault (attempted)", "self-harm sexual-assault")
F("The Godfather", "Francis Ford Coppola", 1972, 175, "crime drama", "m", 5, 5, 4, "S", 4, 1, 3, 1,
  "The aging head of a New York crime family survives an assassination attempt, and his youngest son, the one who wanted out, steps in.",
  "It is nearly three hours and deliberately paced, and it shows its women very little interest.",
  ["Goodfellas", "No Country for Old Men"], "violence; a horse is killed; domestic violence", "animal-harm")
F("Whiplash", "Damien Chazelle", 2014, 106, "drama", "m", 5, 5, 4, "F", 3, 1, 1, 0,
  "A first-year jazz drummer at a cutthroat music conservatory is picked for the band run by a brilliant, abusive conductor.",
  "It is intense and the abuse is unrelenting; there is no warmth to hide in.",
  ["Black Swan", "Nightcrawler"], "verbal and physical abuse; suicide discussed", "self-harm")
F("Little Women", "Greta Gerwig", 2019, 135, "drama romance", "f", 5, 5, 4, "T", 1, 0, 0, 1,
  "Jo March, a struggling writer in New York, remembers growing up with her three sisters in Concord during the Civil War.",
  "It jumps between two timelines, which can be confusing until the colour grading clicks.",
  ["Pride & Prejudice", "Lady Bird"], "death of a sister from illness")
F("Lady Bird", "Greta Gerwig", 2017, 94, "comedy drama", "f", 4, 5, 4, "T", 1, 0, 0, 2,
  "A Sacramento high-school senior who calls herself Lady Bird battles her mother through her final year before college.",
  "It is small and episodic; nothing dramatic happens.",
  ["Little Women", "Mean Girls"], "teen sex; family conflict")
F("Past Lives", "Celine Song", 2023, 105, "romance drama", "f", 5, 5, 3, "S", 1, 0, 0, 1,
  "Two childhood friends separated when one emigrates from Seoul reconnect online twelve years later, and again in New York twelve years after that.",
  "It is quiet and restrained to the point of stillness; the drama is all unsaid.",
  ["Before Sunrise", "Portrait of a Lady on Fire"], "none of note")
F("Murder on the Orient Express", "Sidney Lumet", 1974, 128, "mystery crime", "e", 3, 4, 4, "S", 2, 1, 1, 0,
  "When an American passenger is stabbed in his compartment on the snowbound Orient Express, Hercule Poirot interviews everyone aboard.",
  "It is a stately, talky whodunit; the interviews take the whole middle.",
  ["Knives Out", "Clue"], "murder; a child's kidnapping in the backstory", "child-harm")
F("Clue", "Jonathan Lynn", 1985, 94, "comedy mystery", "e", 1, 4, 5, "F", 1, 0, 1, 0,
  "Six blackmail victims are invited to a remote mansion in 1954 under false names, and their host turns up dead.",
  "It is pure farce; the mystery is a joke delivery system.",
  ["Knives Out", "Bodies Bodies Bodies"], "comic murders")
F("Raiders of the Lost Ark", "Steven Spielberg", 1981, 115, "action adventure", "m", 3, 5, 5, "F", 2, 2, 2, 1,
  "In 1936 archaeologist Indiana Jones races the Nazis to find the Ark of the Covenant.",
  "Indy's past with Marion is uncomfortable by modern standards, and the climax melts faces.",
  ["The Mummy", "Jurassic Park"], "face-melting climax; violence", series="Indiana Jones", part=1)
F("Jurassic Park", "Steven Spielberg", 1993, 127, "scifi adventure thriller", "e", 4, 5, 5, "F", 2, 3, 2, 0,
  "A billionaire invites scientists to preview his island park of cloned dinosaurs, and the power goes out.",
  "The science lecture in the first half is long, and the kids are in serious peril.",
  ["Jaws", "Raiders of the Lost Ark"], "children in peril; dinosaur attacks", series="Jurassic Park", part=1)
F("The Mummy", "Stephen Sommers", 1999, 124, "action adventure fantasy", "e", 2, 3, 5, "F", 2, 2, 2, 2,
  "In 1926 a librarian, her brother and an American legionnaire dig up the city of the dead and wake a cursed priest.",
  "It is cheesy, and its Egyptians are mostly villains or comic relief.",
  ["Raiders of the Lost Ark", "Pirates of the Caribbean: The Curse of the Black Pearl"], "mummification; scarabs; violence",
  series="The Mummy", part=1)
F("Pirates of the Caribbean: The Curse of the Black Pearl", "Gore Verbinski", 2003, 143, "action adventure fantasy", "e", 3, 4, 5, "F", 2, 2, 2, 1,
  "A blacksmith teams up with an eccentric pirate to rescue the governor's daughter from a crew of cursed skeleton pirates.",
  "It is long and Jack Sparrow's act is either the reason to watch or the reason to stop.",
  ["The Mummy", "The Princess Bride"], "skeletal pirates; violence", series="Pirates of the Caribbean", part=1)
F("Coco", "Lee Unkrich", 2017, 105, "animation fantasy", "m", 5, 5, 5, "T", 1, 1, 0, 0,
  "On the Day of the Dead, a boy who dreams of music in a family that has banned it ends up in the Land of the Dead.",
  "It is a family film built to make you cry, and it will.",
  ["Spirited Away", "The Nightmare Before Christmas"], "death and grief")
F("Paprika", "Satoshi Kon", 2006, 90, "animation scifi thriller", "f", 3, 5, 4, "F", 3, 2, 1, 1,
  "A device that lets therapists enter patients' dreams is stolen, and dreams start leaking into the waking world.",
  "It is dense, surreal and hard to follow on a first watch.",
  ["Perfect Blue", "Inception"], "surreal violence; sexual assault (dream)", "sexual-assault")
F("Perfect Blue", "Satoshi Kon", 1997, 81, "animation thriller horror", "f", 4, 5, 3, "T", 5, 4, 3, 2,
  "A pop idol quits her group to become an actress and finds herself stalked by a fan and by an online diary that seems to know her better than she does.",
  "It is an adult film, not a cartoon, with a graphic and upsetting staged rape scene.",
  ["Black Swan", "Paprika"], "stalking; sexual assault depicted; graphic murders", "sexual-assault")
F("Puss in Boots: The Last Wish", "Joel Crawford", 2022, 102, "animation adventure comedy", "m", 4, 5, 5, "F", 2, 1, 0, 0,
  "Down to the last of his nine lives and hunted by a wolf who is Death himself, Puss sets out to find the Wishing Star.",
  "It is a kids' film first, but its fear of death is real.",
  ["Spider-Man: Into the Spider-Verse", "Shrek"], "peril; panic attacks")
