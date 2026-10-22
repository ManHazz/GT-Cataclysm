---
navigation:
  title: "Electric Blast Furnace"
  icon: gtceu:electric_blast_furnace
  parent: multiblocks.md
  position: 10
item_ids:
  - gtceu:electric_blast_furnace
  - gtceu:heatproof_machine_casing
  - gtceu:lv_muffler_hatch
  - gtceu:maintenance_hatch
---

# Electric Blast Furnace

<ItemImage id="gtceu:electric_blast_furnace" scale="4" />

The Electric Blast Furnace (EBF) smelts alloys, cooks metals and refines ores. It is required for aluminium, stainless steel, titanium and naquadah alloy (in-game description).

## What it does

Each recipe lists a heat requirement. The coils set the furnace's heat capacity (controller shows Heat Capacity). Per tooltips: every voltage tier above MV adds 100 K; every 900 K above the recipe's temperature multiplies energy use by 95% before overclocking; every 1800 K above makes one overclock perfect.

The docs note that most EBF recipes need MV power but the first EBF can only be built with LV energy hatches, so it takes two LV energy hatches fed by four LV generators or a 4x Battery Buffer.

## How to make it

<RecipeFor id="gtceu:electric_blast_furnace" />

<RecipeFor id="gtceu:heatproof_machine_casing" />

Coils: see [Heating Coils](coils.md).

## What it makes and uses

| Input | Output | Needs heat | EU/t | Time |
|---|---|---|---|---|
| Iron Ingot (any), 200 mB Oxygen | Steel Ingot, Ash Dust (11.11%) | 1000 K | 120 | 25 s |
| Aluminium Dust (any), Programmed Circuit (config 1, not consumed) | Aluminium Ingot | 1700 K | 120 | 44.2 s |
| Titanium Dust (any), Programmed Circuit (config 1, not consumed) | Hot Titanium Ingot | 1941 K | 480 | 75 s |
| Tungsten Steel Dust (any), Programmed Circuit (config 1, not consumed) | Hot Tungsten Steel Ingot | 3000 K | 1920 | 50 s |

<ItemGrid>
  <ItemIcon id="gtceu:steel_ingot" />
  <ItemIcon id="gtceu:aluminium_ingot" />
  <ItemIcon id="gtceu:titanium_ingot" />
  <ItemIcon id="gtceu:tungsten_steel_ingot" />
</ItemGrid>

Metals that leave the furnace as hot ingots go into a [Vacuum Freezer](vacuum_freezer.md).

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/ebf.nbt" />
  <BlockAnnotation x="1" y="0" z="0">Controller</BlockAnnotation>
  <BoxAnnotation min="0 1 0" max="3 3 3" color="#ff7733">Heating coils: all must be the same type.</BoxAnnotation>
  <BlockAnnotation x="0" y="0" z="2">LV Energy Hatch (the first EBF uses two)</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="2">Second LV Energy Hatch</BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="0">Item Input Bus</BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="1">Fluid Input Hatch</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="0">Item Output Bus</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="1">Fluid Output Hatch</BlockAnnotation>
  <BlockAnnotation x="1" y="3" z="1">Muffler Hatch: needs one block of air in front of it.</BlockAnnotation>
  <BlockAnnotation x="1" y="3" z="0">Maintenance Hatch</BlockAnnotation>
</GameScene>

## Tips

* All heating coils in the structure must match (pattern error: All heating coils must be the same).
* Muffler Hatch must have a block of airspace in front of it or the multiblock reports Muffler Hatch is Obstructed.
* Maintenance Hatch: problems appear every few hours while running and must be fixed with the tool the controller names (docs).
* Preview shown uses Cupronickel coils (1800 K base).
