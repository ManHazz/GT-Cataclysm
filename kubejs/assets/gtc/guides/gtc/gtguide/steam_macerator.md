---
navigation:
  title: "Steam Macerator"
  icon: gtceu:lp_steam_macerator
  parent: steam.md
  position: 20
item_ids:
  - gtceu:lp_steam_macerator
  - gtceu:hp_steam_macerator
  - gtceu:steam_grinder
---

# Steam Macerator

<ItemImage id="gtceu:lp_steam_macerator" scale="4" />

The Low Pressure Steam Macerator crushes ores using steam instead of EU. In-game tooltip: macerating your ores without byproducts.

## What it does

It runs the same Macerator recipes as the electric machines. The docs list its steam use as 2 mB/t (low pressure) and 4 mB/t (high pressure). The Steam Grinder multiblock does the same job on up to eight recipes at once (docs).

## How to make it

<RecipeFor id="gtceu:lp_steam_macerator" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Macerator | Iron Ore | 2x Crushed Iron Ore, Nickel Dust (14%), Stone Dust (67%) | 2 | 20 s |
| Macerator | Copper Ore | 2x Crushed Copper Ore, Cobalt Dust (14%), Stone Dust (67%) | 2 | 20 s |
| Macerator | Iron Raw Ore (any) | 2x Crushed Iron Ore, Nickel Dust (14%) | 2 | 20 s |

<ItemGrid>
  <ItemIcon id="gtceu:iron_ore" />
  <ItemIcon id="gtceu:copper_ore" />
  <ItemIcon id="minecraft:raw_iron" />
  <ItemIcon id="minecraft:raw_copper" />
  <ItemIcon id="gtceu:crushed_iron_ore" />
  <ItemIcon id="gtceu:crushed_copper_ore" />
</ItemGrid>

Byproduct chances in the table apply to machines that have byproduct slots; the steam macerator does not output byproducts.

## How it connects

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="structures/steam_setup.nbt" />
  <BlockAnnotation x="0" y="0" z="1">Boiler: makes the steam.</BlockAnnotation>
  <BlockAnnotation x="4" y="0" z="1">Steam Macerator: feed ore into it, take crushed ore out.</BlockAnnotation>
</GameScene>

## Tips

* Steam machines run on steam only and have no EU buffer or battery slot.
* Crushed ore still has more steps ahead: see [Ore processing](ores.md).
