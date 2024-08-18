from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 10
bosses = {
    "1": {
        "id": "1",
        "name": "Larry Koopa",
        "image": "https://static.wikia.nocookie.net/hello-yoshi/images/7/71/NSMBU_LarryKoopa.png",
        "boss-level": 1,
        "summary": "Larry Koopa, the youngest member of the Koopalings, exhibits a mischievous demeanor and a penchant for magical attacks. Despite being the weakest of his siblings, Larry compensates with agility and cunning tactics. His distinctive blue hair and shell make him easily recognizable among the Koopalings. Larry's battles often involve a mix of projectile attacks and acrobatic maneuvers, challenging Mario with his unpredictable style. While lacking the raw power of his siblings, Larry relies on his quick reflexes and magical abilities to put up a formidable fight.",
        "difficulty": 4,
        "nickname": "Cheatsy Koopa",
        "enemies": ["Goombas", "Hefty Goombas", "Big Goombas", "Koopa Troopas", "Koopa Paratroopas", "Piranha Plants", "Venus Fire Traps", "Hammer Bros", "Dry Bones", "Urchins", "Cheep Cheeps", "Mega Cheep-Cheeps", "Spiny Cheep Cheeps", "Deep-Cheeps", "Mega Deep-Cheeps", "Eep Cheeps", "Clampys", "Thwomps", "Big Thwomps", "Bowser"]
    },
    "2": {
        "id": "2",
        "name": "Morton Koopa Jr.",
        "image": "https://static.wikia.nocookie.net/fantendo/images/b/bb/MortonSSB4.png",
        "boss-level": 6,
        "summary": "Morton Koopa Jr., with his imposing size and rotating shell, presents a formidable challenge to Mario and his allies. Despite his sluggish movements, Morton compensates with brute strength and a relentless assault. His battles often take place in hazardous environments, with rotating platforms and deadly traps adding to the danger. Morton's combat style revolves around charging at his opponents, using his spiked shell as a deadly weapon. Despite his lack of finesse, Morton's sheer power and endurance make him a formidable adversary.",
        "difficulty": 5,
        "nickname": "Big Mouth Koopa",
        "enemies": ["Buzzy Beetles", "Spike Tops", "Porcupuffers","Bowser", "Fish Bones", "Swoopers", "Cooligans", "Spike", "Stone Spikes", "Fishbones", "Piranha Creepers", "Fire Bros", "Boomerang Bros", "Ice Bros", "Boo Buddies"]
    },
    "3": {
        "id": "3",
        "name": "Wendy O. Koopa",
        "image": "https://mario.wiki.gallery/images/thumb/9/95/NSMBW_Wendy_Artwork.png/1200px-NSMBW_Wendy_Artwork.png",
        "boss-level": "4",
        "summary": "Wendy O. Koopa, the only female Koopaling, combines grace with a fierce fighting spirit in her battles against Mario. With her magic wand and twirling acrobatics, Wendy creates a challenging and dynamic combat experience. Her battles often feature intricate patterns of magical projectiles and aerial assaults. Despite her girlish appearance, Wendy proves to be a formidable adversary, demonstrating both agility and cunning in battle. Her emotional reactions to defeat add depth to her character, hinting at a more vulnerable side beneath her tough exterior.",
        "difficulty": 6,
        "nickname" : "Kootie Pie Koopa",
        "enemies": ["Boos", "Circling Boo Buddies", "Broozers", "Swoops", "Foo", "Lava Bubbles", "Podoboos", "Fire Snakes", "Bowser", "Stretch", "Tail Boos", "Bomb Boos", "Fishin' Lakitus", "Spiny Hermit", "Lava Drops"]
    },
    "4": {
        "id": "4",
        "name": "Iggy Koopa",
        "image": "https://static.wikia.nocookie.net/hello-yoshi/images/7/7d/200px-IggyNSMBU.png",
        "boss-level": 5,
        "summary": "Iggy Koopa, with his wild appearance and unpredictable behavior, adds a touch of chaos to Mario's adventures. Iggy's battles are characterized by erratic movements and an arsenal of magical attacks. His maniacal laughter echoes through the battlefield as he unleashes a barrage of spells and traps. Despite his lack of focus, Iggy's sheer unpredictability makes him a challenging opponent to overcome. His battles often feature unconventional hazards and obstacles, keeping Mario on his toes throughout the encounter.",
        "difficulty": 7,
        "nickname": "Iggister",
        "enemies": ["Boomerang Bros", "Boomerang Bros", "Fire Bros", "Ice Bros", "Fire Bros", "Bowser", "Ice Bros", "Porcupuffers", "Fish Bones", "Magikoopas", "Swoops", "Fire Piranha Plants", "Fire Chomps", "Grrrols", "Bowser Statues"]
    },
    "5": {
        "id": "5",
        "name": "Roy Koopa",
        "image": "https://mario.wiki.gallery/images/thumb/6/67/NSMBW_Roy_Artwork.png/1200px-NSMBW_Roy_Artwork.png",
        "boss-level": 2,
        "summary": "Roy Koopa, with his muscular physique and aggressive fighting style, presents a formidable challenge to Mario and his companions. Roy's battles often feature a mix of physical attacks and strategic maneuvers, testing the player's reflexes and spatial awareness. His imposing presence and gruff demeanor make him a memorable adversary in the Mario series. Despite his tough exterior, Roy occasionally displays moments of vulnerability, adding depth to his character. His battles often require a blend of precision timing and strategic thinking to overcome.",
        "difficulty": 8,
        "nickname": "Bully Koopa",
        "enemies": ["Boos", "Big Boos", "Broozers", "Swoops", "Circling Boo Buddies", "Fishbones", "Fishin' Lakitus", "Stretch", "Tail Boos", "Bomb Boos", "Bowser", "Boomerang Bros", "Fire Bros", "Ice Bros", "Boo Buddies", "Boomerang Bros", "Fire Bros", "Ice Bros"]
    },
    "6": {
        "id": "6",
        "name": "Lemmy Koopa",
        "image": "https://static.wikia.nocookie.net/villains/images/7/74/Lemmy_SSBU.png",
        "boss-level": 3,
        "summary" : "Lemmy Koopa, with his playful demeanor and circus-inspired antics, adds a whimsical touch to Mario's adventures. Lemmy's battles often take place in vibrant and colorful settings, reflecting his carefree personality. His acrobatic maneuvers and unconventional attacks provide a unique and dynamic combat experience. Despite his lighthearted appearance, Lemmy proves to be a cunning adversary, using his agility and wit to outsmart Mario. His battles often feature a mix of platforming challenges and puzzle-solving elements, requiring players to think creatively to emerge victorious.",        
        "difficulty": 9,
        "nickname": "Hippity",
        "enemies": ["Cooligans", "Spike", "Stone Spikes", "Spike Tops", "Buzzy Beetles", "Fishbones", "Fire Bros", "Bowser", "Boomerang Bros", "Ice Bros", "Porcupuffers", "Swoopers", "Fire Snakes", "Spike", "Stone Spikes", "Spike Tops"]
    },
    "7": {
        "id": "7",
        "name": "Ludwig von Koopa",
        "image": "https://static.wikia.nocookie.net/ilvg/images/2/2a/Ludwig.png",
        "boss-level": 7,
        "summary": "Ludwig von Koopa, with his refined mannerisms and love for the arts, adds a touch of sophistication to Mario's adventures. Ludwig's battles often feature intricate patterns and elaborate traps, challenging players to stay alert and adapt to changing circumstances. His tall, green hair and aristocratic demeanor make him a memorable and distinctive adversary. Despite his cultured exterior, Ludwig proves to be a formidable fighter, using his intelligence and strategic thinking to gain the upper hand. His battles often require players to employ a mix of precision timing and quick reflexes to emerge victorious.",
        "difficulty": 10,
        "nickname": "Magician Koopa",
        "enemies": ["Porcupuffers", "Spike Tops", "Buzzy Beetles", "Boo Buddies", "Bowser", "Boomerang Bros", "Fire Bros", "Ice Bros", "Fishbones", "Swoopers", "Cooligans", "Boos", "Big Boos", "Broozers", "Swoops"]
    },
    "8": {
        "id": "8",
        "name": "Bowser Jr.",
        "image": "https://ssb.wiki.gallery/images/8/8b/Bowser_Jr._SSB4.png",
        "boss-level": 5,
        "summary": "Bowser Jr., the mischievous son of Bowser, plays a pivotal role in Mario's adventures, often serving as a miniboss or a final obstacle before facing his father. Despite his diminutive size, Bowser Jr. compensates with a wide array of gadgets and contraptions, making him a challenging adversary. His battles often feature a mix of aerial and ground-based attacks, requiring players to stay nimble and adaptable. Bowser Jr.'s relentless pursuit of Mario and Princess Peach fuels his determination to prove himself as a worthy successor to his father. Despite his villainous nature, Bowser Jr. occasionally displays moments of vulnerability, hinting at a more complex character beneath his tough exterior.",
        "difficulty": 9,
        "nickname": "Koopa Jr.",
        "enemies": ["Bullet Bills", "Banzai Bills", "Fire Bars", "Podoboos", "Lava Bubbles", "Bill Blasters", "Bowser Jr.", "Bowser", "Koopa Clown Cars", "Magikoopas", "Dry Bones", "Fishbones", "Boo Buddies", "Thwomps", "Big Thwomps", "Bowser Statues", "Dry Bowser"]
    },
    "9": {
        "id": "9",
        "name": "Kamek",
        "image": "https://static.wikia.nocookie.net/pm-universe/images/8/8e/Mario_Party_Star_Rush_-_Magikoopa.png",
        "boss-level": 8,
        "summary": "Kamek, a venerable Magikoopa and loyal caretaker of Bowser since his infancy, plays a pivotal role as a recurring adversary in the Mario series. Possessing vast magical prowess and cunning intellect, Kamek utilizes his sorcery to thwart Mario and his companions at every turn. His tactics often involve enchanting common foes, bolstering their strength and size to impede Mario's progress. Despite his formidable powers, Kamek is not impervious to defeat, yet his unwavering dedication to Bowser fuels his determination to impede Mario's efforts. Throughout the series, Kamek remains a persistent and formidable adversary, challenging Mario with his mystic abilities and strategic prowess.",
        "difficulty": 8,
        "nickname": "Magician Koopa",
        "enemies": ["Magikoopas", "Fire Bars", "Thwomps", "Big Thwomps", "Bowser Statues", "Dry Bowser", "Bowser", "Bullet Bills", "Banzai Bills", "Bowser Jr.", "Koopa Clown Cars", "Boo Buddies", "Podoboos", "Lava Bubbles", "Bill Blasters"]
    },
    "10": {
        "id": "10",
        "name": "Bowser",
        "image": "https://upload.wikimedia.org/wikipedia/en/9/92/Bowser_Stock_Art_2021.png",
        "boss-level": 8,
        "summary": "Bowser, the malevolent King Koopa and perennial nemesis of Mario, stands as the ultimate adversary in the Mushroom Kingdom. Possessing immense physical strength, mastery of dark magic, and an arsenal of formidable minions, Bowser poses an unparalleled threat to Mario's quest to rescue Princess Peach. Throughout the series, Bowser's ambitions to conquer the Mushroom Kingdom remain steadfast, driving him to devise elaborate schemes and employ brute force to achieve his goals. His fiery breath, massive size, and cunning intellect make him a formidable foe, capable of withstanding even the most determined assaults. Despite his villainous nature, Bowser occasionally exhibits moments of complexity, hinting at a deeper character beneath his tyrannical exterior.",
        "difficulty": 10,
        "nickname": "King Koopa",
        "enemies": ["Bowser Jr.", "Koopa Clown Cars", "Magikoopas", "Dry Bones", "Fishbones", "Bowser", "Boo Buddies", "Thwomps", "Big Thwomps", "Bowser Statues", "Dry Bowser", "Bullet Bills", "Banzai Bills"]
    }
}

