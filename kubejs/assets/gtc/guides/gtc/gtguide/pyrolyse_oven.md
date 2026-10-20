---
navigation:
  title: "Pyrolyse Oven"
  icon: gtceu:pyrolyse_oven
  parent: multiblocks.md
  position: 30
item_ids:
  - gtceu:pyrolyse_oven
---

# Pyrolyse Oven

<ItemImage id="gtceu:pyrolyse_oven" scale="4" />

The Pyrolyse Oven is the electric Coke Oven. In-game description: it turns logs into charcoal and creosote oil, or ash and heavy oil.

## What it does

Cooks logs, coal and sugar into charcoal, coke and oils. Coil type changes its speed (see [Heating Coils](coils.md)). Some recipes add nitrogen to get a different byproduct.

## How to make it

<RecipeFor id="gtceu:pyrolyse_oven" />

Note: this recipe uses an MV machine hull, which is boss-gated in this pack ([Pack: boss-gated hulls](pack.md)).

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Pyrolyse Oven | Programmed Circuit (config 1, not consumed), 16x Logs That Burn (any) | 20x Charcoal, 4000 mB Creosote | 64 | 32 s |
| Pyrolyse Oven | Programmed Circuit (config 4, not consumed), 16x Logs That Burn (any), 1000 mB Nitrogen | 20x Charcoal, 4000 mB Charcoal Byproducts | 96 | 16 s |
| Pyrolyse Oven | Programmed Circuit (config 1, not consumed), 16x Coal Gem (any) | 16x Coke Gem, 8000 mB Creosote | 64 | 32 s |

<ItemGrid>
  <ItemIcon id="minecraft:charcoal" />
  <ItemIcon id="gtceu:coke_gem" />
  <ItemIcon id="gtceu:coke_block" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/pyrolyse_oven.nbt" />
  <BlockAnnotation x="1" y="1" z="0">Controller</BlockAnnotation>
  <BoxAnnotation min="0 0 1" max="3 3 3" color="#ff7733">Heating coils: all must match.</BoxAnnotation>
  <BlockAnnotation x="0" y="0" z="3">LV Energy Hatch (two in the preview)</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="3">Second Energy Hatch</BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="0">Item Input Bus</BlockAnnotation>
  <BlockAnnotation x="0" y="2" z="0">Fluid Input Hatch</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="0">Item Output Bus</BlockAnnotation>
  <BlockAnnotation x="2" y="2" z="0">Fluid Output Hatch</BlockAnnotation>
  <BlockAnnotation x="1" y="1" z="3">Muffler Hatch: keep one block of air in front.</BlockAnnotation>
  <BlockAnnotation x="1" y="2" z="0">Maintenance Hatch</BlockAnnotation>
</GameScene>

## Tips

* Maintenance Hatch: problems appear every few hours while running and must be fixed with the tool the controller names (docs).
* Muffler Hatch needs airspace in front of it.
