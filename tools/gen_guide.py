"""Generates the Patchouli book `patchouli:gtc_guide` into <repo>/patchouli_books/gtc_guide/.
Run: python -I tools/gen_guide.py
External books (game-dir `patchouli_books/<name>/`) are the only form that loads without a mod jar in Patchouli 1.20.1.
Facts: GTCEu 7.5.3 jar (GTOres, lang), Cataclysm 3.31 jar (loot tables, structure biome tags, kill_* advancements), gregtechceu.github.io/GregTech-Modern/1.20.1."""
import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "patchouli_books" / "gtc_guide"
LANG = ROOT / "en_us"
if ROOT.exists():
    shutil.rmtree(ROOT)

def w(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

w(ROOT / "book.json", {
    "name": "GregTech Field Guide",
    "landing_text": "Field notes for GT: Cataclysm. GregTech progression, the pack's boss gates, and an index of every Cataclysm boss you have felled.",
    "version": 1,
    "show_progress": True,
    "i18n": False,
    "pause_game": False,
    "subtitle": "GT: Cataclysm",
})

CATS = {}
def cat(cid, name, icon, desc, sort):
    CATS[cid] = 0
    w(LANG / "categories" / f"{cid}.json", {"name": name, "description": desc, "icon": icon, "sortnum": sort})

def T(text, title=None):
    p = {"type": "patchouli:text", "text": text}
    if title:
        p["title"] = title
    return p

def S(item, title, text):
    return {"type": "patchouli:spotlight", "item": item, "title": title, "text": text}

def entry(cid, eid, name, icon, pages, **extra):
    CATS[cid] += 1
    d = {"name": name, "category": cid, "icon": icon, "sortnum": CATS[cid], "pages": pages}
    d.update(extra)
    w(LANG / "entries" / cid / f"{eid}.json", d)

BR = "$(br2)"

# ------------------------------------------------------------ Getting Started
cat("getting_started", "Getting Started", "gtceu:lp_steam_solid_boiler", "What GregTech changes and how to begin.", 1)
entry("getting_started", "what_gt_changes", "What GregTech changes", "minecraft:book", [
    T("GregTech replaces vanilla crafting with a long chain: steam, then electric tiers LV, MV, HV and up. Almost everything is made in machines, so open JEI (R on an item) often."),
    T("Ore: GT adds its own large ore veins. In this pack vanilla ores also generate alongside them, so early iron and coal are easy. Vanilla's large ore veins are removed." + BR + "A new world is needed to get vanilla ores in old chunks."),
    T("Progression: Steam, LV, then one voltage tier per boss. MV to ZPM machine hulls need a Cataclysm boss drop (see Pack Specifics)."),
])
entry("getting_started", "first_steps", "First steps", "gtceu:bronze_ingot", [
    T("1. Find copper and tin veins (Ores & Veins)." + BR + "2. Alloy 3 copper + 1 tin into bronze." + BR + "3. Build a Low Pressure Steam Solid Boiler and the first steam machines." + BR + "4. Use the Primitive Blast Furnace for steel, then go LV."),
    T("Wrench: right-click a machine to set its facing. Soft Mallet: toggles Up/Down mode on transformers. For any other tool or part, check its recipe in JEI."),
    T("The Heracles quest book (key J, or the Quest Book item) walks through the same order chapter by chapter."),
])

# ------------------------------------------------------------ Ores & Veins
cat("ores", "Ores & Veins", "minecraft:iron_ore", "How GT ore veins work and where to find them.", 2)
entry("ores", "how_veins_work", "How ore veins work", "minecraft:raw_iron", [
    T("GT ore comes in veins: big clusters (about 40 to 50 blocks wide) of several ores at once. Each vein has a weight, a height range and a dimension. Mine the whole cluster, it holds more than one material."),
    T("Veins are placed on a grid of 3 chunks, with up to 12 blocks of random offset (pack config). Ore indicators are on: Surface Rocks of a material mark where a vein lies below."),
    T("Surface Rocks: break one to get 3 Tiny Piles of the dust (Fortune adds more). Look for them on the ground, then dig down in that area."),
    T("In JEI, the 'Show GT Ore Veins' button lists every vein: ores inside, Weight, Spawn Range and Dimensions."),
])
entry("ores", "prospecting", "Prospecting", "gtceu:lv_machine_hull", [
    T("Prospectors scan for ore around you: Ore Prospector (LV), Advanced Prospector (HV), Super Prospector (LuV)." + BR + "They have modes: ores, fluids and bedrock ore, and use battery power."),
])
entry("ores", "early_veins", "Early veins", "gtceu:tin_ingot", [
    T("All Overworld, from GTCEu 7.5.3 data." + BR + "Coal: Y 10 to 140, in stone." + BR + "Iron: Y -10 to 60. Goethite, Limonite, Hematite, Malachite."),
    T("Tin: Cassiterite vein, Y 10 to 80. Tin and Cassiterite ores." + BR + "Copper-Tin: Y -10 to 160. Chalcopyrite, Zeolite, Cassiterite, Realgar."),
    T("Copper: Y -40 to 10, in deepslate. Chalcopyrite, Iron, Pyrite, Copper." + BR + "Many more veins exist (redstone, lapis, diamond, nickel...). Browse them in JEI."),
])

# ------------------------------------------------------------ Steam Age
cat("steam", "Steam Age", "gtceu:bronze_ingot", "Bronze, boilers and the first machines.", 3)
entry("steam", "bronze", "Bronze", "gtceu:bronze_ingot", [
    T("Bronze is the backbone of the steam age: alloy 3 copper with 1 tin. It makes the bronze hulls and casings of your first steam machines."),
])
entry("steam", "boilers", "Boilers and steam", "gtceu:lp_steam_solid_boiler", [
    T("Boilers turn water and fuel into steam. Solid boilers burn coal or charcoal, liquid boilers burn fuel, solar boilers use daylight. Low Pressure (bronze) and High Pressure (steel) versions exist."),
    T("Warning: never let a hot boiler run out of water. The wiki warns that steam can get explosive."),
])
entry("steam", "steam_machines", "Steam machines", "gtceu:lp_steam_macerator", [
    T("Steam machines (macerator, furnace, forge hammer, alloy smelter, compressor, extractor, rock crusher, miner) exist as Low and High Pressure versions. High Pressure uses the improved steel hull and is faster."),
    T("Chain: Coke Oven (coal to coke + creosote), Primitive Blast Furnace (iron + coke to steel), then craft the LV machine hull. Steel ends the steam age."),
])

# ------------------------------------------------------------ Power & Cables
cat("power", "Power & Cables", "gtceu:lv_machine_hull", "EU, voltage tiers, cables and safety.", 4)
entry("power", "eu_tiers", "EU and voltage tiers", "gtceu:lv_machine_hull", [
    T("Energy is EU. Power per tick = voltage x amps." + BR + "ULV 8, LV 32, MV 128, HV 512 EU/t"),
    T("EV 2048, IV 8192, LuV 32768, ZPM 131072 EU/t." + BR + "Each tier is 4 times the voltage of the one below. Machines need the voltage of their tier or lower."),
])
entry("power", "cables", "Cables and loss", "gtceu:tin_single_cable", [
    T("Cables lose about 1 EU per block per amp, so keep runs short. Higher tier cables do not always lose less."),
    T("Overvoltage destroys the cable (it acts as a fuse). Too many amps heats it, burns the insulation and then sets it on fire." + BR + "Touching a bare wire that carried power is dangerous."),
])
entry("power", "transformers", "Transformers and batteries", "gtceu:lv_machine_hull", [
    T("A transformer steps 1 amp of a higher tier to 4 amps of the lower tier, or the reverse. Use a Soft Mallet to switch Up/Down. 2A, 4A and 16A versions exist."),
    T("Batteries and battery buffers store EU to smooth out generation."),
])
entry("power", "explosions", "Explosion warning", "minecraft:tnt", [
    T("Feeding a machine a higher voltage than its tier can destroy it. Put a transformer between tiers, and place a cheap low-tier cable as a fuse in front of expensive machines."),
])

# ------------------------------------------------------------ Machines
cat("machines", "Machines & Multiblocks", "gtceu:electric_blast_furnace", "Hulls, multiblocks and research.", 5)
entry("machines", "hulls", "Machine hulls", "gtceu:lv_machine_hull", [
    T("The hull is the base of every single-block machine of a tier. LV is not gated. MV and above hulls are Assembler-only and need a boss drop catalyst (see Pack Specifics)."),
])
entry("machines", "ebf", "Electric Blast Furnace", "gtceu:electric_blast_furnace", [
    T("A heat-based multiblock for high temperature smelting, built with heating coils (start with Cupronickel). Aluminium needs it. Check the multiblock preview in JEI."),
    T("It needs an Energy Hatch, which uses a machine hull. At MV that is the gated MV hull. The Vacuum Freezer cools hot ingots made in it."),
])
entry("machines", "pyrolyse", "Pyrolyse Oven", "gtceu:pyrolyse_oven", [
    T("A multiblock for processing organic inputs into fuels and oils. Open its multiblock preview and recipes in JEI for exact inputs."),
])
entry("machines", "cleanroom", "Cleanroom", "gtceu:cleanroom", [
    T("Needed for wafers and the HV Nanoprocessor onward. Build the cleanroom multiblock (see JEI preview), it uses Cleanroom Glass and filter casings."),
])
entry("machines", "assembly_line", "Assembly Line and Research", "gtceu:assembly_line", [
    T("The Assembly Line is a long multiblock for the most complex parts (IV and up). Recipes from LuV onward need research first."),
    T("The Research Station creates the research data for those recipes."),
])

# ------------------------------------------------------------ Circuits
cat("circuits", "Circuits & Materials", "gtceu:basic_electronic_circuit", "What each tier needs.", 6)
entry("circuits", "chain", "Circuit chain", "gtceu:basic_electronic_circuit", [
    T("LV: Basic Electronic Circuit" + BR + "MV: Good Electronic Circuit" + BR + "HV: Nanoprocessor (cleanroom wafers)" + BR + "EV: Quantum Processor"),
    T("IV: Crystal Processor (Assembly Line)" + BR + "LuV: Wetware Processor" + BR + "Build a Circuit Assembler early to automate them."),
])
entry("circuits", "metals", "Key metals by tier", "gtceu:steel_ingot", [
    T("LV: steel" + BR + "MV: aluminium (Electric Blast Furnace)" + BR + "HV: stainless steel" + BR + "EV: titanium" + BR + "IV: tungsten steel"),
    T("Hull cables: MV copper, HV gold, EV aluminium, IV platinum, LuV niobium-titanium, ZPM vanadium-gallium."),
])

# ------------------------------------------------------------ Pack Specifics
cat("pack", "Pack Specifics", "cataclysm:flame_eye", "Boss gates, shaders, maps, keys and links.", 7)
entry("pack", "boss_gates", "Boss-gated hulls", "cataclysm:monstrous_horn", [
    T("MV to ZPM machine hulls are craftable only in an Assembler. The recipe needs a boss drop as a non-consumed catalyst: kill each boss once, keep the item, craft all you like."),
    T("MV: Netherite Monstrosity, Monstrous Horn" + BR + "HV: Ignis, Ignitium Ingot" + BR + "EV: The Harbinger, Witherite Ingot" + BR + "IV: Ender Guardian, Gauntlet of Guard"),
    T("LuV: Maledictus, Cursium Ingot" + BR + "ZPM: Scylla, Essence of the Storm" + BR + "The Harbinger drops a Block of Witherite: uncraft it into ingots."),
])
entry("pack", "qol", "Shaders, map, keys", "minecraft:map", [
    T("Shaders (optional): Options > Video Settings > Shader Packs. Potato Shaders is light; MakeUp - Ultra Fast looks nicer. Set Off if FPS drops."),
    T("Xaero's maps: minimap in a corner, world map on M. Waypoint your base and every boss structure."),
    T("Quest book: key J (Open Quests), or right-click the Quest Book item. Rebind in Controls if it clashes."),
])
entry("pack", "links", "Wiki links", "minecraft:writable_book", [
    T("GregTech Modern docs (1.20.1):" + BR + "gregtechceu.github.io/GregTech-Modern/1.20.1/" + BR + "Sections: Gameplay (Steam, Electricity, Ore Generation)."),
])

# ------------------------------------------------------------ Boss Index
cat("boss_index", "Boss Index", "cataclysm:void_eye", "Every Cataclysm boss. Entries unlock when you defeat them.", 8)
entry("boss_index", "00_about", "About the Index", "minecraft:book", [
    T("Each boss has a '???' entry with a rumour of where it lives. Defeat it and its full entry appears: name, home, drops and what it unlocks."),
    T("Unlock uses Cataclysm's own kill advancements. For testing: /advancement grant @s only cataclysm:kill_ignis"),
])

BOSSES = [
    # id, advancement, name, icon, hint, structure, where, eye, drops, drops_icon, gate
    ("monstrosity", "cataclysm:kill_monstrosity", "Netherite Monstrosity", "cataclysm:monstrous_eye",
     "Deep in the Nether, in its forests, soul sand valleys and wastes, a black forge waits by its anvil.",
     "Soul Forge", "Nether: Crimson Forest, Warped Forest, Soul Sand Valley, Nether Wastes", "Eye of Monstrous",
     "Infernal Forge, Monstrous Horn, Lava Power Cell", "cataclysm:monstrous_horn", "MV machine hull (Monstrous Horn)"),
    ("ignis", "cataclysm:kill_ignis", "Ignis", "cataclysm:flame_eye",
     "Only in the barren wastes of the Nether, a scorched arena burns.",
     "Burning Arena", "Nether: Nether Wastes", "Eye of Flame",
     "Ignitium Ingot", "cataclysm:ignitium_ingot", "HV machine hull (Ignitium Ingot)"),
    ("harbinger", "cataclysm:kill_harbinger", "The Harbinger", "cataclysm:mech_eye",
     "Far underground, in the caves, something mechanical still hums.",
     "Ancient Factory", "Overworld: underground", "Eye of Mech",
     "Block of Witherite (uncraft into Witherite Ingots)", "cataclysm:witherite_block", "EV machine hull (Witherite Ingot)"),
    ("guardian", "cataclysm:kill_ender_guardian", "Ender Guardian", "cataclysm:void_eye",
     "Beyond the End island, on the outer highlands and midlands, a ruined citadel stands guard.",
     "Ruined Citadel", "The End: End Highlands, End Midlands", "Eye of Void",
     "Gauntlet of Guard", "cataclysm:gauntlet_of_guard", "IV machine hull (Gauntlet of Guard)"),
    ("maledictus", "cataclysm:kill_maledictus", "Maledictus", "cataclysm:cursed_eye",
     "On the snowy plains, a frozen prison holds the restless dead.",
     "Frosted Prison", "Overworld: Snowy Plains", "Eye of Curse",
     "Cursium Ingot", "cataclysm:cursium_ingot", "LuV machine hull (Cursium Ingot)"),
    ("scylla", "cataclysm:kill_scylla", "Scylla", "cataclysm:storm_eye",
     "In warm, shallow seas, an ancient temple rises from the waves.",
     "Acropolis", "Overworld: Warm Ocean", "Eye of Storm",
     "Lacrima, Essence of the Storm", "cataclysm:essence_of_the_storm", "ZPM machine hull (Essence of the Storm)"),
    ("leviathan", "cataclysm:kill_leviathan", "The Leviathan", "cataclysm:abyss_eye",
     "Far below the surface of the deep ocean, a drowned city sleeps.",
     "Sunken City", "Overworld: Deep Ocean (including lukewarm, cold, frozen)", "Eye of Abyss",
     "Tidal Claws, Abyssal Egg", "cataclysm:tidal_claws", "No hull gate in this pack"),
    ("remnant", "cataclysm:kill_remnant", "Ancient Remnant", "cataclysm:desert_eye",
     "In the open desert, a cursed pyramid hides something ancient.",
     "Cursed Pyramid", "Overworld: Desert", "Eye of Desert",
     "Sandstorm in a Bottle, Remnant's Skull, Block of Ancient Metal", "cataclysm:sandstorm_in_a_bottle", "No hull gate in this pack"),
]

for i, (bid, adv, name, icon, hint, struct, where, eye, drops, dicon, gate) in enumerate(BOSSES, 1):
    entry("boss_index", f"{i:02d}_{bid}_hint", f"No. {i:02d}: ???", "minecraft:barrier", [
        T("Unknown. Rumour: " + hint + BR + "Defeat it to record it here."),
        {**T(f"Recorded. See the entry named {name}."), "advancement": adv},
    ])
    entry("boss_index", f"{i:02d}_{bid}", name, icon, [
        T(f"$(l)No. {i:02d}: {name}$()" + BR + f"Structure: {struct}" + BR + f"Where: {where}" + BR + f"Finder: {eye} (use like an Eye of Ender)."),
        S(dicon, "Drops", f"Drops: {drops}." + BR + f"Opens: {gate}."),
    ], advancement=adv, secret=True)

print("OK", sum(CATS.values()), "entries,", len(CATS), "categories")
for k, v in CATS.items():
    print(" ", k, v)
