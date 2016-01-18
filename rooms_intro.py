from time import sleep

def start_intro():
	print """
   __   __  __   __  ______    _______  __   __ 
  |  |_|  ||  | |  ||    _ |  |       ||  |_|  |
  |       ||  | |  ||   | ||  |    ___||       |
  |       ||  |_|  ||   |_||_ |   |___ |       |
  |       ||       ||    __  ||    ___| |     | 
  | ||_|| ||       ||   |  | ||   |___ |   _   |
  |_|   |_||_______||___|  |_||_______||__| |__|

	Welcome to the world of SECRETS OF THE MUREX
	Unveil our mystery. Carry our tradition. Answer our call.
	We depend on you.

	"""
	print "Enter BEGIN to approach the island."
	print "Type HELP MENU for further instructions."

def help_menu():
	print '*' * 15
	print "\n Murex is a game of exploration and investigation."
	print "Type \'CHECK NOTEBOOK\' to review what you've learned."
	print "Remember to regularly survey your surroundings."
	print "		Secrets may be anywhere.     "
	print "Type LOOK AROUND to expose the truth. \n"
	print '*' * 15

def ship_awaken():
	print """For days you've dreamed of the sight of land,"""
	sleep(2)
	print """but the tiny island that lies on the horizon does nothing 
to quell the uneasy feeling you've had this entire trip. \n"""
	sleep(4)
	print """Seasickness has kept your mouth sour for the week you've been on the boat,
and this morning is no different. \n"""
	sleep(4)
	print """Some distant spire catches the sun and glints impossibly bright, 
making your headache even worse. \n"""
	sleep(3)
	print """You close your eyes and recoil, stepping back from your vantage point 
and directly into the ship's captain. \n"""
	sleep(2)
	print """He glares down at you. Do you apologize? Or run away?"""

def captain_i():
	print """ The Captain sighs at your apology."""
	sleep(2)
	print """
	I WAS BORN WITH A HARD FACE AND THE WEATHER HAS NOT BEEN KIND TO IT.
	IT IS MY CURSE TO BE FOREVER FRIGHTENING TO STRANGERS, 
	WHEN ALL I MIGHT LIKE IS TO LET THEM KNOW THE WARMTH I HAVE TO OFFER.\n"""
	sleep(3)
	print"""You are rendered speechless by the Captain's confession.
He looks up at the sky as if he's forgotten you're there."""
	sleep(2)
	print"""
	THAT THE SKY CAN BE SO BRIGHT AND CLEAR AND BEAUTIFUL 
	WITH SO MANY TERRIBLE THINGS SWIRLING AROUND BENEATH IT.
	IT'S PAINFUL.
	THAT'S A QUOTE FROM SOMEWHERE. \n"""
	sleep(6)
	print """ He sighs again. Your sympathy for this sad man 
has turned to boredom bordering on disgust, 
and he can sense the shift."""
	sleep(3)
	print """ BE THERE SOON, HOPE YOU KNOW WHAT YOU'RE GETTING INTO, \n
he says before he clomps away, leaving you alone again.
Was that a threat? What are you getting yourself into? \n"""
	sleep(3)
	print """ You thumb the edges of the thick envelope 
the letter from your late great-grandfather came in. \n
You've read it over and over so many times, but still, nothing makes much sense.
Do you read it again? Or watch the sea and wait to dock? """

def captain_ii():
	print """
I HOPE YOU KNOW WHAT YOU'RE GETTING INTO, 
you hear the sad and ugly captain call as you run to the other side of the ship.
You catch your breath here and feel the breeze in your hair. 
It eases the pain of your headache.
\n """
	sleep(3)
	print """
You go back over in your mind the Captain's words, 
and the rest of the laconic crew's attitude during the entirety of the trip.
What are they afraid of you learning? Do they even know?
You thumb the edges of the thick envelope the letter 
from your late great-grandfather came in.
You've read it over and over so many times, but still, nothing makes much sense. \n """
	sleep(4)
	print """Do you read it again? 
Or watch the sea and wait to dock? """

def captain_iii():
	print """ He sighs.
It is unlikely that he has had any recent contact with a young girl like you, 
and appears to read all of your actions as nonsense. \n
BE THERE SOON, HOPE YOU KNOW WHAT YOU'RE GETTING INTO, \n
he says before he clomps away, 
leaving you alone again."""
	sleep(4)
	print """
Was that a threat? What are you getting yourself into?
You thumb the edges of the thick envelope the letter from your late great-grandfather came in.
You've read it over and over so many times, but still, nothing makes much sense.
Do you read it again? Or watch the sea and wait to dock? """

