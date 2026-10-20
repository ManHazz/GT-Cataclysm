---
navigation:
  title: "Cleanroom"
  icon: gtceu:cleanroom
  parent: multiblocks.md
  position: 40
item_ids:
  - gtceu:cleanroom
  - gtceu:filter_casing
  - gtceu:sterilizing_filter_casing
  - gtceu:plascrete
  - gtceu:cleanroom_glass
---

# Cleanroom

<ItemImage id="gtceu:cleanroom" scale="4" />

The Cleanroom keeps particles out so that cleanroom recipes can run inside it.

## What it does

Machines placed inside run cleanroom recipes (recipes show Requires Cleanroom). From the controller tooltip: size 5x5x5 up to 15x15x15; filter casings must make up the ceiling except the edges; up to 4 doors; it stays clean when a door is open; it uses 30 EU/t when dirty and 4 EU/t when clean; overclocking increases cleaning per cycle.

Generators, Mufflers, Drills and Primitive Machines are too dirty and cannot go inside (tooltip).

## How to make it

<RecipeFor id="gtceu:cleanroom" />

<RecipeFor id="gtceu:filter_casing" />

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Assembler | Steel Frame (any), 6x Polyethylene Plate (any), 144 mB Concrete | 2x Plascrete | 48 | 10 s |

The Cleanroom recipe uses an HV machine hull, which is boss-gated in this pack ([Pack: boss-gated hulls](pack.md)).

## What it makes and uses

<ItemGrid>
  <ItemIcon id="gtceu:cleanroom" />
  <ItemIcon id="gtceu:filter_casing" />
  <ItemIcon id="gtceu:sterilizing_filter_casing" />
  <ItemIcon id="gtceu:plascrete" />
  <ItemIcon id="gtceu:cleanroom_glass" />
  <ItemIcon id="gtceu:hv_diode" />
</ItemGrid>

Filter Casing creates a particle-free environment; the Sterilizing Filter Casing creates a sterilized one (block tooltips); sterile recipes show Sterile Cleanroom.

## How it connects

<GameScene zoom="2" interactive={true}>
  <ImportStructure src="structures/cleanroom.nbt" />
  <BlockAnnotation x="2" y="4" z="2">Cleanroom controller (centre of the ceiling)</BlockAnnotation>
  <BoxAnnotation min="1 4 1" max="4 5 4" color="#55ffcc">Filter casings: ceiling, not the edges.</BoxAnnotation>
  <BlockAnnotation x="2" y="1" z="4">Iron door (up to 4 doors)</BlockAnnotation>
  <BlockAnnotation x="3" y="0" z="4">Energy hatch for the cleanroom itself</BlockAnnotation>
  <BlockAnnotation x="1" y="0" z="4">Maintenance Hatch</BlockAnnotation>
  <BlockAnnotation x="2" y="2" z="0">HV Diode in the wall: brings power inside.</BlockAnnotation>
  <BlockAnnotation x="2" y="1" z="0">Machine Hull in the wall: passes power or AE2 channels.</BlockAnnotation>
  <BlockAnnotation x="1" y="1" z="0">Item Passthrough Hatch</BlockAnnotation>
  <BlockAnnotation x="3" y="1" z="0">Fluid Passthrough Hatch</BlockAnnotation>
</GameScene>

## Tips

* Send power in through Hulls or Diodes in the walls (tooltip). The docs: Diodes are the usual way.
* AE2 networks can pass through Hulls in the walls; the tooltip says up to 8 channels.
* The scene is the smallest valid layout, 5x5x5 (from the game's multiblock preview).
