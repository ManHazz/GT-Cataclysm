---
navigation:
  title: "Vacuum Freezer"
  icon: gtceu:vacuum_freezer
  parent: multiblocks.md
  position: 50
item_ids:
  - gtceu:vacuum_freezer
  - gtceu:frostproof_machine_casing
---

# Vacuum Freezer

<ItemImage id="gtceu:vacuum_freezer" scale="4" />

The Vacuum Freezer cools hot ingots into normal ingots. Tooltip: Aluminium Ice Box.

## What it does

In-game description: mainly freezing Hot Ingots into regular Ingots, but it can also freeze other substances such as water. Hot ingots come out of the EBF for the harder metals.

## How to make it

<RecipeFor id="gtceu:vacuum_freezer" />

<RecipeFor id="gtceu:frostproof_machine_casing" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Vacuum Freezer | Titanium Hot Ingot (any) | Titanium Ingot | 480 | 7.2 s |
| Vacuum Freezer | Kanthal Hot Ingot (any) | Kanthal Ingot | 120 | 6.6 s |
| Vacuum Freezer | 1000 mB Oxygen | 1000 mB Liquid Oxygen | 1920 | 12 s |

<ItemGrid>
  <ItemIcon id="gtceu:titanium_ingot" />
  <ItemIcon id="gtceu:kanthal_ingot" />
  <ItemIcon id="gtceu:frostproof_machine_casing" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="structures/vacuum_freezer.nbt" />
  <BlockAnnotation x="1" y="1" z="0">Controller</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="2">Maintenance Hatch</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="2">Energy Hatch</BlockAnnotation>
  <BlockAnnotation x="0" y="2" z="1">Item Input Bus</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="0">Item Output Bus</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="0">Fluid Input Hatch</BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="0">Fluid Output Hatch</BlockAnnotation>
</GameScene>

## Tips

* Maintenance Hatch: problems appear every few hours while running and must be fixed with the tool the controller names (docs).
* The freezer's own recipe needs EV circuits and HV pumps (see the recipe above).