def read_letteri():
	print """ You can't help but open the well worn envelope one more time 
before you dock. \n """
	sleep(2)
	print """Something about it is irresistible."""
	sleep(3)
	print """You slide your finger across the dark blue wax seal, 
stamped with the shape of a strange and spiny, spiral seashell.
Your great-grandfather's handwriting stands out in green ink 
that almost glows against the thick, cream paper. """

def visit_memory():
	print """The man's face is a shadow, 
but you recall your mother in an intense argument with him. \n
	You were very young,
	Sent upstairs, but you disobeyed."""
	sleep(4)
	print """You sat just behind the kitchen door, 
trying to make sense of their yelling.
SHE IS THE ONE I'VE BEEN WAITING FOR! and YOU'RE CRAZY! 
are the only two phrases that have stuck with you.
You remember not being able to sleep that night, 
wondering if you were being held back from some great adventure.
Perhaps that's why you didn't tell your mother when you received the letter,
or when you bought your ticket.
Well, you've made your decision, 
and there's nothing she can do to prevent you now.
ou feel the ship's bow knock against the island's dock.
You've arrived."""
	sleep(2)
	print """No one is here to meet you, but your eyes catch the note nailed to the dock post, 
and see a path leading to the rest of the island ahead."""

def mother_story():
	print """Your mother would only speak about her grandfather Taymor 
	when she was really pushed to do it.
When you did push her to the limit, something changed in her eyes.
She wasn't your mother anymore, 
she was a scared and confused young woman, sharper than the one you knew."""
	sleep(3)
	print """
	HE'S AN EVIL MAN. \n
WHEN I WAS A YOUNG GIRL, HE RAN OFF WITH A STRANGE GROUP OF PEOPLE.
CULTISTS. DARK MESSENGERS.
PREACHING SOME NONSENSE ABOUT THE TRUTH BELOW. \n 
HE ASKED US, OUR WHOLE FAMILY, TO JOIN HIM, AND WHEN WE SAID NO, 
WHEN WE TOLD HIM HE WAS BEING RIDICULOUS,
HE TOOK ME WITH HIM IN THE MIDDLE OF THE NIGHT.
I WAS PACKED IN A WOODEN TRUNK.
THEY WHISPERED TO ME. HORRIBLE THINGS THAT WERE MEANT TO BE REASSURING.
THEY SOUNDED HOPEFUL WHEN THEY TALKED ABOUT THE FLOODING OF THE WORLD.
REBORN IN ITS LIGHT THEY SAID OVER AND OVER AGAIN.
THEIR LAUGHTER AND THE SMELL. GOD, THE SMELL.
SOUR. SEWAGE. PICKLED HELL.
I DON'T KNOW WHERE THEY TOOK ME OR WHAT THEY WERE PLANNING TO DO.
I JUST REMEMBER THE POLICE PRYING OPEN THE TOP OF MY TRUNK, 
AND STEPPING OUT INTO AN EMPTY BASEMENT,
THE WALLS WERE CARVED WITH WAVES. ENDLESS. THOUSANDS OF THEM.

Her eyes went far away then, and they didn't take you with them.

DON'T MENTION HIM AGAIN.
PLEASE.

You feel the ship's bow knock against the island's dock.
You've arrived, and there is nothing more she can tell you now.
"""
#THE LAST TWO LINES NEED TO BE FIXED. 
#THEY SAY THAT THE BOAT HAS ARRIVED, THEN IT SAYS THAT IT HASN'T YET.

def wait_dock():
	print """ You stare at the island as the ship approaches.
Something about the bright glint in the distance won't let you look away. 
You can't quite make out its source, but it is hopelessly mesmerizing.
You can only rip your eyes away when you feel the ship 
bump against the dock with a hard wooden knock.
Before you realize what is happening, 
the crew has shuffled you off the deck, thrown your bag at your feet, and set sail once more.
The letter that sent you here in the first pokes against your ribs from inside your pocket. 
A note is nailed to one of the posts on the dock.
Do you read the note? Or revisit the letter from your great-grandfather? """

def dock_note():
	print """ The paper is damp and slick and the ink is faded.
It peels away from the wooden post and rips easily from the nail.
It can't have been left recently, but it reads:

	YOU ARE LATE.
	PREPARATIONS CAN BE DELAYED FOR YOU NO LONGER.
	MEET ME AT THE ENTRY TO THE GREAT PYRAMID.
	IF YOU CAN MAKE IT THERE THEN THE LEADER WAS CORRECT 
	AND YOU ARE WORTH ALL THIS TROUBLE.

	IMPATIENTLY,
		M. DOBBINS

	"""

def read_letteriii():
	print """ Now that you're actually here, all alone, a small panic hits you.
Thinking that there might be something to glean from one more read, 
you pull your great-grandfather's letter from your pocket.
You slide your finger across the dark blue wax seal, stamped with the shape of a strange and spiny, spiral seashell.
Your great-grandfather's handwriting stands out in green ink that almost glows against the thick, cream paper. """

