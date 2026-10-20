"""Generates the GuideME guide gtc:gtguide (kubejs/assets/gtc/guides/gtc/gtguide/*.md).
Run: python -I tools/gen_gtguide.py
All numeric/recipe data comes from tools/gtguide_facts.json, a snapshot dumped from a booted
GTCEu 7.5.3 server (recipe manager, coil/wire/pipe properties, machine registry). Prose is limited to
statements backed by that snapshot, the GTCEu jar lang file, or the GregTech Modern 1.20.1 docs.
Wrapper helpers: R(id) = GT recipe, craft(item) = vanilla-type crafting recipe (RecipeFor), TIERS(type), WIRE(mat)."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "kubejs/assets/gtc/guides/gtc/gtguide"
FACTS = json.loads((ROOT / "tools/gtguide_facts.json").read_text(encoding="utf-8"))
PAGES = {}   # slug -> dict
ORDER = []

# ---------------------------------------------------------------- naming
UP = {"ulv", "lv", "mv", "hv", "ev", "iv", "luv", "zpm", "uv", "uhv", "uev", "uiv", "uxv", "opv", "max", "lp", "hp", "ebf", "led", "ptfe", "pbi"}
KIND = {"ingots": "Ingot", "dusts": "Dust", "plates": "Plate", "crushed_ores": "Crushed Ore", "purified_ores": "Purified Ore",
        "refined_ores": "Refined Ore", "impure_dusts": "Impure Dust", "pure_dusts": "Pure Dust", "raw_materials": "Raw Ore",
        "nuggets": "Nugget", "gems": "Gem", "rods": "Rod", "rings": "Ring", "rotors": "Rotor", "foils": "Foil",
        "fine_wires": "Fine Wire", "storage_blocks": "Block", "small_dusts": "Small Dust", "tiny_dusts": "Tiny Dust",
        "hot_ingots": "Hot Ingot", "gears": "Gear", "ores": "Ore", "frames": "Frame"}


def words(s):
    return " ".join(w.upper() if w in UP else w.capitalize() for w in s.split("_"))


def nm(i):
    i = i.lstrip("#")
    ns, _, p = i.partition(":")
    if "/" in p:
        kind, _, mat = p.partition("/")
        if kind in KIND:
            return f"{words(mat.replace('/', '_'))} {KIND[kind]}"
    return words(p.replace("/", " ").replace(" ", "_"))


def fmt_stack(s):
    if "circuit" in s:
        return f"Programmed Circuit (config {s['circuit']}, not consumed)"
    if "fluid" in s:
        txt = f"{s['mb']} mB {nm(s['fluid'])}"
    else:
        key = s.get("item") or "#" + s["tag"]
        txt = (f"{s['n']}x " if s.get("n", 1) != 1 else "") + nm(key)
        if "tag" in s:
            txt += " (any)"
    ch = s.get("chance")
    if ch is not None:
        txt += " (not consumed)" if ch == 0 else f" ({ch:g}%)"
    return txt


def secs(t):
    s = t / 20
    return f"{s:g} s"


def R(rid):
    key = rid if ":" in rid else "gtceu:" + rid
    r = FACTS["recipes"].get(key)
    if r is None:
        sys.exit(f"missing recipe fact {key} (rebuild gtguide_facts.json)")
    return r


def recipe_table(rids, machine=True):
    rows = ["| Machine | Input | Output | EU/t | Time |", "|---|---|---|---|---|"]
    for rid in rids:
        r = R(rid)
        ins = ", ".join(fmt_stack(x) for x in r["in"] + r.get("fin", [])) or "-"
        outs = ", ".join(fmt_stack(x) for x in r["out"] + r.get("fout", [])) or "-"
        mach = "Furnace" if r["type"] == "minecraft:smelting" else words(r["type"].split(":")[1])
        eut = "-" if r.get("eut") is None else r["eut"]
        dur = "-" if r.get("dur") is None else secs(r["dur"])
        rows.append(f"| {mach} | {ins} | {outs} | {eut} | {dur} |")
    return "\n".join(rows)


def fuel_table(rids, unit="burn time (ticks)"):
    rows = [f"| Fuel | {unit.capitalize()} |", "|---|---|"]
    for rid in rids:
        r = R(rid)
        rows.append(f"| {', '.join(fmt_stack(x) for x in r['in'] + r.get('fin', []))} | {r['dur']} |")
    return "\n".join(rows)


def craft(item):
    if item not in FACTS["crafted"]:
        sys.exit(f"no crafting-table recipe fact for {item}")
    return f'<RecipeFor id="{item}" />'


def grid(ids):
    return "<ItemGrid>\n" + "\n".join(f'  <ItemIcon id="{i}" />' for i in ids) + "\n</ItemGrid>"


def links(ids):
    return "\n".join(f'* <ItemLink id="{i}" />' for i in ids)


def block_scene(block, text, extra=None, zoom=4):
    s = f'<GameScene zoom="{zoom}" interactive={{true}}>\n  <Block id="{block}" />\n'
    s += f'  <BlockAnnotation x="0" y="0" z="0">{text}</BlockAnnotation>\n'
    for e in extra or []:
        s += "  " + e + "\n"
    return s + "</GameScene>"


def struct_scene(src, anns, zoom=3):
    s = f'<GameScene zoom="{zoom}" interactive={{true}}>\n  <ImportStructure src="structures/{src}" />\n'
    for a in anns:
        s += "  " + a + "\n"
    return s + "</GameScene>"


def BA(x, y, z, text, color=None):
    c = f' color="{color}"' if color else ""
    return f'<BlockAnnotation x="{x}" y="{y}" z="{z}"{c}>{text}</BlockAnnotation>'


def BOX(mn, mx, text, color="#55aaff"):
    return f'<BoxAnnotation min="{mn}" max="{mx}" color="{color}">{text}</BoxAnnotation>'


def page(slug, title, parent, pos, icon, items, body, nav_title=None):
    assert slug not in PAGES, slug
    body = re.sub(r"\n+(## )", r"\n\n\1", body.strip()) + "\n"
    PAGES[slug] = dict(title=title, parent=parent, pos=pos, icon=icon, items=items, body=body, nav=nav_title or title)
    ORDER.append(slug)


def sec(title, *parts):
    return f"## {title}\n\n" + "\n\n".join(p.strip() for p in parts if p) + "\n"


def tips(*t):
    return "## Tips\n\n" + "\n".join(f"* {x}" for x in t) + "\n"


def top(item, intro, scale=4):
    return f'<ItemImage id="{item}" scale="{scale}" />\n\n{intro}\n'


def write_all():
    GUIDE.mkdir(parents=True, exist_ok=True)
    keep = set()
    for slug in ORDER:
        p = PAGES[slug]
        fm = ["---", "navigation:", f"  title: {json.dumps(p['nav'])}"]
        if p["icon"]:
            fm.append(f"  icon: {p['icon']}")
        if p["parent"]:
            fm.append(f"  parent: {p['parent']}")
        fm.append(f"  position: {p['pos']}")
        if p["items"]:
            fm.append("item_ids:")
            fm += [f"  - {i}" for i in p["items"]]
        fm.append("---")
        body = f"# {p['title']}\n\n" + p["body"]
        (GUIDE / f"{slug}.md").write_text("\n".join(fm) + "\n\n" + body, encoding="utf-8", newline="\n")
        keep.add(f"{slug}.md")
    for old in GUIDE.glob("*.md"):
        if old.name not in keep:
            old.unlink()
    print(f"wrote {len(ORDER)} pages to {GUIDE}")


# ---------------------------------------------------------------- data helpers (wires, pipes, generators)
VNAME = {8: "ULV", 32: "LV", 128: "MV", 512: "HV", 2048: "EV", 8192: "IV", 32768: "LuV", 131072: "ZPM", 524288: "UV", 2097152: "UHV"}


def WIRE(mat):
    w = FACTS["wires"].get(mat)
    if w is None:
        sys.exit(f"missing wire fact {mat}")
    return w


def PIPE(mat):
    p = FACTS["pipes"].get(mat)
    if p is None:
        sys.exit(f"missing pipe fact {mat}")
    return p


def wire_table(mats):
    rows = ["| Cable material | Max voltage | Max amps (1x cable) | Loss per block per amp |", "|---|---|---|---|"]
    for m in mats:
        w = WIRE(m)
        rows.append(f"| {words(m)} | {w['v']} ({VNAME.get(w['v'], '?')}) | {w['a']} | {w['loss']} |")
    return "\n".join(rows)


def pipe_table(mats):
    yn = lambda b: "yes" if b else "no"
    rows = ["| Pipe material | Max temperature | Gas | Acid | Cryogenic | Plasma |", "|---|---|---|---|---|---|"]
    for m in mats:
        p = PIPE(m)
        rows.append(f"| {words(m)} | {p['temp']} K | {yn(p['gas'])} | {yn(p['acid'])} | {yn(p['cryo'])} | {yn(p['plasma'])} |")
    return "\n".join(rows)


def gen_table(rids):
    rows = ["| Fuel | EU/t produced | Burn time (ticks) |", "|---|---|---|"]
    for rid in rids:
        r = R(rid)
        rows.append(f"| {', '.join(fmt_stack(x) for x in r['in'] + r.get('fin', []))} | {r['eut']} | {r['dur']} |")
    return "\n".join(rows)


# ================================================================ INDEX + CATEGORIES
page("index", "GregTech Visual Guide", None, 0, None, [], """
Illustrated pages for GT-Cataclysm. Every page shows what a machine does, how to craft it, what it makes and
uses, and how it is wired up in the world. Recipe numbers come from a snapshot of the running game (GTCEu 7.5.3);
rules and tooltips come from the GTCEu language file and the GregTech Modern 1.20.1 docs.

