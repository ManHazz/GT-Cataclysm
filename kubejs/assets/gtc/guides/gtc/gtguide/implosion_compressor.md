---
navigation:
  title: "Implosion Compressor"
  icon: gtceu:implosion_compressor
  parent: multiblocks.md
  position: 80
item_ids:
  - gtceu:implosion_compressor
  - gtceu:solid_machine_casing
---

# Implosion Compressor

<ItemImage id="gtceu:implosion_compressor" scale="4" />

The Implosion Compressor uses explosives to turn gem dusts into gems. Tooltip: the only machine you want to go boom.

## What it does

Gem dust plus an explosive in, gem out. The recipes list TNT, dynamite and other explosives.

## How to make it

<RecipeFor id="gtceu:implosion_compressor" />

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Assembler | 6x Steel Plate (any), Steel Frame (any), Programmed Circuit (config 6, not consumed) | 2x Solid Machine Casing | 16 | 2.5 s |

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Implosion Compressor | 4x Diamond Dust, 4x Tnt | 3x Diamond, Dark Ash Dust (25%) | 30 | 1 s |
| Implosion Compressor | 4x Diamond Dust, 2x Dynamite | 3x Diamond, Dark Ash Dust (25%) | 30 | 1 s |

<ItemGrid>
  <ItemIcon id="minecraft:diamond" />
  <ItemIcon id="minecraft:tnt" />
  <ItemIcon id="gtceu:diamond_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="structures/implosion_compressor.nbt" />
  <BlockAnnotation x="1" y="1" z="0">Controller</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="0">Item Input Bus: dust and explosive</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="0">Item Output Bus: gems</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="2">Energy Hatch</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="2">Maintenance Hatch</BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="2">Muffler Hatch</BlockAnnotation>
</GameScene>

## Tips

* Maintenance Hatch: problems appear every few hours while running and must be fixed with the tool the controller names (docs).
* The muffler needs airspace in front of it.
