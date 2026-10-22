---
navigation:
  title: "Assembly Line"
  icon: gtceu:assembly_line
  parent: multiblocks.md
  position: 70
item_ids:
  - gtceu:assembly_line
  - gtceu:assembly_line_casing
  - gtceu:assembly_line_grating
  - gtceu:assembly_line_unit
  - gtceu:basic_data_access_hatch
---

# Assembly Line

<ItemImage id="gtceu:assembly_line" scale="4" />

The Assembly Line builds advanced components. Tooltip: Not a multiblock Assembling Machine!

## What it does

In-game description: a large structure of 5 to 16 slices that makes advanced crafting components. In the preview the item input buses run along the floor and the output bus is at the end. Recipes carry a research condition: for example the LuV motor recipe needs a data stick with the research 1x_gtceu_iv_electric_motor (recipe data).

## How to make it

<RecipeFor id="gtceu:assembly_line" />

The recipe uses an IV machine hull, which is boss-gated in this pack ([Pack: boss-gated hulls](pack.md)).

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Assembly Line | Long Magnetic Samarium Rod (any), 2x Long Hsss Rod (any), 2x Hsss Ring (any), 4x Rounds Hsss (any), 64x Ruridit Fine Wire (any), 2x Niobium Titanium Single Cable, 144 mB Soldering Alloy, 250 mB Lubricant | LUV Electric Motor | 6000 | 30 s |

<ItemGrid>
  <ItemIcon id="gtceu:luv_electric_motor" />
  <ItemIcon id="gtceu:research_station" />
  <ItemIcon id="gtceu:data_bank" />
</ItemGrid>

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/assembly_line.nbt" />
  <BlockAnnotation x="0" y="2" z="0">Controller</BlockAnnotation>
  <BlockAnnotation x="1" y="2" z="0">Data Access Hatch: holds research data sticks.</BlockAnnotation>
  <BoxAnnotation min="0 0 1" max="4 1 2" color="#55aaff">Item input buses: one per slice.</BoxAnnotation>
  <BlockAnnotation x="4" y="0" z="1">Item Output Bus</BlockAnnotation>
  <BlockAnnotation x="0" y="3" z="1">Energy Hatch</BlockAnnotation>
  <BoxAnnotation min="0 1 1" max="5 2 2" color="#aaaaaa">Assembly Control Casings.</BoxAnnotation>
</GameScene>

## Tips

* The preview shows five slices; the structure takes 5 to 16 (in-game description).
* The Research Station is itself built in an Assembly Line (recipe assembly_line/research_station).