Hold **G** over an item that has a page to open it. GregTech machine recipes are not drawn as grids here: use JEI
(press R on an item for its recipes, U for its uses) for the full recipe screen.

* [Steam Age](steam.md)
* [Power](power.md)
* [Single-block machines (LV to IV)](machines.md)
* [Multiblocks](multiblocks.md)
* [Ore processing](ores.md)
* [Pack: boss-gated hulls](pack.md)
""", nav_title="GregTech Visual Guide")

page("steam", "Steam Age", "index.md", 10, "gtceu:lp_steam_solid_boiler", [], """
Steam is the first stage of GregTech. Per the GregTech Modern docs: the most important material is bronze, the
end goal is the LV machine hull, and this tier is gated by the Primitive Blast Furnace (steel).

<SubPages />
""")
page("power", "Power", "index.md", 20, "gtceu:lv_combustion", [], """
EU moves from generators, through cables and transformers, to batteries and machines. Voltage and amperage
rules decide what runs and what blows up.

<SubPages />
""")
page("machines", "Single-block machines", "index.md", 30, "gtceu:lv_assembler", [], """
Electric single-block machines from LV up. All of them follow the rules on
[Amperage and overload](amperage.md).

<SubPages />
""")
page("multiblocks", "Multiblocks", "index.md", 40, "gtceu:electric_blast_furnace", [], """
Multiblocks are built around a controller. Casings, coils, hatches and buses make up the structure.
The structure scenes on these pages were exported from the game's own multiblock previews.

<SubPages />
""")
page("ores", "Ore processing", "index.md", 50, "gtceu:crushed_iron_ore", [], """
How an ore turns into dust and ingots, using iron as the worked example.

<SubPages />
""")
page("pack", "Pack: boss-gated hulls", "index.md", 60, "gtceu:mv_machine_hull", [], """
Machine hulls from MV upward need a Cataclysm boss drop in this pack.

