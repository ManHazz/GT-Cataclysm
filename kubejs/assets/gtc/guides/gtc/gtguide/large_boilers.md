---
navigation:
  title: "Large Boilers"
  icon: gtceu:bronze_large_boiler
  parent: multiblocks.md
  position: 60
item_ids:
  - gtceu:bronze_large_boiler
  - gtceu:steel_large_boiler
  - gtceu:titanium_large_boiler
  - gtceu:tungstensteel_large_boiler
---

# Large Boilers

<ItemImage id="gtceu:bronze_large_boiler" scale="4" />

Large Boilers make steam from fuel and water in large amounts.

## What it does

In-game description: Large Boilers generate steam from any solid fuel with a burn time, or from a diesel or semi-fluid fuel. They can be throttled back to use less fuel (efficiency is not lost). The docs give these numbers:

| Boiler | Steam | Boil up | Max temperature |
|---|---|---|---|
| Bronze | 800 mB/t | 40 s | 1074 K |
| Steel | 1800 mB/t | 90 s | 2074 K |
| Titanium | 3200 mB/t | 160 s | 3474 K |
| Tungstensteel | 6400 mB/t | 160 s | 6674 K |

## How to make it

<RecipeFor id="gtceu:bronze_large_boiler" />

<RecipeFor id="gtceu:steel_large_boiler" />

<RecipeFor id="gtceu:bronze_firebox_casing" />

Titanium and Tungstensteel boilers: use JEI (R on the item).

## What it makes and uses

Fuel in, water in, steam out. Steam feeds steam machines and turbines.

<ItemGrid>
  <ItemIcon id="gtceu:bronze_large_boiler" />
  <ItemIcon id="gtceu:steel_large_boiler" />
  <ItemIcon id="gtceu:titanium_large_boiler" />
  <ItemIcon id="gtceu:tungstensteel_large_boiler" />
  <ItemIcon id="gtceu:bronze_firebox_casing" />
  <ItemIcon id="gtceu:bronze_pipe_casing" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/large_boiler.nbt" />
  <BlockAnnotation x="1" y="1" z="0">Controller</BlockAnnotation>
  <BoxAnnotation min="0 0 0" max="3 1 2" color="#ff7733">Firebox casings (bottom layer).</BoxAnnotation>
  <BlockAnnotation x="1" y="1" z="1">Pipe casing</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="2">Fluid Input Hatch: water</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="2">Item Input Bus: fuel</BlockAnnotation>
  <BlockAnnotation x="2" y="1" z="2">Fluid Output Hatch: steam</BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="2">Muffler Hatch</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="1">Maintenance Hatch</BlockAnnotation>
</GameScene>

## Tips

* Controller tooltip: Will explode if provided Fuel with no Water.
* Muffler Hatch needs airspace in front of it.