def dock_fill():
	print """ You were supposed to meet someone here. 
Perhaps there is more information in the note on the dock or something you missed in the letter you came with. """

def dock_arrivei():
	print """ You stare at the island as the ship approaches.
Something about the bright glint in the distance won't let you look away. 
You can't quite make out its source, but it is hopelessly mesmerizing.
You can only rip your eyes away when you feel the ship 
bump against the dock with a hard wooden knock.
Before you realize what is happening, the crew has shuffled you off the deck, 
thrown your bag at your feet, and set sail once more.
The letter that sent you here in the first pokes against your ribs from inside your pocket. 
A note is nailed to one of the posts on the dock.
Do you read the note? Or revisit the letter from your great-grandfather? """

def still_on_dock():
	print """ You look around your new surroundings. The path lies in front of you. 
Do you look back at the note or the letter or do you forge on ahead? """


def path_from_dock():
	print """ You can see the tip of what must be the Great Pyramid 
	far off in the distance, beyond a giant stone wall. 
The path ahead leads away from the dock and splits in three directions.
One straight ahead toward a door in the stone island fortress.
Another forks to the left toward a sparse wood, removed from the stone walls and hugging the rocky shore.
The path to the right drops off and out of sight. There may be cliffs ahead.
The waves crash and the wind whistles at your back. You know you must proceed, but in which direction?"""

def default_from_dock():
	print """ 
This new world is confusing, but you must carry on.
\n 
Is left, right, or straight the way to begin?"""

def door_with_no_knob():
	print """ What appeared to be a door from a distance has no handle.
Carved in to the surface is a single, enormous closed eye, 
perched atop a massive, winding shell, taller than a man, 
with spines longer than your legs stretching out from it at every angle.
Your great-grandfather and the reason you're here wait somewhere behind this wall, 
but there is no obvious way to open it."""

def push_or_pull_door():
	print """ The giant eye springs open, impossibly.
Beneath the stone lid, there is the real shining eye of some living creature.
It glistens like a man's would in this light. 
It reflects back the waves behind you, flipped and magnified.
You are in shock and lost in the world of the eye that is larger than the car you drive to work, 
when you see it narrow into a glare and hear a thin voice enter your mind from no obvious origin.

	SMALL CREATURE. WHY DO YOU COME? """

def default_door():
	print """ That did not seem to work. You remain locked out 
and unenlightened."""

def door_eye_answer():
	print """ LONG AGO, ENTRANCE WAS FOR ALL, BUT HERETICS HAVE CLOSED OUR DOORS.
THE SECRETS INSIDE ARE SAFE BEHIND ME. I WILL OPEN ONLY FOR THE CHOSEN ONES AND THEIR SERVANTS.
ARE YOU MEANT TO ENTER?"""

def door_eye_other():
	print """ IF THIS IS SOME SORT OF JOKE IT IS UNACCEPTABLE.
I WAS AWAKENED BY THE CHOSEN TO GUARD HIS SECRETS, NOT ENTERTAIN HIS VISITORS.
DISTURB ME AGAIN AT YOUR OWN PERIL.

The eye is a slit now, it waits for your next move."""

def door_eye_name():
	print """ I AM YORHAM.
I ASSUME, IF YOU ARE HERE HONORABLY, THAT YOU KNOW MY PURPOSE.
I ASK AGAIN, ARE YOU MEANT TO ENTER? """

def door_eye_attempt_enter():
	print """ IT IS TRUE, YOUR BLOOD SMELLS PURE, 
BUT YOUR INTENTIONS REMAIN A MYSTERY.
THERE IS A FEAR IN YOU THAT HAS YET TO BE SNUFFED BY THE GREAT ONE.
STEEL YOUR HEART BEFORE HE COMES.
RETURN PURE OR DO NOT RETURN AT ALL.
DELIVERANCE LIES BEHIND MY WALLS ALONE. 

With that, the eye snaps shut, 
and you are left alone again with a stone door 
that cannot be opened by human hands.

Paths stretch to the left, off into a forest
and to the right, away from the walls and rocky cliffs."""

def door_eye_not_chosen():
	print """ I DO NOT WASTE TIME WITH THOSE WHO DO NOT WALK OUR PATH.
BE GONE.
FIND THE GLOW AND PROVE YOUR PURITY OR NEVER RETURN.

With that, the eye snaps shut, 
and you are left alone again with a stone door 
that cannot be opened by human hands. 

Paths stretch to the left, off into a forest
and to the right, away from the walls and rocky cliffs."""

def door_waits():
	print """ The door eyes you suspiciously. 
This is a moment for action.
Satisfy the creature or remain unenlightened."""