<SubPages />
""")

# ================================================================ STEAM AGE
page("steam_boiler", "Steam Boiler", "steam.md", 10, "gtceu:lp_steam_solid_boiler",
     ["gtceu:lp_steam_solid_boiler", "gtceu:hp_steam_solid_boiler", "gtceu:lp_steam_liquid_boiler"],
     top("gtceu:lp_steam_solid_boiler", "The Low Pressure Steam Solid Boiler burns solid fuel to turn water into steam. It is the usual first steam source.")
     + sec("What it does",
           "Solid boilers burn coal-type fuel to heat water. The GregTech Modern docs list base steam output as 6 mB/t for the Low Pressure Solid boiler and 15 mB/t for the High Pressure one. High Pressure versions unlock after steel.")
     + sec("How to make it", craft("gtceu:lp_steam_solid_boiler"), "Press R in JEI on the boiler for the same recipe with item tags expanded.")
     + sec("What it makes and uses",
           fuel_table(["steam_boiler/minecraft_coal", "steam_boiler/minecraft_charcoal", "steam_boiler/gtceu_coke_gem", "steam_boiler/gtceu_coke_block"]),
           grid(["minecraft:coal", "minecraft:charcoal", "gtceu:coke_gem", "gtceu:coke_block"]),
           "Output: steam. Input: water (the docs suggest a Primitive Pump, or a water connection from another mod).")
     + sec("How it connects", struct_scene("steam_setup.nbt", [
         BA(0, 0, 1, "Low Pressure Steam Solid Boiler: fuel and water in, steam out."),
         BA(2, 0, 1, "Bronze fluid pipes carry the steam."),
         BA(4, 0, 1, "Low Pressure Steam Macerator: uses steam while it works."),
     ], zoom=4))
     + tips("Do not pipe steam through wooden pipes: the game data marks wood and treated wood pipes as not gas-proof (tooltip: Gases may leak!).",
            "The docs warn that gas in a pipe that cannot contain it escapes and causes small explosions.",
            "Liquid boilers (for example the Low Pressure Steam Liquid Boiler) burn hot liquids instead of solid fuel; the docs give base output of 12 mB/t low pressure and 30 mB/t high pressure."))

page("steam_macerator", "Steam Macerator", "steam.md", 20, "gtceu:lp_steam_macerator",
     ["gtceu:lp_steam_macerator", "gtceu:hp_steam_macerator", "gtceu:steam_grinder"],
     top("gtceu:lp_steam_macerator", "The Low Pressure Steam Macerator crushes ores using steam instead of EU. In-game tooltip: macerating your ores without byproducts.")
     + sec("What it does",
           "It runs the same Macerator recipes as the electric machines. The docs list its steam use as 2 mB/t (low pressure) and 4 mB/t (high pressure). The Steam Grinder multiblock does the same job on up to eight recipes at once (docs).")
     + sec("How to make it", craft("gtceu:lp_steam_macerator"))
     + sec("What it makes and uses",
           recipe_table(["macerator/macerate_iron_ore_to_crushed_ore", "macerator/macerate_copper_ore_to_crushed_ore", "macerator/macerate_raw_iron_ore_to_crushed_ore"]),
           grid(["gtceu:iron_ore", "gtceu:copper_ore", "minecraft:raw_iron", "minecraft:raw_copper", "gtceu:crushed_iron_ore", "gtceu:crushed_copper_ore"]),
           "Byproduct chances in the table apply to machines that have byproduct slots; the steam macerator does not output byproducts.")
     + sec("How it connects", struct_scene("steam_setup.nbt", [
         BA(0, 0, 1, "Boiler: makes the steam."),
         BA(4, 0, 1, "Steam Macerator: feed ore into it, take crushed ore out."),
     ], zoom=4))
     + tips("Steam machines run on steam only and have no EU buffer or battery slot.",
            "Crushed ore still has more steps ahead: see [Ore processing](ores.md)."))

page("bronze", "Bronze", "steam.md", 30, "gtceu:bronze_ingot",
     ["gtceu:bronze_ingot", "gtceu:bronze_dust", "gtceu:lp_steam_alloy_smelter"],
     top("gtceu:bronze_ingot", "Bronze is the key Steam Age material: three parts copper to one part tin.")
     + sec("What it does", "Bronze plates build the boilers, hulls and pipes of the Steam Age. The docs describe the first batch as: crush the ingots to dust with a GT mortar, mix them 3:1 in a crafting grid, then smelt the dust. A steam alloy smelter makes it faster and needs no mortar.")
     + sec("How to make it", craft("gtceu:bronze_dust"),
           recipe_table(["mixer/bronze", "alloy_smelter/copper_dust_and_tin_dust_into_bronze"]),
           "Smelting bronze dust in a furnace gives a bronze ingot (furnace recipe gtceu:smelting/smelt_dust_bronze_to_ingot).")
     + sec("What it makes and uses",
           grid(["gtceu:bronze_ingot", "gtceu:bronze_dust", "gtceu:bronze_machine_casing", "gtceu:bronze_normal_fluid_pipe", "gtceu:lp_steam_solid_boiler"]),
           "Bronze is used in the [boiler](steam_boiler.md), the [pipes](fluid_pipes.md) and the [hulls](steam_hulls.md).")
     + sec("How it connects", block_scene("gtceu:lp_steam_alloy_smelter", "Low Pressure Steam Alloy Smelter: copper and tin in, bronze out. Runs on steam."))
     + tips("Crafting 3 copper dust + 1 tin dust gives 3 bronze dust; the Mixer and Alloy Smelter give 4 per batch (see tables)."))

page("fluid_pipes", "Fluid Pipes", "steam.md", 40, "gtceu:bronze_normal_fluid_pipe",
     ["gtceu:bronze_normal_fluid_pipe"],
     top("gtceu:bronze_normal_fluid_pipe", "Fluid pipes carry steam, water and every other fluid between machines.")
     + sec("What it does",
           "Each pipe block is a small tank. Pipes also have a maximum temperature and a list of fluid types they can safely contain (docs and tooltips). Pipes come in Tiny (fluid only), Small, Normal, Large and Huge sizes.")
     + sec("How to make it", craft("gtceu:bronze_normal_fluid_pipe"),
           recipe_table(["extruder/extrude_bronze_pipe"]))
     + sec("What it makes and uses", pipe_table(["wood", "treated_wood", "bronze", "steel", "stainless_steel", "titanium", "polytetrafluoroethylene"]),
           "Fluid containment hazards (docs): too-hot fluids destroy the pipe, acids and cryogenics hurt their surroundings and then explode, and gases that cannot be contained escape and cause small explosions.")
     + sec("How it connects", struct_scene("steam_setup.nbt", [
         BA(1, 0, 1, "Bronze Normal Fluid Pipe"),
         BA(3, 0, 1, "Pipes connect to adjacent machines and pipes."),
     ], zoom=4))
     + tips("Placement (docs): a pipe placed normally does not connect to anything; shift-right-click it against a machine or pipe to place it connected.",
            "Wrench a pipe to connect or disconnect a side. Shift-wrench a side to make it output-only.",
            "Fluids above 320 K or below 260 K in a pipe injure entities that touch it (docs)."))

page("steam_hulls", "Bronze Hulls and Casings", "steam.md", 50, "gtceu:bronze_machine_casing",
     ["gtceu:bronze_machine_casing", "gtceu:bronze_brick_casing", "gtceu:steam_machine_casing", "gtceu:bronze_firebox_casing"],
     top("gtceu:bronze_machine_casing", "Casings are the structural blocks of steam machines and multiblocks.")
     + sec("What it does",
           "The Bronze Machine Casing is the core of the bronze steam machines (the Steam Macerator recipe uses it). The Steam Machine Casing and Bronze Firebox Casing build the Large Bronze Boiler.")
     + sec("How to make it", craft("gtceu:bronze_machine_casing"), craft("gtceu:bronze_brick_casing"), craft("gtceu:steam_machine_casing"), craft("gtceu:bronze_firebox_casing"),
           recipe_table(["assembler/casing_bronze_bricks"]))
     + sec("What it makes and uses",
           grid(["gtceu:bronze_machine_casing", "gtceu:bronze_brick_casing", "gtceu:steam_machine_casing", "gtceu:bronze_firebox_casing", "gtceu:bronze_pipe_casing"]),
           "Used in: [Steam Macerator](steam_macerator.md), [Large Boilers](large_boilers.md).")
     + sec("How it connects", block_scene("gtceu:bronze_machine_casing", "Bronze Machine Casing")))


# ================================================================ POWER
page("voltage_tiers", "Voltage Tiers", "power.md", 10, "gtceu:lv_machine_hull",
     ["gtceu:ulv_machine_hull", "gtceu:lv_machine_hull", "gtceu:mv_machine_hull", "gtceu:hv_machine_hull", "gtceu:ev_machine_hull", "gtceu:iv_machine_hull"],
     top("gtceu:lv_machine_hull", "Every machine, cable and generator has a voltage tier. Each tier is four times the voltage of the one before.")
     + sec("What it does",
           "Voltage (V) is the size of one energy packet; amperage (A) is how many packets move at once. Voltage x amperage = EU/t, and EU/t x time = total EU (docs). Tiers in order: ULV, LV, MV, HV, EV, IV, LuV, ZPM, UV, UHV, UEV, UIV, UXV, OpV, MAX.")
     + sec("How to make it", "Each tier's machine hull is the base of every machine of that tier. LV is crafted:", craft("gtceu:lv_machine_hull"),
           "From MV upward the hull recipes are replaced in this pack: see [Pack: boss-gated hulls](pack.md).")
     + sec("What it makes and uses",
           "| Tier | Voltage | Example cable (max voltage from game data) |\n|---|---|---|\n"
           + "\n".join(f"| {t} | {v} | {words(m)} cable ({WIRE(m)['v']} V) |" for t, v, m in
                       [("ULV", 8, "lead"), ("LV", 32, "tin"), ("MV", 128, "copper"), ("HV", 512, "gold"), ("EV", 2048, "aluminium"), ("IV", 8192, "platinum")]),
           grid(["gtceu:ulv_machine_hull", "gtceu:lv_machine_hull", "gtceu:mv_machine_hull", "gtceu:hv_machine_hull", "gtceu:ev_machine_hull", "gtceu:iv_machine_hull"]))
     + sec("How it connects", block_scene("gtceu:lv_machine_hull", "LV Machine Hull: the 32 V base of every LV machine."))
     + tips("A machine fed a voltage above its tier explodes (docs). See [Amperage and overload](amperage.md).",
            "Transformers step between adjacent tiers: [Transformers and Diodes](transformers.md)."))

page("generators", "Generators", "power.md", 20, "gtceu:lv_combustion",
     ["gtceu:lv_combustion", "gtceu:lv_steam_turbine", "gtceu:lv_gas_turbine"],
     top("gtceu:lv_combustion", "Single-block generators burn liquid or gas fuel and output EU from one side.")
     + sec("What it does",
           "From LV to HV, EU comes from single-block generators. They consume liquid or gas fuel (no items), and output exactly 1 amp at their tier voltage from one marked output side (docs). The Basic Combustion Generator burns flammable liquids, the Gas Turbine burns flammable gases, and the Steam Turbine converts steam (tooltips). MV and HV versions burn more fuel per tick to reach their higher voltage (docs). At EV and above generation moves to multiblocks.")
     + sec("How to make it", craft("gtceu:lv_combustion"), craft("gtceu:lv_steam_turbine"), craft("gtceu:lv_gas_turbine"))
     + sec("What it makes and uses",
           gen_table(["combustion_generator/diesel", "gas_turbine/methane", "steam_turbine/steam"]),
           "The table shows the LV-tier fuel rate of each type from the recipe data; JEI lists every valid fuel.",
           grid(["gtceu:lv_combustion", "gtceu:lv_steam_turbine", "gtceu:lv_gas_turbine", "gtceu:mv_combustion"]))
     + sec("How it connects", block_scene("gtceu:lv_combustion", "Fuel liquid in. EU out of the marked output side as 1A at 32 V."))
     + tips("Generators cannot be placed inside a Cleanroom; it blocks the cleanroom controller (docs and tooltip).",
            "A single generator is 1A. A machine that wants more than 1A is fed by a battery buffer or several generators: see [Batteries and Buffers](batteries.md)."))

page("cables", "Cables", "power.md", 30, "gtceu:tin_single_cable",
     ["gtceu:tin_single_cable", "gtceu:copper_single_cable", "gtceu:tin_quadruple_cable"],
     top("gtceu:tin_single_cable", "Cables carry EU between generators, storage and machines. Every cable has a maximum voltage, a maximum amperage and a per-block loss.")
     + sec("What it does",
           "Cables connect on any side (toggle sides with Wire Cutters). A cable that carries too high a voltage burns up; one that carries too many amps heats up, loses its insulation and eventually burns (docs). Each block of cable an amp passes through loses some voltage. Wires can be combined into 2x, 4x, 8x and 16x versions to add up their amperage.")
     + sec("How to make it", craft("gtceu:tin_single_cable"),
           "Higher-tier cables are insulated with an Assembler and liquid rubber; EV and above add thin PVC sheets (docs).")
     + sec("What it makes and uses",
           wire_table(["lead", "tin", "copper", "annealed_copper", "gold", "aluminium", "platinum"]),
           "Superconductor wires have zero loss and need no insulation (docs). Example from the game data: Magnesium Diboride is a superconductor at "
           + str(WIRE("magnesium_diboride")["v"]) + " V with " + str(WIRE("magnesium_diboride")["loss"]) + " loss.",
           grid(["gtceu:tin_single_cable", "gtceu:tin_double_cable", "gtceu:tin_quadruple_cable", "gtceu:tin_octal_cable", "gtceu:tin_hex_cable"]))
     + sec("How it connects", struct_scene("power_line.nbt", [
         BA(1, 0, 1, "Copper cable (MV, 128 V)"),
         BA(4, 0, 1, "Quadruple tin cable (LV, 32 V, 4 amps)"),
     ], zoom=3))
     + tips("Docs example: 16A of LV sent 20 blocks down 16x tin cable arrives at 12 V (68.75% of the power lost). The same power stepped up to MV, sent 20 blocks down 4x annealed copper cable and stepped back down loses 15.6%.",
            "Loss is subtracted per amp, not multiplied, so few high-voltage amps travel farther than many low-voltage amps (docs).",
            "Never touch an uninsulated wire that carried energy: it damages you (docs)."))

page("transformers", "Transformers and Diodes", "power.md", 40, "gtceu:lv_transformer_1a",
     ["gtceu:lv_transformer_1a", "gtceu:lv_transformer_2a", "gtceu:lv_transformer_4a", "gtceu:lv_transformer_16a", "gtceu:lv_diode"],
     top("gtceu:lv_transformer_1a", "Transformers step power between two neighbouring tiers. Diodes make power flow one way and cap its amperage.")
     + sec("What it does",
           "A transformer turns 1 amp of the higher tier into 4 amps of the lower tier, or the reverse. The docs example: an LV Transformer accepts 1A MV and emits 4A LV, or accepts 4A LV and emits 1A MV. The Hi-Amp variants convert 2A to 8A and 4A to 16A, and the Power Transformer converts 16A to 64A.")
     + sec("How to make it", craft("gtceu:lv_transformer_1a"), craft("gtceu:lv_diode"))
     + sec("What it makes and uses",
           "A new transformer starts in Transform Down mode. The in-game tooltip says to use a Screwdriver to change the mode (the online docs say Soft Mallet; trust the tooltip in your game). A Diode starts at 1A; the tooltip says use a Soft Mallet to cycle its amperage.",
           grid(["gtceu:lv_transformer_1a", "gtceu:lv_transformer_2a", "gtceu:lv_transformer_4a", "gtceu:lv_transformer_16a", "gtceu:lv_diode"]),
           "Diodes can sit in the walls of a Cleanroom to bring power in (docs).")
     + sec("How it connects", struct_scene("power_line.nbt", [
         BA(3, 0, 1, "LV Transformer in Transform Down mode: 1A MV in, 4A LV out."),
     ], zoom=3))
     + tips("Transformers let a few high-voltage generators feed many low-voltage machines (docs).",
            "Diodes accept amps equal to their output setting and re-emit them at full voltage, which also helps against cable loss (docs)."))

page("batteries", "Batteries and Buffers", "power.md", 50, "gtceu:lv_battery_buffer_4x",
     ["gtceu:lv_battery_buffer_4x", "gtceu:lv_battery_buffer_8x", "gtceu:lv_battery_buffer_16x"],
     top("gtceu:lv_battery_buffer_4x", "A Battery Buffer holds batteries, smooths out power and hands out several amps from a single block.")
     + sec("What it does",
           "A Battery Buffer has 1, 4, 8 or 16 battery slots. It accepts 2 amps per contained electric item and outputs 1 amp per contained battery, charging and discharging all batteries evenly (docs). It is the main bulk storage from LV to mid EV.")
     + sec("How to make it", craft("gtceu:lv_battery_buffer_4x"))
     + sec("What it makes and uses",
           grid(["gtceu:lv_battery_buffer_4x", "gtceu:lv_battery_buffer_8x", "gtceu:lv_battery_buffer_16x"]),
           "Batteries are normally made in the Canner from a battery hull plus dust such as lithium, cadmium or sodium (docs). A battery in a machine's own battery slot charges when the machine's buffer is more than 2/3 full and discharges when it is under 1/3 (docs).")
     + sec("How it connects", block_scene("gtceu:lv_battery_buffer_4x", "Cables in on any non-output side, up to 4 amps out of the output side with four batteries."))
     + tips("The docs recommend your first EBF is fed by four LV generators or a 4x Battery Buffer.",
            "Never run a cable that carries fewer amps than the buffer can output (docs)."))

page("amperage", "Amperage and Overload", "power.md", 60, "gtceu:lv_energy_input_hatch",
     ["gtceu:lv_energy_input_hatch", "gtceu:tin_single_cable"],
     top("gtceu:lv_energy_input_hatch", "What makes machines stall, cables burn and hatches explode.")
     + sec("What it does",
           "Machines: a machine that receives an amp of power from a voltage above its tier explodes. A machine that runs out of power mid-recipe powerstalls: it stops, resets its recipe progress to 0, and waits to refill its buffer without deleting its items. A single-block machine buffers voltage x 64 EU, accepts 1 amp, and accepts 1 more when below 50% buffer while running (docs). Multiblocks run at the combined input of their energy hatches; a standard energy hatch accepts 2 amps and explodes if it receives an amp of too high a voltage (docs).")
     + sec("How to make it", craft("gtceu:lv_energy_input_hatch"))
     + sec("What it makes and uses",
           "Cables: too much voltage destroys the cable but protects the machines behind it (the cable acts as a fuse). Too many amps heat it until it burns (docs).",
           "Overclocking: a machine of a higher tier running a lower-tier recipe overclocks. The docs rule is 4x EU/t for half the time, so total energy rises 2x per overclock tier.",
           grid(["gtceu:lv_energy_input_hatch", "gtceu:tin_single_cable", "gtceu:lv_battery_buffer_4x"]))
     + sec("How it connects", struct_scene("power_line.nbt", [
         BA(0, 0, 1, "Generator: 1 amp at its own voltage."),
         BA(3, 0, 1, "Transformer: changes voltage and amperage together."),
         BA(6, 0, 1, "Machine: explodes if fed above its tier."),
     ], zoom=3))
     + tips("Safest rule from the docs: never run cables that carry fewer amps than the generators or buffers feeding them can supply.",
            "Large boilers also explode if given fuel but no water (tooltip). See [Large Boilers](large_boilers.md).",
            "A Soft Mallet right-click puts a powerstalling machine on standby without deleting its items (docs)."))

page("power_line", "Power Line Example", "power.md", 70, "gtceu:lv_transformer_1a",
     ["gtceu:mv_combustion", "gtceu:copper_single_cable", "gtceu:lv_transformer_1a", "gtceu:tin_quadruple_cable", "gtceu:lv_macerator"],
     top("gtceu:lv_transformer_1a", "A complete chain: generator, cable, transformer, cable, machine.")
     + sec("What it does",
           "An MV Combustion Generator makes 1 amp at 128 V. Copper cable (max 128 V, 1 amp, from the game data) carries it to an LV Transformer, which by default steps DOWN: 1A MV in, 4A LV out. Quadruple tin cable (max 32 V, 4 amps with 4x the single 1A rating) carries that LV power to an LV Macerator.")
     + sec("How to make it", "Craft each part from its own page:", links(["gtceu:mv_combustion", "gtceu:copper_single_cable", "gtceu:lv_transformer_1a", "gtceu:tin_quadruple_cable", "gtceu:lv_macerator"]))
     + sec("What it makes and uses", "Result: the LV macerator can draw up to 4A at 32 V from one 128 V generator, instead of needing four LV generators.")
     + sec("How it connects", struct_scene("power_line.nbt", [
         BA(0, 0, 1, "MV Combustion Generator (1A @ 128 V)"),
         BOX("1 0 1", "3 1 2", "Copper cable: MV side", "#ffaa33"),
         BA(3, 0, 1, "LV Transformer (Transform Down)"),
         BOX("4 0 1", "6 1 2", "4x tin cable: LV side, 4 amps", "#aaaaaa"),
         BA(6, 0, 1, "LV Macerator"),
     ], zoom=3))
     + tips("The scene shows the layout only. Cable sides must be connected with Wire Cutters if they did not auto-connect when placing.",
            "Check the colored output dot on the generator and transformer before connecting (docs: EU leaves a block only from its output side)."))


# ================================================================ SINGLE-BLOCK MACHINES
def tier_line(rtype):
    names = {0: "ULV", 1: "LV", 2: "MV", 3: "HV", 4: "EV", 5: "IV", 6: "LuV", 7: "ZPM", 8: "UV", 9: "UHV"}
    ms = FACTS["machine_types"][rtype]
    steam = any(i.startswith(("gtceu:lp_", "gtceu:hp_")) for i, _ in ms)
    el = sorted({t for i, t in ms if t >= 1 and not i.startswith(("gtceu:lp_", "gtceu:hp_"))})
    s = ", ".join(names.get(t, f"tier {t}") for t in el)
    return ("steam (low and high pressure), " if steam else "") + s


def mpage(slug, item, rtype, pos, title, intro, does, rids, grid_ids, tip_list, scene_text, items=(), extra=""):
    body = (top(item, intro)
            + sec("What it does", does, f"Available in these tiers: {tier_line(rtype)}. Details of the electric rules: [Amperage and overload](amperage.md).")
            + sec("How to make it", craft(item), extra)
            + sec("What it makes and uses", recipe_table(rids), grid(grid_ids))
            + sec("How it connects", block_scene(item, scene_text))
            + tips(*tip_list))
    page(slug, title, "machines.md", pos, item, [item, *items], body)


mpage("lv_macerator", "gtceu:lv_macerator", "gtceu:macerator", 10, "LV Macerator",
      "The Macerator crushes ores into crushed ore, which doubles your yield. It runs on LV power (up to 32 V).",
      "One ore becomes two crushed ore (see the first row below). Tooltips: the LV and MV Macerators work without byproducts; the HV Macerator tooltip says it works with byproducts, so the byproduct chances in the table apply from HV up.",
      ["macerator/macerate_iron_ore_to_crushed_ore", "macerator/macerate_raw_iron_ore_to_crushed_ore", "macerator/macerate_iron_crushed_ore_to_impure_dust",
       "macerator/macerate_iron_crushed_ore_to_dust", "macerator/macerate_iron_refined_ore_to_dust"],
      ["gtceu:iron_ore", "gtceu:copper_ore", "minecraft:raw_iron", "minecraft:raw_copper", "gtceu:crushed_iron_ore", "gtceu:impure_iron_dust"],
      ["Raw iron and raw copper are macerated through the tags forge:raw_materials/iron and forge:raw_materials/copper (confirmed in game).",
       "The steam version is on [Steam Macerator](steam_macerator.md). The whole chain is on [Ore processing](ores.md)."],
      "Insert ore, supply LV power.", ["gtceu:mv_macerator"])

mpage("lv_electric_furnace", "gtceu:lv_electric_furnace", "gtceu:electric_furnace", 20, "LV Electric Furnace",
      "The Electric Furnace smelts with EU instead of fuel.",
      "Runs furnace-style smelting. The steam Furnace uses the same recipe type, and the docs give its example as Bronze Dust to Bronze Ingot.",
      ["smelting/smelt_dust_bronze_to_ingot", "smelting/smelt_dust_wrought_iron_to_ingot"],
      ["gtceu:bronze_dust", "gtceu:bronze_ingot", "gtceu:wrought_iron_dust", "gtceu:wrought_iron_ingot"],
      ["Alloys that need more heat are made in the [Electric Blast Furnace](ebf.md).",
       "The table shows furnace recipes added by GTCEu (recipe ids start with gtceu:smelting/); EU/t and time are not part of those recipes."],
      "Power in on any side.")

mpage("lv_compressor", "gtceu:lv_compressor", "gtceu:compressor", 30, "LV Compressor",
      "The Compressor squeezes items into denser forms.",
      "Packs nuggets into ingots and ingots into blocks, among other things (recipes below).",
      ["compressor/compress_red_alloy_to_block", "compressor/compress_iron_nugget_to_ingot", "compressor/plant_ball_from_wheat"],
      ["gtceu:red_alloy_ingot", "gtceu:red_alloy_block", "minecraft:iron_nugget", "minecraft:iron_ingot", "gtceu:plant_ball"],
      ["The Compressor also makes Plant Balls from wheat, a fuel for boilers (it appears in the steam boiler fuel list)."],
      "Power in on any side.")

mpage("lv_extractor", "gtceu:lv_extractor", "gtceu:extractor", 40, "LV Extractor",
      "The Extractor pulls fluids and dusts out of items.",
      "Melts ingots into fluid and presses resin into raw rubber (recipes below). The steam Extractor docs example: Rubber Log to Raw Rubber Pulp.",
      ["extractor/raw_rubber_from_resin", "extractor/extract_cupronickel_ingot"],
      ["gtceu:sticky_resin", "gtceu:raw_rubber_dust", "gtceu:cupronickel_ingot"],
      ["Rubber is the insulation for LV cables: see [Cables](cables.md)."],
      "Power in on any side.")

mpage("lv_wiremill", "gtceu:lv_wiremill", "gtceu:wiremill", 50, "LV Wiremill",
      "The Wiremill draws ingots into wire.",
      "The programmed circuit in the recipe picks the wire size: config 1 gives single wire, config 3 fine wire, config 16 hex wire (recipes below).",
      ["wiremill/mill_nickel_wire", "wiremill/mill_tin_wire_fine", "wiremill/mill_copper_wire_16"],
      ["gtceu:nickel_single_wire", "gtceu:fine_tin_wire", "gtceu:copper_hex_wire", "gtceu:programmed_circuit"],
      ["Wire plus insulation becomes cable: see [Cables](cables.md)."],
      "Power in on any side.")

mpage("lv_bender", "gtceu:lv_bender", "gtceu:bender", 60, "LV Bender",
      "The Bender presses ingots and plates into plates, double plates and foils.",
      "The programmed circuit chooses the shape: config 1 plate, config 2 double plate, config 10 foil (recipes below).",
      ["bender/bend_cobalt_to_plate", "bender/bend_tin_ingot_to_double_plate", "bender/bend_bronze_ingot_to_foil"],
      ["gtceu:cobalt_plate", "gtceu:double_tin_plate", "gtceu:bronze_foil", "gtceu:programmed_circuit"],
      ["The LV Bender recipe itself needs steel plates."],
      "Power in on any side.")

mpage("lv_assembler", "gtceu:lv_assembler", "gtceu:assembler", 70, "LV Assembler",
      "The Assembler combines several items, and sometimes a fluid, into one product.",
      "It builds pistons, inductors, casings and machine hulls (recipes below).",
      ["assembler/piston_steel", "assembler/inductor", "assembler/casing_lv", "assembler/hull_lv"],
      ["minecraft:piston", "gtceu:inductor", "gtceu:lv_machine_casing", "gtceu:lv_machine_hull"],
      ["MV and higher hulls have their assembler recipes replaced in this pack: see [Pack: boss-gated hulls](pack.md).",
       "The Assembly Line is a different machine, not a bigger Assembler (tooltip): see [Assembly Line](assembly_line.md)."],
      "Power in on any side.")

mpage("lv_circuit_assembler", "gtceu:lv_circuit_assembler", "gtceu:circuit_assembler", 80, "LV Circuit Assembler",
      "The Circuit Assembler builds circuit boards, chips and circuits.",
      "Takes a board, components and wire plus a fluid (tin in these recipes) and outputs circuits (recipes below).",
      ["circuit_assembler/electronic_circuit_lv", "circuit_assembler/electronic_circuit_mv", "circuit_assembler/microprocessor_lv"],
      ["gtceu:basic_electronic_circuit", "gtceu:good_electronic_circuit", "gtceu:microchip_processor"],
      ["The LV Circuit Assembler's own crafting recipe needs MV circuits (see the recipe above)."],
      "Power in on any side.")

mpage("lv_chemical_reactor", "gtceu:lv_chemical_reactor", "gtceu:chemical_reactor", 90, "LV Chemical Reactor",
      "The Chemical Reactor makes chemicals from items and fluids.",
      "Reacts dusts and fluids into new dusts and fluids (recipes below). Some recipes need a catalyst that is not consumed, such as silver dust.",
      ["chemical_reactor/calcium_hydroxide", "chemical_reactor/sulfur_trioxide", "chemical_reactor/formaldehyde"],
      ["gtceu:calcium_hydroxide_dust", "gtceu:quicklime_dust"],
      ["The Large Chemical Reactor multiblock overclocks perfectly (4x EU/t for 1/4 the time, docs)."],
      "Power in on any side.")

mpage("lv_centrifuge", "gtceu:lv_centrifuge", "gtceu:centrifuge", 100, "LV Centrifuge",
      "The Centrifuge separates mixtures and compounds into their parts.",
      "Spins dusts apart and splits mixtures. Chances in brackets are byproduct chances (recipes below).",
      ["centrifuge/ash_separation", "centrifuge/decomposition_centrifuging__bronze", "centrifuge/centrifuge_iron_pure_dust_to_dust"],
      ["gtceu:ash_dust", "gtceu:bronze_dust", "gtceu:tin_dust", "gtceu:copper_dust", "gtceu:iron_dust"],
      ["Bronze dust can be split back into tin and copper dust."],
      "Power in on any side.")

mpage("lv_electrolyzer", "gtceu:lv_electrolyzer", "gtceu:electrolyzer", 110, "LV Electrolyzer",
      "The Electrolyzer splits compounds into elements with electricity.",
      "Breaks dusts and fluids apart (recipes below).",
      ["electrolyzer/salt_water_electrolysis", "electrolyzer/sphalerite_electrolysis", "electrolyzer/decomposition_electrolyzing_clay"],
      ["gtceu:sodium_hydroxide_dust", "gtceu:zinc_dust", "gtceu:sulfur_dust", "gtceu:aluminium_dust"],
      ["The Large Electrolysis Chamber is the multiblock version (item gtceu:large_electrolyzer)."],
      "Power in on any side.")

mpage("lv_ore_washer", "gtceu:lv_ore_washer", "gtceu:ore_washer", 120, "LV Ore Washer",
      "The Ore Washer cleans crushed ore into purified ore with water.",
      "Crushed ore plus water becomes purified ore plus byproducts. Different programmed circuits and distilled water change speed and byproducts (recipes below).",
      ["ore_washer/wash_iron_crushed_ore_to_purified_ore", "ore_washer/wash_iron_crushed_ore_to_purified_ore_distilled",
       "ore_washer/wash_iron_crushed_ore_to_purified_ore_fast", "ore_washer/wash_iron_dirty_dust_to_dust"],
      ["gtceu:crushed_iron_ore", "gtceu:purified_iron_ore", "gtceu:impure_iron_dust", "gtceu:iron_dust"],
      ["The config 1 recipe takes 20 s with byproducts; the config 2 recipe takes under half a second and gives no byproduct."],
      "Power in on any side. Needs water.")


# ================================================================ MULTIBLOCKS
def ebf_table(rids):
    rows = ["| Input | Output | Needs heat | EU/t | Time |", "|---|---|---|---|---|"]
    for rid in rids:
        r = R(rid)
        ins = ", ".join(fmt_stack(x) for x in r["in"] + r.get("fin", []))
        outs = ", ".join(fmt_stack(x) for x in r["out"] + r.get("fout", []))
        rows.append(f"| {ins} | {outs} | {r['data']['ebf_temp']} K | {r['eut']} | {secs(r['dur'])} |")
    return "\n".join(rows)


def coil_table():
    rows = ["| Coil block | Base heat capacity |", "|---|---|"]
    for c in FACTS["coils"]:
        rows.append(f"| {words(c['name'])} | {c['temp']} K |")
    return "\n".join(rows)


COILS = ["gtceu:cupronickel_coil_block", "gtceu:kanthal_coil_block", "gtceu:nichrome_coil_block", "gtceu:rtm_alloy_coil_block",
         "gtceu:hssg_coil_block", "gtceu:naquadah_coil_block", "gtceu:trinium_coil_block", "gtceu:tritanium_coil_block"]
MAINT = "Maintenance Hatch: problems appear every few hours while running and must be fixed with the tool the controller names (docs)."

page("ebf", "Electric Blast Furnace", "multiblocks.md", 10, "gtceu:electric_blast_furnace",
     ["gtceu:electric_blast_furnace", "gtceu:heatproof_machine_casing", "gtceu:lv_muffler_hatch", "gtceu:maintenance_hatch"],
     top("gtceu:electric_blast_furnace", "The Electric Blast Furnace (EBF) smelts alloys, cooks metals and refines ores. It is required for aluminium, stainless steel, titanium and naquadah alloy (in-game description).")
     + sec("What it does",
           "Each recipe lists a heat requirement. The coils set the furnace's heat capacity (controller shows Heat Capacity). Per tooltips: every voltage tier above MV adds 100 K; every 900 K above the recipe's temperature multiplies energy use by 95% before overclocking; every 1800 K above makes one overclock perfect.",
           "The docs note that most EBF recipes need MV power but the first EBF can only be built with LV energy hatches, so it takes two LV energy hatches fed by four LV generators or a 4x Battery Buffer.")
     + sec("How to make it", craft("gtceu:electric_blast_furnace"), craft("gtceu:heatproof_machine_casing"),
           "Coils: see [Heating Coils](coils.md).")
     + sec("What it makes and uses",
           ebf_table(["electric_blast_furnace/steel_from_iron", "electric_blast_furnace/blast_aluminium", "electric_blast_furnace/blast_titanium", "electric_blast_furnace/blast_tungsten_steel"]),
           grid(["gtceu:steel_ingot", "gtceu:aluminium_ingot", "gtceu:titanium_ingot", "gtceu:tungsten_steel_ingot"]),
           "Metals that leave the furnace as hot ingots go into a [Vacuum Freezer](vacuum_freezer.md).")
     + sec("How it connects", struct_scene("ebf.nbt", [
         BA(1, 0, 0, "Controller"),
         BOX("0 1 0", "3 3 3", "Heating coils: all must be the same type.", "#ff7733"),
         BA(0, 0, 2, "LV Energy Hatch (the first EBF uses two)"),
         BA(1, 0, 2, "Second LV Energy Hatch"),
         BA(0, 0, 0, "Item Input Bus"),
         BA(0, 0, 1, "Fluid Input Hatch"),
         BA(2, 0, 0, "Item Output Bus"),
         BA(2, 0, 1, "Fluid Output Hatch"),
         BA(1, 3, 1, "Muffler Hatch: needs one block of air in front of it."),
         BA(1, 3, 0, "Maintenance Hatch"),
     ], zoom=3))
     + tips("All heating coils in the structure must match (pattern error: All heating coils must be the same).",
            "Muffler Hatch must have a block of airspace in front of it or the multiblock reports Muffler Hatch is Obstructed.",
            MAINT,
            "Preview shown uses Cupronickel coils (1800 K base)."))

page("coils", "Heating Coils", "multiblocks.md", 20, "gtceu:cupronickel_coil_block", COILS,
     top("gtceu:cupronickel_coil_block", "Coils set how hot an EBF can get and how fast a Pyrolyse Oven runs.")
     + sec("What it does",
           "Heating coils come in tiers. Their Base Heat Capacity decides which EBF recipes you can run (each recipe lists a required temperature). All coils in one multiblock must be the same type.")
     + sec("How to make it", recipe_table(["assembler/coil_cupronickel", "assembler/coil_kanthal"]))
     + sec("What it makes and uses", coil_table(), grid(COILS),
           "Pyrolyse Oven (tooltip): Cupronickel coils are 25% slower; every coil after Kanthal increases speed by 50%.")
     + sec("How it connects", struct_scene("ebf.nbt", [BOX("0 1 0", "3 3 3", "Heating coils: two rings of eight.", "#ff7733")], zoom=3))
     + tips("Higher voltage adds heat: +100 K per voltage tier above MV (EBF tooltip).",
            "The coil data on this page was read from the game: Cupronickel 1800 K, Kanthal 2700 K, Nichrome 3600 K, RTM Alloy 4500 K, HSS-G 5400 K, Naquadah 7200 K, Trinium 9001 K, Tritanium 10800 K."))

page("pyrolyse_oven", "Pyrolyse Oven", "multiblocks.md", 30, "gtceu:pyrolyse_oven",
     ["gtceu:pyrolyse_oven"],
     top("gtceu:pyrolyse_oven", "The Pyrolyse Oven is the electric Coke Oven. In-game description: it turns logs into charcoal and creosote oil, or ash and heavy oil.")
     + sec("What it does", "Cooks logs, coal and sugar into charcoal, coke and oils. Coil type changes its speed (see [Heating Coils](coils.md)). Some recipes add nitrogen to get a different byproduct.")
     + sec("How to make it", craft("gtceu:pyrolyse_oven"),
           "Note: this recipe uses an MV machine hull, which is boss-gated in this pack ([Pack: boss-gated hulls](pack.md)).")
     + sec("What it makes and uses",
           recipe_table(["pyrolyse_oven/log_to_creosote", "pyrolyse_oven/log_to_charcoal_byproducts", "pyrolyse_oven/coal_to_coke_creosote"]),
           grid(["minecraft:charcoal", "gtceu:coke_gem", "gtceu:coke_block"]))
     + sec("How it connects", struct_scene("pyrolyse_oven.nbt", [
         BA(1, 1, 0, "Controller"),
         BOX("0 0 1", "3 3 3", "Heating coils: all must match.", "#ff7733"),
         BA(0, 0, 3, "LV Energy Hatch (two in the preview)"),
         BA(1, 0, 3, "Second Energy Hatch"),
         BA(0, 0, 0, "Item Input Bus"),
         BA(0, 2, 0, "Fluid Input Hatch"),
         BA(2, 0, 0, "Item Output Bus"),
         BA(2, 2, 0, "Fluid Output Hatch"),
         BA(1, 1, 3, "Muffler Hatch: keep one block of air in front."),
         BA(1, 2, 0, "Maintenance Hatch"),
     ], zoom=3))
     + tips(MAINT, "Muffler Hatch needs airspace in front of it."))

page("cleanroom", "Cleanroom", "multiblocks.md", 40, "gtceu:cleanroom",
     ["gtceu:cleanroom", "gtceu:filter_casing", "gtceu:sterilizing_filter_casing", "gtceu:plascrete", "gtceu:cleanroom_glass"],
     top("gtceu:cleanroom", "The Cleanroom keeps particles out so that cleanroom recipes can run inside it.")
     + sec("What it does",
           "Machines placed inside run cleanroom recipes (recipes show Requires Cleanroom). From the controller tooltip: size 5x5x5 up to 15x15x15; filter casings must make up the ceiling except the edges; up to 4 doors; it stays clean when a door is open; it uses 30 EU/t when dirty and 4 EU/t when clean; overclocking increases cleaning per cycle.",
           "Generators, Mufflers, Drills and Primitive Machines are too dirty and cannot go inside (tooltip).")
     + sec("How to make it", craft("gtceu:cleanroom"), craft("gtceu:filter_casing"), recipe_table(["assembler/plascrete"]),
           "The Cleanroom recipe uses an HV machine hull, which is boss-gated in this pack ([Pack: boss-gated hulls](pack.md)).")
     + sec("What it makes and uses", grid(["gtceu:cleanroom", "gtceu:filter_casing", "gtceu:sterilizing_filter_casing", "gtceu:plascrete", "gtceu:cleanroom_glass", "gtceu:hv_diode"]),
           "Filter Casing creates a particle-free environment; the Sterilizing Filter Casing creates a sterilized one (block tooltips); sterile recipes show Sterile Cleanroom.")
     + sec("How it connects", struct_scene("cleanroom.nbt", [
         BA(2, 4, 2, "Cleanroom controller (centre of the ceiling)"),
         BOX("1 4 1", "4 5 4", "Filter casings: ceiling, not the edges.", "#55ffcc"),
         BA(2, 1, 4, "Iron door (up to 4 doors)"),
         BA(3, 0, 4, "Energy hatch for the cleanroom itself"),
         BA(1, 0, 4, "Maintenance Hatch"),
         BA(2, 2, 0, "HV Diode in the wall: brings power inside."),
         BA(2, 1, 0, "Machine Hull in the wall: passes power or AE2 channels."),
         BA(1, 1, 0, "Item Passthrough Hatch"),
         BA(3, 1, 0, "Fluid Passthrough Hatch"),
     ], zoom=2))
     + tips("Send power in through Hulls or Diodes in the walls (tooltip). The docs: Diodes are the usual way.",
            "AE2 networks can pass through Hulls in the walls; the tooltip says up to 8 channels.",
            "The scene is the smallest valid layout, 5x5x5 (from the game's multiblock preview)."))

page("vacuum_freezer", "Vacuum Freezer", "multiblocks.md", 50, "gtceu:vacuum_freezer",
     ["gtceu:vacuum_freezer", "gtceu:frostproof_machine_casing"],
     top("gtceu:vacuum_freezer", "The Vacuum Freezer cools hot ingots into normal ingots. Tooltip: Aluminium Ice Box.")
     + sec("What it does", "In-game description: mainly freezing Hot Ingots into regular Ingots, but it can also freeze other substances such as water. Hot ingots come out of the EBF for the harder metals.")
     + sec("How to make it", craft("gtceu:vacuum_freezer"), craft("gtceu:frostproof_machine_casing"))
     + sec("What it makes and uses",
           recipe_table(["vacuum_freezer/cool_hot_titanium_ingot", "vacuum_freezer/cool_hot_kanthal_ingot", "vacuum_freezer/liquid_oxygen"]),
           grid(["gtceu:titanium_ingot", "gtceu:kanthal_ingot", "gtceu:frostproof_machine_casing"]))
     + sec("How it connects", struct_scene("vacuum_freezer.nbt", [
         BA(1, 1, 0, "Controller"),
         BA(1, 0, 2, "Maintenance Hatch"),
         BA(2, 0, 2, "Energy Hatch"),
         BA(0, 2, 1, "Item Input Bus"),
         BA(2, 0, 0, "Item Output Bus"),
         BA(1, 0, 0, "Fluid Input Hatch"),
         BA(0, 0, 0, "Fluid Output Hatch"),
     ], zoom=4))
     + tips(MAINT, "The freezer's own recipe needs EV circuits and HV pumps (see the recipe above)."))

page("large_boilers", "Large Boilers", "multiblocks.md", 60, "gtceu:bronze_large_boiler",
     ["gtceu:bronze_large_boiler", "gtceu:steel_large_boiler", "gtceu:titanium_large_boiler", "gtceu:tungstensteel_large_boiler"],
     top("gtceu:bronze_large_boiler", "Large Boilers make steam from fuel and water in large amounts.")
     + sec("What it does",
           "In-game description: Large Boilers generate steam from any solid fuel with a burn time, or from a diesel or semi-fluid fuel. They can be throttled back to use less fuel (efficiency is not lost). The docs give these numbers:",
           "| Boiler | Steam | Boil up | Max temperature |\n|---|---|---|---|\n| Bronze | 800 mB/t | 40 s | 1074 K |\n| Steel | 1800 mB/t | 90 s | 2074 K |\n| Titanium | 3200 mB/t | 160 s | 3474 K |\n| Tungstensteel | 6400 mB/t | 160 s | 6674 K |")
     + sec("How to make it", craft("gtceu:bronze_large_boiler"), craft("gtceu:steel_large_boiler"), craft("gtceu:bronze_firebox_casing"),
           "Titanium and Tungstensteel boilers: use JEI (R on the item).")
     + sec("What it makes and uses",
           "Fuel in, water in, steam out. Steam feeds steam machines and turbines.",
           grid(["gtceu:bronze_large_boiler", "gtceu:steel_large_boiler", "gtceu:titanium_large_boiler", "gtceu:tungstensteel_large_boiler", "gtceu:bronze_firebox_casing", "gtceu:bronze_pipe_casing"]))
     + sec("How it connects", struct_scene("large_boiler.nbt", [
         BA(1, 1, 0, "Controller"),
         BOX("0 0 0", "3 1 2", "Firebox casings (bottom layer).", "#ff7733"),
         BA(1, 1, 1, "Pipe casing"),
         BA(1, 0, 2, "Fluid Input Hatch: water"),
         BA(2, 0, 2, "Item Input Bus: fuel"),
         BA(2, 1, 2, "Fluid Output Hatch: steam"),
         BA(0, 0, 2, "Muffler Hatch"),
         BA(2, 0, 1, "Maintenance Hatch"),
     ], zoom=3))
     + tips("Controller tooltip: Will explode if provided Fuel with no Water.",
            "Muffler Hatch needs airspace in front of it."))

page("assembly_line", "Assembly Line", "multiblocks.md", 70, "gtceu:assembly_line",
     ["gtceu:assembly_line", "gtceu:assembly_line_casing", "gtceu:assembly_line_grating", "gtceu:assembly_line_unit", "gtceu:basic_data_access_hatch"],
     top("gtceu:assembly_line", "The Assembly Line builds advanced components. Tooltip: Not a multiblock Assembling Machine!")
     + sec("What it does",
           "In-game description: a large structure of 5 to 16 slices that makes advanced crafting components. In the preview the item input buses run along the floor and the output bus is at the end. Recipes carry a research condition: for example the LuV motor recipe needs a data stick with the research 1x_gtceu_iv_electric_motor (recipe data).")
     + sec("How to make it", craft("gtceu:assembly_line"),
           "The recipe uses an IV machine hull, which is boss-gated in this pack ([Pack: boss-gated hulls](pack.md)).")
     + sec("What it makes and uses", recipe_table(["assembly_line/electric_motor_luv"]), grid(["gtceu:luv_electric_motor", "gtceu:research_station", "gtceu:data_bank"]))
     + sec("How it connects", struct_scene("assembly_line.nbt", [
         BA(0, 2, 0, "Controller"),
         BA(1, 2, 0, "Data Access Hatch: holds research data sticks."),
         BOX("0 0 1", "4 1 2", "Item input buses: one per slice.", "#55aaff"),
         BA(4, 0, 1, "Item Output Bus"),
         BA(0, 3, 1, "Energy Hatch"),
         BOX("0 1 1", "5 2 2", "Assembly Control Casings.", "#aaaaaa"),
     ], zoom=3))
     + tips("The preview shows five slices; the structure takes 5 to 16 (in-game description).",
            "The Research Station is itself built in an Assembly Line (recipe assembly_line/research_station)."))

page("implosion_compressor", "Implosion Compressor", "multiblocks.md", 80, "gtceu:implosion_compressor",
     ["gtceu:implosion_compressor", "gtceu:solid_machine_casing"],
     top("gtceu:implosion_compressor", "The Implosion Compressor uses explosives to turn gem dusts into gems. Tooltip: the only machine you want to go boom.")
     + sec("What it does", "Gem dust plus an explosive in, gem out. The recipes list TNT, dynamite and other explosives.")
     + sec("How to make it", craft("gtceu:implosion_compressor"), recipe_table(["assembler/casing_steel_solid"]))
     + sec("What it makes and uses",
           recipe_table(["implosion_compressor/implode_dust_diamond_tnt", "implosion_compressor/implode_dust_diamond_dynamite"]),
           grid(["minecraft:diamond", "minecraft:tnt", "gtceu:diamond_dust"]))
     + sec("How it connects", struct_scene("implosion_compressor.nbt", [
         BA(1, 1, 0, "Controller"),
         BA(2, 0, 0, "Item Input Bus: dust and explosive"),
         BA(1, 0, 0, "Item Output Bus: gems"),
         BA(2, 0, 2, "Energy Hatch"),
         BA(1, 0, 2, "Maintenance Hatch"),
         BA(0, 0, 2, "Muffler Hatch"),
     ], zoom=4))
     + tips(MAINT, "The muffler needs airspace in front of it."))


# ================================================================ ORE PROCESSING
def machine_row(blocks, notes):
    s = '<GameScene zoom="3" interactive={true}>\n'
    for i, b in enumerate(blocks):
        s += f'  <Block id="{b}" x="{i * 2}" y="0" z="0" />\n'
        s += f'  <BlockAnnotation x="{i * 2}" y="0" z="0">{notes[i]}</BlockAnnotation>\n'
    return s + "</GameScene>"


page("ore_chain", "The Ore Chain", "ores.md", 10, "gtceu:iron_ore",
     ["gtceu:iron_ore", "gtceu:crushed_iron_ore", "gtceu:purified_iron_ore", "gtceu:refined_iron_ore", "gtceu:impure_iron_dust", "gtceu:pure_iron_dust", "gtceu:iron_dust"],
     top("gtceu:iron_ore", "Ore does not go straight to a furnace in GregTech. Each stage gives a bit more output and extra byproducts. Iron is the worked example; the recipes are read from the game.")
     + sec("What it does",
           "Main path: Ore -> Macerator -> Crushed Ore -> Ore Washer -> Purified Ore -> Thermal Centrifuge -> Refined Ore -> Macerator -> Dust. You can skip stages: crushed ore can be macerated straight to impure dust, and purified ore to pure dust. Dust is then smelted or processed further.")
     + sec("How to make it", "Every stage is a single-block machine from LV up:",
           links(["gtceu:lv_macerator", "gtceu:lv_ore_washer", "gtceu:lv_thermal_centrifuge", "gtceu:lv_centrifuge"]))
     + sec("What it makes and uses",
           recipe_table(["macerator/macerate_iron_ore_to_crushed_ore", "ore_washer/wash_iron_crushed_ore_to_purified_ore",
                         "thermal_centrifuge/centrifuge_iron_purified_ore_to_refined_ore", "macerator/macerate_iron_refined_ore_to_dust"]),
           "Shortcuts and cleanup:",
           recipe_table(["macerator/macerate_iron_crushed_ore_to_impure_dust", "ore_washer/wash_iron_dirty_dust_to_dust", "macerator/macerate_iron_crushed_ore_to_dust",
                         "centrifuge/centrifuge_iron_pure_dust_to_dust", "centrifuge/centrifuge_iron_dirty_dust_to_dust"]),
           grid(["gtceu:iron_ore", "gtceu:crushed_iron_ore", "gtceu:purified_iron_ore", "gtceu:refined_iron_ore", "gtceu:impure_iron_dust", "gtceu:pure_iron_dust", "gtceu:iron_dust"]))
     + sec("How it connects", machine_row(
         ["gtceu:lv_macerator", "gtceu:lv_ore_washer", "gtceu:lv_thermal_centrifuge", "gtceu:lv_centrifuge"],
         ["1. Macerator: ore to crushed ore", "2. Ore Washer: crushed to purified ore (water)", "3. Thermal Centrifuge: purified to refined ore", "4. Centrifuge: cleans up dusts"]))
     + tips("Percentages in the output column are byproduct chances. Each stage has different byproducts for the same ore.",
            "Machine tiers differ in how many output slots they have; see [LV Macerator](lv_macerator.md) for the byproduct note."))

page("crushed_ore", "Crushed Ore", "ores.md", 20, "gtceu:crushed_iron_ore",
     ["gtceu:crushed_iron_ore", "gtceu:purified_iron_ore", "gtceu:refined_iron_ore"],
     top("gtceu:crushed_iron_ore", "Crushed ore is the first product of ore processing and has three possible next steps.")
     + sec("What it does",
           "Crushed ore can be washed to purified ore, cooked in a Thermal Centrifuge to refined ore, or macerated to impure dust. Which you pick decides your byproducts.")
     + sec("How to make it", recipe_table(["macerator/macerate_iron_ore_to_crushed_ore", "macerator/macerate_raw_iron_ore_to_crushed_ore"]),
           "Two ores per ore block or raw ore, from the table above.")
     + sec("What it makes and uses",
           recipe_table(["ore_washer/wash_iron_crushed_ore_to_purified_ore", "thermal_centrifuge/centrifuge_iron_crushed_ore_to_refined_ore", "macerator/macerate_iron_crushed_ore_to_impure_dust"]),
           grid(["gtceu:crushed_iron_ore", "gtceu:purified_iron_ore", "gtceu:refined_iron_ore", "gtceu:impure_iron_dust"]))
     + sec("How it connects", machine_row(["gtceu:lv_ore_washer", "gtceu:lv_thermal_centrifuge", "gtceu:lv_macerator"],
                                          ["Wash: purified ore", "Thermal centrifuge: refined ore", "Macerate: impure dust"]))
     + tips("See [The Ore Chain](ore_chain.md) for the full route."))

page("lv_thermal_centrifuge", "LV Thermal Centrifuge", "ores.md", 30, "gtceu:lv_thermal_centrifuge",
     ["gtceu:lv_thermal_centrifuge"],
     top("gtceu:lv_thermal_centrifuge", "The Thermal Centrifuge heats ore to turn it into refined ore. Tooltip: separating ores more precisely.")
     + sec("What it does", "Takes crushed or purified ore and outputs refined ore plus byproducts. Available in these tiers: " + tier_line("gtceu:thermal_centrifuge") + ".")
     + sec("How to make it", craft("gtceu:lv_thermal_centrifuge"))
     + sec("What it makes and uses",
           recipe_table(["thermal_centrifuge/centrifuge_iron_purified_ore_to_refined_ore", "thermal_centrifuge/centrifuge_iron_crushed_ore_to_refined_ore"]),
           grid(["gtceu:purified_iron_ore", "gtceu:refined_iron_ore", "gtceu:tin_dust"]))
     + sec("How it connects", block_scene("gtceu:lv_thermal_centrifuge", "Power in on any side."))
     + tips("Refined ore macerates to a dust with its own byproduct (table on [The Ore Chain](ore_chain.md))."))


# ================================================================ PACK: BOSS-GATED HULLS
def gate_cfgs():
    d = ROOT / "kubejs/server_scripts/gating"
    out = []
    for f in sorted(d.glob("0[1-9]_*.js")):
        t = f.read_text(encoding="utf-8")
        g = lambda k: re.search(k + r":\s*'([^']+)'", t).group(1)
        cables = re.search(r"cables:\s*\[([^\]]*)\]", t).group(1)
        out.append(dict(tier=g("tier"), boss=g("boss"), name=g("bossName"), fluid=g("fluid"),
                        cables=[c.strip().strip("'") for c in cables.split(",")], file=f.name))
    base = (d / "00_hull_gate.js").read_text(encoding="utf-8")
    meta = dict(dur=int(re.search(r"duration\((\d+)\)", base).group(1)), eut=int(re.search(r"EUt\((\d+)\)", base).group(1)),
                mb=int(re.search(r"\$\{[^}]*\} (\d+)`", base).group(1)))
    return out, meta


GATES, GMETA = gate_cfgs()
HULLS = [f"gtceu:{g['tier']}_machine_hull" for g in GATES]
BOSSES = [g["boss"] for g in GATES]

TN = {'luv': 'LuV', 'zpm': 'ZPM'}
gate_rows = ["| Hull tier | Boss | Drop (not consumed) | Cable | Fluid (288 mB) |", "|---|---|---|---|---|"]
for g in GATES:
    gate_rows.append(f"| {TN.get(g['tier'], g['tier'].upper())} | {g['name']} | {nm(g['boss'])} | {' or '.join(words(c) for c in g['cables'])} | {nm(g['fluid'])} |")
GATE_TABLE = "\n".join(gate_rows)
assert GMETA["mb"] == 288

page("boss_hulls", "Boss-Gated Hulls", "pack.md", 10, "gtceu:mv_machine_hull", HULLS + BOSSES,
     top("gtceu:mv_machine_hull", "In GT-Cataclysm every machine hull from MV up needs a drop from a Cataclysm boss. No boss drop, no hull, no machines of that tier.")
     + sec("What it does",
           "The pack removes every recipe that outputs these hulls (including the crafting-table route) and adds one Assembler recipe per hull. The boss drop sits in the recipe as a catalyst that is not consumed, so one drop unlocks that tier for good. Source: kubejs/server_scripts/gating/.",
           GATE_TABLE,
           "LV and ULV hulls are untouched.")
     + sec("How to make it", "See [The Gated Hull Recipe](hull_recipe.md).")
     + sec("What it makes and uses", grid(HULLS), grid(BOSSES),
           "Everything built from a hull follows: for example the MV Macerator, the Pyrolyse Oven (MV hull), the Cleanroom (HV hull) and the Assembly Line (IV hull) all list the hull in their recipes.")
     + sec("How it connects", block_scene("gtceu:mv_machine_hull", "MV Machine Hull: needs the Netherite Monstrosity drop."))
     + tips("Hull gates only touch the hull recipe. Casings, cables and fluids keep their normal recipes.",
            "Boss order in the pack: " + ", ".join(f"{TN.get(g['tier'], g['tier'].upper())} {g['name']}" for g in GATES) + "."))

page("hull_recipe", "The Gated Hull Recipe", "pack.md", 20, "gtceu:lv_assembler",
     ["gtceu:lv_machine_casing", "gtceu:mv_machine_casing", "gtceu:lv_assembler"],
     top("gtceu:mv_machine_casing", "How a gated hull is built in the Assembler.")
     + sec("What it does",
           f"Each gated hull recipe is an Assembler recipe: one machine casing of that tier + 2 cables of the tier's cable type, with the boss drop as a non-consumed input, plus 288 mB of the tier's plastic. It takes {GMETA['dur']} ticks ({secs(GMETA['dur'])}) at {GMETA['eut']} EU/t. The MV recipe exists once for copper cable and once for annealed copper cable.")
     + sec("How to make it", "Example (LV hull, for comparison, from the game):", recipe_table(["assembler/hull_lv"]),
           "MV hull in this pack: MV Machine Casing + 2 Copper Cable (or Annealed Copper Cable) + Monstrous Horn (not consumed) + 288 mB Polyethylene.")
     + sec("What it makes and uses", GATE_TABLE, grid(["gtceu:mv_machine_casing", "gtceu:hv_machine_casing", "gtceu:ev_machine_casing", "gtceu:iv_machine_casing", "gtceu:luv_machine_casing", "gtceu:zpm_machine_casing"]))
     + sec("How it connects", block_scene("gtceu:lv_assembler", "The hull recipe runs in an Assembler."))
     + tips(f"All gated hulls use the same numbers in the scripts: {GMETA['dur']} ticks at {GMETA['eut']} EU/t.",
            "Machine casing recipes are not touched by the gate, so casings can be stocked before the boss falls."))


if __name__ == "__main__":
    write_all()
