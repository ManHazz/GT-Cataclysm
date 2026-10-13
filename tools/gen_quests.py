#!/usr/bin/env python3
"""Generate the Heracles questbook under config/heracles/.

Usage (from repo root):  python -I tools/gen_quests.py

Writes config/heracles/groups.txt and config/heracles/quests/<chapter>/<quest>.json.
Every item/entity/structure ID used here was verified from the mod jars
(lang files, recipes, loot tables, structure data) and is re-checked on a
server boot (Heracles logs a load error per bad quest).
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "config" / "heracles"
STEP = 44  # grid spacing in quest-screen pixels

# ---------------------------------------------------------------- helpers
def item(i, n=1):
    return {"type": "heracles:item", "item": i, "amount": n}

def kill(e, title, n=1):
    return {"type": "heracles:kill_entity", "title": title, "entity": {"type": e}, "amount": n}

def check(title):
    return {"type": "heracles:check", "title": title}

def struct(s, title):
    return {"type": "heracles:structure", "title": title, "structures": s}

def xp(n):
    return {"type": "heracles:xp", "xptype": "LEVEL", "amount": n}

def gift(i, n=1):
    return {"type": "heracles:item", "item": {"id": i, "count": n}}

CHAPTERS = []  # (group name, folder, [quests])

def chapter(name, folder, quests):
    CHAPTERS.append((name, folder, quests))

def Q(qid, title, icon, desc, pos, tasks, deps=(), rewards=None, sub=""):
    return dict(id=qid, title=title, icon=icon, desc=desc, pos=pos,
                tasks=tasks, deps=list(deps), rewards=rewards or [xp(1)], sub=sub)

# ---------------------------------------------------------------- Welcome
chapter("Welcome", "welcome", [
    Q("welcome_intro", "Welcome to GT: Cataclysm", "minecraft:book",
      ["This pack combines GregTech progression with L_Ender's Cataclysm bosses.",
       "Work through the chapters on the left. Start with Steam & LV, then one chapter per voltage tier.",
       "You received a Quest Book item: right-click it to open this questbook any time. The Open Quests key defaults to U, which clashes with JEI (Show Uses) and Xaero's waypoints, so rebind it in Controls > Key Binds."],
      (0, 0), [check("Read the intro")], sub="Start here"),
    Q("welcome_gates", "How the gates work", "minecraft:iron_bars",
      ["Machine hulls for MV, HV, EV, IV, LuV and ZPM can only be made in an Assembler, and each recipe needs a Cataclysm boss drop as a catalyst.",
       "The catalyst is NOT consumed. Kill each boss once, keep the drop, and craft as many hulls of that tier as you like."],
      (1, 0), [check("Understood")], deps=["welcome_intro"], sub="Boss drops unlock tiers"),
    Q("welcome_jei", "Recipes with JEI", "minecraft:crafting_table",
      ["Hover over an item and press R to see how it is made, or U to see what it is used in.",
       "GregTech machines have their own recipe tabs. Press the Bookmark key (A) over an item to pin it."],
      (2, 0), [check("Got it")], deps=["welcome_gates"], sub="R = recipes, U = uses"),
    Q("welcome_jade", "Jade tooltips", "minecraft:spyglass",
      ["Look at any block or mob and Jade shows its name, source mod and extra details.",
       "On GregTech machines it also shows energy and progress, which helps a lot when debugging a setup."],
      (3, 0), [check("Got it")], deps=["welcome_jei"], sub="Know what you are looking at"),
    Q("welcome_map", "Xaero's maps", "minecraft:map",
      ["The minimap sits in a screen corner and the full World Map opens with M.",
       "Make a waypoint at your base and at every boss structure you find, so you can always find your way back."],
      (4, 0), [check("Got it")], deps=["welcome_jade"], sub="Never get lost"),
    Q("welcome_shaders", "Shaders (optional)", "minecraft:glowstone",
      ["Go to Options > Video Settings > Shader Packs and pick Potato Shaders for a light, fast look.",
       "MakeUp - Ultra Fast is a nicer-looking alternative if your PC can handle it. If your FPS drops, set Shader Packs back to Off."],
      (5, 0), [check("Got it")], deps=["welcome_map"], sub="Potato or MakeUp"),
    Q("welcome_ram", "Memory", "minecraft:redstone",
      ["Give the game 6 to 8 GB of RAM (for example -Xms6G -Xmx8G in your launcher's Java arguments).",
       "Much less causes lag spikes in big GregTech setups, and much more does not help."],
      (6, 0), [check("Got it")], deps=["welcome_shaders"], rewards=[xp(2)], sub="6-8 GB recommended"),
])

# ---------------------------------------------------------------- Steam Age -> LV
chapter("Steam & LV", "steam_lv", [
    Q("steam_bronze", "Bronze", "gtceu:bronze_ingot",
      ["Bronze is the backbone of the steam age. Alloy 3 copper with 1 tin to get it.",
       "Use JEI on the ingot to see every way of making it."],
      (0, 0), [item("gtceu:bronze_ingot", 8)], deps=["welcome_intro"], sub="3 copper + 1 tin"),
    Q("steam_boiler", "Make some steam", "gtceu:lp_steam_solid_boiler",
      ["The Low Pressure Steam Solid Boiler burns fuel and water into steam, which powers the first machines.",
       "Feed it coal or charcoal and keep it supplied with water."],
      (1, 0), [item("gtceu:lp_steam_solid_boiler")], deps=["steam_bronze"], sub="Steam boiler"),
    Q("steam_macerator", "Steam macerator", "gtceu:lp_steam_macerator",
      ["Macerating ore gives more dust than smelting it directly. It is the first step of the ore processing chain.",
       "Connect it to the boiler with a Bronze pipe or put it right next to it."],
      (2, 0), [item("gtceu:lp_steam_macerator")], deps=["steam_boiler"], sub="Double your ore"),
    Q("steam_furnace", "Steam furnace", "gtceu:lp_steam_furnace",
      ["Smelts items faster than a vanilla furnace and runs on steam."],
      (3, 0), [item("gtceu:lp_steam_furnace")], deps=["steam_macerator"], sub="Smelting on steam"),
    Q("steam_coke", "Coke oven", "gtceu:coke_oven",
      ["The Coke Oven turns coal into coke and creosote oil, which you will need for steel.",
       "Make Coke Oven Bricks, then check the multiblock preview in JEI."],
      (4, 0), [item("gtceu:coke_oven_brick", 8), item("gtceu:coke_oven")], deps=["steam_furnace"], sub="Fuel for steel"),
    Q("steam_pbf", "Primitive blast furnace", "gtceu:primitive_blast_furnace",
      ["Iron plus coke in a Primitive Blast Furnace gives steel, your first big upgrade."],
      (5, 0), [item("gtceu:primitive_blast_furnace")], deps=["steam_coke"], sub="Iron to steel"),
    Q("steam_steel", "Steel", "gtceu:steel_ingot",
      ["Steel is needed for nearly everything in the LV age. Make a good stack of it."],
      (6, 0), [item("gtceu:steel_ingot", 16)], deps=["steam_pbf"], rewards=[xp(2)], sub="The LV material"),
    Q("lv_hull", "LV machine hull", "gtceu:lv_machine_hull",
      ["The hull is the base of every LV single-block machine. LV and below are not gated by a boss.",
       "Craft one, then right-click machines with a wrench to set their facing."],
      (6, 1), [item("gtceu:lv_machine_hull")], deps=["steam_steel"], sub="Base of LV machines"),
    Q("lv_circuit", "First circuit", "gtceu:basic_electronic_circuit",
      ["Circuits unlock every machine upgrade. The Basic Electronic Circuit is your first one."],
      (5, 1), [item("gtceu:basic_electronic_circuit", 4)], deps=["lv_hull"], sub="Basic Electronic Circuit"),
    Q("lv_macerator", "LV macerator", "gtceu:lv_macerator",
      ["Your first electric machine. It is faster and gives better output than the steam version."],
      (4, 1), [item("gtceu:lv_macerator")], deps=["lv_circuit"], sub="Go electric"),
    Q("lv_electric_furnace", "LV electric furnace", "gtceu:lv_electric_furnace",
      ["Time to retire the steam furnace."],
      (3, 1), [item("gtceu:lv_electric_furnace")], deps=["lv_macerator"], sub="Retire the boiler"),
    Q("lv_turbine", "LV steam turbine", "gtceu:lv_steam_turbine",
      ["A Steam Turbine turns steam into electricity (EU). Feed it with a boiler.",
       "Power is the limit for most early machines, so build a few."],
      (2, 1), [item("gtceu:lv_steam_turbine")], deps=["lv_electric_furnace"], sub="Make EU"),
    Q("lv_assembler", "LV assembler", "gtceu:lv_assembler",
      ["The Assembler crafts the most complex items in the pack, including every gated hull.",
       "Make it before you go for your first boss."],
      (1, 1), [item("gtceu:lv_assembler")], deps=["lv_turbine"], sub="Needed for all hulls"),
    Q("lv_circuit_assembler", "Circuit assembler", "gtceu:lv_circuit_assembler",
      ["Automates circuit making and makes later tiers far less painful."],
      (0, 1), [item("gtceu:lv_circuit_assembler")], deps=["lv_assembler"], rewards=[xp(3)], sub="Circuits on demand"),
])

# ---------------------------------------------------------------- tier chapters
def tier(name, folder, p, boss_id, boss_name, boss_text, catalyst, cat_name, cat_text,
         hull, milestones, boss_q, prev):
    """p = id prefix, milestones = [(id, title, icon, item_id, amount, text, sub)]"""
    qs = [
        Q(f"{p}_boss", f"Kill the {boss_name}", catalyst,
          boss_text + ["The kill itself is tracked once, in the Bosses chapter. This quest completes after that one; just tick it off."],
          (0, 0), [check(f"{boss_name} defeated")], deps=[boss_q, prev], rewards=[xp(5)], sub="Boss kill"),
        Q(f"{p}_catalyst", f"Get the {cat_name}", catalyst, cat_text, (1, 0),
          [item(catalyst)], deps=[f"{p}_boss"], rewards=[xp(2)], sub="Catalyst (not consumed)"),
        Q(f"{p}_hull", f"Craft the {name.split()[0]} machine hull", hull,
          [f"Craft the hull in an Assembler. The recipe needs the {cat_name} as a catalyst and does not use it up.",
           "Check the recipe in JEI for the exact inputs. Every machine of this tier is built from this hull."],
          (2, 0), [item(hull)], deps=[f"{p}_catalyst"], rewards=[xp(5)], sub="Unlocks the tier"),
    ]
    for k, (mid, title, icon, iid, amt, text, sub) in enumerate(milestones):
        dep = [f"{p}_hull"] if k == 0 else [f"{p}_{milestones[k-1][0]}"]
        qs.append(Q(f"{p}_{mid}", title, icon, text if isinstance(text, list) else [text],
                    (3 + k, 0), [item(iid, amt)], deps=dep, sub=sub))
    chapter(name, folder, qs)

tier("MV", "mv", "mv",
     "cataclysm:netherite_monstrosity", "Netherite Monstrosity",
     ["A huge Nether boss guarding the Soul Forge. Bring strong armour, potions and plenty of food.",
      "Find the Soul Forge in the Nether (Crimson Forest, Warped Forest, Soul Sand Valley or Nether Wastes). An Eye of Monstrous, used like an Eye of Ender, points to it."],
     "cataclysm:monstrous_horn", "Monstrous Horn",
     ["The Netherite Monstrosity drops the Monstrous Horn. Keep it in your inventory or a chest; it is the MV catalyst and is not consumed."],
     "gtceu:mv_machine_hull", [
         ("assembler", "MV assembler", "gtceu:mv_assembler", "gtceu:mv_assembler", 1,
          "Faster assembling and bigger recipes. Needed for most MV parts.", "Faster crafting"),
         ("ebf", "Electric blast furnace", "gtceu:electric_blast_furnace", "gtceu:electric_blast_furnace", 1,
          ["A heat-based multiblock for high temperature smelting. Check the preview in JEI and build it with Cupronickel Coil Blocks.", "Aluminium smelting in it needs an MV Energy Hatch, which in turn needs the gated MV machine hull you just unlocked."], "High-temperature smelting"),
         ("aluminium", "Aluminium", "gtceu:aluminium_ingot", "gtceu:aluminium_ingot", 8,
          "Aluminium is the key MV metal. Smelt it in the Electric Blast Furnace from the previous quest.", "Key MV metal"),
         ("circuit", "Good circuits", "gtceu:good_electronic_circuit", "gtceu:good_electronic_circuit", 4,
          "The MV circuit. You will need many of them.", "MV circuit"),
     ], "boss_monstrosity", "lv_circuit_assembler")

tier("HV", "hv", "hv",
     "cataclysm:ignis", "Ignis",
     ["Ignis is a fire boss that fights in the Burning Arena, a Nether Wastes structure.",
      "An Eye of Flame, used like an Eye of Ender, points to the arena. Fire resistance helps a lot."],
     "cataclysm:ignitium_ingot", "Ignitium Ingot",
     ["Ignis drops Ignitium Ingots. Keep one; it is the HV catalyst and is not consumed."],
     "gtceu:hv_machine_hull", [
         ("stainless", "Stainless steel", "gtceu:stainless_steel_ingot", "gtceu:stainless_steel_ingot", 8,
          "Stainless steel is the HV workhorse alloy.", "HV alloy"),
         ("freezer", "Vacuum freezer", "gtceu:vacuum_freezer", "gtceu:vacuum_freezer", 1,
          "Cools hot ingots from the Electric Blast Furnace into usable metal.", "Cool hot ingots"),
         ("cleanroom", "Cleanroom", "gtceu:cleanroom", "gtceu:cleanroom", 1,
          "The Nanoprocessor needs wafers made in a cleanroom. Check the multiblock preview in JEI.", "Clean circuit production"),
         ("circuit", "Nanoprocessor", "gtceu:nano_processor", "gtceu:nano_processor", 4,
          "The HV circuit.", "HV circuit"),
         ("chem", "HV chemical reactor", "gtceu:hv_chemical_reactor", "gtceu:hv_chemical_reactor", 1,
          "Plastics and many other chemicals start here.", "Chemistry begins"),
     ], "boss_ignis", "mv_circuit")

tier("EV", "ev", "ev",
     "cataclysm:the_harbinger", "The Harbinger",
     ["A mechanical boss in the Ancient Factory, a large structure that can generate in caves or deep underground. Bring a good pickaxe and light sources.",
      "It is very hard to spot by chance, so the practical way to find it is an Eye of Mech, used like an Eye of Ender."],
     "cataclysm:witherite_ingot", "Witherite Ingot",
     ["The Harbinger drops a Block of Witherite. Put it alone in a crafting grid to get 9 Witherite Ingots.",
      "Keep one ingot; it is the EV catalyst and is not consumed."],
     "gtceu:ev_machine_hull", [
         ("titanium", "Titanium", "gtceu:titanium_ingot", "gtceu:titanium_ingot", 8,
          "Titanium is the main EV metal.", "Main EV metal"),
         ("circuit", "Quantum processor", "gtceu:quantum_processor", "gtceu:quantum_processor", 4,
          "The EV circuit.", "EV circuit"),
         ("chem", "EV chemical reactor", "gtceu:ev_chemical_reactor", "gtceu:ev_chemical_reactor", 1,
          "Faster chemistry, and more fluid slots for bigger recipes.", "Better chemistry"),
     ], "boss_harbinger", "hv_circuit")

tier("IV", "iv", "iv",
     "cataclysm:ender_guardian", "Ender Guardian",
     ["The Ender Guardian lives in the Ruined Citadel, which generates in the End (End Highlands and End Midlands).",
      "An Eye of Void, used like an Eye of Ender, points to the citadel. Be ready for the End first."],
     "cataclysm:gauntlet_of_guard", "Gauntlet of Guard",
     ["The Ender Guardian drops the Gauntlet of Guard. Keep it safe; it is the IV catalyst and is not consumed."],
     "gtceu:iv_machine_hull", [
         ("tungsten_steel", "Tungsten steel", "gtceu:tungsten_steel_ingot", "gtceu:tungsten_steel_ingot", 8,
          "Tungsten steel is the IV metal. It needs a lot of power to make.", "IV metal"),
         ("circuit", "Crystal processor", "gtceu:crystal_processor", "gtceu:crystal_processor", 4,
          "The IV circuit.", "IV circuit"),
         ("assembly_line", "Assembly line", "gtceu:assembly_line", "gtceu:assembly_line", 1,
          "A long multiblock that builds the most complex parts. Recipes from LuV onward need research first.", "Complex parts"),
         ("arm", "IV robot arm", "gtceu:iv_robot_arm", "gtceu:iv_robot_arm", 2,
          "A key component for IV machines and the assembly line.", "Key component"),
     ], "boss_guardian", "ev_circuit")

tier("LuV", "luv", "luv",
     "cataclysm:maledictus", "Maledictus",
     ["Maledictus haunts the Frosted Prison, a structure in snowy plains. Expect undead.",
      "An Eye of Curse, used like an Eye of Ender, points to the prison."],
     "cataclysm:cursium_ingot", "Cursium Ingot",
     ["Maledictus drops Cursium Ingots. Keep one; it is the LuV catalyst and is not consumed."],
     "gtceu:luv_machine_hull", [
         ("research", "Research station", "gtceu:research_station", "gtceu:research_station", 1,
          "Only needed for LuV and higher assembly line recipes, where it creates the research data.", "Unlock recipes"),
         ("circuit", "Wetware processor", "gtceu:wetware_processor", "gtceu:wetware_processor", 4,
          "The LuV circuit.", "LuV circuit"),
         ("fusion", "Fusion reactor", "gtceu:luv_fusion_reactor", "gtceu:luv_fusion_reactor", 1,
          "The Fusion Reactor Computer MK I, the start of fusion power.", "Fusion power"),
     ], "boss_maledictus", "iv_circuit")

tier("ZPM", "zpm", "zpm",
     "cataclysm:scylla", "Scylla",
     ["Scylla is the sea boss of the Acropolis, a structure that generates in warm ocean. Her allies guard it.",
      "An Eye of Storm, used like an Eye of Ender, points to the Acropolis. Water breathing is very handy."],
     "cataclysm:essence_of_the_storm", "Essence of the Storm",
     ["Scylla drops the Essence of the Storm. Keep it safe; it is the ZPM catalyst and is not consumed."],
     "gtceu:zpm_machine_hull", [
         ("motor", "ZPM electric motor", "gtceu:zpm_electric_motor", "gtceu:zpm_electric_motor", 2,
          "A key component for ZPM machines.", "Key component"),
         ("coil", "Naquadah coils", "gtceu:naquadah_coil_block", "gtceu:naquadah_coil_block", 16,
          "The heating coil for the hottest blast furnace recipes.", "Top-tier heating"),
         ("fusion", "Fusion reactor MK II", "gtceu:zpm_fusion_reactor", "gtceu:zpm_fusion_reactor", 1,
          "A bigger fusion reactor, more output.", "More fusion power"),
     ], "boss_scylla", "luv_circuit")

# ---------------------------------------------------------------- Bosses
def boss(qid, title, icon, ent, ent_name, struct_id, struct_name, text, pos, deps=()):
    return Q(qid, title, icon, text, pos,
             [struct(struct_id, f"Find the {struct_name}"), kill(ent, ent_name)],
             deps=deps, rewards=[xp(5)], sub=struct_name)

chapter("Bosses", "bosses", [
    Q("boss_overview", "Boss overview", "cataclysm:flame_eye",
      ["Six Cataclysm bosses each unlock one machine tier. Each structure below was checked against Cataclysm's data.",
       "Craft the matching Eye (see JEI), which needs an Eye of Ender, and use it like an Eye of Ender to find the structure."],
      (0, 0), [check("Got it")], deps=["welcome_gates"], sub="Where to find them"),
    boss("boss_monstrosity", "Netherite Monstrosity", "cataclysm:monstrous_eye", "cataclysm:netherite_monstrosity",
         "Netherite Monstrosity", "cataclysm:soul_black_smith", "Soul Forge",
         ["Soul Forge: Nether structure, found in Crimson Forest, Warped Forest, Soul Sand Valley and Nether Wastes. Drops the Monstrous Horn (MV)."],
         (1, 0), ["boss_overview"]),
    boss("boss_ignis", "Ignis", "cataclysm:flame_eye", "cataclysm:ignis",
         "Ignis", "cataclysm:burning_arena", "Burning Arena",
         ["Burning Arena: Nether Wastes structure. Drops the Ignitium Ingot (HV)."],
         (2, 0), ["boss_monstrosity"]),
    boss("boss_harbinger", "The Harbinger", "cataclysm:mech_eye", "cataclysm:the_harbinger",
         "The Harbinger", "cataclysm:ancient_factory", "Ancient Factory",
         ["Ancient Factory: can generate in caves and deep underground; use the Eye of Mech to find it. Drops a Block of Witherite, which you uncraft into Witherite Ingots (EV)."],
         (3, 0), ["boss_ignis"]),
    boss("boss_guardian", "Ender Guardian", "cataclysm:void_eye", "cataclysm:ender_guardian",
         "Ender Guardian", "cataclysm:ruined_citadel", "Ruined Citadel",
         ["Ruined Citadel: End structure, found in End Highlands and End Midlands. Drops the Gauntlet of Guard (IV)."],
         (4, 0), ["boss_harbinger"]),
    boss("boss_maledictus", "Maledictus", "cataclysm:cursed_eye", "cataclysm:maledictus",
         "Maledictus", "cataclysm:frosted_prison", "Frosted Prison",
         ["Frosted Prison: structure in snowy plains. Drops the Cursium Ingot (LuV)."],
         (5, 0), ["boss_guardian"]),
    boss("boss_scylla", "Scylla", "cataclysm:storm_eye", "cataclysm:scylla",
         "Scylla", "cataclysm:acropolis", "Acropolis",
         ["Acropolis: structure in warm ocean. Drops the Essence of the Storm (ZPM)."],
         (6, 0), ["boss_maledictus"]),
])

# ---------------------------------------------------------------- AE2
chapter("AE2", "ae2", [
    Q("ae2_certus", "Certus quartz", "ae2:certus_quartz_crystal",
      ["Certus Quartz is the base material of Applied Energistics. Find it as ore in the Overworld, often near water or in caves."],
      (0, 0), [item("ae2:certus_quartz_crystal", 8)], deps=["lv_circuit"], sub="The basic resource"),
    Q("ae2_fluix", "Fluix", "ae2:fluix_crystal",
      ["Fluix Crystals are made by throwing charged certus quartz, redstone and quartz into water. They are needed for most network parts."],
      (1, 0), [item("ae2:fluix_crystal", 8)], deps=["ae2_certus"], sub="Throw into water"),
    Q("ae2_controller", "ME controller", "ae2:controller",
      ["The controller is the heart of a large network. Without one, a network works but is limited in size and channels.",
       "Place it, then connect devices with cables. Cable colour and glass cables are all fine."],
      (2, 0), [item("ae2:controller")], deps=["ae2_fluix"], sub="Heart of the network"),
    Q("ae2_drive", "ME drive", "ae2:drive",
      ["The drive holds up to 10 storage cells. Put it next to the controller or on the cable."],
      (3, 0), [item("ae2:drive")], deps=["ae2_controller"], sub="Holds your cells"),
    Q("ae2_cell", "Storage cell", "ae2:item_storage_cell_1k",
      ["Storage cells hold your items. Craft a housing and a storage component, then put them together."],
      (4, 0), [item("ae2:item_storage_cell_1k")], deps=["ae2_drive"], sub="Where items live"),
    Q("ae2_terminal", "ME terminal", "ae2:terminal",
      ["The terminal lets you view and take every item in the network. Right-click it to open."],
      (5, 0), [item("ae2:terminal")], deps=["ae2_cell"], rewards=[xp(2)], sub="Access your items"),
    Q("ae2_crafting_storage", "Crafting storage", "ae2:1k_crafting_storage",
      ["Autocrafting needs a crafting CPU. Build one from a Crafting Unit and a Crafting Storage block, then place them together."],
      (5, 1), [item("ae2:crafting_unit"), item("ae2:1k_crafting_storage")], deps=["ae2_terminal"], sub="Crafting CPU"),
    Q("ae2_pattern_terminal", "Pattern terminal", "ae2:pattern_encoding_terminal",
      ["Encode recipes as patterns here. Patterns tell the network how to craft an item."],
      (4, 1), [item("ae2:pattern_encoding_terminal")], deps=["ae2_crafting_storage"], sub="Teach recipes"),
    Q("ae2_provider", "Pattern provider", "ae2:pattern_provider",
      ["Put patterns in a provider. It pushes the ingredients into the machine next to it, such as a GregTech machine."],
      (3, 1), [item("ae2:pattern_provider")], deps=["ae2_pattern_terminal"], sub="Feed your machines"),
    Q("ae2_molecular", "Molecular assembler", "ae2:molecular_assembler",
      ["Crafts items from crafting-table patterns. Put it next to a provider."],
      (2, 1), [item("ae2:molecular_assembler")], deps=["ae2_provider"], sub="Autocrafting"),
    Q("ae2_crafting_terminal", "Crafting terminal", "ae2:crafting_terminal",
      ["A terminal with a built-in crafting grid and autocrafting requests. Request an item, and the network crafts it for you."],
      (1, 1), [item("ae2:crafting_terminal")], deps=["ae2_molecular"], rewards=[xp(3)], sub="Request and relax"),
])

# ---------------------------------------------------------------- write
def quest_json(q, group):
    j = {
        "display": {
            "icon": {"type": "heracles:item", "item": q["icon"]},
            "title": q["title"],
            "subtitle": q["sub"],
            "description": q["desc"],
            "groups": {group: {"position": [q["pos"][0] * STEP, q["pos"][1] * STEP]}},
        },
        "settings": {"individual_progress": False, "showDependencyArrow": True},
        "dependencies": q["deps"],
        "tasks": {},
        "rewards": {},
    }
    for i, t in enumerate(q["tasks"], 1):
        t = dict(t)
        if t["type"] == "heracles:item":
            t = {"type": t["type"], "item": t["item"], "amount": t["amount"]}
        j["tasks"][f"task_{i}"] = t
    for i, r in enumerate(q["rewards"], 1):
        j["rewards"][f"reward_{i}"] = r
    return j

def main():
    qdir = OUT / "quests"
    if qdir.exists():
        shutil.rmtree(qdir)
    qdir.mkdir(parents=True)
    ids = set()
    total = 0
    for name, folder, quests in CHAPTERS:
        for q in quests:
            assert q["id"] not in ids, q["id"]
            ids.add(q["id"])
        for q in quests:
            for d in q["deps"]:
                assert d in ids or any(d == x["id"] for _, _, qq in CHAPTERS for x in qq), (q["id"], d)
            d = qdir / folder
            d.mkdir(exist_ok=True)
            (d / f"{q['id']}.json").write_text(json.dumps(quest_json(q, name), indent=2) + "\n", encoding="utf-8")
            total += 1
        print(f"{name}: {len(quests)} quests")
    (OUT / "groups.txt").write_text("\n".join(n for n, _, _ in CHAPTERS) + "\n", encoding="utf-8")
    print("total", total)

main()