def door_shut_eye():
	print """ The stone lid does not move. 
It's as if it was never animated. 
If you are to get in this way, you must return with answers."""

def leave_door():
	print """ You step away from the seeing door, 
understanding even less than you did upon arrival.
You are not certain if answers are to be found on the island,
but you do know that you are here to look.
Paths stretch to the left, off into a forest
and to the right, away from the walls and rocky cliffs."""

def wait_after_door():
	print """ The wind whistles and blows. 
Everything has confused you so far, 
and you can feel a sense of hopelessness drawing in on your mind. 
To survive in an unfamiliar world, you must forge on.
	"""
	sleep(3)
	print """ Paths stretch to the left, off into a forest
and to the right, away from the walls and rocky cliffs."""

def hopeless_wait():
	print "This step is missing"

def path_left():
	print """ The sand and rocks near the shore give way almost immediately 
to a firm, well-worn dirt path.
It gets narrower as it winds into a thick, overgrown forest.
It is obvious that, while it has seen much use, 
not much care has been taken with its upkeep recently.
Do you head further into the forest? """


def forest_enter():
	print """ Dense and overgrown, it becomes harder and harder to follow the path.
Something about the thick air and large damp leaves reminds you of something.
Your mind goes back to a favorite film from your childhood, 
a nature tape about South America and its rainforests. 
You cannot remember its title now, but it was narrated by a cheerful, British voice, 
expounding on the countless layers of animal mystery in every centimeter of these 
remote areas of the world."""
	sleep(7)
	print """ He encouraged you, while out in the world, 
to take a moment and listen to all that surrounds you."""
	sleep(5)
	print "You do this now, and your stomach sinks."
	sleep(5)
	print """This is a silent forest."""
	sleep(5)
	print """ You have left behind even the sound of the waves.
It lacks the life of your nature tape, 
of any other place you've ever set foot in this world.
You suddenly become aware of the swift thump of your heart. 
It is the only perceivable sound and it is less than comforting.
To proceed is to descend even further into silence, into dread.
To turn back is to learn nothing.
Indecision is not an option. """

def forest_ruins():
	print """ Moments after it felt as though the path would end in overgrowth, 
it breaks open into a large, man made clearing.
A series of platforms and huts, elevated in the trees and strung together by rope bridges, 
sit above a central fire pit.
These signs of life bring you a moment of joy.
But then you realize, the silence persists.
Across the clearing, the path picks back up.
To your left, a rope ladder leads up to a tree house. """

def tree_house():
	print """ This is not at all what you were expecting from the disarray in the clearing.
This finished interior would be more fitting in an Ivy League library 
than a makeshift building in the South Pacific.
But the formerly beautiful room is in tatters.
Some violence has happened here. \n"""
	sleep(5)
	print"""
Leatherbound books lay ripped apart and scorched on the dark, polished mahogany floor.
A small side table with accompanying chess set lies overturned 
next to a finely upholstered chair.
This place must somehow be related to the compound.
Could this have been Taymor's den? \n"""
	sleep(4)
	print """" Were you too late to respond to his letter?
The room fills you with sadness, but if you're here to learn about your relative, 
this seems like a place to start."""


def tree_house_inspect():
	print """ Upon closer inspection, you notice a few things that seem out of the ordinary:
The corner of a hardcover book peeking out from under the chair's cushion,
The initials G.L. embossed on the back of the chair,
and, gruesomely, scrawled in what looks like gore on the wall next to the opposite door
THE END IS THE ONLY OUTCOME. WE WILL PREVAIL.\n"""
	sleep(6)
	print """ The book is a diary. 
A fine one, with a golden embossed G.L. on the cover,
that has seen much wear and tear.
Whoever G.L. was and whatever happened to him here are questions that cannot have pleasant answers.
But how can you know unless you ask?"""
	 

def open_diary():
	print """ As soon as you open the cover, dust and ash drift out from between musty, 
yellowing pages, and the spine creaks at the effort.
It looks as though someone has carried it through a fire, 
and smells as though it was dragged through a gutter right after.
The odors of piss and smoke fill your nostrils, and it is deeply unpleasant.
Do you try to read it for clues, or discard the worthless piece of garbage?"""

def read_diary ():
	#automatically take diary pages wheen you pick it up
	#these are the pages that you can look back to
	print """ Most of the pages have stuck together, 
	are covered in illegible, bleeding ink, or been ripped out.
The few pages you can make out can be folded into your notebook
\n \n \n """

def discard_diary ():
	print """ Your great grand-grandfather's initials weren't GL anyway.
You're here for one reason and everything else is distraction."""


def clearing_path():
	pass

def default_forest():
	print """ The forest is beautiful but all-enveloping in its silence.
You feel pressure to uncover something, but what? You head to the tree house."""

def path_right():
	pass
	### do something at all with the right path