def names():
    names = []
    for id, item in bosses.items():
        names.append(item["name"])
    return names

@app.route('/')
def homepage():
   return render_template('SMB_wiki_homepage.html', bosses=bosses, names=names())

@app.route('/search_results/<search>', methods=['GET', 'POST'])
def search(search=None):

    global bosses 

    results = [None] * len(bosses)

    for id, boss in bosses.items():
        boss_found = boss
        boss_found["matched"] = []
        boss_found["start_ind_name"] = [] 
        boss_found["end_ind_name"] = []
        boss_found["start_ind_summary"] = [] 
        boss_found["end_ind_summary"] = []
        boss_found["start_ind_nickname"] = []
        boss_found["end_ind_nickname"] = []
        if search.lower() in boss["name"].lower():
            boss_found["matched"].append("name")
            start_index = 0
            while True:
                substring_index = boss["name"].lower().find(search.lower(), start_index)
                if substring_index != -1:
                    boss_found["start_ind_name"].append(substring_index)
                    boss_found["end_ind_name"].append(boss_found["start_ind_name"][-1] + len(search))
                    start_index = substring_index + 1
                else:
                    break
            results[int(id)-1] = (boss_found)
        if search.lower() in boss["summary"].lower():
            boss_found["matched"].append("summary")
            start_index = 0
            while True:
                substring_index = boss["summary"].lower().find(search.lower(), start_index)
                if substring_index != -1:
                    boss_found["start_ind_summary"].append(substring_index)
                    boss_found["end_ind_summary"].append(boss_found["start_ind_summary"][-1] + len(search))
                    start_index = substring_index + 1
                else:
                    break
            results[int(id)-1] = (boss_found)
        if search.lower() in boss["nickname"].lower():
            boss_found["matched"].append("nickname")
            start_index = 0
            while True:
                substring_index = boss["nickname"].lower().find(search.lower(), start_index)
                if substring_index != -1:
                    boss_found["start_ind_nickname"].append(substring_index)
                    boss_found["end_ind_nickname"].append(boss_found["start_ind_nickname"][-1] + len(search))
                    start_index = substring_index + 1
                else:
                    break
            results[int(id)-1] = (boss_found)
    results = [value for value in results if value is not None]
    return render_template('SMB_wiki_searchpage.html', n_items=len(results), results=results, names=names(), search=search)

@app.route('/view/<id>')
def view(id=None):
    return render_template('SMB_wiki_charc.html', boss=bosses.get(id), names=names())

    

@app.route('/add')
def add():
    return render_template('SMB_wiki_add.html', names=names())

@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    global bosses
    global current_id



    new_boss = request.get_json()
    new_boss["enemies"]=list(set(new_boss["enemies"]))
    current_id+=1
    new_boss["id"] = str(current_id)

    bosses[str(current_id)] = (new_boss)
    return jsonify(url="view/"+new_boss["id"])

@app.route('/edit/<id>')
def edit(id=None):
    return render_template('SMB_wiki_edit.html', boss=bosses.get(id), names=names())

@app.route('/edit_entry', methods=['GET', 'POST'])
def edit_entry():
    global bosses
    global current_id

    new_boss = request.get_json()
    new_boss["enemies"]=list(set(new_boss["enemies"]))
    del bosses[new_boss["id"]]
    current_id+=1
    new_boss["id"] = str(current_id)

    bosses[str(current_id)] = (new_boss)
    return jsonify(url="/view/"+new_boss["id"])

if __name__ == '__main__':
   app.run(debug = True)

